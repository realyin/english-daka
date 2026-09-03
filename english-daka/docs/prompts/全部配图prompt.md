# 配图 Prompt 总表 · 205 张

> **每条 prompt 都是完整的，复制整段直接用，不需要再拼风格前缀或负面词。**
> 「存为」就是文件名，也是入库后卡片里的 `image` 名，一名三用。

出完图全部丢进同一个目录，一次入库：

```bash
python3 ingest_images.py <图片目录> --dry     # 先看会入库成什么名
python3 ingest_images.py <图片目录>
```

| 组 | 张数 | 用途 |
|---|---|---|
| A · 字母卡 | 26 | K1 字母课现在是 CSS 字形，太简陋。字母是开篇 |
| B · 场所卡 | 5 | 新增的 farm / jungle / ocean / nest / pets 卡，目前无图 |
| C · 课程封面 | 12 | 目录页现在铺的是巨型中文徽章 |
| D · 回收物品 | 3 | 课件里有、还没做成卡的三样东西 |
| E · 一问一图 | 153 | 主体和卡片不是一回事的问，各配自己的图 |
| F · K2 组图标 | 6 | 补 K2 独有的 6 组，见文末 |

**E 组是重点。** 现在 1265 问里只有 56 问有自己的图，其余共用卡片那张。共用对大多数问是对的（问 man 的首音，配 man 的图就对），但有 178 问的主体和卡片不是一回事——lion 卡问「狮子住哪里→动物园」，画着狮子却答动物园。这 153 张就是补这个（另 25 张见文末「不出图的」）。

补齐后考一考的「听句选图」题从 **127 题涨到约 800 题**——那个题型只认自带图的问，现在整张卡多于一问又没单格图的，一题都出不来。

---

# A 组 · 26 张字母卡

⚠️ **这一组画的主体就是字母，所以负面词里没有 `NO letters`。**

⚠️ **每张只画一个字形**（要么大写要么小写，下面逐张写明了）。K1 要考「Is it a big A or a small a?」，画了大小写并排就答不出来了。

### A1. `k1-letter-a` — 大写 A + apple

**存为**：`k1-letter-a.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "A" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright green, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly apple at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "A" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A2. `k1-letter-b` — 小写 b + ball

**存为**：`k1-letter-b.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "b" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright blue, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly ball at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "b" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A3. `k1-letter-c` — 大写 C + cat

**存为**：`k1-letter-c.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "C" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright orange, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly cat at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "C" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A4. `k1-letter-d` — 小写 d + dog

**存为**：`k1-letter-d.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "d" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright purple, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly dog at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "d" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A5. `k1-letter-e` — 大写 E + elephant

**存为**：`k1-letter-e.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "E" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright red, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly elephant at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "E" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A6. `k1-letter-f` — 小写 f + fish

**存为**：`k1-letter-f.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "f" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright pink, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly fish at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "f" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A7. `k1-letter-g` — 大写 G + bunch of grapes

**存为**：`k1-letter-g.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "G" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright teal, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly bunch of grapes at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "G" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A8. `k1-letter-h` — 小写 h + hat

**存为**：`k1-letter-h.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "h" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright yellow, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly hat at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "h" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A9. `k1-letter-i` — 大写 I + ice cream cone

**存为**：`k1-letter-i.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "I" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright turquoise, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly ice cream cone at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "I" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A10. `k1-letter-j` — 小写 j + jar of jam

**存为**：`k1-letter-j.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "j" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright purple, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly jar of jam at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "j" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A11. `k1-letter-k` — 大写 K + kite

**存为**：`k1-letter-k.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "K" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright orange, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly kite at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "K" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A12. `k1-letter-l` — 小写 l + lion

**存为**：`k1-letter-l.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "l" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright green, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly lion at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "l" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A13. `k1-letter-m` — 小写 m + crescent moon

**存为**：`k1-letter-m.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "m" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright pink, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly crescent moon at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "m" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A14. `k1-letter-n` — 大写 N + bird nest

**存为**：`k1-letter-n.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "N" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright orange, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly bird nest at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "N" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A15. `k1-letter-o` — 小写 o + orange fruit

**存为**：`k1-letter-o.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "o" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright blue, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly orange fruit at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "o" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A16. `k1-letter-p` — 大写 P + penguin

**存为**：`k1-letter-p.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "P" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright red, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly penguin at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "P" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A17. `k1-letter-q` — 大写 Q + little queen with a crown

**存为**：`k1-letter-q.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "Q" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright purple, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly little queen with a crown at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "Q" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A18. `k1-letter-r` — 小写 r + rabbit

**存为**：`k1-letter-r.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "r" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright red, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly rabbit at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "r" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A19. `k1-letter-s` — 大写 S + sun

**存为**：`k1-letter-s.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "S" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright blue, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly sun at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "S" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A20. `k1-letter-t` — 小写 t + tiger

**存为**：`k1-letter-t.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "t" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright red, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly tiger at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "t" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A21. `k1-letter-u` — 大写 U + umbrella

**存为**：`k1-letter-u.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "U" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright green, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly umbrella at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "U" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A22. `k1-letter-v` — 大写 V + violin

**存为**：`k1-letter-v.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "V" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright orange, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly violin at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "V" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A23. `k1-letter-w` — 小写 w + watermelon slice

**存为**：`k1-letter-w.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "w" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright teal, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly watermelon slice at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "w" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A24. `k1-letter-x` — 大写 X + xylophone

**存为**：`k1-letter-x.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "X" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright purple, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly xylophone at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "X" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A25. `k1-letter-y` — 小写 y + yo-yo

