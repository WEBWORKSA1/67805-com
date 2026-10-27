#!/usr/bin/env python3
"""Static site builder for 67805.com.
Every page in src/pages and src/guides starts with a JSON header comment:
<!--{"title":"…","desc":"…","nav":"tools"}-->
Run:  python3 src/build.py   (writes HTML into the repo root and /guides)
"""
import json, os, re, datetime, html

_jd = json.dumps
json.dumps = lambda o, **k: _jd(o, ensure_ascii=False, **k)  # keep real characters in JSON-LD

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://67805.com"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
TODAY = datetime.date.today().isoformat()

NAV = [("tools", "tools.html", "AI tools"), ("stack", "stack-builder.html", "Stack builder"),
       ("roi", "roi-calculator.html", "ROI"), ("prompts", "prompts.html", "Prompts"),
       ("guides", "guides.html", "Guides"), ("videos", "videos.html", "Videos")]

LOGO = '''<svg viewBox="0 0 32 32" aria-hidden="true"><rect x="3" y="21" width="26" height="7" rx="1.5" fill="currentColor"/><rect x="5" y="12.5" width="22" height="7" rx="1.5" fill="currentColor" opacity=".72"/><rect x="7" y="4" width="18" height="7" rx="1.5" fill="#F2C230"/></svg>'''

def head(meta, p):
    title = meta["title"]
    full = title if "67805" in title else f"{title} | 67805.com"
    desc = html.escape(meta["desc"], quote=True)
    url = DOMAIN + "/" + meta["_path"].replace("index.html", "")
    schema = meta.get("schema", "")
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(full)}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{meta.get('robots','index,follow,max-image-preview:large')}">
<meta name="theme-color" content="#18212F">
<meta property="og:type" content="{'article' if meta.get('article') else 'website'}">
<meta property="og:site_name" content="67805.com">
<meta property="og:title" content="{html.escape(full, quote=True)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{p}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{p}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/site.css">
{ADSENSE}
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"WebPage","name":full,"description":meta["desc"],"url":url,"isPartOf":{"@type":"WebSite","name":"67805.com","url":DOMAIN+"/"},"dateModified":TODAY})}</script>
{schema}
</head>'''

def header(active, p):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{p}{href}"{cur if key==active else ""}>{label}</a>' for key, href, label in NAV)
    return f'''<body{' data-nocta' if active in ('blueprint',) else ''}>
