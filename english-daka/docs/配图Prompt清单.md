# 配图 Prompt 清单

全部课程卡片的配图生成提示词。每条有唯一编号，出图后按编号回传即可批量入库。

**总计 116 条**：编号 001–089 为 **P1 必做**（现有图是裁坏的或看不清的文字海报），
090–116 为 **P2 可选**（现在没图，加了更好）。Signs 课的 4 张现有图合格，无需重做。

---

## 一、使用方法

1. **每条 prompt 前面都要加下面的「统一风格前缀」**，保证 88 张图画风一致。
2. 出图后按 **编号命名**保存（`001.png`、`002.png`…），或直接用「目标文件名」命名。
   丢给我一个目录，我用 `add_image.py` 批量归一化入库（3:4、720×960、webp ≤150KB）并改好 JSON。
3. 优先级：**P1 必做**（现在是裁坏的图或看不清的文字海报）→ **P2 可选**（现在没图，加了更好）。
4. 一次生成建议按课程分批（同一批风格更稳），不要 88 张混着出。

### 统一风格前缀（复制到每条 prompt 前面）

```
Children's picture book illustration, soft watercolor style with clean rounded
outlines, warm bright cheerful colors, simple uncluttered background, single
clear subject centered in frame, vertical 3:4 composition, friendly and cute,
suitable for a 5-year-old, NO text, NO letters, NO words, NO numbers, NO speech
bubbles, NO labels, NO borders or frames, NO panel dividers.
```

### 负面提示（如果工具支持 negative prompt）

```
text, letters, words, captions, labels, watermark, speech bubble, comic panels,
grid lines, borders, frame, collage of photos, realistic photo, scary, cluttered
```

### 风格标杆：照着这 4 张的样子出图

`lessons/images/` 下这四张是**现有素材里最合格的**，构图和画风就按它们来：

`street.webp`、`market.webp`、`bus-stop.webp`、`zoo.webp`

它们的共同点，也是新图要复制的：单一主体占满画面、3:4 竖构图、小女孩在画面一角
指着主体（有代入感）、背景干净不抢戏、水彩卡通画风、色彩明亮温暖。

**这 4 张不用重做**（Signs 课的路牌上有 STREET / MARKET 字样，但"认路牌"正是这节课
要教的内容，属于合理例外）。如果你的出图工具支持参考图（reference image / style
reference），直接把这几张喂进去，风格一致性会好很多。

### 三个例外与注意事项

- **字母卡（编号带 ★）允许出现那一个大写+小写字母**，因为字母本身就是教学内容。
  其余一切文字仍然禁止。
- **四格卡（标注「2×2」）**：一张图里 2×2 四个小场景，每格一个物体，**格与格之间不要分隔线、不要文字标签**。
  AI 很容易在格子里自动加英文单词，出图后请检查，有字就重出。
- 主体要**完整**（现在 camel 的头被切掉了就是反面教材），主体占画面 60% 以上，
  上下留白一点，因为入库时会居中裁成 3:4。

---

## 二、P1 必做（现有图有问题）

### 主题 · At the Zoo（k2-zoo）

| 编号 | 目标文件名 | 卡片 | Prompt（接在风格前缀后） |
|---|---|---|---|
| 001 | zoo-gate | zoo 动物园 | A cheerful zoo entrance gate made of wood and stone, with an arch, green trees and a blue sky behind it. A happy little girl in a green dress stands in front looking up excitedly. |
| 002 | camel | camel 骆驼 | One friendly camel with two humps standing in a sunny zoo enclosure, **full body visible including the head**, looking gently at the viewer, sandy ground and a wooden fence behind. |
| 003 | lion | lion 狮子 | One friendly male lion with a big fluffy golden mane, full body, sitting calmly on grass in a zoo enclosure, warm sunlight, gentle friendly expression, not scary. |
| 004 | gorilla | gorilla 大猩猩 | One friendly gorilla sitting on a rock in a green zoo enclosure, full body, calm and gentle expression, leafy plants around, not scary. |
| 005 | rhino | rhino 犀牛 | One friendly rhinoceros standing in a zoo enclosure, full body with the horn clearly visible, gentle expression, grass and a wooden fence behind. |
| 006 | alligator | alligator 短吻鳄 | One friendly cartoon alligator resting at the edge of a shallow pond in a zoo, full body, mouth closed, cute and harmless looking, green plants around. |
| 007 | owl | owl 猫头鹰 | One cute owl with big round eyes perched on a tree branch in a zoo aviary, full body, soft brown feathers, friendly expression, green leaves around. |

### 字母 · Letter S（k2-letter-s）

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 008 ★ | s-letter | letter S 字母 S | A large friendly capital letter S and lowercase letter s, drawn in bright blue with a soft dotted texture, floating on a clean pale background with a few small stars and sparkles. Only these two letters, nothing else written. |
| 009 | s-sea | sea 大海 | A calm beautiful blue sea with gentle waves, a sandy beach in the foreground, sunshine and a few soft white clouds, peaceful and inviting. |
| 010 | s-words | S words（2×2） | 2×2 grid of four separate cute scenes, no dividers and no labels: top-left a fluffy white sheep on grass; top-right a friendly green snake curled up; bottom-left a cheerful school building; bottom-right a smiling bright sun in a blue sky. |

