"""Shared layout + components for the 0Office.com static site generator."""
import json, html

SITE_NAME = "0Office.com"
# Canonical base. Switch to "https://0office.com" after pointing the domain (see README).
SITE_URL = "https://webworksa1.github.io/0Office-com"
OWNER_URL = "https://web.works/contact"
TAGLINE = "Run your business from anywhere — zero office required."
YEAR = "2026"

NAV = [
    ("tools/index.html", "Free Tools", "tools"),
    ("guides/index.html", "Guides", "guides"),
    ("stack.html", "Remote Stack", "stack"),
    ("videos.html", "Videos", "videos"),
    ("hire.html", "Hire Talent", "hire"),
    ("contests.html", "Contests", "contests"),
    ("support.html", "Support Us", "support"),
]

INDEX = []  # search index entries, filled by page()
# "jekyll": pages are emitted as front matter + body and share _layouts/default.html
# (GitHub Pages renders them). "static": fully rendered standalone HTML (local preview).
MODE = "jekyll"


def esc(s):
    return html.escape(s, quote=True)


def topbar():
    return f'''<div class="topbar" role="note"><div class="container"><span class="dot" aria-hidden="true"></span>
<span><a href="{OWNER_URL}" target="_blank" rel="noopener">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership</a></span></div></div>'''


def header(root, active, liquid=False):
    cur = ' aria-current="page"'
    if liquid:
        links = "".join(
            f'<a href="{root}{u}"{{% if page.active == "{k}" %}}{cur}{{% endif %}}>{t}</a>' for u, t, k in NAV
        )
    else:
        links = "".join(
            f'<a href="{root}{u}"{cur if k == active else ""}>{t}</a>' for u, t, k in NAV
        )
    return f'''<a class="skip" href="#main">Skip to content</a>
{topbar()}
<header class="site-header"><div class="container nav">
<a class="logo" href="{root}index.html" aria-label="0Office.com home"><img class="logo-mark" src="{root}assets/img/logo.svg" alt="" width="36" height="36"><span>0Office<small>.com</small></span></a>
<nav class="nav-links" id="navLinks" aria-label="Main">{links}<a href="{root}get-started.html" class="btn btn-primary btn-sm" style="margin-left:6px">Free Plan</a></nav>
<div class="nav-actions">
<button class="icon-btn" data-search aria-label="Search (Ctrl+K)" title="Search (Ctrl+K)">⌕</button>
<button class="icon-btn" id="themeBtn" aria-label="Toggle dark mode" title="Toggle theme">◐</button>
<button class="icon-btn menu-btn" id="menuBtn" aria-label="Menu" aria-controls="navLinks" aria-expanded="false">☰</button>
</div></div></header>'''


def footer(root):
    r = root
    return f'''<footer class="site-footer"><div class="container">
<div class="foot-grid">
<div><a class="logo" href="{r}index.html" style="color:#fff"><img class="logo-mark" src="{r}assets/img/logo.svg" alt="" width="36" height="36"><span>0Office<small style="color:#9fb0cc">.com</small></span></a>
<p style="margin-top:12px">{TAGLINE} Free in-browser office tools, practical remote-work guides, and vetted help to set up a business that doesn't need a lease.</p>
<a class="btn btn-primary btn-sm" href="{r}get-started.html">Get your free plan →</a></div>
<div><h4>Free tools</h4><ul>
<li><a href="{r}tools/invoice-generator.html">Invoice Generator</a></li>
<li><a href="{r}tools/meeting-cost-calculator.html">Meeting Cost Calculator</a></li>
<li><a href="{r}tools/time-zone-planner.html">Time Zone Planner</a></li>
<li><a href="{r}tools/pomodoro-timer.html">Pomodoro Timer</a></li>
<li><a href="{r}tools/index.html">All tools →</a></li></ul></div>
<div><h4>Resources</h4><ul>
<li><a href="{r}guides/index.html">Guides</a></li>
<li><a href="{r}stack.html">Remote Stack Directory</a></li>
<li><a href="{r}checklist.html">Zero-Office Checklist</a></li>
<li><a href="{r}videos.html">Videos</a></li>
<li><a href="{r}hire.html">Hire Remote Talent</a></li></ul></div>
<div><h4>Partner &amp; earn</h4><ul>
<li><a href="{r}advertise.html">Advertise / Sponsor</a></li>
<li><a href="{r}contests.html">Contests &amp; Prizes</a></li>
<li><a href="{r}careers.html">Work With Us</a></li>
<li><a href="{r}support.html">Donate / Support</a></li>
<li><a href="{OWNER_URL}" target="_blank" rel="noopener">Buy / Partner on this domain</a></li></ul></div>
<div><h4>Company</h4><ul>
<li><a href="{r}about.html">About</a></li>
<li><a href="{r}contact.html">Contact</a></li>
<li><a href="{r}privacy.html">Privacy &amp; Cookies</a></li>
<li><a href="{r}terms.html">Terms of Use</a></li>
<li><a href="{r}disclaimer.html">Disclaimer &amp; Trademarks</a></li></ul></div>
</div>
<p class="foot-legal">0Office.com is an independent website and is not affiliated with, endorsed by, or sponsored by Microsoft Corporation (Microsoft Office / Microsoft 365), Ascensio System SIA (ONLYOFFICE), The Document Foundation (LibreOffice), Kingsoft (WPS Office), Google, Zoho or any other company named on this site. All product names, logos and brands are property of their respective owners and are used for identification only. Some links may be affiliate or sponsored links — see our <a href="{r}disclaimer.html">disclosures</a>.</p>
<div class="foot-bottom"><span>© <span id="year">{YEAR}</span> 0Office.com. All rights reserved. Original content and code are protected by copyright.</span>
<span><a href="{r}sitemap.xml">Sitemap</a> · <a href="{r}contact.html">Contact</a> · <a href="{OWNER_URL}" target="_blank" rel="noopener">Domain &amp; partnership inquiries</a></span></div>
</div></footer>
<a class="btn btn-primary float-cta no-print" id="floatCta" href="{r}get-started.html">Get free plan →</a>
<div class="cookie" id="cookie" role="dialog" aria-live="polite" aria-label="Cookie consent"><strong>Cookies &amp; privacy</strong>
<p class="muted" style="margin:6px 0 0;font-size:.9rem">We use essential storage to run the tools. With your consent we also use analytics and advertising cookies (e.g. Google AdSense) to keep the site free. <a href="{r}privacy.html#cookies">Details</a></p>
<div class="row"><button class="btn btn-primary btn-sm" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div></div>
<div class="modal" id="searchModal" role="dialog" aria-label="Search"><div class="modal-box"><input id="searchInput" type="search" placeholder="Search tools, guides, pages…" aria-label="Search"><div class="results" id="searchResults"></div></div></div>'''


