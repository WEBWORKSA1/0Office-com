"""Core site pages."""
import json
from layout import page, page_hero, ad, newsletter, lead_form, honey, status, faq_block, OWNER_URL, NEEDS
from tools_pages import TOOLS
from guides import GUIDES

FALLBACK_VIDEOS = [
    {"title": "Home office setup ideas for productive remote work", "topic": "Workspace", "q": "home office setup tour productive"},
    {"title": "Async communication for remote teams", "topic": "Teams", "q": "async communication remote teams"},
    {"title": "What is a virtual office and how does it work?", "topic": "Virtual office", "q": "what is a virtual office explained"},
    {"title": "How to hire remote employees internationally", "topic": "Hiring", "q": "how to hire remote employees internationally EOR"},
    {"title": "Pomodoro technique explained", "topic": "Focus", "q": "pomodoro technique explained"},
    {"title": "Freelance pricing: how to set your rate", "topic": "Money", "q": "how to set freelance rate"},
]


def home():
    r = ""
    tools = "".join(f'<a class="card reveal" href="tools/{t["slug"]}.html"><div class="ico">{t["icon"]}</div><h3>{t["name"]}</h3><p>{t["short"]}</p></a>' for t in TOOLS[:8])
    guides = "".join(f'<a class="card reveal" href="guides/{g["slug"]}.html"><span class="tag">{g["cat"]}</span><h3>{g["title"]}</h3><p>{g["desc"]}</p></a>' for g in GUIDES[:3])
    faq_html, faq_schema = faq_block([
        ("What does “0Office” mean?", "Zero office: running a business, team or freelance career without a traditional leased office. We help you replace each thing an office did — address, phone, meeting space, tools and team coordination — with flexible, pay-as-you-go options."),
        ("Are the tools really free?", "Yes. All tools run in your browser with no signup. The site is funded by advertising, sponsorships, partner referrals and reader support."),
        ("What happens when I request a Zero-Office plan?", "A specialist reviews your needs and emails a short plan with matched options. With your consent we may introduce you to up to three relevant, vetted providers. There is no cost or obligation."),
        ("Is 0Office.com related to Microsoft Office or other office software?", "No. 0Office.com is an independent site and is not affiliated with Microsoft, ONLYOFFICE, LibreOffice, WPS or any other office-software brand."),
        ("How can my company advertise or partner?", "See our advertising and sponsorship options, or use the contact link at the top of every page for partnership, sponsorship or domain inquiries."),
    ])
    hero = f'''<section class="hero"><div class="container hero-grid">
<div><span class="eyebrow">Remote business hub</span>
<h1>Run your business with <span class="grad">zero office</span>.</h1>
<p class="lead">Free in-browser office tools, practical playbooks, and a free personalised plan to replace your lease with a virtual address, cloud phone, global payroll and remote talent.</p>
<form class="hero-search" id="heroSearch" role="search"><input type="search" placeholder="Try “invoice”, “time zones” or “virtual office”" aria-label="Search 0Office"><button class="btn btn-primary" type="submit">Search</button></form>
<div class="hero-cta"><a class="btn btn-primary btn-lg" href="get-started.html">Get my free Zero-Office plan →</a><a class="btn btn-ghost btn-lg" href="tools/index.html">Explore free tools</a></div>
<div class="intent-row"><a class="chip" href="get-started.html?need=virtual-office">🏢 Need an address</a><a class="chip" href="hire.html">🧑‍💻 Hire remote talent</a><a class="chip" href="get-started.html?need=payroll">🌍 Pay a global team</a><a class="chip" href="tools/invoice-generator.html">🧾 Send an invoice</a></div>
</div>
<div class="hero-panel reveal" aria-label="What an office used to do"><strong>Everything an office did — without the lease</strong>
<div class="mini-row"><span>🏢 Business address</span><span class="tag" style="margin:0">Virtual office</span></div>
<div class="mini-row"><span>📞 Front desk &amp; phone</span><span class="tag" style="margin:0">Cloud VoIP</span></div>
<div class="mini-row"><span>🪑 Meeting rooms</span><span class="tag" style="margin:0">By the hour</span></div>
<div class="mini-row"><span>🌍 Payroll &amp; HR</span><span class="tag" style="margin:0">EOR / contractors</span></div>
<div class="mini-row"><span>🗂 Files &amp; tools</span><span class="tag" style="margin:0">Cloud stack</span></div>
<div class="mini-row"><span>🤝 Team culture</span><span class="tag" style="margin:0">Async-first</span></div>
<a class="btn btn-primary btn-block" style="margin-top:14px" href="get-started.html">Build my stack free</a></div>
</div></section>'''
    body = f'''<section style="padding:10px 0 40px"><div class="container"><div class="stats">
<div class="stat"><b data-count="{len(TOOLS)}">{len(TOOLS)}</b>free office tools</div><div class="stat"><b>0</b>signups required</div><div class="stat"><b>100%</b>processed in your browser</div><div class="stat"><b data-count="{len(GUIDES)}">{len(GUIDES)}</b>in-depth playbooks</div></div></div></section>
{ad("top")}
<section><div class="container"><div class="section-head"><span class="eyebrow">Free tools</span><h2>Office tools that open instantly</h2><p class="muted">No downloads. No accounts. Nothing uploaded. Just the job done.</p></div>
<div class="grid g4">{tools}</div><p class="center" style="margin-top:24px"><a class="btn btn-ghost" href="tools/index.html">See all {len(TOOLS)} tools →</a></p></div></section>
<section class="alt"><div class="container"><div class="section-head"><span class="eyebrow">Who it's for</span><h2>Built for people who work from anywhere</h2></div>
<div class="grid g4">
<div class="card reveal"><div class="ico">🚀</div><h3>Founders</h3><p>Launch with a real address, phone and payroll — without a lease. <a href="get-started.html">Get a plan</a>.</p></div>
<div class="card reveal"><div class="ico">🧑‍💻</div><h3>Freelancers</h3><p>Invoice, price and focus with free tools. Join the <a href="hire.html#talent">talent network</a>.</p></div>
<div class="card reveal"><div class="ico">👥</div><h3>Remote teams</h3><p>Cut meeting costs and find shared hours across time zones.</p></div>
<div class="card reveal"><div class="ico">📣</div><h3>Brands &amp; providers</h3><p>Reach remote decision-makers. <a href="advertise.html">Advertise or sponsor</a>.</p></div></div></div></section>
<section id="plan"><div class="container lead-wrap">
<div><span class="eyebrow">Free Zero-Office plan</span><h2>Replace your office in 60 seconds</h2>
<p class="muted">Answer three quick questions. A specialist sends a short, personalised plan with matched options for your city and budget.</p>
<ul class="ticks"><li>Business address &amp; mail scanning options in your city</li><li>Cloud phone, payroll/EOR and talent recommendations</li><li>Estimated monthly cost vs. a traditional office</li><li>Free, no obligation — unsubscribe any time</li></ul>
<p class="muted"><small>Providers: want to receive qualified leads? <a href="advertise.html#partners">Become a partner</a>.</small></p></div>
{lead_form(r)}</div></section>
{ad("inContent")}
<section class="alt"><div class="container"><div class="section-head"><span class="eyebrow">Playbooks</span><h2>Learn the zero-office way</h2></div><div class="grid g3">{guides}</div>
<p class="center" style="margin-top:24px"><a class="btn btn-ghost" href="guides/index.html">All guides →</a> <a class="btn btn-ghost" href="checklist.html">Free launch checklist</a></p></div></section>
<section><div class="container"><div class="section-head"><span class="eyebrow">Watch</span><h2>Remote work, explained in minutes</h2></div>
<div class="grid g3" id="videoGrid" data-fallback='{json.dumps(FALLBACK_VIDEOS[:3])}'></div>
<p class="center" style="margin-top:24px"><a class="btn btn-ghost" href="videos.html">More videos →</a></p></div></section>
<section class="alt"><div class="container"><div class="grid g3">
<a class="card reveal" href="contests.html"><div class="ico">🏆</div><h3>Contests &amp; prizes</h3><p>Show off your remote setup, pitch a tool idea, share your story — win sponsor-funded prizes.</p></a>
<a class="card reveal" href="careers.html"><div class="ico">🤝</div><h3>We're hiring talent</h3><p>Writers, video editors, developers and partnership sellers — remote, flexible, paid.</p></a>
<a class="card reveal" href="support.html"><div class="ico">💚</div><h3>Support 0Office</h3><p>Keep the tools free. Donations fund hosting, new tools, promotion and prizes.</p></a></div></div></section>
<section><div class="container"><div class="section-head"><h2>Frequently asked questions</h2></div><div style="max-width:800px;margin:0 auto">{faq_html}</div></div></section>
{newsletter(r)}'''
    org = {"@context": "https://schema.org", "@type": "Organization", "name": "0Office.com", "url": "https://0office.com", "logo": "https://0office.com/assets/img/logo.svg"}
    return page("index.html", "0Office.com — Run Your Business With Zero Office | Free Tools & Remote Work Hub",
                "Free online office tools, remote-work playbooks and a free personalised plan to replace your office with a virtual address, cloud phone, global payroll and remote talent.",
                body, active="", schema=[org, faq_schema], hero=hero, keywords="home remote office")