**存为**：`k1-letter-y.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative lowercase letter "y" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright yellow, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly yo-yo at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "y" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

### A26. `k1-letter-z` — 大写 Z + zebra

**存为**：`k1-letter-z.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single large decorative capital letter "Z" as the main subject filling most of the frame: rounded candy-like 3D letterform in bright blue, glossy highlights and small polka dots on the letter surface, standing upright and perfectly legible. Beside the letter, one cute friendly zebra at about one third of the letter's height. Soft cream background with a few small pastel stars scattered around. The letter must be correctly shaped, correctly spelled and clearly readable as "Z" and nothing else. NO speech bubbles, NO labels, NO borders, NO frames, NO extra letters, NO words, NO sentences, NO numbers, not cluttered.
```

---

# B 组 · 5 张场所卡

⚠️ 这几张画的是**地方**不是动物，要和同课的动物卡明显区分——考一考的选项来自同一课，画重了孩子无从分辨。

### B1. `k1-place-farm` — 农场 farm

**存为**：`k1-place-farm.png` ／ **要能回答**：What's this place?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A wide sunny farm landscape: a big red barn with a white door on green rolling fields, a wooden fence along the front, a windmill in the distance, blue sky with fluffy clouds. Wide establishing view of the whole farm, no animals in the foreground. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### B2. `k1-place-jungle` — 丛林 jungle

**存为**：`k1-place-jungle.png` ／ **要能回答**：What's this place?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A lush green jungle scene: tall trees with broad leaves, hanging vines, thick ferns and tropical plants, a small stream winding through, warm sunlight filtering down through the canopy. Wide view of the jungle itself, no animals. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### B3. `k1-place-ocean` — 海洋 ocean

**存为**：`k1-place-ocean.png` ／ **要能回答**：What's this place?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A wide blue ocean scene: deep blue sea water with gentle rolling waves, sunlight sparkling on the surface, a clear horizon line and soft blue sky above, a few seagulls far away. Wide view of the open ocean, no fish or sea creatures. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### B4. `k1-place-nest` — 鸟巢 nest

**存为**：`k1-place-nest.png` ／ **要能回答**：What's this?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One empty round bird nest woven from small twigs and dry grass, resting on a tree branch with green leaves around it, three small pale blue eggs inside. Soft sky background. The nest is the clear main subject, no birds. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### B5. `k1-place-pets` — 宠物 pets

**存为**：`k1-place-pets.png` ／ **要能回答**：What are they?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Three cute pets sitting together side by side on a soft rug in a cozy home: a small golden hamster, a little green turtle, and a round glass fish bowl with one orange goldfish. Warm indoor background, all three clearly visible and evenly spaced. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

---

# C 组 · 12 张课程封面

封面卡是竖的但会 `object-fit: cover` 裁切，主体放中间；铺满不留白边；目录页一排卡片并列，靠颜色区分组，配色要鲜明。

### C1. `k1-cover-letters` — 字母 Letters

**存为**：`k1-cover-letters.png`

⚠️ 主体就是字母，负面词里保留了对数字和单词的禁止，但不禁字母。

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. A joyful pile of colorful rounded 3D toy alphabet letters stacked and scattered together, candy-like glossy surfaces in many bright colors, filling the entire frame edge to edge. NO words, NO sentences, NO numbers, NO labels, NO borders, NO frames, not cluttered.
```

### C2. `k1-cover-numbers` — 数字 Numbers

**存为**：`k1-cover-numbers.png`

⚠️ 主体就是数字，负面词里不禁数字。

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. Colorful rounded 3D toy numerals scattered together with a few wooden abacus beads, candy-like glossy surfaces, bright colors filling the entire frame edge to edge. NO text, NO letters, NO words, NO sentences, NO labels, NO borders, NO frames, not cluttered.
```

### C3. `k1-cover-colors` — 颜色 Colors

**存为**：`k1-cover-colors.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. An overturned artist's palette with seven bright paint colors flowing and swirling into each other, glossy wet paint, filling the entire frame edge to edge. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### C4. `k1-cover-animals` — 动物 Animals

**存为**：`k1-cover-animals.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. A cheerful crowd of cute animals peeking together toward the viewer — a cow, a monkey, a fish and a small bird — packed happily into the frame edge to edge. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### C5. `k1-cover-body` — 身体 Body

**存为**：`k1-cover-body.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. One happy young child standing with both arms flung wide open in a joyful pose, full body in frame, bright cheerful background filling the frame edge to edge. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### C6. `k1-cover-actions` — 动作 Actions

**存为**：`k1-cover-actions.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. Four children in energetic motion together — one running, one jumping, one singing, one painting — dynamic and lively, filling the frame edge to edge. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### C7. `k1-cover-jobs` — 职业 Jobs

**存为**：`k1-cover-jobs.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. Four friendly workers standing in a row facing the viewer — a policeman, a doctor, a pilot and an artist — each in their own uniform, filling the frame edge to edge. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### C8. `k1-cover-weather` — 天气 Weather

**存为**：`k1-cover-weather.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. One picture divided into four soft weather zones blending together — bright sun, falling rain, drifting snow, and blowing wind with leaves — filling the frame edge to edge. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### C9. `k1-cover-shapes` — 形状 Shapes

**存为**：`k1-cover-shapes.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. A tall tower built from colorful wooden geometric blocks — circles, squares, triangles and trapezoids — stacked playfully, filling the frame edge to edge. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### C10. `k1-cover-patterns` — 规律 Patterns

**存为**：`k1-cover-patterns.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. A long string of colorful round beads threaded in a clear repeating color sequence, curving across the whole picture, filling the frame edge to edge. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### C11. `k1-cover-instruments` — 乐器 Instruments

**存为**：`k1-cover-instruments.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. A cheerful group of musical instruments arranged together — an upright piano, a guitar, a violin and a drum — filling the frame edge to edge. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### C12. `k1-cover-holidays` — 节日 Holidays

**存为**：`k1-cover-holidays.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. A joyful festive collage in one scene — a decorated Christmas tree, a smiling jack-o-lantern, red paper lanterns and painted Easter eggs — filling the frame edge to edge. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

---

# D 组 · 3 张回收物品

⚠️ 同课已有 newspaper / soda can / plastic bottle / glass bottle / apple core / banana peel，**纸箱别画成报纸、塑料杯别画成塑料瓶**。

### D1. `rec-cardboard-box` — 纸箱 cardboard box

**存为**：`rec-cardboard-box.png` ／ **要能回答**：Where should the cardboard box go?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One empty brown corrugated cardboard box, flaps open at the top, standing upright, the ridged corrugated edge clearly visible on the open flap. Single box centered. It must read as a box, not as a newspaper or a bottle. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### D2. `rec-plastic-bag` — 塑料袋 plastic bag

**存为**：`rec-plastic-bag.png` ／ **要能回答**：Where should the plastic bag go?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One translucent light-blue plastic shopping bag with two loop handles, standing slightly puffed up and empty, soft glossy highlights showing thin plastic. Single bag centered. It must read as a bag, not as a bottle or a cup. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### D3. `rec-plastic-cup` — 塑料杯 plastic cup

**存为**：`rec-plastic-cup.png` ／ **要能回答**：Where should the plastic cup go?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One clear disposable plastic drinking cup, empty, wide at the top and narrower at the base, with a smooth ribbed rim, soft glossy highlights showing clear plastic. Single cup centered. Not a bottle, no cap, no straw, no lid. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

---

# E 组 · 153 张「一问一图」

按课程分。每条都写明了**属于哪一课的哪张卡的哪一问**——入库后我会把它挂到那一问的 `dialog[].image` 上。

⚠️ **同一课内的图必须互相分得开。** 考一考让孩子听句子选图，一课里两张图看着一样就成了送命题。农场那四张（牛/羊/鸡/马）背景都是农场，靠动物区分；动物园那七张同理。

## 动作 · 吃与喝　`k1-action-eat`

### E1. `k1-eat-apples`

卡片 `eat` ／ **要能回答**：What do you like to eat?

**存为**：`k1-eat-apples.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A happy young child sitting at a small table biting into a big shiny red apple, a bowl of more red apples beside them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E2. `k1-drink-milk`

卡片 `drink` ／ **要能回答**：What do you like to drink?

**存为**：`k1-drink-milk.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A happy young child holding a tall glass of white milk with both hands and drinking it, a milk carton standing on the table. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E3. `k1-drink-water`

卡片 `drink` ／ **要能回答**：What else can you drink?

**存为**：`k1-drink-water.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A happy young child drinking clear water from a glass, a glass pitcher of water on the table beside them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 动作 · 帮助与分享　`k1-action-help`

### E4. `k1-care-animals`

