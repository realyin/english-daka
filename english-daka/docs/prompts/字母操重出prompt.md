# 配图 Prompt · 字母操重出（6 张必做 + 3 张可选）

> **每条 prompt 都是完整的，复制整段直接用。**「存为」= 文件名，和现有文件同名，
> 入库直接覆盖，课程 JSON 一个字都不用改。
> 出图目录：`generated-images/字母操重出prompt/`

## 为什么要重出

上一批 26 张字母操里，**凡是「侧身 / 扭腰 / 转头」的姿势，AI 都把人画坏了**；
凡是**正面站直、只用胳膊摆字母**的，26 张里一张没坏。这不是随机翻车，是姿势选型的问题——
所以这次不是把同样的 prompt 再跑一遍，而是**把这 6 个字母的姿势全部改成正面站姿**。

对照（现有图的实际毛病）：

| 字母 | 现在坏在哪 | 原 prompt 里的姿势 |
|---|---|---|
| **C** | 身子朝左弯、头却拧成正脸，脖子像断的；下面那条胳膊从胸口长出来，没有肩膀 | standing sideways and curving the whole body |
| **M** | 两条胳膊糊成一坨、末端却有两只手；侧身趴着但头转成正脸 | on all fours, seen from the side |
| **P** | **少一条胳膊**；剩下那条绕回来，手接在自己的胳膊肘上 | one arm curved back to the hip |
| **G** | 第二条胳膊是**没有手的断肢**，末端一团白 | squatting and curving sideways |
| **E** | 下面那条胳膊从**腰上**长出来，没有肩膀，像第三只手 | standing sideways, both arms forward |
| **J** | 空着的那条小臂**悬在半空**，和身体不相连 | one arm up, one leg bent |

新 prompt 三处硬约束（每条里都写死了）：

1. **正面站立**——`squarely facing the viewer`，脸朝前、肩膀齐、腰不拧、明令 `not a side view`
2. **字母只用胳膊摆**，躯干保持直立当竖笔画；不弯腰、不趴地、不侧倒
3. **闲着的那条胳膊必须交代清楚**——垂在身侧且手可见，这是 P/G/J 断肢的直接来源

⚠️ 摆的字形和课上一致：C/E/G/P 是**大写**，j/m 是**小写**，别弄反。

---

## 必做 6 张

### 1. `k1-pose-c` — 大写 C

**存为**：`k1-pose-c.png`　／　**这一问**：`Can you show me letter C?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright and not twisted, not bending sideways. Normal human anatomy: exactly two arms, two hands, two legs and two feet, both legs and both feet clearly visible and separated, every limb growing from the correct shoulder or hip and fully connected, clear natural elbows and knees, normal child limb proportions. The child uses only the arms to act out a letter: both arms are held out in front of the body and curved strongly toward the child's left, the upper arm arcing above the head with the hand reaching left, the lower arm arcing at waist height with the hand reaching left, the two hands clearly apart so a wide open gap is left on the right side, the two curved arms together drawing a big open capital letter C. Full body visible from head to toe, the arm shape unmistakable. Playful gymnastics pose, happy expression. NO side view, NO profile view, NO twisted neck, NO bent-over torso, NO floating or detached limbs, NO arm growing out of the chest or the waist, NO arm ending without a hand, NO missing, duplicated or merged limbs. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

### 2. `k1-pose-e` — 大写 E

**存为**：`k1-pose-e.png`　／　**这一问**：`Can you show me letter E?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright and not twisted, not bending sideways. Normal human anatomy: exactly two arms, two hands, two legs and two feet, both legs and both feet clearly visible and separated, every limb growing from the correct shoulder or hip and fully connected, clear natural elbows and knees, normal child limb proportions. The child uses only the arms to act out a letter: the left arm reaches straight out sideways at shoulder height with the palm flat, and the right arm is held low across the front of the tummy with the right hand also pointing out to the same side at waist height, the two arms clearly separated with a visible gap between them so they read as two stacked horizontal bars, the upright body making the tall spine of a capital letter E. Full body visible from head to toe, the arm shape unmistakable. Playful gymnastics pose, happy expression. NO side view, NO profile view, NO twisted neck, NO bent-over torso, NO floating or detached limbs, NO arm growing out of the chest or the waist, NO arm ending without a hand, NO missing, duplicated or merged limbs. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