### 字母 · Letter T（k2-letter-t）

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 011 ★ | t-letter | letter T 字母 T | A large friendly capital letter T and lowercase letter t in bright red with soft dotted texture, on a clean pale background with small stars. Beside them, one small yellow taxi car. Only these two letters, no other writing. |
| 012 | t-words-1 | T words（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a green turtle walking; top-right a slice of golden toast on a plate; bottom-left a child happily brushing their teeth; bottom-right two open hands showing ten fingers. |
| 013 | t-words-2 | T words around us（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a shiny golden trumpet; top-right a decorated Christmas tree; bottom-left a friendly teacher standing by a blackboard; bottom-right a small turtle inside a glass tank. |
| 014 | t-words-3 | more T words（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a bright orange triangle shape; top-right a child touching their own face with both hands; bottom-left a tall rectangle next to a shorter square; bottom-right a roast turkey on a Thanksgiving table. |

### 字母 · Letter M（k2-letter-m）

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 015 ★ | m-letter | letter M 字母 M | A large friendly capital letter M and lowercase letter m in bright purple with soft dotted texture, on a clean pale background with small hearts. Beside them, a warm smiling mother holding her child. Only these two letters, no other writing. |
| 016 | m-words-1 | M words（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a playful brown monkey hanging from a branch; top-right a small gray mouse; bottom-left a tall glass of white milk; bottom-right a close-up of a child's smiling open mouth. |
| 017 | m-words-2 | more M words（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a red paint blob and a yellow paint blob mixing into orange; top-right a colorful fruit market stall with apples and bananas; bottom-left a cozy Christmas scene with gifts; bottom-right four electric fans in a row. |

### 字母 · Letter A（k2-letter-a）

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 018 ★ | a-letter | letter A 字母 A | A large friendly capital letter A and lowercase letter a in bright green with soft dotted texture, on a clean pale background. Beside them, one shiny red apple. Only these two letters, no other writing. |
| 019 | a-words-1 | A words（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a shiny red apple; top-right a happy dolphin jumping out of blue water; bottom-left a friendly alligator; bottom-right a smiling astronaut in a white spacesuit. |
| 020 | a-words-2 | short A words（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a cute bat flying in a night sky; top-right a friendly dad standing and smiling; bottom-left a pink sun hat; bottom-right four electric fans in a row. |
| 021 | a-words-3 | more A words（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a child holding up two open hands; top-right a child with shiny black hair; bottom-left a friendly policeman; bottom-right a very fat happy orange cat. |

### 字母 · Letter N（k2-letter-n）

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 022 ★ | n-letter | letter N 字母 N | A large friendly capital letter N and lowercase letter n in bright orange with soft dotted texture, on a clean pale background. Beside them, one metal nail. Only these two letters, no other writing. |
| 023 | n-notebook | notebook 笔记本 | One clean new notebook with a colorful cover lying on a wooden desk, next to a pencil, bright and inviting. |
| 024 | n-nose-neck | nose and neck 鼻子和脖子 | A cheerful little girl in a green dress pointing at her own nose with one finger, her face and neck clearly visible, simple pale background. |
| 025 | n-need | need 需要（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left an electric fan blowing; top-right a colorful open umbrella in the rain; bottom-left a warm coat and scarf; bottom-right a child nodding their head happily. |
| 026 | n-nurse-nest | nurse and nest（2×2） | Two scenes side by side, no dividers and no labels: on the left a friendly nurse in a white uniform smiling; on the right a bird's nest in a tree with an eagle sitting in it. |

### 字母 · Letter O（k2-letter-o）

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 027 ★ | o-letter | letter O 字母 O | A large friendly capital letter O and lowercase letter o in bright orange with soft dotted texture, on a clean pale background. Beside them, one fresh orange fruit. Only these two letters, no other writing. |
| 028 | o-on | on 在……上面 | One open book lying on top of a wooden table in a cozy room, clearly showing that the book is ON the table. |
| 029 | o-box | box 盒子 | One cardboard box sitting on the floor with a cute orange fox peeking out from inside it, playful and funny. |
| 030 | o-clock | clock 时钟 | One round wall clock sitting on top of a fallen wooden log in a green forest clearing, sunny and cheerful. |
| 031 | o-fox | fox 狐狸 | One cute orange fox sitting on top of a cardboard box, full body, bushy tail, friendly expression, simple background. |
| 032 | o-mop | mop 拖把 | One cleaning mop with a wooden handle standing next to a bucket on a clean floor, simple and clear. |

