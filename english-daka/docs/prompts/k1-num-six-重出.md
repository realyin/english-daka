# 配图 Prompt · `k1-num-six` 重出（1 张）

> **整段复制直接用。**「存为」= 文件名 = 卡片里的 `image` 名，和现有文件**同名**，入库即覆盖。

## 为什么重出、为什么换物品

`k1-number-6-10` 的 `six` 卡例句原来是 **How many horns are there? / There are six horns.**，配图是六根金色管子，大人也认不出。

线下课件（`01 英语整理.md` 第 129–133 行）原话就是 horns，但中文注释明确写着：

> 这里有多少个喇叭？**（物品可以替换）**

教学点是**数到六**，物品本身线下课就允许换。第一版想画成小号，但 `trumpet` 本身就是一张卡（K1 乐器课、K2 字母 T 课都有），画成小号会让孩子把两个词混掉——所以不用乐器，换物品。

**换成 gifts（礼物）**：K1 圣诞课已经教过、有配图；六个包好的礼物盒是离散的、一眼能数；和任何数数题都不撞车；和乐器毫无关系。例句已改为：

```
How many gifts are there?  →  There are six gifts.
```

key 仍是 `six`。音频和闯关的两条干扰句按新句子重建，不用你管。

## `k1-num-six` — six 六

**存为**：`k1-num-six.png`　／　**要能回答**：What's this number? · How many gifts are there?

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly SIX wrapped gift boxes, each a small cube box in bright wrapping paper with a big ribbon bow on top, each box a different cheerful color (red, blue, yellow, green, pink, orange), all the same size. Arranged neatly in two rows of three, evenly spaced with clear gaps between them so each box can be counted at a glance, sitting on a plain soft cream background. The objects must be instantly recognizable as gift boxes. NO text, NO letters, NO words, NO numbers, NO labels, NO borders, NO frames, NO people, NO hands, NO Christmas tree, not cluttered.
```

⚠️ 数量必须**正好六个**、两行三个——这张图是拿来数数的，多一个少一个都是错题。出完请放大数一遍。

## 出完之后

```bash
python3 ingest_images.py <图片目录> --dry
python3 ingest_images.py <图片目录>
```

同名覆盖，不用改任何 JSON（例句我已经改好）。我入库后会：从 webp 复核确实是六个、封面和学一学/考一考三处都换过来、bump sw、提交。

## 备选

要是你更想要别的，饺子（dumplings，K1 春节课教过）也满足全部条件，只是六个饺子在盘里容易挤成一团、不如礼物盒好数。说一声就换。