def get_started():
    r = ""
    body = f'''<section style="padding-top:36px"><div class="container lead-wrap">
<div><h2>How it works</h2><ol class="prose" style="margin:0;padding-left:1.2em;font-size:1rem">
<li><b>Tell us what you need</b> — address, phone, payroll, talent, IT.</li>
<li><b>We match options</b> for your city, team size and budget.</li>
<li><b>You get a plan by email</b> within one business day, with up to 3 vetted provider introductions if you want them.</li></ol>
<ul class="ticks"><li>100% free for you — providers pay us, not you</li><li>No spam lists, no sold data</li><li>Independent: we recommend what fits, not who pays most</li></ul>
<div class="card"><strong>Prefer to talk to a human?</strong><p style="margin:6px 0 10px">Send a quick message and we'll reply by email.</p><a class="btn btn-ghost btn-sm" href="contact.html">Contact us</a> <a class="btn btn-ghost btn-sm" href="#" data-mail="Zero-Office plan question">Email us</a></div></div>
{lead_form(r)}</div></section>
{ad("inContent")}
<section class="alt"><div class="container"><div class="section-head"><h2>What can we help with?</h2></div><div class="grid g4">
{"".join(f'<a class="card" href="get-started.html?need={v}"><div class="ico">{i}</div><h3 style="font-size:1rem">{t}</h3></a>' for v, i, t in NEEDS)}
</div></div></section>'''
    hero = page_hero(r, [("Free Zero-Office Plan", "")], "Get your free Zero-Office plan", "Replace the lease with flexible services that fit your city, team and budget. Takes about 60 seconds.", eyebrow="Free · No obligation")
    return page("get-started.html", "Free Zero-Office Plan — Virtual Office, Phone, Payroll & Talent", "Get a free personalised plan to run your business without an office: virtual address, cloud phone, remote payroll, coworking and remote talent matched to your city.", body, active="", hero=hero, keywords="quote plan virtual office leads")


CHECK = [
    ("Legal & address", ["Choose business structure and register the company", "Get a business address that isn't your home (virtual mailbox / office)", "Register a registered agent if your jurisdiction requires one", "Open a business bank account with strong online access", "Set up bookkeeping and invoicing"]),
    ("Communication", ["Business email on your own domain", "Cloud phone number with voicemail-to-email", "One team chat tool with a short channel list", "Video calling with recording and screen share"]),
    ("Work & documents", ["Company-owned shared drive with a clear folder structure", "Task / project board", "Written handbook: working hours, response times, meeting rules", "Password manager with shared vaults + 2FA everywhere"]),
    ("People", ["Decide contractor vs EOR vs own entity per hire", "Remote-ready job descriptions with time-zone overlap", "Contracts: IP assignment, confidentiality, payment terms", "Onboarding plan: accounts, laptop, 30-60-90 goals, buddy"]),
    ("Spaces", ["Ergonomic home setup: chair, monitor, light, mic, internet backup", "Coworking day-pass / meeting-room account for in-person days", "Budget for team meetups"]),
]


