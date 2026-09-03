#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
课程音频预生成脚本(句级 + 词级)
================================
读取一节课的 JSON,生成三类高质量神经语音并把路径写回 JSON:
  1. 句级:每个问题(童声)、每句回答(成人女声)
  2. 词级:课程里出现的每一个单词,慢速朗读(点读用)
  3. 鼓励语:答对/答错时的反馈语音

用法:
    pip install edge-tts
    python gen_audio.py lessons/2026-08-29.json

目录约定(课程专属的按课分,全局资产进公共池):
    audio/sentences/<课程id>/q-whats-this-sign-db146c.mp3   句子,q/a 前缀区分角色
    audio/words/street.mp3                                  单词点读,跨课复用
    audio/praise/great-job.mp3                              鼓励语,全局
    audio/voices.json                                       各角色实际使用的音色清单

角色与音色的对应只在下面 ROLES 一处定义;生成时按角色查表,不手工传音色。
改了某个角色的音色后重跑任意一课:脚本对比 voices.json 发现变化,会自动
重新生成该角色名下的**所有**音频(扫全部课程),保证不会新旧音色混播。

音标记号会被拼接,不交给 TTS 读
--------------------------------
句子里写 /s/ /a/ 这类音标时,不能让 TTS 直接念——神经 TTS 发不出孤立辅音,
会把 "/s/" 读成字母名 "ess",于是 "S says /s/" 听起来是 "ess says ess",
该有的咝音根本不存在。所以遇到 /x/ 就改成拼接:
    TTS"S says" + phonics/s.mp3 + TTS", A says" + phonics/ae.mp3 + ...
