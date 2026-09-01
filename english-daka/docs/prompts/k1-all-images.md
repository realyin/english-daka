# 配图 Prompt · K1 全套（一次性）

K1 共 **59 节课**，需要新出 **126 张图**（另有 5 张复用 K2 现成配图）。

**不需要出图的两类**（应用里用 CSS 画，比出图准）：字母课的 26 个字形、
规律课的 10 条规律条、颜色卡的色块、形状卡的形状——它们的主体就是字母/数字/
纯色/几何形，AI 出图既不准也和「NO text/letters/numbers」的风格前缀冲突。

---

## 怎么用

1. 每条 prompt **前面都要加下面的统一风格前缀**（保证全站画风一致）
2. 出图后按每条的「**存为**」命名（文件名 = 入库名 = 卡片 `image` 字段名，一名三用）
3. 全部丢进一个目录，一次入库：

```bash
python ingest_images.py <图片目录> --dry   # 先预览
python ingest_images.py <图片目录>
```

### 统一风格前缀

```
Children's picture book illustration, soft watercolor style with clean rounded
outlines, warm bright cheerful colors, simple uncluttered background, single
clear subject centered in frame, vertical 3:4 composition, friendly and cute,
suitable for a 5-year-old, NO text, NO letters, NO words, NO numbers, NO speech
bubbles, NO labels, NO borders or frames, NO panel dividers.
```

### 负面提示（工具支持的话）

```
text, letters, words, captions, labels, watermark, speech bubble, comic panels,
grid lines, borders, frame, collage of photos, realistic photo, scary, horror,
cluttered, multiple scenes, extra limbs, deformed hands
```

### 三条通用要求

- **一图一词**：画面主体必须就是那个词，不要顺带画出同一课其它卡片的东西（考一考的选项来自同一课，画重了孩子无从分辨）
- **数量必须准**：数字课那 15 张要逐个点清楚，排列成整齐的行，**画错数量比没有图更糟**
- **不要文字**：任何画面里都不要出现字母、数字、招牌字（数字卡画的是「N 个物品」，不是数字符号本身）

---

## 数字 Numbers（15 张）

⚠️ 这一组是**数数课**：数量必须精确，物品要排成整齐的行、彼此分开、一眼能点清。生成后**逐个数一遍**再入库。

### `k1-num-five` — five 五

- **存为**：`k1-num-five.png`
- **所属**：k1-number-1-5
- **画面要能回答**：What's this number?

```
exactly FIVE identical toy telephones arranged in one neat row on a plain cream background, evenly spaced and easy to count.
```

### `k1-num-four` — four 四

- **存为**：`k1-num-four.png`
- **所属**：k1-number-1-5
- **画面要能回答**：What's this number?

```
exactly FOUR colorful skipping ropes laid out in a neat row on a plain cream background, each a different bright color, clearly separated.
```

### `k1-num-one` — one 一

- **存为**：`k1-num-one.png`
- **所属**：k1-number-1-5
- **画面要能回答**：What's this number?

```
exactly ONE small blue electric desk fan standing on a plain cream background, blades visible, friendly rounded shape.
```

### `k1-num-three` — three 三

- **存为**：`k1-num-three.png`
- **所属**：k1-number-1-5
- **画面要能回答**：What's this number?

```
exactly THREE identical small hanging lamps with warm glowing bulbs in a row against a plain cream background, evenly spaced.
```

### `k1-num-two` — two 二

- **存为**：`k1-num-two.png`
- **所属**：k1-number-1-5
- **画面要能回答**：What's this number?

```
exactly TWO identical small wooden chairs standing side by side on a plain cream background, evenly spaced.
```

### `k1-num-eight` — eight 八

- **存为**：`k1-num-eight.png`
- **所属**：k1-number-6-10
- **画面要能回答**：What's this number?

```
exactly EIGHT colorful wooden toy blocks arranged in two neat rows of four on a plain cream background, each block a different bright color, clearly separated.
```

### `k1-num-nine` — nine 九

- **存为**：`k1-num-nine.png`
- **所属**：k1-number-6-10
- **画面要能回答**：What's this number?

```
exactly NINE small cheerful birds perched in two rows, five on a branch above and four on a branch below, soft blue sky background, evenly spaced.
```

### `k1-num-seven` — seven 七

- **存为**：`k1-num-seven.png`
- **所属**：k1-number-6-10
- **画面要能回答**：What's this number?

```
exactly SEVEN small colorful toys (balls and blocks) arranged in two neat rows, four in front and three behind, on a plain cream background, clearly separated.
```

### `k1-num-six` — six 六

- **存为**：`k1-num-six.png`
- **所属**：k1-number-6-10
- **画面要能回答**：What's this number?

```
exactly SIX identical small golden party horns arranged in two rows of three on a plain cream background, evenly spaced.
```

### `k1-num-ten` — ten 十

- **存为**：`k1-num-ten.png`
- **所属**：k1-number-6-10
- **画面要能回答**：What's this number?

```
exactly TEN fluffy yellow baby chicks standing in two neat rows of five on green grass, evenly spaced and clearly separated.
```

### `k1-num-eleven` — eleven 十一

- **存为**：`k1-num-eleven.png`
- **所属**：k1-number-11-12
- **画面要能回答**：What's this number?

