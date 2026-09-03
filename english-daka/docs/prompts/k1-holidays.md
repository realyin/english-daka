# 配图 Prompt · K1 T12 节日 Holidays

五节课共 16 张卡，其中 **5 张复用 K2 已有配图**（下面「已有，不用出」一节列了），
**11 张需要新出**。

出图后按每条的「**存为**」命名，然后一次入库：

```bash
python ingest_images.py <图片目录>          # 先 --dry 预览
```

文件名 = 入库名 = 卡片 `image` 字段名，一名三用，不需要编号对照表。

---

## 统一风格前缀（**每条 prompt 前面都要加**）

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
grid lines, borders, frame, collage of photos, realistic photo, scary, horror,
gore, cluttered, multiple scenes
```

> ⚠️ 万圣节那两张要特别注意 **NO scary / NO horror** —— 给 5 岁孩子看的，
> 南瓜灯要笑脸、装扮要可爱，不要恐怖元素。

---

## 已有，不用出（5 张）

| 卡片 | 复用 | 画的是 |
|---|---|---|
| Christmas tree | `sw-on-holiday-christmas.webp` | 挂满彩球的圣诞树 + 树下礼物 |
| gifts | `m-words-2-christmas.webp` | 壁炉旁的圣诞树，树下一堆彩色礼盒 |
| egg hunt | `sw-on-holiday-egg.webp` | 一篮子彩绘复活节蛋 |
| Thanksgiving | `t-words-3-thanksgiving.webp` | 烤火鸡 + 南瓜 + 秋叶的感恩节餐桌 |
| turkey | `sw-on-holiday-turkey.webp` | 整只烤火鸡配配菜 |

---

## 需要新出（11 张）

### 1. `hol-christmas` — Christmas 圣诞节

- **存为**：`hol-christmas.png`
- **画面要能回答**：What's this holiday?（这是什么节日？）
- **注意**：和已有的 `sw-on-holiday-christmas`（圣诞树特写）要**明显不同** ——
  这张画的是「过节的场面」，不是树。同一课里两张太像，考一考会分不出。

```
A cozy Christmas morning scene: two happy children in red and green pajamas
sitting on a soft rug in a warm living room, a decorated Christmas tree with
glowing lights standing behind them, a brick fireplace with hanging stockings
on the side, gentle snow falling outside the window. Warm golden light,
festive and joyful mood.
```

### 2. `hol-easter` — Easter 复活节

- **存为**：`hol-easter.png`
- **画面要能回答**：What's this holiday?
- **注意**：不要画成一篮子蛋（已有 `sw-on-holiday-egg` 是那个），这张要有「过节」的场面。

```
A cheerful spring Easter scene in a green meadow: a smiling child in a pastel
outfit kneeling on fresh grass, holding a woven basket, surrounded by pastel
painted eggs hidden among spring flowers and tulips, a soft blue sky with
fluffy clouds above. Fresh pastel colors, gentle sunshine, springtime mood.
```

### 3. `hol-easter-clothes` — pretty clothes 漂亮的衣服

- **存为**：`hol-easter-clothes.png`
- **画面要能回答**：What do we wear on Easter?

```
A happy child standing and showing off a pretty pastel Easter outfit: a light
yellow dress with a wide ribbon sash and a straw hat decorated with small pink
and white flowers, white shoes, arms spread cheerfully. Plain soft cream
background so the clothes are the clear subject. Fresh spring pastel palette.
```

### 4. `hol-easter-bunny` — Easter Bunny 复活节兔子

- **存为**：`hol-easter-bunny.png`
- **画面要能回答**：What's this?

```
One cute fluffy white Easter bunny sitting upright in soft green grass, long
ears standing up, pink inner ears and a small pink nose, big friendly eyes,
a pastel ribbon bow around its neck, one decorated pastel egg resting beside
it. Soft cream and spring-green background. Single bunny, centered, adorable.
```

### 5. `hol-halloween` — Halloween 万圣节

- **存为**：`hol-halloween.png`
- **画面要能回答**：What's this holiday?
- ⚠️ **必须可爱不吓人**：南瓜灯是笑脸，配色暖橙，不要黑暗/恐怖氛围

```
A friendly cheerful Halloween scene for young children: a big round orange
jack-o-lantern with a happy smiling carved face glowing warmly, sitting on
autumn leaves, a small cute cartoon ghost with a round smiling face floating
beside it, one friendly little bat with a smile above. Warm orange and soft
purple evening colors, cozy and playful, absolutely not scary.
```

### 6. `hol-halloween-dressup` — dress up 盛装打扮

- **存为**：`hol-halloween-dressup.png`
- **画面要能回答**：What do we do on Halloween?
- ⚠️ 装扮要可爱系（小猫、小南瓜、小巫师），不要骷髅血腥

```
Two happy young children wearing cute Halloween costumes and posing
cheerfully: one dressed as a friendly orange pumpkin with a round costume,
one dressed as a little black cat with soft ears and a tail, both smiling
brightly. Warm autumn evening background with soft orange light. Adorable and
playful, absolutely not scary.
```

### 7. `hol-halloween-candies` — candies 糖果

- **存为**：`hol-halloween-candies.png`
- **画面要能回答**：What can we get on Halloween?

```
A pile of colorful wrapped Halloween candies spilling out of an orange
pumpkin-shaped treat bucket: round lollipops, striped wrapped sweets, small
chocolate pieces in bright red, yellow, green, purple and orange wrappers.
Plain soft cream background, candies clearly separated and easy to see.
Bright, sweet and inviting.
```

### 8. `hol-spring-festival` — Spring Festival 春节

- **存为**：`hol-spring-festival.png`
- **画面要能回答**：What's this holiday?
- **注意**：中国春节的视觉符号——红灯笼、唐装、烟花；**不要写任何汉字**
  （对联那张也一样，见下）

```
A joyful Chinese Spring Festival scene: two happy children in red traditional
Chinese outfits standing together and waving, round red paper lanterns hanging
above them, small colorful fireworks sparkling in the night sky behind, warm
red and gold festive colors. Cheerful family celebration mood. No written
characters anywhere.
```

### 9. `hol-lucky-money` — lucky money 压岁钱

- **存为**：`hol-lucky-money.png`
- **画面要能回答**：What can we do during Spring Festival?

```
A smiling child in a red Chinese outfit holding up a bright red envelope with
both hands, receiving it happily; two more red envelopes with simple gold
decorative patterns resting beside. Plain soft cream background, the red
envelope is the clear main subject. Warm red and gold, joyful. No written
characters on the envelopes, only simple gold ornament patterns.
```

### 10. `hol-dumplings` — dumplings 饺子

- **存为**：`hol-dumplings.png`
- **画面要能回答**：What do we eat during Spring Festival?

```
A round plate of plump white Chinese dumplings with neatly pleated edges,
steam gently rising, arranged in a circle on a simple ceramic plate, a pair
of chopsticks resting beside, a small dish of dipping sauce. Plain warm cream
background. Appetizing, cozy and simple.
```

### 11. `hol-couplets` — couplets 对联

- **存为**：`hol-couplets.png`
- **画面要能回答**：What can we do during Spring Festival?
- ⚠️ **这张最容易出错**：对联本体就是写着汉字的红纸条，但风格前缀要求 NO text。
  解决办法：**画贴对联这个动作**，红纸上只画金色装饰花纹、不画字。

```
A happy child in a red outfit standing on tiptoe and pressing a long red paper
strip onto the side of a wooden doorway, decorating for Chinese New Year; a
matching red strip already on the other side, and a red diamond-shaped paper
above the door. The red papers carry only simple gold ornamental patterns and
borders, completely blank of any writing. Warm red and gold, festive doorway
scene.
```

---

## 出图后的步骤

```bash
python ingest_images.py <图片目录> --dry     # 先看会入库成什么名
python ingest_images.py <图片目录>

# 五节课逐个生成音频。K1 是孩子早学完的内容，一律 --backfill，
# 不盖课堂日戳（否则「按课堂复习」会冒出一堆假课堂）
for l in christmas easter thanksgiving halloween spring-festival; do
  python gen_audio.py lessons/k1-holiday-$l.json --backfill
done

python check_lesson.py        # ❌ 必须清零
```
