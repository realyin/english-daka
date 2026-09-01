#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新课脚手架（按课型）
====================
一条命令产出三样东西：

  1. lessons/<课程id>.json   骨架已填好 seq/group/badge/title，
                             问答按该课型的固定句式生成，只留 cn / 例句 待填
  2. docs/prompts/<课程id>.md 这一课每张卡的配图 prompt（含统一风格前缀）
  3. 终端打印「上线前同步清单」——比如新字母要改 app.html 的选项池

课型（决定骨架长什么样，也决定 seq 落在哪一段）：

  letter        字母课        seq 1xx   字母卡 + 词卡，各 2 问
  word-family   词族课        seq 2xx   族卡 + 词卡（词卡带拼读面板）
  cvc           拼读课        seq 3xx   全是带拼读面板的 CVC 卡
  sight-word    常见词课      seq 4xx   虚词卡（quiz:false）+ 例句词卡
  topic         通用词汇课    seq 5xx   主题/数学/科学共用，一词一卡

用法：

  python new_lesson.py letter      --badge C --words cat,cup,car
  python new_lesson.py word-family --rime at --words sat,fat,mat
  python new_lesson.py cvc         --vowel a --words man,fan,can
  python new_lesson.py sight-word  --words my,like --extra dog,ice cream
  python new_lesson.py topic       --group "主题 Topics" --title "At the Farm · 农场" \\
                                   --badge 🐄 --words cow,pig,duck

⚠️ 脚本不替你选词。词表永远来自线下课的原始课件，见 CLAUDE.md
   「课程内容跟线下课走」——不要提前造课，也不要替换选词。

建课完整流程见 docs/课程制作规范.md，简版：
  1. 本脚本生成骨架 + prompt
  2. 填 cn / 例句 / a_cn（骨架里标了 待填 的地方）
  3. python check_lesson.py lessons/<id>.json    ← 自检，必须全绿
  4. 出图 → python ingest_images.py <图目录>
  5. python gen_audio.py lessons/<id>.json
  6. 拼读/词族课再跑 python gen_phonics.py --blends lessons/<id>.json
  7. 再跑一次 check_lesson.py（这次会连音频一起查）