```
exactly ELEVEN small cartoon rocket spaceships arranged in a neat grid, six in the top row and five in the bottom row, soft starry night background, evenly spaced.
```

### `k1-num-twelve` — twelve 十二

- **存为**：`k1-num-twelve.png`
- **所属**：k1-number-11-12
- **画面要能回答**：What's this number?

```
exactly TWELVE happy cartoon children standing in two rows of six, holding hands, plain soft background, all clearly separated and countable.
```

### `k1-num-fifteen` — fifteen 十五

- **存为**：`k1-num-fifteen.png`
- **所属**：k1-number-13-15
- **画面要能回答**：What's this number?

```
exactly FIFTEEN identical fluffy white clouds arranged in three neat rows of five against a soft blue sky, evenly spaced and clearly separated.
```

### `k1-num-fourteen` — fourteen 十四

- **存为**：`k1-num-fourteen.png`
- **所属**：k1-number-13-15
- **画面要能回答**：What's this number?

```
exactly FOURTEEN identical smiling cartoon suns arranged in two neat rows of seven, soft blue sky background, evenly spaced.
```

### `k1-num-thirteen` — thirteen 十三

- **存为**：`k1-num-thirteen.png`
- **所属**：k1-number-13-15
- **画面要能回答**：What's this number?

```
exactly THIRTEEN white round plates arranged in a neat grid, seven in the top row and six in the bottom row, plain cream background.
```

## 颜色 Colors（11 张）

⚠️ 这一组考的是颜色：**目标颜色必须鲜明、占画面主导**，背景用中性米白，不要出现其它抢眼的颜色。

### `k1-color-blue` — blue 蓝色

- **存为**：`k1-color-blue.png`
- **所属**：k1-color-red
- **画面要能回答**：What is blue?

```
a wide clear blue sky with two or three small fluffy white clouds and a distant green horizon line at the very bottom, the blue sky fills most of the frame.
```

### `k1-color-red` — red 红色

- **存为**：`k1-color-red.png`
- **所属**：k1-color-red
- **画面要能回答**：What is red?

```
one bright red apple with a small green leaf, plain cream background, the red color is vivid and unmistakable.
```

### `k1-color-yellow` — yellow 黄色

- **存为**：`k1-color-yellow.png`
- **所属**：k1-color-red
- **画面要能回答**：What is yellow?

```
one bright yellow banana, plain cream background, the yellow color is vivid and unmistakable.
```

### `k1-color-green` — green 绿色

- **存为**：`k1-color-green.png`
- **所属**：k1-color-orange
- **画面要能回答**：What is green?

```
one leafy green tree with a brown trunk standing on a small patch of grass, plain soft background, the green foliage fills most of the frame.
```

### `k1-color-orange` — orange 橙色

- **存为**：`k1-color-orange.png`
- **所属**：k1-color-orange
- **画面要能回答**：What is orange?

```
one bright orange fruit with a small green leaf, plain cream background, the orange color is vivid and unmistakable.
```

### `k1-color-purple` — purple 紫色

- **存为**：`k1-color-purple.png`
- **所属**：k1-color-orange
- **画面要能回答**：What is purple?

```
one bunch of round purple grapes with a green leaf, plain cream background, the purple color is vivid and unmistakable.
```

### `k1-color-black` — black 黑色

- **存为**：`k1-color-black.png`
- **所属**：k1-color-black
- **画面要能回答**：What is black?

```
one glossy black crow standing on a bare branch, plain soft cream background, the black feathers are the clear subject.
```

### `k1-color-gray` — gray 灰色

- **存为**：`k1-color-gray.png`
- **所属**：k1-color-black
- **画面要能回答**：What is gray?

```
one cute little gray mouse with round ears and a long tail sitting on a plain cream background, the gray fur is the clear subject.
```

### `k1-color-white` — white 白色

- **存为**：`k1-color-white.png`
- **所属**：k1-color-black
- **画面要能回答**：What is white?

```
a smooth white snowy hill with soft white snow covering everything and a few gentle snowflakes falling, pale blue sky, white fills most of the frame.
```

### `k1-color-brown` — brown 棕色

- **存为**：`k1-color-brown.png`
- **所属**：k1-color-pink
- **画面要能回答**：What is brown?

```
one cute brown monkey sitting and smiling, plain cream background, the brown fur is the clear subject.
```

### `k1-color-pink` — pink 粉色

- **存为**：`k1-color-pink.png`
- **所属**：k1-color-pink
- **画面要能回答**：What is pink?

```
one large pink flower in full bloom with a green stem, plain cream background, the pink petals are vivid and unmistakable.
```

## 动物 Animals（17 张）

### `k1-animal-chicken` — chicken 小鸡

- **存为**：`k1-animal-chicken.png`
- **所属**：k1-animal-farm
- **画面要能回答**：What's this farm animal?

```
one plump white hen with a red comb standing on green farm grass, facing forward.
```

### `k1-animal-cow` — cow 奶牛

- **存为**：`k1-animal-cow.png`
- **所属**：k1-animal-farm
- **画面要能回答**：What's this farm animal?

```
one friendly black-and-white dairy cow standing on green farm grass, facing forward, plain sky background.
```

