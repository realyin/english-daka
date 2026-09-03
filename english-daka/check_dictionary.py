#!/usr/bin/env python3
"""词典自检:把课程里能长按查词、却查不到中文的单词列出来。

    python check_dictionary.py            # 列出全部缺词(按出现课数排序)
    python check_dictionary.py k2-cvc-u   # 只看某几课

匹配规则照抄 app.html 的 lookup():精确 → 's → 去 s/es/ies → 去 ing/ed(双写辅音去一个、丢掉的 e 补回)。
句中的 /s/ /oh/ 这类音标记号在应用里点了只发纯音、不能长按,不算缺词。
app.html 里还有一份内置基础词典(DICT 字面量),这里一并算进已收词。
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
LESSONS = ROOT / "lessons"
NON_LESSON = {"index.json", "phonics.json", "dictionary.json", "classes.json"}
PHONEME_RE = re.compile(r"^/[a-z]+/[.,!?]*$")


def builtin_dict() -> set:
    """app.html 里 `let DICT = {...}` 的键"""
    src = (ROOT / "app.html").read_text(encoding="utf-8")
    m = re.search(r"let DICT = \{(.*?)\n\};", src, re.S)
    return set(re.findall(r'"([^"]+)"\s*:', m.group(1))) if m else set()


def make_lookup(dic: set):
    def lookup(w: str) -> bool:
        if w in dic:
            return True
        if w.endswith("'s") and w[:-2] in dic:
            return True
        if w.endswith("s") and w[:-1] in dic:
            return True
        if w.endswith("es") and w[:-2] in dic:
            return True
        if w.endswith("ies") and w[:-3] + "y" in dic:
            return True
        for suf in ("ing", "ed"):
            if not w.endswith(suf):
                continue
            stem = w[:-len(suf)]
            if stem in dic:                                    # jumping→jump
                return True
            if len(stem) > 2 and stem[-1] == stem[-2] and stem[:-1] in dic:
                return True                                    # running→run
            if stem + "e" in dic:                              # making→make
                return True
        return False
    return lookup


def lesson_texts(data: dict):
    """课程里所有会被拆成可长按单词的英文:词条、问句、答句、闯关选项"""
    for card in data.get("cards", []):
        if card.get("word"):
            yield card["word"]
        for dl in card.get("dialog", []):
            yield dl.get("q", "")
            yield from dl.get("a", [])
            for o in dl.get("opts", []):
                yield o.get("text", "")


def missing_words(only=None):
    dic = set(json.loads((LESSONS / "dictionary.json").read_text(encoding="utf-8")))
    dic |= builtin_dict()
    lookup = make_lookup(dic)
    missing = defaultdict(set)
    for lp in sorted(LESSONS.glob("*.json")):
        if lp.name in NON_LESSON:
            continue
        if only and lp.stem not in only:
            continue
        data = json.loads(lp.read_text(encoding="utf-8"))
        for text in lesson_texts(data):
            for raw in text.split():
                if PHONEME_RE.match(raw):
                    continue
                w = re.sub(r"[^a-z']", "", raw.lower())
                if w and not lookup(w):
                    missing[w].add(lp.stem)
    return missing


def main():
    only = set(sys.argv[1:]) or None
    missing = missing_words(only)
    if not missing:
        print("✅ 课程里的词全部能查到中文")
        return
    print(f"❌ {len(missing)} 个词查不到中文(词  课数  出现的课):")
    for w, ls in sorted(missing.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        shown = ", ".join(sorted(ls)[:4]) + (" …" if len(ls) > 4 else "")
        print(f"  {w:<16}{len(ls):>3}  {shown}")
    sys.exit(1)


if __name__ == "__main__":
    main()