卡片 `care` ／ **要能回答**：What can you care for?

**存为**：`k1-care-animals.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A gentle young child kneeling on the grass and softly stroking a small puppy while a kitten leans against their knee. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E5. `k1-play-games`

卡片 `play` ／ **要能回答**：What do you like to play?

**存为**：`k1-play-games.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two happy children sitting cross-legged on a rug playing a colorful board game together, game pieces spread between them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 动物 · 鸟类　`k1-animal-birds`

### E6. `k1-bird-eagle-nest`

卡片 `eagle` ／ **要能回答**：Where does an eagle live?

**存为**：`k1-bird-eagle-nest.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One large brown eagle sitting inside a big twig nest built on a high rocky cliff ledge, blue sky behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E7. `k1-birds-fly`

卡片 `eagle` ／ **要能回答**：What can birds do?

**存为**：`k1-birds-fly.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Three colorful small birds flying together with wings spread wide across a bright blue sky with soft white clouds. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E8. `k1-bird-crow-nest`

卡片 `crow` ／ **要能回答**：Where does a crow live?

**存为**：`k1-bird-crow-nest.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One glossy black crow perched on the edge of a twig nest resting in the fork of a leafy tree branch. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E9. `k1-crow-is-bird`

卡片 `crow` ／ **要能回答**：What kind of animal is a crow?

**存为**：`k1-crow-is-bird.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One glossy black crow standing on a branch between a small brown sparrow and a gray pigeon, all three clearly birds with feathers and beaks. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E10. `k1-bird-owl-nest`

卡片 `owl` ／ **要能回答**：Where does an owl live?

**存为**：`k1-bird-owl-nest.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One round fluffy brown owl with big eyes sitting in a twig nest tucked inside a hollow in a tree trunk. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 动物 · 农场　`k1-animal-farm`

### E11. `k1-farm-cow`

卡片 `cow` ／ **要能回答**：Where does a cow live?

**存为**：`k1-farm-cow.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One black-and-white dairy cow standing on green grass in front of a red barn with a wooden fence, blue sky above. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E12. `k1-farm-sheep`

卡片 `sheep` ／ **要能回答**：Where does a sheep live?

**存为**：`k1-farm-sheep.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One fluffy white sheep standing in a green fenced pasture with a red barn in the background. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E13. `k1-farm-chicken`

卡片 `chicken` ／ **要能回答**：Where does a chicken live?

**存为**：`k1-farm-chicken.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One brown hen standing in a dusty farmyard beside a small wooden chicken coop, red barn behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E14. `k1-farm-horse`

卡片 `horse` ／ **要能回答**：Where does a horse live?

**存为**：`k1-farm-horse.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One brown horse standing in a green paddock behind a wooden rail fence, red barn in the background. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 动物 · 丛林　`k1-animal-jungle`

### E15. `k1-jungle-elephant`

卡片 `elephant` ／ **要能回答**：Where does an elephant live?

**存为**：`k1-jungle-elephant.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One big gray elephant walking among tall jungle trees with broad green leaves and hanging vines. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E16. `k1-jungle-hippo`

卡片 `hippo` ／ **要能回答**：Where does a hippo live?

**存为**：`k1-jungle-hippo.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One round gray hippo standing half in a jungle river, thick green tropical plants along both banks. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E17. `k1-jungle-monkey`

卡片 `monkey` ／ **要能回答**：Where does a monkey live?

**存为**：`k1-jungle-monkey.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One brown monkey hanging by an arm from a thick jungle vine among broad green leaves. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E18. `k1-jungle-leopard`

卡片 `leopard` ／ **要能回答**：Where does a leopard live?

**存为**：`k1-jungle-leopard.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One spotted leopard lying along a thick jungle tree branch surrounded by dense green leaves. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E19. `k1-leopard-jungle-animal`

卡片 `leopard` ／ **要能回答**：What kind of animal is a leopard?

**存为**：`k1-leopard-jungle-animal.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One spotted leopard walking through dense jungle undergrowth, with a monkey on a vine and a hippo in a river visible behind among the trees. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 动物 · 海洋　`k1-animal-ocean`

### E20. `k1-ocean-shark`

卡片 `shark` ／ **要能回答**：Where does a shark live?

**存为**：`k1-ocean-shark.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One gray shark swimming underwater in deep blue ocean, rays of sunlight streaming down from the surface above. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E21. `k1-ocean-dolphin`

卡片 `dolphin` ／ **要能回答**：Where does a dolphin live?

**存为**：`k1-ocean-dolphin.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One gray dolphin leaping up out of blue ocean waves with spray around it, open sea and sky behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E22. `k1-ocean-whale`

卡片 `whale` ／ **要能回答**：Where does a whale live?

**存为**：`k1-ocean-whale.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One huge blue whale swimming through deep blue ocean water with a spout of mist rising from its blowhole. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E23. `k1-whale-ocean-animal`

卡片 `whale` ／ **要能回答**：What kind of animal is a whale?

**存为**：`k1-whale-ocean-animal.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One big blue whale swimming in the deep ocean with a dolphin above it and a small orange fish nearby, all underwater. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 动物 · 宠物　`k1-animal-pets`

### E24. `k1-pet-hamster-cage`

卡片 `hamster` ／ **要能回答**：Where does a hamster live?

**存为**：`k1-pet-hamster-cage.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One small golden hamster inside a wire pet cage with soft bedding, a little running wheel and a food bowl. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E25. `k1-pet-turtle-tank`

卡片 `turtle` ／ **要能回答**：Where does a turtle live?

**存为**：`k1-pet-turtle-tank.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One small green turtle inside a glass tank with shallow water, a smooth basking rock and a green plant. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E26. `k1-pet-goldfish-tank`

卡片 `goldfish` ／ **要能回答**：Where does a goldfish live?

**存为**：`k1-pet-goldfish-tank.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One orange goldfish swimming inside a round glass fish tank with green water plants and colorful pebbles at the bottom. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 身体 · 手臂与手　`k1-body-arms`

### E27. `k1-two-arms`

卡片 `arms` ／ **要能回答**：How many arms do you have?

**存为**：`k1-two-arms.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One happy child standing and stretching both arms straight out to the sides, both arms fully visible. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E28. `k1-touch-arms`

卡片 `arms` ／ **要能回答**：Can you touch your arms?

**存为**：`k1-touch-arms.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One smiling child using the right hand to hold and touch the left upper arm. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E29. `k1-two-hands`

卡片 `hands` ／ **要能回答**：How many hands do you have?

**存为**：`k1-two-hands.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child holding up both open hands side by side at chest height, palms facing forward, fingers together. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E30. `k1-clap-hands`

卡片 `hands` ／ **要能回答**：Can you clap your hands?

**存为**：`k1-clap-hands.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One joyful child clapping both hands together in front of the chest, small motion lines around the hands. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E31. `k1-ten-fingers`

卡片 `fingers` ／ **要能回答**：How many fingers do you have?

**存为**：`k1-ten-fingers.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child holding up both hands with all ten fingers spread wide apart, palms forward. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 身体 · 眼睛与耳朵　`k1-body-eyes`

### E32. `k1-two-eyes`

