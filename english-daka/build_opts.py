#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
闯关整句选项
============
给每道闯关题预造两条**整句**干扰句，写进 `dialog[].opts`。

    python build_opts.py                          # 补全站所有缺选项的题
    python build_opts.py lessons/k2-letter-c.json # 只补这一课（框架库照样全站扫）
    python build_opts.py lessons/x.json --force   # 这一课的例句改过了：先丢掉旧选项重造
    python build_opts.py --dry [--show] [--fail]  # 只看不写 / 打印每种句式 / 列出造不出的

在建课流程里排在 gen_audio.py **之前**：gen_audio 会把 opts 里没音频的句子一并合成
（和答句同音色 Jenny，否则三条选项里正确的那条会是另一个音色，一听就露）。
check_lesson.py 会校验：正好 2 条、答案不和正确答案相同、不重复、音频必须在。

为什么是整句
------------
只给一个单词太好蒙 —— 抓住题面里那个词、或认出三个里哪个"像答案"就完了。
三条整句只差那一个词，必须听完整句才分得出。孩子不认字，所以每条自带喇叭。

怎么造（两层）
--------------
① **换词**：不去"造"句子，而是把语料里在同一个槽位真实出现过的词换进来。
   先把每条答句拆成「框架 + 槽位词」（`These are ___.` ＋ `eyes`），全站扫一遍得到
   「哪个框架里出现过哪些词、各自写成什么样」，换的时候只从同框架的已见词里挑，
   并照抄它在原句里的大小写。语法天然正确 —— 不用再补冠词/单复数/词性一类的规则
   （补也补不完：`These are see.`、`They are cage.`、`we candies up.` 都是那样漏出来的）。
   框架里凑不够时退回音标/字母/数字这些**闭合池**（它们的框架是固定模板，任何成员填进去都通），
   渲染时照原词的大小写（`begins with letter A` 不能塞成 `letter n`）。
② **真句**：框架全站只出现过一次的句子（`I can read a book.`）换不了词，就拿**本课**别的
   真实答句当干扰项 —— 按长短和「带不带音标」排序挑最像的，音频现成。
   不排序会给「How do you read: m — an?」配上「Tan ends with the sound /n/.」，一眼就能排除。

三条守卫（都是实撞过的）
------------------------
- key 在句中出现两次以上的不造（换前一个会把题干改掉：`One fewer than two is one.`）。
- 干扰词已在句中出现过的不用（`A whale is a whale animal.`）。
- 本课出现过的词优先（框架库是全站的，不然农场课里会冒出 `It's a trapezoid.`）。

两条纪律（不守就会把别人的活搅乱）
----------------------------------
- **已有两条干扰句且音频齐的题一律跳过**。干扰项按哈希从候选池里挑，别的会话新增一课
  就会让候选池变大、结果漂移 —— 没这条，改一句例句会把 89 课的干扰句全部重选，
  而新句子没音频，只能整批回退。例句真改过的课用 `--force`。
- **内容没变的文件不回写**。无条件 json.dumps 会把别人用不同缩进写的文件重新序列化：
  语义零差，git 却标成 77 个 M。
