/* ================================================================
   两页共用的存档读写层 —— index.html 和 app.html 都 <script src> 它。

   为什么抽出来:这几十行原先在两个文件里各存一份,注释上自己写着
   "改一处要同步改两处"。两份已经开始飘了 —— app.html 那份多一个 today(),
   两边的注释措辞也各说各的。同一份数据只该有一处解释它的代码,
   靠人记得改两遍的约定,迟早会在某次改字段时兑现成一片白屏。

   ⚠️ 这里只放"读/写/校验/补默认字段"这一层。谁在什么时候记几颗星、
   怎么调度复习,是各页自己的事,不要往这里搬 —— 一搬就又变成两页耦合,
   改目录页的显示会波及课程页的记账。
   ⚠️ 另外两个键不在这里:"daka.coach"(示能演示,app.html 独有)和
   "daka.shelf"(货架横滚位置,index.html 独有、而且在 sessionStorage)。
   只有一处用的东西放到公共文件里,只会让人以为另一页也在用。

   ⚠️ 这个文件是 ES5 安全区:只用 var / function,不用箭头函数、let/const、
   模板串。它排在两页的主脚本之前,老内核上一旦解析失败,后面整页的
   <script> 连带完蛋(而两页的白屏兜底恰恰要靠 store 才能显示出存档还在)。
   ⚠️ 隐私模式 / 关了站点数据的浏览器,连碰一下 localStorage 都可能抛,
   所以每一次读写都各自包 try/catch,失败就静默退回"不记账"的老行为 ——
   打卡记不住是遗憾,页面白屏是事故。
   ⚠️ 日期一律本地时区手拼,不要 toISOString():那是 UTC,东八区晚上
   8 点以后会算成"明天",孩子睡前打的卡记到第二天,连续天数直接断。
   ================================================================ */

/* ================================================================
   进度存档 —— localStorage 单键 "daka.v1"
   { total, lessons:{id:{stars,done}}, days:["YYYY-MM-DD"],
     dayStars:{"YYYY-MM-DD":n}, dayCards:{"YYYY-MM-DD":n},
     last:{lesson,at}, lastBackupAt:"YYYY-MM-DD" }
   ⚠️ dayStars / dayCards / lastBackupAt 都是后加的字段:**旧存档里没有它们**,
   load() 一律补默认值 —— 少补一条,老用户一进来就是 undefined 上取属性,
   整页白屏。同理,读它们的地方永远要当"可能没有这一天"来写。
   ================================================================ */
var STORE_KEY = "daka.v1";
function ymd(d){
  var m = d.getMonth() + 1, day = d.getDate();
  return d.getFullYear() + "-" + (m < 10 ? "0" : "") + m + "-" + (day < 10 ? "0" : "") + day;
}
function today(){ return ymd(new Date()); }
var store = {
  load: function(){
    var o = null;
    try{
      var s = localStorage.getItem(STORE_KEY);
      if(s) o = JSON.parse(s);
    }catch(e){ o = null; }
    if(!o || typeof o !== "object") o = {};
    if(typeof o.total !== "number" || !isFinite(o.total)) o.total = 0;
    if(!o.lessons || typeof o.lessons !== "object") o.lessons = {};
    if(!(o.days instanceof Array)) o.days = [];
    // 数组也是 object,所以要单独挡一下:老存档里万一存成了数组,
    // 后面 dayStars[key] += n 会往数组上挂字符串下标,存出去就是个怪东西
    if(!o.dayStars || typeof o.dayStars !== "object" || o.dayStars instanceof Array) o.dayStars = {};
    // dayCards(当天听过几张卡,给日历分深浅)同 dayStars:后加字段,旧存档没有
    if(!o.dayCards || typeof o.dayCards !== "object" || o.dayCards instanceof Array) o.dayCards = {};
    if(!o.last || typeof o.last !== "object") o.last = null;
    return o;
  },
  save: function(o){
    try{ localStorage.setItem(STORE_KEY, JSON.stringify(o)); return true; }
    catch(e){ return false; }
  }
};

