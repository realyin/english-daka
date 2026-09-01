#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
课程自检
========
把「做课时容易踩、但要到孩子面前才发现」的坑全部前移成一条命令。

    python check_lesson.py lessons/k2-letter-c.json   # 查一课
    python check_lesson.py                            # 查全部 29 课
    python check_lesson.py --fix-index                # 顺带核对 index.json

分两档：
  ❌ 错误  —— 会让课直接坏掉（考一考整栏消失、点下去是哑的、音频念错）
  ⚠ 警告  —— 不致命但违反约定（同课 key 重复、词条像页面标题）

音频相关的检查只在跑过 gen_audio.py 之后才有意义，没跑过会自动跳过并说明。

新增检查项时请同步更新 docs/课程制作规范.md 的「自检清单」一节。
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
LESSONS = ROOT / "lessons"
NON_LESSON = {"index.json", "phonics.json", "dictionary.json"}

# ⚠️ 与 gen_audio.py / app.html / new_lesson.py 是同一张表，改一处要四处同步
PHONEME_MAP = {"a": "ae", "e": "eh", "i": "ih", "o": "aa", "u": "ah",
               "ks": "x", "kw": "qu"}
PHONEME_RE = re.compile(r"/([a-zA-Z]+)/")
# "C-at, cat." 这种写法 TTS 会念成字母名（"see-at"），必须写成音标记号
SPELLED_RE = re.compile(r"\b[A-Za-z]-[a-z]{2,3}\b")
# 词条像教材页标题而不是一个词条 —— 考一考的提问是 "Which one is <word>?"，问不出来
PAGE_TITLE_RE = re.compile(r"\b(and|more|other|sort|words?|things?|items?)\b", re.I)
SEQ_BANDS = {"字母 Letters": 100, "词族 Word Family": 200, "拼读 Phonics": 300,
             "常见词 Sight Words": 400, "主题 Topics": 500, "数学 Math": 600,
             "科学 Science": 700}
TODO = "待填"


def slug(t):
    return re.sub(r"[^a-z0-9']+", "-", t.lower()).replace("'", "-").strip("-")


def chip_pools():
    """从 app.html 读出闯关的干扰项词池，用来检查 key 有没有同步进去"""
    app = (ROOT / "app.html").read_text(encoding="utf-8")
    pools = {}
    for name in ("PHONEME_CHIPS", "RIME_CHIPS", "COLOR_CHIPS", "NUM_CHIPS",
                 "LETTER_CHIPS", "SHAPE_CHIPS"):
        m = re.search(rf"const {name}\s*=\s*\[(.*?)\]", app, re.S)
        pools[name] = set(re.findall(r'"([^"]+)"', m.group(1))) if m else set()
    return pools


def blendable(word):
    """这个词能不能自动生成拼读面板。复用 new_lesson.phonics_block，
       免得两处各写一份「c 的音是 k」这类映射"""
    import importlib.util
    global _NL
    if "_NL" not in globals():
        spec = importlib.util.spec_from_file_location("_nl", ROOT / "new_lesson.py")
        _NL = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_NL)
    return _NL.phonics_block(word, _NL.load_phonics()) is not None


def chip_family(k, pools):
    """复刻 app.html 的 chipFamily()：这个 key 属于哪个闭合词池，不属于就返回 None"""
    if PHONEME_RE.fullmatch(k):
        return pools["RIME_CHIPS"] if len(k) > 3 else pools["PHONEME_CHIPS"]
    for name in ("COLOR_CHIPS", "NUM_CHIPS", "LETTER_CHIPS", "SHAPE_CHIPS"):
        if k in pools[name]:
            return pools[name]
    return None


class Report:
    def __init__(self, lesson_id):
        self.id, self.err, self.warn = lesson_id, [], []

    def e(self, where, msg):
        self.err.append(f"{where}: {msg}")

    def w(self, where, msg):
        self.warn.append(f"{where}: {msg}")

    def show(self):
        if not self.err and not self.warn:
            print(f"✓ {self.id}")
            return True
        print(f"{'✗' if self.err else '⚠'} {self.id}")
        for m in self.err:
            print(f"    ❌ {m}")
        for m in self.warn:
            print(f"    ⚠  {m}")
        return not self.err


# ------------------------------------------------------------------ 检查项