### 字母 · Letter F（k2-letter-f）

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 033 ★ | f-letter | letter F 字母 F | A large friendly capital letter F and lowercase letter f in bright pink with soft dotted texture, on a clean pale background with sparkles. Beside them, a tiny cute fairy with wings. Only these two letters, no other writing. |
| 034 | f-fox | fox 狐狸 | One cute orange fox standing among tall green trees in a sunny forest, full body, bushy tail, friendly expression. |
| 035 | f-fun | fun 有趣 | A happy little girl laughing and jumping with joy, arms in the air, colorful confetti around her, very cheerful. |
| 036 | f-forest | forest 森林 | A beautiful green forest with tall trees, dappled sunlight coming through the leaves, a small path, peaceful and inviting. |
| 037 | f-face-fingers | face and fingers（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a smiling child's face; top-right two bare feet; bottom-left two open hands showing ten fingers; bottom-right five fingers held up on one hand. |
| 038 | f-fan-flower | fan and flower（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left an electric fan; top-right a colorful blooming flower; bottom-left a red barn on a green farm; bottom-right a small bird flying in a blue sky. |

### 字母 · Letter I（k2-letter-i）

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 039 ★ | i-letter | letter I 字母 I | A large friendly capital letter I and lowercase letter i in bright teal with soft dotted texture, on a clean pale background. Beside them, a small igloo made of snow blocks. Only these two letters, no other writing. |
| 040 | i-iguana | iguana 鬣蜥（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a friendly green iguana on a rock; top-right white eggs in a sandy nest; bottom-left green leafy plants; bottom-right a bright smiling sun in a blue sky. |

### 字母 · Letter R（k2-letter-r）

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 041 ★ | r-letter | letter R 字母 R | A large friendly capital letter R and lowercase letter r in bright red with soft dotted texture, on a clean pale background. Beside them, a cute raccoon with a striped tail. Only these two letters, no other writing. |
| 042 | r-sleep-can | sleep and can（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a child sleeping peacefully in bed at night with stars outside the window; top-right a child singing happily with a microphone; bottom-left a small crayfish; bottom-right a clear river flowing between green banks. |
| 043 | r-rat-ring | rat and ring（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a big tree with a round hollow opening in its trunk; top-right a city skyline with tall buildings; bottom-left a small gray rat; bottom-right a shiny golden ring with a gem. |

### 字母 · Letter B / D（k2-letter-b, k2-letter-d）

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 044 ★ | b-letter | letter B 字母 B | A large friendly capital letter B and lowercase letter b in bright blue with soft dotted texture, on a clean pale background. Beside them, one colorful bouncing ball. Only these two letters, no other writing. |
| 045 | b-ends | ends with b（2×2） | Three cute scenes arranged together, no dividers and no labels: a spider web sparkling with dew; a baby's cloth bib; a cute little bear cub sitting on grass. |
| 046 ★ | d-letter | letter D 字母 D | A large friendly capital letter D and lowercase letter d in bright green with soft dotted texture, on a clean pale background. Beside them, a happy dolphin jumping. Only these two letters, no other writing. |
| 047 | d-ends | ends with d（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a cozy bed with a pillow and blanket; top-right a friendly dog wagging its tail; bottom-left a cute green cartoon dinosaur; bottom-right a rag doll toy. |

### 常见词 Sight Words

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 048 | sw-my | my 我的 | A happy little girl in a green dress hugging her own favorite teddy bear close to her chest, clearly showing it belongs to her. |
| 049 | sw-like | like 喜欢 ⚠️**已作废，改看 165** | ~~A happy child holding an ice cream cone with both hands and smiling with delight, hearts floating around.~~ 这条出的图画成了「指着自己」，和 sw-i 撞了，需要重出——**重出条目在 165，不要用这一条**。 |
| 050 | sw-i | I 我 | A cheerful little girl in a green dress pointing at herself with her thumb, smiling proudly, simple pale background. |
| 051 | sw-too | too 也 | Two happy children side by side, both holding the same red balloon and smiling at each other, showing they both like it. |
| 052 | sw-go | go 去 | A happy child in a swimsuit running toward a blue swimming pool on a sunny summer day, full of energy. |
| 053 | sw-on | on 在……上 | A cute orange fox sitting on top of a cardboard box, clearly showing it is ON the box, simple background. |
| 054 | sw-on-farm | on the farm 在农场 | A friendly black and white cow standing on green grass on a farm, a red barn and blue sky behind. |
| 055 | sw-on-holiday | on Christmas 在节日里（2×2） | Three festive scenes together, no dividers and no labels: a decorated Christmas tree with gifts; colorful Easter eggs in a basket; a roast turkey on a Thanksgiving table. |
| 056 | sw-here | here 这里 | A little girl in a green dress waving and calling out, with a cute orange fox sitting right beside her feet, clearly nearby. |
| 057 | sw-is | is 是（2×2） | Three scenes together, no dividers and no labels: a friendly pilot in uniform waving from a plane cockpit; a solid blue circle shape; a sunny summer beach with a parasol. |
| 058 | sw-to | to 去；到（2×2） | Three scenes together, no dividers and no labels: a child singing into a microphone; a child playing a red drum set; a friendly teacher by a blackboard. |
| 059 | sw-and | and 和 | A grand piano with black and white keys on the left, and a basket of red apples and yellow bananas on the right, in one cheerful scene. |
| 060 | sw-all | all 所有 | Four colorful birds all flying together in a bright blue sky, and below them two happy boys playing football on green grass. |
| 061 | sw-from | from 从……来 | A cheerful little girl waving goodbye as she steps out of a house doorway, showing she is coming FROM the house. |
| 062 | sw-have | have 有 | A happy child holding up a big red apple in each hand, clearly showing that they have two apples. |
| 063 | sw-egg-hatch | egg and hatch（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a white egg in a nest; top-right a fluffy yellow chick hatching out of a cracked egg; bottom-left a small green seedling growing in soil; bottom-right a bright smiling sun. |