### 3. `k1-pose-g` — 大写 G

**存为**：`k1-pose-g.png`　／　**这一问**：`Can you show me letter G?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright and not twisted, not bending sideways, not squatting. Normal human anatomy: exactly two arms, two hands, two legs and two feet, both legs and both feet clearly visible and separated, every limb growing from the correct shoulder or hip and fully connected, both hands fully drawn with fingers, clear natural elbows and knees, normal child limb proportions. The child uses only the arms to act out a letter: both arms are held out in front of the body and curved strongly toward the child's left like a big open C, the upper arm arcing above the head and the lower arm arcing at waist height, and the lower hand is turned inward so the fingers point back toward the middle of the chest, adding the small inward bar of a capital letter G. Full body visible from head to toe, the arm shape unmistakable. Playful gymnastics pose, happy expression. NO side view, NO profile view, NO twisted neck, NO bent-over torso, NO floating or detached limbs, NO arm growing out of the chest or the waist, NO arm ending without a hand, NO stump, NO missing, duplicated or merged limbs. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

### 4. `k1-pose-j` — 小写 j

**存为**：`k1-pose-j.png`　／　**这一问**：`Can you show me letter J?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright and not twisted. Normal human anatomy: exactly two arms, two hands, two legs and two feet, every limb growing from the correct shoulder or hip and fully connected all the way from shoulder to fingertips, clear natural elbows and knees, normal child limb proportions. The child acts out a letter: the right arm is raised straight up above the head with the index finger pointing at the sky, the left arm hangs straight down close to the body with the whole arm from shoulder to hand clearly visible beside the hip, and the left foot is swung out sideways at the bottom so it hooks outward, the raised fingertip reading as the dot and the upright body with the hooked foot reading as the tail of a lowercase letter j. Full body visible from head to toe, the shape unmistakable. Playful gymnastics pose, happy expression. NO side view, NO profile view, NO twisted neck, NO floating or detached limbs, NO forearm separated from the shoulder, NO arm growing out of the chest or the waist, NO arm ending without a hand, NO missing, duplicated or merged limbs. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

### 5. `k1-pose-m` — 小写 m

