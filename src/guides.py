"""Long-form guides (original content)."""
from layout import page, page_hero, ad, newsletter

GUIDES = [
dict(slug="zero-office-playbook", title="The Zero-Office Playbook: How to Run a Business Without an Office", cat="Pillar guide", mins=9,
 desc="A complete, practical framework for running a company with no lease: address, phone, money, people, tools and culture.",
 body='''<p>An office used to solve six problems at once: it gave your business an <b>address</b>, a <b>phone line</b>, a place to <b>meet clients</b>, a place for <b>people to work together</b>, a home for <b>equipment and records</b>, and a visible signal that you were <b>legitimate</b>. Going “zero-office” simply means solving each of those problems separately, with the cheapest tool that does the job well.</p>
<p>This playbook walks through each layer in the order most businesses should tackle it.</p>
<h2 id="address">1. Get a business address that isn’t your home</h2>
<p>You’ll need an address for company registration, invoices, bank accounts, your website footer and possibly your listing on maps. Options, from lightest to heaviest:</p>
<ul><li><b>Virtual mailbox</b> — a real street address with mail scanning and forwarding. Best for solo founders and online businesses.</li>
<li><b>Virtual office</b> — address plus extras such as a receptionist, meeting-room credits and sometimes a local phone number.</li>
<li><b>Registered agent service</b> — required in some jurisdictions to receive legal notices; often bundled with formation services.</li></ul>
<p>Check local rules before you buy: some registries, banks and map listings do not accept certain virtual addresses. See our guide to <a href="business-address-without-office.html">getting a business address without an office</a>.</p>
<h2 id="phone">2. Separate your business phone</h2>
<p>A cloud phone system (VoIP) gives you a business number that rings on your mobile and laptop, with voicemail-to-email, business hours and call routing. It keeps your personal number private and lets you add teammates later without new hardware.</p>
<h2 id="money">3. Set up money flows that don’t need a desk</h2>
<ul><li>A business bank account with strong online and mobile access.</li>
<li>Invoicing and accounting software — or start with our <a href="../tools/invoice-generator.html">free invoice generator</a>.</li>
<li>If you pay people in other countries, decide early between contractors, an Employer of Record (EOR), or your own local entity. We cover the trade-offs in <a href="hire-first-remote-employee.html">hiring your first remote employee</a>.</li></ul>
<h2 id="meet">4. Meet people without owning the room</h2>
<p>Book meeting rooms or day passes by the hour through coworking networks when you need a physical space. For most recurring meetings, a good video setup and a written agenda beat a room.</p>
<h2 id="people">5. Design how the team works — on purpose</h2>
<p>Offices create coordination by accident: you overhear things. Remote teams need to create it deliberately:</p>
<ul><li><b>Write things down.</b> Decisions, processes and project status belong in a shared, searchable place.</li>
<li><b>Default to async.</b> Use meetings for decisions and relationships, not status updates. Our <a href="../tools/meeting-cost-calculator.html">meeting cost calculator</a> makes the trade-off visible.</li>
<li><b>Protect overlap hours.</b> Agree on a few shared hours across time zones — find them with the <a href="../tools/time-zone-planner.html">time zone planner</a>.</li></ul>
<h2 id="tools">6. Choose a minimum viable tool stack</h2>
<p>You need far fewer tools than vendors suggest: communication, documents, tasks, files, passwords and money. We list sensible options in the <a href="../stack.html">Remote Stack directory</a> and the <a href="minimum-viable-remote-stack.html">minimum viable stack guide</a>.</p>
<h2 id="security">7. Secure it like there’s no IT room</h2>
<ul><li>Use a password manager and turn on two-factor authentication everywhere.</li><li>Encrypt laptops and enable remote wipe.</li><li>Keep company files in company-owned accounts, not personal drives.</li></ul>
<h2 id="culture">8. Keep the human side</h2>
<p>Budget for occasional in-person meetups, celebrate wins publicly, and give people clear working-hours norms so “remote” doesn’t become “always on.”</p>
<blockquote>Rule of thumb: rent space by the hour, not by the year — until the hours add up to more than a lease.</blockquote>
<h2 id="next">Your next step</h2>
<p>Work through our printable <a href="../checklist.html">Zero-Office Launch Checklist</a>, or <a href="../get-started.html">request a free personalised plan</a> and we’ll match you with address, phone, payroll and talent options for your city and budget.</p>'''),
dict(slug="virtual-office-vs-coworking-vs-home", title="Virtual Office vs Coworking vs Home Office: Which Setup Fits Your Stage?", cat="Comparison", mins=7,
 desc="A clear comparison of virtual offices, coworking and home offices — cost drivers, pros, cons and a decision tree.",
 body='''<p>These three options are often compared as if they compete. In practice most office-free businesses combine them. The real question is which one should be your <em>default</em> and which you should buy only when needed.</p>
<h2>At a glance</h2>
<div class="table-wrap"><table><thead><tr><th></th><th>Home office</th><th>Virtual office</th><th>Coworking</th></tr></thead><tbody>
<tr><td><b>Main job</b></td><td>Daily workspace</td><td>Address, mail, image</td><td>Workspace + community</td></tr>
<tr><td><b>Cost driver</b></td><td>Setup + utilities</td><td>Monthly plan + add-ons</td><td>Per desk / per day</td></tr>
<tr><td><b>Privacy of your home</b></td><td>Low (if address used)</td><td>High</td><td>High</td></tr>
<tr><td><b>Client meetings</b></td><td>Video only</td><td>Room credits (often)</td><td>Yes</td></tr>
<tr><td><b>Flexibility</b></td><td>Highest</td><td>High (monthly)</td><td>Medium–high</td></tr></tbody></table></div>
<h2>Home office: the default for most</h2>
<p>If you can work productively at home, it’s the cheapest daily workspace. Invest in a proper chair, a large monitor, decent lighting, a good microphone and reliable internet. The main downsides are isolation, blurred work–life boundaries and the privacy cost of putting your home address on public records — which is exactly what a virtual office fixes.</p>
<h2>Virtual office: the professional layer</h2>
<p>A virtual office gives you a business address in a chosen city, mail handling and usually access to meeting rooms. It’s ideal when you need a credible address for registration, invoices and your website — or a presence in a city where you don’t live.</p>
<h2>Coworking: buy it by the day</h2>
<p>Coworking makes sense for focus days away from home, workshops, team meetups and client meetings. Many networks sell day passes and hourly rooms, so you only pay for what you use.</p>
<h2>A simple decision tree</h2>
<ol><li><b>Do you need an address that isn’t your home?</b> Yes → virtual mailbox or virtual office.</li>
<li><b>Can you focus at home most days?</b> Yes → home office default. No → coworking membership.</li>
<li><b>Do you meet clients or the team in person monthly?</b> Yes → add day passes / meeting-room credits.</li>
<li><b>Are you paying for more than ~8–10 coworking days per month?</b> Price a dedicated desk.</li></ol>
<p>Want us to price the combination for your city? <a href="../get-started.html?need=virtual-office">Get a free Zero-Office plan</a>.</p>'''),
dict(slug="business-address-without-office", title="How to Get a Business Address Without Renting an Office", cat="How-to", mins=6,
 desc="Virtual mailboxes, virtual offices and registered agents explained — plus what to check before you buy.",
 body='''<p>Putting your home address on a company registry, invoices and your website exposes it permanently. Here’s how to get a professional address without signing a lease.</p>
<h2>Your three options</h2>
<h3>1. Virtual mailbox</h3><p>A real street address at a mail-handling location. Mail is received, the envelope is scanned, and you choose to open-and-scan, forward, shred or hold it — all from an app. Best for solo founders, e-commerce and online services.</p>
<h3>2. Virtual office</h3><p>Everything a mailbox does, usually at a business centre, plus optional services: a receptionist or call answering, a local phone number, and meeting-room or day-office credits. Best when you want to meet clients at “your” address occasionally.</p>
<h3>3. Registered agent / registered office service</h3><p>Many jurisdictions require a registered address to receive official and legal documents. Formation services often bundle this. It may not include general mail handling, so check.</p>
<h2>Checklist before you buy</h2>
<ul><li><b>Is it a real street address</b> (not a P.O. box)? Many registries and banks require one.</li>
<li><b>Is it accepted where you need it?</b> Company registry, your bank, payment processors and map listings each have their own rules. Map listings in particular can be strict about virtual addresses.</li>
<li><b>What does “per item” cost?</b> Scans, forwarding and package handling are often billed separately.</li>
<li><b>Identity verification.</b> In some countries (for example, the U.S. with USPS Form 1583) you must verify identity and authorise the provider to receive mail for you.</li>
<li><b>Contract terms.</b> Monthly vs annual, cancellation notice, and what happens to mail after you leave.</li>
<li><b>Suite number format.</b> Some providers use a suite or unit number; make sure it’s usable in your paperwork.</li></ul>
<h2>Which should you choose?</h2>
<p>Start with a virtual mailbox if you just need an address and mail. Upgrade to a virtual office when you need a receptionist, a local number or rooms. Add a registered agent if your jurisdiction requires one and your mailbox provider doesn’t act as one.</p>
<p><a href="../get-started.html?need=virtual-office">Tell us your city</a> and we’ll send matched address options — free.</p>
<p class="muted"><small>This article is general information, not legal advice. Requirements vary by jurisdiction.</small></p>'''),
dict(slug="real-cost-of-meetings", title="The Real Cost of Meetings (and How Remote Teams Cut Them)", cat="Productivity", mins=6,
 desc="How to calculate what meetings cost and the async habits that replace most of them.",
 body='''<p>Meetings feel free because nobody gets an invoice. But every attendee is paid for that hour, and the work they would otherwise do doesn’t happen. Putting a number on it changes behaviour fast.</p>
<h2>The formula</h2>
<p><b>Meeting cost = attendees × hourly cost × duration</b>, where hourly cost = annual salary ÷ paid hours (about 2,080 for full-time) × (1 + overhead). Overhead for benefits, taxes and equipment is often estimated at 20–40%.</p>
<p>Example: 8 people averaging 90,000 a year, 30% overhead, 1 hour → 8 × (90,000 ÷ 2,080) × 1.3 ≈ <b>450 per meeting</b>. Weekly for 48 weeks ≈ <b>21,600 a year</b> — for one recurring meeting. Try your own numbers in the <a href="../tools/meeting-cost-calculator.html">meeting cost calculator</a>.</p>
<h2>What to replace with async</h2>
<ul><li><b>Status updates</b> → a short written update in a shared channel or doc, same time each week.</li>
<li><b>Demos</b> → a 3-minute screen recording people watch at 1.5× when it suits them.</li>
<li><b>Brainstorms</b> → a shared doc open for 48 hours, then a short meeting only to decide.</li>
<li><b>FYI announcements</b> → written posts with a clear “action needed / no action needed” label.</li></ul>
<h2>Meetings that are worth it</h2>
<ul><li>Decisions with real disagreement.</li><li>Sensitive conversations: feedback, conflict, bad news.</li><li>Relationship-building, especially for new teammates.</li><li>Kick-offs where alignment early saves weeks later.</li></ul>
<h2>Rules that stick</h2>
<ol><li>No agenda, no meeting.</li><li>Default to 25 or 50 minutes, not 30 or 60.</li><li>Invite decision-makers; send notes to everyone else.</li><li>End with owners and deadlines written down.</li><li>Review recurring meetings every quarter — cancel one by default.</li></ol>
<p>For distributed teams, schedule within shared hours using the <a href="../tools/time-zone-planner.html">time zone planner</a> so nobody always takes the 7 a.m. slot.</p>'''),
dict(slug="hire-first-remote-employee", title="Hiring Your First Remote Employee or Contractor: A Step-by-Step Checklist", cat="Hiring", mins=8,
 desc="Contractor vs employee vs Employer of Record, how to write the role, where to find talent, and onboarding remotely.",
 body='''<p>Your first remote hire shapes how your company works for years. This checklist covers the decisions in order.</p>
<h2>Step 1 — Define the outcome, not the job title</h2>
<p>Write down what success looks like after 90 days, in measurable terms. “Publish 8 SEO articles a month that rank” is hireable; “marketing person” is not.</p>
<h2>Step 2 — Choose the engagement model</h2>
<div class="table-wrap"><table><thead><tr><th>Model</th><th>Good for</th><th>Watch out for</th></tr></thead><tbody>
<tr><td><b>Freelancer / contractor</b></td><td>Defined projects, part-time, testing fit</td><td>Misclassification risk if you control them like an employee</td></tr>
<tr><td><b>Employer of Record (EOR)</b></td><td>Full-time hires in countries where you have no entity</td><td>Monthly per-employee fee; you still manage the work</td></tr>
<tr><td><b>Your own entity</b></td><td>Many hires in one country</td><td>Setup and ongoing compliance cost</td></tr></tbody></table></div>
<p>Employment rules differ by country. When the role is long-term, full-time and closely directed, get local advice before choosing “contractor”.</p>
<h2>Step 3 — Write a remote-ready job post</h2>
<ul><li>Time zone overlap required (e.g. “4 hours overlap with 9–5 ET”).</li><li>Salary or rate range — posts with ranges typically attract more qualified applicants.</li><li>How the team works: async tools, meeting load, response-time expectations.</li><li>A small, paid work sample as part of the process.</li></ul>
<h2>Step 4 — Source candidates</h2>
<p>Use a mix of remote job boards, your network, communities in the role’s niche and specialist talent partners. <a href="../hire.html">Tell us what you need</a> and we’ll connect you with vetted remote talent or staffing partners.</p>
<h2>Step 5 — Interview for remote skills</h2>
<ul><li>Clear written communication (review their written answers carefully).</li><li>Self-management: ask how they plan a week with no manager online.</li><li>Proactiveness: how they flag blockers.</li></ul>
<h2>Step 6 — Pay and paperwork</h2>
<p>Agree on currency, invoicing schedule, IP assignment, confidentiality and termination terms in writing. The <a href="../tools/salary-converter.html">salary converter</a> helps compare hourly and annual offers.</p>
<h2>Step 7 — Onboard like it’s a product launch</h2>
<ol><li>Accounts, laptop and password manager ready on day one.</li><li>A written 30-60-90 day plan.</li><li>A buddy who isn’t their manager.</li><li>Daily check-ins in week one, then taper.</li></ol>
<p class="muted"><small>General information only — not legal, tax or employment advice.</small></p>'''),
dict(slug="minimum-viable-remote-stack", title="The Minimum Viable Remote Tech Stack", cat="Tools", mins=6,
 desc="The seven tool categories every office-free business needs — and the ones you can skip.",
 body='''<p>Tool sprawl is the hidden tax of remote work: more subscriptions, more logins, more places to look. Start with the minimum, then add only when a real problem appears.</p>
<h2>The 7 essentials</h2>
<ol><li><b>Chat</b> — one place for quick questions and announcements. Keep channels few and named clearly.</li>
<li><b>Video</b> — reliable calls with screen sharing and recording.</li>
<li><b>Docs &amp; files</b> — an office suite with shared drives owned by the company, not individuals.</li>
<li><b>Tasks / projects</b> — who is doing what by when. Simple boards are enough early on.</li>
<li><b>Password manager</b> — shared vaults for team credentials, two-factor everywhere.</li>
<li><b>Money</b> — invoicing, accounting and payroll/contractor payments.</li>
<li><b>Knowledge base</b> — a handbook: how we work, policies, processes. Often just a folder of docs at first.</li></ol>
<h2>Nice-to-haves (add when needed)</h2>
<ul><li>Async screen recording for demos and feedback.</li><li>Time tracking if you bill hourly.</li><li>E-signatures for contracts.</li><li>A cloud phone system once clients call you.</li><li>CRM once you have a repeatable sales process.</li></ul>
<h2>Three rules to avoid sprawl</h2>
<ol><li><b>One tool per job.</b> Two chat apps means half your messages are in the wrong one.</li><li><b>Company-owned accounts.</b> Use your business domain for sign-ups so access survives staff changes.</li><li><b>Quarterly audit.</b> Cancel anything nobody opened in 30 days.</li></ol>
<p>Browse options by category in our <a href="../stack.html">Remote Stack directory</a>, and use our <a href="../tools/index.html">free tools</a> for the jobs that don’t deserve a subscription.</p>'''),
]