### `k1-animal-horse` — horse 马

- **存为**：`k1-animal-horse.png`
- **所属**：k1-animal-farm
- **画面要能回答**：What's this farm animal?

```
one friendly brown horse standing on green farm grass, facing forward, full body visible.
```

### `k1-animal-sheep` — sheep 绵羊

- **存为**：`k1-animal-sheep.png`
- **所属**：k1-animal-farm
- **画面要能回答**：What's this farm animal?

```
one fluffy white sheep with a soft woolly coat standing on green farm grass, facing forward.
```

### `k1-animal-goldfish` — goldfish 金鱼

- **存为**：`k1-animal-goldfish.png`
- **所属**：k1-animal-pets
- **画面要能回答**：What pet is it?

```
one bright orange goldfish swimming inside a clear round glass fish tank with water plants and pebbles, plain cream background.
```

### `k1-animal-hamster` — hamster 仓鼠

- **存为**：`k1-animal-hamster.png`
- **所属**：k1-animal-pets
- **画面要能回答**：What pet is it?

```
one cute golden hamster sitting inside a simple wire cage with a small wooden house and a water bottle, plain cream background.
```

### `k1-animal-turtle` — turtle 乌龟

- **存为**：`k1-animal-turtle.png`
- **所属**：k1-animal-pets
- **画面要能回答**：What pet is it?

```
one small green turtle inside a clear glass tank with shallow water, a rock and a small plant, plain cream background.
```

### `k1-animal-elephant` — elephant 大象

- **存为**：`k1-animal-elephant.png`
- **所属**：k1-animal-jungle
- **画面要能回答**：What's this animal?

```
one friendly gray elephant with big ears standing among green jungle plants and tall trees.
```

### `k1-animal-hippo` — hippo 河马

- **存为**：`k1-animal-hippo.png`
- **所属**：k1-animal-jungle
- **画面要能回答**：What's this animal?

```
one chubby gray hippo standing at the edge of a jungle river with green plants around.
```

### `k1-animal-leopard` — leopard 豹

- **存为**：`k1-animal-leopard.png`
- **所属**：k1-animal-jungle
- **画面要能回答**：What's this animal?

```
one spotted leopard with golden fur and black rosettes standing calmly among green jungle plants, friendly cartoon face, not fierce.
```

### `k1-animal-monkey` — monkey 猴子

- **存为**：`k1-animal-monkey.png`
- **所属**：k1-animal-jungle
- **画面要能回答**：What's this animal?

```
one cute brown monkey hanging from a green jungle vine, smiling.
```

### `k1-animal-crow` — crow 乌鸦

- **存为**：`k1-animal-crow.png`
- **所属**：k1-animal-birds
- **画面要能回答**：What bird is it?

```
one glossy black crow sitting in a twig nest on a tree branch, green leaves around.
```

### `k1-animal-eagle` — eagle 老鹰

- **存为**：`k1-animal-eagle.png`
- **所属**：k1-animal-birds
- **画面要能回答**：What bird is it?

```
one brown eagle with a white head sitting in a large twig nest on a rocky ledge, blue sky behind.
```

### `k1-animal-owl` — owl 猫头鹰

- **存为**：`k1-animal-owl.png`
- **所属**：k1-animal-birds
- **画面要能回答**：What bird is it?

```
one round friendly owl with big eyes sitting in a twig nest inside a tree hollow, night sky with a moon behind.
```

### `k1-animal-dolphin` — dolphin 海豚

- **存为**：`k1-animal-dolphin.png`
- **所属**：k1-animal-ocean
- **画面要能回答**：What's this animal?

```
one cheerful gray dolphin leaping above blue ocean waves, splashing water, sunny sky.
```

### `k1-animal-shark` — shark 鲨鱼

- **存为**：`k1-animal-shark.png`
- **所属**：k1-animal-ocean
- **画面要能回答**：What's this animal?

```
one friendly cartoon shark with a rounded smiling face swimming underwater, blue ocean water with light rays, not scary.
```

### `k1-animal-whale` — whale 鲸鱼

- **存为**：`k1-animal-whale.png`
- **所属**：k1-animal-ocean
- **画面要能回答**：What's this animal?

```
one big friendly blue whale swimming underwater with a small spout, blue ocean water and light rays.
```

## 身体 Body（15 张）

⚠️ 这一组的主体是**身体部位**，不是小朋友本人：构图要让那个部位成为明显焦点（数量类的「两只/十根」还要能点清）。

### `k1-body-ears` — ears 耳朵

- **存为**：`k1-body-ears.png`
- **所属**：k1-body-eyes
- **画面要能回答**：What are these body parts?

```
a happy child's head seen from the front with hair tucked back so that BOTH ears are clearly visible and are the obvious focus.
```

### `k1-body-eyes` — eyes 眼睛

- **存为**：`k1-body-eyes.png`
- **所属**：k1-body-eyes
- **画面要能回答**：What are these body parts?

```
a close-up of a happy child's face showing TWO big bright eyes clearly, the eyes are the obvious focus, rest of the face soft and simple.
```

### `k1-body-mouth` — mouth 嘴巴

- **存为**：`k1-body-mouth.png`
- **所属**：k1-body-nose
- **画面要能回答**：What's this body part?

