#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
拼读音素公共库生成脚本
======================
英语拼读的"纯音"是个有限集合:字母音 + 短/长元音 + CVC 韵尾。
这个脚本维护完整清单(INVENTORY),生成音频并输出全局音素库
lessons/phonics.json,前端全局加载,任何课程直接复用,
课程 JSON 里不再需要 phonics_audio / phonics_labels / phonics_cues。

生成手法(TTS 直接念音素名会念错,所以每个音都有配方):
  sustain   可持续纯音:念 "sss/shh" 这类拉长写法,整段可用
  initial   爆破音:念 "bah" 载体音节,只留起始 ~0.19s 并淡出
  first     短元音:念 "at/odd" 真词,切在尾塞音爆破前的闭塞静音处,留前半
  second    同上留后半(如从 "ox" 里取 /ks/)
  behead:N  斩头:从真词里去掉起始辅音 N 毫秒,留韵尾(如 kid → /ɪd/)
  asis      真词/可读音节直接用(仅去头尾静音)
候选按顺序尝试;若 TTS 把文本逐字母拼读(合成时长异常)自动换下一个。

用法:
    pip install edge-tts   (系统还需要 ffmpeg;校验需要 whisper)
    python gen_phonics.py                    # 生成全部缺失的音 + 写 phonics.json
    python gen_phonics.py --force            # 全部重新生成
    python gen_phonics.py ae an ute          # 只重做指定的音
    python gen_phonics.py --blends lessons/2026-08-30.json   # 重建某课的拼读串联
    python gen_phonics.py --verify-only      # 用 whisper 转录现有音频(仅供参考)

