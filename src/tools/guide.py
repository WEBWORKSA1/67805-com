"""Helper: wraps guide content into a page with header, byline and sidebar. Used by src/tools/make_guides.py"""
import json, os
def guide(slug, title, desc, cat, mins, body, related, faq=None):
    meta={"title":title,"desc":desc,"nav":"guides","article":True,"date":"2026-10-27","crumbs":[["Guides","guides.html"],[title,None]]}
    if faq: meta["faq"]=faq
    rel="".join(f'<li><a href="{{P}}guides/{s}.html">{t}</a></li>' for s,t in related)
    faqhtml=""
    if faq:
        faqhtml='<h2>Frequently asked questions</h2>'+"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)
    html=f'''<!--{json.dumps(meta)}-->
<header class="pagehead"><div class="wrap"><span class="tag sig">{cat}</span><h1 style="margin-top:12px;max-width:22ch">{title}</h1><p class="lead">{desc}</p>
<p class="byline"><span>By the 67805.com editorial team</span><span>Updated October 27, 2026</span><span>{mins} min read</span></p></div></header>
<div class="wrap article">
<div class="body">
{body}
{faqhtml}
<div class="callout"><strong>Next step:</strong> turn this into a plan for your business. <a href="{{P}}stack-builder.html">Build your AI stack</a> in two minutes or <a href="{{P}}blueprint.html">request a free blueprint</a>.</div>
<p class="small">This guide is general information, not legal, tax or financial advice. Product names are trademarks of their owners and are mentioned for identification only. Check vendors’ current pricing and terms before buying. See our <a href="{{P}}editorial-policy.html">editorial and AI policy</a>.</p>
</div>
<aside>
<div class="panel ink"><h3>Free AI blueprint</h3><p>A written plan for your business: what to automate first, which tools, and a 30-day checklist.</p><a class="btn sig" href="{{P}}blueprint.html?from={slug}">Get mine free</a></div>
<div class="panel"><h3>Related guides</h3><ul style="padding-left:1.1rem;margin:0">{rel}</ul></div>
<div class="panel"><h3>Try the tools</h3><p class="mb0"><a href="{{P}}roi-calculator.html">ROI calculator</a><br><a href="{{P}}ai-readiness.html">Readiness score</a><br><a href="{{P}}prompts.html">Prompt library</a></p></div>
</aside>
</div>
'''
    open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"guides",slug+".html"),"w",encoding="utf-8").write(html)