def checklist():
    r = ""
    sec = ""
    for h, items in CHECK:
        sec += f"<h2>{h}</h2>" + "".join(f'<label class="check" style="font-size:1rem;color:var(--text);margin:10px 0"><input type="checkbox"> {i}</label>' for i in items)
    body = f'''<section style="padding-top:36px"><div class="container tool-shell"><div class="tool-box prose" style="max-width:none">{sec}
<p class="no-print" style="margin-top:24px"><button class="btn btn-primary" onclick="window.print()" type="button">⬇ Print / save as PDF</button></p></div>
<aside class="sidebar no-print"><div class="card"><h3>Get the template pack</h3><p style="margin-bottom:12px">Handbook template, onboarding checklist and meeting rules — sent to your inbox.</p>
<form class="form" data-form="Checklist template pack" data-success="Sent! Check your inbox for the template pack.">{honey()}<input type="text" name="name" placeholder="First name" required aria-label="First name"><input type="email" name="email" placeholder="Email" required aria-label="Email"><button class="btn btn-primary btn-block" type="submit">Email me the pack</button>{status()}</form></div>
<div class="card"><h3>Skip the legwork</h3><p style="margin-bottom:12px">We'll match providers for every line on this list.</p><a class="btn btn-ghost btn-block" href="get-started.html">Get free plan</a></div></aside></div></section>'''
    hero = page_hero(r, [("Resources", "guides/index.html"), ("Launch Checklist", "")], "Zero-Office Launch Checklist", "Everything you need to run a business with no office — tick it off, print it, share it.", eyebrow="Free download")
    return page("checklist.html", "Zero-Office Launch Checklist (Free, Printable)", "A free printable checklist for launching or moving a business to a fully remote, office-free setup.", body, hero=hero, keywords="checklist template remote setup")


STACK = [
    ("💬", "Team chat & video", [("Slack", "https://slack.com"), ("Microsoft Teams", "https://www.microsoft.com/microsoft-teams"), ("Zoom", "https://zoom.us"), ("Google Meet", "https://meet.google.com")]),
    ("📄", "Docs & office suites", [("Google Workspace", "https://workspace.google.com"), ("Microsoft 365", "https://www.microsoft.com/microsoft-365"), ("LibreOffice", "https://www.libreoffice.org"), ("Zoho Workplace", "https://www.zoho.com/workplace/")]),
    ("✅", "Projects & tasks", [("Asana", "https://asana.com"), ("Trello", "https://trello.com"), ("Notion", "https://www.notion.com"), ("ClickUp", "https://clickup.com")]),
    ("🌍", "Global payroll & EOR", [("Deel", "https://www.deel.com"), ("Remote", "https://remote.com"), ("Oyster", "https://www.oysterhr.com"), ("Gusto", "https://gusto.com")]),
    ("📬", "Virtual address & mail", [("Anytime Mailbox", "https://www.anytimemailbox.com"), ("iPostal1", "https://ipostal1.com"), ("Davinci Virtual", "https://www.davincivirtual.com"), ("Regus", "https://www.regus.com")]),
    ("🪑", "Coworking on demand", [("LiquidSpace", "https://liquidspace.com"), ("Deskpass", "https://www.deskpass.com"), ("Coworker", "https://www.coworker.com"), ("WeWork", "https://www.wework.com")]),
    ("🧾", "Invoicing & accounting", [("FreshBooks", "https://www.freshbooks.com"), ("QuickBooks", "https://quickbooks.intuit.com"), ("Wave", "https://www.waveapps.com"), ("Xero", "https://www.xero.com")]),
    ("⏱️", "Time tracking", [("Toggl Track", "https://toggl.com/track/"), ("Clockify", "https://clockify.me"), ("Harvest", "https://www.getharvest.com")]),
    ("🔐", "Passwords & security", [("1Password", "https://1password.com"), ("Bitwarden", "https://bitwarden.com"), ("NordLayer", "https://nordlayer.com")]),
    ("🎥", "Async video", [("Loom", "https://www.loom.com"), ("Vimeo", "https://vimeo.com")]),
    ("📞", "Cloud phone / VoIP", [("RingCentral", "https://www.ringcentral.com"), ("Dialpad", "https://www.dialpad.com"), ("Grasshopper", "https://www.grasshopper.com")]),
    ("✍️", "E-signature", [("DocuSign", "https://www.docusign.com"), ("Dropbox Sign", "https://sign.dropbox.com"), ("PandaDoc", "https://www.pandadoc.com")]),
]


def slug(s):
    return "".join(c.lower() if c.isalnum() else "-" for c in s).strip("-")


def stack():
    r = ""
    cards = ""
    for icon, cat, items in STACK:
        li = "".join(f'<li><a href="{u}" data-aff="{slug(n)}" target="_blank" rel="noopener sponsored">{n} ↗</a></li>' for n, u in items)
        cards += f'<div class="card reveal"><div class="ico">{icon}</div><h3>{cat}</h3><ul style="list-style:none;padding:0;margin:10px 0 0">{li}</ul></div>'
    body = f'''<section style="padding-top:36px"><div class="container">
<p class="card" style="margin-bottom:24px"><b>Disclosure:</b> Listings are independent and in no particular order. Some links may become affiliate or sponsored links, which help fund this free site at no cost to you. Sponsored placements are always labelled. Trademarks belong to their owners; 0Office.com is not affiliated with these companies.</p>
<div class="grid g3">{cards}</div></div></section>
{ad("inContent")}
<section class="alt"><div class="container center"><h2>Are you a vendor?</h2><p class="muted">Get a featured listing, sponsored comparison or qualified referrals from teams going remote.</p><a class="btn btn-primary" href="advertise.html#partners">List your product</a> <a class="btn btn-ghost" href="get-started.html">Not sure what to pick? Get a free plan</a></div></section>
{newsletter(r)}'''
    hero = page_hero(r, [("Remote Stack", "")], "The Remote Stack directory", "Well-known tools for every job an office used to do — grouped by category so you can pick one per job and skip the sprawl.", eyebrow="Directory")
    return page("stack.html", "Remote Work Software Directory — The Zero-Office Stack", "A categorised directory of remote-work software: chat, docs, project management, global payroll, virtual mailboxes, coworking, invoicing, security and more.", body, active="stack", hero=hero, keywords="software directory saas tools slack zoom deel")


