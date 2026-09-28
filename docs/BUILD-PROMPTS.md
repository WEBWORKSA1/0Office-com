# 0Office.com — Concept & Phase-wise Build Prompts

## 1. The winning idea

**0Office = "Zero Office": the hub for running a business without an office.**

| Pillar | What it is | Why it earns |
|---|---|---|
| Free browser office tools | Invoice generator, meeting cost calculator, time-zone planner, pomodoro, word counter, salary / freelance-rate / savings / business-days calculators, password & email-signature generators, notes | Evergreen, high-volume search traffic ("invoice generator", "time zone converter", "word counter") → AdSense page views. Tools are sticky and bookmarkable. |
| Zero-Office plan (lead gen) | 3-step form: needs → team/city/budget → contact + consent | Virtual office, VoIP, EOR/payroll, staffing and formation providers pay per lead / per referral. These B2B verticals often command high CPL/CPC. |
| Remote talent marketplace (two-sided) | "Hire talent" requests + "join talent network" | Staffing referral fees; later paid job posts. |
| Remote Stack directory + guides | Categorised SaaS directory, pillar guides | Affiliate commissions from SaaS; sponsored/featured listings; SEO authority. |
| Community | Contests, videos, newsletter | Sponsor inventory, YouTube revenue, owned audience. |
| Support | Donations/pledges, sponsorship, advertising, domain/partnership inquiries | Direct revenue and exit options. |

**Why this beats the alternatives:** a pure "free office suite" (competing with Google/Microsoft) needs a backend and heavy engineering; a pure remote-job board is saturated. The tool + lead-gen hybrid runs on static hosting at $0, monetizes the traffic three ways (ads, affiliate, leads), and matches the domain meaning exactly.

**Revenue stack (ordered by expected impact at scale):** 1) lead partnerships (virtual office / EOR / staffing), 2) AdSense on tool pages, 3) SaaS affiliates, 4) direct sponsorships (tools, newsletter, contests, video), 5) YouTube, 6) donations.

## 2. Research basis

The build draws on patterns observed across 44 sites in the remote-jobs, global-payroll, coworking/virtual-office, free-tools and software-directory niches. See `docs/RESEARCH.md`.

---

## 3. Phase-wise prompts

Each prompt is self-contained. Run them in order with an AI coding assistant. Shared constraints to paste at the top of every phase:

> **Global constraints:** Static site only (HTML/CSS/vanilla JS) so it runs on the free GitHub Pages plan. Relative links everywhere. Mobile-first, responsive, light/dark mode, WCAG AA contrast, no horizontal scroll at 360px. On top of every page show the bar: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership" linking to https://web.works/contact. All forms submit via AJAX to FormSubmit; the owner's email must never appear as text anywhere in the source or UI: store it encoded in `assets/js/config.js` and assemble it only at send time, or use a FormSubmit alias. "Email us" links build the mailto on click. No trademark claims on "0Office"; include an independence/trademark disclaimer (not affiliated with Microsoft Office/365, ONLYOFFICE, LibreOffice, WPS, Google, Zoho). All original content, © 0Office.com.