卡片 `eyes` ／ **要能回答**：How many eyes do you have?

**存为**：`k1-two-eyes.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Close-up of one smiling child's face with both bright open eyes clearly visible and looking forward. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E33. `k1-see-with-eyes`

卡片 `eyes` ／ **要能回答**：What can you do with your eyes?

**存为**：`k1-see-with-eyes.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child shading their eyes with a flat hand and gazing out at a bright rainbow in the distance. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E34. `k1-two-ears`

卡片 `ears` ／ **要能回答**：How many ears do you have?

**存为**：`k1-two-ears.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child with hair tucked back, pointing with both index fingers at both ears, smiling. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E35. `k1-hear-with-ears`

卡片 `ears` ／ **要能回答**：What can you do with your ears?

**存为**：`k1-hear-with-ears.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child cupping a hand behind one ear and listening to a small songbird singing on a nearby branch. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 身体 · 头发与脸　`k1-body-hair`

### E36. `k1-black-hair`

卡片 `hair` ／ **要能回答**：What color is your hair?

**存为**：`k1-black-hair.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Head and shoulders of one smiling child with neat shiny black hair, the hair color clearly the focus. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E37. `k1-long-hair`

卡片 `hair` ／ **要能回答**：Do you have long hair or short hair?

**存为**：`k1-long-hair.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One smiling child with very long flowing hair falling well past the shoulders, turned slightly to show its length. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E38. `k1-touch-face`

卡片 `face` ／ **要能回答**：Can you touch your face?

**存为**：`k1-touch-face.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One smiling child gently placing both palms flat on their own cheeks. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 身体 · 头颈肩　`k1-body-head`

### E39. `k1-nod-head`

卡片 `head` ／ **要能回答**：Can you nod your head?

**存为**：`k1-nod-head.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One cheerful child nodding, head tipped forward with eyes closed and a smile, small curved motion arcs beside the head. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E40. `k1-short-neck`

卡片 `neck` ／ **要能回答**：Do you have a long neck or a short neck?

**存为**：`k1-short-neck.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child standing beside a tall giraffe and pointing at their own short neck, the giraffe's very long neck stretching up beside them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E41. `k1-two-shoulders`

卡片 `shoulders` ／ **要能回答**：How many shoulders do you have?

**存为**：`k1-two-shoulders.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child with both hands placed on their own two shoulders, elbows out, smiling. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 身体 · 腿脚　`k1-body-legs`

### E42. `k1-two-legs`

卡片 `legs` ／ **要能回答**：How many legs do you have?

**存为**：`k1-two-legs.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child standing upright, full body in frame, both legs clearly visible side by side. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E43. `k1-two-feet`

卡片 `feet` ／ **要能回答**：How many feet do you have?

**存为**：`k1-two-feet.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child sitting on the floor with both bare feet stretched forward toward the viewer. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E44. `k1-touch-feet`

卡片 `feet` ／ **要能回答**：Can you touch your feet?

**存为**：`k1-touch-feet.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child bending forward with straight legs and touching their own toes with both hands. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E45. `k1-ten-toes`

卡片 `toes` ／ **要能回答**：How many toes do you have?

**存为**：`k1-ten-toes.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Close view of one child's two bare feet with all ten toes spread and wiggling. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 身体 · 鼻子与嘴　`k1-body-nose`

### E46. `k1-smell-with-nose`

卡片 `nose` ／ **要能回答**：What can you do with your nose?

**存为**：`k1-smell-with-nose.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child leaning in with eyes closed and sniffing a big colorful flower, small scent swirls rising. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E47. `k1-touch-nose`

卡片 `nose` ／ **要能回答**：Can you touch your nose?

**存为**：`k1-touch-nose.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One smiling child touching the tip of their own nose with one index finger. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E48. `k1-eat-with-mouth`

卡片 `mouth` ／ **要能回答**：What can you do with your mouth?

**存为**：`k1-eat-with-mouth.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child taking a big bite of a sandwich with mouth wide open, cheeks full and happy. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E49. `k1-drink-with-mouth`

卡片 `mouth` ／ **要能回答**：What else can you do with your mouth?

**存为**：`k1-drink-with-mouth.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child drinking orange juice through a bendy straw from a tall cup, lips on the straw. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 颜色 · 黑白灰　`k1-color-black`

### E50. `k1-mix-gray`

卡片 `gray` ／ **要能回答**：Which two colors can make gray?

**存为**：`k1-mix-gray.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two thick paint blobs on a clean white palette, one black and one white, flowing together and blending into a clear gray swirl in the middle. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 颜色 · 橙绿紫　`k1-color-orange`

### E51. `k1-mix-orange`

卡片 `orange` ／ **要能回答**：Which two colors can make orange?

**存为**：`k1-mix-orange.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two thick paint blobs on a clean white palette, one red and one yellow, flowing together and blending into a clear orange swirl in the middle. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E52. `k1-mix-green`

卡片 `green` ／ **要能回答**：Which two colors can make green?

**存为**：`k1-mix-green.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two thick paint blobs on a clean white palette, one yellow and one blue, flowing together and blending into a clear green swirl in the middle. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E53. `k1-mix-purple`

卡片 `purple` ／ **要能回答**：Which two colors can make purple?

**存为**：`k1-mix-purple.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two thick paint blobs on a clean white palette, one red and one blue, flowing together and blending into a clear purple swirl in the middle. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 颜色 · 粉与棕　`k1-color-pink`

### E54. `k1-mix-pink`

卡片 `pink` ／ **要能回答**：Which two colors can make pink?

**存为**：`k1-mix-pink.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two thick paint blobs on a clean white palette, one red and one white, flowing together and blending into a clear pink swirl in the middle. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E55. `k1-mix-brown`

卡片 `brown` ／ **要能回答**：Which two colors can make brown?

**存为**：`k1-mix-brown.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two thick paint blobs on a clean white palette, one black and one yellow, flowing together and blending into a clear brown swirl in the middle. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 节日 · 圣诞节　`k1-holiday-christmas`

### E56. `k1-say-merry-christmas`

卡片 `Christmas` ／ **要能回答**：What do we say on Christmas?

**存为**：`k1-say-merry-christmas.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A family of four standing together beside a decorated Christmas tree, all smiling and waving cheerfully toward the viewer in a warm living room. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 节日 · 复活节　`k1-holiday-easter`

### E57. `k1-say-happy-easter`

卡片 `Easter` ／ **要能回答**：What do we say on Easter?

**存为**：`k1-say-happy-easter.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two children in soft pastel spring clothes standing in a green meadow waving cheerfully toward the viewer, painted eggs in the grass around them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 节日 · 万圣节　`k1-holiday-halloween`

### E58. `k1-say-happy-halloween`

卡片 `Halloween` ／ **要能回答**：What do we say on Halloween?

**存为**：`k1-say-happy-halloween.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two children in cute friendly costumes standing at a doorway waving cheerfully, a smiling carved pumpkin glowing beside them, warm and playful, absolutely not scary. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 节日 · 春节　`k1-holiday-spring-festival`

### E59. `k1-say-happy-new-year`

卡片 `Spring Festival` ／ **要能回答**：What do we say during Spring Festival?

**存为**：`k1-say-happy-new-year.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two children in red traditional Chinese outfits bowing with clasped hands in a New Year greeting, round red paper lanterns hanging above them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 节日 · 感恩节　`k1-holiday-thanksgiving`