def guide_page(g):
    root = "../"
    others = [x for x in GUIDES if x["slug"] != g["slug"]][:3]
    more = "".join(f'<a class="card" href="{x["slug"]}.html"><span class="tag">{x["cat"]}</span><h3>{x["title"]}</h3><p>{x["desc"]}</p></a>' for x in others)
    schema = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
              "author": {"@type": "Organization", "name": "0Office.com Editorial"}, "publisher": {"@type": "Organization", "name": "0Office.com"},
              "datePublished": "2026-09-28", "dateModified": "2026-09-28"}
    # insert an ad after the 3rd h2
    parts = g["body"].split("<h2", 3)
    body_html = g["body"] if len(parts) < 4 else "<h2".join(parts[:3]) + ad("inContent") + "<h2" + parts[3]
    body = f'''<section style="padding-top:36px"><div class="container"><article class="prose">
<div class="meta"><span>By 0Office.com Editorial</span><span>{g["mins"]} min read</span><span>Updated Sep 2026</span></div>
{body_html}
<div class="card" style="margin-top:36px;border:2px solid var(--brand)"><h3>Get a free Zero-Office plan</h3><p style="margin-bottom:12px">Tell us your city, team size and needs. We’ll send matched options for address, phone, payroll and talent — free, no obligation.</p><a class="btn btn-primary" href="../get-started.html">Start in 60 seconds →</a></div>
</article></div></section>
{ad("footer")}
<section class="alt"><div class="container"><h2 class="center">Keep reading</h2><div class="grid g3">{more}</div></div></section>
{newsletter(root)}'''
    hero = page_hero(root, [("Guides", "guides/index.html"), (g["cat"], "")], g["title"], g["desc"], eyebrow=g["cat"])
    return page(f'guides/{g["slug"]}.html', g["title"], g["desc"], body, active="guides", schema=[schema], hero=hero, keywords=g["cat"])


def guides_index():
    root = "../"
    cards = "".join(f'<a class="card reveal" href="{g["slug"]}.html"><span class="tag">{g["cat"]}</span><h3>{g["title"]}</h3><p>{g["desc"]}</p><p style="margin-top:10px"><small>{g["mins"]} min read</small></p></a>' for g in GUIDES)
    body = f'''<section style="padding-top:36px"><div class="container"><div class="grid g3">{cards}</div></div></section>
{ad("inContent")}
<section class="alt"><div class="container center"><h2>Write for 0Office.com</h2><p class="muted">Experienced remote operator, founder or HR lead? We publish practical, original guides — with credit and a link.</p><a class="btn btn-primary" href="../careers.html#apply">Pitch a guide</a></div></section>
{newsletter(root)}'''
    hero = page_hero(root, [("Guides", "")], "Zero-Office guides", "Practical, no-fluff playbooks for running a business without an office — addresses, hiring, meetings, tools and more.", eyebrow="Learn")
    return page("guides/index.html", "Remote Work & Zero-Office Guides", "Practical guides for running an office-free business: virtual offices, coworking, remote hiring, meeting costs and tool stacks.", body, active="guides", hero=hero, keywords="guides articles blog")