### Phase 1 — Foundation & design system
> Create the repo structure: `assets/css/style.css`, `assets/js/{config,app,tools}.js`, `assets/img/logo.svg`, `src/` (Python generator) and `build.py` that renders every page from one shared layout (top interest bar, sticky header with nav, search button, theme toggle, mobile menu; footer with 5 columns, trademark notice, copyright). Design tokens: teal brand (#0d9488), indigo accent, navy footer, Inter font, 16px radius cards, soft shadows. Components: buttons, chips, cards, stats, forms, choice tiles, progress bar, tiers, CTA band, FAQ accordion, ad slots, toast, cookie banner, search modal (Ctrl/Cmd+K). Add `robots.txt`, `sitemap.xml`, `manifest.webmanifest`, `.nojekyll`, `ads.txt`, `404.html`, OG image, JSON-LD (WebSite, Organization, FAQPage, WebApplication, Article).

### Phase 2 — Free tools (traffic engine)
> Build 12 client-side tools, each on its own SEO page with: H1, live tool, in-content ad, "How to use" steps, FAQ with FAQPage schema, sidebar (lead CTA, ad, related tools, "sponsor this tool"), newsletter band. Tools: invoice generator (line items, tax, discount, shipping, paid, currency, autosave, print-to-PDF), meeting cost calculator (live meter), time-zone planner (overlap grid, DST-aware via Intl, shareable URL), pomodoro (tasks, custom intervals, notifications), word counter (keyword density, readability, case converter), salary converter, remote-work savings calculator, freelance rate calculator, business-days calculator, password generator (Web Crypto), email signature generator (copy rich HTML), quick notes (local storage, .txt/.md download). No data leaves the browser.

### Phase 3 — Lead generation (money engine)
> Build `get-started.html` and embed the same 3-step form on the home page. Step 1 multi-select needs (virtual office, coworking, VoIP, payroll/EOR, talent, formation, IT setup, consulting); step 2 team size, timeline, city, country, budget; step 3 name, work email, phone, company, notes, explicit consent to share with up to 3 vetted providers. Progress bar, per-step validation, `?need=` pre-selection from intent chips, honeypot, success message, GA4 `generate_lead` event. Add lead magnet `checklist.html` (printable checklist + "email me the template pack" form). Add partner CTA for providers who want leads.

### Phase 4 — Content & directory (SEO + affiliate)
> Write 6 original pillar/cluster guides (Zero-Office Playbook, virtual office vs coworking vs home, business address without an office, real cost of meetings, hiring first remote employee, minimum viable remote stack) with Article schema, inline ads after the 3rd H2, internal links to tools and the lead form. Build `stack.html`: 12 categories of well-known remote-work tools with `data-aff` slugs so affiliate URLs can be swapped in from config, plus clear affiliate disclosure.

### Phase 5 — Community, talent & video
> `hire.html` (company talent request + professional talent-network signup), `careers.html` (open remote roles + application form), `contests.html` (3 contests, entry form, rules summary, sponsor-a-prize CTA), `videos.html` (YouTube grid from config video IDs with click-to-load privacy-enhanced embeds; topic fallback cards; video sponsorship/pitch form).

### Phase 6 — Monetization & support
> `advertise.html` (8 packages incl. tool sponsorship, newsletter, sponsored guide, featured listing, contest, video, lead partnership; media-kit request form; domain/partnership link). `support.html` (donation tiers, provider buttons driven by config — PayPal, Stripe Payment Link, Buy Me a Coffee, Ko-fi, GitHub Sponsors — pledge form fallback, planned allocation bars for operations, promotion/marketing, hiring talent, contests/prizes). AdSense loader that activates only when `adsenseClient` is set; otherwise slots show house ads for "Advertise here". Cookie consent that gates analytics and personalised ads.

### Phase 7 — Trust & legal
> `about.html` (mission, "how we make money" transparency, editorial policy), `contact.html` (topic-routed form + hidden-email link + owner link), `privacy.html` (FormSubmit processor, local storage, Google AdSense cookie language + opt-out links, GDPR/PIPEDA/Law 25/CCPA rights), `terms.html`, `disclaimer.html` (trademark disclosure, copyright notice + takedown process, affiliate & advertising disclosure).

### Phase 8 — QA & launch
> Automated Playwright checks for every page: no JS errors, top bar present and linking to web.works/contact, owner email never present in HTML, no horizontal overflow at 390px; functional tests for each tool and a full lead-form submission with FormSubmit mocked. Push to GitHub `WEBWORKSA1/0Office-com` and publish on GitHub Pages (free plan, public repo, deploy from branch).

### Phase 9 — Growth (post-launch)
> 1) Apply for AdSense after ~20–30 indexed pages and some traffic; add `ads.txt` line. 2) Submit sitemap to Google Search Console and Bing. 3) Activate FormSubmit (first submission sends an activation email) and switch to the alias. 4) Add 2 guides and 1 tool per month; build "X vs Y" comparison pages and city landing pages only when they contain real, unique data. 5) Sign affiliate programs (payroll/EOR, VoIP, virtual mailbox, SaaS) and set `affiliates` in config. 6) Recruit 3–5 lead buyers per vertical. 7) Launch a YouTube channel with tool walkthroughs and embed the IDs. 8) Point 0office.com DNS to GitHub Pages and add a CNAME.

## 4. Configuration checklist (`assets/js/config.js`)

- `adsenseClient`, `adSlots` — AdSense publisher & slot IDs
- `ga4` — Google Analytics 4 ID
- `formAlias` — FormSubmit random alias (after activation)
- `donate.*` — PayPal / Stripe / BMAC / Ko-fi / GitHub Sponsors URLs
- `youtubeChannel`, `videos[]` — channel URL and video IDs
- `affiliates{}` — slug → tracked URL for the stack directory