### E60. `k1-say-happy-thanksgiving`

卡片 `Thanksgiving` ／ **要能回答**：What do we say on Thanksgiving?

**存为**：`k1-say-happy-thanksgiving.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A family seated around a Thanksgiving table with a roast turkey, everyone smiling and raising their hands in a warm greeting toward the viewer. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 乐器　`k1-instruments`

### E61. `k1-play-piano-hands`

卡片 `piano` ／ **要能回答**：Which body parts can you use to play the piano?

**存为**：`k1-play-piano-hands.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Close view of a child's two hands with fingers pressing down on the black and white keys of a piano keyboard. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E62. `k1-piano-black-white`

卡片 `piano` ／ **要能回答**：What color is a piano?

**存为**：`k1-piano-black-white.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One upright piano seen straight from the front, its glossy black body and the row of black and white keys clearly visible. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E63. `k1-play-guitar-hands`

卡片 `guitar` ／ **要能回答**：Which body parts can you use to play the guitar?

**存为**：`k1-play-guitar-hands.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A child's two hands on an acoustic guitar, the left hand pressing the strings on the neck and the right hand strumming over the sound hole. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E64. `k1-like-piano`

卡片 `guitar` ／ **要能回答**：Which musical instrument do you like?

**存为**：`k1-like-piano.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One happy child sitting on a piano bench at an upright piano, turning to smile brightly toward the viewer. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E65. `k1-play-violin-hands`

卡片 `violin` ／ **要能回答**：Which body parts can you use to play the violin?

**存为**：`k1-play-violin-hands.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A child's two hands playing a violin, the left hand pressing the fingerboard and the right hand drawing the bow across the strings. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E66. `k1-violin-bow`

卡片 `violin` ／ **要能回答**：What do you need to play the violin?

**存为**：`k1-violin-bow.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One wooden violin bow with pale horsehair lying alone on a soft cloth, the bow clearly the single subject, no violin. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E67. `k1-play-trumpet-mouth`

卡片 `trumpet` ／ **要能回答**：Which body parts can you use to play the trumpet?

**存为**：`k1-play-trumpet-mouth.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child blowing into a golden trumpet, lips pressed to the mouthpiece and both hands holding the valves, cheeks puffed. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E68. `k1-play-drums-hands`

卡片 `drums` ／ **要能回答**：Which body parts can you use to play the drums?

**存为**：`k1-play-drums-hands.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A child's two open hands beating down on the skin of a round drum, small motion lines above the hands. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 职业 · 医生护士　`k1-job-doctor`

### E69. `k1-doctor-help`

卡片 `doctor` ／ **要能回答**：What can doctors do?

**存为**：`k1-doctor-help.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A friendly doctor in a white coat listening to a smiling child's chest with a stethoscope in a bright clinic. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E70. `k1-nurse-care`

卡片 `nurse` ／ **要能回答**：What can nurses do?

**存为**：`k1-nurse-care.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A kind nurse in blue scrubs gently putting a bandage on a child's arm, the child smiling. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 职业 · 工程师画家　`k1-job-engineer`

### E71. `k1-engineer-house`

卡片 `engineer` ／ **要能回答**：What can engineers do?

**存为**：`k1-engineer-house.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. An engineer in a yellow hard hat holding a rolled building plan, standing in front of a half-built house with scaffolding. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E72. `k1-engineer-robot`

卡片 `engineer` ／ **要能回答**：What else can engineers do?

**存为**：`k1-engineer-robot.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. An engineer at a workbench using a screwdriver to assemble a small friendly robot, tools and gears on the bench. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E73. `k1-artist-draw`

卡片 `artist` ／ **要能回答**：What can artists do?

**存为**：`k1-artist-draw.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. An artist in a paint-spattered apron painting a colorful landscape picture on a standing easel, brush in hand. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 职业 · 飞行员宇航员　`k1-job-pilot`

### E74. `k1-pilot-fly`

卡片 `pilot` ／ **要能回答**：What can pilots do?

**存为**：`k1-pilot-fly.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A pilot in a blue uniform and cap sitting in an airplane cockpit with hands on the controls, clouds and sky through the windshield. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E75. `k1-astronaut-space`

卡片 `astronaut` ／ **要能回答**：What can astronauts do?

**存为**：`k1-astronaut-space.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. An astronaut in a white spacesuit floating weightless in outer space, stars and a colorful planet behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 职业 · 警察消防员　`k1-job-police`

### E76. `k1-police-catch`

卡片 `policeman` ／ **要能回答**：What can policemen do?

**存为**：`k1-police-catch.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A friendly policeman in uniform running forward and reaching out to catch a cartoon thief in a striped shirt and eye mask, playful and light-hearted, absolutely not scary. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E77. `k1-firefighter-fire`

卡片 `firefighter` ／ **要能回答**：What can firefighters do?

**存为**：`k1-firefighter-fire.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A firefighter in yellow gear and helmet spraying a strong jet of water from a hose onto a small orange fire, fire truck behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 数字 6–10　`k1-number-6-10`

### E78. `k1-five-years-old`

卡片 `ten` ／ **要能回答**：How old are you?

**存为**：`k1-five-years-old.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One happy child holding up one hand with five fingers spread wide, standing behind a birthday cake with lit candles. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 天气 · 冷热　`k1-weather-hot`

### E79. `k1-need-fan`

卡片 `hot` ／ **要能回答**：What do you need when you feel hot?

**存为**：`k1-need-fan.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child sitting in front of a spinning electric fan with hair blowing back, looking cool and relieved on a hot day. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E80. `k1-need-down-jacket`

卡片 `cold` ／ **要能回答**：What do you need to wear when you feel cold?

**存为**：`k1-need-down-jacket.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child bundled up in a thick puffy winter down jacket with the hood pulled up, snow falling around them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 天气 · 雨雪　`k1-weather-rainy`

### E81. `k1-rainy-umbrella`

卡片 `rainy` ／ **要能回答**：What do you need on rainy days?

**存为**：`k1-rainy-umbrella.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child holding a big bright umbrella overhead in falling rain, puddles on the wet ground around their feet. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E82. `k1-rainy-cool`

卡片 `rainy` ／ **要能回答**：How do you feel on rainy days?

**存为**：`k1-rainy-cool.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child in a light long-sleeved jacket standing in gentle rain, looking comfortable and refreshed, eyes closed and smiling. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E83. `k1-rainy-raincoat`

卡片 `rainy` ／ **要能回答**：What else do you need on rainy days?

**存为**：`k1-rainy-raincoat.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child wearing a bright yellow raincoat and rain boots, jumping and splashing in a puddle. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E84. `k1-snowy-snowman`

卡片 `snowy` ／ **要能回答**：What can you do on snowy days?