def check_lesson(path: Path, pools, lib, audio_ready=None) -> Report:
    d = json.loads(path.read_text(encoding="utf-8"))
    r = Report(path.name)
    cards = d.get("cards") or []

    # ---- 顶层
    lv = d.get("level")
    if not lv:
        r.e("顶层", "缺 level(K1/K2/…)—— 目录页按它分级,混合复习按它给新卡排队；"
                    "老课回填 K2,新课由 new_lesson.py --level 写入")
    elif lv not in ("K1", "K2", "K3", "S1", "S2", "S3"):
        r.w("顶层", f"level「{lv}」不在已知级别表里(K1/K2/K3/S1/S2/S3)")
    for k in ("seq", "group", "badge", "title", "cards"):
        if k not in d:
            r.e("顶层", f"缺字段 {k}（目录页靠 seq/group/badge 分组和排序）")
    if "num" in d or "date" in d:
        r.e("顶层", "还在用 num/date —— 现役课程一律 seq/group/badge，"
                    "用 num 会掉进目录页的「未分组」分支，进不了任何组")
    grp = d.get("group")
    if grp and grp in SEQ_BANDS:
        band = SEQ_BANDS[grp]
        if not (band < d.get("seq", 0) < band + 100):
            r.e("顶层", f"seq={d.get('seq')} 不在「{grp}」的 {band}xx 段里")
    elif grp:
        r.w("顶层", f"分组「{grp}」不在已知段位表里，目录页排序会不确定")
    if "word_audio" in d and not any(d["word_audio"].values()):
        r.w("顶层", "word_audio 是空的 —— 这个字段由 gen_audio.py 回写，不要手写")

    # ---- 逐卡
    seen_key, ask_key = {}, {}
    for c in cards:
        w = c.get("word", "?")
        where = f"卡「{w}」"
        for k in ("word", "cn", "tag", "dialog"):
            if not c.get(k):
                r.e(where, f"缺 {k}")
        if c.get("cn") == TODO or c.get("word") == TODO:
            r.e(where, f"还有没填的「{TODO}」")

        # sight word 徽章只属于「标题宣称的那几个常见词」。
        # 例词卡(box/cow/piano 这类普通名词)标 sight word,学一学的徽章就在
        # 说谎 —— 曾经 20 张例词卡全标错。例词一律 tag:word
        if c.get("tag") == "sight word" and "Sight Words" in (d.get("title") or ""):
            claimed = [x.strip().lower() for x in d["title"].split("·")[1].split("/")]
            if w.lower() not in claimed:
                r.w(where, f"tag 是 sight word,但「{w}」不在标题宣称的词里 —— "
                           f"例词卡应当 tag:word,常见词徽章只给虚词卡")

        # 一卡一词。只报「真聚合卡」:多问、多个不同答案、还共用一张卡片图 ——
        # 那是一页四格塞进一张卡的形状,该用 split_panels.py 拆开。
        # 单问的算式卡("two and three" 讲 2+3=5)是一整幅场景、只问一个和,
        # 名字里带 and 不代表它该拆,对它报警只是噪音
        dlg = c.get("dialog") or []
        keys = {" ".join(t.get("key") or []) for t in dlg}
        aggregate = len(dlg) > 1 and len(keys) > 1 and not any(t.get("image") for t in dlg)
        if PAGE_TITLE_RE.search(w) and not w.startswith("-") and aggregate:
            r.w(where, f"word 像教材页标题、而且是「{len(dlg)} 问共用一张卡片图」的聚合卡 —— "
                       f"考一考问的是「Which one is {w}?」，这么问答不出来。"
                       f"用 split_panels.py 按主体切开，拆成一卡一词")

        # 上课日期戳(added):按课堂复习的分批依据,由 gen_audio.py 盖,格式必须
        # 是 YYYY-MM-DD —— 目录页按字典序倒排日期,格式歪了排序和"今天/昨天"
        # 的判断都会错。没有这个字段不报:老底子的卡(早于盖戳机制)就没有
        if c.get("added") is not None and \
                not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(c["added"])):
            r.e(where, f"added「{c['added']}」不是 YYYY-MM-DD —— "
                       f"课堂日列表按它排序,格式错了整批都找不到")

        # 考一考要的画面
        if not (c.get("image") or c.get("eq") or c.get("emoji")):
            r.w(where, "既没有 image 也没有 eq/emoji —— 学一学没画面，"
                       "考一考也用不上这张卡")
        img = c.get("image")
        if img and not (LESSONS / img).exists():
            r.e(where, f"图片不存在：{img}")

        # collage 必须显式声明（app.html 的 isCollage 只认这个字段）
        if c.get("collage") and c.get("quiz") is not False:
            r.w(where, "标了 collage:true 却没有 quiz:false —— "
                       "拼图画着好几样东西，两种考题都出不来，建议一起标上")

        # 拼读面板该有没有。
        # 面板挂在**词**上，不挂在问法上：只要这个词能拼合（辅音+短元音+辅音，
        # 三个音都在库里），而且这一课的教学目标包含拼读（拼读组 / 词族组，
        # 或者卡片 tag 就写着 CVC），就该有面板。
        # 曾经的不齐：-at 课里 sat/fat/mat/cat 有面板，从聚合卡拆出来的 bat/hat 没有，
        # 因为它俩的问是「Can the bat fly?」而不是「How do you read」—— 但面板是
        # 教这个词怎么拼，跟问法无关。
        if (blendable(c.get("word", "")) and not c.get("phonics")
                and (grp in ("拼读 Phonics", "词族 Word Family") or c.get("tag") == "CVC")):
            r.w(where, f"「{c['word']}」是能拼合的三音词、又在教拼读的课里，"
                       f"但没有 phonics 拼读面板 —— 同一课里别的词有、它没有，看着就是漏了")

        # 拼读面板
        ph = c.get("phonics")
        if ph:
            for part in ph.get("parts", []):
                s = part.get("sound")
                if s and s not in lib:
                    r.e(where, f"拼读面板的 sound「{s}」不在 lessons/phonics.json 里，"
                               f"点下去是哑的")
            for slot in ("onset", "rime"):
                s = (ph.get(slot) or {}).get("sound")
                if s and s not in lib:
                    r.e(where, f"拼读面板 {slot} 的 sound「{s}」不在音素库里")
            ba = ph.get("blend_audio")
            if ba and audio_ready and not (LESSONS / ba).exists():
                r.e(where, f"串联音频不存在：{ba} —— "
                           f"跑 python gen_phonics.py --blends {path}")

        # ---- 逐问
        for i, t in enumerate(c.get("dialog") or []):
            qw = f"{where} 第{i+1}问"
            for k in ("q", "a", "key", "q_cn", "a_cn"):
                if not t.get(k):
                    r.e(qw, f"缺 {k}")
                    break
            else:
                if TODO in [t["q"], *t["a"], t["q_cn"], *t["a_cn"]]:
                    r.e(qw, f"还有没填的「{TODO}」")
                if len(t["a"]) != len(t["a_cn"]):
                    r.e(qw, f"a 有 {len(t['a'])} 条、a_cn 有 {len(t['a_cn'])} 条，对不上")

                # 音标只能出现在回答句
                if PHONEME_RE.search(t["q"]):
                    r.e(qw, f"提问里出现了音标记号：{t['q']!r} —— "
                            f"提问是童声(Ana)，音素库是 Jenny，一句话会混音色；"
                            f"音标只能写在回答句里")
                # 音标记号必须能映射到音素库
                for s in t["a"]:
                    for m in PHONEME_RE.finditer(s):
                        raw = m.group(1).lower()
                        key = PHONEME_MAP.get(raw, raw)
                        if key not in lib:
                            r.e(qw, f"音标 /{raw}/ 映射到「{key}」，但音素库里没有 —— "
                                    f"合成时会退回 TTS 念成字母名")
                # 字母拼读的写法
                for s in [t["q"], *t["a"]]:
                    m = SPELLED_RE.search(s)
                    if m:
                        r.e(qw, f"{s!r} 里的 {m.group()!r} 会被 TTS 念成字母名"
                                f"（\"C-at\" → \"see-at\"），要写成音标记号 "
                                f"如 \"/k/ /at/, cat.\"")

                # 记 key → 用了它的卡。放在 for k 循环外面：
                # key 可能是 ["bus","stop"] 这种多词，写在循环里会按元素数重复计。
                # ask_key 只收会进闯关的问 —— practice:false 的问既不出题，
                # 它的 key 也不该当别人的干扰项（app.html 的 askable() 同样口径）
                seen_key.setdefault(" ".join(t["key"]), set()).add(w)
                if t.get("practice") is not False:
                    ask_key.setdefault(" ".join(t["key"]), set()).add(w)

                # key
                for k in t["key"]:
                    if k != k.lower():
                        r.e(qw, f"key「{k}」不是小写")
                    if k == TODO:
                        r.e(qw, f"key 还没填")
                    # key 应当出现在答句里（音标记号除外，答句里写法可能不同）
                    if not PHONEME_RE.fullmatch(k) and \
                       not any(k.lower() in s.lower() for s in t["a"]):
                        r.w(qw, f"key「{k}」在答句里找不到 —— "
                                f"key 是孩子要说出来的那个词")
                    # 干扰项同类：key 属于某个词池就必须在池子里
                    if PHONEME_RE.fullmatch(k):
                        pool = "RIME_CHIPS" if len(k) > 3 else "PHONEME_CHIPS"
                        if k not in pools[pool]:
                            r.e(qw, f"key「{k}」不在 app.html 的 {pool} 里 —— "
                                    f"闯关会掉进普通名词池，变成「听音选名词」的送分题")

    # 一课之内 word 不许重复。
    # 同一个词拆成两张卡（-an 课里 man 曾经有「词族卡」和「生活场景卡」各一张），
    # 学一学里就是同一个词连着出现两遍，看着像 bug；正确写法是一张卡挂两问，
    # 两问各带自己的图（dialog[].image）。
    # 注：考一考不会因此出错 —— nextQuestion() 的干扰项按 word 字符串排除同词项，
    # 两张卡都叫 man 也挡得住；这一条是为了学一学的观感和「一卡一词」的约定。
    words = {}
    for c in cards:
        words.setdefault(c.get("word", "").lower(), []).append(c)
    for w, cs in words.items():
        if len(cs) > 1:
            r.w("整课", f"「{w}」有 {len(cs)} 张卡 —— 学一学里会连着出现两遍。"
                        f"合成一张卡、把问都挂上去，图不一样就写进 dialog[].image")

    # 闯关的干扰项够不够。
    # 直接量「这一题能抽到几个同类干扰项」，而不是数 key 重复了几次 ——
    # key 重复只是代理指标：recycling 里 paper 被三张卡用（纸桶 / 纸 / 报纸），
    # 实测同类候选仍有 4 个，一点没伤着；而 math-1-5 的 count / same 只有 1 个候选，
    # 会掉进 `[...cands, ...plain, ...NUM_CHIPS]` 兜底，凑出「count / same / seven」
    # 这种跨类选项 —— 孩子不用听懂，看出另外两个明显不是一类就能排除。
    plain = sorted({k for k in ask_key if not chip_family(k, pools)})
    for k, ws in sorted(ask_key.items()):
        cands = [x for x in (chip_family(k, pools) or plain) if x != k]
        if len(cands) < 2:
            r.w("整课", f"「{k}」（{sorted(ws)}）只有 {len(cands)} 个同类干扰项，"
                        f"闯关会掺进数字凑数，凑出的选项可能本身也说得通 —— "
                        f"要么补同类词，要么给这一问加 \"practice\": false "
                        f"（学一学照常教，只是不进闯关）")

    # 考一考可用图
    pics = quiz_pics(cards, audio_ready)
    if len(pics) < 2:
        r.w("整课", f"考一考可用图只有 {len(pics)} 张（<2 会整栏隐藏）"
                    f"{'' if audio_ready else '；音频还没生成，这个数会偏低'}")

    # 音频
    if audio_ready:
        for c in cards:
            for i, t in enumerate(c.get("dialog") or []):
                if not t.get("q_audio"):
                    r.e(f"卡「{c.get('word')}」第{i+1}问", "没有 q_audio，跑 gen_audio.py")
                if len(t.get("a_audio") or []) != len(t.get("a") or []):
                    r.e(f"卡「{c.get('word')}」第{i+1}问", "a_audio 条数和 a 对不上")
        for k in {kk for c in cards for t in c.get("dialog", []) for kk in t["key"]}:
            m = PHONEME_RE.fullmatch(k)
            f = (LESSONS / "audio" / "phonics" /
                 f"{PHONEME_MAP.get(m.group(1), m.group(1))}.mp3") if m else \
                (LESSONS / "audio" / "words" / f"{slug(k)}.mp3")
            if not f.exists():
                r.e("整课", f"闯关选项「{k}」没有点读音频（{f.relative_to(LESSONS)}）—— "
                            f"孩子还不认字，选项念不出来就等于让他认读")
    return r


