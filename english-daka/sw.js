/* ================================================================
   Service Worker —— 让「天天打卡」在没网/网差的时候也能打开。
   这里可以用现代语法:SW 本身只在支持它的内核上跑,注册处已经探测过
   'serviceWorker' in navigator,老浏览器根本不会加载这个文件。
   (app.html / index.html 的 <script> 顶层仍然是 ES5 安全区,别混淆。)

   ⚠️ 不做全量预下载。整站音频 47MB,装一次 App 就闷头拉 47MB
   对家里的流量和一台低端平板都不友好,而且大部分课孩子这周根本不会点。
   策略是「边用边缓」:今天在线学过的课,明天没网也能原样再学一遍。

   ⚠️ 更新策略:HTML 和 lessons/*.json 一律 network-first。
   壳(app.html)是 cache-first 的话,改了代码上线,用户手里永远是旧版本,
   而且他不会知道 —— 没有版本号可看,页面也不会报错,只是行为对不上。
   联网时永远拿新的、断网时才回缓存,是这个应用唯一说得通的取舍。
   改 precache 清单或缓存策略时,把 CACHE 的版本号往上加一位,
   activate 会把旧版整个删掉。
   ================================================================ */
const CACHE = "daka-v44";   // v44:收起卡的旗子一律隐藏(插旗态也不再残留);v43:音频预取改 fetch(媒体元素 preload 会触碰音频栈,蓝牙上每批一声"嗯嗒");v42:日历规则文案改精确(点开 3 张不同的卡即点亮/重复不计/不足 3 张不折算);v41:去掉手势换课的「已切到·撤销」提示条(顶栏课名+滑动方向已足够,黑条多余;main 侧 v40 已被占用,让号);v40:日历色阶四档扩六档(数组驱动分档);v39:课程页 html 封 overflow-x(换课/换题的平移过渡不再闪横向滚动条;main 侧 v38 已被日历整月窗口占用,让号);v38:日历默认窗口按整月起画(固定 12 周会把第一个月拦腰截断,标签间距忽宽忽窄);v37:日历行标补日;月份标签钉在含 1 号的列(不漂移,月初当天即标出新月);v36:打卡日历去掉今天的蓝圈(读作被选中)+四档绿明度差拉开;networkFirst 强制 no-cache 再验证(裸 fetch 会吃浏览器启发式缓存,网络优先拿回旧文件);v35:结果 emoji 行高写死 50px(min-height 44 挡不住真实行高,答对页面长 6px);v34:闯关答对后 hint 行改隐形占位,页面不再突然变短上跳;v33:货架连续拖动防打架(按下瞬时 scrollTo 掐掉上一次松手的 smooth 滑行,再记起点);v32:收起卡的小旗防误触(未插旗隐形占位,插旗只展示;展开后才可点);v31:窄屏打卡条独占一行铺满卡宽,七点均匀摊开+连胜收尾(折行右挂难看,实测点名);v30:打卡条改为只包住内容(悬停底色不再铺满整行空白),连胜三位数+窄屏时自动折行;v29:导出存档桌面直接下载(share 面板只留触屏;share 被系统拒绝时回退下载,不再静默吞掉);v28:目录页从课程页回来时重读存档刷新(bfcache 恢复不重跑脚本,总星星/打卡条/角标全是旧快照);v27:学一学卡片展开改 FLIP,滚动补位与展开动画同步跑(以前展完再瞬移,先张嘴又猛跳,割裂);v26:鼠标拖动改为拖动中临时关 snap(吸附会把逐帧 scrollLeft 拽回,拖着像卡住猛跳),松手自算惯性落点吸卡缘再还原;v25:货架/打卡日历横滚支持鼠标拖动(桌面滚动条藏了又没横划手势,实测完全滑不动);v24:按课堂复习(卡片盖上课日期 added,目录页选日期进当天整套;main 侧的 v23 已被存档层占用,和 v3 同款让号);v23:存档读写层抽成 shell 里的 shared.js(两页共用)+ 家长可导出/导入存档(日历弹窗底部)+ 启动申请 persist();v22:答题快照 30 分钟过期 + 亲手切页签即弃考(修陈年半轮劫持进课落地页);v21:修小旗不对齐(+选择器够不着角标,auto 边距平分空隙);v20:标错题的图标书本改小旗(插旗=标记要练);v19:学一学卡头手动进/出错题本;v18:帽子行三入口统一粉彩(继续学也改淡绿,不再实心);v17:目录页次按钮上淡彩(混合复习淡蓝/错题本淡橙);v16:考一考并入复习账本(P3);v15:错题本(账本切片专练)+ 记账一天一笔;v9:目录页标题收进帽子与打卡条同排 + 打卡日历弹窗(周记录改周一起点);v7:目录页帽子收进同列卡(v6:课程页顶栏/气泡/标签减重;v5:目录页改横滚货架;v4:UI 素材入库 + 混合复习 Leitner 版;main 侧曾占用 v3)