**存为**：`k1-snowy-snowman.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child kneeling in snow and rolling a big snowball to build a snowman, a half-finished snowman beside them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E85. `k1-snowy-cold`

卡片 `snowy` ／ **要能回答**：How do you feel on snowy days?

**存为**：`k1-snowy-cold.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child hugging themselves and shivering with rosy cheeks in heavy falling snow, a small puff of breath in the air. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E86. `k1-snowy-scarf`

卡片 `snowy` ／ **要能回答**：What do you need on snowy days?

**存为**：`k1-snowy-scarf.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child wrapping a long red knitted scarf around their neck outdoors while snow falls. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 天气 · 四季　`k1-weather-spring`

### E87. `k1-spring-flowers`

卡片 `spring` ／ **要能回答**：What can you see in spring?

**存为**：`k1-spring-flowers.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child standing in a green meadow filled with blooming pink and yellow spring flowers, butterflies nearby. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E88. `k1-spring-warm`

卡片 `spring` ／ **要能回答**：How do you feel in spring?

**存为**：`k1-spring-warm.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child in a light shirt smiling with arms open under a gentle spring sun, fresh green trees and blossom behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E89. `k1-spring-kite`

卡片 `spring` ／ **要能回答**：What can you do in spring?

**存为**：`k1-spring-kite.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child running across a green spring field flying a colorful diamond kite high on a string. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E90. `k1-summer-swimming`

卡片 `summer` ／ **要能回答**：What can you do in summer?

**存为**：`k1-summer-swimming.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child swimming in a bright blue outdoor pool with arms stroking through the water, sunny sky above. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E91. `k1-summer-hot`

卡片 `summer` ／ **要能回答**：How do you feel in summer?

**存为**：`k1-summer-hot.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child wiping their forehead and fanning themselves with a hand under a strong summer sun, looking hot. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E92. `k1-summer-icecream`

卡片 `summer` ／ **要能回答**：What else can you do in summer?

**存为**：`k1-summer-icecream.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child licking a tall colorful ice cream cone on a bright sunny summer day. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E93. `k1-fall-yellow-trees`

卡片 `fall` ／ **要能回答**：What can you see in fall?

**存为**：`k1-fall-yellow-trees.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child walking under a row of trees covered in golden yellow autumn leaves, leaves drifting down around them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E94. `k1-fall-cool`

卡片 `fall` ／ **要能回答**：How do you feel in fall?

**存为**：`k1-fall-cool.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child in a light knitted sweater standing among falling autumn leaves, looking comfortable and content. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E95. `k1-winter-scarf`

卡片 `winter` ／ **要能回答**：What do you need in winter?

**存为**：`k1-winter-scarf.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child pulling a thick woolly scarf snug around their neck in a snowy winter street. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E96. `k1-winter-cold`

卡片 `winter` ／ **要能回答**：How do you feel in winter?

**存为**：`k1-winter-cold.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child with rosy cheeks and hunched shoulders shivering in a white snowy winter landscape. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E97. `k1-winter-snowman`

卡片 `winter` ／ **要能回答**：What can you do in winter?

**存为**：`k1-winter-snowman.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child reaching up to press a carrot nose onto a finished snowman wearing a hat and scarf. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 天气 · 晴阴　`k1-weather-sunny`

### E98. `k1-sunny-icecream`

卡片 `sunny` ／ **要能回答**：What can you do on sunny days?

**存为**：`k1-sunny-icecream.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child holding and eating an ice cream cone under a bright yellow sun in a clear blue sky. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E99. `k1-sunny-hot`

卡片 `sunny` ／ **要能回答**：How do you feel on sunny days?

**存为**：`k1-sunny-hot.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child shading their eyes with one hand and wiping sweat from their forehead under a blazing sun. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E100. `k1-sunny-swim`

卡片 `sunny` ／ **要能回答**：What else can you do on sunny days?

**存为**：`k1-sunny-swim.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child jumping into a swimming pool with a big splash of water, bright sunshine overhead. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E101. `k1-cloudy-indoor`

卡片 `cloudy` ／ **要能回答**：What can you do on cloudy days?

**存为**：`k1-cloudy-indoor.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child sitting on the floor indoors building a tower of colorful toy blocks, a gray cloudy sky visible through the window. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E102. `k1-cloudy-cool`

卡片 `cloudy` ／ **要能回答**：How do you feel on cloudy days?

**存为**：`k1-cloudy-cool.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child in a light jacket walking outdoors under a soft gray cloudy sky, looking comfortable. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 天气 · 风与暴风　`k1-weather-windy`

### E103. `k1-windy-kite`

卡片 `windy` ／ **要能回答**：What can you do on windy days?

**存为**：`k1-windy-kite.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child flying a colorful kite high on a windy day, their hair and clothes blowing sideways in the wind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E104. `k1-windy-cool`

卡片 `windy` ／ **要能回答**：How do you feel on windy days?

**存为**：`k1-windy-cool.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child standing with arms open enjoying a strong breeze, leaves and hair swept sideways, smiling. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E105. `k1-stormy-indoor`

卡片 `stormy` ／ **要能回答**：What can you do on stormy days?

**存为**：`k1-stormy-indoor.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child curled up indoors reading a picture book while heavy rain lashes the window and a lightning flash lights the dark sky outside. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E106. `k1-stormy-hot`

卡片 `stormy` ／ **要能回答**：How do you feel on stormy days?

**存为**：`k1-stormy-hot.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child looking out of a window at a dark stormy sky while fanning themselves with a hand in a warm stuffy room. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 字母 A　`k2-letter-a`

### E107. `k2-a-apple-red`

卡片 `apple` ／ **要能回答**：What color is the apple?

**存为**：`k2-a-apple-red.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One shiny bright red apple with a small green leaf on the stem, single fruit centered, the red color clearly the focus. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E108. `k2-a-bat-fly`

卡片 `bat` ／ **要能回答**：Can the bat fly?

**存为**：`k2-a-bat-fly.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One small friendly brown bat flying with both wings spread wide against a deep blue night sky with a few stars, cute not scary. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E109. `k2-a-hat-pink`

卡片 `hat` ／ **要能回答**：What color is your hat?

**存为**：`k2-a-hat-pink.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One pink sun hat with a soft ribbon band, single hat centered, the pink color clearly the focus. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E110. `k2-four-fans`

卡片 `fan` ／ **要能回答**：How many fans are there?

**存为**：`k2-four-fans.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Four identical small electric table fans standing in a row, evenly spaced and easy to count, plain background. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E111. `k2-two-hands-plain`

卡片 `hand` ／ **要能回答**：How many hands do you have?

**存为**：`k2-two-hands-plain.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two open child's hands held up side by side, palms facing forward, fingers together, plain background. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E112. `k2-a-black-hair`

卡片 `hair` ／ **要能回答**：What color is your hair?

**存为**：`k2-a-black-hair.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Head and shoulders of one smiling child with shiny black hair, the hair color clearly the focus. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E113. `k2-a-police-catch`

卡片 `policeman` ／ **要能回答**：What can policemen do?

**存为**：`k2-a-police-catch.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A friendly policeman in uniform running forward to catch a cartoon thief in a striped shirt and eye mask, playful and light-hearted, absolutely not scary. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E114. `k2-a-fat-cat`

卡片 `cat` ／ **要能回答**：Do you have a fat cat?