### 数学 Math

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 064 | math-one | one 一 | Exactly ONE cardboard box sitting alone on a wooden floor, and one single red round counting chip on the floor next to it. Clearly just one of each. |
| 065 | math-two | two 二 | Exactly TWO unicycles standing side by side on a wooden floor, one red and one blue, and two round counting chips (red and blue) on the floor below. Clearly just two of each. |
| 066 | math-three | three 三 | Exactly THREE toy cars in a row on a wooden floor — red, blue and yellow — and three round counting chips below them. Clearly just three of each. |
| 067 | math-four | four 四 | Exactly FOUR toys in a row on a wooden floor — a teddy bear, a robot, a doll and a rocket — and four round counting chips below them. Clearly just four of each. |
| 068 | math-five | five 五 | Exactly FIVE cute stuffed animal toys in a row — lion, panda, elephant, giraffe, rabbit — and five round counting chips below them. Clearly just five of each. |
| 069 | math-count | count 数一数 | A happy little girl holding up one open hand with all five fingers spread wide, counting, with five red round chips on the table in front of her. |
| 070 | math-chips | chips 圆片复习 | A row of five colorful round counting chips on a wooden table next to a group of five small toy animals, showing the two groups match in number. |
| 071 | math-six | six 六 | Exactly SIX fluffy white chickens standing on green grass in front of a red barn on a sunny farm. Clearly just six chickens. |
| 072 | math-seven | seven 七 | Exactly SEVEN fluffy white chickens standing on green grass in front of a red barn on a sunny farm. Clearly just seven chickens. |
| 073 | math-eight | eight 八 | Exactly EIGHT fluffy white chickens standing on green grass in front of a red barn on a sunny farm. Clearly just eight chickens. |
| 074 | math-nine-ten | nine and ten 九和十 | Ten fluffy white chickens on green grass on the left, and ten round purple counting chips arranged in two neat rows on the right, showing the two groups match. |
| 075 | math-fingers | ten fingers 十根手指 | A cheerful little girl holding up both hands with all ten fingers spread wide, smiling proudly, simple pale background. |
| 076 | math-altogether | altogether 一共 | Two red apples on the left and three red apples on the right, with all five apples together in a wicker basket below, showing two plus three makes five. |

### 科学 Science · Recycling

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 077 | recycling-bins | recycling bin 回收箱 | Four recycling bins standing in a row with recycling arrow symbols on them — blue, green, orange and purple — on green grass under a blue sky. Only the recycling arrow symbol, no written words. |
| 078 | recycling-paper-metal | paper and metal | A blue recycling bin on the left with newspapers and a cardboard box beside it, and a green recycling bin on the right with a soda can and a tin can beside it. Recycling arrow symbols only, no written words. |
| 079 | recycling-plastic-glass | plastic and glass | An orange recycling bin with a plastic bottle and plastic cup beside it, a purple recycling bin with glass bottles beside it, and a wooden compost box with an apple core. Recycling arrow symbols only, no written words. |
| 080 | recycling-sort | sort it out 分一分（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a newspaper next to a blue bin; top-right a soda can next to a green bin; bottom-left a plastic bottle next to an orange bin; bottom-right a banana peel next to a wooden compost box. |

### 词族 Word Family

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 081 | wf-an-1 | -an family（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a friendly grown-up man standing; top-right an electric fan; bottom-left a light-brown tan puppy dog; bottom-right a metal food can. |
| 082 | wf-an-2 | man fan tan can | A friendly dad standing beside a light-brown tan dog, with an electric fan on a table next to them in a cozy living room. |
| 083 | wf-it | -it family | Three scenes together, no dividers and no labels: a boy hitting a ball with a bat; a girl eating a small bite of cake; a glowing lit table lamp. |
| 084 | wf-at | -at family | Three scenes together, no dividers and no labels: a cute bat flying in a night sky; a small gray rat; a straw sun hat. |
| 085 | wf-ot | -ot family | Three scenes together, no dividers and no labels: a happy toddler hopping; a bright sun with a hot thermometer; a single black dot drawn on white paper with a pencil. |
| 086 | wf-ad | -ad family | Three scenes together, no dividers and no labels: a smiling dad hugging his daughter; a sad girl with a tear and a rain cloud; a grumpy boy holding a red X sign. |
| 087 | wf-id | -id family | Three scenes together, no dividers and no labels: a boy giving a proud thumbs up; a cat hiding inside a cardboard box; a blue cooking pot with its lid. |
| 088 | wf-at-1 | -at family（2×2） | 2×2 grid of four cute scenes, no dividers and no labels: top-left a gray cat sitting on a green mat; top-right a very fat orange cat; bottom-left a colorful striped floor mat; bottom-right a cute gray tabby cat. |
| 089 | wf-at-2 | cat bat hat | A cute gray cat sitting on a striped mat, with a cute bat flying above and a pink sun hat hanging on a hook nearby, in one cheerful room scene. |