```
a close-up of a smiling child's open mouth showing teeth, the mouth is the obvious focus.
```

### `k1-body-nose` — nose 鼻子

- **存为**：`k1-body-nose.png`
- **所属**：k1-body-nose
- **画面要能回答**：What's this body part?

```
a close-up of a smiling child's face with the nose clearly at the center as the obvious focus.
```

### `k1-body-face` — face 脸

- **存为**：`k1-body-face.png`
- **所属**：k1-body-hair
- **画面要能回答**：What's this body part?

```
a happy child's whole round face smiling warmly, seen from the front, plain cream background.
```

### `k1-body-hair` — hair 头发

- **存为**：`k1-body-hair.png`
- **所属**：k1-body-hair
- **画面要能回答**：What's this body part?

```
a happy child with long soft black hair, seen from the front, the hair is the obvious focus, plain cream background.
```

### `k1-body-head` — head 头

- **存为**：`k1-body-head.png`
- **所属**：k1-body-head
- **画面要能回答**：What's this body part?

```
a happy child pointing at their own head with one finger, upper body visible, plain cream background.
```

### `k1-body-neck` — neck 脖子

- **存为**：`k1-body-neck.png`
- **所属**：k1-body-head
- **画面要能回答**：What's this body part?

```
a happy child touching their own neck with one hand, head and shoulders visible, plain cream background.
```

### `k1-body-shoulders` — shoulders 肩膀

- **存为**：`k1-body-shoulders.png`
- **所属**：k1-body-head
- **画面要能回答**：What are these body parts?

```
a happy child with both hands placed on their own TWO shoulders, upper body visible, plain cream background.
```

### `k1-body-arms` — arms 手臂

- **存为**：`k1-body-arms.png`
- **所属**：k1-body-arms
- **画面要能回答**：What are these body parts?

```
a happy child stretching out BOTH arms wide to the sides, full body visible, plain cream background.
```

### `k1-body-fingers` — fingers 手指

- **存为**：`k1-body-fingers.png`
- **所属**：k1-body-arms
- **画面要能回答**：What are these body parts?

```
a close-up of a child's TWO open hands side by side with all TEN fingers spread and clearly countable, plain cream background.
```

### `k1-body-hands` — hands 手

- **存为**：`k1-body-hands.png`
- **所属**：k1-body-arms
- **画面要能回答**：What are these body parts?

```
a happy child holding up BOTH open hands with fingers spread toward the viewer, plain cream background.
```

### `k1-body-feet` — feet 脚

- **存为**：`k1-body-feet.png`
- **所属**：k1-body-legs
- **画面要能回答**：What are these body parts?

```
a close-up of a child's TWO bare feet standing side by side on a plain cream background.
```

### `k1-body-legs` — legs 腿

- **存为**：`k1-body-legs.png`
- **所属**：k1-body-legs
- **画面要能回答**：What are these body parts?

```
a happy child standing and pointing down at their own TWO legs, full body visible, plain cream background.
```

### `k1-body-toes` — toes 脚趾

- **存为**：`k1-body-toes.png`
- **所属**：k1-body-legs
- **画面要能回答**：What are these body parts?

```
a close-up of a child's TWO bare feet with all TEN toes clearly visible and countable, plain cream background.
```

## 动作 Actions（17 张）

⚠️ 这一组画的是**动作**：姿态要一眼看懂在干什么，全身或半身入镜，别只画个静止的脸。

### `k1-act-brush-hair` — brush my hair 梳头

- **存为**：`k1-act-brush-hair.png`
- **所属**：k1-action-wash
- **画面要能回答**：What can you do?

```
a happy child brushing their long hair with a hairbrush in front of a mirror.
```

### `k1-act-brush-teeth` — brush my teeth 刷牙

- **存为**：`k1-act-brush-teeth.png`
- **所属**：k1-action-wash
- **画面要能回答**：What can you do?

```
a happy child brushing their teeth with a toothbrush, white foam, standing at a bathroom sink.
```

### `k1-act-wash-face` — wash my face 洗脸

- **存为**：`k1-act-wash-face.png`
- **所属**：k1-action-wash
- **画面要能回答**：What can you do?

```
a happy child washing their face with both hands and water at a bathroom sink, water droplets around.
```

### `k1-act-wash-hands` — wash my hands 洗手

- **存为**：`k1-act-wash-hands.png`
- **所属**：k1-action-wash
- **画面要能回答**：What can you do?

```
a happy child washing both hands with soap bubbles under running water at a bathroom sink.
```

### `k1-act-drink` — drink 喝

- **存为**：`k1-act-drink.png`
- **所属**：k1-action-eat
- **画面要能回答**：What can you do?

```
a happy child holding a glass of milk with both hands and drinking from it.
```

### `k1-act-eat` — eat 吃

- **存为**：`k1-act-eat.png`
- **所属**：k1-action-eat
- **画面要能回答**：What can you do?

```
a happy child sitting at a table eating from a bowl with a spoon, cheerful expression.
```

### `k1-act-jump` — jump 跳

- **存为**：`k1-act-jump.png`
- **所属**：k1-action-walk
- **画面要能回答**：What can you do?

```
a happy child jumping up in the air with both arms raised and both feet off the ground, full body.
```

