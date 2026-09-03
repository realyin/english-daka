# 配图 Prompt · 课件词表补卡（32 张）

> **每条 prompt 都是完整的，复制整段直接用，不需要再拼风格前缀或负面词。**
> 「存为」就是文件名，也是入库后卡片里的 `image` 名，一名三用。

## 这批是什么

K2 课件的 `03 letters/` 里，**s / t / m / a 四课带「分类汇总」词表**（其余七课没有）。词表共 99 个词，**51 个已经做成卡了，48 个还没有**。

48 个里挑出 **32 个能一词一图的**。剩下 16 个不做卡：

| 不做的 | 为什么 |
|---|---|
| am / an / at / than / has / me / make / makes | 功能词，没有可画的主体 |
| today / times / missing / many / Merry / musical / taller | 抽象或形容词变形，画不出 |
| stop | 和 `k2-signs` 已有的 bus stop 卡重了 |

硬做只能标 `quiz:false` 挡在考一考外面 —— 那是例外，不该一次加 16 个。

## 出完图之后

```bash
python3 ingest_images.py <图片目录> --dry
python3 ingest_images.py <图片目录>
```

入库后我来建卡、写问答、跑 `gen_audio.py --backfill`、过 `check_lesson.py`。

⚠️ **每条都写了这张卡会问什么**，画面要对得上。首音/首字母的问法出自课件字母课原文（`What sound does X begin with?` / `Which letter does X begin with?`），答案一律落在 **K2 已学的 11 个字母/音**（s t m a n o f i r b d）之内 —— `clap`/`catch`/`happy`/`lamp` 的首字母 C/H/L 还没学到，所以只问中间音 /a/；`thank` 首音是 /θ/ 也没学，只问首字母 T。

⚠️ **同一课里的图必须互相分得开**。考一考让孩子听句子选图，一课里两张看着一样就成了送命题。letter s 这一课要一口气加 11 张，每张的主体都写明了。

---

## letter S（现 6 卡 → 17 卡）　`k2-letter-s`

### 1. `s-sandwich` — sandwich 三明治

**存为**：`s-sandwich.png`　／　**这张卡会问**：认物 + 首音 /s/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One triangular sandwich cut in half showing layers of bread, lettuce, tomato and cheese, resting on a small white plate. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 2. `s-snow` — snow 雪

**存为**：`s-snow.png`　／　**这张卡会问**：认物 + 首音 /s/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A quiet snowy scene: thick white snow covering the ground and a bare tree, large soft snowflakes drifting down from a pale winter sky, no people. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 3. `s-station` — station 车站

**存为**：`s-station.png`　／　**这张卡会问**：认物 + 首音 /s/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A small friendly train station platform with a clock on a post, a bench, and a green train waiting at the platform edge. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 4. `s-space` — space 太空

**存为**：`s-space.png`　／　**这张卡会问**：认物 + 首音 /s/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A deep purple-blue outer space scene with bright stars, a ringed planet and a small crescent moon, calm and wondrous, no astronaut. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 5. `s-say` — say 说

**存为**：`s-say.png`　／　**这张卡会问**：认物 + 首音 /s/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One happy child with an open mouth clearly saying something, one hand cupped beside the mouth, a few small curved sound arcs in the air. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 6. `s-see` — see 看见

**存为**：`s-see.png`　／　**这张卡会问**：认物 + 首音 /s/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child with wide bright eyes shading their brow with a flat hand and looking out into the distance at a colorful butterfly. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 7. `s-smart` — smart 聪明的

**存为**：`s-smart.png`　／　**这张卡会问**：认物 + 首音 /s/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One proud clever-looking child tapping their own temple with one finger and smiling knowingly, a glowing yellow lightbulb floating above their head. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 8. `s-sick` — sick 生病的

**存为**：`s-sick.png`　／　**这张卡会问**：认物 + 首音 /s/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child lying in bed under a blanket with a cooling cloth on the forehead and rosy flushed cheeks, looking unwell but calm, gentle and reassuring. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 9. `s-same` — same 相同的

**存为**：`s-same.png`　／　**这张卡会问**：认物 + 首音 /s/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two completely identical red apples sitting side by side on a plain surface, exactly the same size, shape and color, so their sameness is obvious. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 10. `s-sailor` — sailor 水手

**存为**：`s-sailor.png`　／　**这张卡会问**：认物 + 首音 /s/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One cheerful sailor in a white sailor uniform with a navy collar and a round white cap, standing and waving, a ship's wheel behind. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 11. `s-students` — students 学生

**存为**：`s-students.png`　／　**这张卡会问**：认物 + 首音 /s/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Three young students sitting at small desks in a bright classroom, each with an open book, all looking forward attentively and smiling. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## letter T（现 14 卡 → 23 卡）　`k2-letter-t`

### 12. `t-tomato` — tomato 西红柿

**存为**：`t-tomato.png`　／　**这张卡会问**：认物 + 首音 /t/ + 首字母 T

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One shiny round red tomato with a small green star-shaped stem on top, single fruit centered. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 13. `t-teeth` — teeth 牙齿

**存为**：`t-teeth.png`　／　**这张卡会问**：认物 + 首音 /t/ + 首字母 T

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child smiling widely to show a full row of clean white teeth, holding a toothbrush beside their cheek. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 14. `t-tooth` — tooth 牙齿（一颗）

**存为**：`t-tooth.png`　／　**这张卡会问**：认物 + 首音 /t/ + 首字母 T

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One single clean white tooth with a rounded crown and two small roots, floating alone on a plain background, clearly just one tooth. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 15. `t-truck` — truck 卡车