<a class="skip" href="#main">Skip to content</a>
<div class="owner" role="note">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership: <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></div>
<header class="hdr"><div class="wrap">
<a class="logo" href="{p}index.html" aria-label="67805.com home">{LOGO}<span>67805<small>AI business stack</small></span></a>
<button class="iconbtn burger" id="burger" aria-controls="nav" aria-expanded="false" aria-label="Open menu"><svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M2 5h16M2 10h16M2 15h16" stroke="currentColor" stroke-width="2"/></svg></button>
<nav class="nav" id="nav" aria-label="Main">{links}
<button class="iconbtn" id="themeBtn" type="button" aria-label="Switch light or dark theme"><svg width="18" height="18" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 2a8 8 0 1 0 0 16V2z" fill="currentColor"/><circle cx="10" cy="10" r="7.2" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button>
<a class="btn sm" href="{p}blueprint.html">Free AI blueprint</a></nav>
</div></header>
<main id="main">'''

NEWS = '''<section class="sec tight alt" aria-labelledby="newsH"><div class="wrap news">
<div><h2 id="newsH">The Friday Stack</h2><p class="mb0">One email a week: three AI tools worth testing, one workflow you can copy, and what changed in pricing. Five minutes to read. No spam, unsubscribe in one click.</p></div>
<form data-form="Newsletter signup" data-ok="You’re in. The next issue arrives Friday." novalidate>
<label class="hp" aria-hidden="true">Leave empty<input name="hp_name" tabindex="-1" autocomplete="off"></label>
<label for="nlEmail{n}" class="hide">Email address</label>
<input id="nlEmail{n}" name="email" type="email" required placeholder="you@business.com" autocomplete="email">
<button class="btn" type="submit">Subscribe</button>
<p class="form-msg" aria-live="polite"></p>
</form></div></section>'''

def footer(p, meta):
    news = "" if meta.get("nonews") else NEWS.replace("{n}", "F")
    return f'''</main>
{news}
<footer class="ftr"><div class="wrap">
<div class="cols">
<div><a class="logo" href="{p}index.html" style="color:#fff">{LOGO}<span>67805</span></a>
<p class="mt" style="margin-top:14px">Independent guides, tools and estimates that help small businesses choose and set up AI. Free to use. Funded by advertising, sponsorships and reader support.</p></div>
<div><h4>Tools</h4><ul><li><a href="{p}tools.html">AI tools directory</a></li><li><a href="{p}compare.html">Compare tools</a></li><li><a href="{p}stack-builder.html">Stack builder</a></li><li><a href="{p}roi-calculator.html">ROI calculator</a></li><li><a href="{p}ai-readiness.html">Readiness score</a></li><li><a href="{p}prompts.html">Prompt library</a></li></ul></div>
<div><h4>Learn</h4><ul><li><a href="{p}guides.html">Guides</a></li><li><a href="{p}videos.html">Videos</a></li><li><a href="{p}glossary.html">AI glossary</a></li><li><a href="{p}guides/five-step-ai-automation-method.html">The 5-step method</a></li></ul></div>
<div><h4>Work with us</h4><ul><li><a href="{p}blueprint.html">Free AI blueprint</a></li><li><a href="{p}list-your-tool.html">List your tool</a></li><li><a href="{p}advertise.html">Advertise & sponsor</a></li><li><a href="{p}contests.html">Contests & prizes</a></li><li><a href="{p}careers.html">Careers</a></li><li><a href="{p}support.html">Support us</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="{p}about.html">About</a></li><li><a href="{p}contact.html">Contact</a></li><li><a href="{p}editorial-policy.html">Editorial & AI policy</a></li><li><a href="{p}how-we-make-money.html">How we make money</a></li><li><a href="{p}privacy.html">Privacy</a></li><li><a href="{p}terms.html">Terms</a></li><li><a href="{p}disclaimer.html">Disclaimer</a></li><li><a href="{p}trademark.html">Trademark & copyright</a></li></ul></div>
</div>
<div class="legal">© <span data-year>2026</span> 67805.com. All rights reserved. Original text, tools and design on this site are protected by copyright. Third-party product names, logos and brands mentioned are trademarks of their respective owners, used only to identify those products; their use does not imply endorsement or affiliation. “67805” is used here only as this site’s domain name and is not affiliated with any other business, ZIP code area, phone number or product using similar digits. Information is general and educational, not financial, legal or tax advice. See <a href="{p}trademark.html">Trademark & copyright notice</a> and <a href="{p}disclaimer.html">Disclaimer</a>.</div>
</div></footer>
<div class="sticky" id="sticky" role="complementary" aria-label="Free blueprint offer"><p><strong>Free AI blueprint.</strong> Tell us how you work; get a written plan in 2 business days.</p><a class="btn sig sm" href="{p}blueprint.html">Get mine</a><button class="iconbtn x" type="button" aria-label="Dismiss" style="color:inherit;border-color:rgba(255,255,255,.3);width:32px;height:32px">×</button></div>
<div class="modal" id="exit" role="dialog" aria-modal="true" aria-labelledby="exitH"><div class="panel"><button class="iconbtn x" type="button" aria-label="Close">×</button>
<h2 id="exitH" style="font-size:1.6rem">Before you go: find your AI quick wins</h2><p>Answer 8 questions and get your AI readiness score with the three changes that would save you the most time. Takes 2 minutes.</p>
<a class="btn" href="{p}ai-readiness.html">Get my score</a> <a class="btn ghost" href="{p}blueprint.html">Request a blueprint</a></div></div>
<div class="consent" id="consent" role="dialog" aria-label="Cookie notice"><p>We use cookies for ads (Google AdSense), basic analytics and to remember your settings. Read our <a href="{p}privacy.html">privacy policy</a>.</p><button class="btn sm" data-consent="all" type="button">Accept</button> <button class="btn sm ghost" data-consent="essential" type="button">Essential only</button></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="{p}assets/js/main.js" defer></script>
{meta.get('scripts_html','')}
</body>
</html>
'''

def crumbs(meta, p):
    c = meta.get("crumbs")
    if not c: return ""
    items = [("Home", p + "index.html")] + [(n, p + h if h else None) for n, h in c]
    parts, ld = [], []
    for i, (n, h) in enumerate(items):
        parts.append(f'<a href="{h}">{n}</a>' if h else f'<span aria-current="page">{n}</span>')
        ld.append({"@type": "ListItem", "position": i + 1, "name": n, **({"item": DOMAIN + "/" + h.replace("../", "")} if h else {})})
    meta["schema"] = meta.get("schema", "") + '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld}) + "</script>"
    return '<nav class="crumbs wrap" aria-label="Breadcrumb">' + " / ".join(parts) + "</nav>"

def render(src, out_rel, prefix):
    raw = open(src, encoding="utf-8").read()
    m = re.match(r"<!--(\{.*?\})-->\s*", raw, re.S)
    meta = json.loads(m.group(1)); body = raw[m.end():]
    meta["_path"] = out_rel
    scripts = meta.get("scripts", [])
    meta["scripts_html"] = "\n".join(f'<script src="{prefix}assets/js/{s}" defer></script>' for s in scripts)
    if meta.get("faq"):
        meta["schema"] = meta.get("schema", "") + '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in meta["faq"]]}) + "</script>"
    if meta.get("article"):
        meta["schema"] = meta.get("schema", "") + '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": meta["title"], "description": meta["desc"], "author": {"@type": "Organization", "name": "67805.com Editorial Team"}, "publisher": {"@type": "Organization", "name": "67805.com"}, "datePublished": meta.get("date", TODAY), "dateModified": TODAY, "mainEntityOfPage": DOMAIN + "/" + out_rel}) + "</script>"
    cr = crumbs(meta, prefix)
    body = body.replace("{P}", prefix).replace("{NEWS_INLINE}", NEWS.replace("{n}", "I"))
    page = head(meta, prefix) + header(meta.get("nav", ""), prefix) + cr + body + footer(prefix, meta)
    dst = os.path.join(ROOT, out_rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, "w", encoding="utf-8").write(page)
    return meta

def main():
    urls, guides = [], []
    gdir = os.path.join(ROOT, "src", "guides")
    for f in sorted(os.listdir(gdir)):
        if f.endswith(".html"):
            meta = render(os.path.join(gdir, f), "guides/" + f, "../")
            guides.append((f, meta)); urls.append(("guides/" + f, "0.8"))
    pdir = os.path.join(ROOT, "src", "pages")
    for f in sorted(os.listdir(pdir)):
        if f.endswith(".html"):
            meta = render(os.path.join(pdir, f), f, "/" if f == "404.html" else "")
            if f != "404.html" and "noindex" not in meta.get("robots", ""):
                urls.append((f, "1.0" if f == "index.html" else "0.7"))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr in sorted(urls, key=lambda x: (x[0] != "index.html", x[0])):
        loc = DOMAIN + "/" + ("" if u == "index.html" else u)
        sm.append(f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    print(f"Built {len(urls)+1} pages")

if __name__ == "__main__":
    main()