### `k1-act-run` — run 跑

- **存为**：`k1-act-run.png`
- **所属**：k1-action-walk
- **画面要能回答**：What can you do?

```
a happy child running fast on green grass, arms swinging, side view, full body, motion feel.
```

### `k1-act-walk` — walk 走

- **存为**：`k1-act-walk.png`
- **所属**：k1-action-walk
- **画面要能回答**：What can you do?

```
a happy child walking forward on a garden path, one foot stepping ahead, side view, full body.
```

### `k1-act-care` — care 关心

- **存为**：`k1-act-care.png`
- **所属**：k1-action-help
- **画面要能回答**：What can you do?

```
a gentle child hugging a small puppy carefully with a caring expression, plain soft background.
```

### `k1-act-help` — help 帮忙

- **存为**：`k1-act-help.png`
- **所属**：k1-action-help
- **画面要能回答**：What can you do?

```
a kind child helping another child stand up by holding their hand, both smiling, plain soft background.
```

### `k1-act-play` — play 玩

- **存为**：`k1-act-play.png`
- **所属**：k1-action-help
- **画面要能回答**：What can you do?

```
two happy children playing together with a colorful ball on green grass.
```

### `k1-act-share` — share 分享

- **存为**：`k1-act-share.png`
- **所属**：k1-action-help
- **画面要能回答**：What can you do?

```
one child handing half of an apple to another child with both smiling, plain soft background.
```

### `k1-act-dance` — dance 跳舞

- **存为**：`k1-act-dance.png`
- **所属**：k1-action-read
- **画面要能回答**：What can you do?

```
a happy child dancing with both arms up and one leg lifted, joyful movement, plain soft background.
```

### `k1-act-draw` — draw a picture 画画

- **存为**：`k1-act-draw.png`
- **所属**：k1-action-read
- **画面要能回答**：What can you do?

```
a happy child drawing a colorful picture on paper with crayons at a table.
```

### `k1-act-read` — read a book 读书

- **存为**：`k1-act-read.png`
- **所属**：k1-action-read
- **画面要能回答**：What can you do?

```
a happy child sitting cross-legged and reading an open picture book on their lap.
```

### `k1-act-sing` — sing a song 唱歌

- **存为**：`k1-act-sing.png`
- **所属**：k1-action-read
- **画面要能回答**：What can you do?

```
a happy child singing with an open mouth and one hand raised, small music notes floating around.
```

## 职业 Jobs（14 张）

⚠️ 职业卡画人（制服要能认出职业），场所/车辆卡画物 —— 同一课里两者不要混进同一张画面。

### `k1-job-fire-truck` — fire truck 消防车

- **存为**：`k1-job-fire-truck.png`
- **所属**：k1-job-police
- **画面要能回答**：What's this?

```
one bright red cartoon fire truck with a ladder on top, side view, plain soft background.
```

### `k1-job-firefighter` — firefighter 消防员

- **存为**：`k1-job-firefighter.png`
- **所属**：k1-job-police
- **画面要能回答**：What's this job?

```
one friendly smiling firefighter in a red-and-yellow uniform and helmet standing upright, full body, plain soft background.
```

### `k1-job-police-car` — police car 警车

- **存为**：`k1-job-police-car.png`
- **所属**：k1-job-police
- **画面要能回答**：What's this?

```
one cartoon police car in white and blue with a red-blue light bar on top, side view, plain soft background.
```

### `k1-job-policeman` — policeman 警察

- **存为**：`k1-job-policeman.png`
- **所属**：k1-job-police
- **画面要能回答**：What's this job?

```
one friendly smiling policeman in a blue uniform and cap standing upright, full body, plain soft background.
```

### `k1-job-ambulance` — ambulance 救护车

- **存为**：`k1-job-ambulance.png`
- **所属**：k1-job-doctor
- **画面要能回答**：What's this?

```
one white cartoon ambulance with red stripes and a light bar, side view, plain soft background.
```

### `k1-job-doctor` — doctor 医生

- **存为**：`k1-job-doctor.png`
- **所属**：k1-job-doctor
- **画面要能回答**：What's this job?

```
one friendly smiling doctor in a white coat with a stethoscope around the neck, full body, plain soft background.
```

### `k1-job-hospital` — hospital 医院

- **存为**：`k1-job-hospital.png`
- **所属**：k1-job-doctor
- **画面要能回答**：What's this?

```
one simple white hospital building with a red cross sign shape on the wall and an entrance, blue sky, plain surroundings.
```

### `k1-job-nurse` — nurse 护士

- **存为**：`k1-job-nurse.png`
- **所属**：k1-job-doctor
- **画面要能回答**：What's this job?

```
one friendly smiling nurse in a light blue uniform with a nurse cap, full body, plain soft background.
```

### `k1-job-airport` — airport 机场

- **存为**：`k1-job-airport.png`
- **所属**：k1-job-pilot
- **画面要能回答**：What's this?

```
a simple airport scene with one passenger airplane parked beside a small terminal building and a control tower, blue sky.
```

### `k1-job-astronaut` — astronaut 宇航员

- **存为**：`k1-job-astronaut.png`
- **所属**：k1-job-pilot
- **画面要能回答**：What's this job?