---

## 三、P2 可选（现在没图，加了更好）

### CVC 拼读课 27 个单词（2026-08-30）

这节课现在只有拼读面板没有配图，加上单主体小图会更直观。
**统一 prompt 模板**（把 `{OBJECT}` 换成下表的描述）：

```
【风格前缀】One single {OBJECT}, centered, full view, clean simple background.
```

| 编号 | 文件名 | 单词 | {OBJECT} |
|---|---|---|---|
| 090 | cvc-man | man 男人 | friendly grown-up man standing and smiling |
| 091 | cvc-fan | fan 风扇 | blue electric desk fan |
| 092 | cvc-ban | ban 禁止 | red circular no-entry sign with a white bar |
| 093 | cvc-can | can 罐头 | shiny metal food can |
| 094 | cvc-van | van 货车 | white delivery van |
| 095 | cvc-fed | fed 喂过 | mother bird feeding a worm to a baby bird in a nest |
| 096 | cvc-beg | beg 乞求 | cute puppy sitting up on hind legs begging |
| 097 | cvc-vet | vet 兽医 | friendly veterinarian in a white coat holding a puppy |
| 098 | cvc-fit | fit 健康的 | happy child doing exercise, strong and healthy |
| 099 | cvc-big | big 大的 | one very large elephant next to one tiny mouse |
| 100 | cvc-bin | bin 垃圾桶 | green trash bin with an open lid |
| 101 | cvc-dig | dig 挖 | child digging in sand with a shovel |
| 102 | cvc-six | six 六 | exactly six colorful balloons |
| 103 | cvc-kid | kid 小孩 | cheerful young child waving |
| 104 | cvc-top | top 顶部 | red ball resting on top of a tall stack of blocks |
| 105 | cvc-dot | dot 点 | single black dot drawn on white paper with a pencil |
| 106 | cvc-got | got 得到 | happy child receiving a wrapped gift |
| 107 | cvc-hot | hot 热的 | steaming hot mug with a red thermometer beside it |
| 108 | cvc-log | log 原木 | fallen wooden log in a green forest |
| 109 | cvc-job | job 工作 | friendly firefighter in uniform |
| 110 | cvc-dog | dog 狗 | happy golden puppy wagging its tail |
| 111 | cvc-tub | tub 浴缸 | white bathtub full of bubbles |
| 112 | cvc-gum | gum 口香糖 | pack of colorful chewing gum |
| 113 | cvc-code | code 密码 | keypad lock with glowing buttons |
| 114 | cvc-cute | cute 可爱的 | very cute fluffy kitten with big eyes |
| 115 | cvc-date | date 日期 | wall calendar with one day circled in red |
| 116 | cvc-kite | kite 风筝 | colorful diamond kite flying in a blue sky |

### 第 20 课「比…少一」（20-one-fewer-than-and-zero）

**不需要配图**。这节课用应用内置的彩色算式块（`eq` 字段）渲染 `10−1`、`9−1`，
比插画更清楚，也不占体积。

---

## 四、建议不配图的卡片（用 emoji 或算式块）

这些卡片内容抽象，配图反而干扰：

| 课程 | 卡片 | 建议 |
|---|---|---|
| k2-letter-o | sound it out（拼读练习 -ot） | 用拼读面板即可，emoji 🔤 |
| k2-letter-f | sound it out（拼读练习） | 同上 |
| k2-sw-on-the-go | sound it out（拼读练习） | 同上 |
| k2-sw-here-is-to-and-all | CVC words（拼读小词） | 同上 |

---

## 五、出图后怎么入库

图片按**编号命名**（`001.png`、`002.png`…）放进一个目录，然后跑：

```bash
cd english-daka
python3 ingest_images.py generated-images/001-007 --dry   # 先预览会做什么
python3 ingest_images.py generated-images/001-007         # 确认后执行
```

脚本会自动：
1. **从本文档的表格解析编号 → 目标文件名**（不用手工对照）
2. 归一化入库：3:4 居中裁剪 → 720×960 → webp ≤150KB，覆盖同名旧图
3. 打印每张图被哪几节课引用，以及可直接点开验证的课程链接

