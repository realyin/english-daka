# 配图 Prompt · 一问一图补齐（33 张）

> **每条 prompt 都是完整的，复制整段直接用。**「存为」= 文件名 = 卡片里的 `image` 名。

## 先说全站的账

**没有画面的句子：0 句。** 1271 问全都有画面可看。

| 画面来源 | 问数 |
|---|---|
| 自带图（`dialog[].image`） | 209 |
| 继承所在卡片的图 | 979 |
| CSS 规律条 / 字形 | 62 |
| CSS 算式 | 16 |
| emoji | 5 |

## 「重复用图」要分三种，只有一种该拆

课内共用同一张画面的问共 901 条，拆开看：

| 情形 | 问数 | 该不该各出一张 |
|---|---|---|
| **音标/拼读类**：`man` 卡的首音、中音、尾音、首字母…… | 604 | **不该。**问的都是同一个词，画八张 man 只会让考一考的听句选图彼此撞脸 |
| **答案相同**：「你会做什么→唱歌」和「你喜欢做什么→唱歌」 | 130 | **不该。**答案一样，画面本就该一样 |
| **答案不同却共用一张** | **96** | **该。**下面逐条处理 |

## 那 96 条里，真正要出图的是 33 张

| 情形 | 问数 | 处理 |
|---|---|---|
| K1 字母卡的「字母操」问（`Can you show me letter A?`） | 26 | **出图**，见 A 组 |
| K1 字母卡的「大小写」问（`Is it a big A or a small a?`） | 26 | **不出**。这一问就是看着卡上那个字形回答的，本来就该用同一张 |
| 回收课「这是什么」vs「该扔哪个箱」 | 10 | **出 5 张**（扔进箱子的画面），认物那一半用现有单品图 |
| 形状课的边数/角数 | 13 | **不出**。几何形状按项目约定走 CSS，AI 画不准边角数 |
| 数字课「哪个数字不见了 / 下一个是几」 | 3 | **不出**。要的是数字序列，该做成 `pattern` 卡（和 K1 字母排序卡同款），不是配图 |
| 拼读串联（`How do you sound out s, o, t?`） | 6 | **不出**。抽象音素拼合，没有可画的实物 |
| `k2-letter-o` 的 box / fox | 4 | **出 1 张**（fox on a box）；box 卡的「这是什么」改指向已有的 `rec-cardboard-box`（空纸箱） |
| `k1-instruments` 的 drums | 2 | **出 1 张**（鼓槌） |
| `k2-sw-on-the-go` 的 Easter egg | 2 | **不出**。「复活节说什么」改指向已有的 `k1-say-happy-easter`，跨课复用不冲突 |

出完这 33 张，**「答案不同却共用一张图」归零**。

---

# A 组 · 26 张「字母操」

K1 字母课每张卡的第二问是 `Can you show me letter A?` → `I can show you letter A.`，课件原文写的是「**说并做出对应字母的动作**」—— 用身体摆出字母的形状。现在这一问和「这是什么字母」共用同一张字母卡图，画面对不上这个动作。

⚠️ **画的是小朋友摆姿势，不是字母本身**。和同卡那张糖果质感的字母图要一眼分得开。

⚠️ 摆的是**哪个字形**必须和该课答案一致（下面逐张写明了，和现有字母卡同一个字形）。

### A1. `k1-pose-a` — 大写 A

**存为**：`k1-pose-a.png`　／　**这一问**：`Can you show me letter A?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing with both arms raised and pressed together above the head and both legs spread wide apart, forming a clear triangular A shape. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A2. `k1-pose-b` — 小写 b

**存为**：`k1-pose-b.png`　／　**这一问**：`Can you show me letter B?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing straight and tall with one arm curved forward from the waist to make a round belly shape at the lower half, forming a lowercase b. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A3. `k1-pose-c` — 大写 C

**存为**：`k1-pose-c.png`　／　**这一问**：`Can you show me letter C?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing sideways and curving the whole body, both arms reaching forward, forming an open C curve. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A4. `k1-pose-d` — 小写 d

**存为**：`k1-pose-d.png`　／　**这一问**：`Can you show me letter D?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing straight with one arm curved forward at the lower half on the opposite side, forming a lowercase d. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A5. `k1-pose-e` — 大写 E

**存为**：`k1-pose-e.png`　／　**这一问**：`Can you show me letter E?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing sideways with both arms held straight out forward, one at shoulder height and one at waist height, and one leg extended forward, forming an E. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A6. `k1-pose-f` — 小写 f

**存为**：`k1-pose-f.png`　／　**这一问**：`Can you show me letter F?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing on tiptoe with the upper body leaning and one arm curling over the head and the other arm straight out to the side, forming a lowercase f. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A7. `k1-pose-g` — 大写 G

