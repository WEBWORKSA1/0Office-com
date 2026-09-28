# 0Office.com — Run your business with zero office

Static, responsive website: 12 free in-browser office tools, remote-work guides, a multi-step lead-generation funnel, talent marketplace, contests, videos, donations, and advertising/sponsorship pages. It is hosted free on GitHub Pages.

**Live:** https://webworksa1.github.io/0Office-com/

## Structure
- `build.py` + `src/*.py`: the Python generator. Edit content in `src/`, run `python3 build.py`, and commit. It writes each page as front matter plus body, and `_layouts/default.html` holds the shared header, top bar and footer. GitHub Pages' built-in Jekyll assembles the final HTML on the free plan, with no Actions needed. Run `python3 build.py --static out/` to get fully rendered standalone HTML for local preview or another host.
- `assets/js/config.js`: **the only file you need to edit for monetization.** It holds the AdSense, GA4, donation links, YouTube videos, affiliate links and FormSubmit alias.
- `assets/js/app.js`: site runtime (theme, search, forms, ads, consent, videos, donations).
- `assets/js/tools.js`: logic for all tools. Everything runs client-side.
- `docs/BUILD-PROMPTS.md`: the concept and phase-wise build prompts.
- `docs/RESEARCH.md`: the competitive research the build is based on.

## Forms & contact privacy
All forms post over AJAX to FormSubmit. The owner's address is stored encoded in `config.js` and is assembled only when a form is sent, so it never appears as text in any page. **Step 1:** the very first form submission triggers an activation email from FormSubmit, and you must click "Activate". **Step 2 (recommended):** paste the random alias FormSubmit gives you into `formAlias`.

## Go-live checklist
1. Enable ads: set `adsenseClient` and `adSlots`, and add your line to `ads.txt`. For EEA/UK traffic, also enable a Google-certified CMP in AdSense.
2. Donations: add your PayPal, Stripe Payment Link, Buy Me a Coffee, Ko-fi or GitHub Sponsors URLs.
3. Custom domain: point `0office.com` DNS to GitHub Pages and set the custom domain under Settings → Pages. Then set `SITE_URL = "https://0office.com"` in `src/layout.py`, run `python3 build.py` and commit.
4. Submit `sitemap.xml` to Google Search Console.

## Legal
© 2026 0Office.com. All rights reserved. The site is independent and not affiliated with Microsoft Office/365, ONLYOFFICE, LibreOffice, WPS Office, Google, Zoho or any other brand named on it. See `disclaimer.html`.
