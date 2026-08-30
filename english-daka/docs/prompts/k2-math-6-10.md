# 配图 Prompt · Numbers · Six to Ten（补缺）

这一课叫 Six to Ten，但 **9 和 10 没有独立卡片**：六/七/八各有一张「红谷仓 + N 只小鸡」，
九和十被塞在一张 `math-nine-ten.webp` 里当聚合卡（`word` 是 "nine and ten"，
考一考问「Which one is nine and ten?」问不出题）。

而且那张图**画的根本不是九和十**——实测是 **10 只小鸡 + 10 个紫圆片**（上下各 5+5），
画面里没有任何一组是九。所以它切不出「九」那一格，只能补画。

出图后按「存为」那一列命名，然后：

```bash
python ingest_images.py <图片目录>
```

文件名即入库名，也是卡片 `image` 字段的名字，不需要编号对照表。

---

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

> ⚠️ 这一课是**数数课**，数量必须准。生成后**逐只点一遍**再入库——
> 画错数量的图比没有图更糟（孩子会数出和答案不一样的数）。

---

## A 组 · 必做：把聚合卡拆开

现有 `math-nine-ten.webp` 只能回答「十」那一问，「九」那一问没有画面。补这一张之后，
`nine and ten` 就能拆成 `nine` / `ten` 两张卡，考一考也能用。

### `math-nine-chips` — 九只小鸡配九个圆片

- **存为**：`math-nine-chips.png`
- **画面必须能回答**：How many chips can show nine chickens?
- **对应句子**：Nine chips can show nine chickens.
- **必须和 `math-nine-ten.webp` 同一套构图**（无谷仓、绿草地、蓝天白云、左鸡右圆片）

```
A wide green grassy meadow under a light blue sky with a few soft white clouds.
On the LEFT side: exactly NINE small fluffy white baby chickens with red combs
and orange feet, arranged in two neat rows — five chickens in the top row and
four chickens in the bottom row, all standing on the grass facing forward.
On the RIGHT side, clearly separated from the chickens: exactly NINE flat round
purple counting chips lying on the grass, arranged to match the chickens —
five chips in the top row and four chips in the bottom row, each chip lined up
with one chicken. Simple flat meadow, no barn, no fence, no other animals.
```

**核对点**：左边 5+4=9 只鸡，右边 5+4=9 个圆片，且**上下行与小鸡一一对齐**（这一课教的
就是一一对应）。

---

## B 组 · 可选：把九和十补成正经的数数卡

六/七/八都有一张「红谷仓 + N 只小鸡」的数数卡（`What's this number?` /
`How many chickens are there?`），九和十没有。补上这两张，这一课才名副其实。

> 这两张会带来**新卡片**，属于「教什么」的改动。要不要加由你定；
> 我不会自己加课文。

### `math-nine` — 九只小鸡

- **存为**：`math-nine.png`
- **画面必须能回答**：How many chickens are there?
- **构图照抄 `math-six` / `math-seven` / `math-eight`**

```
A red wooden barn with a white door frame and a small square window, standing
on a green grassy hill under a light blue sky with soft white clouds.
In front of the barn: exactly NINE small fluffy white baby chickens with red
combs, orange beaks and orange feet, standing on the grass in two neat rows —
five chickens in the front row and four chickens in the back row, all facing
forward, evenly spaced and clearly separated so each one is easy to count.
No other animals, no fence, no farmer.
```

### `math-ten` — 十只小鸡

- **存为**：`math-ten.png`
- **画面必须能回答**：How many chickens are there?

```
A red wooden barn with a white door frame and a small square window, standing
on a green grassy hill under a light blue sky with soft white clouds.
In front of the barn: exactly TEN small fluffy white baby chickens with red
combs, orange beaks and orange feet, standing on the grass in two neat rows of
five, all facing forward, evenly spaced and clearly separated so each one is
easy to count. No other animals, no fence, no farmer.
```

---

## 入库之后要做的

**A 组（只补了 `math-nine-chips`）：**

1. 把 `nine and ten` 这张卡拆成两张：
   - `nine` ← `images/math-nine-chips.webp`，留第 1 问（How many chips can show nine chickens?）
   - `ten` ← `images/math-nine-ten.webp`，留第 2 问（How many chips can show ten chickens?）
2. 顺手把 `math-nine-ten.webp` 改名成 `math-ten-chips.webp`（它画的是十，名字里带 nine 会误导）
3. 两张卡都**去掉** `quiz: false` —— 拆开之后「Which one is nine?」问得出来了
4. `python gen_audio.py lessons/k2-math-6-10.json`（补两张新卡的 `quiz_audio`）
5. `python check_lesson.py lessons/k2-math-6-10.json` 必须全绿

**B 组（还加了 `math-nine` / `math-ten`）：**

再加两张数数卡，问答照抄 `six` / `seven` / `eight` 的句式：

```jsonc
{ "word": "nine", "cn": "九", "tag": "number", "image": "images/math-nine.webp",
  "dialog": [
    { "q": "What's this number?", "a": ["It's number nine."], "key": ["nine"],
      "q_cn": "这是数字几？", "a_cn": ["这是数字九。"] },
    { "q": "How many chickens are there?", "a": ["There are nine chickens."],
      "key": ["nine"], "q_cn": "有几只小鸡？", "a_cn": ["有九只小鸡。"] }
  ]}
```

`ten` 同理。加完同样跑 `gen_audio.py` + `check_lesson.py`。
