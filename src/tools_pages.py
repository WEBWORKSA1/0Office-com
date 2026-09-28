"""Free tool pages."""
from layout import page, page_hero, ad, faq_block, newsletter

CUR = '<option>USD</option><option>EUR</option><option>GBP</option><option>CAD</option><option>AUD</option><option>INR</option><option>AED</option><option>SGD</option><option>JPY</option><option>CHF</option><option>NZD</option><option>ZAR</option><option>BRL</option><option>MXN</option><option>PHP</option>'


def sel_cur(id_):
    return f'<select id="{id_}" aria-label="Currency">{CUR}</select>'


TOOLS = [
 dict(slug="invoice-generator", name="Free Invoice Generator", icon="🧾", cat="Money", key="invoice",
  short="Create a professional invoice in seconds, print or save as PDF. No signup.",
  kw="invoice template bill receipt pdf freelance",
  ui=f'''<div class="form-row"><div><label for="invFrom">From (your business)</label><textarea id="invFrom" data-keep rows="3" placeholder="Your name / company&#10;Address&#10;Tax ID"></textarea></div>
<div><label for="invTo">Bill to</label><textarea id="invTo" data-keep rows="3" placeholder="Client name&#10;Address"></textarea></div></div>
<div class="form-row"><div><label for="invNo">Invoice #</label><input id="invNo" data-keep value="INV-0001"></div><div><label for="invCur">Currency</label>{sel_cur("invCur").replace('id="invCur"','id="invCur" data-keep')}</div></div>
<div class="form-row"><div><label for="invDate">Invoice date</label><input id="invDate" data-keep type="date"></div><div><label for="invDueDate">Due date</label><input id="invDueDate" data-keep type="date"></div></div>
<div class="table-wrap"><table><thead><tr><th>Description</th><th>Qty</th><th>Rate</th><th>Amount</th><th class="no-print"></th></tr></thead><tbody id="invItems"></tbody></table></div>
<button class="btn btn-ghost btn-sm no-print" id="invAdd" type="button" style="margin:10px 0">+ Add line</button>
<div class="form-row"><div><label for="invNotes">Notes / payment terms</label><textarea id="invNotes" data-keep rows="4" placeholder="Payment by bank transfer within 14 days. Thank you!"></textarea></div>
<div class="tool-out"><table>
<tr><td>Subtotal</td><td id="invSub" style="text-align:right"></td></tr>
<tr><td>Discount % <input id="invDisc" data-keep type="number" min="0" value="0" style="width:80px;padding:6px" aria-label="Discount percent"></td><td id="invDiscOut" style="text-align:right"></td></tr>
<tr><td>Tax % <input id="invTax" data-keep type="number" min="0" value="0" style="width:80px;padding:6px" aria-label="Tax percent"></td><td id="invTaxOut" style="text-align:right"></td></tr>
<tr><td>Shipping <input id="invShip" data-keep type="number" min="0" value="0" style="width:90px;padding:6px" aria-label="Shipping"></td><td></td></tr>
<tr><th>Total</th><th id="invTotal" style="text-align:right;font-size:1.2rem;color:var(--text)"></th></tr>
<tr><td>Amount paid <input id="invPaid" data-keep type="number" min="0" value="0" style="width:90px;padding:6px" aria-label="Amount paid"></td><td></td></tr>
<tr><th>Balance due</th><th id="invDue" style="text-align:right;font-size:1.2rem;color:var(--brand)"></th></tr></table></div></div>
<div class="no-print" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:14px"><button class="btn btn-primary" id="invPrint" type="button">⬇ Download / Print PDF</button><button class="btn btn-ghost" id="invReset" type="button">Start new</button></div>''',
  how=["Fill in your business and client details.", "Add line items — totals, discount and tax update live.", "Click <b>Download / Print PDF</b> and choose “Save as PDF”. Your draft auto-saves in this browser."],
  faq=[("Is this invoice generator really free?", "Yes. No account, no watermark, no limits. Everything runs in your browser and your data is never uploaded."),
       ("How do I save the invoice as a PDF?", "Click Download / Print PDF, then choose “Save as PDF” as the printer. The page prints only the invoice, without site navigation or ads."),
       ("Is my invoice data stored?", "Only in your own browser’s local storage so you can come back to a draft. Click “Start new” to clear it.")]),
 dict(slug="meeting-cost-calculator", name="Meeting Cost Calculator", icon="💸", cat="Teams", key="meeting",
  short="See what a meeting really costs — with a live running meter you can share on screen.",
  kw="meeting cost calculator salary time waste",
  ui=f'''<div class="form-row"><div><label for="mcPeople">Attendees</label><input id="mcPeople" type="number" min="1" value="6"></div><div><label for="mcSalary">Average annual salary</label><input id="mcSalary" type="number" min="0" value="85000"></div></div>
<div class="form-row"><div><label for="mcMins">Planned length (minutes)</label><input id="mcMins" type="number" min="1" value="60"></div><div><label for="mcFreq">Times per week</label><input id="mcFreq" type="number" min="0" value="1"></div></div>
<div class="form-row"><div><label for="mcOverhead">Benefits &amp; overhead %</label><input id="mcOverhead" type="number" min="0" value="30"></div><div><label for="mcHours">Paid hours per year</label><input id="mcHours" type="number" min="1" value="2080"></div></div>
<div><label for="mcCur">Currency</label>{sel_cur("mcCur")}</div>
<div class="kpis" style="margin-top:16px"><div class="kpi"><span>This meeting</span><b id="mcPlanned"></b></div><div class="kpi"><span>Per minute</span><b id="mcPerMin"></b></div><div class="kpi"><span>Per week</span><b id="mcWeekly"></b></div><div class="kpi"><span>Per year (48 wks)</span><b id="mcYearly"></b></div></div>
<div class="tool-out center" style="margin-top:16px"><div class="muted">Live meter</div><div class="big-num" id="mcLive" style="color:var(--danger)"></div><div class="muted" id="mcClock"></div>
<div style="display:flex;gap:10px;justify-content:center;margin-top:12px;flex-wrap:wrap"><button class="btn btn-primary" id="mcStart" type="button">▶ Start live meter</button><button class="btn btn-ghost" id="mcStop" type="button">Reset</button></div></div>''',
  how=["Enter attendees and their average salary.", "Adjust overhead (benefits, taxes, equipment — 20–40% is common).", "Start the live meter during your meeting to watch the cost climb in real time."],
  faq=[("How is meeting cost calculated?", "Attendees × (annual salary ÷ paid hours per year) × (1 + overhead %) × meeting length. It’s an estimate of fully-loaded labour cost, not including opportunity cost."),
       ("What overhead percentage should I use?", "Many businesses estimate 20–40% on top of salary for benefits, payroll taxes and equipment. Use your own finance numbers if you have them.")]),
 dict(slug="time-zone-planner", name="Time Zone Meeting Planner", icon="🌐", cat="Teams", key="timezone",
  short="Find overlapping working hours across cities and share the view with one link.",
  kw="time zone converter world clock meeting planner overlap",
  ui='''<form id="tzAdd" class="form-row" style="align-items:end"><div><label for="tzInput">Add a city / time zone</label><input id="tzInput" list="tzList" placeholder="e.g. Europe/Paris" autocomplete="off"><datalist id="tzList"></datalist></div><div><button class="btn btn-primary" type="submit">+ Add zone</button></div></form>
<div class="form-row" style="margin-top:10px"><div><label for="tzStart">Working day starts (local hour)</label><input id="tzStart" type="number" min="0" max="23" value="9"></div><div><label for="tzEnd">Working day ends</label><input id="tzEnd" type="number" min="1" max="24" value="17"></div></div>
<div class="tz-grid" id="tzGrid" style="margin-top:16px"></div>
<p id="tzBest" class="muted" style="margin-top:10px"></p>
<button class="btn btn-ghost btn-sm" id="tzShare" type="button">🔗 Copy shareable link</button>''',
  how=["Your local zone is added automatically. Add teammates’ zones from the list.", "Set your working-day window.", "Solid-coloured columns are hours when everyone is inside working hours. Copy the link to share this exact view."],
  faq=[("Does it handle daylight saving time?", "Yes. It uses your browser’s built-in time zone database, which applies daylight-saving rules for each zone."),
       ("Can I share the planner with my team?", "Yes — the URL updates with your selected zones. Click “Copy shareable link” and paste it into chat.")]),
 dict(slug="pomodoro-timer", name="Pomodoro Focus Timer", icon="⏱️", cat="Focus", key="pomodoro",
  short="A clean focus timer with task list, custom intervals and desktop notifications.",
  kw="pomodoro timer focus productivity tomato",
  ui='''<div class="center"><div class="seg" role="tablist"><button type="button" data-mode="focus" class="on">Focus</button><button type="button" data-mode="short">Short break</button><button type="button" data-mode="long">Long break</button></div>
<div class="timer-face" id="pmFace" aria-live="off">25:00</div>
<div style="display:flex;gap:10px;justify-content:center"><button class="btn btn-primary btn-lg" id="pmGo" type="button">Start</button><button class="btn btn-ghost btn-lg" id="pmReset" type="button">Reset</button></div>
<p class="muted" style="margin-top:12px">Focus sessions completed today: <b id="pmDone">0</b></p></div>
<div class="form-row" style="grid-template-columns:repeat(3,1fr)"><div><label for="pm-focus">Focus (min)</label><input id="pm-focus" type="number" min="1" value="25"></div><div><label for="pm-short">Short (min)</label><input id="pm-short" type="number" min="1" value="5"></div><div><label for="pm-long">Long (min)</label><input id="pm-long" type="number" min="1" value="15"></div></div>
<h3 style="margin-top:20px">Tasks</h3><form id="pmTaskForm" style="display:flex;gap:8px"><input id="pmTask" placeholder="What are you working on?" aria-label="New task"><button class="btn btn-primary" type="submit">Add</button></form>
<ul id="pmTasks" style="list-style:none;padding:0;margin:12px 0"></ul><button class="btn btn-ghost btn-sm" id="pmClear" type="button">Clear finished</button>''',
  how=["Add what you’re working on.", "Press Start — focus for 25 minutes, then take a 5-minute break. Every 4th break is long.", "Allow notifications to get alerted even when the tab is in the background."],
  faq=[("What is the Pomodoro Technique?", "A time-management method: work in focused blocks (traditionally 25 minutes) separated by short breaks, with a longer break after four blocks."),
       ("Can I change the intervals?", "Yes. Set custom focus, short and long break lengths below the timer.")]),
 dict(slug="word-counter", name="Word & Character Counter", icon="🔤", cat="Writing", key="words",
  short="Live word, character, sentence and reading-time counts, keyword density and case converter.",
  kw="word count character count reading time keyword density case converter",
  ui='''<label for="wcText">Paste or type your text</label><textarea id="wcText" rows="12" placeholder="Start typing…"></textarea>
<div style="display:flex;gap:8px;flex-wrap:wrap;margin:10px 0"><button class="btn btn-ghost btn-sm" id="wcCopy" type="button">Copy</button><button class="btn btn-ghost btn-sm" id="wcClear" type="button">Clear</button>
<select id="wcCase" aria-label="Change case" style="width:auto"><option value="">Change case…</option><option value="sentence">Sentence case</option><option value="title">Title Case</option><option value="upper">UPPERCASE</option><option value="lower">lowercase</option></select></div>
<div class="kpis"><div class="kpi"><span>Words</span><b id="wcWords">0</b></div><div class="kpi"><span>Characters</span><b id="wcChars">0</b></div><div class="kpi"><span>No spaces</span><b id="wcNoSp">0</b></div><div class="kpi"><span>Sentences</span><b id="wcSent">0</b></div><div class="kpi"><span>Paragraphs</span><b id="wcPara">0</b></div><div class="kpi"><span>Reading time</span><b id="wcRead">0</b></div><div class="kpi"><span>Speaking time</span><b id="wcSpeak">0</b></div><div class="kpi"><span>Readability (Flesch)</span><b id="wcFre">—</b></div></div>
<h3 style="margin-top:18px">Top keywords</h3><div class="table-wrap"><table><thead><tr><th>Word</th><th>Count</th><th>Density</th></tr></thead><tbody id="wcKw"></tbody></table></div>''',
  how=["Paste your text — counts update as you type.", "Use keyword density to spot over-used words.", "Convert case in one click."],
  faq=[("How is reading time calculated?", "Using an average adult silent-reading speed of about 238 words per minute; speaking time uses about 140 words per minute."),
       ("What does the Flesch score mean?", "Flesch Reading Ease: 60–70 is plain English; higher is easier, lower is harder. It’s an approximation for English text.")]),
 dict(slug="salary-converter", name="Salary & Hourly Rate Converter", icon="💱", cat="Money", key="salary",
  short="Convert between hourly, daily, weekly, monthly and annual pay instantly.",
  kw="salary converter hourly to annual wage calculator",
  ui=f'''<div class="form-row"><div><label for="sc-hour">Hourly</label><input id="sc-hour" type="number" step="any"></div><div><label for="sc-day">Daily</label><input id="sc-day" type="number" step="any"></div></div>
<div class="form-row"><div><label for="sc-week">Weekly</label><input id="sc-week" type="number" step="any"></div><div><label for="sc-biweek">Bi-weekly</label><input id="sc-biweek" type="number" step="any"></div></div>
<div class="form-row"><div><label for="sc-month">Monthly</label><input id="sc-month" type="number" step="any"></div><div><label for="sc-year">Annual</label><input id="sc-year" type="number" step="any" value="60000"></div></div>
<details style="margin-top:8px"><summary>Assumptions</summary><div class="form-row" style="margin-top:12px"><div><label for="scHours">Hours per week</label><input id="scHours" type="number" value="40"></div><div><label for="scDays">Days per week</label><input id="scDays" type="number" value="5"></div></div>
<div class="form-row"><div><label for="scWeeks">Paid weeks per year</label><input id="scWeeks" type="number" value="52"></div><div><label for="scTax">Estimated tax %</label><input id="scTax" type="number" value="25"></div></div><div><label for="scCur">Currency</label>{sel_cur("scCur")}</div></details>
<div class="tool-out" style="margin-top:14px"><div class="muted">Estimated take-home</div><div class="big-num" id="scNet" style="font-size:1.4rem"></div></div>''',
  how=["Type into any field — all the others update.", "Open Assumptions to set your hours, days, weeks and an estimated tax rate."],
  faq=[("How do I convert hourly to annual salary?", "Hourly rate × hours per week × paid weeks per year. At 40 hours and 52 weeks, that’s hourly × 2,080."),
       ("Is the take-home figure exact?", "No — it applies a single flat estimated tax rate. Real take-home depends on your country, brackets, deductions and benefits.")]),
 dict(slug="remote-work-savings-calculator", name="Remote Work Savings Calculator", icon="🏡", cat="Money", key="savings",
  short="How much time and money does working remotely save you — and your company?",
  kw="remote work savings commute cost calculator work from home",
  ui=f'''<h3>You</h3><div class="form-row"><div><label for="rsDays">Remote days per week</label><input id="rsDays" type="number" min="0" max="7" value="5"></div><div><label for="rsWeeks">Working weeks per year</label><input id="rsWeeks" type="number" value="48"></div></div>
<div class="form-row"><div><label for="rsMins">One-way commute (minutes)</label><input id="rsMins" type="number" value="40"></div><div><label for="rsCommuteCost">Commute cost per day (fuel, transit, parking)</label><input id="rsCommuteCost" type="number" value="12"></div></div>
<div class="form-row"><div><label for="rsLunch">Extra spend per office day (lunch, coffee)</label><input id="rsLunch" type="number" value="10"></div><div><label for="rsClothes">Work clothes per year</label><input id="rsClothes" type="number" value="400"></div></div>
<div class="form-row"><div><label for="rsCare">Extra childcare / pet care per month</label><input id="rsCare" type="number" value="0"></div><div><label for="rsHome">Added home costs per month (power, internet)</label><input id="rsHome" type="number" value="40"></div></div>
<div class="form-row"><div><label for="rsWage">Value of your time per hour</label><input id="rsWage" type="number" value="30"></div><div><label for="rsCur">Currency</label>{sel_cur("rsCur")}</div></div>
<div class="kpis" style="margin-top:12px"><div class="kpi"><span>Cash saved / year</span><b id="rsCash"></b></div><div class="kpi"><span>Commute time saved</span><b id="rsHours"></b></div><div class="kpi"><span>That's</span><b id="rsDaysBack"></b></div><div class="kpi"><span>Total value / year</span><b id="rsTotal"></b></div></div>
<h3 style="margin-top:20px">Your company</h3><div class="form-row"><div><label for="rsTeam">Team members</label><input id="rsTeam" type="number" value="10"></div><div><label for="rsRent">Office cost per seat per month</label><input id="rsRent" type="number" value="600"></div></div>
<div class="tool-out"><div class="muted">Office cost avoided per year (seat cost only)</div><div class="big-num" id="rsEmployer"></div><a href="../get-started.html?need=virtual-office" class="btn btn-primary btn-sm">Replace the lease with a virtual office →</a></div>''',
  how=["Enter your commute and office-day spending.", "Subtract any extra home costs.", "See personal savings and the seat cost your company avoids."],
  faq=[("What costs does this include?", "Commuting, office-day food, work clothing, extra care costs, minus added home costs. Time savings are valued at the hourly rate you enter."),
       ("How accurate is the employer figure?", "It multiplies seats by your per-seat cost. Real savings depend on lease terms, utilities, equipment stipends and any coworking you still buy.")]),
 dict(slug="freelance-rate-calculator", name="Freelance Rate Calculator", icon="🧮", cat="Money", key="rate",
  short="Work out the hourly and day rate you need to hit your income goal after tax and time off.",
  kw="freelance rate calculator hourly rate consultant pricing",
  ui=f'''<div class="form-row"><div><label for="frIncome">Target take-home income / year</label><input id="frIncome" type="number" value="70000"></div><div><label for="frCosts">Business costs / month (software, insurance, gear)</label><input id="frCosts" type="number" value="400"></div></div>
<div class="form-row"><div><label for="frTax">Tax rate %</label><input id="frTax" type="number" value="30"></div><div><label for="frOff">Weeks off per year (holidays, sick)</label><input id="frOff" type="number" value="6"></div></div>
<div class="form-row"><div><label for="frHours">Working hours per week</label><input id="frHours" type="number" value="40"></div><div><label for="frBill">Billable % of time</label><input id="frBill" type="number" value="65"></div></div>
<div class="form-row"><div><label for="frMargin">Profit / safety margin %</label><input id="frMargin" type="number" value="10"></div><div><label for="frCur">Currency</label>{sel_cur("frCur")}</div></div>
<div class="kpis" style="margin-top:12px"><div class="kpi"><span>Minimum hourly rate</span><b id="frHourly"></b></div><div class="kpi"><span>Day rate</span><b id="frDay"></b></div><div class="kpi"><span>Gross revenue needed</span><b id="frGross"></b></div><div class="kpi"><span>Billable hours</span><b id="frBillable"></b></div></div>''',
  how=["Enter the income you want to take home and your monthly costs.", "Be honest about billable % — admin, sales and learning aren’t billable.", "Use the hourly rate as your floor, not your price."],
  faq=[("Why is billable percentage so important?", "Freelancers rarely bill every working hour. At 65% billable on a 40-hour week, only 26 hours generate revenue."),
       ("Should I charge exactly this rate?", "Treat it as your minimum. Price based on value and market rates for your niche, above this floor.")]),
 dict(slug="business-days-calculator", name="Business Days Calculator", icon="📅", cat="Teams", key="bizdays",
  short="Count working days between dates, exclude holidays, or add N business days to a date.",
  kw="business days calculator working days between dates deadline",
  ui='''<div class="form-row"><div><label for="bdStart">Start date</label><input id="bdStart" type="date"></div><div><label for="bdEnd">End date</label><input id="bdEnd" type="date"></div></div>
<div><label for="bdHol">Holidays to exclude (YYYY-MM-DD, comma separated)</label><input id="bdHol" placeholder="2026-12-25, 2027-01-01"></div>
<div class="form-row"><div><label for="bdHpd">Hours per working day</label><input id="bdHpd" type="number" value="8"></div><div><label for="bdAdd">Add business days to start</label><input id="bdAdd" type="number" value="10"></div></div>
<div class="kpis" style="margin-top:12px"><div class="kpi"><span>Business days</span><b id="bdWork"></b></div><div class="kpi"><span>Calendar days</span><b id="bdCal"></b></div><div class="kpi"><span>Weekend days</span><b id="bdWk"></b></div><div class="kpi"><span>Working hours</span><b id="bdHours"></b></div></div>
<div class="tool-out" style="margin-top:12px"><div class="muted">Start date + business days =</div><div class="big-num" id="bdAddOut" style="font-size:1.4rem"></div></div>''',
  how=["Pick a start and end date (both inclusive).", "List public holidays to exclude.", "Use “Add business days” to find a deadline."],
  faq=[("Are start and end dates included?", "Yes, both are counted when they fall on a working day."),
       ("Which days count as weekends?", "Saturday and Sunday.")]),
 dict(slug="password-generator", name="Strong Password Generator", icon="🔐", cat="Security", key="password",
  short="Generate strong random passwords and passphrases locally with your browser's secure RNG.",
  kw="password generator strong random passphrase security",
  ui='''<div style="display:flex;gap:8px"><input id="pwOut" readonly aria-label="Generated password" style="font-family:var(--mono);font-size:1.15rem"><button class="btn btn-primary" id="pwCopy" type="button">Copy</button></div>
<p id="pwStrength" class="muted" style="margin:8px 0 14px"></p>
<label for="pwLen">Length: <b id="pwLenOut">20</b></label><input id="pwLen" type="range" min="8" max="64" value="20">
<div class="choice-grid" style="margin-top:12px"><label class="check"><input type="checkbox" id="pwLower" checked> Lowercase</label><label class="check"><input type="checkbox" id="pwUpper" checked> Uppercase</label><label class="check"><input type="checkbox" id="pwNum" checked> Numbers</label><label class="check"><input type="checkbox" id="pwSym" checked> Symbols</label><label class="check"><input type="checkbox" id="pwAmbig" checked> Avoid look-alikes (l, I, O, 0, 1)</label></div>
<div style="display:flex;gap:10px;margin-top:14px;flex-wrap:wrap"><button class="btn btn-ghost" id="pwGen" type="button">↻ New password</button><button class="btn btn-ghost" id="pwPhrase" type="button">Make a passphrase</button></div>''',
  how=["Choose a length (16+ recommended) and character sets.", "Copy the password straight into your password manager.", "Nothing is sent over the network — generation uses crypto.getRandomValues()."],
  faq=[("Is it safe to generate passwords online?", "This generator runs entirely in your browser using the Web Crypto API; nothing is transmitted or stored."),
       ("How long should a password be?", "For most accounts, 16+ random characters or a 5-word passphrase, stored in a password manager.")]),
 dict(slug="email-signature-generator", name="Email Signature Generator", icon="✉️", cat="Writing", key="signature",
  short="Build a clean, professional HTML email signature and copy it into Gmail or Outlook.",
  kw="email signature generator gmail outlook html",
  ui='''<div class="form-row"><div><label for="sgName">Full name</label><input id="sgName" value="Alex Morgan"></div><div><label for="sgTitle">Job title</label><input id="sgTitle" value="Founder"></div></div>
<div class="form-row"><div><label for="sgCompany">Company</label><input id="sgCompany" value="Northwind Studio"></div><div><label for="sgPhone">Phone</label><input id="sgPhone" value="+1 555 0100"></div></div>
<div class="form-row"><div><label for="sgWeb">Website</label><input id="sgWeb" value="example.com"></div><div><label for="sgColor">Accent colour</label><input id="sgColor" type="color" value="#0d9488" style="height:48px"></div></div>
<div><label for="sgHours">Working hours / time zone note</label><input id="sgHours" value="Remote · Mon–Fri 9–5 ET · async-first"></div>
<div class="tool-out" style="background:#fff;margin-top:14px"><div id="sgPreview"></div></div>
<div style="display:flex;gap:10px;margin-top:12px;flex-wrap:wrap"><button class="btn btn-primary" id="sgCopy" type="button">Copy signature</button><button class="btn btn-ghost" id="sgCopyHtml" type="button">Copy HTML code</button></div>''',
  how=["Fill in your details — the preview updates live.", "Click Copy signature and paste into Gmail (Settings → Signature) or Outlook.", "Adding a working-hours note helps distributed teams set expectations."],
  faq=[("Will this work in Gmail and Outlook?", "Yes. It uses simple table-based inline HTML, which major email clients support."),
       ("Why add working hours to a signature?", "In distributed teams it tells people when to expect a reply, reducing pressure to be always-on.")]),
 dict(slug="quick-notes", name="Private Quick Notes", icon="🗒️", cat="Focus", key="notes",
  short="A distraction-free notepad that autosaves in your browser. Download as .txt or .md.",
  kw="online notepad notes autosave private",
  ui='''<textarea id="ntText" rows="16" placeholder="Type anything. It saves automatically in this browser." style="font-size:1.05rem"></textarea>
<p class="muted" id="ntInfo" style="margin:8px 0"></p>
<div style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn btn-primary" id="ntDl" type="button">Download .txt</button><button class="btn btn-ghost" id="ntMd" type="button">Download .md</button><button class="btn btn-ghost" id="ntCopy" type="button">Copy</button><button class="btn btn-ghost" id="ntClear" type="button">Clear</button></div>''',
  how=["Just type — notes save automatically to your browser’s local storage.", "Download a copy any time. Notes never leave your device."],
  faq=[("Where are my notes stored?", "Only in your browser’s local storage on this device. Clearing site data deletes them — download a copy for safekeeping."),
       ("Can other people see my notes?", "No. Nothing is uploaded to any server.")]),
]