/* 壳:没有它们页面根本打不开。装 SW 的时候一次性拉齐。
   ⚠️ preview-img.js 436KB 也在里面 —— 它只在直接打开 app.html(不带 ?lesson=)
   时才用得上,但预缓存的代价是一次性的,而没有它离线预览就是一片 emoji。 */
const SHELL = [
  "index.html",
  "app.html",
  /* 两页的存档读写层。它是真·壳:拿不到这一个文件,两页的主脚本第一行
     store.load() 就抛 ReferenceError,整页白屏 —— 比少一张封面严重得多 */
  "shared.js",
  "theme.css",
  "preview-img.js",
  "manifest.webmanifest",
  "icon.svg",
  "lessons/index.json",
  "lessons/dictionary.json",
  "lessons/phonics.json",
  /* 界面素材:三张课程封面 + 四张入口/结算贴纸 + 主屏图标,已全部入库(v4)。
     逐个 add 各自 catch 的机制保留:哪台机器上少了哪张也只是装不上那一张,
     页面两边都有回退(封面退回巨型字形徽章、贴纸退回 emoji)。 */
  "lessons/images/cover-zoo.webp",
  "lessons/images/cover-signs.webp",
  "lessons/images/cover-recycling.webp",
  "lessons/images/ui-mic.webp",
  "lessons/images/ui-target.webp",
  "lessons/images/ui-trophy.webp",
  "lessons/images/ui-party.webp",
  "icon-180.png"
];

self.addEventListener("install", (e) => {
  // 单个文件 404 不该让整次安装失败(比如某台机器上还没生成 phonics.json),
  // 所以逐个 add 并各自吞掉错误,而不是 addAll 一把梭
  e.waitUntil(
    caches.open(CACHE)
      .then((c) => Promise.all(SHELL.map((u) => c.add(u).catch(() => null))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

/* 内容不可变的资源:音频文件名带内容哈希、配图入库后就不再改。
   这两类走 cache-first 且命中后不回源 —— 它们占了流量的 99%,
   每次都发一个校验请求,离线时还要等它超时。 */
function immutable(path) {
  return path.indexOf("/audio/") >= 0 ||
         path.indexOf("/images/") >= 0 ||
         /\.(mp3|m4a|wav|ogg|webp|png|jpg|jpeg|svg)$/i.test(path);
}

function networkFirst(req) {
  /* ⚠️ cache:"no-cache" 是这条策略的命门:裸 fetch(req) 会先问浏览器的
     HTTP 启发式缓存(python http.server 只给 Last-Modified 不给 Cache-Control,
     浏览器就按"改动时间的 10%"自作主张缓存),"网络优先"拿回来的其实是
     旧文件 —— 实测改了代码刷新还是旧页面。no-cache 强制向服务器再验证,
     文件没变走 304,代价只是一个条件请求;离线时照样落到 catch 回缓存。
     用 req.url 而不是 req:带 init 重用 navigation Request 在部分内核会抛 */
  return fetch(req.url, { cache: "no-cache", credentials: "same-origin" }).then((res) => {
    if (res && res.ok) {
      const copy = res.clone();
      caches.open(CACHE).then((c) => c.put(req, copy)).catch(() => {});
    }
    return res;
  }).catch(() => caches.match(req).then((hit) => hit || Response.error()));
}

function cacheFirst(req) {
  return caches.match(req).then((hit) => {
    if (hit) return hit;
    return fetch(req).then((res) => {
      if (res && res.ok) {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(req, copy)).catch(() => {});
      }
      return res;
    });
  });
}

self.addEventListener("fetch", (e) => {
  const req = e.request;
  // 只管同源的 GET。POST 之类不能重放,跨域(将来若有)也不该由我们代管
  if (req.method !== "GET") return;
  let url;
  try { url = new URL(req.url); } catch (err) { return; }
  if (url.origin !== self.location.origin) return;

  const path = url.pathname;
  const isHTML = /\.html?$/i.test(path) || path.endsWith("/") ||
                 (req.mode === "navigate");
  const isLessonJSON = path.indexOf("/lessons/") >= 0 && /\.json$/i.test(path);

  if (isHTML || isLessonJSON) {
    // 新壳、新课文永远优先走网络,断网才回缓存(见顶部「更新策略」)
    e.respondWith(networkFirst(req));
  } else if (immutable(path)) {
    e.respondWith(cacheFirst(req));
  } else {
    // 其余(theme.css、manifest 等)也按 network-first 处理:数量少、体积小,
    // 拿新的代价可以忽略,而拿旧的会和新壳对不上
    e.respondWith(networkFirst(req));
  }
});
