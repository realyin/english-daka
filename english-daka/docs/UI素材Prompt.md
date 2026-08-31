# UI 素材 Prompt（封面 / 贴纸 / 应用图标）

这批素材用于把界面里的装饰性 emoji（课程封面的 🦁🚏♻️、问答页的 🎤、考一考的 🎯、结算页的 🏆🎉）换成和课程配图同一套水彩风格的图片。每个代码块可单独复制到 ChatGPT 生成。

## 使用方法

1. 建议在同一个会话里连续生成；开始前可上传 `lessons/images/zoo.webp`、`street.webp`、`market.webp` 作画风参考。
2. 每次只提交一个代码块，生成一张。
3. 下载后按下面标注的文件名保存（如 `cover-zoo.png`），放进一个目录，然后：
   ```
   python ingest_images.py <那个目录>
   ```
   会自动归一化成 `lessons/images/*.webp` 入库（`ui-*` 命名会自动走贴纸支线：保留透明底、不裁 3:4）。页面代码已经在引用这些文件名，图片一入库就生效；没入库之前页面自动回退到现在的样子，不会坏。
   ⚠️ `icon-app.png` / `icon-180.png` 不要放进 ingest 的目录（或逐张 ingest 时跳过）——应用图标不属于 `lessons/images/`，按第 4 步单独处理。
4. 应用图标 `icon-app.png` 不走 ingest：在 macOS 上执行
   ```
   sips -Z 180 icon-app.png --out english-daka/icon-180.png
   ```
   生成 180×180 的主屏图标（页面里 `<link rel="apple-touch-icon">` 已指向它）。
5. 封面和贴纸里**禁止出现任何文字、字母、数字**；贴纸要透明背景。

---

## 课程封面（竖版 3:4）

### C1 · cover-zoo · At the Zoo 封面

保存为：`cover-zoo.png`

```text
Generate exactly ONE image. Do not return multiple alternatives. If this conversation contains style reference images, use them only as visual style references.

Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old.

Keep the main subject group centered, fully visible, and occupying roughly 60–75% of the frame. Leave modest breathing room above and below for later cropping.

Subject and composition:
A cheerful zoo scene as a storybook cover: a friendly lion, a small elephant and a giraffe standing together on green grass, a wooden zoo fence and leafy trees behind them, blue sky with soft clouds. All animals smiling gently at the viewer.

Do not include any text, letters, words, numbers, captions, labels, watermarks, or speech bubbles.
No borders or frames. Avoid realistic photography, scary expressions, clutter, cropped body parts, and accidental extra objects.

Output only the generated image, with no caption or explanation.
```

### C2 · cover-signs · Signs 生活标识封面

保存为：`cover-signs.png`

```text
Generate exactly ONE image. Do not return multiple alternatives. If this conversation contains style reference images, use them only as visual style references.

Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old.

Keep the main subject group centered, fully visible, and occupying roughly 60–75% of the frame. Leave modest breathing room above and below for later cropping.

Subject and composition:
A sunny street corner for kids: a friendly traffic light showing green, a striped crosswalk on the road, and one round blue street sign on a pole showing ONLY a simple white walking-person pictogram (a pictogram, not a letter). A few small trees and simple houses in the background.

The sign must show only a simple pictogram silhouette. Do not include any text, letters, words, numbers, captions, labels, watermarks, or speech bubbles anywhere, including on the signs.
No borders or frames. Avoid realistic photography, scary expressions, clutter, cropped body parts, and accidental extra objects.

Output only the generated image, with no caption or explanation.
```

### C3 · cover-recycling · Recycling 垃圾分类封面

保存为：`cover-recycling.png`

```text
Generate exactly ONE image. Do not return multiple alternatives. If this conversation contains style reference images, use them only as visual style references.

Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, simple uncluttered background, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old.

Keep the main subject group centered, fully visible, and occupying roughly 60–75% of the frame. Leave modest breathing room above and below for later cropping.

Subject and composition:
Three cute recycling bins side by side — one blue, one green, one yellow — with simple happy faces, standing on grass under a blue sky. A smiling child drops a plastic bottle into one bin. A paper sheet and a banana peel sit in front of the other bins.

The bins must be plain colored bins with no symbols printed on them. Do not include any text, letters, words, numbers, recycling logos, captions, labels, watermarks, or speech bubbles.
No borders or frames. Avoid realistic photography, scary expressions, clutter, cropped body parts, and accidental extra objects.

Output only the generated image, with no caption or explanation.
```