因为目标文件名和课程 JSON 里已有的引用一致，**入库后 JSON 一个字都不用改**，刷新即生效。
（P2 那批 CVC 图是新增的，需要额外写进 JSON，脚本会用 ⚠ 提示哪些图还没有课程引用。）

**不必一次交齐**，建议一课一批出，验证风格没跑偏再继续。

### 完成状态（2026-08-30）：✅ 116 / 116 全部入库并接进课程 JSON

- 出图规格：1086×1448（正好 3:4），零裁剪，绝大多数以最高质量档 q=85 入库，成品 21–149KB
- 抽查结论：★字母卡只有字母无多余文字 ✓；2×2 四格卡没有被 AI 加英文标签 ✓；
  数量题（六/七/八只鸡、五个动物+五个圆片、四个玩具+四个圆片、十只+十片、2+3=5）
  **数目全部准确** ✓
- 入库后清理了 57 张被替换掉的旧海报/旧裁切图，图片库从 178 张精简到 121 张（9.5MB）
- 卡片配图覆盖率：151 张卡片中 124 张有图（82%），其余是抽象卡和用算式块的数字课

**⚠ 替换同名图后浏览器会用缓存显示旧图**（文件名没变，`?v=` 参数只能刷新 HTML/JSON）。
看到图没更新时用 Cmd+Shift+R 强制刷新，不是入库失败。

---

## 六、P3 补缺：拆卡后剩下的图文缺口（117–166，共 50 条）

全库审计出来的缺口：**一张卡里几个问答讲不同的东西，却共用同一张卡片图**。
比如 letter N 的 need 卡问「拼一下 one」，配的却是整张 need 拼图；
letter O 的 box 卡问「盒子里有什么」，配的是 box 的图，看不到里面的狐狸。

不需要配图的三类已排除：音标题（听音辨音本来就不靠图）、拼写题、
拼读串联（sot / mot / fot 是假词，画不出来）。

**完整可直接复制的 prompt 见 `配图Prompt手动生成版-补缺.md`**，本表只列索引。

