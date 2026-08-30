#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
音色试音间:一次生成所有候选音色的样品,听完挑两个
====================================================
用法:
    pip install edge-tts
    python try_voices.py
    → 生成 voice_samples/ 目录,每个音色两个文件(问句样品 + 答句样品)
    → 逐个播放试听,选定后改 gen_audio.py 顶部的 VOICE_Q / VOICE_A

挑选建议:VOICE_Q(提问角色)从"童声组"里挑,VOICE_A(回答/领读)从
"成人组"里挑发音最清晰标准的。
"""

import asyncio
from pathlib import Path

import edge_tts

# 试听文本:用真实课程内容,听感才作数
SAMPLE_Q = "What's this sign? Can we run on the street?"
SAMPLE_A = "It's the bus stop. We should get on the bus at the bus stop."

CANDIDATES = {
    # ---- 童声组(提问角色候选) ----
    "en-US-AnaNeural":     "美音小女孩(当前默认)",
    "en-GB-MaisieNeural":  "英音小女孩,更软糯",
    # ---- 成人组(回答/领读角色候选) ----
    "en-US-JennyNeural":   "美音女声,清晰亲切(当前默认)",
    "en-US-AriaNeural":    "美音女声,播音感",
    "en-US-EmmaNeural":    "美音女声,自然度高",
    "en-US-AvaNeural":     "美音女声,最新一代,非常自然",
    "en-US-MichelleNeural":"美音女声,温和",
    "en-GB-SoniaNeural":   "英音女声(想学英音可选)",
    "en-US-GuyNeural":     "美音男声(想要男声角色可选)",
}

RATE = "-15%"
OUT = Path("voice_samples")


async def main():
    OUT.mkdir(exist_ok=True)
    for voice, desc in CANDIDATES.items():
        for kind, text in (("q", SAMPLE_Q), ("a", SAMPLE_A)):
            out = OUT / f"{voice}_{kind}.mp3"
            if out.exists():
                continue
            await edge_tts.Communicate(text, voice, rate=RATE).save(str(out))
        print(f"✓ {voice:<24} {desc}")
    print(f"\n样品在 {OUT}/ 目录,Mac 上直接空格键预听。")
    print("选定后,改 gen_audio.py 顶部的 VOICE_Q 和 VOICE_A,")
    print("然后重跑 gen_audio.py —— 旧音色的文件不影响,新音色会全量重新生成。")


if __name__ == "__main__":
    asyncio.run(main())