**存为**：`k1-pose-g.png`　／　**这一问**：`Can you show me letter G?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: crouching in a rounded curve with one arm tucked inward across the chest, forming a G. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A8. `k1-pose-h` — 小写 h

**存为**：`k1-pose-h.png`　／　**这一问**：`Can you show me letter H?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing straight with one arm bent down and forward from shoulder height like an arch, forming a lowercase h. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A9. `k1-pose-i` — 大写 I

**存为**：`k1-pose-i.png`　／　**这一问**：`Can you show me letter I?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing perfectly straight and stiff with both arms held tight against the sides and feet together, forming a straight I. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A10. `k1-pose-j` — 小写 j

**存为**：`k1-pose-j.png`　／　**这一问**：`Can you show me letter J?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing straight with the lower body hooked to one side and one hand raised above the head with a finger pointing up like the dot, forming a lowercase j. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A11. `k1-pose-k` — 大写 K

**存为**：`k1-pose-k.png`　／　**这一问**：`Can you show me letter K?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing with one arm raised diagonally up and one leg kicked out diagonally down on the same side, forming a K. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A12. `k1-pose-l` — 小写 l

**存为**：`k1-pose-l.png`　／　**这一问**：`Can you show me letter L?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing perfectly straight and tall with both arms pressed to the sides, a single vertical line, forming a lowercase l. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A13. `k1-pose-m` — 小写 m

**存为**：`k1-pose-m.png`　／　**这一问**：`Can you show me letter M?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: crouching on hands and knees with both arms and both legs down making two arches side by side, forming a lowercase m. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A14. `k1-pose-n` — 大写 N

**存为**：`k1-pose-n.png`　／　**这一问**：`Can you show me letter N?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing with one arm raised straight up and the other arm reaching diagonally down across the body, forming an N. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A15. `k1-pose-o` — 小写 o

**存为**：`k1-pose-o.png`　／　**这一问**：`Can you show me letter O?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet. The child stands comfortably with feet shoulder-width apart, raises both arms above the head, curves both elbows naturally outward, and touches the fingertips together once above the head, creating one large clear oval around the head to form a lowercase o. Both arms connect naturally to the shoulders; no arms or hands in front of the chest. This must be a safe, easy pose that a real five-year-old can copy. Full body clearly visible from head to toe against a plain soft background. Happy expression. NO duplicated limbs, NO extra arms, NO extra hands, NO merged limbs, NO impossible joints, NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A16. `k1-pose-p` — 大写 P

**存为**：`k1-pose-p.png`　／　**这一问**：`Can you show me letter P?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing straight with one arm curved forward from the shoulder making a loop at the upper half, forming a P. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A17. `k1-pose-q` — 大写 Q

**存为**：`k1-pose-q.png`　／　**这一问**：`Can you show me letter Q?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet. The child balances safely on the left foot, raises both arms above the head, curves both elbows naturally outward, and touches the fingertips together once above the head, creating one large clear oval around the head. The right leg extends diagonally down and outward to the side like the short tail of an uppercase Q. Both arms connect naturally to the shoulders; no arms or hands in front of the chest. This must be a safe, easy pose that a real five-year-old can copy. Full body clearly visible from head to toe against a plain soft background. Happy expression. NO duplicated limbs, NO extra arms, NO extra hands, NO merged limbs, NO impossible joints, NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A18. `k1-pose-r` — 小写 r

**存为**：`k1-pose-r.png`　／　**这一问**：`Can you show me letter R?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing straight with one arm bent forward at shoulder height like a small hook, forming a lowercase r. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A19. `k1-pose-s` — 大写 S

**存为**：`k1-pose-s.png`　／　**这一问**：`Can you show me letter S?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing with the whole body curved into a wavy double curve, one arm curling up and the other curling down, forming an S. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A20. `k1-pose-t` — 小写 t

**存为**：`k1-pose-t.png`　／　**这一问**：`Can you show me letter T?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing straight with both arms held straight out sideways at chest height, forming a cross shape like a lowercase t. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A21. `k1-pose-u` — 大写 U

**存为**：`k1-pose-u.png`　／　**这一问**：`Can you show me letter U?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing with both arms raised straight up on either side and the body dipped low in the middle, forming a U. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A22. `k1-pose-v` — 大写 V

**存为**：`k1-pose-v.png`　／　**这一问**：`Can you show me letter V?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing with both arms raised straight up and spread wide apart in a V shape. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A23. `k1-pose-w` — 小写 w