def tool_page(t):
    root = "../"
    related = [x for x in TOOLS if x["slug"] != t["slug"]][:6]
    rel = "".join(f'<li><a href="{x["slug"]}.html">{x["icon"]} {x["name"]}</a></li>' for x in related)
    faq_html, faq_schema = faq_block(t["faq"])
    app = {"@context": "https://schema.org", "@type": "WebApplication", "name": t["name"], "applicationCategory": "BusinessApplication",
           "operatingSystem": "Any (web browser)", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": t["short"]}
    how = "".join(f"<li>{s}</li>" for s in t["how"])
    body = f'''<div class="container" style="padding-top:28px;padding-bottom:20px">
<div class="tool-shell"><div>
<div class="tool-box" data-tool="{t["key"]}">{t["ui"]}</div>
{ad("inContent")}
<div class="prose" style="margin:0;max-width:none"><h2>How to use the {t["name"]}</h2><ol>{how}</ol>
<h2>Frequently asked questions</h2>{faq_html}</div>
</div>
<aside class="sidebar no-print">
<div class="card"><h3>Going office-free?</h3><p style="margin-bottom:12px">Get a free, personalised plan: address, phone, payroll and tools — matched to your city and budget.</p><a class="btn btn-primary btn-block" href="{root}get-started.html">Get my free plan</a></div>
{ad("sidebar").replace('class="ad-slot no-print"','class="ad-slot no-print" style="padding:0;margin:0 0 16px"')}
<div class="card"><h3>More free tools</h3><ul>{rel}</ul></div>
<div class="card"><h3>Sponsor this tool</h3><p style="margin-bottom:12px">Put your brand in front of people doing this exact task.</p><a class="btn btn-ghost btn-block" href="{root}advertise.html">See sponsorships</a></div>
</aside></div></div>
{newsletter(root)}'''
    hero = page_hero(root, [("Free Tools", "tools/index.html"), (t["name"], "")], f'{t["icon"]} {t["name"]}', t["short"] + " 100% free, private, runs in your browser.", eyebrow=t["cat"])
    return page(f'tools/{t["slug"]}.html', f'{t["name"]} — Free, No Signup', t["short"], body, active="tools", schema=[app, faq_schema],
                scripts=("tools.js",), keywords=t["kw"], hero=hero)


def tools_index():
    root = "../"
    cats = []
    for t in TOOLS:
        if t["cat"] not in cats:
            cats.append(t["cat"])
    cards = "".join(
        f'<a class="card reveal" href="{t["slug"]}.html"><div class="ico">{t["icon"]}</div><span class="tag">{t["cat"]}</span><h3>{t["name"]}</h3><p>{t["short"]}</p></a>' for t in TOOLS)
    body = f'''<section style="padding-top:36px"><div class="container">
<div class="stats" style="margin-bottom:28px"><div class="stat"><b>{len(TOOLS)}</b>free tools</div><div class="stat"><b>0</b>signups needed</div><div class="stat"><b>100%</b>runs in your browser</div><div class="stat"><b>{len(cats)}</b>categories</div></div>
<div class="grid g3">{cards}</div></div></section>
{ad("inContent")}
<section class="alt"><div class="container center"><h2>Want a tool we don't have yet?</h2><p class="muted">Suggest it — the most-requested ideas get built next, and contributors are credited.</p><a class="btn btn-primary" href="../contact.html?topic=Tool%20request">Suggest a tool</a> <a class="btn btn-ghost" href="../advertise.html">Sponsor a tool</a></div></section>
{newsletter(root)}'''
    hero = page_hero(root, [("Free Tools", "")], "Free online office tools", "Invoices, time zones, meeting costs, focus timers and more. No downloads, no accounts, no data leaves your device.", eyebrow="Toolbox")
    return page("tools/index.html", "Free Online Office Tools — No Signup", "Free browser-based office tools for remote workers and small businesses: invoice generator, time zone planner, meeting cost calculator, pomodoro timer and more.", body, active="tools", hero=hero, keywords="tools calculators generators")