def videos():
    r = ""
    body = f'''<section style="padding-top:36px"><div class="container">
<div class="grid g3" id="videoGrid" data-fallback='{json.dumps(FALLBACK_VIDEOS)}'></div>
<div class="card center" style="margin-top:32px"><h3>Subscribe on YouTube</h3><p style="margin-bottom:14px">New remote-work explainers, tool walkthroughs and setup tours.</p><a class="btn btn-accent" id="ytChannel" href="https://www.youtube.com/results?search_query=remote+work+tips" target="_blank" rel="noopener">▶ Watch on YouTube</a></div></div></section>
{ad("inContent")}
<section class="alt"><div class="container lead-wrap"><div><h2>Sponsor a video or send us your story</h2><p class="muted">Brands can sponsor episodes, tool walkthroughs and setup tours. Remote workers can pitch their workspace or story for a feature.</p><a class="btn btn-ghost" href="advertise.html">Video sponsorship options</a></div>
<form class="form lead-card" data-form="Video pitch / sponsorship" data-success="Thanks! We'll review your pitch and reply by email.">{honey()}
<div class="form-row"><div><label for="v-name">Name</label><input id="v-name" name="name" required></div><div><label for="v-email">Email</label><input id="v-email" type="email" name="email" required></div></div>
<div><label for="v-type">I want to…</label><select id="v-type" name="type"><option>Sponsor a video</option><option>Be featured (my setup / story)</option><option>Collaborate as a creator</option></select></div>
<div><label for="v-msg">Details / links</label><textarea id="v-msg" name="message" required></textarea></div><button class="btn btn-primary" type="submit">Send</button>{status()}</form></div></section>'''
    hero = page_hero(r, [("Videos", "")], "Videos", "Short, practical videos on remote setups, async teamwork, hiring and money. Click to play.", eyebrow="Watch &amp; learn")
    return page("videos.html", "Remote Work Videos & Tutorials", "Watch practical videos on home office setup, async communication, virtual offices, remote hiring and freelance pricing.", body, active="videos", hero=hero, keywords="youtube video tutorials")


def hire():
    r = ""
    body = f'''<section style="padding-top:36px"><div class="container lead-wrap">
<div><span class="eyebrow">For companies</span><h2>Hire vetted remote talent</h2><p class="muted">Developers, designers, marketers, virtual assistants, customer support and sales — matched to your time zone and budget, via our talent network and trusted staffing partners.</p>
<ul class="ticks"><li>Shortlist of pre-screened candidates</li><li>Contractor, EOR or direct-hire options</li><li>Time-zone overlap you specify</li><li>Free to request — no obligation</li></ul></div>
<form class="form lead-card" data-form="Hire talent request" data-success="Got it ✓ — we'll email you a shortlist plan within 1–2 business days.">{honey()}
<div class="form-row"><div><label for="h-role">Role needed</label><input id="h-role" name="role" required placeholder="e.g. React developer"></div>
<div><label for="h-level">Seniority</label><select id="h-level" name="seniority"><option>Junior</option><option selected>Mid-level</option><option>Senior</option><option>Lead / Principal</option></select></div></div>
<div class="form-row"><div><label for="h-type">Engagement</label><select id="h-type" name="engagement"><option>Freelance / project</option><option>Part-time contractor</option><option>Full-time contractor</option><option>Full-time employee (EOR)</option></select></div>
<div><label for="h-tz">Time-zone overlap needed</label><input id="h-tz" name="timezone" placeholder="e.g. 4h with Eastern Time"></div></div>
<div class="form-row"><div><label for="h-budget">Budget</label><input id="h-budget" name="budget" placeholder="e.g. $40–60/hr or $6k/mo"></div>
<div><label for="h-start">Start</label><select id="h-start" name="start"><option>ASAP</option><option>Within 30 days</option><option>1–3 months</option></select></div></div>
<div class="form-row"><div><label for="h-name">Your name</label><input id="h-name" name="name" required></div><div><label for="h-email">Work email</label><input id="h-email" type="email" name="email" required></div></div>
<div><label for="h-co">Company &amp; website</label><input id="h-co" name="company"></div>
<div><label for="h-notes">Must-have skills</label><textarea id="h-notes" name="notes" rows="3"></textarea></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted and introduced to relevant talent or staffing partners.</label>
<button class="btn btn-primary" type="submit">Request talent</button>{status()}</form></div></section>
{ad("inContent")}
<section class="alt" id="talent"><div class="container lead-wrap">
<div><span class="eyebrow">For professionals</span><h2>Join the remote talent network</h2><p class="muted">Get matched to remote projects and roles from companies that request talent through 0Office.com. Free to join.</p>
<ul class="ticks"><li>Profile reviewed by a human</li><li>Only relevant opportunities, by email</li><li>Remove yourself any time</li></ul></div>
<form class="form lead-card" data-form="Talent network signup" data-success="Welcome to the network ✓ — we'll be in touch when a matching role comes in.">{honey()}
<div class="form-row"><div><label for="t-name">Full name</label><input id="t-name" name="name" required></div><div><label for="t-email">Email</label><input id="t-email" type="email" name="email" required></div></div>
<div class="form-row"><div><label for="t-skill">Primary skill</label><input id="t-skill" name="skill" required placeholder="e.g. UX design"></div><div><label for="t-exp">Years of experience</label><select id="t-exp" name="experience"><option>0–2</option><option>3–5</option><option>6–10</option><option>10+</option></select></div></div>
<div class="form-row"><div><label for="t-loc">Country / time zone</label><input id="t-loc" name="location" required></div><div><label for="t-rate">Rate expectation</label><input id="t-rate" name="rate" placeholder="e.g. $35/hr"></div></div>
<div><label for="t-url">Portfolio / LinkedIn URL</label><input id="t-url" type="url" name="portfolio" placeholder="https://"></div>
<button class="btn btn-primary" type="submit">Join the network</button>{status()}</form></div></section>'''
    hero = page_hero(r, [("Hire Talent", "")], "Hire remote talent — or get hired", "A two-sided network connecting companies with vetted remote professionals.", eyebrow="Talent")
    return page("hire.html", "Hire Remote Talent & Join the Remote Talent Network", "Request vetted remote developers, designers, marketers and assistants, or join the 0Office remote talent network for free.", body, active="hire", hero=hero, keywords="hire remote developers freelancers talent jobs")


CONTESTS = [
    ("🖥️", "Best Remote Workspace", "Share a photo of your home office or nomad setup with a short note on what makes it work.", "Photo link + 100–200 words"),
    ("💡", "Tool Idea Challenge", "Pitch a free browser tool that would save remote workers time. The winning idea gets built and credited.", "Idea + problem it solves (≤300 words)"),
    ("✍️", "Zero-Office Story", "Tell us how you run a business, team or career without an office — lessons, numbers, mistakes.", "Article 600–1,500 words"),
]