纯音来自 gen_phonics.py 生成的音素库(audio/phonics/),音色与回答角色一致。
"""

import array
import random
import asyncio
import hashlib
import json
import re
import sys
import tempfile
from datetime import date
from pathlib import Path

import edge_tts

# 复用音素库脚本里的音频处理(采样率、拼接、去首尾静音)
from gen_phonics import (SR, internal_silences, mp3_to_samples,
                         samples_to_mp3, strip_edges)

# 课文里的音标记号 → 音素库 key(辅音同名,元音要转)
PHONEME_MAP = {"a": "ae", "e": "eh", "i": "ih", "o": "aa", "u": "ah",
               "ks": "x", "kw": "qu"}
PHONEME_RE = re.compile(r"/([a-zA-Z]+)/")
BEAT = "—"                       # 破折号:排版上是一拍,音频上也给一拍
PAUSE_MARKS = ",;:—"             # 会让 TTS 停一下的标点(按出现顺序对应停顿)
GAP_MS = 100                     # 音与音之间的基础停顿:靠得近才拼得成一个词
GAP_PUNCT_MS = 620               # 标点处的停顿:"/d/ /a/ /d/, dad." 里逗号那一下。
                                 # 两档要拉开到 5 倍以上,孩子才听得出"这里换了一拍"
PUNCT = ",.;:!?"                 # 断口上的标点(文字段送进 TTS 前会被摘掉)

# ---------- 音色与语速(可按试听喜好调整;改动后重跑会自动全量刷新该角色) ----------
VOICE_Q = "en-US-AnaNeural"      # 提问:儿童音色
VOICE_A = "en-US-JennyNeural"    # 回答:成人女声
RATE_SENT = "-15%"               # 句子语速
RATE_WORD = "-30%"               # 单词点读:更慢更清晰

# 角色 → (音色, 语速)。所有音频的音色都从这里查,别处不许写音色。
ROLES = {
    "q":      (VOICE_Q, RATE_SENT),   # 提问句
    "a":      (VOICE_A, RATE_SENT),   # 回答句
    "word":   (VOICE_A, RATE_WORD),   # 单词点读
    "praise": (VOICE_Q, RATE_SENT),   # 鼓励语
}

PRAISES = ["Great job!", "Well done!", "Awesome!", "Excellent!", "Perfect!",
           "Try again!", "Hmm, try again!", "You did it! Amazing!",
           "You did it! See you tomorrow!"]

AUDIO_DIR = "audio"
LEVEL_ORDER = ["K1", "K2", "K3", "S1", "S2", "S3"]   # 目录页级别切换器同序


def slug(t: str) -> str:
    return re.sub(r"[^a-z0-9']+", "-", t.lower()).replace("'", "-").strip("-")


def clip_rel(role: str, text: str, lesson_id: str = "") -> str:
    """按角色生成音频相对路径(相对 lessons/)"""
    if role in ("q", "a"):
        h = hashlib.md5(text.encode()).hexdigest()[:6]
        return f"{AUDIO_DIR}/sentences/{lesson_id}/{role}-{slug(text)[:36]}-{h}.mp3"
    if role == "word":
        return f"{AUDIO_DIR}/words/{slug(text)}.mp3"
    return f"{AUDIO_DIR}/praise/{slug(text)}.mp3"


def words_of(sentence: str):
    """拆出句中的单词(保留缩写里的撇号),统一小写"""
    return [w.lower() for w in re.findall(r"[A-Za-z']+", sentence)]


async def tts_to_file(text: str, voice: str, rate: str, out: Path):
    """合成一句写进 out。带指数退避重试 —— edge-tts 是微软的公共服务,
    连续合成上千句时会间歇性回 503(WSServerHandshakeError);
    没有重试的话一次抖动就把整课的生成打断在半路,回写出来的 JSON
    指着一堆不存在的 mp3。"""
    last = None
    for i in range(6):
        try:
            await edge_tts.Communicate(text, voice, rate=rate).save(str(out))
            return
        except Exception as e:                      # 503 / 握手失败 / 连接被掐
            last = e
            if i == 5:
                break
            await asyncio.sleep(min(2 ** i, 20) + random.random())
    raise last


async def tts_samples(text: str, voice: str, rate: str) -> array.array:
    """合成一段文字并返回去掉首尾静音的采样"""
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tf:
        tmp = Path(tf.name)
    await tts_to_file(text, voice, rate, tmp)
    s = strip_edges(mp3_to_samples(tmp))
    tmp.unlink()
    return s


def peak(s: array.array) -> int:
    return max((abs(x) for x in s), default=0)


async def stretch_beat(text: str, voice: str, rate: str, out: Path):
    """破折号那一拍:整句只渲染一次,再把 TTS 自带的那处停顿撑到 GAP_PUNCT_MS。

    不能把句子拆成两段分别合成——孤立的片段会被 TTS 当字母名念("an?"→"N",
    和 "C-at"→"Seattle" 同一类坑)。整句渲染发音才是对的,所以只动静音长度。
    TTS 的句内停顿硬上限约 300ms,靠标点本身撑不开。
    """
    s = strip_edges(await tts_samples(text, voice, rate))
    sil = internal_silences(s, min_ms=120)          # 只认真正的语气停顿
    if not sil:
        print(f"⚠ {text!r} 里没找到可以撑长的停顿,破折号按普通标点处理")
        samples_to_mp3(s, out)
        return
    # 文本里第 k 个停顿标点 ↔ 音频里第 k 段静音;破折号是第几个就撑第几段
    marks = [c for c in text if c in PAUSE_MARKS]
    idx = min(marks.index(BEAT) if BEAT in marks else len(sil) - 1, len(sil) - 1)
    a, b = sil[idx]
    gap = array.array("h", [0] * (GAP_PUNCT_MS * SR // 1000))
    merged = array.array("h", s[:a])
    merged.extend(gap)
    merged.extend(s[b:])
    samples_to_mp3(merged, out)


async def synth(text: str, voice: str, rate: str, out: Path,
                lessons_root: Path) -> bool:
    """合成一句。含 /x/ 音标时改为拼接,返回是否走了拼接路径。"""
    if BEAT in text and not PHONEME_RE.search(text):
        await stretch_beat(text, voice, rate, out)
        return True

    parts = PHONEME_RE.split(text)          # [文字, 记号, 文字, 记号, ..., 文字]
    if len(parts) == 1:                      # 没有音标 → 整句交给 TTS
        await tts_to_file(text, voice, rate, out)
        return False
    segs = [f"/{p}/" if i % 2 else p for i, p in enumerate(parts) if p]

    phonics_dir = lessons_root / AUDIO_DIR / "phonics"
    chunks, ref_peak = [], 0                # [(是否纯音, 采样, 前面的停顿ms)]
    pending = GAP_MS                        # 下一个断口该留多长

    for seg in segs:
        ph = PHONEME_RE.fullmatch(seg)
        if ph:                               # 音标记号 → 音素库纯音
            key = PHONEME_MAP.get(ph.group(1).lower(), ph.group(1).lower())
            f = phonics_dir / f"{key}.mp3"
            if not f.exists():
                raise SystemExit(f"❌ 音素库缺 {key}.mp3(记号 {seg}),"
                                 f"先跑 gen_phonics.py")
            chunks.append((True, strip_edges(mp3_to_samples(f)), pending))
            pending = GAP_MS
        else:                                # 文字段
            raw = seg.strip()
            frag = raw.strip(PUNCT + " ")    # 去掉断口处的孤立标点
            if not frag:
                # 整段只剩标点(如 "/d/, /a/"):把这个停顿记到下一个断口上
                if raw:
                    pending = GAP_PUNCT_MS
                continue
            # 逗号/句号一侧的断口停久一点:拼完三个音要停一拍再说整词,
            # 等长的停顿会让 "/d/ /a/ /d/, dad." 听成并排的四个音
            gap = GAP_PUNCT_MS if raw[0] in PUNCT else pending
            s = await tts_samples(frag, voice, rate)
            ref_peak = max(ref_peak, peak(s))
            chunks.append((False, s, gap))
            pending = GAP_PUNCT_MS if raw[-1] in PUNCT else GAP_MS

    merged = array.array("h")
    for i, (is_phon, ch, gap_ms) in enumerate(chunks):
        s = array.array("h", ch)
        if is_phon and ref_peak:             # 纯音:对齐到文字段的响度再插入
            p = peak(s)
            if p:
                g = min(3.0, ref_peak / p)
                s = array.array("h", [max(-32768, min(32767, int(x * g))) for x in s])
        if i:
            merged.extend(array.array("h", [0] * (gap_ms * SR // 1000)))
        merged.extend(s)
    samples_to_mp3(merged, out)
    return True


NON_LESSON = {"index.json", "phonics.json", "dictionary.json", "classes.json"}


def lesson_files(lessons_root: Path):
    """lessons/ 下的全部课程 JSON(排除索引/音素库/词典这些数据文件)"""
    return sorted(p for p in lessons_root.glob("*.json")
                  if p.name not in NON_LESSON)


def manifest_path(lessons_root: Path) -> Path:
    return lessons_root / AUDIO_DIR / "voices.json"


def phonics_fingerprint(lessons_root: Path) -> str:
    """拼接配方的指纹:音素库内容 + 停顿参数。
    库里任何一个音重做了、或者停顿改了,拼接句都得跟着重做。

    ⚠️ 排除 blend-*.mp3:那是「m→an→man」这类**单词**的串联音频,
    是 gen_phonics.py --blends 的产物,不参与 /x/ 句子的拼接。
    早先把它也算进指纹,结果给一节课加几个拼读面板(=多几个 blend 文件)
    就会让全站所有含 /x/ 的句子重合成一遍,白跑一趟 TTS。"""
    h = hashlib.md5(f"gap={GAP_MS},{GAP_PUNCT_MS}".encode())
    for f in sorted((lessons_root / AUDIO_DIR / "phonics").glob("*.mp3")):
        if f.name.startswith("blend-"):
            continue
        h.update(f.name.encode())
        h.update(f.read_bytes())
    return h.hexdigest()[:12]


def current_manifest(lessons_root: Path) -> dict:
    m = {r: f"{v}|{rate}" for r, (v, rate) in ROLES.items()}
    m["_phonics"] = phonics_fingerprint(lessons_root)
    return m


def changed_roles(lessons_root: Path) -> set:
    """对比 voices.json,返回音色/语速配置发生变化的角色"""
    current = current_manifest(lessons_root)
    if not manifest_path(lessons_root).exists():
        return set()                       # 首次运行,无历史可比
    stored = json.loads(manifest_path(lessons_root).read_text())
    return {r for r in ROLES if stored.get(r) != current[r]}


def phonics_changed(lessons_root: Path) -> bool:
    """音素库变了吗(变了则所有含 /x/ 的拼接句都过期)"""
    if not manifest_path(lessons_root).exists():
        return False                       # 首次运行,无历史可比
    stored = json.loads(manifest_path(lessons_root).read_text())
    if "_phonics" not in stored:
        return False                       # 老 manifest 没记指纹,不做全量重生成
    return stored["_phonics"] != phonics_fingerprint(lessons_root)


def write_manifest(lessons_root: Path):
    manifest_path(lessons_root).write_text(
        json.dumps(current_manifest(lessons_root), indent=2), encoding="utf-8")


# "C-at, cat." 这种字母+韵脚的写法会被 TTS 念成字母名("see-at",whisper 都
# 转成 "Seattle"),必须改成音标记号 "/k/ /at/, cat." 才会走拼接
SPELLED_RE = re.compile(r"\b[A-Za-z]-[a-z]{2,3}\b")
# 拼读提问里孤立的字母/韵脚,后面没标点 TTS 就会一口气念过去,孩子听不清是哪个
PHONICS_Q_RE = re.compile(r"\b(read|sound out|spell)\b", re.I)
LOOSE_LETTER_RE = re.compile(r"(?<![A-Za-z])([a-z])\s+(?=[A-Za-z])")


def lint_lesson(lesson: dict, lesson_id: str):
    """写课文时容易踩的坑,合成前先喊一声(只警告,不拦)"""
    def warn(card, msg):
        print(f"⚠ {lesson_id} · {card['word']}:{msg}")

    for card in lesson["cards"]:
        # 短文卡(lines)的句子和答句一样要过这一关;*…* 是重点词标记,先剥掉
        texts = [ln["t"].replace("*", "") for ln in card.get("lines") or []]
        for qa in card.get("dialog") or []:
            texts += [qa["q"], *qa["a"]]
        for text in texts:
            m = SPELLED_RE.search(text)
            if m:
                warn(card, f"{text!r} 里的 {m.group()!r} 会被 TTS 念成字母名,"
                           f"拼读要写成音标记号(如 /k/ /at/, cat.)")
        for qa in card.get("dialog") or []:
            if PHONICS_Q_RE.search(qa["q"]):
                loose = LOOSE_LETTER_RE.findall(qa["q"])
                if loose:
                    warn(card, f"{qa['q']!r} 里的字母 {loose} 后面没有标点,"
                               f"TTS 会一口气念完,孩子听不清"
                               f"(用破折号断开:\"How do you read: f — an?\")")


def plan_lesson(lesson: dict, lesson_id: str, tasks: dict, write_back=True):
    """把一节课需要的全部音频加入任务表;write_back 时把路径写回 lesson dict"""
    all_words = set()
    for card in lesson["cards"]:
        all_words.add(card["word"].lower())          # 整词条,如 "bus stop"
        # 短文卡:一句一条音频,角色同答句(a=Jenny)—— 整篇都是孩子要说的话,
        # 和「回答句 = 孩子要说的 = Jenny」口径一致;句里的 /r/ 也照常走拼接。
        # *…* 是渲染用的重点词标记,合成前剥掉。短文的 word 是标题,
        # 不出「Which one is My Morning Routine?」这种考一考提问
        if card.get("tag") == "passage":
            for ln in card.get("lines") or []:
                plain = ln["t"].replace("*", "")
                rel = clip_rel("a", plain, lesson_id)
                tasks[rel] = ("a", plain)
                if write_back:
                    ln["audio"] = rel
                all_words.update(words_of(plain))
        else:
            # 考一考的提问音频("Which one is xxx?")
            quiz_q = f"Which one is {card['word']}?"
            quiz_rel = clip_rel("q", quiz_q, lesson_id)
            tasks[quiz_rel] = ("q", quiz_q)
            if write_back:
                card["quiz_audio"] = quiz_rel
        for qa in card.get("dialog") or []:
            q_rel = clip_rel("q", qa["q"], lesson_id)
            a_rels = [clip_rel("a", s, lesson_id) for s in qa["a"]]
            tasks[q_rel] = ("q", qa["q"])
            for s, rel in zip(qa["a"], a_rels):
                tasks[rel] = ("a", s)
            if write_back:
                qa["q_audio"] = q_rel
                qa["a_audio"] = a_rels
            # 闯关的干扰句(build_opts.py 预造的整句选项)。
            # 第二层直接复用了本课别的答句,自带 audio,跳过不重复合成;
            # 第一层是换词造出来的新句子,要在这儿排进任务表 —— 和答句同一个
            # 角色(a=Jenny),否则三个选项里正确的那条会是另一个音色,一听就露
            for opt in (qa.get("opts") or []):
                # ⚠️ 收词要在 continue 之前:第二层干扰句自带 audio、第一层
                # 重跑时 audio 也已经填好,两种都会走 continue —— 收词写在下面
                # 就永远收不到,选项句里的词(doctor/horse/mittens…)进不了
                # word_audio,点读时静默退回浏览器 TTS,换了个音色
                all_words.update(words_of(opt["text"]))
                if opt.get("audio"): continue
                rel = clip_rel("a", opt["text"], lesson_id)
                tasks[rel] = ("a", opt["text"])
                if write_back:
                    opt["audio"] = rel
            for s in [qa["q"], *qa["a"]]:
                all_words.update(words_of(s))

    word_map = {w: clip_rel("word", w) for w in sorted(all_words)}
    praise_map = {p: clip_rel("praise", p) for p in PRAISES}
    for w, rel in word_map.items():
        tasks[rel] = ("word", w)
    for p, rel in praise_map.items():
        tasks[rel] = ("praise", p)
    if write_back:
        lesson["word_audio"] = word_map
        lesson["praise_audio"] = praise_map


def stamp_added(lesson: dict, class_date: str) -> int:
    """给这次新加的卡盖上课日期(added,目录页「按课堂复习」按它分批)。
    新卡的判据:既没有 added、也还没生成过任何问句音频 —— 刚写进 JSON 的卡
    两样都没有;老底子的卡(早于盖戳机制入库)虽然没有 added,但 q_audio
    早就回写过了,不会在老课重生成时被误盖成今天。补录昨天的课用 --date。"""
    n = 0
    for c in lesson.get("cards", []):
        if c.get("added"):
            continue
        if any(t.get("q_audio") for t in c.get("dialog", [])):
            continue
        if any(ln.get("audio") for ln in c.get("lines", [])):   # 短文卡同理
            continue
        c["added"] = class_date
        n += 1
    return n


def build_days(lessons_root: Path):
    """扫全部课程,把卡片的 added 聚合成「课堂日」汇总 —— 写进 index.json 的
    days 字段,目录页的日期选择面板直接读它,不用把 30 个课程 JSON 全拉一遍。
    没有 added 的老卡不属于任何课堂日,天然不进汇总。
    ⚠️ check_lesson.py 里有一份逐字一致的拷贝(自检不 import 本文件:
    这里 import 了 edge_tts,没装它的机器自检就跑不了),改一处要同步改另一处。"""
    days = {}
    for f in lesson_files(lessons_root):
        d = json.loads(f.read_text(encoding="utf-8"))
        for c in d.get("cards", []):
            a = c.get("added")
            if not a:
                continue
            rec = days.setdefault(a, {"date": a, "cards": 0, "lessons": []})
            rec["cards"] += 1
            if f.stem not in rec["lessons"]:
                rec["lessons"].append(f.stem)
    # 课名按日期登记在 classes.json 里,这里拼进来。
    # 为什么不写进每张卡:一节课一个名字,改错别字只改一处;卡片在课程之间搬家
    # (这个项目里发生过很多次)名字也不会跟着散;--backfill 的历史内容没有日期,
    # 自然就没有条目,不用特判
    names = load_classes(lessons_root)
    for k, rec in days.items():
        if names.get(k):
            rec["name"] = names[k]
    return [days[k] for k in sorted(days, reverse=True)]


def days_lost(old_days, new_days):
    """课堂日汇总「只增不减」自检:重建后某个日期消失、或某天卡数变少,通常是
    课程 JSON 被批量重写时把卡片的 added 字段冲掉了(K1 全套导入 11235d6 出过
    一次:K2 卡的 added 整批丢失,days 被清空,「按课堂复习」失去数据源)。
    返回丢失明细;合法的减少(删卡、清误盖的戳)用 --allow-days-shrink 显式放行。
    ⚠️ check_lesson.py 里有一份逐字一致的拷贝,改一处要同步改另一处。"""
    old = {d["date"]: d["cards"] for d in old_days}
    new = {d["date"]: d["cards"] for d in new_days}
    return [f"{k}: {old[k]} 张 → {new.get(k, 0)} 张"
            for k in sorted(old) if new.get(k, 0) < old[k]]


def classes_path(lessons_root: Path) -> Path:
    return lessons_root / "classes.json"


def load_classes(lessons_root: Path) -> dict:
    f = classes_path(lessons_root)
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}


def save_class_name(lessons_root: Path, date: str, name: str):
    """给某一天的课起个名字。日期是这节课的身份,名字是给人看的标签"""
    f = classes_path(lessons_root)
    data = load_classes(lessons_root)
    data[date] = name
    f.write_text(json.dumps(dict(sorted(data.items(), reverse=True)),
                            ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_index(lessons_root: Path, lesson_id: str, lesson: dict,
                 allow_days_shrink: bool = False):
    """把课程登记进目录页 index.json(按日期倒序)"""
    index_file = lessons_root / "index.json"
    index = json.loads(index_file.read_text(encoding="utf-8")) \
        if index_file.exists() else {"lessons": []}
    entry = {"id": lesson_id, "title": lesson["title"],
             "words": len(lesson["cards"])}
    # cover 是课程 JSON 顶层字段,必须在这儿带上 —— 只写进 index.json
    # 的话,下次对这一课跑 gen_audio 就会被这个重建函数抹掉
    for k in ("num", "group", "badge", "badge_sub", "seq", "level", "cover"):
        if lesson.get(k) is not None:
            entry[k] = lesson[k]
    index["lessons"] = [x for x in index["lessons"] if x["id"] != lesson_id]
    index["lessons"].append(entry)
    # 归属由 group 决定,组内顺序由 seq 决定;没有 group 的按课号/日期排在前后
    # 未分组课号课(新课在上) → 分组课程(按 seq) → 未分组日期课(新日期在上)
    has = lambda x, k: k in x
    numbered = sorted([x for x in index["lessons"]
                       if not has(x, "group") and has(x, "num")],
                      key=lambda x: x["num"], reverse=True)
    # 级别优先(K1→K2→K3→S1→S2→S3),级内按 seq;没标 level 的老条目按 K2
    grouped = sorted([x for x in index["lessons"] if has(x, "group")],
                     key=lambda x: (LEVEL_ORDER.index(x.get("level", "K2"))
                                    if x.get("level", "K2") in LEVEL_ORDER else 99,
                                    x.get("seq", x.get("num", 0))))
    dated = sorted([x for x in index["lessons"]
                    if not has(x, "group") and not has(x, "num")],
                   key=lambda x: x["id"], reverse=True)
    index["lessons"] = numbered + grouped + dated
    # 顺带重建课堂日汇总:此刻课程文件都已回写到磁盘,扫出来的就是最新状态
    new_days = build_days(lessons_root)
    lost = days_lost(index.get("days") or [], new_days)
    if lost and not allow_days_shrink:
        print("❌ 课堂日汇总(days)重建后变少了 —— 通常是课程 JSON 被重写时"
              "把卡片的 added 冲掉了:")
        for m in lost:
            print(f"   {m}")
        print("index.json 未更新。先用 git diff 查课程 JSON、把丢失的 added 恢复;\n"
              "确实要减(删卡、清误盖的戳)就重跑并加 --allow-days-shrink。")
        sys.exit(1)
    index["days"] = new_days
    index_file.write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


async def main(lesson_path: str, class_date: str = None, class_name: str = None,
               allow_days_shrink: bool = False):
    lesson_file = Path(lesson_path)
    lesson = json.loads(lesson_file.read_text(encoding="utf-8"))
    lessons_root = lesson_file.parent
    lesson_id = lesson_file.stem

    # 清理脚手架模板的占位字段("_示例" 说明行、没填的空 image)
    for card in lesson["cards"]:
        for k in [k for k in card if k.startswith("_")]:
            del card[k]
        if card.get("image") == "":
            del card["image"]

    # 补录历史内容(--backfill)不盖课堂日戳:K1 这类"孩子早学完、现在才导入"的课,
    # 盖上今天的戳会让「按课堂复习」冒出一条"今天的课 · 几百张卡"
    stamped = 0 if class_date == "--backfill" else \
        stamp_added(lesson, class_date or date.today().isoformat())

    lint_lesson(lesson, lesson_id)

    tasks = {}                              # rel_path → (role, text)
    plan_lesson(lesson, lesson_id, tasks, write_back=True)

    # 音色配置或音素库变了 → 扫全部课程,把过期的音频一并加入重生成
    drift = changed_roles(lessons_root)
    phon_drift = phonics_changed(lessons_root)
    if drift:
        print(f"⚠ 角色音色配置有变化: {sorted(drift)},将全量刷新这些角色的音频")
    if phon_drift:
        print("⚠ 音素库有变化,将全量刷新所有含 /x/ 音标的拼接句"
              "(拼读串联音频请另跑 gen_phonics.py --blends)")
    if drift or phon_drift:
        for lp in lesson_files(lessons_root):
            if lp == lesson_file:
                continue
            other = json.loads(lp.read_text(encoding="utf-8"))
            plan_lesson(other, lp.stem, tasks, write_back=False)

    made = skipped = 0
    for rel, (role, text) in tasks.items():
        out = lessons_root / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        stale = role in drift or (phon_drift and PHONEME_RE.search(text))
        if out.exists() and not stale:
            skipped += 1
            continue
        voice, rate = ROLES[role]
        spliced = await synth(text, voice, rate, out, lessons_root)
        made += 1
        tag = "拼接" if spliced else f"{voice.split('-')[-1]:<12}{rate:>5}"
        print(f"  ✓ [{role:<6}|{tag}] {text}")

    write_manifest(lessons_root)
    lesson_file.write_text(
        json.dumps(lesson, ensure_ascii=False, indent=2), encoding="utf-8")
    # 课名要在 update_index 之前落盘 —— build_days 会读它
    if class_name:
        save_class_name(lessons_root, class_date, class_name)
        print(f"课名已登记:{class_date} → 「{class_name}」")
    update_index(lessons_root, lesson_id, lesson, allow_days_shrink)
    print(f"\n完成:新生成 {made} 条,复用已有 {skipped} 条")
    if stamped:
        print(f"新卡 {stamped} 张已盖上课日期 {class_date or date.today().isoformat()}"
              f"(补录昨天的课用 --date 改)")
    print(f"目录页 index.json 已更新:{lesson_id} · {lesson['title']}")
    print(f"其中词级点读 {len(lesson['word_audio'])} 个单词")
    print(f"音频目录:{lessons_root / AUDIO_DIR}")
    print(f"已回写:{lesson_file}")


if __name__ == "__main__":
    argv = sys.argv[1:]
    allow_days_shrink = "--allow-days-shrink" in argv
    if allow_days_shrink:
        argv.remove("--allow-days-shrink")
    class_date = None
    if "--backfill" in argv:
        argv.remove("--backfill")
        class_date = "--backfill"          # 哨兵:main 里跳过盖戳
    if "--date" in argv:
        i = argv.index("--date")
        class_date = argv[i + 1] if i + 1 < len(argv) else ""
        del argv[i:i + 2]
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", class_date):
            print("--date 要求 YYYY-MM-DD,例如 --date 2026-08-30")
            sys.exit(1)
    class_name = None
    if "--class" in argv:
        i = argv.index("--class")
        class_name = argv[i + 1].strip() if i + 1 < len(argv) else ""
        del argv[i:i + 2]
        if not class_name:
            print("--class 后面要跟课名,例如 --class \"T4L2 动物 · 宠物\"")
            sys.exit(1)
        if not class_date or class_date == "--backfill":
            print("--class 得配 --date 一起用:课名是挂在某一天的课上的\n"
                  "  例: python gen_audio.py lessons/k2-zoo.json "
                  "--date 2026-09-05 --class \"T4L2 动物 · 宠物\"")
            sys.exit(1)
    if len(argv) != 1:
        print("用法: python gen_audio.py lessons/x.json "
              "[--date 2026-08-30 [--class \"课名\"] | --backfill] "
              "[--allow-days-shrink]")
        sys.exit(1)
    asyncio.run(main(argv[0], class_date, class_name, allow_days_shrink))
