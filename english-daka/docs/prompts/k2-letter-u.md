# 配图 Prompt · Letter U · /ʌ/

共 4 张卡，出 3 张新图，bug 复用拼读课的图。

出图后按「存为」的名字命名，然后：

```bash
python ingest_images.py <图片目录>
```

文件名即入库名，也是卡片 `image` 字段的名字。

## 统一风格前缀（复制到每条 prompt 前面）

```
Children's picture book illustration, soft watercolor style with clean rounded
outlines, warm bright cheerful colors, simple uncluttered background, single
clear subject centered in frame, vertical 3:4 composition, friendly and cute,
suitable for a 5-year-old, NO text, NO letters, NO words, NO numbers, NO speech
bubbles, NO labels, NO borders or frames, NO panel dividers.
```

## 负面提示（工具支持的话）

```
text, letters, words, captions, labels, watermark, speech bubble, comic panels,
grid lines, borders, frame, collage of photos, realistic photo, scary, cluttered
```

## 复用现有图（不用出）

- `cvc-bug.webp` ← 拼读课 k2-cvc-u 的 bug 图（见 k2-cvc-u.md），字母课 bug 卡直接复用，两课同图

## 逐张 prompt

### `u-letter` — letter U

- **存为**：`u-letter.png`
- **画面必须能回答**：What's this letter?
- **对应句子**：It's letter U. / U makes the sound /ʌ/.
- ⚠️ 字母卡是唯一允许出现字母的图：前缀里的 NO letters 对这张不适用，但只许出现 U 和 u 两个字母。

```
A large friendly capital letter U and a smaller lowercase letter u, bright purple with a soft dotted watercolor texture, standing side by side on a clean pale cream background. The two letters together fill about 55% of the frame, same size ratio as the other K2 letter cards. Nothing else in the picture — no objects, no faces on the letters.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```

### `u-uncle` — uncle

- **存为**：`u-uncle.png`
- **画面必须能回答**：Which letter does uncle begin with?
- **对应句子**：Uncle begins with the sound /ʌ/. / /ʌ/ /ʌ/ /ʌ/, uncle.
- ⚠️ 不要给他拿伞——umbrella 是同一课的另一张卡，画上就撞了。

```
A friendly cheerful uncle — a grown man in his thirties with short brown hair, a warm smile, wearing a yellow sweater and jeans — standing and waving hello with one hand, in a sunny park with soft green grass. He is NOT holding anything (no umbrella, no bag). Single person, full body visible.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```

### `u-umbrella` — umbrella

- **存为**：`u-umbrella.png`
- **画面必须能回答**：Which letter does umbrella begin with?
- **对应句子**：Umbrella begins with the sound /ʌ/. / /ʌ/ /ʌ/ /ʌ/, umbrella.
- ⚠️ 不要有人、不要有虫子（uncle、bug 都是同课的卡）。

```
One big open umbrella with bright red and white panels and a curved wooden handle, standing alone on the ground with a few soft raindrops falling around it. No person, no animal, no insect. Just the umbrella, large and centered.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```