---

## 界面贴纸（正方形 1:1 · 透明背景）

### S1 · ui-mic · 问答闯关入口

保存为：`ui-mic.png`

```text
Generate exactly ONE image. Do not return multiple alternatives. If this conversation contains style reference images, use them only as visual style references.

A single sticker-style illustration for a children's learning app: soft watercolor style with clean rounded outlines, warm bright cheerful colors, friendly and cute, suitable for a 5-year-old. Square 1:1, ONE object only, centered, isolated on a fully transparent background (PNG with alpha). No shadow cast on the ground.

Subject:
A cute cartoon handheld microphone, slightly tilted, silver head and warm coral-pink body, with two tiny sparkles beside it.

Do not include any text, letters, words, numbers, captions, labels, watermarks, or speech bubbles.
No borders or frames. Avoid realistic photography and clutter.

Output only the generated image, with no caption or explanation.
```

### S2 · ui-target · 考一考入口

保存为：`ui-target.png`

```text
Generate exactly ONE image. Do not return multiple alternatives. If this conversation contains style reference images, use them only as visual style references.

A single sticker-style illustration for a children's learning app: soft watercolor style with clean rounded outlines, warm bright cheerful colors, friendly and cute, suitable for a 5-year-old. Square 1:1, ONE object only, centered, isolated on a fully transparent background (PNG with alpha). No shadow cast on the ground.

Subject:
A cute round dartboard with red and white rings, and one small teal dart with feather flights landing right in the golden center. Two tiny sparkles beside it.

Do not include any text, letters, words, numbers, captions, labels, watermarks, or speech bubbles.
No borders or frames. Avoid realistic photography and clutter.

Output only the generated image, with no caption or explanation.
```

### S3 · ui-trophy · 结算页奖杯

保存为：`ui-trophy.png`

```text
Generate exactly ONE image. Do not return multiple alternatives. If this conversation contains style reference images, use them only as visual style references.

A single sticker-style illustration for a children's learning app: soft watercolor style with clean rounded outlines, warm bright cheerful colors, friendly and cute, suitable for a 5-year-old. Square 1:1, ONE object only, centered, isolated on a fully transparent background (PNG with alpha). No shadow cast on the ground.

Subject:
A shiny golden trophy cup with two handles on a small base, with a happy little smiling face on the cup, tiny yellow stars and confetti dots floating around it.

Do not include any text, letters, words, numbers, captions, labels, watermarks, or speech bubbles.
No borders or frames. Avoid realistic photography and clutter.

Output only the generated image, with no caption or explanation.
```

### S4 · ui-party · 结算页庆祝

保存为：`ui-party.png`

```text
Generate exactly ONE image. Do not return multiple alternatives. If this conversation contains style reference images, use them only as visual style references.

A single sticker-style illustration for a children's learning app: soft watercolor style with clean rounded outlines, warm bright cheerful colors, friendly and cute, suitable for a 5-year-old. Square 1:1, ONE object only, centered, isolated on a fully transparent background (PNG with alpha). No shadow cast on the ground.

Subject:
A cute golden party popper cone bursting with colorful confetti ribbons and small stars in pink, yellow, green and blue, tilted at a playful angle.

Do not include any text, letters, words, numbers, captions, labels, watermarks, or speech bubbles.
No borders or frames. Avoid realistic photography and clutter.

Output only the generated image, with no caption or explanation.
```

---

## 应用图标（正方形 1:1 · 纯色背景）

### A1 · icon-app · 主屏图标

保存为：`icon-app.png`（生成 1024×1024，再按「使用方法」第 4 步缩成 icon-180.png）

```text
Generate exactly ONE image. Do not return multiple alternatives.

An app icon for a children's English learning app, 1024×1024 square. Soft watercolor style with clean rounded outlines, warm bright cheerful colors, friendly and cute, suitable for a 5-year-old.

Composition:
A solid soft light-blue background (around #EAF3FF) filling the entire square, edge to edge. Centered on it, ONE big friendly golden five-pointed star with a happy smiling face, slightly tilted, with a tiny open picture book resting at its base. The star occupies about 65% of the square. The design must stay clear and readable when scaled down to 60×60 pixels.

Do not include any text, letters, words, numbers, captions, labels, watermarks, or speech bubbles.
No borders, no frames, no rounded-corner mask (the OS applies its own mask). Avoid realistic photography, gradients on the background, and clutter.

Output only the generated image, with no caption or explanation.
```