```
one friendly astronaut in a white spacesuit and helmet floating with stars behind, full body.
```

### `k1-job-pilot` — pilot 飞行员

- **存为**：`k1-job-pilot.png`
- **所属**：k1-job-pilot
- **画面要能回答**：What's this job?

```
one friendly smiling pilot in a navy uniform with a captain cap and gold stripes, full body, plain soft background.
```

### `k1-job-spaceship` — spaceship 太空飞船

- **存为**：`k1-job-spaceship.png`
- **所属**：k1-job-pilot
- **画面要能回答**：What's this?

```
one cartoon rocket spaceship flying upward with a flame trail, dark blue starry sky.
```

### `k1-job-artist` — artist 画家

- **存为**：`k1-job-artist.png`
- **所属**：k1-job-engineer
- **画面要能回答**：What's this job?

```
one friendly smiling artist in an apron holding a paint palette and brush in front of an easel, full body.
```

### `k1-job-engineer` — engineer 工程师

- **存为**：`k1-job-engineer.png`
- **所属**：k1-job-engineer
- **画面要能回答**：What's this job?

```
one friendly smiling engineer in an orange safety vest and yellow hard hat holding a rolled blueprint, full body, plain soft background.
```

## 天气 Weather（14 张）

⚠️ 前四张（hot/cool/cold/warm）画的是**人的感受**，后面几张画的是**天空和场景**，两类不要混。

### `k1-wx-cold` — cold 冷

- **存为**：`k1-wx-cold.png`
- **所属**：k1-weather-hot
- **画面要能回答**：How do you feel?

```
a child hugging themselves and shivering with a blue-tinted cold expression, breath visible, snowy background.
```

### `k1-wx-cool` — cool 凉爽

- **存为**：`k1-wx-cool.png`
- **所属**：k1-weather-hot
- **画面要能回答**：How do you feel?

```
a comfortable child smiling with a gentle breeze lifting their hair, light clothes, soft green background, feeling refreshed.
```

### `k1-wx-hot` — hot 热

- **存为**：`k1-wx-hot.png`
- **所属**：k1-weather-hot
- **画面要能回答**：How do you feel?

```
a child fanning themselves and wiping sweat with a hot flushed face under a big bright sun, feeling hot.
```

### `k1-wx-warm` — warm 温暖

- **存为**：`k1-wx-warm.png`
- **所属**：k1-weather-hot
- **画面要能回答**：How do you feel?

```
a cozy child smiling comfortably in a soft sweater with gentle warm sunlight around, feeling warm.
```

### `k1-wx-cloudy` — cloudy 阴天

- **存为**：`k1-wx-cloudy.png`
- **所属**：k1-weather-sunny
- **画面要能回答**：What's the weather like?

```
a cloudy day scene: a sky fully covered with soft gray and white clouds above a green field, no sun visible.
```

### `k1-wx-sunny` — sunny 晴天

- **存为**：`k1-wx-sunny.png`
- **所属**：k1-weather-sunny
- **画面要能回答**：What's the weather like?

```
a bright sunny day scene: a big smiling sun in a clear blue sky above a green sunny meadow, no clouds.
```

### `k1-wx-rainy` — rainy 雨天

- **存为**：`k1-wx-rainy.png`
- **所属**：k1-weather-rainy
- **画面要能回答**：What's the weather like?

```
a rainy day scene: gray clouds with steady rain falling, puddles on the ground, a child under a colorful umbrella.
```

### `k1-wx-snowy` — snowy 雪天

- **存为**：`k1-wx-snowy.png`
- **所属**：k1-weather-rainy
- **画面要能回答**：What's the weather like?

```
a snowy day scene: white snowflakes falling from a pale sky onto a snow-covered ground with a small snow-topped house.
```

### `k1-wx-stormy` — stormy 雷雨天

- **存为**：`k1-wx-stormy.png`
- **所属**：k1-weather-windy
- **画面要能回答**：What's the weather like?

```
a stormy day scene: dark gray clouds with a bright yellow lightning bolt and heavy rain, seen safely from a distance, not frightening.
```

### `k1-wx-windy` — windy 刮风天

- **存为**：`k1-wx-windy.png`
- **所属**：k1-weather-windy
- **画面要能回答**：What's the weather like?

```
a windy day scene: trees bending, leaves flying sideways, a child's scarf and hair blowing strongly in the wind.
```

### `k1-wx-fall` — fall 秋天

- **存为**：`k1-wx-fall.png`
- **所属**：k1-weather-spring
- **画面要能回答**：What season is it?

```
an autumn scene: trees with golden yellow and orange leaves, fallen leaves on the ground, warm amber colors.
```

### `k1-wx-spring` — spring 春天

- **存为**：`k1-wx-spring.png`
- **所属**：k1-weather-spring
- **画面要能回答**：What season is it?

```
a spring scene: a green meadow full of blooming colorful flowers, a blossoming tree, butterflies, bright fresh colors.
```

### `k1-wx-summer` — summer 夏天

- **存为**：`k1-wx-summer.png`
- **所属**：k1-weather-spring
- **画面要能回答**：What season is it?

```
a summer scene: a bright sunny beach with blue sea, a sun umbrella and a beach ball, hot golden sunshine.
```

### `k1-wx-winter` — winter 冬天