**存为**：`t-truck.png`　／　**这张卡会问**：认物 + 首音 /t/ + 首字母 T

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One bright red fire truck seen from the side with a ladder on top and round headlights, cheerful and toy-like. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 16. `t-toys` — toys 玩具

**存为**：`t-toys.png`　／　**这张卡会问**：认物 + 首音 /t/ + 首字母 T

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A cheerful pile of children's toys together: a teddy bear, a wooden block, a spinning top and a small ball, spread on a soft rug. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 17. `t-television` — television 电视

**存为**：`t-television.png`　／　**这张卡会问**：认物 + 首音 /t/ + 首字母 T

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One friendly rounded television set with a blank glowing screen, two small antennas on top and a chunky frame, standing on a low table. The screen is completely blank. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 18. `t-talk` — talk 说话

**存为**：`t-talk.png`　／　**这张卡会问**：认物 + 首音 /t/ + 首字母 T

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Two children facing each other and chatting happily, both with open mouths mid-conversation, hands gesturing. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 19. `t-tall` — tall 高的

**存为**：`t-tall.png`　／　**这张卡会问**：认物 + 首音 /t/ + 首字母 T

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One very tall giraffe standing beside a much shorter small rabbit, the enormous height difference obvious at a glance. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 20. `t-thank` — thank 感谢

**存为**：`t-thank.png`　／　**这张卡会问**：认物 + **只问首字母 T**（首音是 /th/，K2 还没学）

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One grateful child bowing slightly with both hands together in front of the chest, smiling warmly at someone off to the side. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## letter M（现 10 卡 → 13 卡）　`k2-letter-m`

### 21. `m-mittens` — mittens 手套

**存为**：`m-mittens.png`　／　**这张卡会问**：认物 + 首音 /m/ + 首字母 M

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One pair of cozy knitted red mittens lying side by side, joined by a woolly cord, soft winter texture. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 22. `m-money` — money 钱

**存为**：`m-money.png`　／　**这张卡会问**：认物 + 首音 /m/ + 首字母 M

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. A small pile of shiny gold and silver coins beside two folded paper banknotes, the banknotes showing only simple decorative patterns and no writing or figures. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 23. `m-music` — music 音乐

**存为**：`m-music.png`　／　**这张卡会问**：认物 + 首音 /m/ + 首字母 M

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Several colorful musical notes floating and dancing through the air above a small open songbook, cheerful and lively. The songbook pages are completely blank. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

## letter A（现 13 卡 → 22 卡）　`k2-letter-a`

### 24. `a-ant` — ant 蚂蚁

**存为**：`a-ant.png`　／　**这张卡会问**：认物 + 首音 /a/ + 首字母 A

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One friendly little black ant with a round head, big eyes and six legs, standing on a green leaf. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 25. `a-animal` — animal 动物（总称）

**存为**：`a-animal.png`　／　**这张卡会问**：认物 + 首音 /a/ + 首字母 A

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Four different cute animals standing together in a row facing the viewer — a dog, a cat, a rabbit and a bird — clearly a group of animals. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 26. `a-clap` — clap 拍手

**存为**：`a-clap.png`　／　**这张卡会问**：中间音 /a/（首字母 C 未学，不问）

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One joyful child clapping both hands together in front of the chest with a big smile, small motion arcs around the hands. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 27. `a-catch` — catch 抓住

**存为**：`a-catch.png`　／　**这张卡会问**：中间音 /a/（首字母 C 未学，不问）

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child leaning forward with both hands cupped open, just about to catch a bright yellow ball flying toward them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 28. `a-happy` — happy 开心的

**存为**：`a-happy.png`　／　**这张卡会问**：中间音 /a/（首字母 H 未学，不问）

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child laughing with a huge open smile and both arms thrown up in the air with joy. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 29. `a-lamp` — lamp 台灯

**存为**：`a-lamp.png`　／　**这张卡会问**：中间音 /a/（首字母 L 未学，不问）

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One warm desk lamp with a wide trapezoid-shaped shade glowing softly, standing on a small wooden table. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 30. `a-stand` — stand 站立

**存为**：`a-stand.png`　／　**这张卡会问**：中间音 /a/ + 首字母 S

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child standing straight and tall on both feet, arms relaxed at their sides, full body clearly visible. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 31. `a-fast` — fast 快的

**存为**：`a-fast.png`　／　**这张卡会问**：中间音 /a/ + 首字母 F

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One child running very fast with both arms pumping, hair blown back, with speed lines trailing behind them. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

### 32. `a-bag` — bag 包

**存为**：`a-bag.png`　／　**这张卡会问**：中间音 /a/ + 中字母 A + 首字母 B

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. One cheerful red school backpack with two shoulder straps and a front pocket, standing upright on the floor. NO text, NO letters, NO words, NO numbers, NO speech bubbles, NO labels, NO borders, NO frames, NO panel dividers, not scary, not cluttered.
```

---

## 加完之后的量

| 课 | 现在 | 加后 |
|---|---|---|
| letter S | 6 卡 12 问 | 17 卡 · 约 45 问 |
| letter T | 14 卡 37 问 | 23 卡 · 约 63 问 |
| letter M | 10 卡 25 问 | 13 卡 · 约 34 问 |
| letter A | 13 卡 34 问 | 22 卡 · 约 57 问 |

K2 合计 264 卡 855 问 → 约 **296 卡 940 问**。
