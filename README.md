# 67805.com — AI Business Stack

Free AI tools directory, stack builder, ROI calculator, readiness score, prompt library and plain-English guides that help small businesses choose, set up and measure AI.

- **Live:** https://67805.com (GitHub Pages, free plan)
- **Stack:** static HTML/CSS/JS, no framework, no build step needed to serve
- **Monetization:** Google AdSense (auto ads, `ca-pub-6620975821265271`, `ads.txt` included), sponsored listings, sponsorships, partner introductions, reader support
- **Lead generation:** 3-step Free AI Blueprint form, stack-builder and readiness-score result capture, newsletter, sticky and exit-intent CTAs. All forms post to one hidden inbox via FormSubmit.

## Edit and rebuild

Pages live in `src/pages/*.html` and guides in `src/guides/*.html`; each starts with a JSON header comment. Shared layout is in `src/build.py`.

```bash
python3 src/build.py   # regenerates the HTML in the repo root, /guides and sitemap.xml
```

Tool data: `assets/js/tools-data.js`. Prompts: `assets/js/prompts-data.js`. Interactive logic: `assets/js/app.js`. Site-wide behavior and form routing: `assets/js/main.js`.

## After deploying

1. Point 67805.com DNS at GitHub Pages (A records 185.199.108-111.153, `www` CNAME to `webworksa1.github.io`), then enable **Enforce HTTPS**.
2. Submit one form on the live site and click FormSubmit's activation email.
3. Add the site in AdSense and turn on the Google consent message for EEA/UK/CH.
4. Submit `https://67805.com/sitemap.xml` in Google Search Console.

See `PROMPTS.md` for the phase-wise build prompts and `trademark.html` for the trademark and copyright notice.