**存为**：`k2-a-fat-cat.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One round chubby tabby cat sitting upright with a very plump belly, looking content, plain background. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 字母 M　`k2-letter-m`

### E115. `k2-four-fans` — **复用 E110，不用另出**

卡片 `fan` ／ 问句 `How many fans are there?`　和 E110 是同一句同一画面，同一张图挂两处即可。

### E116. `k2-m-mouse-gray`

卡片 `mouse` ／ **要能回答**：What color is the mouse?

**存为**：`k2-m-mouse-gray.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One small gray mouse with big round ears and a long thin tail sitting on a plain background, the gray color clearly the focus. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 字母 I　`k2-letter-i`

### E117. `k2-i-iguana-tail`

卡片 `iguana` ／ **要能回答**：Do iguanas have long tails?

**存为**：`k2-i-iguana-tail.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One green iguana resting on a branch with its very long banded tail curling far behind it, the length of the tail clearly the focus. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 字母 N　`k2-letter-n`

### E118. `k2-n-new-notebook`

卡片 `notebook` ／ **要能回答**：Is this a new notebook?

**存为**：`k2-n-new-notebook.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One brand-new spiral notebook lying closed with crisp clean edges and a plain bright cover, looking untouched. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E119. `k2-n-nice-notebook`

卡片 `notebook` ／ **要能回答**：Is this a nice notebook?

**存为**：`k2-n-nice-notebook.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One pretty notebook with a decorated floral patterned cover and a silky ribbon bookmark hanging from the pages. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 字母 R　`k2-letter-r`

### E120. `k2-r-sing-song`

卡片 `sing` ／ **要能回答**：Can you sing a song?

**存为**：`k2-r-sing-song.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One happy child standing and singing with mouth open wide and eyes closed, a few musical notes floating in the air around them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 字母 T　`k2-letter-t`

### E121. `k2-t-toast-square`

卡片 `toast` ／ **要能回答**：What shape is the toast like?

**存为**：`k2-t-toast-square.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One clearly square slice of golden toasted bread lying flat on a white plate, its four straight edges and square shape obvious. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 数学 1–5　`k2-math-1-5`

### E122. `k2-two-lions`

卡片 `lions` ／ **要能回答**：How many lions are there?

**存为**：`k2-two-lions.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two friendly cartoon lions sitting side by side, evenly spaced and easy to count, plain background. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E123. `k2-two-lions-chips`

卡片 `lions` ／ **要能回答**：How many chips can show two lions?

**存为**：`k2-two-lions-chips.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two friendly cartoon lions in the upper half and two round flat red counting chips laid side by side directly below them, one chip under each lion. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E124. `k2-four-apples`

卡片 `apples` ／ **要能回答**：How many apples are there?

**存为**：`k2-four-apples.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Four red apples in a row, evenly spaced and easy to count, plain background. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E125. `k2-four-apples-chips`

卡片 `apples` ／ **要能回答**：How many chips can show four apples?

**存为**：`k2-four-apples-chips.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Four red apples in a row in the upper half and four round flat red counting chips in a row directly below, one chip under each apple. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E126. `k2-two-hands-math`

卡片 `hands` ／ **要能回答**：How many hands do you have?

**存为**：`k2-two-hands-math.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two open child's hands held up side by side, palms forward, on a plain background, easy to count as two. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E127. `k2-two-hands-chips`

卡片 `hands` ／ **要能回答**：How many chips can show two hands?

**存为**：`k2-two-hands-chips.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two open child's hands side by side in the upper half and two round flat red counting chips laid side by side directly below, one chip under each hand. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 数学 6–10　`k2-math-6-10`

### E128. `k2-two-plus-three`

卡片 `two and three` ／ **要能回答**：I have two apples. You have three apples. How many apples altogether?

**存为**：`k2-two-plus-three.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two red apples grouped on the left and three red apples grouped on the right with a clear gap between the groups, five apples in total, plain background. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E129. `k2-five-plus-five`

卡片 `five and five` ／ **要能回答**：I have five fingers on this hand, and five on this hand. How many fingers altogether?

**存为**：`k2-five-plus-five.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two open child's hands side by side, each with five fingers spread wide apart, ten fingers in total and easy to count. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 科学 · 垃圾分类　`k2-recycling`

### E130. `k2-rec-apple-core-compost`

卡片 `apple core` ／ **要能回答**：Where should the apple core go?

**存为**：`k2-rec-apple-core-compost.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. An apple core being dropped by a hand into an open brown compost bin already holding vegetable peels and leaves. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E131. `k2-rec-can-metal-bin`

卡片 `soda can` ／ **要能回答**：Where should the soda can go?

**存为**：`k2-rec-can-metal-bin.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. An aluminium soda can being dropped by a hand into an open gray metal recycling bin holding other cans. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E132. `k2-rec-peel-compost`

卡片 `banana peel` ／ **要能回答**：Where should the banana peel go?

**存为**：`k2-rec-peel-compost.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A yellow banana peel being dropped by a hand into an open brown compost bin already holding vegetable peels and leaves. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 常见词 all　`k2-sw-all`

### E133. `k2-all-birds-wings`

卡片 `birds` ／ **要能回答**：Do all the birds have wings?

**存为**：`k2-all-birds-wings.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Four different birds standing in a row — a sparrow, a crow, an owl and a duck — each with both wings held open to show the wings clearly. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E134. `k2-all-birds-fly`

卡片 `birds` ／ **要能回答**：Can all the birds fly?

**存为**：`k2-all-birds-fly.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Four different birds all flying together across a bright blue sky, wings beating, seen from below. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E135. `k2-dad-running`

卡片 `questions` ／ **要能回答**：What is dad's hobby?

**存为**：`k2-dad-running.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A dad in sportswear and running shoes jogging along a sunny park path, arms swinging. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E136. `k2-mom-eating`

卡片 `questions` ／ **要能回答**：What is mom's hobby?

**存为**：`k2-mom-eating.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A mom sitting at a kitchen table happily eating a big bowl of noodles with chopsticks. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 常见词 on/the/go　`k2-sw-on-the-go`

### E137. `k2-season-summer`

卡片 `go` ／ **要能回答**：What's the season now?

**存为**：`k2-season-summer.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A bright summer beach scene with a striped sun umbrella, a beach ball on the sand and blue sea under a hot sun. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E138. `k2-fox-on-box`

卡片 `fox` ／ **要能回答**：Where's the fox?

**存为**：`k2-fox-on-box.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One orange fox sitting on top of a closed brown cardboard box, clearly above and on the box. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E139. `k2-cow-on-farm`

卡片 `cow` ／ **要能回答**：Where does the cow live?

**存为**：`k2-cow-on-farm.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One black-and-white cow standing on a green farm field with a red barn and wooden fence behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E140. `k2-book-on-table`

卡片 `book` ／ **要能回答**：Where is the book?

**存为**：`k2-book-on-table.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One closed picture book lying flat on top of a wooden table, clearly resting on the table surface. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E141. `k2-give-gifts`

卡片 `Christmas` ／ **要能回答**：What can we do on Christmas?

