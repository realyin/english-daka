#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配图入库脚本:把任意来源的图片归一化为课程标准资产
====================================================
不管图片来自 AI 生成、课本翻拍还是图库下载,过这道脚本后统一为:
  - 3:4 竖图(居中裁剪,不变形);横图素材可加 --landscape 参数
  - 960×720 分辨率(手机/iPad 视网膜屏够用)
  - webp 格式,自动调质量压到 150KB 以内
  - 语义化文件名,落到 lessons/images/

用法:
    pip install Pillow
    python add_image.py 下载的原图.png halloween-scene
    → 产出 lessons/images/halloween-scene.webp,并打印可直接粘进 JSON 的路径

批量:
    python add_image.py 目录/  → 目录下所有图片按原文件名归一化入库
"""

import sys
from pathlib import Path

if "--landscape" in sys.argv:
    sys.argv.remove("--landscape")
    _LANDSCAPE = True
else:
    _LANDSCAPE = False

from PIL import Image

TARGET_W, TARGET_H = 720, 960          # 3:4 竖图(卡片标准);横图素材加 --landscape
MAX_BYTES = 150 * 1024                 # 150KB
OUT_DIR = Path("lessons/images")


def normalize(src: Path, name: str) -> Path:
    global TARGET_W, TARGET_H
    if _LANDSCAPE and TARGET_W < TARGET_H:
        TARGET_W, TARGET_H = TARGET_H, TARGET_W
    img = Image.open(src).convert("RGB")

    # --- 居中裁剪到 4:3(只裁不拉伸,保证不变形) ---
    w, h = img.size
    target_ratio = TARGET_W / TARGET_H
    if w / h > target_ratio:            # 太宽 → 裁左右
        new_w = int(h * target_ratio)
        x = (w - new_w) // 2
        img = img.crop((x, 0, x + new_w, h))
    else:                               # 太高 → 裁上下
        new_h = int(w / target_ratio)
        y = (h - new_h) // 2
        img = img.crop((0, y, w, y + new_h))

    img = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)

    # --- 转 webp,质量从高到低试,压进 150KB 为止 ---
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{name}.webp"
    for quality in (85, 75, 65, 55, 45):
        img.save(out, "WEBP", quality=quality)
        if out.stat().st_size <= MAX_BYTES:
            break
    kb = out.stat().st_size // 1024
    print(f"  ✓ {out}  ({kb}KB, q={quality})")
    print(f'    JSON 里写: "image": "images/{name}.webp"')
    return out


def main():
    if len(sys.argv) < 2:
        print("用法: python add_image.py 原图.png [语义化名字]")
        print("      python add_image.py 图片目录/")
        sys.exit(1)

    src = Path(sys.argv[1])
    if src.is_dir():
        exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
        files = [f for f in sorted(src.iterdir()) if f.suffix.lower() in exts]
        print(f"批量入库 {len(files)} 张:")
        for f in files:
            normalize(f, f.stem.replace(" ", "-").lower())
    else:
        name = sys.argv[2] if len(sys.argv) > 2 else src.stem
        normalize(src, name.replace(" ", "-").lower())


if __name__ == "__main__":
    main()
