#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新课程脚手架
============
一条命令生成带示例卡片的课程 JSON 模板,照着改内容就行。
课程用课号标识(不用日期),文件名 = 课号-标题slug.json。

用法:
    python new_lesson.py 20 "One fewer than and zero"
    → 生成 lessons/20-one-fewer-than-and-zero.json

建课完整流程:
    1. python new_lesson.py <课号> "<标题>"     ← 生成模板
    2. 编辑 lessons/<日期>.json:替换示例卡片为真实内容
       - 普通单词卡:word/cn/emoji/dialog 必填,image 可选
       - 拼读卡:额外加 phonics 块,sound 用 lessons/phonics.json 里的 key
    3. (可选)配图: python add_image.py 原图.png 语义名
       → 把打印出的 "images/xxx.webp" 填进卡片的 image 字段
    4. python gen_audio.py lessons/<日期>.json  ← 生成音频+回写路径+更新目录
    5. (可选,拼读课)python gen_phonics.py --blends lessons/<日期>.json
       → 生成 "m→an→man" 串联音频(卡片里要先写好 blend_audio 路径)

卡片字段速查:
    word     单词/词条(可以带空格,如 "bus stop")
    cn       中文意思
    tag      标签:word / sight word / sign / CVC ...
    emoji    没配图时显示的 emoji
    image    可选,"images/xxx.webp"(用 add_image.py 入库)
    dialog   问答对列表:
      q / q_cn     问题及中文(童声播放)
      a / a_cn     回答句列表及中文(成人女声,可多句)
      key          语音答题的判分关键词(答案里必须说出的词,小写)
    phonics  可选,拼读面板:
      group        分组标题,相同 group 的卡片显示在一个分区下
      ipa          整词音标,如 "/mæn/"
      parts        逐字母:[{text:"m", sound:"m", kind:"consonant"},
                          {text:"a", sound:"ae", kind:"vowel"}, ...]
                   sound 必须是 lessons/phonics.json 里的 key;不发音的字母
                   (如 magic-e 的 e)不写 sound
      onset/rime   首音+韵尾:{text:"m", sound:"m"} / {text:"an", sound:"an"}
      blend_audio  "audio/phonics/blend-<word>.mp3"(--blends 会生成)
"""

import datetime
import json
import re
import sys
from pathlib import Path

LESSONS = Path(__file__).parent / "lessons"


def slug(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def template(num: int, title: str) -> dict:
    return {
        "num": num,
        "date": datetime.date.today().isoformat(),
        "title": title,
        "cards": [
            {
                "_示例": "普通单词卡 —— 改成你的内容后删掉这行",
                "word": "apple",
                "cn": "苹果",
                "tag": "word",
                "emoji": "🍎",
                "image": "",
                "dialog": [
                    {
                        "q": "What's this?",
                        "a": ["It's an apple."],
                        "key": ["apple"],
                        "q_cn": "这是什么？",
                        "a_cn": ["这是一个苹果。"]
                    },
                    {
                        "q": "What color is the apple?",
                        "a": ["It's red."],
                        "key": ["red"],
                        "q_cn": "苹果是什么颜色的？",
                        "a_cn": ["它是红色的。"]
                    }
                ]
            },
            {
                "_示例": "拼读卡(CVC)—— 不教拼读就整卡删掉;sound 用 phonics.json 里的 key",
                "word": "cat",
                "cn": "猫",
                "tag": "CVC",
                "emoji": "🐱",
                "phonics": {
                    "group": "短音 a /æ/ · -at 词族",
                    "ipa": "/kæt/",
                    "parts": [
                        {"text": "c", "sound": "k", "kind": "consonant"},
                        {"text": "a", "sound": "ae", "kind": "vowel"},
                        {"text": "t", "sound": "t", "kind": "consonant"}
                    ],
                    "onset": {"text": "c", "sound": "k"},
                    "rime": {"text": "at", "sound": "at"},
                    "blend_audio": "audio/phonics/blend-cat.mp3"
                },
                "dialog": [
                    {
                        "q": "What word is this?",
                        "a": ["It's cat."],
                        "key": ["cat"],
                        "q_cn": "这是什么单词？",
                        "a_cn": ["是 cat。"]
                    }
                ]
            }
        ]
    }


def main():
    if len(sys.argv) != 3 or not sys.argv[1].isdigit():
        print('用法: python new_lesson.py 20 "One fewer than and zero"')
        sys.exit(1)
    num, title = int(sys.argv[1]), sys.argv[2]
    lesson_id = f"{num}-{slug(title)}"
    out = LESSONS / f"{lesson_id}.json"
    if out.exists():
        print(f"❌ {out} 已存在,不覆盖")
        sys.exit(1)
    out.write_text(json.dumps(template(num, title), ensure_ascii=False, indent=2),
                   encoding="utf-8")
    print(f"✓ 已创建 {out}(第{num}课,含 2 张示例卡片)")
    print("""
接下来:
  1. 编辑这个文件,把示例卡片换成真实内容(删掉 "_示例" 行)
  2. 配图(可选): python add_image.py 原图.png 语义名
  3. 生成音频:   python gen_audio.py lessons/%s.json
     (会自动把课程加进目录页 index.json)
  4. 拼读课再跑: python gen_phonics.py --blends lessons/%s.json""" % (lesson_id, lesson_id))


if __name__ == "__main__":
    main()