**存为**：`k2-give-gifts.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child handing a wrapped present with a ribbon to another child beside a decorated Christmas tree, both smiling. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E142. `k2-easter-clothes`

卡片 `Easter egg` ／ **要能回答**：What do we wear on Easter?

**存为**：`k2-easter-clothes.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child in a pastel Easter dress and a straw hat with flowers, spinning happily to show the outfit, plain soft background. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E143. `k2-say-thanksgiving`

卡片 `turkey` ／ **要能回答**：What do we say on Thanksgiving?

**存为**：`k2-say-thanksgiving.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A family seated around a Thanksgiving table with a roast turkey, everyone smiling and waving warmly toward the viewer. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 常见词 to/and　`k2-sw-to-and`

### E144. `k2-want-teacher`

卡片 `drums` ／ **要能回答**：What do you want to be?

**存为**：`k2-want-teacher.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child standing beside a blank blackboard holding a pointer and pretending to be a teacher, the blackboard completely empty. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E145. `k2-piano-bw`

卡片 `piano` ／ **要能回答**：What color is a piano?

**存为**：`k2-piano-bw.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One upright piano seen straight from the front, glossy black body and a long row of black and white keys clearly visible. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 词族 -an　`k2-wf-an`

### E146. `k2-an-birds-fly`

卡片 `birds` ／ **要能回答**：Can birds fly?

**存为**：`k2-an-birds-fly.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Several small birds flying together with wings spread across a bright blue sky with soft clouds. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## 主题 · 动物园　`k2-zoo`

### E147. `k2-zoo-camel`

卡片 `camel` ／ **要能回答**：Where does a camel live?

**存为**：`k2-zoo-camel.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One camel standing inside a zoo enclosure behind a low fence, a zoo path and a visitor bench visible behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E148. `k2-zoo-lion`

卡片 `lion` ／ **要能回答**：Where does a lion live?

**存为**：`k2-zoo-lion.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One lion resting on a rock inside a zoo enclosure behind a low fence, a zoo path and a visitor bench visible behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E149. `k2-zoo-gorilla`

卡片 `gorilla` ／ **要能回答**：Where does a gorilla live?

**存为**：`k2-zoo-gorilla.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One gorilla sitting inside a zoo enclosure behind a low fence, a zoo path and a visitor bench visible behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E150. `k2-zoo-rhino`

卡片 `rhino` ／ **要能回答**：Where does a rhino live?

**存为**：`k2-zoo-rhino.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One rhino standing inside a zoo enclosure behind a low fence, a zoo path and a visitor bench visible behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E151. `k2-zoo-alligator`

卡片 `alligator` ／ **要能回答**：Where does an alligator live?

**存为**：`k2-zoo-alligator.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One alligator lying beside a shallow pool inside a zoo enclosure behind a low fence, a zoo path visible behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E152. `k2-zoo-owl`

卡片 `owl` ／ **要能回答**：Where does an owl live?

**存为**：`k2-zoo-owl.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One owl perched on a branch inside a zoo aviary behind wire mesh, a zoo path and a visitor bench visible behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### E153. `k2-zoo-elephant`

卡片 `elephant` ／ **要能回答**：Where does an elephant live?

**存为**：`k2-zoo-elephant.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One elephant standing inside a zoo enclosure behind a low fence, a zoo path and a visitor bench visible behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

---

---

# F 组 · 6 张 K2 组图标（补）

目录页每条货架的标题前有一个圆形组图标（30×30 圆形裁切）。K1 那 12 组已经有了，K2 独有的这 6 组还缺，现在标题是光秃秃的文字，两级看着不一致。

⚠️ **会被裁成圆形**，主体一定要在正中间，四角的东西会被切掉。

| 存为 | 组 |
|---|---|
| `k2-cover-word-family.png` | 词族 Word Family |
| `k2-cover-phonics.png` | 拼读 Phonics |
| `k2-cover-sight-words.png` | 常见词 Sight Words |
| `k2-cover-topics.png` | 主题 Topics |
| `k2-cover-math.png` | 数学 Math |
| `k2-cover-science.png` | 科学 Science |

### F1. `k2-cover-word-family` — 词族 Word Family

**存为**：`k2-cover-word-family.png`

⚠️ 主体就是字母，负面词里不禁字母。

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. A cluster of colorful rounded 3D toy letters arranged so that several small groups share the same two-letter ending, the repeated endings tinted one bright color and the leading letters another, playful and clearly grouped. NO words, NO sentences, NO numbers, NO labels, NO borders, NO frames, not cluttered.
```

### F2. `k2-cover-phonics` — 拼读 Phonics

**存为**：`k2-cover-phonics.png`

⚠️ 主体就是字母，负面词里不禁字母。

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. Three colorful rounded 3D toy letters sliding toward each other and merging into one word block, with small motion arcs showing them blending together, candy-like glossy surfaces. NO words, NO sentences, NO numbers, NO labels, NO borders, NO frames, not cluttered.
```

### F3. `k2-cover-sight-words` — 常见词 Sight Words

**存为**：`k2-cover-sight-words.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. A child's hand pointing at a bright flash card held up in the air, with more blank colorful flash cards fanned out behind it, cheerful and inviting, all cards completely blank. NO text, NO letters, NO words, NO numbers, NO labels, NO borders, NO frames, not cluttered.
```

### F4. `k2-cover-topics` — 主题 Topics

**存为**：`k2-cover-topics.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. A cheerful town scene packed with everyday places side by side — a zoo gate, a bus stop, a market stall and a street corner — bright and busy, filling the frame edge to edge. NO text, NO letters, NO words, NO numbers, NO labels, NO borders, NO frames, not cluttered.
```

### F5. `k2-cover-math` — 数学 Math

**存为**：`k2-cover-math.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. A joyful pile of bright round counting chips, colorful wooden abacus beads and stacking rings spread across the whole picture, candy-like glossy surfaces. NO text, NO letters, NO words, NO numbers, NO labels, NO borders, NO frames, not cluttered.
```

### F6. `k2-cover-science` — 科学 Science

**存为**：`k2-cover-science.png`

```
Children's picture book illustration, soft watercolor style, bright saturated cheerful colors filling the entire frame edge to edge, no white margins, playful and inviting. Four brightly colored recycling bins standing in a row with a green compost pile beside them, a leafy plant and a bright sun above, fresh and cheerful. NO text, NO letters, NO words, NO numbers, NO labels, NO borders, NO frames, not cluttered.
```

---

# 不出图的 25 问（说明，不用管）

这些问也是「主体和卡片不是一回事」，但**不能交给 AI 画**，项目里一律用 CSS 渲染，任意尺寸都清晰、且画得准：

| 类型 | 问数 | 为什么 |
|---|---|---|
| 形状的边数角数（三角形几条边…） | 9 | 几何形状用 CSS 画，AI 画不准边角数 |
| 规律条（What comes next?） | 8 | 规律条是 `pattern` 字段渲染的彩色格子 |
| 数字序列（哪个数字不见了） | 3 | 同上，数字块 |
| 拼读串联（How do you sound out s, o, t?） | 5 | 抽象音素拼合，没有可画的实物 |

另有 16 张 `one fewer than` 算式卡，走 `eq` 字段的彩色数字块，也不出图。