| 117 | recycling-bin-paper | k2-recycling·回收箱「纸」 | One blue recycling bin with a recycling arrow symbol on it, filled with folded newspapers and fl… |
| 118 | recycling-bin-metal | k2-recycling·回收箱「金属」 | One green recycling bin with a recycling arrow symbol on it, filled with shiny tin cans and soda… |
| 119 | recycling-bin-plastic | k2-recycling·回收箱「塑料」 | One orange recycling bin with a recycling arrow symbol on it, filled with clear plastic bottles … |
| 120 | recycling-bin-glass | k2-recycling·回收箱「玻璃」 | One purple recycling bin with a recycling arrow symbol on it, filled with glass bottles and glas… |
| 121 | recycling-compost | k2-recycling·堆肥堆 | A wooden compost box in a sunny garden, filled with vegetable scraps, fruit peels and fallen lea… |
| 122 | recycling-item-paper | k2-recycling·纸类物品 | A folded newspaper and a flattened brown cardboard box lying together on a plain light backgroun… |
| 123 | recycling-item-metal | k2-recycling·金属物品 | A shiny empty tin can and an aluminium soda can lying together on a plain light background. No b… |
| 124 | recycling-item-plastic | k2-recycling·塑料物品 | An empty clear plastic water bottle and a plastic cup lying together on a plain light background… |
| 125 | recycling-item-glass | k2-recycling·玻璃物品 | An empty clear glass bottle and a glass jar standing together on a plain light background. No bi… |
| 126 | recycling-apple-core | k2-recycling·苹果核 | A single eaten apple core lying on a plain light background. |
| 127 | recycling-sort-glass | k2-recycling·分一分「玻璃瓶去哪个桶」 | A clear empty glass bottle lying on green grass beside a purple recycling bin with a recycling a… |
| 128 | n-letter-nail | k2-letter-n·letter N 卡「这是什么」→ nail | One shiny metal nail with a flat round head, lying on a light wooden workbench. |
| 129 | n-nose-touch | k2-letter-n·摸鼻子 | A smiling child touching the tip of their own nose with one index finger, head and shoulders vis… |
| 130 | n-nose-smell | k2-letter-n·用鼻子闻 | A child leaning close to a big colorful flower and sniffing it, eyes closed with a happy express… |
| 131 | n-neck-touch | k2-letter-n·摸脖子 | A smiling child resting one open hand on their own neck, head and shoulders visible, plain soft … |
| 132 | n-nod | k2-letter-n·点头 | A cheerful child nodding their head yes, with two small soft motion arcs beside the head to sugg… |
| 133 | n-nurse-sick | k2-letter-n·护士照顾病人 | A kind nurse in a light blue uniform gently caring for a child who is lying in bed with a blanke… |
| 134 | n-nest-eagle | k2-letter-n·鹰住在鸟巢里 | One big friendly eagle sitting in a large twig nest on a thick tree branch, blue sky behind. |
| 135 | f-letter-fairy | k2-letter-f·letter F 卡「这是什么」→ fairy | One cute little fairy with sparkling translucent wings and a small wand, hovering above green gr… |
| 136 | f-fox-forest | k2-letter-f·fox 卡「狐狸在哪里」→ forest | One friendly red fox standing among tall green trees in a sunny forest, full body visible, soft … |
| 137 | r-letter-raccoon | k2-letter-r·letter R 卡「这是什么动物」→ raccoon | One friendly raccoon with a black mask marking and a striped bushy tail, full body, sitting on g… |
| 138 | o-box-fox-in | k2-letter-o·box 卡「盒子里有什么」→ fox in the box | One friendly red fox sitting inside an open cardboard box, only its head and front paws poking o… |
| 139 | o-fox-box-on | k2-letter-o·fox 卡「狐狸在哪里」→ fox on the box | One friendly red fox sitting on top of a closed cardboard box, full body visible above the box. |
| 140 | o-clock-log | k2-letter-o·clock 卡「时钟在哪里」→ on a log | One round wall clock with simple hands resting on top of a fallen wooden log in a sunny meadow. … |
| 141 | on-table-book | k2-letter-o·on 卡 / k2-sw-on-the-go·on the farm 卡「书在哪里」 | One closed colorful picture book lying flat on a small wooden table in a simple bright room. The… |
| 142 | walk-on-street | k2-letter-o·on 卡 / k2-signs·street 卡「街上不能跑，要走」 | Two cheerful children walking calmly side by side on a city sidewalk beside a street, holding ha… |
| 143 | math-count-chips-five | k2-math-1-5·count 卡「有几个圆片」→ five | Exactly five identical round flat counting chips arranged in a neat row on a plain light backgro… |
| 144 | math-chips-two-lions | k2-math-1-5·chips 卡「有几只狮子」→ two | Exactly two friendly cartoon lions standing side by side above a row of exactly two round flat c… |
| 145 | math-chips-four-apples | k2-math-1-5·chips 卡「有几个苹果」→ four | Exactly four red apples in a neat row above a row of exactly four round flat counting chips, on … |
| 146 | math-chips-two-hands | k2-math-1-5·chips 卡「你有几只手」→ two | Exactly two open child hands side by side, palms facing the viewer, above a row of exactly two r… |
| 147 | math-five-fingers | k2-math-6-10·ten fingers 卡「伸出五根手指」 | One open child hand held up with all five fingers spread and clearly visible, palm facing the vi… |
| 148 | math-two-plus-three | k2-math-6-10·altogether 卡「2 个苹果加 3 个苹果」→ five | Exactly two red apples grouped on the left and exactly three red apples grouped on the right, wi… |
| 149 | math-five-plus-five | k2-math-6-10·altogether 卡「一只手五根加一只手五根」→ ten | Two open child hands held up side by side, palms facing the viewer, each hand showing all five f… |
| 150 | sw-here-come | k2-sw-here-is-to-and-all·here 卡「你能过来吗」→ come | A cheerful child walking toward the viewer with one arm waving, a welcoming open path behind. |
| 151 | sw-and-piano | k2-sw-here-is-to-and-all·and 卡「钢琴是什么颜色」→ black and white | One upright piano with clearly visible black and white keys, lid open, standing in a bright simp… |
| 152 | sw-all-birds-wings | k2-sw-here-is-to-and-all·all 卡「鸟都有翅膀吗」/ k2-wf-an「鸟会飞吗」 | Three friendly birds flying together in a blue sky with their wings fully spread and clearly vis… |
| 153 | sw-all-play | k2-sw-here-is-to-and-all·all 卡「Dan 和 Cam 在做什么」→ play | Two happy children playing together outdoors with a ball on green grass, sunny day. |
| 154 | sw-all-questions | k2-sw-here-is-to-and-all·all 卡「你的爱好是什么」→ asking questions | One curious cheerful child sitting at a small desk with one hand raised high to ask a question. |
| 155 | sw-cvc-dan-man | k2-sw-here-is-to-and-all·CVC 卡「Dan 是谁」→ a man | One friendly young man with short hair, smiling warmly at the viewer, upper body visible, plain … |
| 156 | sw-cvc-pat-cat | k2-sw-here-is-to-and-all·CVC 卡「你能摸摸猫吗」→ pat the tan cat | A gentle child softly patting a tan cat on its head, both clearly visible, warm cozy background. |
| 157 | sw-cvc-rat-mat | k2-sw-here-is-to-and-all·CVC 卡「老鼠坐在哪里」→ on the mat | One small cute grey rat sitting in the middle of a woven straw mat on a wooden floor. |
| 158 | sw-cvc-skip | k2-sw-here-is-to-and-all·CVC 卡「你会跳吗」→ skip | One cheerful child skipping happily on a path, one knee lifted mid-skip, arms swinging. |
| 159 | sw-go-swimming | k2-sw-on-the-go·go 卡「夏天你能做什么」→ go swimming | One happy child swimming in a bright blue swimming pool on a sunny summer day, water splashing g… |
| 160 | sw-go-subway | k2-sw-on-the-go·go 卡「爸爸怎么去上班」→ by subway | A friendly dad with a backpack stepping onto a subway train at a bright station platform. |
| 161 | sw-on-elephant | k2-sw-on-the-go·on 卡「哪种动物鼻子最长」→ elephant | One friendly grey elephant with a long trunk clearly visible, full body, standing on grass under… |
| 162 | sw-on-farm-cow | k2-sw-on-the-go·on the farm 卡「奶牛住在哪里」→ on the farm | One friendly black and white cow standing in a green farm field, a red barn and a wooden fence b… |
| 163 | sw-on-snowman | k2-sw-on-the-go·on the farm 卡「下雪天能做什么」→ build a snowman | A cheerful child building a snowman on a snowy day, the snowman has a carrot nose, a scarf and s… |
| 164 | wf-an-dad | k2-wf-an·「这个男人是谁」→ my dad | One friendly dad smiling warmly with his young child beside him, upper bodies visible, warm cozy… |
| **165** | sw-like | k2-sw-my-like-i-too·like（**重出，取代已作废的 049**；注意不是 135，135 是 `f-letter-fairy`） | One happy child holding an ice cream cone with both hands, taking a lick, with small soft hearts… |
| 166 | n-need-spell-one | k2-letter-n·need 卡「拼一下 one」 | Three big colorful wooden alphabet blocks in a neat row on a table, spelling the word ONE, with … |