**存为**：`k1-pose-m.png`　／　**这一问**：`Can you show me letter M?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright on both feet and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright, standing on two feet and definitely not on all fours, not crawling, not bending over. Normal human anatomy: exactly two arms, two hands, two legs and two feet, both legs and both feet clearly visible and separated, every limb growing from the correct shoulder or hip and fully connected, clear natural elbows and knees, normal child limb proportions. The child uses only the arms to act out a letter: both arms are raised out to the sides at shoulder height and bent sharply straight down at the elbows so both forearms hang vertically, making two matching rounded arches, one on the left of the head and one on the right, perfectly symmetrical, together drawing the two humps of a lowercase letter m. Full body visible from head to toe, the arm shape unmistakable. Playful gymnastics pose, happy expression. NO side view, NO profile view, NO twisted neck, NO crawling pose, NO hands on the ground, NO floating or detached limbs, NO arm growing out of the chest or the waist, NO arm ending without a hand, NO missing, duplicated or merged limbs, NO two hands on one arm. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

### 6. `k1-pose-p` — 大写 P

**存为**：`k1-pose-p.png`　／　**这一问**：`Can you show me letter P?`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright and not twisted. Normal human anatomy: exactly two arms, two hands, two legs and two feet, both arms present and both clearly visible, both legs and both feet clearly visible and separated, every limb growing from the correct shoulder or hip and fully connected, clear natural elbows and knees, normal child limb proportions. The child uses only the arms to act out a letter: the right arm is raised from the shoulder and curved forward and around so the right hand comes back and rests on the upper chest near the collarbone, closing a clear round loop beside the head and upper body, while the left arm hangs straight down close to the body with the whole arm from shoulder to hand clearly visible beside the hip, the upright body making the stem and the round loop at the top making a capital letter P. Full body visible from head to toe, the arm shape unmistakable. Playful gymnastics pose, happy expression. NO side view, NO profile view, NO twisted neck, NO missing arm, NO one-armed child, NO hand attached to an elbow, NO floating or detached limbs, NO arm growing out of the chest or the waist, NO arm ending without a hand, NO missing, duplicated or merged limbs. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

---

## 可选 3 张（不吓人，但也不对）

这三张的毛病是**两条腿糊成一条 / 一条胳膊几乎没画出来**，小图上不容易看出来，
你觉得无所谓就跳过；要一起重出就用下面的 prompt。

### 7. `k1-pose-b` — 小写 b（现在只有一条腿一只脚）

**存为**：`k1-pose-b.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright. Normal human anatomy: exactly two arms, two hands, two legs and two feet, the two legs clearly separated with a visible gap between them and both feet flat on the ground and fully drawn, every limb growing from the correct shoulder or hip and fully connected, clear natural elbows and knees, normal child limb proportions. The child uses only the arms to act out a letter: the left arm is raised straight up above the head making a tall straight stem, and the right arm is curved forward from the shoulder down to the waist with the right hand resting on the tummy so the arm closes a round belly shape on the lower half of the body, together drawing a lowercase letter b. Full body visible from head to toe, the shape unmistakable. Playful gymnastics pose, happy expression. NO side view, NO profile view, NO twisted neck, NO single leg, NO merged legs, NO missing foot, NO floating or detached limbs, NO arm growing out of the chest or the waist, NO arm ending without a hand. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

### 8. `k1-pose-d` — 小写 d（左胳膊只剩一只手贴在肚子上）

**存为**：`k1-pose-d.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright. Normal human anatomy: exactly two arms, two hands, two legs and two feet, the two legs clearly separated and both feet fully drawn, every limb growing from the correct shoulder or hip and fully connected, both arms drawn completely from shoulder to elbow to hand with nothing hidden behind the body, clear natural elbows and knees, normal child limb proportions. The child uses only the arms to act out a letter: the right arm is raised straight up above the head making a tall straight stem, and the left arm is curved forward from the shoulder down to the waist with the left hand resting on the tummy so the arm closes a round belly shape on the lower half of the body, together drawing a lowercase letter d. Full body visible from head to toe, the shape unmistakable. Playful gymnastics pose, happy expression. NO side view, NO profile view, NO twisted neck, NO merged legs, NO floating or detached limbs, NO shoulder hidden behind the torso, NO arm growing out of the chest or the waist, NO arm ending without a hand. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

### 9. `k1-pose-f` — 小写 f（现在只有一条腿一只脚）

**存为**：`k1-pose-f.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright. Normal human anatomy: exactly two arms, two hands, two legs and two feet, the two legs clearly separated with a visible gap between them and both feet flat on the ground and fully drawn, every limb growing from the correct shoulder or hip and fully connected, clear natural elbows and knees, normal child limb proportions. The child uses only the arms to act out a letter: the left arm is raised high and curved gently over the top of the head with the hand hanging forward, making the hook at the top, and the right arm reaches straight out sideways at chest height with the palm flat, making the crossbar, the upright body making the stem of a lowercase letter f. Full body visible from head to toe, the shape unmistakable. Playful gymnastics pose, happy expression. NO side view, NO profile view, NO twisted neck, NO single leg, NO merged legs, NO missing foot, NO floating or detached limbs, NO arm growing out of the chest or the waist, NO arm ending without a hand. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

---

## 出完之后

图丢进 `generated-images/字母操重出prompt/`，文件名就是上面的「存为」名，然后：

