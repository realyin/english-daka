# 配图 Prompt · Short u · 短元音 u 拼读

共 4 张卡，出 3 张新图，tub 复用已有的 cvc-tub。

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

- `cvc-tub.webp` ← 已在库里（k2-cvc-eu 用的浴缸图），本课 tub 卡直接复用

## 逐张 prompt

### `cvc-hut` — hut

- **存为**：`cvc-hut.png`
- **画面必须能回答**：What word is this?
- **对应句子**：It's hut. / The hut is small.

```
A small cozy straw hut with a round thatched roof and a little wooden door, standing on green grass under a blue sky with one fluffy cloud. Simple, single building, nothing else around it.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```

### `cvc-bug` — bug

- **存为**：`cvc-bug.png`
- **画面必须能回答**：What word is this?
- **对应句子**：It's bug. / The bug is on a leaf.
- ⚠️ 这张图同时给字母课 k2-letter-u 的 bug 卡用。

```
One cute smiling red ladybug with black spots sitting on a big bright green leaf, large and centered, soft pale background. Only one bug, no other insects, no flowers.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```

### `cvc-nut` — nut

- **存为**：`cvc-nut.png`
- **画面必须能回答**：What word is this?
- **对应句子**：It's nut. / The squirrel has a nut.

```
A cute fluffy orange squirrel sitting up and holding one big brown acorn nut with both paws, the nut clearly visible and large, on a soft green background. Only one nut.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```