def ad(pos="inContent"):
    return f'<div class="ad-slot no-print" aria-label="Advertisement"><div class="ad-inner" data-ad="{pos}"></div></div>'


def status():
    return '<div class="form-status" role="status" aria-live="polite"></div>'


def honey():
    return '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'


def newsletter(root, heading="Get the Zero-Office Brief", text="One practical email every two weeks: new free tools, remote-work playbooks, and deals on the software remote teams actually use. No spam — unsubscribe anytime."):
    return f'''<section><div class="container"><div class="cta-band reveal">
<div><span class="eyebrow" style="background:rgba(255,255,255,.12);color:#99f6e4">Newsletter</span><h2 style="color:#fff">{heading}</h2><p>{text}</p></div>
<form class="form" data-form="Newsletter signup" data-success="You're in! Watch your inbox for the next Zero-Office Brief.">{honey()}
<label class="sr-only" for="nl-email">Email</label><input id="nl-email" type="email" name="email" required placeholder="you@company.com" autocomplete="email">
<select name="role" aria-label="I am a…"><option>Founder / business owner</option><option>Freelancer / solopreneur</option><option>Team lead / HR</option><option>Remote employee</option><option>Digital nomad</option></select>
<button class="btn btn-primary btn-block" type="submit">Subscribe free</button>{status()}
<p class="form-note" style="color:#94a3b8">By subscribing you agree to our <a href="{root}privacy.html" style="color:#cbd5e1">privacy policy</a>.</p></form>
</div></div></section>'''


NEEDS = [
    ("virtual-office", "🏢", "Virtual office address + mail scanning"),
    ("coworking", "🪑", "Coworking desk, day pass or meeting rooms"),
    ("phone", "📞", "Business phone number / VoIP"),
    ("payroll", "🌍", "Remote payroll, EOR or contractor payments"),
    ("talent", "🧑‍💻", "Hire remote talent (dev, design, VA, sales)"),
    ("formation", "📄", "Company formation / registered agent"),
    ("it-setup", "💻", "Laptops, IT security & software setup"),
    ("consulting", "🧭", "Remote-work policy & team consulting"),
]


