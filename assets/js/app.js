/* 0Office.com — site runtime. Vanilla JS, no dependencies. */
(function () {
  "use strict";
  var C = window.OFFICE0 || {};
  var ROOT = document.body.getAttribute("data-root") || "";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* ---------- contact routing (address never rendered) ---------- */
  function addr() {
    var k = C._ck || [];
    return k.slice().reverse().map(function (n) { return String.fromCharCode(n ^ 0x5A); }).join("");
  }
  function endpoint() {
    return "https://formsubmit.co/ajax/" + (C.formAlias ? C.formAlias : addr());
  }
  // Links marked data-mail open the mail client without exposing the address in the page
  $$("[data-mail]").forEach(function (a) {
    a.setAttribute("href", "#contact");
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var subj = a.getAttribute("data-mail") || "Inquiry from 0Office.com";
      window.location.href = "mai" + "lto:" + addr() + "?subject=" + encodeURIComponent(subj);
    });
  });

  /* ---------- toast ---------- */
  var toastEl;
  function toast(msg) {
    if (!toastEl) { toastEl = document.createElement("div"); toastEl.className = "toast"; toastEl.setAttribute("role", "status"); document.body.appendChild(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add("show");
    clearTimeout(toastEl._t); toastEl._t = setTimeout(function () { toastEl.classList.remove("show"); }, 2600);
  }
  window.O0toast = toast;

  /* ---------- theme ---------- */
  var saved = store.get("o0-theme");
  if (saved) document.documentElement.setAttribute("data-theme", saved);
  var tbtn = $("#themeBtn");
  if (tbtn) tbtn.addEventListener("click", function () {
    var cur = document.documentElement.getAttribute("data-theme") ||
      (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    var next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next); store.set("o0-theme", next);
  });

  /* ---------- mobile menu ---------- */
  var mbtn = $("#menuBtn"), links = $("#navLinks");
  if (mbtn && links) mbtn.addEventListener("click", function () {
    var open = links.classList.toggle("open"); mbtn.setAttribute("aria-expanded", open ? "true" : "false");
  });

  /* ---------- site search (Ctrl/Cmd+K) ---------- */
  var modal = $("#searchModal"), sInput = $("#searchInput"), sRes = $("#searchResults");
  function openSearch(q) {
    if (!modal) return; modal.classList.add("open"); sInput.value = q || ""; runSearch(); setTimeout(function () { sInput.focus(); }, 30);
  }
  function closeSearch() { if (modal) modal.classList.remove("open"); }
  function runSearch() {
    var idx = window.O0_INDEX || [], q = sInput.value.trim().toLowerCase();
    var hits = !q ? idx.slice(0, 8) : idx.filter(function (p) { return (p.t + " " + p.d + " " + (p.k || "")).toLowerCase().indexOf(q) > -1; }).slice(0, 12);
    sRes.innerHTML = hits.length ? hits.map(function (p) {
      return '<a href="' + ROOT + p.u + '"><strong>' + p.t + "</strong><small>" + p.d + "</small></a>";
    }).join("") : '<a href="' + ROOT + 'get-started.html"><strong>No match — tell us what you need</strong><small>Get a free, personalised Zero-Office plan</small></a>';
  }
  $$("[data-search]").forEach(function (b) { b.addEventListener("click", function () { openSearch(); }); });
  if (sInput) sInput.addEventListener("input", runSearch);
  if (modal) modal.addEventListener("click", function (e) { if (e.target === modal) closeSearch(); });
  document.addEventListener("keydown", function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") { e.preventDefault(); openSearch(); }
    if (e.key === "Escape") closeSearch();
  });
  var hs = $("#heroSearch");
  if (hs) hs.addEventListener("submit", function (e) { e.preventDefault(); openSearch($("input", hs).value); });

  /* ---------- cookie consent + deferred third-party scripts ---------- */
  var consent = store.get("o0-consent");
  var cookie = $("#cookie");
  function loadThirdParty() {
    if (C.ga4) {
      var g = document.createElement("script"); g.async = true; g.src = "https://www.googletagmanager.com/gtag/js?id=" + C.ga4; document.head.appendChild(g);
      window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); };
      gtag("js", new Date()); gtag("config", C.ga4);
    }
  }
  if (cookie && !consent) cookie.classList.add("show");
  $$("[data-consent]").forEach(function (b) {
    b.addEventListener("click", function () {
      var v = b.getAttribute("data-consent"); store.set("o0-consent", v); cookie.classList.remove("show");
      if (v === "all") { loadThirdParty(); setupAds(true); }
    });
  });
  if (consent === "all") loadThirdParty();

  /* ---------- ads: AdSense if configured, otherwise house ads ---------- */
  function setupAds(personalised) {
    var slots = $$(".ad-slot [data-ad]");
    if (!C.adsenseClient) {
      slots.forEach(function (s) {
        s.innerHTML = '<span class="ad-label">Advertisement</span><span>Reach remote founders, freelancers &amp; distributed teams. <a href="' + ROOT + 'advertise.html">Advertise here →</a></span>';
      });
      return;
    }
    if (!document.getElementById("adsbygoogle-js")) {
      var s = document.createElement("script"); s.async = true; s.id = "adsbygoogle-js"; s.crossOrigin = "anonymous";
      s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient;
      document.head.appendChild(s);
    }
    (window.adsbygoogle = window.adsbygoogle || []);
    if (!personalised) window.adsbygoogle.requestNonPersonalizedAds = 1;
    slots.forEach(function (el) {
      if (el.getAttribute("data-live")) return;
      var pos = el.getAttribute("data-ad"), slot = (C.adSlots || {})[pos] || "";
      el.classList.add("live"); el.setAttribute("data-live", "1");
      el.innerHTML = '<ins class="adsbygoogle" style="display:block" data-ad-client="' + C.adsenseClient + '"' +
        (slot ? ' data-ad-slot="' + slot + '"' : "") + ' data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { window.adsbygoogle.push({}); } catch (e) {}
    });
  }
  setupAds(consent === "all");

  /* ---------- forms: AJAX to FormSubmit, honeypot, status ---------- */
  function serialize(form) {
    var data = {}, fd = new FormData(form);
    fd.forEach(function (v, k) {
      if (k === "_honey") return;
      if (data[k]) data[k] = data[k] + ", " + v; else data[k] = v;
    });
    return data;
  }
  $$("form[data-form]").forEach(function (form) {
    form.setAttribute("novalidate", "");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = $(".form-status", form);
      if (!form.checkValidity()) {
        var bad = $(":invalid", form); if (bad) { bad.focus(); if (bad.reportValidity) bad.reportValidity(); }
        return;
      }
      var hp = form.querySelector('[name="_honey"]'); if (hp && hp.value) return;
      var data = serialize(form), kind = form.getAttribute("data-form");
      data._subject = "[0Office.com] " + kind + (data.name ? " — " + data.name : "");
      data._template = "table"; data._captcha = "false";
      data.form_type = kind; data.page = location.pathname; data.submitted_at = new Date().toISOString();
      var btn = $('[type="submit"]', form), label = btn ? btn.textContent : "";
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok || res.j.success === "false" || res.j.success === false) throw new Error(res.j.message || "Send failed");
          if (status) { status.className = "form-status ok"; status.textContent = form.getAttribute("data-success") || "Thanks — we received your submission and will reply shortly."; }
          form.reset(); if (form._resetSteps) form._resetSteps();
          if (window.gtag) gtag("event", "generate_lead", { form_type: kind });
          toast("Submitted ✓");
        })
        .catch(function () {
          if (status) { status.className = "form-status err"; status.textContent = "Couldn't send right now. Please try again in a minute."; }
        })
        .then(function () { if (btn) { btn.disabled = false; btn.textContent = label; } });
    });
  });

  /* ---------- multi-step lead form ---------- */
  $$("[data-steps]").forEach(function (form) {
    var steps = $$(".step", form), bar = $(".progress i", form), i = 0;
    function show(n) {
      i = n; steps.forEach(function (s, k) { s.classList.toggle("active", k === n); });
      if (bar) bar.style.width = ((n + 1) / steps.length * 100) + "%";
      var lab = $("[data-step-label]", form); if (lab) lab.textContent = "Step " + (n + 1) + " of " + steps.length;
    }
    function valid(step) {
      var fields = $$("input,select,textarea", step), ok = true;
      var groups = {};
      fields.forEach(function (f) {
        if (f.type === "checkbox" && f.hasAttribute("data-group-required")) { groups[f.name] = groups[f.name] || f.checked; return; }
        if (!f.checkValidity()) { if (ok) { f.reportValidity && f.reportValidity(); } ok = false; }
      });
      Object.keys(groups).forEach(function (g) { if (!groups[g]) { ok = false; toast("Pick at least one option"); } });
      return ok;
    }
    $$("[data-next]", form).forEach(function (b) { b.addEventListener("click", function () { if (valid(steps[i])) show(Math.min(i + 1, steps.length - 1)); }); });
    $$("[data-prev]", form).forEach(function (b) { b.addEventListener("click", function () { show(Math.max(i - 1, 0)); }); });
    form._resetSteps = function () { show(0); };
    // pre-select from ?need=
    var need = new URLSearchParams(location.search).get("need");
    if (need) { var box = form.querySelector('input[value="' + need + '"]'); if (box) box.checked = true; }
    show(0);
  });

  /* ---------- donations ---------- */
  var D = C.donate || {};
  $$("[data-donate]").forEach(function (b) {
    var k = b.getAttribute("data-donate");
    if (D[k]) { b.setAttribute("href", D[k]); b.setAttribute("target", "_blank"); b.setAttribute("rel", "noopener"); }
    else { b.setAttribute("href", "#pledge"); }
  });
  $$("[data-amount]").forEach(function (b) {
    b.addEventListener("click", function () {
      var f = $("#pledgeAmount"); if (f) { f.value = b.getAttribute("data-amount"); }
      $$("[data-amount]").forEach(function (x) { x.classList.remove("on"); }); b.classList.add("on");
      var link = D.stripe || D.paypal || D.buymeacoffee || D.kofi;
      if (!link) { var p = $("#pledge"); if (p) p.scrollIntoView({ behavior: "smooth" }); }
    });
  });

  /* ---------- affiliate links from config ---------- */
  var AFF = C.affiliates || {};
  $$("[data-aff]").forEach(function (a) { var k = a.getAttribute("data-aff"); if (AFF[k]) a.setAttribute("href", AFF[k]); });

  /* ---------- videos ---------- */
  var vg = $("#videoGrid");
  if (vg) {
    var vids = (C.videos || []).filter(function (v) { return v && v.id; });
    var fallback = JSON.parse(vg.getAttribute("data-fallback") || "[]");
    var list = vids.length ? vids : fallback;
    vg.innerHTML = list.map(function (v) {
      var thumb = v.id ? '<img loading="lazy" alt="" src="https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg">' : "";
      var q = encodeURIComponent(v.q || v.title);
      return '<article class="card video-card reveal"><button class="video-thumb" type="button" data-vid="' + (v.id || "") + '" data-q="' + q + '" aria-label="Play: ' + v.title + '">' + thumb + '<span class="play"></span></button><div class="body"><span class="tag">' + (v.topic || "Video") + "</span><h3>" + v.title + "</h3></div></article>";
    }).join("");
    vg.addEventListener("click", function (e) {
      var t = e.target.closest(".video-thumb"); if (!t) return;
      var id = t.getAttribute("data-vid");
      if (id) { t.outerHTML = '<iframe class="video-frame" src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1" title="YouTube video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'; }
      else { window.open("https://www.youtube.com/results?search_query=" + t.getAttribute("data-q"), "_blank", "noopener"); }
    });
    var ch = $("#ytChannel"); if (ch && C.youtubeChannel) { ch.href = C.youtubeChannel; }
  }

  /* ---------- reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } }); }, { threshold: .08 });
    $$(".reveal").forEach(function (el) { io.observe(el); });
    new MutationObserver(function () { $$(".reveal:not(.in)").forEach(function (el) { io.observe(el); }); }).observe(document.body, { childList: true, subtree: true });
  } else { $$(".reveal").forEach(function (el) { el.classList.add("in"); }); }

  /* ---------- floating CTA ---------- */
  var fc = $("#floatCta");
  if (fc) window.addEventListener("scroll", function () { fc.classList.toggle("show", window.scrollY > 900); }, { passive: true });

  /* ---------- counters ---------- */
  $$("[data-count]").forEach(function (el) {
    var end = +el.getAttribute("data-count"), t0 = null;
    function step(t) { if (!t0) t0 = t; var p = Math.min((t - t0) / 1200, 1); el.textContent = Math.round(end * p).toLocaleString() + (el.getAttribute("data-suffix") || ""); if (p < 1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  });

  var y = $("#year"); if (y) y.textContent = new Date().getFullYear();
})();
