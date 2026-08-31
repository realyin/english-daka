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
const CACHE = "daka-v7";   // v7:目录页帽子收进同列卡(v6:课程页顶栏/气泡/标签减重;v5:目录页改横滚货架;v4:UI 素材入库 + 混合复习 Leitner 版;main 侧曾占用 v3)

/* 壳:没有它们页面根本打不开。装 SW 的时候一次性拉齐。
   ⚠️ preview-img.js 436KB 也在里面 —— 它只在直接打开 app.html(不带 ?lesson=)
   时才用得上,但预缓存的代价是一次性的,而没有它离线预览就是一片 emoji。 */
const SHELL = [
  "index.html",
  "app.html",
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
  return fetch(req).then((res) => {
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
