# 配图 Prompt · Sight Words · what / do / you / see

共 4 张卡、7 张图：4 张常见词卡图 + see 卡下 3 张「What do you see?」递进场景图（一问一图）。

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

## 逐张 prompt

### `sw-what` — what

- **存为**：`sw-what.png`
- **画面必须能回答**：What's this sight word?
- **对应句子**：What do you see?

```
A curious little girl with pigtails, one hand raised to shade her eyes, leaning forward and looking far into the distance with a big wondering expression, as if asking what is out there. Plain soft sky-blue background, nothing else in the picture.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```

### `sw-do` — do

- **存为**：`sw-do.png`
- **画面必须能回答**：What's this sight word?
- **对应句子**：I do my homework.

```
A happy little boy sitting at a small wooden desk, holding a pencil and drawing on a blank sheet of paper, concentrating with a smile. Simple room background. The paper is blank — no writing on it.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```

### `sw-you` — you

- **存为**：`sw-you.png`
- **画面必须能回答**：What's this sight word?
- **对应句子**：I see you!

```
A giggling little girl playing peekaboo, peeking out from behind a big tree trunk with one eye showing and pointing one finger straight at the viewer, as if saying 'I see you'. Soft garden background.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```

### `sw-see` — see

- **存为**：`sw-see.png`
- **画面必须能回答**：What's this sight word?
- **对应句子**：I see a bird.

```
A little boy in a green cap looking through a pair of small toy binoculars, and a cute blue bird sitting on a nearby branch that he is looking at. Two clear subjects: the boy looking, the bird being seen. Soft park background.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```

### `sw-see-uncle` — see → uncle

- **存为**：`sw-see-uncle.png`
- **画面必须能回答**：What do you see?
- **对应句子**：I see my uncle.
- ⚠️ 三张 see 场景图是递进的：只有叔叔 → 叔叔打伞 → 伞上有虫。听句选图靠差异，第一张绝不能出现伞。

```
A friendly cheerful uncle — a grown man with short brown hair, glasses, a warm smile, wearing a blue shirt — standing and waving hello with one hand, in a sunny park. He holds NOTHING in his hands. No umbrella anywhere in the picture.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```

### `sw-see-umbrella` — see → umbrella

- **存为**：`sw-see-umbrella.png`
- **画面必须能回答**：What do you see?
- **对应句子**：I see my uncle's umbrella.
- ⚠️ 伞上绝不能有虫子，否则和下一张分不开。

```
The SAME friendly uncle (short brown hair, glasses, blue shirt) standing in light rain, holding one big open umbrella with bright yellow and white panels above his head, smiling. The umbrella is large and clearly the focus. The umbrella is completely clean — NO bug, NO insect, nothing sitting on it.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```

### `sw-see-bug` — see → bug

- **存为**：`sw-see-bug.png`
- **画面必须能回答**：What do you see?
- **对应句子**：I see a bug on my uncle's umbrella.
- ⚠️ 虫子要画得大、红、显眼，这张和上一张的唯一区别就是它。

```
The SAME friendly uncle (short brown hair, glasses, blue shirt) standing in light rain holding the same big open yellow-and-white umbrella — and ONE big cute red ladybug with black spots sitting right on top of the umbrella, drawn large and bright so it is instantly noticeable. The uncle looks up at the bug with a surprised smile.

Keep the main subject centered, fully visible, occupying roughly 60–75% of the frame, with modest breathing room above and below.
```
