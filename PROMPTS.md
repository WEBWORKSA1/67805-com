# 67805.com: phase-wise build prompts

The prompts used to plan, build, monetize and grow **67805.com — AI Business Stack**, a free AI-tools directory, planning toolkit and lead-generation site for small businesses. Run them in order. Each phase ends with a check before moving on.

Constants used across every phase:

- Domain: `67805.com` (read as "678 05": a rising 6-7-8 run, then the 5-step method)
- AdSense publisher ID: `ca-pub-6620975821265271`
- AdSense code, in the `<head>` of every page:
  `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>`
- Owner banner on top of every page: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership" linking to `https://web.works/contact`
- One inbox for every form, never visible on the site: the address is stored char-shifted in `assets/js/main.js` and rebuilt only at send time
- Hosting: GitHub Pages, free plan, repo `WEBWORKSA1/67805-com`, branch `main`, root folder

---

## Phase 0: Research and positioning

> Research the number 67805 across commerce, business, AI, economy and people. Report any existing meaning (postal codes, phone prefixes, numerology, product codes) and any trademark risk. Then propose the most monetizable website concept for a numeric five-digit .com with no inherent meaning. Score candidates on: AdSense RPM, lead value, sponsorship potential, content depth for AdSense approval, repeat-visit tools, and differentiation from sites already in the portfolio. Pick one and justify it with numbers.

> Visit 25 leading sites in the chosen niche (calculator hubs, AI tool directories, small-business resource sites, finance publishers). For each, list standout features, forms, lead-gen mechanics, trust pages and monetization. Merge into one must-have checklist.

**Check:** a one-paragraph concept, target audience, the 3 primary revenue streams, and the feature checklist.

## Phase 1: Information architecture and design system

> Design the sitemap for "67805 — AI Business Stack": home, AI tools directory, compare, stack builder, ROI calculator, AI readiness score, prompt library, guides hub plus at least 10 long-form guides, glossary, videos, free AI blueprint (lead gen), list your tool, advertise/partner, contests, careers, support (donations), about, contact, editorial & AI policy, how we make money, privacy, terms, disclaimer, trademark & copyright, 404, plus ads.txt, robots.txt, sitemap.xml, manifest, CNAME.

> Create a distinctive design system that avoids generic AI-site looks. Concept: an industrial parts catalog for business software. Cool paper background, blueprint-ink navy, signal-yellow tags, cobalt actions, mint for savings. One typeface family (Archivo, variable width): expanded weights for display, normal width for body. Light and dark themes with a toggle, visible focus, reduced-motion support, mobile-first down to 360px, no horizontal scroll.

**Check:** CSS tokens, a header/footer layout, and one memorable element (the live "stack" that assembles in the hero).

## Phase 2: Static build system

> Build a dependency-free static site. Write `src/build.py` that wraps every page in `src/pages/` and `src/guides/` with a shared head (meta, Open Graph, canonical, AdSense script, JSON-LD WebPage/BreadcrumbList/FAQPage/Article), the owner banner, sticky header, footer with legal notice, newsletter band, sticky lead CTA, exit-intent offer, cookie notice and scripts. Output plain HTML to the repo root so GitHub Pages serves it with no build step. Generate `sitemap.xml` automatically.

**Check:** `python3 src/build.py` produces every page; no page is missing the AdSense script or the owner banner.

## Phase 3: Interactive tools (the repeat-visit engine)

> Create `assets/js/tools-data.js` with 75+ real AI tools across 14 business categories. Each tool: name, category, pricing model, original one-line description, official URL, best-for business types, skill level, editors' pick flag. Write all descriptions originally; never copy vendor copy.

> Create `assets/js/app.js` with:
> 1. Hero stack: goal chips that drop tool "layers" into a stack and update hours saved and dollar value.
> 2. Directory: search, category, pricing, sort, local shortlist, compare checkboxes (max 3) and URL state.
> 3. Compare: three selects and a side-by-side table.
> 4. Stack builder: 5 questions produce a layered stack, hours/month and dollar value, print, and an "email me this stack" lead form carrying the result.
> 5. ROI calculator: hours saved, gross and net monthly savings, payback, first-year ROI, the full formula shown, and a shareable link.
> 6. AI readiness score: 8 questions, score out of 100, level, weak areas, and a gated "full report" lead form.
> 7. Prompt library: 30 original prompts with team filter and copy buttons.

