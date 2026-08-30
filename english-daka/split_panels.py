#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
拼图配图拆分脚本:把「一张图拼了好几个词」的聚合配图切成一格一图
================================================================
配图清单里有 30 张图是按「2×2 四格」或「三格并排」的 prompt 生成的
(docs/配图Prompt清单.md 里写死了 `2×2 grid of four separate cute scenes`),
每一格本来就对应卡片里的一组问答。这个脚本把它们切开、归一化入库,
并把 `dialog[].image` 回填进课程 JSON。

切完之后:
  - 学一学:每组问答上面是它自己那张图(卡片图不再重复显示)
  - 问答闯关:app.html 的 `qa.image || c.image` 自动用上单格图
  - 考一考:每格有了真名字,聚合卡才有条件拆成「一图一词」(下一步)

用法:
    python3 split_panels.py --dry      # 只打印会切哪些、回填哪些,不写文件
    python3 split_panels.py            # 真的写
    python3 split_panels.py --only a-words-1 wf-it

源图取全分辨率原稿 generated-images/001-007/<编号>.png (1086×1448),
不是已经压过的 lessons/images/*.webp,避免二次压缩掉画质。
编号→文件名的映射和 ingest_images.py 一样从 docs/配图Prompt清单.md 解析。

坐标约定:每格的 box 是 (x0, y0, x1, y1) 的相对比例。
所有 box 的宽高比都 >= 3:4(不比 3:4 更瘦),脚本只在上下补背景色补足 3:4,
绝不裁掉主体——这些插画的底色是均匀米白,补出来看不出接缝。
"""

import json
import re
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent
DOC = ROOT / "docs" / "配图Prompt清单.md"
SRC_DIR = ROOT / "generated-images" / "001-007"

# 少数几格的原稿不在 generated-images 里(生成图画错了内容),得回到课件原版去切
SRC_OVERRIDE = {
    "math-chips": ROOT / "lessons_original" / "K2" / "06_math" / "01_one_to_five"
                       / "01_math-02-review.png",
}
IMAGES = ROOT / "lessons" / "images"
LESSONS = ROOT / "lessons"

TARGET_W, TARGET_H = 720, 960
MAX_BYTES = 150 * 1024

# 2×2 四格的标准坐标
Q_TL = (0.00, 0.00, 0.50, 0.50)
Q_TR = (0.50, 0.00, 1.00, 0.50)
Q_BL = (0.00, 0.50, 0.50, 1.00)
Q_BR = (0.50, 0.50, 1.00, 1.00)

# ---------------------------------------------------------------------------
# 每张聚合图 → [(单格语义名, box, 用在第几组问答)]
# dialog 序号可以重复(同一格图服务多组问答,如 iguana 的头尾两问),
# 也可以缺号(那组问答在图里没有对应格子 —— 见文件末尾的 MISMATCH 注释)
# ---------------------------------------------------------------------------
PANELS = {
    # ---- 2×2 四格 ----
    "s-words":        [("sheep", Q_TL, 0), ("snake", Q_TR, 1),
                       ("school", Q_BL, 2), ("sun", Q_BR, 3)],
    "t-words-1":      [("turtle", Q_TL, 0), ("toast", Q_TR, 1),
                       ("brush", Q_BL, 2), ("ten", Q_BR, 3)],
    "t-words-2":      [("trumpet", Q_TL, 0), ("tree", Q_TR, 1),
                       ("teacher", Q_BL, 2), ("tank", Q_BR, 3)],
    "t-words-3":      [("triangle", Q_TL, 0), ("touch", Q_TR, 1),
                       ("rectangle", Q_BL, 2), ("thanksgiving", Q_BR, 3)],
    "m-words-1":      [("monkey", Q_TL, 0), ("mouse", Q_TR, 1),
                       ("milk", Q_BL, 2), ("mouth", Q_BR, 3)],
    "m-words-2":      [("orange", Q_TL, 0), ("market", Q_TR, 1),
                       ("christmas", Q_BL, 2), ("fans", Q_BR, 3)],
    "a-words-1":      [("apple", Q_TL, 0), ("dolphin", Q_TR, 1),
                       ("alligator", Q_BL, 2), ("astronaut", Q_BR, 3)],
    "a-words-2":      [("bat", Q_TL, 0), ("dad", Q_TR, 1),
                       ("hat", Q_BL, 2), ("fans", Q_BR, 3)],
    "a-words-3":      [("hands", Q_TL, 0), ("hair", Q_TR, 1),
                       ("policeman", Q_BL, 2), ("cat", Q_BR, 3)],
    "n-need":         [("fan", Q_TL, 0), ("umbrella", Q_TR, 1),
                       ("clothes", Q_BL, 2)],                      # BR 点头图无对应问答
    "f-face-fingers": [("face", Q_TL, 0), ("feet", Q_TR, 1),
                       ("ten", Q_BL, 2), ("five", Q_BR, 3)],
    "f-fan-flower":   [("fan", Q_TL, 0), ("flower", Q_TR, 1),
                       ("farm", Q_BL, 2), ("fly", Q_BR, 3)],
    "i-iguana":       [("iguana", Q_TL, 0), ("eggs", Q_TR, 1),
                       ("plants", Q_BL, 2), ("sun", Q_BR, 3),
                       ("iguana", Q_TL, 4)],                       # 第 5 问也是问鬣蜥
    "r-sleep-can":    [("sleep", Q_TL, 0), ("sing", Q_TR, 1),
                       ("crayfish", Q_BL, 2), ("river", Q_BR, 3)],
    "r-rat-ring":     [("tree", Q_TL, 0), ("city", Q_TR, 1),
                       ("rat", Q_BL, 2), ("ring", Q_BR, 3)],
    "d-ends":         [("bed", Q_TL, 0), ("bed", Q_TL, 1),
                       ("dog", Q_TR, 2), ("dinosaur", Q_BL, 3)],   # BR 娃娃无对应问答
    "sw-egg-hatch":   [("egg", Q_TL, 0), ("hatch", Q_TR, 1),
                       ("plant", Q_BL, 2), ("sun", Q_BR, 3)],
    "recycling-sort": [("paper", Q_TL, 0), ("metal", Q_TR, 1),
                       ("plastic", Q_BL, 2), ("compost", Q_BR, 4)],  # 第 4 问 glass 图里没有
    "wf-an-1":        [("man", Q_TL, 1), ("fan", Q_TR, 2),
                       ("tan", Q_BL, 3)],                          # 0=/an/ 4=family 无图;BR can 未用

    "wf-at-1":        [("sat", Q_TL, 1), ("fat", Q_TR, 2),
                       ("mat", Q_BL, 3)],                          # 0=/at/ 4=family 无图;BR 猫未用

    # ---- 不是拼图,是一整幅场景,但一问一个主体,照样按主体切 ----
    # 客厅里同时有爸爸、浅棕小狗、风扇,三问各问一个 —— 整幅图配哪一问都对不准。
    # 源图本身就是 3:4,所以这里的 box 宽高比例取相等值,切出来正好 3:4,不用补边。
    "wf-an-2":        [("man", (0.06, 0.02, 0.62, 0.58), 0),
                       ("tan", (0.24, 0.50, 0.68, 0.94), 1),
                       ("fan", (0.56, 0.22, 1.00, 0.66), 2)],      # 第 4 问 can(鸟会飞)图里没有

    # ---- 课件原版四格,不是生成图(见 SRC_OVERRIDE) ----
    # chips 卡的四问出自课件的 review 页:动物园两只狮子 / 市场四个苹果 /
    # 两只手 / 动物对圆片,而卡片图(生成的 math-chips)画的是圆片配玩偶,
    # 四问没有一问对得上。原版每格上半是插画、下半是对话文字,只取上半;
    # 每格还有一圈黑色描边框,box 再往里收几个像素把它切掉 —— 留着的话
    # 这张图在考一考里靠"有黑框"就能一眼认出来,等于白送答案。
    # 这张卡后来拆成了四张单卡(图从问答级升到卡片级),脚本已经找不到"在用
    # math-chips 的卡"、整条会跳过 —— 坐标留在这里是备查,要重切照这个 box 切。
    # 另外前三格已换成单独生成的干净白底图,只剩第 4 格还在用课件切图。
    "math-chips":     [("two-lions",    (0.0051, 0.0109, 0.2439, 0.6618), 0),
                       ("four-apples",  (0.2531, 0.0109, 0.4939, 0.6618), 1),
                       ("two-hands",    (0.5041, 0.0109, 0.7439, 0.6618), 2),
                       ("same-number",  (0.7551, 0.0109, 0.9932, 0.6618), 3)],

    # ---- 两格并排 ----
    "n-nurse-nest":   [("nurse", (0.00, 0.04, 0.50, 0.54), 0),
                       ("nurse", (0.00, 0.04, 0.50, 0.54), 1),
                       ("nest",  (0.50, 0.22, 1.00, 0.72), 2),
                       ("nest",  (0.50, 0.22, 1.00, 0.72), 3)],

    # ---- 三格,版式不规则,坐标逐张目测 ----
    "b-ends":         [("web", (0.04, 0.02, 0.96, 0.48), 0),
                       ("bib", (0.00, 0.44, 0.56, 1.00), 1),
                       ("cub", (0.46, 0.44, 1.00, 0.98), 2)],
    "sw-on-holiday":  [("christmas", (0.00, 0.02, 0.50, 0.52), 0),
                       ("egg",       (0.48, 0.08, 1.00, 0.58), 1),
                       ("turkey",    (0.00, 0.55, 1.00, 1.00), 2)],
    "sw-is":          [("pilot",  (0.02, 0.00, 1.00, 0.40), 0),
                       ("circle", (0.00, 0.37, 0.50, 0.75), 1),
                       ("summer", (0.32, 0.40, 1.00, 1.00), 2)],
    "sw-to":          [("sing",    (0.00, 0.04, 0.50, 0.54), 0),
                       ("drums",   (0.42, 0.08, 1.00, 0.54), 1),
                       ("teacher", (0.18, 0.52, 0.92, 1.00), 2)],
    "wf-it":          [("hit", (0.18, 0.00, 0.88, 0.47), 0),
                       ("bit", (0.02, 0.46, 0.60, 1.00), 1),
                       ("lit", (0.50, 0.46, 1.00, 0.96), 2)],
    "wf-at":          [("bat", (0.02, 0.00, 0.98, 0.52), 0),
                       ("rat", (0.00, 0.52, 0.52, 1.00), 1),
                       ("hat", (0.46, 0.56, 1.00, 0.94), 2)],
    "wf-ot":          [("tot", (0.00, 0.02, 0.52, 0.50), 0),
                       ("hot", (0.46, 0.06, 1.00, 0.58), 1),
                       ("dot", (0.08, 0.58, 1.00, 1.00), 2)],
    "wf-ad":          [("dad", (0.14, 0.00, 0.86, 0.50), 0),
                       ("sad", (0.00, 0.48, 0.52, 1.00), 1),
                       ("bad", (0.48, 0.48, 1.00, 1.00), 2)],
    "wf-id":          [("did", (0.00, 0.00, 0.50, 0.48), 0),
                       ("hid", (0.46, 0.24, 1.00, 0.64), 1),
                       ("lid", (0.08, 0.60, 0.86, 1.00), 2)],
}


def load_num_mapping() -> dict:
    """docs/配图Prompt清单.md 的表格: 编号 → 目标文件名(反向用)"""
    mapping = {}
    for line in DOC.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d{3})\s*[★\s]*\|\s*([a-z0-9\-]+)\s*\|", line)
        if m:
            mapping[m.group(2)] = m.group(1)
    return mapping


def bg_color(img: Image.Image) -> tuple:
    """取整图外圈 2% 的中位色当背景色 —— 这些插画四周都是均匀米白"""
    w, h = img.size
    bw, bh = max(1, w // 50), max(1, h // 50)
    px = (list(img.crop((0, 0, w, bh)).getdata())
          + list(img.crop((0, h - bh, w, h)).getdata())
          + list(img.crop((0, 0, bw, h)).getdata())
          + list(img.crop((w - bw, 0, w, h)).getdata()))
    return tuple(sorted(c[i] for c in px)[len(px) // 2] for i in range(3))


def cut(img: Image.Image, box: tuple, bg: tuple) -> Image.Image:
    """按比例裁一格 → 上下补背景色补足 3:4 → 缩放到 720×960"""
    w, h = img.size
    x0, y0, x1, y1 = (int(box[0] * w), int(box[1] * h),
                      int(box[2] * w), int(box[3] * h))
    panel = img.crop((x0, y0, x1, y1))
    pw, ph = panel.size

    ratio = TARGET_W / TARGET_H            # 0.75
    if pw / ph > ratio:                    # 比 3:4 宽 → 上下补
        canvas_w, canvas_h = pw, round(pw / ratio)
    else:                                  # 已经是 3:4 或更瘦 → 左右补(坐标表已保证不会太瘦)
        canvas_w, canvas_h = round(ph * ratio), ph
        canvas_w = max(canvas_w, pw)

    canvas = Image.new("RGB", (canvas_w, canvas_h), bg)
    canvas.paste(panel, ((canvas_w - pw) // 2, (canvas_h - ph) // 2))
    return canvas.resize((TARGET_W, TARGET_H), Image.LANCZOS)


def save_webp(img: Image.Image, name: str) -> int:
    out = IMAGES / f"{name}.webp"
    for quality in (85, 75, 65, 55, 45):
        img.save(out, "WEBP", quality=quality)
        if out.stat().st_size <= MAX_BYTES:
            break
    return out.stat().st_size


def main():
    dry = "--dry" in sys.argv
    only = None
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1:])

    nums = load_num_mapping()
    IMAGES.mkdir(parents=True, exist_ok=True)

    # 先建 图名 → (课程文件, 卡片下标) 索引
    where = {}
    for lp in sorted(LESSONS.glob("*.json")):
        if lp.name in ("index.json", "phonics.json", "dictionary.json"):
            continue
        data = json.loads(lp.read_text(encoding="utf-8"))
        for ci, card in enumerate(data.get("cards", [])):
            im = card.get("image", "")
            stem = Path(im).stem
            if stem in PANELS:
                where[stem] = (lp, ci)

    edits = {}          # 课程文件 → data(改过的)
    made, filled, warns = 0, 0, []

    for stem, panels in PANELS.items():
        if only and stem not in only:
            continue
        if stem not in where:
            warns.append(f"⚠ {stem}: 没有卡片在用这张图,跳过")
            continue
        lp, ci = where[stem]
        data = edits.setdefault(lp, json.loads(lp.read_text(encoding="utf-8")))
        card = data["cards"][ci]
        ndlg = len(card["dialog"])

        # 聚合卡后来被拆成了一图一词的单卡,原卡只剩下"图里没有对应格子"的残余问答,
        # 此时 PANELS 里的问答下标已经全部错位 —— 再按表回填会把图配到错的题上
        # (例:n-need 只剩 "Can you spell number one?",却会被配上风扇图)。
        # 拆卡只会让问答变少,所以「比表里假设的还少」就是被拆过,跳过不猜;
        # 反过来问答比表里多是正常的 —— 末尾那几问图里本来就没有对应主体
        # (wf-an-2 的 can:"鸟会飞"客厅场景里没有鸟),它们照旧回落到卡片图。
        expect = max(di for _, _, di in panels) + 1
        if ndlg < expect:
            warns.append(f"⚠ {stem}: 卡片已被拆过(现 {ndlg} 问,表里假设 {expect} 问),"
                         f"下标会错位,跳过 —— 要重切请先更新 PANELS 表")
            continue

        num = nums.get(stem)
        src = SRC_OVERRIDE.get(stem) or (SRC_DIR / f"{num}.png" if num else None)
        if not src or not src.exists():
            warns.append(f"⚠ {stem}: 找不到原稿 {src},跳过")
            continue

        img = Image.open(src).convert("RGB")
        bg = bg_color(img)
        print(f"\n{stem}  [{lp.stem} / {card['word']}]  {ndlg} 组问答")

        seen = {}
        for word, box, di in panels:
            if di >= ndlg:
                warns.append(f"⚠ {stem}: 问答下标 {di} 越界({ndlg} 组),跳过该格")
                continue
            name = f"{stem}-{word}"
            if name not in seen:
                if dry:
                    print(f"   切 {name}.webp  box={box}")
                else:
                    kb = save_webp(cut(img, box, bg), name) // 1024
                    print(f"   ✓ {name}.webp ({kb}KB)")
                seen[name] = True
                made += 1
            card["dialog"][di]["image"] = f"images/{name}.webp"
            filled += 1
            print(f"     → 第 {di+1} 问 ({' '.join(card['dialog'][di]['key'])})")

        missing = [i for i in range(ndlg) if "image" not in card["dialog"][i]]
        if missing:
            warns.append(f"⚠ {stem}: 第 {[i+1 for i in missing]} 问图里没有对应格子,"
                         f"仍回落到卡片图")

    if not dry:
        for lp, data in edits.items():
            lp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8")
        print(f"\n已改写 {len(edits)} 个课程 JSON")

    print(f"\n{'[dry] ' if dry else ''}切出单格图 {made} 张,回填 dialog[].image {filled} 处")
    if warns:
        print("\n需要人工确认:")
        for w in warns:
            print("  " + w)


if __name__ == "__main__":
    main()
