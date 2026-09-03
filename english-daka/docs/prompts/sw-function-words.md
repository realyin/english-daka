# 配图 Prompt · 虚词卡补图（is / to / and / all）

拆 `k2-sw-here-is-to-and-all` 时，is/to/and/all 四张虚词卡临时用了课件的单元封面
拼图当配图 —— 孩子看到「is」配一张"飞行员+蓝圆+海滩"的杂烩，读不出任何词义。

按 `my / like / I / too` 的达标标准补：**一张演出例句的单场景图 + 一条描述这张图的
答句**。`on` 不用出（现有的"狐狸在箱上"达标）。

**存为名 = 现在占位的拼图名**，入库直接覆盖，JSON 不用改路径：

| 存为 | 词 | 描述句（入库后我会写进答句并生成音频） |
|---|---|---|
| `sw-is.png` | is | This is a cat. |
| `sw-to.png` | to | I go to school. |
| `sw-and.png` | and | I see a dog and a cat. |
| `sw-all.png` | all | The apples are all red. |

出图后：

```bash
python ingest_images.py <图片目录>
```

> 画面里**不要出现同一课其它卡片的东西**（听句选图的选项来自同课）：
> is 课里有 pilot/circle/summer，to-and 课里有 sing/drums/teacher/piano/market，
> all 课里有 birds/play —— 下面的画面主体都避开了，别改成这些。

---

## 每条 prompt 已含统一风格前缀，整块复制即可

### `sw-is.png` — This is a cat.

```
Children's picture book illustration, soft watercolor style with clean rounded
outlines, warm bright cheerful colors, simple uncluttered background, single
clear subject centered in frame, vertical 3:4 composition, friendly and cute,
suitable for a 5-year-old, NO text, NO letters, NO words, NO numbers, NO speech
bubbles, NO labels, NO borders or frames, NO panel dividers.

A cheerful young boy standing beside a fluffy gray cat, pointing at the cat
with one hand as if introducing it, the cat sitting calmly on the floor looking
up, warm cream background, just the boy and the one cat, nothing else.
```

### `sw-to.png` — I go to school.

```
Children's picture book illustration, soft watercolor style with clean rounded
outlines, warm bright cheerful colors, simple uncluttered background, single
clear subject centered in frame, vertical 3:4 composition, friendly and cute,
suitable for a 5-year-old, NO text, NO letters, NO words, NO numbers, NO speech
bubbles, NO labels, NO borders or frames, NO panel dividers.

A happy young child with a small backpack walking along a short path toward a
small friendly schoolhouse with a red roof in the near distance, morning
sunshine, the child seen from behind at three-quarter angle mid-step, a clear
sense of walking toward the building, no other people.
```

### `sw-and.png` — I see a dog and a cat.

```
Children's picture book illustration, soft watercolor style with clean rounded
outlines, warm bright cheerful colors, simple uncluttered background, single
clear subject centered in frame, vertical 3:4 composition, friendly and cute,
suitable for a 5-year-old, NO text, NO letters, NO words, NO numbers, NO speech
bubbles, NO labels, NO borders or frames, NO panel dividers.

A friendly golden puppy and a fluffy white cat sitting side by side as a pair,
touching shoulders, both facing forward with happy expressions, exactly one dog
and one cat, plain warm background, clearly two buddies together.
```

### `sw-all.png` — The apples are all red.

```
Children's picture book illustration, soft watercolor style with clean rounded
outlines, warm bright cheerful colors, simple uncluttered background, single
clear subject centered in frame, vertical 3:4 composition, friendly and cute,
suitable for a 5-year-old, NO text, NO letters, NO words, NO numbers, NO speech
bubbles, NO labels, NO borders or frames, NO panel dividers.

A woven basket completely full of shiny red apples, every single apple the same
bright red color, about eight apples clearly visible, basket centered on a
plain warm background, emphasizing that every apple looks the same.
```

## 负面提示（工具支持的话，每张都加）

```
text, letters, words, captions, labels, watermark, speech bubble, comic panels,
grid lines, borders, frame, collage of photos, multiple scenes, split image,
realistic photo, scary, cluttered
```

---

## 入库之后我要做的（记录在此备查）

1. `python ingest_images.py <目录>` —— 同名覆盖四张拼图
2. 四张虚词卡去掉 `collage: true`（不再是拼图）
3. 答句各补第二条描述句（上表）+ `a_cn`，跑 `gen_audio.py` 三课
   （k2-sw-here-is / k2-sw-to-and / k2-sw-all）
4. `check_lesson.py` 全绿 + 浏览器验证听句选图能用上这四张