- **存为**：`k1-wx-winter.png`
- **所属**：k1-weather-spring
- **画面要能回答**：What season is it?

```
a winter scene: a snow-covered landscape with bare trees, a small snowman and falling snowflakes, pale blue cold colors.
```

## 形状 Shapes（7 张）

### `k1-shape-egg` — oval 椭圆形

- **存为**：`k1-shape-egg.png`
- **所属**：k1-shape-circle
- **画面要能回答**：What is like an oval?

```
one white chicken egg standing upright, seen from the side so the oval shape is obvious, plain cream background.
```

### `k1-shape-pizza` — circle 圆形

- **存为**：`k1-shape-pizza.png`
- **所属**：k1-shape-circle
- **画面要能回答**：What is like a circle?

```
one whole round pizza seen from directly above, perfectly circular, plain cream background, the round shape is obvious.
```

### `k1-shape-bus` — rectangle 长方形

- **存为**：`k1-shape-bus.png`
- **所属**：k1-shape-square
- **画面要能回答**：What is like a rectangle?

```
one yellow school bus seen from the side so its long rectangular body is obvious, plain soft background.
```

### `k1-shape-toast` — square 正方形

- **存为**：`k1-shape-toast.png`
- **所属**：k1-shape-square
- **画面要能回答**：What is like a square?

```
one square slice of toasted bread seen from directly above, clearly square with four equal sides, plain cream background.
```

### `k1-shape-sandwich` — triangle 三角形

- **存为**：`k1-shape-sandwich.png`
- **所属**：k1-shape-triangle
- **画面要能回答**：What is like a triangle?

```
one triangular sandwich half seen from directly above, clearly a triangle with three sides, plain cream background.
```

### `k1-shape-kite` — diamond 菱形

- **存为**：`k1-shape-kite.png`
- **所属**：k1-shape-diamond
- **画面要能回答**：What is like a diamond?

```
one diamond-shaped kite with a long ribbon tail flying in a blue sky, the diamond shape is obvious.
```

### `k1-shape-flowerpot` — trapezoid 梯形

- **存为**：`k1-shape-flowerpot.png`
- **所属**：k1-shape-trapezoid
- **画面要能回答**：What is like a trapezoid?

```
one empty terracotta flowerpot seen from the side, wide at the top and narrow at the bottom so the trapezoid shape is obvious, plain cream background.
```

## 乐器 Instruments（5 张）

### `k1-inst-piano` — piano 钢琴

- **存为**：`k1-inst-piano.png`
- **所属**：k1-instrument-piano
- **画面要能回答**：What's this musical instrument?

```
one black grand piano with the lid open and white-and-black keys clearly visible, seen from a friendly angle, plain soft background.
```

### `k1-inst-guitar` — guitar 吉他

- **存为**：`k1-inst-guitar.png`
- **所属**：k1-instrument-guitar
- **画面要能回答**：What's this musical instrument?

```
one wooden acoustic guitar standing upright with six strings visible, plain soft background.
```

### `k1-inst-violin` — violin 小提琴

- **存为**：`k1-inst-violin.png`
- **所属**：k1-instrument-violin
- **画面要能回答**：What's this musical instrument?

```
one wooden violin lying beside its bow, strings visible, plain soft background.
```

### `k1-inst-trumpet` — trumpet 小号

- **存为**：`k1-inst-trumpet.png`
- **所属**：k1-instrument-trumpet
- **画面要能回答**：What's this musical instrument?

```
one shiny golden trumpet seen from the side with its valves and bell clearly visible, plain soft background.
```

### `k1-inst-drums` — drums 鼓

- **存为**：`k1-inst-drums.png`
- **所属**：k1-instrument-drums
- **画面要能回答**：What's this musical instrument?

```
a small colorful drum set with two drums and a pair of wooden drumsticks resting on top, plain soft background.
```

## 节日 Holidays（11 张）

### `hol-christmas` — Christmas 圣诞节

- **存为**：`hol-christmas.png`
- **所属**：k1-holiday-christmas
- **画面要能回答**：What's this holiday?
- **注意**：和已有的 `sw-on-holiday-christmas`（圣诞树特写）要**明显不同** ——

```
A cozy Christmas morning scene: two happy children in red and green pajamas
sitting on a soft rug in a warm living room, a decorated Christmas tree with
glowing lights standing behind them, a brick fireplace with hanging stockings
on the side, gentle snow falling outside the window. Warm golden light,
festive and joyful mood.
```

### `hol-easter` — Easter 复活节

- **存为**：`hol-easter.png`
- **所属**：k1-holiday-easter
- **画面要能回答**：What's this holiday?
- **注意**：不要画成一篮子蛋（已有 `sw-on-holiday-egg` 是那个），这张要有「过节」的场面。

```
A cheerful spring Easter scene in a green meadow: a smiling child in a pastel
outfit kneeling on fresh grass, holding a woven basket, surrounded by pastel
painted eggs hidden among spring flowers and tulips, a soft blue sky with
fluffy clouds above. Fresh pastel colors, gentle sunshine, springtime mood.
```

### `hol-easter-bunny` — Easter Bunny 复活节兔子

- **存为**：`hol-easter-bunny.png`
- **所属**：k1-holiday-easter
- **画面要能回答**：What's this?