QUIZ_FORMULA = re.compile(
    r"^(it's|this is|it is)\s+(sight word|key word|letter|number)\b|\bbegins with\b"
    r"|\bends with\b|\bmakes the sound\b|belong to|family\.?$", re.I)


def quiz_pics(cards, audio_ready):
    """复刻 app.html 的 quizPics()：这一课能出多少张不同的图当选项"""
    pics = []
    for c in cards:
        coll = bool(c.get("collage"))
        if c.get("quiz") is not False and (c.get("image") or c.get("eq") or c.get("emoji")) \
                and not coll:
            pics.append(c.get("image") or c.get("eq") or c.get("emoji"))
        for t in c.get("dialog") or []:
            img = t.get("image") or (c.get("image")
                                     if len(c.get("dialog") or []) == 1 and not coll else None)
            if not img:
                continue
            aa = t.get("a_audio")
            if audio_ready and not aa:
                continue
            ok = any((not audio_ready or aa[i]) and not QUIZ_FORMULA.search(s)
                     for i, s in enumerate(t.get("a") or []))
            if ok:
                pics.append(img)
    seen, out = set(), []
    for p in pics:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def build_days(lessons_root: Path):
    """扫全部课程,把卡片的 added 聚合成「课堂日」汇总(index.json 的 days)。
    ⚠️ 与 gen_audio.py 的 build_days 逐字一致(不 import 它:那边 import 了
    edge_tts,没装它的机器自检就跑不了),改一处要同步改另一处。"""
    days = {}
    for f in sorted(lessons_root.glob("*.json")):
        if f.name in NON_LESSON:
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        for c in d.get("cards", []):
            a = c.get("added")
            if not a:
                continue
            rec = days.setdefault(a, {"date": a, "cards": 0, "lessons": []})
            rec["cards"] += 1
            if f.stem not in rec["lessons"]:
                rec["lessons"].append(f.stem)
    return [days[k] for k in sorted(days, reverse=True)]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = [Path(a) for a in args] if args else \
        sorted(f for f in LESSONS.glob("*.json") if f.name not in NON_LESSON)
    pools = chip_pools()
    lib = set(json.loads((LESSONS / "phonics.json").read_text(encoding="utf-8"))["sounds"])

    ok = True
    for f in files:
        if not f.exists():
            print(f"✗ {f} 不存在")
            ok = False
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        # 跑没跑过 gen_audio：看有没有回写 q_audio
        audio_ready = any(t.get("q_audio") for c in d.get("cards", [])
                          for t in c.get("dialog", []))
        ok &= check_lesson(f, pools, lib, audio_ready).show()

    if "--fix-index" in sys.argv or not args:
        idx_file = LESSONS / "index.json"
        idx_data = json.loads(idx_file.read_text(encoding="utf-8"))
        idx = idx_data["lessons"]
        listed = {l["id"] for l in idx}
        on_disk = {f.stem for f in LESSONS.glob("*.json") if f.name not in NON_LESSON}
        for miss in sorted(on_disk - listed):
            print(f"❌ index.json 里没有 {miss} —— 跑一次 gen_audio.py 会自动补上")
            ok = False
        for ghost in sorted(listed - on_disk):
            print(f"❌ index.json 里的 {ghost} 找不到对应课程文件")
            ok = False
        # 课堂日汇总(days)和卡片的 added 对不上就地重建:gen_audio 每次会重算,
        # 但手改课程文件(删卡/挪卡/补 added)不跑音频时,这里是唯一的重建口
        days = build_days(LESSONS)
        if (idx_data.get("days") or []) != days:
            idx_data["days"] = days
            if "--fix-index" in sys.argv:
                idx_file.write_text(
                    json.dumps(idx_data, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"✔ index.json 的课堂日汇总已重建({len(days)} 个课堂日)")
            else:
                print("⚠ index.json 的课堂日汇总(days)和卡片的 added 对不上 —— "
                      "跑 python check_lesson.py --fix-index 重建")

    print(f"\n{'全部通过' if ok else '有错误，见上'}（{len(files)} 节课）")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
