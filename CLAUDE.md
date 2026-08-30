# 英语打卡（english-daka）

给孩子（K2 幼儿园水平）做的英语每日打卡学习应用。纯前端、零构建、零依赖，
本地 `python3 -m http.server` 即可运行。项目代码在 `english-daka/` 子目录。

## 运行

```bash
python3 -m http.server 8123 -d english-daka
# 打开 http://localhost:8123  （.claude/launch.json 已配置同名 preview）
```

## 架构

- `english-daka/index.html` — 课程目录页：每个 `group` 渲染成一个**专辑封面流**
  （coverflow）——中间卡正面最大、左右卡 `rotateY` 折叠并随角度加深阴影，
  可拖动/点侧卡/点圆点/方向键切换，点中间那张才进课程。封面色按组内序号
  循环取 `--c1..--c5`（比主题色深一档，保证白色巨型字形对比度达标）。
  ⚠️ `html{overflow-x:hidden}` **不能删**：折叠到最外侧的卡片会被 `translateX`
  甩出 `.stage`（它是 `overflow:visible`），整页因此横向可滚——414px 宽实测能滚
  290px。手指在封面流上横划时浏览器会顺手平移整页，看着就是整个页面在抖。
  只写在 `body` 上没用（body 自己变成滚动容器，不再往视口传递）。
- `english-daka/app.html` — 单文件应用，三个模块：
  - **学一学**：卡片 + 中英问答对话，点单词点读、长按查词典、点空白播整句
  - **问答闯关**：听题目→孩子大声说答案→点选答案（3 选 1）。
    ⚠️ 语音识别已移除（对儿童英语识别太差，别加回来）；判分靠点选。
    **题目进题就自动播**（孩子还不认字，题面对他就是一串图形，不出声没法答，
    每题先按一下按钮纯属多一道手续）；要重听点问题气泡或气泡里的 🔊。
    ⚠️ **但选项仍然手动**（「🔊 听选项」）——认得的词他会伸手就点，
    自动念选项会变成边选边播。
    ⚠️ **不自动翻页**：答对后**停在原地**，绿色选项留着，出口是
    「👀 看答案 / 下一题 ➜」——以前会 2.6 秒自动翻到答案页，
    孩子正要点下一题画面就跳走了。
  - **考一考**：听音选卡（预生成的 "Which one is …?" 提问）。
    只收「一图一词」的卡片：`quiz: false` 的卡和无图无算式无 emoji 的卡都排除；
    可用卡 < 2 张整栏隐藏
- 闯关和考一考每轮抽题上限 `ROUND_MAX = 12`（app.html）。整课 25 问对 K2
  太长，而打卡是天天来的——每次随机抽一轮，几天下来自然覆盖全课
- `english-daka/theme.css` — 主题 token（字体/配色/线条/阴影），两页面共用。
  字体栈英文圆体优先、中文回落苹方；**不要把 PingFang 放第一位**（英文会难看）
- 课程数据：`lessons/<课程id>.json`，结构与建课流程见
  `english-daka/docs/课程制作指南.md`（改课程/建课前先读它）
- `english-daka/docs/排障记录.md` — 线上发现、开发机不易复现的问题记录（症状 →
  走过的弯路 → 怎么量准 → 根因 → 验证数字）。遇到"平板上不对但本地看着好好的"
  先翻它；里面也有拍屏视频测位移、量页面溢出的可复用方法

## 关键脚本（都在 english-daka/ 下运行）

- `python3 new_lesson.py 21 "标题"` — 新课脚手架（课号标识，不用日期）
- `python3 gen_audio.py lessons/x.json` — 生成句子/单词/鼓励语/考题音频，
  回写 JSON 并自动更新 index.json
- `python3 gen_phonics.py` — 拼读音素公共库（lessons/phonics.json，87 个音）；
  `--blends lessons/x.json` 生成"m→an→man"串联音频