"""

import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).parent
LESSONS = ROOT / "lessons"
PROMPTS = ROOT / "docs" / "prompts"

TODO = "待填"          # 骨架里等人填的地方，check_lesson.py 会挑出来

LEVELS = ["k1", "k2", "k3", "s1", "s2", "s3"]     # 学习路径顺序,id 前缀用小写

# 课型 → (目录页分组, seq 段)。课程 id 前缀 = <级别>-<课型缩写>-,由 --level 决定
TYPES = OrderedDict([
    ("letter",      ("字母 Letters",       100, "letter-")),
    ("word-family", ("词族 Word Family",   200, "wf-")),
    ("cvc",         ("拼读 Phonics",       300, "cvc-")),
    ("sight-word",  ("常见词 Sight Words", 400, "sw-")),
    ("topic",       (None,                 500, "")),         # 分组由 --group 指定
])
# topic 类课程可以落在这几段
TOPIC_BANDS = {"主题 Topics": 500, "数学 Math": 600, "科学 Science": 700}

# 音标记号 → 音素库 key。⚠️ 与 gen_audio.py / app.html 的 PHONEME_MAP 是同一张表，
# 改一处要三处同步（见 docs/课程制作规范.md「一处改动要同步三个地方」）
PHONEME_MAP = {"a": "ae", "e": "eh", "i": "ih", "o": "aa", "u": "ah",
               "ks": "x", "kw": "qu"}
VOWEL_IPA = {"a": "æ", "e": "ɛ", "i": "ɪ", "o": "ɑ", "u": "ʌ"}
# 字母 → 音标记号。多数字母写自己就对（S→/s/），这三个不是：
#   C 发 /k/（"cat"）、Q 发 /kw/、X 发 /ks/。写 /c/ 会映射不到音素库，
#   合成时退回 TTS 把它念成字母名 "see"。
# 一字多音的（C 也可以发 /s/、G 可以发 /dʒ/）用 --sound 指定，别硬套。
LETTER_SOUND = {"c": "k", "q": "kw", "x": "ks"}
# 辅音字母 → 音素库 key（拼读面板的 parts[].sound 直接写库 key，不是记号）。
# cat 的 c 要写 "k"，写 "c" 库里没有、面板点下去是哑的
CONSONANT_KEY = {"c": "k", "q": "qu"}

STYLE_PREFIX = """Children's picture book illustration, soft watercolor style with clean rounded
outlines, warm bright cheerful colors, simple uncluttered background, single
clear subject centered in frame, vertical 3:4 composition, friendly and cute,
suitable for a 5-year-old, NO text, NO letters, NO words, NO numbers, NO speech
bubbles, NO labels, NO borders or frames, NO panel dividers."""

NEG_PROMPT = """text, letters, words, captions, labels, watermark, speech bubble, comic panels,
grid lines, borders, frame, collage of photos, realistic photo, scary, cluttered"""


# ---------------------------------------------------------------- 小工具

def slug(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def load_phonics() -> dict:
    return json.loads((LESSONS / "phonics.json").read_text(encoding="utf-8"))["sounds"]


def ipa_of(marker: str, lib: dict) -> str:
    """字母记号 → 真 IPA（写在课程标题和中文里）。/a/ → /æ/、/s/ → /s/。
       映射不到就直接报错 —— 静默回落会生成一节音标全错的课"""
    key = PHONEME_MAP.get(marker, marker)
    if key not in lib:
        sys.exit(f"❌ 音标记号 /{marker}/ 映射到「{key}」，但 lessons/phonics.json 里没有。\n"
                 f"   可用的记号见音素库；一字多音的字母请用 --sound 指定，"
                 f"例如字母 C 发 /k/：--sound k")
    return lib[key]["ipa"]


def next_seq(band: int, group: str) -> int:
    """同组里往后排一个号；组里还没有课就取 band+1"""
    idx_path = LESSONS / "index.json"
    if not idx_path.exists():
        return band + 1
    used = [l.get("seq", 0) for l in json.loads(idx_path.read_text(encoding="utf-8"))["lessons"]
            if l.get("group") == group and l.get("level", "K2") == LEVEL]
    return max(used) + 1 if used else band + 1


def qa(q, a, key, q_cn, a_cn):
    """一问一答。a / a_cn 一律用列表，答句可以不止一条"""
    return OrderedDict([("q", q), ("a", a if isinstance(a, list) else [a]),
                        ("key", key if isinstance(key, list) else [key]),
                        ("q_cn", q_cn),
                        ("a_cn", a_cn if isinstance(a_cn, list) else [a_cn])])


def card(word, cn, tag, image, dialog, **extra):
    c = OrderedDict([("word", word), ("cn", cn), ("tag", tag), ("image", image)])
    c.update(extra)                      # quiz / collage / emoji / phonics
    c["dialog"] = dialog
    return c


def phonics_block(word: str, lib: dict) -> OrderedDict:
    """CVC 三音词 → 拼读面板结构。不是三个字母的词返回 None，由调用方决定怎么办"""
    if len(word) != 3 or not word.isalpha():
        return None
    c1, v, c2 = word.lower()
    if v not in VOWEL_IPA:
        return None
    rime = v + c2
    k1, k2 = CONSONANT_KEY.get(c1, c1), CONSONANT_KEY.get(c2, c2)
    parts = [{"text": c1, "sound": k1, "kind": "consonant"},
             {"text": v, "sound": PHONEME_MAP[v], "kind": "vowel"},
             {"text": c2, "sound": k2, "kind": "consonant"}]
    # sound 必须是音素库里真有的 key，否则面板点下去是哑的
    for p in parts:
        if p["sound"] not in lib:
            return None
    if rime not in lib:
        return None
    return OrderedDict([
        ("group", f"短音 {v} /{VOWEL_IPA[v]}/ · -{rime} 词族"),
        ("ipa", f"/{c1}{VOWEL_IPA[v]}{c2}/"),
        ("parts", parts),
        ("onset", {"text": c1, "sound": k1}),
        ("rime", {"text": rime, "sound": rime}),
        ("blend_audio", f"audio/phonics/blend-{word}.mp3"),
    ])


# ---------------------------------------------------------------- 各课型骨架

def build_letter(args, lib):
    L = args.badge.strip().upper()
    low = L.lower()
    snd = args.sound or LETTER_SOUND.get(low, low)     # 音标记号，不一定等于字母
    marker = f"/{snd}/"
    title = f"Letter {L} · {ipa_of(snd, lib)}"
    lesson_id = f"{PREFIX}letter-{low}"
    cards = [card(
        f"letter {L}", f"字母 {L}", "letter", f"images/{low}-letter.webp",
        [qa(f"What's this letter?", f"It's letter {L}.", [low],
            "这是什么字母？", f"这是字母 {L}。"),
         qa(f"What sound does letter {L} make?",
            f"{L} makes the sound {marker}.", [marker],
            f"字母 {L} 发什么音？", f"{L} 发 {ipa_of(snd, lib)} 的音。")])]
    for w in args.words:
        cards.append(card(
            w, TODO, "word", f"images/{low}-{slug(w)}.webp",
            [qa(f"Which letter does {w} begin with?",
                f"{w.capitalize()} begins with letter {L}.", [low],
                f"{w} 以哪个字母开头？", f"{w} 以字母 {L} 开头。"),
             qa(f"What sound does {w} begin with?",
                f"{w.capitalize()} begins with the sound {marker}.", [marker],
                f"{w} 以什么音开头？", f"{w} 以 {ipa_of(snd, lib)} 音开头。")]))
    return lesson_id, title, L, cards


def build_word_family(args, lib):
    rime = args.rime.strip().lower()
    title = f"Word Family · -{rime} 词族"
    lesson_id = f"{PREFIX}wf-{rime}"
    marker = f"/{rime}/"
    cards = [card(
        f"-{rime} family", f"-{rime} 词族", "CVC", f"images/wf-{rime}.webp",
        [qa(f"What sound does -{rime} make?",
            f"{rime.capitalize()} makes the sound {marker}.", [marker],
            f"-{rime} 发什么音？", f"-{rime} 发 {ipa_of(rime, lib)} 的音。"),
         qa("What's this family?", f"It's -{rime} family.", ["family"],
            "这是什么词族？", f"这是 -{rime} 词族。")],
        quiz=False)]
    for w in args.words:
        onset = w[:-len(rime)]
        ph = phonics_block(w, lib)
        extra = {"phonics": ph} if ph else {}
        cards.append(card(
            w, TODO, "word", f"images/wf-{rime}-{slug(w)}.webp",
            [qa(f"How do you read: {onset} — {rime}?",
                [f"/{onset}/ {marker}, {w}.", TODO],       # 第二条是描述这张图的例句
                [w],
                f"{onset} 加 {rime} 怎么读？",
                [f"/{onset}/ {ipa_of(rime, lib)}，{w}。", TODO])],
            **extra))
    return lesson_id, title, f"-{rime}", cards


def build_cvc(args, lib):
    v = args.vowel.strip().lower()
    title = f"Short {v} · 短元音 {v} 拼读"
    lesson_id = f"{PREFIX}cvc-{v}"
    cards = []
    for w in args.words:
        ph = phonics_block(w, lib)
        extra = {"phonics": ph} if ph else {}
        cards.append(card(
            w, TODO, "CVC", f"images/cvc-{slug(w)}.webp",
            [qa("What word is this?", f"It's {w}.", [w],
                "这是什么单词？", f"这是 {w}。")],
            **extra))
    return lesson_id, title, v, cards


def build_sight_word(args, lib):
    sws = args.words
    title = "Sight Words · " + " / ".join(sws)
    lesson_id = f"{PREFIX}sw-" + "-".join(slug(w) for w in sws)
    cards = []
    for w in sws:
        # 虚词画不出来 → quiz:false 挡住「哪一个是 X」。
        # 但第二条答句是描述画面的，听句选图照样成立，所以必须写。
        cards.append(card(
            w, TODO, "sight word", f"images/sw-{slug(w)}.webp",
            [qa("What's this sight word?",
                [f"It's sight word {w}.", TODO], [w],
                "这是什么常见词？", [f"是常见词 {w}。", TODO])],
            quiz=False))
    for w in args.extra:
        cards.append(card(
            w, TODO, "word", f"images/sw-{slug(w)}.webp",
            [qa(TODO, [TODO], [slug(w).replace("-", " ")], TODO, [TODO])]))
    return lesson_id, title, sws[0], cards


def build_topic(args, lib):
    title = args.title
    lesson_id = PREFIX + slug(title.split(" · ")[0])
    cards = [card(w, TODO, args.tag, f"images/{slug(lesson_id[3:])}-{slug(w)}.webp",
                  [qa(TODO, [TODO], [slug(w).replace("-", " ")], TODO, [TODO])])
             for w in args.words]
    return lesson_id, title, args.badge, cards


BUILDERS = {"letter": build_letter, "word-family": build_word_family,
            "cvc": build_cvc, "sight-word": build_sight_word, "topic": build_topic}


# ---------------------------------------------------------------- 配图 prompt

def write_prompts(lesson_id, title, cards):
    """每课一个 prompt 文件。文件名就是入库名，也是卡片 image 字段的名字 ——
       一名三用，不需要编号映射表（ingest_images.py 支持语义命名直接入库）"""
    PROMPTS.mkdir(parents=True, exist_ok=True)
    out = PROMPTS / f"{lesson_id}.md"
    lines = [f"# 配图 Prompt · {title}", "",
             f"共 {len(cards)} 张。**每条 prompt 前面都要加下面的统一风格前缀**，",
             "保证全站画风一致。出图后按「存为」那一列的名字命名，然后：", "",
             "```bash", f"python ingest_images.py <图片目录>", "```", "",
             "文件名即入库名，也是卡片 `image` 字段的名字，不需要编号对照表。", "",
             "## 统一风格前缀（复制到每条 prompt 前面）", "",
             "```", STYLE_PREFIX, "```", "",
             "## 负面提示（工具支持的话）", "",
             "```", NEG_PROMPT, "```", "",
             "## 逐张 prompt", ""]
    for c in cards:
        name = Path(c["image"]).stem
        sents = [s for qa_ in c["dialog"] for s in qa_["a"] if s != TODO]
        hint = sents[-1] if sents else ""
        lines += [f"### `{name}` — {c['word']}", "",
                  f"- **存为**：`{name}.png`",
                  f"- **画面必须能回答**：{c['dialog'][0]['q']}"]
        if hint:
            lines.append(f"- **对应句子**：{hint}")
        lines += ["",
                  "```",
                  f"{TODO}：一句话描述画面主体。要求：单一主体、"
                  f"能让 5 岁孩子一眼认出是「{c['word']}」，",
                  f"不要画出这一课其它卡片的东西（会和考一考的选项撞车）。",
                  "```", ""]
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


# ---------------------------------------------------------------- 同步清单

def checklist(ctype, lesson_id, cards, args):
    tips = []
    if ctype == "letter":
        low = args.badge.lower()
        snd = args.sound or LETTER_SOUND.get(low, low)
        app = (ROOT / "app.html").read_text(encoding="utf-8")
        for pool, item in [("LETTER_CHIPS", f'"{low}"'), ("PHONEME_CHIPS", f'"/{snd}/"')]:
            line = re.search(rf"const {pool}\s*=\s*\[(.*?)\]", app, re.S)
            if line and item not in line.group(1):
                tips.append(f"app.html 的 {pool} 里没有 {item} —— 不加进去，"
                            f"闯关的干扰项会掉进普通名词池，变成送分题")
    if ctype == "word-family":
        app = (ROOT / "app.html").read_text(encoding="utf-8")
        m = re.search(r"const RIME_CHIPS\s*=\s*\[(.*?)\]", app, re.S)
        if m and f'"/{args.rime}/"' not in m.group(1):
            tips.append(f'app.html 的 RIME_CHIPS 里没有 "/{args.rime}/" —— '
                        f"不加进去，词族的听音辨音题会拿名词当干扰项")
    if any(c.get("phonics") for c in cards):
        tips.append(f"这课有拼读面板，音频要多跑一步："
                    f"python gen_phonics.py --blends lessons/{lesson_id}.json")
    no_ph = [c["word"] for c in cards
             if c["tag"] in ("CVC",) and not c.get("phonics") and not c.get("quiz") is False]
    if no_ph:
        tips.append(f"这些词不是「辅音+短元音+辅音」三音词，没能自动生成拼读面板，"
                    f"要手写或去掉：{no_ph}")
    return tips


# ---------------------------------------------------------------- 主流程

def main():
    p = argparse.ArgumentParser(
        description="按课型生成新课骨架 + 配图 prompt",
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    p.add_argument("type", choices=list(TYPES), help="课型")
    p.add_argument("--level", default="k2", choices=LEVELS,
                   help="级别(默认 k2)。决定课程 id 前缀和目录页归属;"
                        "级别间 seq 独立编号,组名可以同名")
    p.add_argument("--words", default="", help="词表，逗号分隔（来自线下课件，脚本不替你选词）")
    p.add_argument("--badge", default="", help="目录页封面上的大字：字母课填 C，主题课填 emoji")
    p.add_argument("--sound", default="",
                   help="letter: 音标记号，一字多音时指定（字母 C 发 /k/ 就写 --sound k）；"
                        "不写则按 LETTER_SOUND 表推断")
    p.add_argument("--rime", default="", help="word-family: 韵脚，如 at")
    p.add_argument("--vowel", default="", help="cvc: 短元音字母，如 a")
    p.add_argument("--extra", default="", help="sight-word: 除虚词外的实词卡")
    p.add_argument("--group", default="", help="topic: 目录页分组（主题 Topics / 数学 Math / 科学 Science）")
    p.add_argument("--title", default="", help="topic: 课程标题，如 \"At the Farm · 农场\"")
    p.add_argument("--tag", default="word", help="topic: 卡片 tag（word / number / science …）")
    a = p.parse_args()
    a.words = [w.strip() for w in a.words.split(",") if w.strip()]
    a.extra = [w.strip() for w in a.extra.split(",") if w.strip()]

    need = {"letter": ["badge", "words"], "word-family": ["rime", "words"],
            "cvc": ["vowel", "words"], "sight-word": ["words"],
            "topic": ["group", "title", "badge", "words"]}[a.type]
    for n in need:
        if not getattr(a, n):
            p.error(f"课型 {a.type} 需要 --{n}")

    global LEVEL, PREFIX
    LEVEL = a.level.upper()
    PREFIX = a.level.lower() + "-"
    lib = load_phonics()
    lesson_id, title, badge, cards = BUILDERS[a.type](a, lib)

    group = a.group if a.type == "topic" else TYPES[a.type][0]
    band = TOPIC_BANDS.get(group, TYPES[a.type][1]) if a.type == "topic" else TYPES[a.type][1]
    if a.type == "topic" and group not in TOPIC_BANDS:
        p.error(f"--group 只能是 {list(TOPIC_BANDS)} 之一")

    out = LESSONS / f"{lesson_id}.json"
    if out.exists():
        print(f"❌ {out} 已存在，不覆盖")
        sys.exit(1)

    lesson = OrderedDict([("seq", next_seq(band, group)), ("level", LEVEL),
                          ("group", group),
                          ("badge", str(badge)), ("title", title), ("cards", cards)])
    out.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pf = write_prompts(lesson_id, title, cards)

    print(f"✓ {out}")
    print(f"    seq={lesson['seq']}  group={group}  badge={badge}  {len(cards)} 张卡")
    print(f"✓ {pf}  （{len(cards)} 条配图 prompt）")

    tips = checklist(a.type, lesson_id, cards, a)
    if tips:
        print("\n⚠ 上线前要同步的：")
        for t in tips:
            print(f"   · {t}")

    steps = [f"填掉骨架里的「{TODO}」：cn / 例句 / a_cn",
             f"python check_lesson.py lessons/{lesson_id}.json      ← 必须全绿",
             f"补 docs/prompts/{lesson_id}.md 里的画面描述 → 出图 → "
             f"python ingest_images.py <图目录>",
             f"python gen_audio.py lessons/{lesson_id}.json"]
    if any(c.get("phonics") for c in cards):
        steps.append(f"python gen_phonics.py --blends lessons/{lesson_id}.json")
    steps.append("再跑一次 check_lesson.py（这次连音频一起查）")
    print("\n接下来：")
    for i, st in enumerate(steps, 1):
        print(f"  {i}. {st}")


if __name__ == "__main__":
    main()
