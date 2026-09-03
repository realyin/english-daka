#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配图批量入库脚本
================
把生成好的图片（按编号命名,如 001.png）批量归一化入库到 lessons/images/。
编号 → 目标文件名的映射直接从 docs/配图Prompt清单.md 的表格里解析,
不用手工维护第二份对照表。

用法:
    python ingest_images.py generated-images/001-007          # 入库整个目录
    python ingest_images.py generated-images/001-007 --dry    # 只看会做什么,不写文件

支持的源文件命名:
    001.png / 001.jpg / 001.webp      → 按编号查表得到目标名
    zoo-gate.png                       → 直接用文件名作目标名(不查表)

入库后会打印哪些课程 JSON 引用了这些图,方便去浏览器验证。
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DOC = ROOT / "docs" / "配图Prompt清单.md"
IMAGES = ROOT / "lessons" / "images"
EXTS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}


def load_mapping() -> dict:
    """从 prompt 文档的 markdown 表格解析 编号 → 目标文件名"""
    if not DOC.exists():
        print(f"⚠ 找不到 {DOC},只能用文件名模式")
        return {}
    mapping = {}
    for line in DOC.read_text(encoding="utf-8").splitlines():
        # 形如: | 001 | zoo-gate | zoo 动物园 | prompt... |
        m = re.match(r"\|\s*(\d{3})\s*[★\s]*\|\s*([a-z0-9\-]+)\s*\|", line)
        if m:
            mapping[m.group(1)] = m.group(2)
    return mapping


def find_usage(name: str):
    """哪些课程 JSON 引用了 images/<name>.webp"""
    hits = []
    for lp in sorted((ROOT / "lessons").glob("*.json")):
        if lp.name in ("index.json", "phonics.json", "dictionary.json"):
            continue
        if f"images/{name}.webp" in lp.read_text(encoding="utf-8"):
            hits.append(lp.stem)
    return hits


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    if not args:
        print("用法: python ingest_images.py <图片目录> [--dry]")
        sys.exit(1)

    src = Path(args[0])
    if src.is_dir():
        files = sorted(f for f in src.iterdir() if f.suffix.lower() in EXTS)
    elif src.is_file() and src.suffix.lower() in EXTS:
        files = [src]                      # 补单张图时直接传文件路径
    else:
        print(f"❌ {src} 不是图片目录或图片文件")
        sys.exit(1)

    mapping = load_mapping()
    if not files:
        print(f"❌ {src} 里没有图片")
        sys.exit(1)

    print(f"从文档解析到 {len(mapping)} 条编号映射,待处理 {len(files)} 张图\n")
    done, skipped, used_by, overwrites = 0, [], {}, []
    for f in files:
        stem = f.stem
        if re.fullmatch(r"\d{3}", stem):              # 编号命名 → 查表
            name = mapping.get(stem)
            if not name:
                skipped.append((f.name, "文档里没有这个编号"))
                continue
            label = f"{stem} → {name}"
        else:                                          # 语义命名 → 直接用
            name = stem.lower().replace(" ", "-")
            label = name

        hits = find_usage(name)
        used_by[name] = hits
        overwrote = (IMAGES / f"{name}.webp").exists()
        if overwrote:
            overwrites.append(name)
        flag = "覆盖已有" if overwrote else "新增"
        note = f"（{flag}，被 {len(hits)} 节课引用）" if hits else f"（{flag}，⚠ 暂无课程引用）"
        if dry:
            print(f"  [预览] {label} {note}")
            continue
        # ui-* 是界面贴纸(透明底正方形),走 add_image.py 的 --sticker 支线:
        # 默认支线会 convert("RGB")+裁 3:4 —— 透明底变黑底、贴纸被切边
        cmd = [sys.executable, "add_image.py", str(f), name]
        if name.startswith("ui-"):
            cmd.insert(2, "--sticker")
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        ok = [l for l in r.stdout.splitlines() if "✓" in l]
        print(f"  {ok[0].strip() if ok else '✗ ' + label} {note}")
        done += 1

    if skipped:
        print("\n跳过:")
        for n, why in skipped:
            print(f"  - {n}: {why}")

    if not dry:
        print(f"\n完成:入库 {done} 张")
        lessons = sorted({l for hits in used_by.values() for l in hits})
        if lessons:
            print("受影响的课程（去浏览器验证）:")
            for l in lessons:
                print(f"  http://localhost:8123/app.html?lesson={l}")
        orphan = [n for n, h in used_by.items() if not h]
        if orphan:
            print(f"⚠ 这些图暂时没有课程引用,需要手动写进 JSON: {orphan}")
        if overwrites:
            print(f"\n⚠ 同名覆盖了 {len(overwrites)} 张已有图片: {overwrites}")
            print("  必须 bump sw.js 的 CACHE 版本号!媒体是 cache-first,不让号的话")
            print("  装过 PWA 的设备永远拿旧图 —— 强刷是新图、正常打开还是旧图,实测踩过")


if __name__ == "__main__":
    main()