def contests():
    r = ""
    cards = "".join(f'<div class="card reveal"><div class="ico">{i}</div><span class="tag new">Entries open</span><h3>{t}</h3><p>{d}</p><p style="margin-top:10px"><small><b>Format:</b> {f}</small></p><a class="btn btn-primary btn-sm" style="margin-top:12px" href="#enter">Enter</a></div>' for i, t, d, f in CONTESTS)
    opts = "".join(f"<option>{t}</option>" for _, t, _, _ in CONTESTS)
    body = f'''<section style="padding-top:36px"><div class="container"><div class="grid g3">{cards}</div></div></section>
<section class="alt"><div class="container"><div class="grid g3">
<div class="card"><h3>🏆 Prizes</h3><p>Cash, gear and software prizes are funded by sponsors and reader support. Each round's prize list is published on this page before judging begins.</p></div>
<div class="card"><h3>⚖️ Judging</h3><p>Judged by the 0Office.com editorial team on usefulness, originality and clarity. Winners are featured on the site, newsletter and videos.</p></div>
<div class="card"><h3>🤝 Sponsor a prize</h3><p>Put your brand on a contest and in front of every entrant. <a href="advertise.html">See contest sponsorship</a>.</p></div></div></div></section>
{ad("inContent")}
<section id="enter"><div class="container lead-wrap">
<div><h2>Submit your entry</h2><p class="muted">One entry per person per contest. Free to enter — no purchase necessary.</p>
<details><summary>Official rules (summary)</summary><p>Open to individuals aged 18+ (or the age of majority where they live) where not prohibited by law. Void where prohibited or restricted. No purchase necessary. Entries must be original work you own; by entering you grant 0Office.com a non-exclusive licence to display your entry with credit. Winners are chosen by judging, not chance, and notified by email; unclaimed prizes after 14 days may be re-awarded. Skill-testing questions, tax obligations and additional local rules may apply. Full rules for each round are published with its prize list. See also our <a href="terms.html">Terms</a>.</p></details></div>
<form class="form lead-card" data-form="Contest entry" data-success="Entry received ✓ — good luck! We'll email you before judging.">{honey()}
<div><label for="c-which">Contest</label><select id="c-which" name="contest" required>{opts}</select></div>
<div class="form-row"><div><label for="c-name">Full name</label><input id="c-name" name="name" required></div><div><label for="c-email">Email</label><input id="c-email" type="email" name="email" required></div></div>
<div><label for="c-country">Country</label><input id="c-country" name="country" required></div>
<div><label for="c-link">Link to your entry (image, doc or post)</label><input id="c-link" type="url" name="entry_link" placeholder="https://"></div>
<div><label for="c-text">Your entry / description</label><textarea id="c-text" name="entry" required rows="6"></textarea></div>
<label class="check"><input type="checkbox" name="rules" value="accepted" required> I confirm I'm eligible, this is my original work, and I accept the rules.</label>
<button class="btn btn-primary" type="submit">Submit entry</button>{status()}</form></div></section>
{newsletter(r, "Get notified about new contests", "New rounds, prize announcements and winners — straight to your inbox.")}'''
    hero = page_hero(r, [("Contests", "")], "Contests &amp; prizes", "Show your setup, pitch a tool, tell your story — and win sponsor-funded prizes.", eyebrow="Community")
    return page("contests.html", "Remote Work Contests & Prizes", "Enter 0Office.com contests: best remote workspace, tool idea challenge and zero-office stories. Free to enter, sponsor-funded prizes.", body, active="contests", hero=hero, keywords="contest giveaway prize competition")


def support():
    r = ""
    alloc = [("Operations &amp; hosting", 30), ("New free tools &amp; content", 30), ("Promotion &amp; marketing", 15), ("Hiring talent", 15), ("Contest prizes", 10)]
    bars = "".join(f'<div style="margin:12px 0"><div style="display:flex;justify-content:space-between"><span>{n}</span><b>{p}%</b></div><div class="progress" style="margin:6px 0 0"><i style="width:{p}%"></i></div></div>' for n, p in alloc)
    body = f'''<section style="padding-top:36px"><div class="container">
<div class="grid g4">
<div class="card tier"><h3>☕ Coffee</h3><div class="price">$5</div><ul><li>Keeps a tool online for a month</li><li>Our sincere thanks</li></ul><button class="btn btn-ghost btn-block" data-amount="5" type="button">Give $5</button></div>
<div class="card tier featured"><span class="ribbon">Popular</span><h3>💚 Supporter</h3><div class="price">$25</div><ul><li>Funds a new guide or tool feature</li><li>Name on the supporters wall (optional)</li></ul><button class="btn btn-primary btn-block" data-amount="25" type="button">Give $25</button></div>
<div class="card tier"><h3>🚀 Champion</h3><div class="price">$100</div><ul><li>Funds contest prizes &amp; promotion</li><li>Supporters wall + newsletter thanks</li></ul><button class="btn btn-ghost btn-block" data-amount="100" type="button">Give $100</button></div>
<div class="card tier"><h3>🏢 Patron</h3><div class="price">Custom</div><ul><li>Monthly or one-off</li><li>Recognition options for companies</li></ul><a class="btn btn-ghost btn-block" href="#pledge">Talk to us</a></div></div>
<div class="card center" style="margin-top:24px"><h3>Give securely with</h3><div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin-top:10px">
<a class="btn btn-ghost" data-donate="paypal">PayPal</a><a class="btn btn-ghost" data-donate="stripe">Card (Stripe)</a><a class="btn btn-ghost" data-donate="buymeacoffee">Buy Me a Coffee</a><a class="btn btn-ghost" data-donate="kofi">Ko-fi</a><a class="btn btn-ghost" data-donate="githubSponsors">GitHub Sponsors</a></div>
<p class="form-note" style="margin-top:10px">Payment is processed by the provider you choose; we never see your card details. If a button takes you to the pledge form, that method is being set up — pledge below and we'll send a secure payment link.</p></div></div></section>
<section class="alt"><div class="container lead-wrap">
<div><h2>Where your support goes</h2><p class="muted">Our planned allocation of reader support:</p>{bars}
<p class="muted" style="margin-top:14px"><small>0Office.com is an independent website, not a registered charity; contributions are not tax-deductible.</small></p>
<h3 style="margin-top:24px">Other ways to help</h3><ul class="ticks"><li>Share a tool with a colleague</li><li><a href="careers.html#apply">Contribute a guide</a></li><li><a href="contests.html">Enter or sponsor a contest</a></li><li>Whitelist us in your ad blocker</li></ul></div>
<form class="form lead-card" id="pledge" data-form="Donation pledge" data-success="Thank you! 💚 We'll email you a secure payment link shortly.">{honey()}
<h3>Pledge your support</h3>
<div class="form-row"><div><label for="pledgeAmount">Amount (USD)</label><input id="pledgeAmount" type="number" min="1" name="amount" value="25" required></div>
<div><label for="p-freq">Frequency</label><select id="p-freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div><label for="p-use">Direct it to (optional)</label><select id="p-use" name="direct_to"><option>Wherever needed most</option><option>Operations &amp; hosting</option><option>New tools &amp; content</option><option>Promotion &amp; marketing</option><option>Hiring talent</option><option>Contest prizes</option></select></div>
<div class="form-row"><div><label for="p-name">Name</label><input id="p-name" name="name" required></div><div><label for="p-email">Email</label><input id="p-email" type="email" name="email" required></div></div>
<div><label for="p-msg">Message (optional)</label><textarea id="p-msg" name="message" rows="3"></textarea></div>
<label class="check"><input type="checkbox" name="public_credit" value="yes"> List my name on the supporters wall</label>
<button class="btn btn-primary" type="submit">Pledge support</button>{status()}</form></div></section>'''
    hero = page_hero(r, [("Support Us", "")], "Keep 0Office free for everyone", "Your support funds operations, new tools, promotion, hiring talent and contest prizes.", eyebrow="Donate")
    return page("support.html", "Support 0Office.com — Donate", "Support 0Office.com with a one-time or monthly donation to keep free office tools online and fund new tools, promotion, talent and contest prizes.", body, active="support", hero=hero, keywords="donate support patron sponsor")


