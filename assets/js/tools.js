/* 0Office.com — free browser tools. All processing happens locally in the browser. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var toast = window.O0toast || function () {};
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  function money(n, cur) {
    try { return new Intl.NumberFormat(undefined, { style: "currency", currency: cur || "USD", maximumFractionDigits: 2 }).format(n || 0); }
    catch (e) { return (cur || "$") + " " + (n || 0).toFixed(2); }
  }
  function num(v) { var n = parseFloat(v); return isFinite(n) ? n : 0; }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function copy(text) {
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(function () { toast("Copied to clipboard"); });
    else { var t = document.createElement("textarea"); t.value = text; document.body.appendChild(t); t.select(); document.execCommand("copy"); t.remove(); toast("Copied"); }
  }
  function download(name, text, type) {
    var b = new Blob([text], { type: type || "text/plain" }), a = document.createElement("a");
    a.href = URL.createObjectURL(b); a.download = name; document.body.appendChild(a); a.click(); a.remove();
  }
  var T = {};

  /* 1. Invoice generator */
  T.invoice = function (root) {
    var body = $("#invItems", root);
    function row(d, q, r) {
      var tr = document.createElement("tr");
      tr.innerHTML = '<td><input aria-label="Description" class="d" value="' + esc(d || "") + '" placeholder="Service or product"></td>' +
        '<td style="width:90px"><input aria-label="Quantity" class="q" type="number" min="0" step="any" value="' + (q == null ? 1 : q) + '"></td>' +
        '<td style="width:130px"><input aria-label="Rate" class="r" type="number" min="0" step="any" value="' + (r == null ? 0 : r) + '"></td>' +
        '<td class="amt" style="width:120px;font-weight:700"></td><td style="width:40px" class="no-print"><button class="icon-btn del" type="button" aria-label="Remove line">×</button></td>';
      body.appendChild(tr); calc();
    }
    function calc() {
      var cur = $("#invCur", root).value, sub = 0;
      $$("tr", body).forEach(function (tr) { var a = num($(".q", tr).value) * num($(".r", tr).value); sub += a; $(".amt", tr).textContent = money(a, cur); });
      var disc = sub * num($("#invDisc", root).value) / 100, taxed = (sub - disc) * num($("#invTax", root).value) / 100, ship = num($("#invShip", root).value);
      var total = sub - disc + taxed + ship, paid = num($("#invPaid", root).value);
      $("#invSub", root).textContent = money(sub, cur); $("#invDiscOut", root).textContent = "−" + money(disc, cur);
      $("#invTaxOut", root).textContent = money(taxed, cur); $("#invTotal", root).textContent = money(total, cur);
      $("#invDue", root).textContent = money(total - paid, cur);
      save();
    }
    function save() {
      var data = { f: {}, items: [] };
      $$("[data-keep]", root).forEach(function (el) { data.f[el.id] = el.value; });
      $$("tr", body).forEach(function (tr) { data.items.push([$(".d", tr).value, $(".q", tr).value, $(".r", tr).value]); });
      store.set("o0-invoice", JSON.stringify(data));
    }
    root.addEventListener("input", calc);
    root.addEventListener("click", function (e) { if (e.target.classList.contains("del")) { e.target.closest("tr").remove(); calc(); } });
    $("#invAdd", root).addEventListener("click", function () { row(); });
    $("#invPrint", root).addEventListener("click", function () { window.print(); });
    $("#invReset", root).addEventListener("click", function () { store.set("o0-invoice", ""); location.reload(); });
    var d = new Date(), due = new Date(Date.now() + 14 * 864e5);
    $("#invDate", root).value = d.toISOString().slice(0, 10); $("#invDueDate", root).value = due.toISOString().slice(0, 10);
    var saved = null; try { saved = JSON.parse(store.get("o0-invoice") || "null"); } catch (e) {}
    if (saved) {
      Object.keys(saved.f).forEach(function (k) { var el = document.getElementById(k); if (el) el.value = saved.f[k]; });
      saved.items.forEach(function (it) { row(it[0], it[1], it[2]); });
    } else { row("Website design — 10 hrs", 10, 75); row("Hosting setup", 1, 120); }
    calc();
  };

  /* 2. Meeting cost calculator (live ticking) */
  T.meeting = function (root) {
    var timer = null, start = 0, elapsed = 0;
    function perSecond() {
      var people = num($("#mcPeople", root).value), salary = num($("#mcSalary", root).value), hrs = num($("#mcHours", root).value) || 2080;
      var overhead = 1 + num($("#mcOverhead", root).value) / 100;
      return people * (salary / hrs) * overhead / 3600;
    }
    function render() {
      var cur = $("#mcCur", root).value, ps = perSecond(), mins = num($("#mcMins", root).value);
      $("#mcPlanned", root).textContent = money(ps * mins * 60, cur);
      $("#mcPerMin", root).textContent = money(ps * 60, cur);
      $("#mcWeekly", root).textContent = money(ps * mins * 60 * num($("#mcFreq", root).value), cur);
      $("#mcYearly", root).textContent = money(ps * mins * 60 * num($("#mcFreq", root).value) * 48, cur);
      $("#mcLive", root).textContent = money(ps * elapsed, cur);
      var s = Math.floor(elapsed), m = Math.floor(s / 60);
      $("#mcClock", root).textContent = String(Math.floor(m / 60)).padStart(2, "0") + ":" + String(m % 60).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
    }
    root.addEventListener("input", render);
    $("#mcStart", root).addEventListener("click", function () {
      if (timer) { clearInterval(timer); timer = null; this.textContent = "▶ Resume"; return; }
      start = Date.now() - elapsed * 1000; this.textContent = "❚❚ Pause";
      timer = setInterval(function () { elapsed = (Date.now() - start) / 1000; render(); }, 250);
    });
    $("#mcStop", root).addEventListener("click", function () { clearInterval(timer); timer = null; elapsed = 0; $("#mcStart", root).textContent = "▶ Start live meter"; render(); });
    render();
  };

  /* 3. Time zone planner */
  T.timezone = function (root) {
    var zones = [];
    var all = (Intl.supportedValuesOf ? Intl.supportedValuesOf("timeZone") : ["UTC", "America/New_York", "America/Chicago", "America/Denver", "America/Los_Angeles", "America/Toronto", "America/Sao_Paulo", "Europe/London", "Europe/Paris", "Europe/Berlin", "Africa/Lagos", "Asia/Dubai", "Asia/Kolkata", "Asia/Singapore", "Asia/Tokyo", "Australia/Sydney"]);
    var dl = $("#tzList", root); dl.innerHTML = all.map(function (z) { return '<option value="' + z + '">'; }).join("");
    var local = Intl.DateTimeFormat().resolvedOptions().timeZone || "UTC";
    var fromUrl = new URLSearchParams(location.search).get("z");
    zones = fromUrl ? fromUrl.split(",") : [local, "America/New_York", "Europe/London"];
    zones = zones.filter(function (z, i, a) { return a.indexOf(z) === i; });
    function offsetHours(z, d) {
      var p = {};
      new Intl.DateTimeFormat("en-US", { timeZone: z, hourCycle: "h23", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit" })
        .formatToParts(d).forEach(function (x) { p[x.type] = x.value; });
      return (Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour % 24, +p.minute) - Math.floor(d.getTime() / 6e4) * 6e4) / 36e5;
    }
    function render() {
      var ws = num($("#tzStart", root).value), we = num($("#tzEnd", root).value), base = new Date(); base.setUTCMinutes(0, 0, 0);
      var baseZone = zones[0], bOff = offsetHours(baseZone, base);
      var html = "", counts = new Array(24).fill(0);
      var rows = zones.map(function (z) {
        var off = offsetHours(z, base), cells = [];
        for (var h = 0; h < 24; h++) {
          var lh = ((h + off - bOff) % 24 + 24) % 24, work = lh >= ws && lh < we;
          if (work) counts[h]++;
          cells.push({ lh: lh, work: work });
        }
        return { z: z, cells: cells, now: new Date().toLocaleTimeString([], { timeZone: z, hour: "2-digit", minute: "2-digit" }) };
      });
      rows.forEach(function (r, ri) {
        html += '<div class="tz-row"><div class="lbl">' + esc(r.z.split("/").pop().replace(/_/g, " ")) + '<br><small class="muted">' + r.now + (ri ? ' · <a href="#" data-rm="' + ri + '">remove</a>' : " · base") + "</small></div>";
        r.cells.forEach(function (c, h) {
          var lh = Math.floor(c.lh), mm = Math.round((c.lh - lh) * 60);
          html += '<div class="' + (counts[h] === zones.length ? "overlap" : c.work ? "work" : "") + '">' + lh + (mm ? ":" + String(mm).padStart(2, "0") : "") + "</div>";
        });
        html += "</div>";
      });
      $("#tzGrid", root).innerHTML = html;
      var best = counts.map(function (c, h) { return c === zones.length ? h : -1; }).filter(function (h) { return h > -1; });
      $("#tzBest", root).textContent = best.length ? best.length + " overlapping working hour(s) — highlighted in solid colour. Times shown in each city's local hour." : "No full overlap inside working hours. Try widening the working window or dropping a city.";
      var u = new URL(location.href); u.searchParams.set("z", zones.join(",")); history.replaceState(null, "", u);
    }
    $("#tzAdd", root).addEventListener("submit", function (e) {
      e.preventDefault(); var v = $("#tzInput", root).value.trim();
      if (all.indexOf(v) === -1) { toast("Pick a zone from the list, e.g. Europe/Paris"); return; }
      if (zones.indexOf(v) === -1) zones.push(v); $("#tzInput", root).value = ""; render();
    });
    root.addEventListener("click", function (e) { var r = e.target.getAttribute("data-rm"); if (r) { e.preventDefault(); zones.splice(+r, 1); render(); } });
    root.addEventListener("input", function (e) { if (e.target.id === "tzStart" || e.target.id === "tzEnd") render(); });
    $("#tzShare", root).addEventListener("click", function () { copy(location.href); });
    render(); setInterval(render, 60000);
  };

  /* 4. Pomodoro timer */
  T.pomodoro = function (root) {
    var modes = { focus: 25, short: 5, long: 15 }, mode = "focus", left = 25 * 60, t = null, done = +(store.get("o0-pomo-" + new Date().toDateString()) || 0);
    function draw() {
      var m = Math.floor(left / 60), s = left % 60, txt = String(m).padStart(2, "0") + ":" + String(s).padStart(2, "0");
      $("#pmFace", root).textContent = txt; document.title = txt + " · " + (mode === "focus" ? "Focus" : "Break") + " — 0Office";
      $("#pmDone", root).textContent = done;
    }
    function set(m) { mode = m; modes[m] = num($("#pm-" + m, root).value) || modes[m]; left = modes[m] * 60; stop(); $$(".seg button", root).forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-mode") === m); }); draw(); }
    function stop() { clearInterval(t); t = null; $("#pmGo", root).textContent = "Start"; }
    function beep() {
      try { var a = new (window.AudioContext || window.webkitAudioContext)(), o = a.createOscillator(), g = a.createGain(); o.connect(g); g.connect(a.destination); o.frequency.value = 880; g.gain.value = .15; o.start(); setTimeout(function () { o.stop(); a.close(); }, 600); } catch (e) {}
      if (window.Notification && Notification.permission === "granted") new Notification(mode === "focus" ? "Focus block done — take a break" : "Break over — back to it");
    }
    $("#pmGo", root).addEventListener("click", function () {
      if (t) { stop(); return; }
      if (window.Notification && Notification.permission === "default") Notification.requestPermission();
      this.textContent = "Pause"; var end = Date.now() + left * 1000;
      t = setInterval(function () {
        left = Math.max(0, Math.round((end - Date.now()) / 1000)); draw();
        if (!left) { stop(); beep(); if (mode === "focus") { done++; store.set("o0-pomo-" + new Date().toDateString(), done); set(done % 4 ? "short" : "long"); } else set("focus"); }
      }, 250);
    });
    $("#pmReset", root).addEventListener("click", function () { set(mode); });
    $$(".seg button", root).forEach(function (b) { b.addEventListener("click", function () { set(b.getAttribute("data-mode")); }); });
    $$("[id^=pm-]", root).forEach(function (i) { i.addEventListener("change", function () { set(mode); }); });
    // tasks
    var tasks = []; try { tasks = JSON.parse(store.get("o0-pomo-tasks") || "[]"); } catch (e) {}
    function drawTasks() {
      $("#pmTasks", root).innerHTML = tasks.map(function (k, i) { return '<li><label class="check"><input type="checkbox" data-i="' + i + '"' + (k.d ? " checked" : "") + "> <span" + (k.d ? ' style="text-decoration:line-through"' : "") + ">" + esc(k.t) + '</span></label></li>'; }).join("") || '<li class="muted">No tasks yet.</li>';
      store.set("o0-pomo-tasks", JSON.stringify(tasks));
    }
    $("#pmTaskForm", root).addEventListener("submit", function (e) { e.preventDefault(); var v = $("#pmTask", root).value.trim(); if (v) { tasks.push({ t: v, d: false }); $("#pmTask", root).value = ""; drawTasks(); } });
    $("#pmTasks", root).addEventListener("change", function (e) { var i = e.target.getAttribute("data-i"); if (i != null) { tasks[i].d = e.target.checked; drawTasks(); } });
    $("#pmClear", root).addEventListener("click", function () { tasks = tasks.filter(function (k) { return !k.d; }); drawTasks(); });
    drawTasks(); draw();
  };

  /* 5. Word counter */
  T.words = function (root) {
    var ta = $("#wcText", root);
    var stop = "the a an and or but of to in on for with at by from is are was were be been it this that as i you he she we they not".split(" ");
    function run() {
      var s = ta.value, words = s.match(/[\p{L}\p{N}'’-]+/gu) || [];
      var sentences = (s.match(/[^.!?]+[.!?]+/g) || []).length || (s.trim() ? 1 : 0);
      var paras = s.split(/\n\s*\n/).filter(function (p) { return p.trim(); }).length;
      $("#wcWords", root).textContent = words.length;
      $("#wcChars", root).textContent = s.length;
      $("#wcNoSp", root).textContent = s.replace(/\s/g, "").length;
      $("#wcSent", root).textContent = sentences; $("#wcPara", root).textContent = paras;
      $("#wcRead", root).textContent = Math.max(0, Math.ceil(words.length / 238)) + " min";
      $("#wcSpeak", root).textContent = Math.max(0, Math.ceil(words.length / 140)) + " min";
      var syll = words.reduce(function (a, w) { return a + Math.max(1, (w.toLowerCase().replace(/e$/, "").match(/[aeiouy]+/g) || []).length); }, 0);
      var fre = words.length && sentences ? 206.835 - 1.015 * (words.length / sentences) - 84.6 * (syll / words.length) : 0;
      $("#wcFre", root).textContent = words.length ? Math.round(fre) : "—";
      var freq = {}; words.forEach(function (w) { w = w.toLowerCase(); if (w.length > 2 && stop.indexOf(w) === -1) freq[w] = (freq[w] || 0) + 1; });
      var top = Object.keys(freq).sort(function (a, b) { return freq[b] - freq[a]; }).slice(0, 10);
      $("#wcKw", root).innerHTML = top.map(function (w) { return "<tr><td>" + esc(w) + "</td><td>" + freq[w] + "</td><td>" + (freq[w] / words.length * 100).toFixed(1) + "%</td></tr>"; }).join("") || '<tr><td colspan="3" class="muted">Start typing…</td></tr>';
      store.set("o0-words", s);
    }
    ta.value = store.get("o0-words") || ""; ta.addEventListener("input", run);
    $("#wcCopy", root).addEventListener("click", function () { copy(ta.value); });
    $("#wcClear", root).addEventListener("click", function () { ta.value = ""; run(); });
    $("#wcCase", root).addEventListener("change", function () {
      var v = this.value, s = ta.value;
      if (v === "upper") s = s.toUpperCase(); else if (v === "lower") s = s.toLowerCase();
      else if (v === "title") s = s.toLowerCase().replace(/\b\p{L}/gu, function (c) { return c.toUpperCase(); });
      else if (v === "sentence") s = s.toLowerCase().replace(/(^\s*|[.!?]\s+)(\p{L})/gu, function (m, a, b) { return a + b.toUpperCase(); });
      ta.value = s; this.value = ""; run();
    });
    run();
  };

  /* 6. Salary converter */
  T.salary = function (root) {
    var ids = ["hour", "day", "week", "biweek", "month", "year"];
    function factors() {
      var h = num($("#scHours", root).value) || 40, d = num($("#scDays", root).value) || 5, w = num($("#scWeeks", root).value) || 52;
      var perYear = { hour: h * w, day: d * w, week: w, biweek: w / 2, month: 12, year: 1 };
      return perYear;
    }
    function from(src) {
      var f = factors(), yearly = num($("#sc-" + src, root).value) * f[src], cur = $("#scCur", root).value;
      ids.forEach(function (k) { if (k !== src) $("#sc-" + k, root).value = (yearly / f[k]).toFixed(2); });
      var tax = num($("#scTax", root).value) / 100;
      $("#scNet", root).textContent = money(yearly * (1 - tax), cur) + " / year  ·  " + money(yearly * (1 - tax) / 12, cur) + " / month";
    }
    ids.forEach(function (k) { $("#sc-" + k, root).addEventListener("input", function () { from(k); }); });
    ["scHours", "scDays", "scWeeks", "scTax", "scCur"].forEach(function (k) { $("#" + k, root).addEventListener("input", function () { from("year"); }); });
    from("year");
  };

  /* 7. Remote work savings calculator */
  T.savings = function (root) {
    function run() {
      var cur = $("#rsCur", root).value, days = num($("#rsDays", root).value) * num($("#rsWeeks", root).value);
      var commute = num($("#rsCommuteCost", root).value) * days, lunch = num($("#rsLunch", root).value) * days;
      var clothes = num($("#rsClothes", root).value), childcare = num($("#rsCare", root).value) * 12;
      var homeCost = num($("#rsHome", root).value) * 12;
      var hours = num($("#rsMins", root).value) * 2 * days / 60, hourly = num($("#rsWage", root).value);
      var cash = commute + lunch + clothes + childcare - homeCost, timeVal = hours * hourly;
      $("#rsCash", root).textContent = money(cash, cur);
      $("#rsHours", root).textContent = Math.round(hours) + " h";
      $("#rsDaysBack", root).textContent = (hours / 8).toFixed(1) + " workdays";
      $("#rsTotal", root).textContent = money(cash + timeVal, cur);
      var team = num($("#rsTeam", root).value), rent = num($("#rsRent", root).value);
      $("#rsEmployer", root).textContent = money(team * rent * 12, cur);
    }
    root.addEventListener("input", run); run();
  };

  /* 8. Password generator */
  T.password = function (root) {
    function gen() {
      var len = num($("#pwLen", root).value); $("#pwLenOut", root).textContent = len;
      var sets = "";
      if ($("#pwLower", root).checked) sets += "abcdefghijkmnopqrstuvwxyz";
      if ($("#pwUpper", root).checked) sets += "ABCDEFGHJKLMNPQRSTUVWXYZ";
      if ($("#pwNum", root).checked) sets += "23456789";
      if ($("#pwSym", root).checked) sets += "!@#$%^&*()-_=+[]{};:,.?";
      if (!$("#pwAmbig", root).checked) sets += "lIO01";
      if (!sets) { $("#pwOut", root).value = ""; return; }
      var arr = new Uint32Array(len); crypto.getRandomValues(arr);
      var pw = Array.prototype.map.call(arr, function (n) { return sets[n % sets.length]; }).join("");
      $("#pwOut", root).value = pw;
      var bits = Math.round(len * Math.log2(sets.length)), label = bits < 50 ? "Weak" : bits < 75 ? "Fair" : bits < 100 ? "Strong" : "Very strong";
      $("#pwStrength", root).textContent = label + " · ~" + bits + " bits of entropy";
    }
    function phrase() {
      var w = "anchor bamboo canyon desert ember falcon garden harbor island jungle kettle lantern meadow nectar orbit pepper quartz river saddle timber umbrella velvet walnut yonder zephyr cobalt maple sprout copper breeze glacier summit".split(" ");
      var arr = new Uint32Array(5); crypto.getRandomValues(arr);
      $("#pwOut", root).value = Array.prototype.map.call(arr, function (n) { return w[n % w.length]; }).join("-") + "-" + (arr[0] % 90 + 10);
      $("#pwStrength", root).textContent = "Passphrase · easier to remember";
    }
    root.addEventListener("input", gen);
    $("#pwGen", root).addEventListener("click", gen); $("#pwPhrase", root).addEventListener("click", phrase);
    $("#pwCopy", root).addEventListener("click", function () { copy($("#pwOut", root).value); });
    gen();
  };

  /* 9. Email signature generator */
  T.signature = function (root) {
    function html() {
      var v = function (id) { return esc($("#" + id, root).value.trim()); };
      var color = $("#sgColor", root).value;
      var lines = [];
      if (v("sgTitle") || v("sgCompany")) lines.push(v("sgTitle") + (v("sgTitle") && v("sgCompany") ? " · " : "") + v("sgCompany"));
      if (v("sgPhone")) lines.push(v("sgPhone"));
      if (v("sgWeb")) lines.push('<a href="' + (/^https?:/.test(v("sgWeb")) ? v("sgWeb") : "https://" + v("sgWeb")) + '" style="color:' + color + ';text-decoration:none">' + v("sgWeb").replace(/^https?:\/\//, "") + "</a>");
      if (v("sgHours")) lines.push('<span style="color:#6b7280">' + v("sgHours") + "</span>");
      return '<table cellpadding="0" cellspacing="0" style="font-family:Arial,Helvetica,sans-serif;font-size:13px;color:#111827;line-height:1.5"><tr>' +
        '<td style="border-left:3px solid ' + color + ';padding-left:12px"><div style="font-size:16px;font-weight:bold;color:' + color + '">' + (v("sgName") || "Your Name") + "</div>" +
        lines.map(function (l) { return "<div>" + l + "</div>"; }).join("") + "</td></tr></table>";
    }
    function run() { $("#sgPreview", root).innerHTML = html(); }
    root.addEventListener("input", run);
    $("#sgCopy", root).addEventListener("click", function () {
      var h = html();
      if (window.ClipboardItem && navigator.clipboard && navigator.clipboard.write) {
        navigator.clipboard.write([new ClipboardItem({ "text/html": new Blob([h], { type: "text/html" }), "text/plain": new Blob([$("#sgPreview", root).innerText], { type: "text/plain" }) })]).then(function () { toast("Signature copied — paste into your mail settings"); });
      } else copy(h);
    });
    $("#sgCopyHtml", root).addEventListener("click", function () { copy(html()); });
    run();
  };

  /* 10. Quick notes */
  T.notes = function (root) {
    var ta = $("#ntText", root), info = $("#ntInfo", root);
    ta.value = store.get("o0-notes") || "";
    function upd() { var w = (ta.value.match(/\S+/g) || []).length; info.textContent = w + " words · saved in this browser only"; }
    ta.addEventListener("input", function () { store.set("o0-notes", ta.value); upd(); });
    $("#ntDl", root).addEventListener("click", function () { download("0office-notes.txt", ta.value); });
    $("#ntMd", root).addEventListener("click", function () { download("0office-notes.md", ta.value, "text/markdown"); });
    $("#ntCopy", root).addEventListener("click", function () { copy(ta.value); });
    $("#ntClear", root).addEventListener("click", function () { if (confirm("Clear all notes?")) { ta.value = ""; store.set("o0-notes", ""); upd(); } });
    upd();
  };

  /* 11. Business days calculator */
  T.bizdays = function (root) {
    function run() {
      var a = new Date($("#bdStart", root).value), b = new Date($("#bdEnd", root).value);
      if (isNaN(a) || isNaN(b)) return;
      var holidays = $("#bdHol", root).value.split(/[\s,]+/).filter(Boolean);
      var sign = a <= b ? 1 : -1, d = new Date(a), work = 0, cal = 0, wk = 0;
      while ((sign > 0 && d <= b) || (sign < 0 && d >= b)) {
        var day = d.getUTCDay(), iso = d.toISOString().slice(0, 10);
        cal++; if (day === 0 || day === 6) wk++; else if (holidays.indexOf(iso) === -1) work++;
        d.setUTCDate(d.getUTCDate() + sign);
      }
      $("#bdWork", root).textContent = work; $("#bdCal", root).textContent = cal; $("#bdWk", root).textContent = wk;
      $("#bdHours", root).textContent = work * num($("#bdHpd", root).value) + " h";
      // add N business days
      var n = num($("#bdAdd", root).value), s = new Date($("#bdStart", root).value), c = 0;
      while (c < n) { s.setUTCDate(s.getUTCDate() + 1); var dd = s.getUTCDay(), is = s.toISOString().slice(0, 10); if (dd && dd !== 6 && holidays.indexOf(is) === -1) c++; }
      $("#bdAddOut", root).textContent = s.toISOString().slice(0, 10) + " (" + s.toLocaleDateString(undefined, { weekday: "long", timeZone: "UTC" }) + ")";
    }
    var t = new Date(); $("#bdStart", root).value = t.toISOString().slice(0, 10);
    $("#bdEnd", root).value = new Date(t.getTime() + 30 * 864e5).toISOString().slice(0, 10);
    root.addEventListener("input", run); run();
  };

  /* 12. Freelance rate calculator */
  T.rate = function (root) {
    function run() {
      var cur = $("#frCur", root).value, income = num($("#frIncome", root).value), costs = num($("#frCosts", root).value) * 12;
      var tax = num($("#frTax", root).value) / 100, weeks = 52 - num($("#frOff", root).value), hrs = num($("#frHours", root).value), bill = num($("#frBill", root).value) / 100;
      var gross = (income + costs) / Math.max(0.01, 1 - tax), billable = weeks * hrs * bill;
      var hourly = billable ? gross / billable : 0, margin = 1 + num($("#frMargin", root).value) / 100;
      $("#frHourly", root).textContent = money(hourly * margin, cur);
      $("#frDay", root).textContent = money(hourly * margin * hrs / 5 * bill, cur);
      $("#frGross", root).textContent = money(gross, cur);
      $("#frBillable", root).textContent = Math.round(billable) + " h / year";
    }
    root.addEventListener("input", run); run();
  };

  $$("[data-tool]").forEach(function (el) { var fn = T[el.getAttribute("data-tool")]; if (fn) try { fn(el); } catch (e) { console.error(e); } });
})();