def lead_form(root, compact=False):
    choices = "".join(
        f'<label class="choice"><input type="checkbox" name="needs" value="{v}" data-group-required><span>{i} {t}</span></label>' for v, i, t in NEEDS
    )
    return f'''<form class="form lead-card" data-form="Zero-Office Plan request" data-steps data-success="Request received ✓ — a Zero-Office specialist will email your personalised plan and matched options within 1 business day.">
{honey()}
<div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><strong>Your free Zero-Office plan</strong><span class="muted" data-step-label style="font-size:.85rem"></span></div>
<div class="progress" aria-hidden="true"><i></i></div>
<div class="step"><label>What do you need? <span class="muted">(pick all that apply)</span></label><div class="choice-grid">{choices}</div>
<div class="step-nav"><span></span><button type="button" class="btn btn-primary" data-next>Continue →</button></div></div>
<div class="step">
<div class="form-row"><div><label for="lf-size">Team size</label><select id="lf-size" name="team_size" required><option value="">Select…</option><option>Just me</option><option>2–5</option><option>6–20</option><option>21–100</option><option>100+</option></select></div>
<div><label for="lf-when">Timeline</label><select id="lf-when" name="timeline" required><option value="">Select…</option><option>ASAP (this week)</option><option>Within 30 days</option><option>1–3 months</option><option>Just researching</option></select></div></div>
<div class="form-row"><div><label for="lf-city">City</label><input id="lf-city" name="city" required placeholder="e.g. Montréal, Austin, Dubai"></div>
<div><label for="lf-country">Country</label><input id="lf-country" name="country" required placeholder="e.g. Canada"></div></div>
<div><label for="lf-budget">Monthly budget (USD)</label><select id="lf-budget" name="budget"><option>Under $100</option><option>$100–$500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option><option>Not sure yet</option></select></div>
<div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div></div>
<div class="step">
<div class="form-row"><div><label for="lf-name">Full name</label><input id="lf-name" name="name" required autocomplete="name"></div>
<div><label for="lf-email">Work email</label><input id="lf-email" type="email" name="email" required autocomplete="email"></div></div>
<div class="form-row"><div><label for="lf-phone">Phone <span class="muted">(optional)</span></label><input id="lf-phone" type="tel" name="phone" autocomplete="tel"></div>
<div><label for="lf-co">Company <span class="muted">(optional)</span></label><input id="lf-co" name="company" autocomplete="organization"></div></div>
<div><label for="lf-notes">Anything else? <span class="muted">(optional)</span></label><textarea id="lf-notes" name="notes" rows="3" placeholder="e.g. Need a Toronto address for incorporation + 3 contractors paid in USD"></textarea></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about this request and that 0Office.com may share my details with up to 3 relevant, vetted providers. <a href="{root}privacy.html">Privacy</a></label>
{status()}
<div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="submit" class="btn btn-primary">Get my free plan</button></div></div>
<p class="form-note" style="margin:6px 0 0">🔒 Free, no obligation. Your details are never sold to lists.</p>
</form>'''


def page(path, title, desc, body, active="", schema=None, scripts=(), keywords="", index=True, hero=None, root_override=None):
    depth = path.count("/")
    root = root_override if root_override is not None else "../" * depth
    url = f"{SITE_URL}/{path}".replace("/index.html", "/") if path != "index.html" else f"{SITE_URL}/"
    full_title = title if "0Office" in title else f"{title} | 0Office.com"
    if index:
        INDEX.append({"u": path, "t": title.replace(" | 0Office.com", ""), "d": desc[:140], "k": keywords})
    ld = ""
    base_ld = {"@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME, "url": SITE_URL + "/"}
    for s in ([base_ld] if path == "index.html" else []) + (schema or []):
        ld += f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>\n'
    extra = "".join(f'<script src="{root}assets/js/{s}" defer></script>' for s in scripts)
    if MODE == "jekyll":
        fm = {"layout": "default", "t": esc(full_title), "d": esc(desc), "canon": url,
              "robots": "index,follow" if index else "noindex", "root": root, "active": active, "ld": ld, "extra": extra}
        front = "---\n" + "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in fm.items()) + "---\n"
        return front + "{% raw %}" + f"{hero or ''}\n{body}" + "{% endraw %}\n"
    return shell(root, active, esc(full_title), esc(desc), url, "index,follow" if index else "noindex", ld, extra, f"{hero or ''}\n{body}")


def jekyll_layout():
    return shell("{{ page.root }}", None, "{{ page.t }}", "{{ page.d }}", "{{ page.canon }}", "{{ page.robots }}", "{{ page.ld }}", "{{ page.extra }}", "{{ content }}", liquid=True)


def shell(root, active, title, desc, url, robots, ld, extra, content, liquid=False):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0d9488">
<meta property="og:type" content="website"><meta property="og:site_name" content="0Office.com">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{root}assets/img/logo.svg" type="image/svg+xml">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
<script>document.documentElement.classList.add("js");try{{var t=localStorage.getItem("o0-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{ld}</head>
<body data-root="{root}">
{header(root, active, liquid)}
<main id="main">
{content}
</main>
{footer(root)}
<script src="{root}assets/js/config.js"></script>
<script src="{root}assets/js/search-index.js" defer></script>
<script src="{root}assets/js/app.js" defer></script>
{extra}
</body>
</html>
'''


def page_hero(root, crumbs, h1, lead, eyebrow=""):
    cr = " / ".join([f'<a href="{root}index.html">Home</a>'] + [f'<a href="{root}{u}">{t}</a>' if u else t for t, u in crumbs])
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    return f'''<div class="page-hero"><div class="container"><nav class="crumbs" aria-label="Breadcrumb">{cr}</nav>{eb}<h1>{h1}</h1><p class="lead muted" style="font-size:1.15rem;max-width:760px">{lead}</p></div></div>'''


def faq_block(items):
    body = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)}} for q, a in items]}
    return body, schema