```bash
python3 ingest_images.py generated-images/字母操重出prompt
```

同名覆盖，**课程 JSON 一个字都不用改**（`image` 字段指的就是这些名字）。
我这边再 bump 一次 `sw.js` 版本号，让装过 PWA 的平板刷掉旧图。

---

# 第二批 · 2 张必重出 + 2 张可选（镜像修正）

**第一批结果**：9 张里 7 张过（b c e f g j m），已入库。姿势全部改成正面站姿之后，
**断肢、糊肢、拧脖子一例都没有**——姿势选型这条路走通了。扣下 2 张，原因不是画坏了，是**画错了**。

## 必重出

### 10. `k1-pose-p` — 大写 P（姿势跑偏了）

**存为**：`k1-pose-p.png`

第一批那张**双手举过头顶**，根本没有 P 的那个圈，而且和同一课的 `k1-pose-o`（双臂头顶抱圆）
撞脸——O 和 P 在同一节课 `k1-letter-mnop` 里，一课两张一样的图。

原 prompt 说「手绕回来贴住锁骨」太抽象了，这次改成一个具体的、孩子做得出来的动作：
**手臂侧平举再屈肘、指尖点在脖子边上**，胳膊和脑袋之间就空出一个圆洞——那就是 P 的圈。

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright and not twisted, standing on two feet. Normal human anatomy: exactly two arms, two hands, two legs and two feet, both arms present and both clearly visible, both legs and both feet clearly visible and separated, every limb growing from the correct shoulder or hip and fully connected, clear natural elbows and knees, normal child limb proportions. The child acts out a letter with one arm only: the right arm is lifted straight out to the side at shoulder height and then bent sharply at the elbow so the forearm comes back inward and the fingertips touch the side of the neck, so that the upper arm, the forearm and the head enclose a clear empty round hole high up beside the head, and this closed loop is the bowl at the top of a capital letter P; meanwhile the left arm hangs straight down close to the body with the whole arm from shoulder to hand clearly visible beside the hip, and the upright body is the tall stem of the P. Full body visible from head to toe, the closed round loop beside the head clearly readable. Playful gymnastics pose, happy expression. IMPORTANT: only ONE arm is lifted, the other arm hangs down at the side. NOT both arms raised, NOT both arms above the head, NO arms overhead, NO circle above the head, NO hands touching above the head. NO side view, NO profile view, NO twisted neck, NO missing arm, NO one-armed child, NO hand attached to an elbow, NO floating or detached limbs, NO arm growing out of the chest or the waist, NO arm ending without a hand. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

### 11. `k1-pose-d` — 小写 d（画成了 b）

**存为**：`k1-pose-d.png`

第一批那张身体没毛病，但**举起的那条胳膊在画面左边**——和同一批的 `k1-pose-b` 一模一样，
看上去是个 **b**。b 和 d 在同一节课 `k1-letter-abcd`，而 b/d 分不清正是这个年纪最典型的错，
拿一张 b 的图去教 d，比现在那张胳膊没画全的还糟，所以没入库。

**这一张唯一要盯的就是左右**：竖的那笔（举起的胳膊）必须在**画面右边**，圆肚子在**画面左边**。

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright, standing on two feet with the two legs clearly separated and both feet fully drawn. Normal human anatomy: exactly two arms, two hands, two legs and two feet, both arms drawn completely from shoulder to elbow to hand with nothing hidden behind the body, every limb growing from the correct shoulder or hip and fully connected, clear natural elbows and knees, normal child limb proportions. The child uses only the arms to act out a letter: the arm on the RIGHT-HAND SIDE OF THE PICTURE is raised straight up above the head, tall and vertical, making the straight stem; the arm on the LEFT-HAND SIDE OF THE PICTURE curves forward from the shoulder down to the waist with that hand resting on the tummy, closing a round belly shape on the lower LEFT of the body. LAYOUT IS CRITICAL: the tall straight raised arm must be on the RIGHT side of the image and the round belly curve must be on the LEFT side of the image, so the whole figure reads as a lowercase letter d and NOT as a lowercase letter b. Full body visible from head to toe, the shape unmistakable. Playful gymnastics pose, happy expression. NO mirrored layout, NO raised arm on the left side of the image, NO side view, NO profile view, NO twisted neck, NO merged legs, NO floating or detached limbs, NO arm growing out of the chest or the waist, NO arm ending without a hand. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