- `python3 add_image.py 原图.png 语义名` — 单张配图归一化（3:4 720×960 webp ≤150KB）
- `python3 split_panels.py [--dry]` — 聚合拼图（2×2/三格）按格切成单图并回填
  `dialog[].image`；每格坐标写死在脚本的 PANELS 表里，改图后要同步改坐标
- `python3 ingest_images.py <目录> [--dry]` — 批量入库新配图；编号→文件名的映射
  自动从 `docs/配图Prompt清单.md` 的表格解析（该文档是 116 条配图 prompt 的清单）

## 音频体系约定（重要）

- **角色→音色只在 gen_audio.py 的 ROLES 表定义**（q=Ana 童声, a=Jenny,
  word=Jenny 慢速, praise=Ana）。任何地方不得手写音色，避免一句话混音色。
- 改音色或改音素库后重跑任意一课：脚本对比 `lessons/audio/voices.json`
  （角色音色 + `_phonics` 音素库指纹）自动全量刷新——音色变了刷该角色的
  全部音频，音素库变了刷所有含 `/x/` 的拼接句。两种情况都还要另跑
  `gen_phonics.py --blends <课程>` 重建 CVC 课的拼读串联音频。
- 目录布局：`sentences/<课程id>/`（课程专属）、`words/`、`praise/`、
  `phonics/`（全局池，按文本内容命名，跨课自动复用去重）。
- 音素纯音不能让 TTS 直接念文本（会念字母名），gen_phonics.py 每个音
  有专门配方；改动后用 whisper 转录校验 + 人耳抽查。**校验重点是"呃"音**：
  `initial` 配方从 "dah/bah" 载体音节里截辅音，必须按能量切在元音起头处
  （`vowel_onset()`），截固定长度会把整个元音留下来，`/d/` 就变成 "duh"。
  whisper 把纯音转成 "Duh"/"Bye" 这类词，就是切多了。
- **句子里的 `/s/` `/a/` 这类音标同样不能交给 TTS 读**：TTS 会念成字母名
  （"S says /s/" → "ess says ess"，咝音根本不存在）。gen_audio.py 遇到 `/x/`
  自动改为拼接：TTS 念文字段 + 插入 audio/phonics/ 的纯音（记号→库 key 的
  映射见 PHONEME_MAP，元音要转：/a/→ae、/o/→aa、/i/→ih，另有 /ks/→x、
  /kw/→qu；app.html 里有一份同样的表，改一处要同步）。新写课文时放心用
  `/x/` 记号，脚本会处理；但音标只能出现在回答句（与音素库同为 Jenny 音色）。
  拼接的停顿分两档：音与音之间 `GAP_MS`=100ms，**逗号处 `GAP_PUNCT_MS`=620ms**
  ——"/d/ /a/ /d/, dad." 拼完三个音要停一拍再说整词，四个停顿等长会听成
  "d-a-d-dad" 四个并排的音。改停顿参数会进 `_phonics` 指纹，重跑任意一课自动全量刷新。
- **拼读句绝不能写成 "C-at, cat."**（字母-韵脚形式）：不含 `/x/` 就整句交给
  TTS，字母念成字母名——C-at → "see-at"（whisper 听成 "Seattle"）、M-an →
  "em-an"，把"c 发 /k/"这个教学点念反了。写 `"/k/ /at/, cat."`。
  **提问句里的部件用破折号断开**："How do you read f and an?" 会被一口气念完
  （零停顿）→ 写 "How do you read: f — an?"（停顿 300/670ms）。and /ænd/ 和
  an /æn/ 是近音必须去掉。**` — ` 在 gen_audio.py 里是真停顿**:TTS 句内标点
  硬上限 ~300ms,所以 `stretch_beat()` 整句渲染一次、再把破折号处那段静音撑到
  `GAP_PUNCT_MS`。**不能改成拆句分别合成**——孤立的 "an?" 会被 TTS 当成不定
  冠词弱读成 /ən/(schwa+n,听着只剩一个 "n");整句里它在句尾拿到重音才是 /æn/。
  短词的发音取决于句子上下文,所以整句渲染、只动静音。
  两类写法 `lint_lesson()` 都会在合成前扫出来并警告。