**存为**：`k1-pose-w.png`　／　**这一问**：`Can you show me letter W?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: crouching low with both arms out to the sides and both knees bent, forming a zigzag w. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A24. `k1-pose-x` — 大写 X

**存为**：`k1-pose-x.png`　／　**这一问**：`Can you show me letter X?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing with both arms raised diagonally and both legs spread wide, arms and legs crossing to form an X. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A25. `k1-pose-y` — 小写 y

**存为**：`k1-pose-y.png`　／　**这一问**：`Can you show me letter Y?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing with both arms raised up in a V and one leg kicked out to the side below, forming a lowercase y. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

### A26. `k1-pose-z` — 大写 Z

**存为**：`k1-pose-z.png`　／　**这一问**：`Can you show me letter Z?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child with normal human anatomy, exactly two arms, two hands, two legs and two feet, every limb fully visible and connected naturally to the correct shoulder or hip, normal child limb proportions, clear natural elbows and knees, no hidden, duplicated, missing, merged, rubbery or stretched limbs, no dislocated shoulders or impossible joints, using their whole body to act out the shape of a letter: standing with one arm straight out at head height, body leaning diagonally, and one leg straight out at the bottom, forming a Z. Full body clearly visible from head to toe against a plain soft background, the body shape unmistakable. Playful gymnastics pose, happy expression. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO sentences, NO numbers, not scary, not cluttered.
```

---

# B 组 · 5 张「扔进哪个箱」

回收课每张物品卡有两问：`What's this item?`（答物品）和 `Where should it go?`（答箱子）。现在两问共用同一张单品图，第二问看不出分类结果。apple core / soda can / banana peel 三张已经是这个样式了，这 5 张补齐其余。

⚠️ **箱子颜色要固定**：纸类=蓝，塑料=黄。同课里孩子靠颜色区分。

### B1. `rec-newspaper-to-paper` — newspaper 报纸 → 纸类回收箱

**存为**：`rec-newspaper-to-paper.png`　／　**这一问**：Where should the newspaper go?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A folded newspaper being dropped by a hand into an open blue paper recycling bin already holding flattened paper and cardboard. The newspaper shows only gray printed lines and blocks, completely blank of readable writing. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### B2. `rec-bottle-to-plastic` — plastic bottle 塑料瓶 → 塑料回收箱

**存为**：`rec-bottle-to-plastic.png`　／　**这一问**：Where should the plastic bottle go?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A clear plastic drink bottle with a colored cap being dropped by a hand into an open yellow plastic recycling bin already holding other plastic bottles. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### B3. `rec-cardboard-to-paper` — cardboard box 纸箱 → 纸类回收箱

**存为**：`rec-cardboard-to-paper.png`　／　**这一问**：Where should the cardboard box go?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A flattened brown corrugated cardboard box being pushed by a hand into an open blue paper recycling bin already holding folded paper. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### B4. `rec-bag-to-plastic` — plastic bag 塑料袋 → 塑料回收箱

**存为**：`rec-bag-to-plastic.png`　／　**这一问**：Where should the plastic bag go?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A translucent light-blue plastic shopping bag being dropped by a hand into an open yellow plastic recycling bin already holding other plastic items. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### B5. `rec-cup-to-plastic` — rec cup 塑料杯 → 塑料回收箱

**存为**：`rec-cup-to-plastic.png`　／　**这一问**：Where should the plastic cup go?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A clear disposable plastic cup being dropped by a hand into an open yellow plastic recycling bin already holding other plastic items. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

---

# C 组 · 2 张零散

### C1. `o-fox-on-box` — fox on a box（`k2-letter-o` 的 fox 卡）

**存为**：`o-fox-on-box.png`　／　**这一问**：Where is the fox?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One orange fox sitting neatly on top of a closed brown cardboard box, clearly above and on the box, the box fully visible underneath. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### C2. `k1-drumsticks` — drumsticks 鼓槌（`k1-instruments` 的 drums 卡）

**存为**：`k1-drumsticks.png`　／　**这一问**：What do you need to play the drums?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One pair of wooden drumsticks lying crossed on a plain surface, smooth tapered tips, clearly just the two sticks and no drum. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

---

## 出完之后

```bash
python3 ingest_images.py <图片目录> --dry
python3 ingest_images.py <图片目录>
```

入库后我来挂 `dialog[].image`、跑 `gen_audio.py --backfill`、过 `check_lesson.py`，并把 box 卡和 Easter egg 卡改指向已有的那两张图。