新课怎么用:卡片里写 phonics.parts/onset/rime,sound 用下面清单里的
key 即可,无需再生成任何东西;想要"m→an→man"串联音频就跑一次 --blends。
"""

import array
import asyncio
import json
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import edge_tts

VOICE = "en-US-JennyNeural"
RATE = "-30%"
SR = 24000                      # 与 edge-tts 输出一致
ROOT = Path(__file__).parent / "lessons"
OUT = ROOT / "audio" / "phonics"
LIB = ROOT / "phonics.json"

# ============================================================
# 音素总清单: key → (IPA, 中文提示(可空), [(模式, 合成文本), ...])
# ============================================================
INVENTORY = {
    # ---------- 辅音(字母音) ----------
    "b":  ("/b/",  "b：双唇轻碰后弹开，不加“呃”音", [("initial", "bah")]),
    "t":  ("/t/",  "t：舌尖轻弹，只留短促气流，不加“呃”音", [("initial", "tah")]),
    "p":  ("/p/",  "p：双唇送气后立刻收住，不加“呃”音", [("initial", "pah")]),
    "d":  ("/d/",  "d：舌尖轻碰后立刻收住，不加“呃”音", [("initial", "dah")]),
    "g":  ("/ɡ/",  "g：喉咙带声，短促收住，不加“呃”音", [("initial", "gah")]),
    "k":  ("/k/",  "c/k：只留短促送气声 /k/，不加“呃”音", [("initial", "kah")]),
    "j":  ("/dʒ/", "j：短促发 /dʒ/，马上收住，不加“呃”音", [("initial", "jah")]),
    "h":  ("/h/",  "h：轻轻哈气", [("initial", "hah")]),
    "l":  ("/l/",  "l：舌尖顶上齿后方，只发 /l/，不加“呃”音", [("initial", "lah")]),
    "m":  ("/m/",  "m：双唇闭合，连续发 /m/，不加“呃”音",
           [("sustain", "hmm"), ("initial", "mah")]),
    "n":  ("/n/",  "n：舌尖顶住，连续发 /n/，不加“呃”音",
           [("sustain", "nnn"), ("initial", "nah")]),
    "s":  ("/s/",  "s：像小蛇一样“丝—”", [("sustain", "sss"), ("initial", "sah")]),
    "f":  ("/f/",  "f：上齿轻碰下唇，只留摩擦声 /f/",
           [("sustain", "fff"), ("initial", "fah")]),
    "v":  ("/v/",  "v：上齿轻碰下唇，带声摩擦",
           [("sustain", "vvv"), ("initial", "vah")]),
    "z":  ("/z/",  "z：像小蜜蜂一样“兹—”",
           [("sustain", "zzz"), ("initial", "zah")]),
    "r":  ("/r/",  "r：舌头卷起不碰上颚，不加“呃”音", [("initial", "rah")]),
    "w":  ("/w/",  "w：嘴唇收圆再展开", [("initial", "wah")]),
    "y":  ("/j/",  "y：像快速说“呀”的开头", [("initial", "yah")]),
    "x":  ("/ks/", "x：先 /k/ 后 /s/，快速连成 /ks/", [("second", "ox")]),
    "qu": ("/kw/", "qu：/k/ 和 /w/ 快速连读", [("initial", "kwah")]),
    "ch": ("/tʃ/", "ch：像小火车“嚓”，短促收住", [("initial", "chah")]),
    "sh": ("/ʃ/",  "sh：食指放嘴边“嘘—”",
           [("sustain", "shh"), ("initial", "shah")]),
    "th": ("/θ/",  "th：舌尖轻咬在上下齿之间吹气", [("initial", "thah")]),
    # ---------- 短元音 ----------
    "ae": ("/æ/", "a：嘴巴张开，短促 /æ/", [("first", "at")]),
    "eh": ("/ɛ/", "e：短促 /ɛ/，像“诶”但更短", [("first", "Ed")]),
    "ih": ("/ɪ/", "i：短促 /ɪ/，嘴角放松", [("first", "it")]),
    "aa": ("/ɑ/", "o：美音短 /ɑ/，嘴巴张圆", [("first", "odd")]),
    "ah": ("/ʌ/", "u：短促 /ʌ/，像轻短的“啊”", [("first", "utt"), ("first", "ut")]),
    # ---------- 长元音(字母名) ----------
    "ay":  ("/eɪ/",  "a_e：a 说字母名 /eɪ/", [("first", "ate")]),
    "eye": ("/aɪ/",  "i_e：i 说字母名 /aɪ/", [("asis", "eye")]),
    "oh":  ("/oʊ/",  "o_e：o 说字母名 /oʊ/", [("asis", "oh")]),
    "yoo": ("/juː/", "u_e：u 说 /juː/", [("asis", "you")]),
    "ee":  ("/iː/",  "ee：e 说字母名 /iː/，嘴角咧开", [("first", "eat")]),
    # ---------- 韵尾: 短元音 a ----------
    "ab": ("/æb/", "", [("asis", "abb"), ("behead:150", "tab")]),
    "ad": ("/æd/", "", [("asis", "add")]),
    "ag": ("/æɡ/", "", [("asis", "agg"), ("behead:120", "bag")]),
    "am": ("/æm/", "", [("asis", "am"), ("behead:150", "ham")]),
    "an": ("/æn/", "", [("asis", "Ann")]),
    "ap": ("/æp/", "", [("asis", "app")]),
    "at": ("/æt/", "", [("asis", "at")]),
    "ax": ("/æks/", "", [("asis", "ax")]),
    # ---------- 韵尾: 短元音 e ----------
    "eb": ("/ɛb/", "", [("behead:150", "web")]),
    "ed": ("/ɛd/", "", [("asis", "ed")]),
    "eg": ("/ɛɡ/", "", [("asis", "egg")]),
    "em": ("/ɛm/", "", [("asis", "em"), ("behead:150", "hem")]),
    "en": ("/ɛn/", "", [("asis", "en"), ("behead:150", "hen")]),
    "ep": ("/ɛp/", "", [("behead:140", "pep")]),
    "et": ("/ɛt/", "", [("behead:140", "vet")]),
    "ex": ("/ɛks/", "", [("asis", "ex")]),
    # ---------- 韵尾: 短元音 i ----------
    "ib": ("/ɪb/", "", [("behead:120", "bib")]),
    "id": ("/ɪd/", "", [("behead:130", "kid")]),
    "ig": ("/ɪɡ/", "", [("behead:140", "big")]),
    "im": ("/ɪm/", "", [("behead:150", "him")]),
    "in": ("/ɪn/", "", [("asis", "in")]),
    "ip": ("/ɪp/", "", [("behead:120", "tip")]),
    "it": ("/ɪt/", "", [("asis", "it")]),
    "ix": ("/ɪks/", "", [("asis", "icks"), ("asis", "ix")]),
    # ---------- 韵尾: 短元音 o ----------
    "ob": ("/ɑb/", "", [("asis", "obb"), ("asis", "ob")]),
    "od": ("/ɑd/", "", [("asis", "odd")]),
    "og": ("/ɑɡ/", "", [("asis", "ogg"), ("asis", "og")]),
    "om": ("/ɑm/", "", [("behead:160", "mom")]),
    "on": ("/ɑn/", "", [("asis", "on")]),
    "op": ("/ɑp/", "", [("asis", "opp"), ("asis", "op")]),
    "ot": ("/ɑt/", "", [("asis", "ott"), ("asis", "ot")]),
    "ox": ("/ɑks/", "", [("asis", "ox")]),
    # ---------- 韵尾: 短元音 u ----------
    "ub": ("/ʌb/", "", [("asis", "ubb"), ("asis", "ub")]),
    "ud": ("/ʌd/", "", [("behead:140", "dud")]),
    "ug": ("/ʌɡ/", "", [("behead:120", "bug")]),
    "um": ("/ʌm/", "", [("asis", "um")]),
    "un": ("/ʌn/", "", [("asis", "un")]),
    "up": ("/ʌp/", "", [("asis", "up")]),
    "us": ("/ʌs/", "", [("asis", "us")]),
    "ut": ("/ʌt/", "", [("behead:150", "hut")]),
    # ---------- 韵尾: magic-e 长元音 ----------
    "ake": ("/eɪk/", "", [("asis", "ache")]),
    "ame": ("/eɪm/", "", [("asis", "aim")]),
    "ate": ("/eɪt/", "", [("asis", "ate")]),
    "ide": ("/aɪd/", "", [("behead:150", "hide")]),
    "ike": ("/aɪk/", "", [("behead:150", "hike")]),
    "ime": ("/aɪm/", "", [("behead:120", "time")]),
    "ine": ("/aɪn/", "", [("behead:150", "nine")]),
    "ite": ("/aɪt/", "", [("behead:150", "height")]),
    "ode": ("/oʊd/", "", [("asis", "ode")]),
    "oke": ("/oʊk/", "", [("asis", "oak")]),
    "one": ("/oʊn/", "", [("asis", "own")]),
    "ope": ("/oʊp/", "", [("behead:150", "hope")]),
    "ude": ("/uːd/", "", [("behead:170", "dude")]),
    "ute": ("/juːt/", "", [("asis", "yoot")]),
}

FRAME = SR // 100               # 10ms 分析窗
SIL_TH = 250                    # 16-bit RMS 静音阈值
SPELLED_DUR = 1.5               # 合成超过此秒数视为被逐字母拼读
ONSET_RATIO = 0.55              # 载体音节里能量达峰值这个比例 → 元音已经起头
CLIP_TAIL_MS = 40               # 靠爆破撑着的浊塞音:元音起头后留这么长的释放段
CLIP_TAIL_FRIC_MS = 20          # 自带送气/摩擦段的音(t/k/h/ch…):释放段更短


def run(cmd):
    subprocess.run(cmd, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def mp3_to_samples(mp3: Path) -> array.array:
    with tempfile.NamedTemporaryFile(suffix=".wav") as tf:
        run(["ffmpeg", "-y", "-i", str(mp3), "-ac", "1", "-ar", str(SR),
             "-sample_fmt", "s16", tf.name])
        with wave.open(tf.name) as w:
            data = array.array("h")
            data.frombytes(w.readframes(w.getnframes()))
    return data


def samples_to_mp3(samples: array.array, out: Path):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tf:
        with wave.open(tf.name, "w") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
            w.writeframes(samples.tobytes())
        run(["ffmpeg", "-y", "-i", tf.name, "-b:a", "48k", str(out)])
    Path(tf.name).unlink()


def rms(win) -> float:
    if not len(win): return 0.0
    return (sum(x * x for x in win) / len(win)) ** 0.5


def silence_map(s: array.array):
    return [rms(s[i:i + FRAME]) < SIL_TH for i in range(0, len(s), FRAME)]


def strip_edges(s: array.array, pad_ms=25) -> array.array:
    m = silence_map(s)
    try:
        first = m.index(False); last = len(m) - 1 - m[::-1].index(False)
    except ValueError:
        return s
    pad = pad_ms * SR // 1000
    a = max(0, first * FRAME - pad)
    b = min(len(s), (last + 1) * FRAME + pad)
    return s[a:b]


def internal_silences(s: array.array, min_ms=40):
    m = silence_map(s)
    runs, start = [], None
    for i, sil in enumerate(m):
        if sil and start is None: start = i
        if not sil and start is not None:
            runs.append((start, i)); start = None
    min_w = max(1, min_ms // 10)
    return [(a * FRAME, b * FRAME) for a, b in runs
            if b - a >= min_w and a > 0]


def vowel_onset(s: array.array) -> int:
    """载体音节(bah/dah/lah)里元音起头的位置(样本下标)。

    爆破/摩擦/流音本体的能量都明显低于后面的元音,所以取"首次达到全段峰值
    ONSET_RATIO"的那一帧;前 30ms 是爆破本身,不参与判定。找不到就退回 190ms。
    """
    env = [rms(s[i:i + FRAME]) for i in range(0, len(s), FRAME)]
    if not env:
        return len(s)
    th = max(env) * ONSET_RATIO
    for i, v in enumerate(env):
        if i >= 3 and v >= th:
            return i * FRAME
    return min(len(s), 190 * SR // 1000)


def fade(s: array.array, in_ms=5, out_ms=20) -> array.array:
    s = array.array("h", s)
    n_in = min(len(s), in_ms * SR // 1000)
    n_out = min(len(s), out_ms * SR // 1000)
    for i in range(n_in):
        s[i] = int(s[i] * i / n_in)
    for i in range(n_out):
        s[len(s) - 1 - i] = int(s[len(s) - 1 - i] * i / n_out)
    return s


def cut(mode: str, s: array.array) -> array.array:
    s = strip_edges(s)
    if mode.startswith("behead:"):              # 斩掉起始辅音 N 毫秒
        drop = int(mode.split(":")[1]) * SR // 1000
        return fade(s[drop:], in_ms=15)
    if mode == "initial":                       # 只留辅音本体,切在元音起头处
        onset = vowel_onset(s)
        # 送气/摩擦段够长的音本体已经听得清,少借元音;纯爆破音(b/d/g)只有
        # 二三十毫秒,得留一小段带声释放才听得见,全程淡出以免变成"呃"音
        tail = CLIP_TAIL_MS if onset < 100 * SR // 1000 else CLIP_TAIL_FRIC_MS
        return fade(s[:onset + tail * SR // 1000], out_ms=tail)
    if mode in ("first", "second"):
        sil = internal_silences(s)
        if sil:
            s = s[:sil[0][0]] if mode == "first" else s[sil[-1][1]:]
        elif mode == "first":                   # 找不到闭塞就掐掉尾部 35%
            s = s[:int(len(s) * 0.65)]
    if mode == "sustain" and len(s) > SR:       # 纯音最长 1s
        s = s[:SR]
    return fade(s)


async def synth(text: str, out: Path):
    await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(out))


async def gen_sound(key: str, attempts: list) -> str:
    for idx, (mode, text) in enumerate(attempts):
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tf:
            raw = Path(tf.name)
        await synth(text, raw)
        s = mp3_to_samples(raw)
        raw.unlink()
        # 被逐字母拼读时时长异常 → 换下一个候选
        if len(s) / SR > SPELLED_DUR and idx + 1 < len(attempts):
            continue
        samples_to_mp3(cut(mode, s), OUT / f"{key}.mp3")
        return f"[{mode:<10}] 文本={text!r}"
    return "!"


def write_library():
    lib = {
        "_comment": "拼读音素公共库,由 gen_phonics.py 生成/维护。课程卡片的 phonics.parts[].sound 直接用这里的 key。",
        "sounds": {
            key: {"ipa": ipa, **({"cue": cue} if cue else {}),
                  "audio": f"audio/phonics/{key}.mp3"}
            for key, (ipa, cue, _) in INVENTORY.items()
        },
    }
    LIB.write_text(json.dumps(lib, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    print(f"音素库已写入 {LIB}({len(lib['sounds'])} 个音)")


def build_blends(lesson_path: Path):
    lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
    gap = array.array("h", [0] * (350 * SR // 1000))
    gap2 = array.array("h", [0] * (500 * SR // 1000))
    n = 0
    for c in lesson["cards"]:
        p = c.get("phonics")
        if not p or not p.get("blend_audio"):
            continue
        onset = mp3_to_samples(OUT / f"{p['onset']['sound']}.mp3")
        rime = mp3_to_samples(OUT / f"{p['rime']['sound']}.mp3")
        word_rel = (lesson.get("word_audio") or {}).get(c["word"].lower())
        merged = array.array("h")
        merged.extend(onset); merged.extend(gap)
        merged.extend(rime); merged.extend(gap2)
        if word_rel and (ROOT / word_rel).exists():
            merged.extend(strip_edges(mp3_to_samples(ROOT / word_rel)))
        samples_to_mp3(merged, ROOT / p["blend_audio"])
        n += 1
    print(f"{lesson_path.name}: 拼读串联音频重建 {n} 个")


def verify(keys=None):
    files = sorted(OUT.glob("*.mp3"))
    files = [f for f in files if not f.stem.startswith("blend-")
             and (keys is None or f.stem in keys)]
    with tempfile.TemporaryDirectory() as td:
        for f in files:
            subprocess.run(["whisper", str(f), "--model", "base",
                            "--language", "en", "--output_format", "txt",
                            "--output_dir", td, "--verbose", "False",
                            "--temperature", "0"],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            txt = Path(td) / (f.stem + ".txt")
            heard = txt.read_text().strip().replace("\n", " ") if txt.exists() else ""
            print(f"  {f.stem:>5}  → {heard!r}")


async def main():
    args = sys.argv[1:]
    if "--verify-only" in args:
        verify(); return
    if "--blends" in args:
        build_blends(Path(args[args.index("--blends") + 1])); return

    OUT.mkdir(parents=True, exist_ok=True)
    force = "--force" in args
    only = {a for a in args if not a.startswith("-")}
    todo = [k for k in INVENTORY
            if (not only or k in only)
            and (force or bool(only) or not (OUT / f"{k}.mp3").exists())]

    for key in todo:
        info = await gen_sound(key, INVENTORY[key][2])
        print(f"  ✓ {key:>5}  {info}")
    if todo:
        print(f"共生成 {len(todo)} 个音")
    else:
        print("音频均已存在(--force 可全部重做)")

    write_library()
    if todo:
        print("\n--- whisper 校验(仅供参考,短片段转录不稳) ---")
        verify(set(todo))


if __name__ == "__main__":
    asyncio.run(main())