**出图注意**
- 全部单图一物，**不要出 2×2 四格图**。
- 垃圾分类配色沿用已有约定：纸=蓝、金属=绿、塑料=橙、玻璃=紫、厨余=木箱（同 077–080）。
- 编号 141 / 142 / 152 各被两张卡共用，只出一张。
- 编号 165 是**替换同名图**（`sw-like` 现在画成了「指着自己」，和 sw-i 撞了），
  入库后 JSON 不用改，注意浏览器缓存要 Cmd+Shift+R。
  ⚠️ **`sw-like` 在本清单里出现两次：049（已作废）和 165（要出的）**。
  049 在「P1 必做」里、位置靠前，容易先撞上并误以为已经做过；找 sw-like 一律认 165。
  另外曾有人把它记成"第 135 条"——135 是 `f-letter-fairy`，不相干。
- 编号 166 是唯一允许出现字母的一张（积木拼 O N E）。
- 数学那几张（143–149）**数目必须准确**，出完请数一遍再入库。

## 七、字母卡拆卡补图（167–172，共 6 条）

字母卡上「What sound does igloo begin with?」这类问答讲的是**别的词**，却和字母
共用一张字母图。这 6 张出完，letter I / B / M / T 就能按一图一词拆开。
完整 prompt 见 `配图Prompt手动生成版-补缺.md` 第七节。

| 编号 | 目标文件名 | 卡片 | Prompt |
|---|---|---|---|
| 167 | i-igloo | k2-letter-i · igloo | round igloo made of white snow blocks with a small arched entrance |
| 168 | i-insect | k2-letter-i · insect | friendly colorful ladybug on a green leaf |
| 169 | i-ink | k2-letter-i · ink | open glass ink bottle with a feather quill pen |
| 170 | b-ball | k2-letter-b · ball | colorful striped beach ball on green grass |
| 171 | m-mom | k2-letter-m · mom | a warm smiling mom hugging her young child |
| 172 | t-taxi | k2-letter-t · taxi | cheerful yellow taxi cab parked on a city street |

其余同类词已复用现成图，不用再出：apple、bed、dolphin、orange、fairy、nail、raccoon。

## 八、拼读串联卡补图（173–174）—— ⛔ 已作废，不用出图

| 编号 | 目标文件名 | 卡片 | 状态 |
|---|---|---|---|
| ~~173~~ | ~~cvc-sam~~ | k2-sw-on-the-go · 拼读 sam | ⛔ 作废，改用字母块 |
| ~~174~~ | ~~cvc-not~~ | k2-letter-f / k2-letter-o · 拼读 not | ⛔ 作废，改用字母块 |

**作废原因**：拼读串联卡改成了「没有配图的问答直接放大字母」——
app.html 的 `letterTiles()` 把这一问要拼的词（`key`）渲染成一个整词色块
（`SOT` / `MOT` / `NOT` / `SAM`），同一底色、字母连在一起。

这比配图更对题，有两点：

1. **假词的问题自然消解**。`sot` / `mot` 没有对应的东西，硬配一张图等于告诉
   孩子这是个真词；字母块没有这个问题。
2. **顺序是对的**。拼读练习先给图，孩子会直接说出那个词、跳过解码；
   字母块反而逼他走一遍「看字母 → 出声 → 连成词」。

所以拼读串联卡**以后都不要配图**，缺图就是正常状态，`letterTiles()` 会接住。
sat / mat / fox / tot / cat 那几处已有的图是复用旧图，留着无妨，但不必再补。