```
One cute fluffy white Easter bunny sitting upright in soft green grass, long
ears standing up, pink inner ears and a small pink nose, big friendly eyes,
a pastel ribbon bow around its neck, one decorated pastel egg resting beside
it. Soft cream and spring-green background. Single bunny, centered, adorable.
```

### `hol-easter-clothes` — pretty clothes 漂亮的衣服

- **存为**：`hol-easter-clothes.png`
- **所属**：k1-holiday-easter
- **画面要能回答**：What do we wear on Easter?

```
A happy child standing and showing off a pretty pastel Easter outfit: a light
yellow dress with a wide ribbon sash and a straw hat decorated with small pink
and white flowers, white shoes, arms spread cheerfully. Plain soft cream
background so the clothes are the clear subject. Fresh spring pastel palette.
```

### `hol-halloween` — Halloween 万圣节

- **存为**：`hol-halloween.png`
- **所属**：k1-holiday-halloween
- **画面要能回答**：What's this holiday?
- ⚠️ **必须可爱不吓人**：南瓜灯是笑脸，配色暖橙，不要黑暗/恐怖氛围

```
A friendly cheerful Halloween scene for young children: a big round orange
jack-o-lantern with a happy smiling carved face glowing warmly, sitting on
autumn leaves, a small cute cartoon ghost with a round smiling face floating
beside it, one friendly little bat with a smile above. Warm orange and soft
purple evening colors, cozy and playful, absolutely not scary.
```

### `hol-halloween-candies` — candies 糖果

- **存为**：`hol-halloween-candies.png`
- **所属**：k1-holiday-halloween
- **画面要能回答**：What can we get on Halloween?

```
A pile of colorful wrapped Halloween candies spilling out of an orange
pumpkin-shaped treat bucket: round lollipops, striped wrapped sweets, small
chocolate pieces in bright red, yellow, green, purple and orange wrappers.
Plain soft cream background, candies clearly separated and easy to see.
Bright, sweet and inviting.
```

### `hol-halloween-dressup` — dress up 盛装打扮

- **存为**：`hol-halloween-dressup.png`
- **所属**：k1-holiday-halloween
- **画面要能回答**：What do we do on Halloween?
- ⚠️ 装扮要可爱系（小猫、小南瓜、小巫师），不要骷髅血腥

```
Two happy young children wearing cute Halloween costumes and posing
cheerfully: one dressed as a friendly orange pumpkin with a round costume,
one dressed as a little black cat with soft ears and a tail, both smiling
brightly. Warm autumn evening background with soft orange light. Adorable and
playful, absolutely not scary.
```

### `hol-couplets` — couplets 对联

- **存为**：`hol-couplets.png`
- **所属**：k1-holiday-spring-festival
- **画面要能回答**：What can we do during Spring Festival?
- ⚠️ **这张最容易出错**：对联本体就是写着汉字的红纸条，但风格前缀要求 NO text。

```
A happy child in a red outfit standing on tiptoe and pressing a long red paper
strip onto the side of a wooden doorway, decorating for Chinese New Year; a
matching red strip already on the other side, and a red diamond-shaped paper
above the door. The red papers carry only simple gold ornamental patterns and
borders, completely blank of any writing. Warm red and gold, festive doorway
scene.
```

### `hol-dumplings` — dumplings 饺子

- **存为**：`hol-dumplings.png`
- **所属**：k1-holiday-spring-festival
- **画面要能回答**：What do we eat during Spring Festival?

```
A round plate of plump white Chinese dumplings with neatly pleated edges,
steam gently rising, arranged in a circle on a simple ceramic plate, a pair
of chopsticks resting beside, a small dish of dipping sauce. Plain warm cream
background. Appetizing, cozy and simple.
```

### `hol-lucky-money` — lucky money 压岁钱

- **存为**：`hol-lucky-money.png`
- **所属**：k1-holiday-spring-festival
- **画面要能回答**：What can we do during Spring Festival?

```
A smiling child in a red Chinese outfit holding up a bright red envelope with
both hands, receiving it happily; two more red envelopes with simple gold
decorative patterns resting beside. Plain soft cream background, the red
envelope is the clear main subject. Warm red and gold, joyful. No written
characters on the envelopes, only simple gold ornament patterns.
```

### `hol-spring-festival` — Spring Festival 春节

- **存为**：`hol-spring-festival.png`
- **所属**：k1-holiday-spring-festival
- **画面要能回答**：What's this holiday?
- **注意**：中国春节的视觉符号——红灯笼、唐装、烟花；**不要写任何汉字**

```
A joyful Chinese Spring Festival scene: two happy children in red traditional
Chinese outfits standing together and waving, round red paper lanterns hanging
above them, small colorful fireworks sparkling in the night sky behind, warm
red and gold festive colors. Cheerful family celebration mood. No written
characters anywhere.
```

---

## 出图入库后

```bash
python ingest_images.py <图片目录>

# K1 是孩子早学完的内容，一律 --backfill：不盖课堂日戳，
# 否则「按课堂复习」会冒出一堆根本没上过的假课堂
for f in lessons/k1-*.json; do python gen_audio.py "$f" --backfill; done

python check_lesson.py          # ❌ 必须清零
```