## 可选 2 张（左右反了，但不难看）

已入库的 c 和 f 身体都是好的，只是**字形左右反了**：C 的开口朝左（成了 `Ɔ`），f 的钩和横都朝左。
比原来那两张（断脖子 / 一条腿）强得多，所以我先上了。你觉得反着别扭就补这两张，同名覆盖。

### 12. `k1-pose-c` — 大写 C（开口要朝右）

**存为**：`k1-pose-c.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright and not twisted, standing on two feet. Normal human anatomy: exactly two arms, two hands, two legs and two feet, both legs and both feet clearly visible and separated, every limb growing from the correct shoulder or hip and fully connected, clear natural elbows and knees, normal child limb proportions. The child uses only the arms to act out a letter: both arms are held out in front of the body and curved so that BOTH HANDS REACH TOWARD THE RIGHT-HAND SIDE OF THE PICTURE, the upper arm arcing above the head with that hand ending on the right, the lower arm arcing at waist height with that hand also ending on the right, the two hands clearly apart so a wide open gap is left on the RIGHT side of the picture while the child's body closes the curve on the LEFT side, together drawing a big open capital letter C that opens to the right. LAYOUT IS CRITICAL: the opening of the C must be on the RIGHT of the image, not the left, so it does not look like a backwards C. Full body visible from head to toe, the arm shape unmistakable. Playful gymnastics pose, happy expression. NO backwards C, NO mirrored layout, NO side view, NO profile view, NO twisted neck, NO bent-over torso, NO floating or detached limbs, NO arm growing out of the chest or the waist, NO arm ending without a hand. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

### 13. `k1-pose-f` — 小写 f（钩和横都要朝右）

**存为**：`k1-pose-f.png`

```
Children's picture book illustration, soft watercolor style with clean rounded outlines, warm bright cheerful colors, plain soft pale-yellow watercolor wash background, single clear subject centered in frame, vertical 3:4 composition, friendly and cute, suitable for a 5-year-old. Exactly one cheerful young child standing upright and squarely facing the viewer, front view only, face looking straight at the viewer, neck straight and untwisted, shoulders square to the camera, torso upright, standing on two feet with the two legs clearly separated and both feet fully drawn. Normal human anatomy: exactly two arms, two hands, two legs and two feet, every limb growing from the correct shoulder or hip and fully connected, clear natural elbows and knees, normal child limb proportions. The child uses only the arms to act out a letter: the arm on the LEFT-HAND SIDE OF THE PICTURE is raised high and curved gently over the top of the head so that its hand ends on the RIGHT-HAND SIDE of the head, making a hook that curls to the right; the arm on the RIGHT-HAND SIDE OF THE PICTURE reaches straight out sideways to the right at chest height with the palm flat, making the crossbar pointing right; the upright body is the stem of a lowercase letter f. LAYOUT IS CRITICAL: both the top hook and the crossbar must point toward the RIGHT of the image, not the left, so it does not look like a backwards f. Full body visible from head to toe, the shape unmistakable. Playful gymnastics pose, happy expression. NO backwards f, NO mirrored layout, NO side view, NO profile view, NO twisted neck, NO single leg, NO merged legs, NO floating or detached limbs, NO arm growing out of the chest or the waist, NO arm ending without a hand. NO speech bubbles, NO labels, NO borders, NO frames, NO written words, NO letters, NO numbers, not scary, not cluttered.
```

---

**第二批出完照旧**：丢进 `generated-images/字母操重出prompt/`，然后

```bash
python3 ingest_images.py generated-images/字母操重出prompt
```