## 数据约定

- 课程标识：新课用课号（`"num": 20`，文件名 `20-标题slug.json`）；
  K2 课程用 `seq`（topic*100+序号）+ `group` + `badge` 分组展示。
  分组段位按**学习路径**排，目录页的组序就是 seq 段序：
  1xx 字母 → 2xx 词族 → 3xx 拼读 → 4xx 常见词 → 5xx 主题 → 6xx 数学
  → 7xx 科学（8xx 留给未做的绘本）。先认字母和音，再韵脚成块，再整词拼读
- 卡片判分关键词 `key` = 该题正确答案（小写单词）；闯关选项从本课 key 池抽取，
  同课内各题 key 尽量不重复
- **答案是音时，key 就写音标**：`"What sound does sea begin with?"` 的 key 是
  `["/s/"]`，不是 `["sea"]`（sea 是题干里的词，不是孩子该说的答案）。
  闯关识别到 `/x/` 形状的 key 会改从音标池抽干扰项（app.html 的
  `PHONEME_CHIPS` / `RIME_CHIPS`），变成真正的听音辨音题
- **一张卡 = 一个词条 = 一张图**。卡片的 `word` 必须是孩子要学的那个词，
  不能是 "more T words"、"face and fingers"、"sort it out" 这种教材页标题——
  考一考的提问是 `"Which one is " + card.word`，页面标题问不出题。
  原始课件一页四格的，用 split_panels.py 切图后按格拆成四张卡
- 实在拆不动的卡（拼读串联、"这是什么词族"这类无实物可画的题）加
  `"quiz": false` 挡在考一考外面；这是例外，不是常态
- 没有配图的卡填 `emoji`，学一学/闯关/考一考都会拿它当图用；出图后补
  `image` 字段即可，emoji 自动退居备胎
- 数学算式卡用 `"eq": "9-1"`（渲染彩色数字块），不用 keycap emoji（丑且不一致）
- `q_audio/a_audio/quiz_audio/word_audio/praise_audio` 由 gen_audio.py 回写，手写课程勿填
- `lessons/index.json` 由脚本维护，勿手改

## 原始素材与遗留

- `lessons/lessons_original/K2/` — 原始课件（topic 分层，文件夹内文本↔图片对应）。
  已全部转换为 k2-*.json（除 `05_books/` 纯图片绘本，待做绘本阅读模式）
- 日期命名的课已全部退役：`2026-08-30`（27 张卡的 CVC 大课）已按元音拆成
  `k2-cvc-a/i/o/eu/magic-e` 五课，归入新的「拼读 Phonics」组（seq 301–305）
- **仍缺 15 个字母**（c e g h j k l p q u v w x y z），字母课停在 11 节（seq 101–111）。
  词族/CVC 课已经在用 c g h j k l p v 的音（cat、hat、log、gum、pot、van、kid），
  但**这些字母孩子还没学到**——等课上学到哪个就补哪个，用户手里有对应材料，
  不要提前批量造课
- 聚合卡、字母卡里「讲别的词」的问答都已拆成一图一词；29 节课 259 张卡，
  每张卡一个词条一张图，考一考全部可用
- 迁移备份 `audio/_old_hashed/`、`audio/phonics_backup/` 已清理，不存在了
- 仓库还有两个大目录：`generated-images/`（248M，116 张配图的原始 PNG，已全部
  入库成 webp）、`lessons_original/`（168M，线下课原始课件，建课的唯一来源）。
  前者理论上可删，后者**不能删**——新课都要从它来。删前问用户
- `split_panels.py` 的 PANELS 表是按**拆卡之前**的问答下标写的，对已拆的卡
  已经对不上；脚本有守卫会跳过并报「卡片已被拆过」，不会写错。要重切那些卡
  得先更新 PANELS 表
