# 配图 Prompt · 规律课封面（6 张）

> **每条 prompt 都是完整的，复制整段直接用。**「存为」= 文件名 = 卡片里的 `image` 名。

## 为什么现在才做

你指出颜色 / 形状 / 规律三组的封面都是巨型汉字（「红黄蓝」「圆」「字母」）。

查下来 **颜色和形状那 7 课其实是有图的** —— 图挂在 `dialog[].image`（每问一图）而不是卡片上，我上一轮自动选封面时只看了 `card.image`，才把它们判成「无图」。已经直接改用它们自己的图，不用出：

```
k1-color-red    → 红苹果      k1-shape-circle → 披萨
k1-color-orange → 橙子        k1-shape-square → 吐司
k1-color-black  → 乌鸦        k1-shape-more   → 三角三明治
k1-color-pink   → 粉花
```

**真正缺图的只剩规律课 5 张**（整组一张图都没有）+ 数学 1 张。

⚠️ **卡片里的 CSS 渲染不动。** 规律条要画准重复序列，AI 画不准；这批只换目录页的封面，是装饰用途，不参与教学判分。

## 出完之后

```bash
python3 ingest_images.py <图片目录> --dry
python3 ingest_images.py <图片目录>
```

入库后我写 `cover` 字段（写在课程 JSON 顶层，不是 index.json —— 只写 index.json 的话下次跑 `gen_audio.py` 会被重建抹掉）。

---

## 规律 Patterns

五张统一用**一串穿好的珠子/方块横贯画面**，重复两轮以上，让「规律」这件事本身看得出来。靠珠子上是什么来区分五节课。

### 1. `k1-pattern-letter` — 字母规律 Letter Pattern

**存为**：`k1-pattern-letter.png`

⚠️ 这张的主体就是字母/数字，负面词里没有禁它们。

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old, subject centered and filling most of the frame. A long string of chunky wooden alphabet beads stretching across the picture, the same short run of three capital letters repeating over and over in the same order, each bead a different bright color, letters large and clearly readable. NO words, NO sentences, NO labels, NO borders, NO frames, not cluttered.
```

### 2. `k1-pattern-number` — 数字规律 Number Pattern

**存为**：`k1-pattern-number.png`

⚠️ 这张的主体就是字母/数字，负面词里没有禁它们。

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old, subject centered and filling most of the frame. A long string of chunky wooden number beads stretching across the picture, the same short run of numerals repeating over and over in the same order, each bead a different bright color, numerals large and clearly readable. NO words, NO sentences, NO labels, NO borders, NO frames, not cluttered.
```

### 3. `k1-pattern-color` — 颜色规律 Color Pattern

**存为**：`k1-pattern-color.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old, subject centered and filling most of the frame. A long string of round glossy beads stretching across the picture in a clear repeating color sequence — red, yellow, blue, red, yellow, blue — the repeat obvious at a glance, beads plain and unmarked. NO text, NO letters, NO words, NO numbers, NO labels, NO borders, NO frames, not cluttered.
```

### 4. `k1-pattern-shape` — 形状规律 Shape Pattern

**存为**：`k1-pattern-shape.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old, subject centered and filling most of the frame. A long row of flat colorful wooden shape tiles laid across the picture in a clear repeating sequence — circle, square, triangle, circle, square, triangle — the repeat obvious at a glance, tiles plain and unmarked. NO text, NO letters, NO words, NO numbers, NO labels, NO borders, NO frames, not cluttered.
```

### 5. `k1-pattern-symbol` — 符号规律 Symbol Pattern

**存为**：`k1-pattern-symbol.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old, subject centered and filling most of the frame. A long row of cute little fruit figures laid across the picture in a clear repeating sequence — banana, strawberry, orange, banana, strawberry, orange — the repeat obvious at a glance, each fruit simple and friendly. NO text, NO letters, NO words, NO numbers, NO labels, NO borders, NO frames, not cluttered.
```

## 数学 Math（可选）

这张的徽章是「−1」，不是汉字，没你说的那个问题。顺手补上就整套齐了，不想出也可以跳过。

### 6. `20-one-fewer-than-and-zero` — 比…少一和零 One Fewer & Zero

**存为**：`20-one-fewer-than-and-zero.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old, subject centered and filling most of the frame. A row of five red apples on a plain surface with one apple lifted away to the side by a child's hand, leaving four in the row — the idea of taking one away shown clearly, apples easy to count. NO text, NO letters, NO words, NO numbers, NO labels, NO borders, NO frames, not cluttered.
```

---

## 如果不想出图

你说的次选是「好看的英文」。那就把这 13 课的 `badge` 从汉字换成英文短标：

| 课 | 现在 | 换成 |
|---|---|---|
| `k1-pattern-letter` | 字母 | AB |
| `k1-pattern-number` | 数字 | 12 |
| `k1-pattern-color` | 颜色 | RGB |
| `k1-pattern-shape` | 形状 | ○□ |
| `k1-pattern-symbol` | 符号 | ★ |

说一声我就改，两分钟的事。但封面图肯定比字母缩写好看。