**Check:** run every tool in a headless browser on desktop and mobile; zero JavaScript errors.

## Phase 4: Lead generation and forms

> Build a 3-step "Free AI blueprint" form (business, goals, contact) with progress bar, consent checkbox, optional partner-introduction opt-in, and UTM/referrer capture. Add a short version on the homepage, a sticky CTA after scroll, an exit-intent offer on desktop, and lead capture inside the stack builder and readiness score.

> Route every form (blueprint, newsletter, contact, tool submission, advertising inquiry, contest entry, job application, support pledge) through one handler in `main.js` that posts JSON to FormSubmit's AJAX endpoint. The destination address must never appear in HTML, visible text or plain-text JS: store it char-shifted and reversed, rebuild it only at send time. Include a honeypot field on every form.

**Check:** `grep -r` for the address across the repo returns nothing.

## Phase 5: Monetization pages

> Write: List your tool (free review, featured listing from $149/month, category sponsor from $499/month), Advertise & partner (newsletter, guide, contest sponsorships, implementation-partner network, domain/website acquisition linking to web.works/contact), Support (PayPal donations with amounts and purpose buttons for operations, promotion and marketing, hiring talent and contest prizes, plus a pledge form and a funds-allocation table), Contests (monthly AI Workflow Challenge with prizes, judging criteria, entry form and full official rules), Careers (4 roles, hiring steps, application form).

**Check:** every paid placement is labeled Sponsored and separated from editorial.

## Phase 6: Content for AdSense approval and search

> Write 10 original guides of 900–1,400 words each, for small-business owners: building an AI stack, measuring AI ROI, customer support playbook, the 5-step automation method, a content workflow, bookkeeping and admin automation, prompt writing for teams, a simple AI use policy, choosing an AI assistant, and AI for sales follow-up. Each with byline, updated date, read time, tables, a callout, FAQ schema where useful, related guides, and a sidebar blueprint CTA. Add a 30-term glossary and a videos page with verified YouTube embeds loaded through click-to-play facades.

> Write trust pages: About (including what "67805" means and does not mean), Editorial & AI policy, How we make money, Privacy (AdSense cookie disclosure, opt-out links, GDPR/CCPA rights, form processor and PayPal), Terms, Disclaimer, Trademark & copyright notice (third-party marks, nominative use, no affiliation with any business using similar digits including "67858", infringement reporting).

**Check against AdSense program policies:** original and substantial content on every indexable page; clear navigation; About, Contact and Privacy pages; no ads on empty or error pages beyond auto ads; no prohibited content; no encouragement to click ads; ads.txt present.

## Phase 7: Deploy on GitHub Pages (free plan)

> Push to `WEBWORKSA1/67805-com` on `main`. Include `.nojekyll` and `CNAME` (67805.com). Enable Pages from `main` / root. At the registrar, point DNS to GitHub Pages: A records for `@` to 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 and a CNAME for `www` to `webworksa1.github.io`. After DNS resolves, tick "Enforce HTTPS".

**Check:** the home page, a guide, ads.txt and sitemap.xml load over HTTPS on 67805.com.

## Phase 8: Launch and growth

> Submit the sitemap in Google Search Console. Apply the site in AdSense (Sites > Add site > 67805.com) and set up the Google-certified consent message under Privacy & messaging for EEA/UK/CH. Activate FormSubmit by submitting the first form and clicking the confirmation email, then replace the obfuscated address with FormSubmit's random alias for extra privacy.

> Publish 2 new guides a week for 8 weeks, each targeting a "best AI tool for [job]" or "how to automate [task]" query. Send The Friday Stack weekly. Pitch 20 AI tool makers on featured listings. Recruit 5 implementation partners for blueprint introductions. Run the first Workflow Challenge in November 2026.

**Targets for month 3:** 30+ guides, AdSense approved, 300 newsletter subscribers, 40 blueprint leads per month, 3 paying sponsors.