def advertise():
    r = ""
    pk = [("🧰", "Tool sponsorship", "“Brought to you by” placement on a free tool page — high-intent users in the middle of a task."),
          ("📰", "Newsletter sponsorship", "Primary or secondary slot in the Zero-Office Brief."),
          ("🖼️", "Display &amp; native ads", "Direct-sold banners and native cards across guides and tools."),
          ("✍️", "Sponsored guide", "An expert, clearly-labelled guide on a topic relevant to your product."),
          ("⭐", "Featured directory listing", "Top placement in your Remote Stack category with a “Featured” label."),
          ("🏆", "Contest sponsorship", "Fund prizes and get branding on the contest, entries and winner announcements."),
          ("🎥", "Video sponsorship", "Integrated mention or dedicated walkthrough on our YouTube videos."),
          ("🎯", "Lead partnership", "Receive qualified, consented leads for virtual office, VoIP, payroll/EOR or staffing.")]
    cards = "".join(f'<div class="card reveal"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in pk)
    opts = "".join(f"<option>{t.replace('&amp;', '&')}</option>" for _, t, _ in pk)
    body = f'''<section style="padding-top:36px"><div class="container"><div class="grid g4">{cards}</div></div></section>
<section class="alt" id="partners"><div class="container lead-wrap">
<div><h2>Why 0Office.com</h2><ul class="ticks"><li>Audience of founders, freelancers and remote team leads actively setting up how they work</li><li>Contextual placements next to the exact task (invoicing, hiring, scheduling)</li><li>All sponsored content clearly labelled — trust is the product</li><li>Flexible: one-off tests, monthly packages or performance (CPL) deals</li></ul>
<div class="card" style="margin-top:18px"><h3>Interested in the domain itself?</h3><p style="margin-bottom:10px">For acquisition, joint-venture or strategic partnership on 0Office.com:</p><a class="btn btn-accent" href="{OWNER_URL}" target="_blank" rel="noopener">Contact the owner ↗</a></div></div>
<form class="form lead-card" data-form="Advertising / sponsorship inquiry" data-success="Thanks! We'll send our media kit and rates by email within 1 business day.">{honey()}
<h3>Request the media kit &amp; rates</h3>
<div class="form-row"><div><label for="a-name">Name</label><input id="a-name" name="name" required></div><div><label for="a-email">Work email</label><input id="a-email" type="email" name="email" required></div></div>
<div class="form-row"><div><label for="a-co">Company</label><input id="a-co" name="company" required></div><div><label for="a-web">Website</label><input id="a-web" name="website" placeholder="https://"></div></div>
<div><label for="a-pkg">Interested in</label><select id="a-pkg" name="package">{opts}<option>Domain / partnership</option><option>Not sure — advise me</option></select></div>
<div class="form-row"><div><label for="a-bud">Monthly budget</label><select id="a-bud" name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div><div><label for="a-start">Start</label><select id="a-start" name="start"><option>This month</option><option>Next month</option><option>This quarter</option></select></div></div>
<div><label for="a-goals">Goals</label><textarea id="a-goals" name="goals" rows="3"></textarea></div>
<button class="btn btn-primary" type="submit">Get media kit</button>{status()}</form></div></section>'''
    hero = page_hero(r, [("Advertise", "")], "Advertise, sponsor &amp; partner", "Reach people at the exact moment they're choosing how to run a business without an office.", eyebrow="Partners")
    return page("advertise.html", "Advertise & Sponsor on 0Office.com", "Advertising, sponsorship and lead partnership options on 0Office.com: tool sponsorships, newsletter, sponsored guides, directory listings, contests and video.", body, hero=hero, keywords="advertise sponsor media kit partnership")


ROLES = [("✍️", "Content writer (remote work, SaaS, HR)", "Freelance · per article"), ("🎬", "YouTube video editor / creator", "Freelance · per video"),
         ("💻", "Front-end developer (vanilla JS tools)", "Contract · per tool"), ("📈", "SEO specialist", "Part-time contract"),
         ("📣", "Community &amp; social media manager", "Part-time"), ("🤝", "Partnerships &amp; ad sales", "Commission-based")]


def careers():
    r = ""
    cards = "".join(f'<div class="card reveal"><div class="ico">{i}</div><h3>{t}</h3><p>{m} · 100% remote</p><a class="btn btn-ghost btn-sm" style="margin-top:12px" href="#apply">Apply</a></div>' for i, t, m in ROLES)
    opts = "".join(f"<option>{t.replace('&amp;', '&')}</option>" for _, t, _ in ROLES)
    body = f'''<section style="padding-top:36px"><div class="container"><div class="grid g3">{cards}</div></div></section>
<section class="alt" id="apply"><div class="container lead-wrap">
<div><h2>How we work</h2><ul class="ticks"><li>Fully remote, async-first — work from anywhere</li><li>Paid per deliverable or agreed rate, on time</li><li>Credit for your work (bylines, portfolio links)</li><li>Small team, real ownership</li></ul>
<p class="muted">Don't see your role? Apply anyway — tell us what you'd build.</p></div>
<form class="form lead-card" data-form="Job application" data-success="Application received ✓ — we review every one and reply within a week.">{honey()}
<div><label for="j-role">Role</label><select id="j-role" name="role">{opts}<option>Guest guide / contributor</option><option>Other</option></select></div>
<div class="form-row"><div><label for="j-name">Full name</label><input id="j-name" name="name" required></div><div><label for="j-email">Email</label><input id="j-email" type="email" name="email" required></div></div>
<div class="form-row"><div><label for="j-loc">Country / time zone</label><input id="j-loc" name="location" required></div><div><label for="j-avail">Availability</label><select id="j-avail" name="availability"><option>A few hours / week</option><option>10–20 h / week</option><option>20–40 h / week</option></select></div></div>
<div class="form-row"><div><label for="j-url">Portfolio / LinkedIn</label><input id="j-url" type="url" name="portfolio" required placeholder="https://"></div><div><label for="j-rate">Rate expectation</label><input id="j-rate" name="rate"></div></div>
<div><label for="j-why">Why you, in a few lines</label><textarea id="j-why" name="pitch" required rows="4"></textarea></div>
<button class="btn btn-primary" type="submit">Send application</button>{status()}</form></div></section>'''
    hero = page_hero(r, [("Work With Us", "")], "Work with 0Office.com", "We hire remote talent to build tools, write guides, produce videos and grow partnerships.", eyebrow="Careers")
    return page("careers.html", "Careers — Remote Jobs at 0Office.com", "Join 0Office.com remotely: content writers, video editors, front-end developers, SEO, community and partnership roles.", body, hero=hero, keywords="careers jobs hiring apply writer developer")


def about():
    r = ""
    body = f'''<section style="padding-top:36px"><div class="container prose">
<h2>Our mission</h2><p>Offices used to be the default cost of doing business. Today, most of what an office did can be bought by the hour, by the month or for free. 0Office.com exists to make that switch simple: free tools for everyday office jobs, honest guides, and a matching service that connects you with the right providers.</p>
<h2>What we believe</h2><ul><li><b>Free should be genuinely free.</b> Our tools need no signup and process your data in your browser.</li><li><b>Independence.</b> We recommend what fits your situation. Sponsored content is always labelled.</li><li><b>Practical over trendy.</b> Every guide should help you make a decision or finish a task.</li></ul>
<h2>How we make money</h2><p>Transparency matters, so here it is: we earn from advertising (including Google AdSense), sponsorships, affiliate links, referral fees from providers when readers request introductions, and reader donations. None of these change what our free tools do or cost.</p>
<h2>Editorial policy</h2><p>Guides are written or reviewed by people with hands-on remote-work experience, updated when things change, and corrected quickly when we get something wrong — <a href="contact.html">tell us</a>.</p>
<h2>Work with us</h2><p><a href="careers.html">Join the team</a>, <a href="advertise.html">advertise</a>, <a href="contests.html">enter a contest</a> or <a href="support.html">support the project</a>. For domain, sponsorship or partnership interest, use the <a href="{OWNER_URL}" target="_blank" rel="noopener">owner contact page</a>.</p></div></section>'''
    hero = page_hero(r, [("About", "")], "About 0Office.com", "An independent hub for running a business with zero office.", eyebrow="About")
    return page("about.html", "About 0Office.com", "About 0Office.com: an independent hub of free office tools, remote-work guides and matching services for office-free businesses.", body, hero=hero, keywords="about mission")


def contact():
    r = ""
    body = f'''<section style="padding-top:36px"><div class="container lead-wrap">
<div><h2>Get in touch</h2><p class="muted">We reply to every message, usually within one business day.</p>
<div class="card" style="margin:14px 0"><h3>📧 Email</h3><p style="margin-bottom:10px">Prefer your own mail app?</p><a class="btn btn-ghost btn-sm" href="#" data-mail="Hello from 0Office.com">Email us</a></div>
<div class="card" style="margin:14px 0"><h3>🤝 Domain, sponsorship &amp; partnership</h3><p style="margin-bottom:10px">Interested in this website or the 0Office.com domain?</p><a class="btn btn-accent btn-sm" href="{OWNER_URL}" target="_blank" rel="noopener">Owner contact ↗</a></div>
<div class="card"><h3>⚡ Quick links</h3><p><a href="get-started.html">Free Zero-Office plan</a> · <a href="advertise.html">Advertise</a> · <a href="hire.html">Hire talent</a> · <a href="careers.html">Careers</a></p></div></div>
<form class="form lead-card" data-form="Contact message" data-success="Message sent ✓ — we'll reply by email soon.">{honey()}
<div><label for="ct-topic">Topic</label><select id="ct-topic" name="topic"><option>General question</option><option>Tool request</option><option>Bug report</option><option>Partnership</option><option>Advertising / sponsorship</option><option>Press</option><option>Domain / website acquisition</option><option>Privacy request</option></select></div>
<div class="form-row"><div><label for="ct-name">Name</label><input id="ct-name" name="name" required autocomplete="name"></div><div><label for="ct-email">Email</label><input id="ct-email" type="email" name="email" required autocomplete="email"></div></div>
<div><label for="ct-msg">Message</label><textarea id="ct-msg" name="message" required rows="6"></textarea></div>
<button class="btn btn-primary" type="submit">Send message</button>{status()}</form></div></section>
<script>(function(){{var t=new URLSearchParams(location.search).get("topic");if(t){{var s=document.getElementById("ct-topic");var o=document.createElement("option");o.text=t;o.selected=true;s.add(o,0);}}}})();</script>'''
    hero = page_hero(r, [("Contact", "")], "Contact us", "Questions, ideas, partnerships or bug reports — we'd love to hear from you.", eyebrow="Contact")
    return page("contact.html", "Contact 0Office.com", "Contact 0Office.com for questions, tool requests, partnerships, advertising, press or privacy requests.", body, hero=hero, keywords="contact email support")


def legal(path, title, lead, html_body, kw):
    hero = page_hero("", [(title, "")], title, lead, eyebrow="Legal")
    return page(path, title, lead, f'<section style="padding-top:36px"><div class="container prose">{html_body}</div></section>', hero=hero, keywords=kw)


def privacy():
    return legal("privacy.html", "Privacy & Cookie Policy", "How 0Office.com collects, uses and protects information. Last updated: September 28, 2026.", f'''
<h2>Summary</h2><ul><li>Our tools run in your browser; what you type into them is not sent to us.</li><li>When you submit a form, we receive what you entered so we can respond.</li><li>With your consent, we use analytics and advertising cookies to keep the site free.</li></ul>
<h2>Information we collect</h2><p><b>Form submissions:</b> name, email, and anything else you choose to enter (for example on the Zero-Office plan, hire, contest, careers, donation-pledge or contact forms). Forms are delivered to us by a third-party form-processing service (FormSubmit), which processes the data on our behalf.</p>
<p><b>Local storage:</b> some tools (e.g. invoice drafts, notes, theme preference) save data in your browser's local storage on your device only. You can clear it at any time through your browser settings.</p>
<p><b>Automatically collected data:</b> if you accept analytics cookies, Google Analytics may collect usage data such as pages visited, device and approximate location.</p>
<h2 id="cookies">Cookies and advertising</h2><p>We may use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on visits to this and other sites. You may opt out of personalised advertising by visiting <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>. Learn more in <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses information from sites that use its services</a>.</p>
<p>You can change your choice by clearing this site's storage in your browser; the consent banner will reappear.</p>
<h2>How we use information</h2><ul><li>To reply to you and deliver what you requested (plans, media kits, newsletters).</li><li>With your explicit consent on the relevant form, to introduce you to up to three relevant providers or talent partners.</li><li>To improve the site and prevent spam and abuse.</li></ul><p>We do not sell personal information to data brokers or mailing lists.</p>
<h2>Retention</h2><p>We keep submissions only as long as needed for the purpose you submitted them for, or as required by law.</p>
<h2>Your rights</h2><p>Depending on where you live (for example under the GDPR, UK GDPR, Canada's PIPEDA and Québec's Law 25, or California's CCPA/CPRA), you may have rights to access, correct, delete or port your data, and to withdraw consent or opt out of certain processing. To make a request, use our <a href="contact.html?topic=Privacy%20request">contact form</a>.</p>
<h2>Children</h2><p>This site is not directed to children under 16 and we do not knowingly collect their data.</p>
<h2>Changes</h2><p>We will post any changes on this page with a new “last updated” date.</p>''', "privacy cookies gdpr")


def terms():
    return legal("terms.html", "Terms of Use", "Rules for using 0Office.com. Last updated: September 28, 2026.", '''
<h2>Acceptance</h2><p>By using 0Office.com you agree to these terms. If you don't agree, please don't use the site.</p>
<h2>Free tools — provided “as is”</h2><p>Our tools and calculators are provided free, “as is” and without warranties of any kind. Results are estimates for general information. You are responsible for checking any figures, invoices or documents before relying on them.</p>
<h2>Not professional advice</h2><p>Content on this site is general information, not legal, tax, financial, employment or other professional advice. Consult a qualified professional for your situation.</p>
<h2>Third-party services and links</h2><p>We link to and may introduce you to third-party providers. We don't control them and aren't responsible for their products, services, pricing or policies. Any agreement you make is between you and that provider.</p>
<h2>User submissions</h2><p>When you submit content (e.g. contest entries, guide pitches, messages), you confirm you have the right to share it and grant 0Office.com a non-exclusive, worldwide, royalty-free licence to use, display and adapt it for operating and promoting the site, with credit where appropriate. Don't submit anything unlawful, infringing or confidential.</p>
<h2>Contests</h2><p>Each contest round is governed by its published rules and prize list, which prevail over these terms for that contest.</p>
<h2>Donations</h2><p>Donations are voluntary, generally non-refundable, and not tax-deductible. Payments are processed by third-party payment providers under their terms.</p>
<h2>Intellectual property</h2><p>The site's original text, design, graphics and code are © 0Office.com and protected by copyright. You may not copy or republish substantial parts without permission. Third-party trademarks belong to their owners — see our <a href="disclaimer.html">Disclaimer &amp; Trademarks</a>.</p>
<h2>Limitation of liability</h2><p>To the maximum extent permitted by law, 0Office.com is not liable for any indirect, incidental or consequential damages arising from your use of the site or tools.</p>
<h2>Changes</h2><p>We may update these terms; continued use means you accept the updated version.</p>''', "terms conditions rules")


def disclaimer():
    return legal("disclaimer.html", "Disclaimer, Trademark & Copyright Notice", "Independence, trademark, copyright, affiliate and advertising disclosures.", f'''
<h2>Trademark disclosure</h2><p><b>0Office.com is an independent website.</b> It is not affiliated with, associated with, authorised by, endorsed by, or in any way officially connected with Microsoft Corporation (including Microsoft Office and Microsoft 365), Ascensio System SIA (ONLYOFFICE), The Document Foundation (LibreOffice / OpenOffice-derived projects), Kingsoft Office Software (WPS Office), Google LLC (Google Workspace), Zoho Corporation, or any other company, product or service mentioned on this site.</p>
<p>“0Office” is used as the name of this website and its domain, describing the concept of working with <em>zero office</em>. No claim is made to any registered trademark rights in the word “Office” or in any third-party mark, and the name is not intended to suggest any connection with office-software brands. All product and company names, logos and brands mentioned on this site are trademarks™ or registered® trademarks of their respective holders and are used for identification and descriptive purposes only (nominative use). Their use does not imply endorsement.</p>
<p>If you believe any content on this site infringes your trademark, please <a href="contact.html">contact us</a> and we will review it promptly.</p>
<h2>Copyright notice</h2><p>© {2026} 0Office.com. All rights reserved. Original text, tool code, graphics and site design are protected by copyright. Third-party logos are not reproduced on this site. Videos embedded from YouTube remain the property of their creators and are shown under YouTube's embedding terms.</p>
<p><b>Copyright complaints:</b> if you believe material on this site infringes your copyright, send a notice via our <a href="contact.html?topic=Copyright%20notice">contact form</a> including: identification of the work, the URL of the material, your contact details, a good-faith statement, and a statement that the information is accurate and you are authorised to act. We will respond and remove infringing material where appropriate.</p>
<h2>Affiliate &amp; referral disclosure</h2><p>Some links on 0Office.com may be affiliate links, and we may receive referral fees when readers request introductions to providers. This comes at no extra cost to you and does not affect our free tools. Sponsored placements are labelled “Sponsored” or “Featured”.</p>
<h2>Advertising disclosure</h2><p>This site may display ads served by Google AdSense and other networks, and direct-sold sponsorships. Advertisers do not control our editorial content.</p>
<h2>General disclaimer</h2><p>All content is for general information only and is not professional advice. Calculators provide estimates. We make no guarantees about the accuracy, completeness or availability of third-party services listed.</p>''', "disclaimer trademark copyright affiliate disclosure")


def notfound(BASE):
    body = f'''<section><div class="container center"><h1>404 — zero pages found here</h1><p class="muted">That page doesn't exist (maybe it went remote?).</p><p><a class="btn btn-primary" href="{BASE}index.html">Go home</a> <a class="btn btn-ghost" href="{BASE}tools/index.html">Free tools</a></p></div></section>'''
    return page("404.html", "Page not found", "Page not found.", body, index=False, root_override=BASE)