"""
import argparse
import collections
import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
LESSONS = ROOT / "lessons"
sys.path.insert(0, str(ROOT))
import check_lesson  # noqa: E402  —— 闭合词池和 NON_LESSON 只在它那儿定义，不另抄一份

POOLS = check_lesson.chip_pools()
VOWEL = tuple("aeiouAEIOU")


def h32(s: str) -> int:
    """稳定哈希。⚠️ 别用内置 hash()：Python 对字符串每个进程随机加盐，同一课跑两次会选出不同干扰项"""
    return int(hashlib.md5(s.encode("utf-8")).hexdigest(), 16)


def family(k):
    """key 属于哪个闭合池；普通名词返回 None（和 app.html 的 chipFamily 同一套判断）"""
    if re.fullmatch(r"/[a-z]+/", k):
        return POOLS["PHONEME_CHIPS"] if k in POOLS["PHONEME_CHIPS"] else POOLS["RIME_CHIPS"]
    for n in ("COLOR_CHIPS", "NUM_CHIPS", "LETTER_CHIPS", "SHAPE_CHIPS", "CASE_CHIPS"):
        if k in POOLS[n]:
            return POOLS[n]
    return None


def slot(sent, key):
    """把句子拆成 (前, 后, 这个词在句子里写成什么样)。
    key 出现不是正好一次就返回 None：换前一个会改掉题干，换后一个在规律条里一样别扭"""
    ms = list(re.finditer(r"(?<![A-Za-z])" + re.escape(key) + r"(?![A-Za-z])", sent, re.I))
    if len(ms) != 1:
        return None
    m = ms[0]
    return sent[:m.start()], sent[m.end():], sent[m.start():m.end()]


def norm_frame(pre, post):
    return (pre.strip().lower(), post.strip().lower())


def render(pre, post, shown):
    """把写法接回框架；接在句首就提大写，冠词跟着新词改（a oval → an oval）"""
    m = re.search(r"\b(a|an)(\s+)$", pre, re.I)
    if m:
        art = "an" if shown[:1] in VOWEL else "a"
        if m.group(1)[:1].isupper():
            art = art[0].upper() + art[1:]
        pre = pre[:m.start()] + art + m.group(2)
    if not pre.strip() and shown[:1].isalpha():
        shown = shown[0].upper() + shown[1:]
    return pre + shown + post


def lesson_files():
    return sorted(p for p in LESSONS.glob("*.json") if p.name not in check_lesson.NON_LESSON)


def scan_frames(files):
    """第一遍：全站扫框架 → {框架: {key: 它在句子里的写法}}"""
    seen = collections.defaultdict(dict)
    for f in files:
        d = json.loads(f.read_text(encoding="utf-8"))
        for c in d.get("cards", []):
            for t in (c.get("dialog") or []):
                if t.get("practice") is False or not t.get("a"):
                    continue
                sl = slot(t["a"][0], " ".join(t["key"]))
                if sl:
                    pre, post, shown = sl
                    seen[norm_frame(pre, post)].setdefault(" ".join(t["key"]), shown)
    return seen


def pick(seen, sent, key, local, want=2):
    """第一层：换词。返回 [(key, 句子), ...]，凑不齐返回 []"""
    sl = slot(sent, key)
    if not sl:
        return []
    pre, post, shown0 = sl
    cands = {k: v for k, v in seen[norm_frame(pre, post)].items() if k != key}
    if len(cands) < want:
        fam = family(key)
        if fam:
            for k in fam:
                if k != key and k not in cands:
                    cands[k] = (k.upper() if shown0.isupper()
                                else k[0].upper() + k[1:] if shown0[:1].isupper() else k)
    if len(cands) < want:
        return []
    h = h32(sent)
    keys = sorted(cands, key=lambda k: (0 if k in local else 1, (h + h32(k)) % 997))
    out = []
    for k in keys:
        if re.search(r"(?<![A-Za-z])" + re.escape(k) + r"(?![A-Za-z])", sent, re.I):
            continue
        txt = render(pre, post, cands[k])
        if txt != sent:
            out.append((k, txt))
        if len(out) == want:
            break
    return out


def realpool(d):
    """本课所有『key, 答句, 答句音频』—— 第二层从这里取，句子和音频都是现成的"""
    return [(" ".join(t["key"]), t["a"][0], t["a_audio"][0])
            for c in d["cards"] for t in (c.get("dialog") or [])
            if t.get("practice") is not False and t.get("a") and t.get("a_audio")]


def pick_real(sent, key, pool, want=2):
    """第二层：本课真实答句，形状（长短 / 带不带音标）最像的优先"""
    cands = [(k, a, au) for k, a, au in pool if k != key and a != sent]
    if len(cands) < want:
        return []

    def shape(x):
        return (1 if "/" in x else 0, len(x.split()))

    s0 = shape(sent)
    h = h32(sent)
    ranked = sorted(cands, key=lambda c: (abs(shape(c[1])[0] - s0[0]) * 10
                                          + abs(shape(c[1])[1] - s0[1]),
                                          (h + h32(c[1])) % 997))
    out, seen_a = [], {sent}
    for k, a, au in ranked:
        if a in seen_a:
            continue
        seen_a.add(a)
        out.append({"key": k, "text": a, "audio": au})
        if len(out) == want:
            break
    return out


def complete(opts, sent):
    """已有两条、文本和音频都在、且没有一条和正确答句相同 → 不动它"""
    return (isinstance(opts, list) and len(opts) == 2
            and all(o.get("text") and o.get("audio")
                    and (LESSONS / o["audio"]).exists() for o in opts)
            and not any(o["text"] == sent for o in opts))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("lessons", nargs="*", help="只处理这些课（默认全部）；框架库始终全站扫")
    ap.add_argument("--force", action="store_true", help="目标课先丢掉旧 opts 再造（例句改过时用）")
    ap.add_argument("--dry", action="store_true", help="只报告，不写文件")
    ap.add_argument("--show", action="store_true", help="每种句式打印一条「正确 / 干扰」样例")
    ap.add_argument("--fail", action="store_true", help="列出两层都造不出的题")
    args = ap.parse_args()

    files = lesson_files()
    targets = {Path(x).resolve() for x in args.lessons} if args.lessons else {f.resolve() for f in files}
    bad = [x for x in args.lessons if Path(x).resolve() not in {f.resolve() for f in files}]
    if bad:
        sys.exit(f"❌ 不是课程文件：{bad}")

    seen = scan_frames(files)
    kept = made = made2 = fail = written = 0
    failrows, samples = [], {}
    for f in files:
        if f.resolve() not in targets:
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        before = json.loads(json.dumps(d))
        pool = realpool(d)
        local = {k for k, _, _ in pool}
        for c in d.get("cards", []):
            for t in (c.get("dialog") or []):
                if t.get("practice") is False:
                    continue
                if args.force:
                    t.pop("opts", None)
                key, sent = " ".join(t["key"]), t["a"][0]
                if complete(t.get("opts"), sent):
                    kept += 1
                    continue
                got = pick(seen, sent, key, local)
                if len(got) >= 2:
                    t["opts"] = [{"key": k, "text": x} for k, x in got]
                    made += 1
                    samples.setdefault(sent, got[0][1])
                    continue
                got2 = pick_real(sent, key, pool)
                if len(got2) >= 2:
                    t["opts"] = got2
                    made2 += 1
                    samples.setdefault(sent, got2[0]["text"])
                    continue
                fail += 1
                failrows.append((f.stem, c["word"], sent, key))
                t.pop("opts", None)
        if d != before and not args.dry:
            f.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            written += 1

    print(f"已有且音频齐,跳过: {kept}")
    print(f"第一层 换词造句(要合成音频): {made}")
    print(f"第二层 用本课真实答句(音频现成): {made2}")
    print(f"两层都不行(退回单词选项): {fail}")
    print(("(dry) " if args.dry else "") + f"回写文件: {written}")
    if made or made2:
        print("→ 接着跑 gen_audio.py 合成新干扰句的音频，再 check_lesson.py")
    if args.show:
        for a, b in sorted(samples.items()):
            print("  正 %-52s 干扰 %s" % (a[:52], b[:52]))
    if args.fail:
        for r in failrows:
            print("  ", r)


if __name__ == "__main__":
    main()
