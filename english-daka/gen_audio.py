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
import asyncio
import hashlib
import json
import re
import sys
import tempfile
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
    await edge_tts.Communicate(text, voice, rate=rate).save(str(out))


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


NON_LESSON = {"index.json", "phonics.json", "dictionary.json"}


def lesson_files(lessons_root: Path):
    """lessons/ 下的全部课程 JSON(排除索引/音素库/词典这些数据文件)"""
    return sorted(p for p in lessons_root.glob("*.json")
                  if p.name not in NON_LESSON)


def manifest_path(lessons_root: Path) -> Path:
    return lessons_root / AUDIO_DIR / "voices.json"


def phonics_fingerprint(lessons_root: Path) -> str:
    """拼接配方的指纹:音素库内容 + 停顿参数。
    库里任何一个音重做了、或者停顿改了,拼接句都得跟着重做。"""
    h = hashlib.md5(f"gap={GAP_MS},{GAP_PUNCT_MS}".encode())
    for f in sorted((lessons_root / AUDIO_DIR / "phonics").glob("*.mp3")):
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
        for qa in card["dialog"]:
            for text in [qa["q"], *qa["a"]]:
                m = SPELLED_RE.search(text)
                if m:
                    warn(card, f"{text!r} 里的 {m.group()!r} 会被 TTS 念成字母名,"
                               f"拼读要写成音标记号(如 /k/ /at/, cat.)")
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
        # 考一考的提问音频("Which one is xxx?")
        quiz_q = f"Which one is {card['word']}?"
        quiz_rel = clip_rel("q", quiz_q, lesson_id)
        tasks[quiz_rel] = ("q", quiz_q)
        if write_back:
            card["quiz_audio"] = quiz_rel
        for qa in card["dialog"]:
            q_rel = clip_rel("q", qa["q"], lesson_id)
            a_rels = [clip_rel("a", s, lesson_id) for s in qa["a"]]
            tasks[q_rel] = ("q", qa["q"])
            for s, rel in zip(qa["a"], a_rels):
                tasks[rel] = ("a", s)
            if write_back:
                qa["q_audio"] = q_rel
                qa["a_audio"] = a_rels
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


def update_index(lessons_root: Path, lesson_id: str, lesson: dict):
    """把课程登记进目录页 index.json(按日期倒序)"""
    index_file = lessons_root / "index.json"
    index = json.loads(index_file.read_text(encoding="utf-8")) \
        if index_file.exists() else {"lessons": []}
    entry = {"id": lesson_id, "title": lesson["title"],
             "words": len(lesson["cards"])}
    for k in ("num", "group", "badge", "badge_sub", "seq"):
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
    grouped = sorted([x for x in index["lessons"] if has(x, "group")],
                     key=lambda x: x.get("seq", x.get("num", 0)))
    dated = sorted([x for x in index["lessons"]
                    if not has(x, "group") and not has(x, "num")],
                   key=lambda x: x["id"], reverse=True)
    index["lessons"] = numbered + grouped + dated
    index_file.write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


async def main(lesson_path: str):
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
    update_index(lessons_root, lesson_id, lesson)
    print(f"\n完成:新生成 {made} 条,复用已有 {skipped} 条")
    print(f"目录页 index.json 已更新:{lesson_id} · {lesson['title']}")
    print(f"其中词级点读 {len(lesson['word_audio'])} 个单词")
    print(f"音频目录:{lessons_root / AUDIO_DIR}")
    print(f"已回写:{lesson_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python gen_audio.py lessons/2026-08-29.json")
        sys.exit(1)
    asyncio.run(main(sys.argv[1]))