/* ================================================================
   复习账本 —— 单键 "daka.rev.v1",和进度、演示标记互不纠缠(清谁都不伤谁)。
   每张进过混合复习的卡记一条:{ b:盒号 0-5, t:最后见到的日期, w:累计错次 }。
   盒号是 Leitner 间隔重复的全部状态:REV_GAP[b] 天后到期,答对升盒、答错降盒。
   读不到(隐私模式)就当人人都是新卡 —— 调度退化成随机抽新卡,和旧行为一个档次。
   ⚠️ 写入方只有 app.html;目录页只读(错题本按钮上的"N 个词在练")。
   即便如此读法也要走同一份 load/revRec —— 目录页报 5 个、点进去只有 3 个,
   就是两边各写一遍判断的下场。
   ================================================================ */
var REV_KEY = "daka.rev.v1";
var REV_GAP = [0, 1, 2, 4, 7, 14];             // 盒号 → 间隔天数,14 天封顶
/* 野键:纯数字开头的 "12:bat"。app.html 的 startPractice 曾把复习卡上的
   _src(来源课程 id)覆盖成数字下标,复习账本就按下标记了一批账(修在 v74)。
   这些键谁也查不到 —— 两个消费方都是拿真卡去查账本、从不遍历键 —— 纯死重量。
   ⚠️ 判据只认「冒号前全是数字」:退役的日期命名课 id 是 "2026-08-30",
   \d+ 吃完 2026 撞上的是 '-' 不是 ':',所以它们的账不会被误扫。 */
var REV_JUNK = /^\d+:/;
var revStore = {
  load: function(){
    try{
      var s = localStorage.getItem(REV_KEY);
      var o = s ? JSON.parse(s) : null;
      if(!o || typeof o !== "object") return {};
      // 扫一次就写回,下次 load 无键可扫也就不再写 —— 自愈一次即收敛
      var k, dirty = false;
      for(k in o) if(o.hasOwnProperty(k) && REV_JUNK.test(k)){ delete o[k]; dirty = true; }
      if(dirty) revStore.save(o);
      return o;
    }catch(e){ return {}; }
  },
  save: function(o){
    try{ localStorage.setItem(REV_KEY, JSON.stringify(o)); }catch(e){}
  }
};
function revRec(o, k){                         // 取/修某卡的账,字段坏了就地扶正
  var r = o[k];
  if(!r || typeof r !== "object") r = {b:0, t:today(), w:0};
  if(!(typeof r.b === "number" && isFinite(r.b))) r.b = 0;
  r.b = Math.min(Math.max(Math.round(r.b), 0), 5);
  if(!(typeof r.w === "number" && isFinite(r.w))) r.w = 0;
  if(!(typeof r.t === "string" && /^\d{4}-\d{2}-\d{2}$/.test(r.t))) r.t = today();
  o[k] = r;
  return r;
}

/* ── 级别(K1/K2/…):目录页切换器和混合复习的"当前级别"共用 ──────────────
   学习路径就是这个顺序;没标 level 的老课一律当 K2(回填前的数据)。
   ⚠️ gen_audio.py 的 LEVEL_ORDER 是同一张表,改了要同步 */
var LV_ORDER = ["K1", "K2", "K3", "S1", "S2", "S3"];
function lvOf(l){ return (l && l.level) || "K2"; }
function lvRank(lv){ var i = LV_ORDER.indexOf(lv); return i < 0 ? 1 : i; }
/* 一批课里的"当前级别" = 排位最高的那个:导入永远跟着孩子的进度走,
   手里最高的级别就是正在学的(K1 已学完才会去学 K2) */
function lvCurrent(lessons){
  var best = "K2", r = -1;
  (lessons || []).forEach(function(l){
    if(lvRank(lvOf(l)) > r){ r = lvRank(lvOf(l)); best = lvOf(l); }
  });
  return best;
}
