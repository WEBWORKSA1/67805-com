import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guide import guide

guide("how-to-build-an-ai-stack","How to build an AI stack for a small business",
"The layers, the order and the budget, with three example stacks you can copy.","Strategy",9,
"""
<p>Most small businesses do not have an AI problem. They have a tool-pile problem: five subscriptions bought in a burst of enthusiasm, two used once, none connected to the way work actually flows. An AI stack fixes that. It is a short list of tools, one per job, chosen in a deliberate order and connected so information moves without anyone copying and pasting.</p>
<p>This guide walks through the layers of a practical stack, the order to add them in, what a sensible budget looks like, and three example stacks for common business types.</p>

<h2>Think in layers, not apps</h2>
<p>A stack is easier to plan when you think of it as layers, each with a single job. Apps are interchangeable; layers are not. If you know which layer you are filling, you can swap one app for another later without rebuilding everything.</p>
<div class="tablewrap"><table><thead><tr><th>Layer</th><th>Job it does</th><th>Typical tools</th></tr></thead><tbody>
<tr><td>Base: assistant</td><td>Daily drafting, summarizing, thinking through problems</td><td>Claude, ChatGPT, Gemini, Microsoft Copilot</td></tr>
<tr><td>Front door</td><td>Answers customer questions and captures leads</td><td>Website chat and help-desk tools such as Tidio, Intercom or Zendesk</td></tr>
<tr><td>Memory</td><td>Holds customer, deal and project information</td><td>A CRM or shared workspace such as HubSpot or Notion</td></tr>
<tr><td>Output</td><td>Creates content, visuals, video and documents</td><td>Canva, Descript, Gamma and similar</td></tr>
<tr><td>Glue</td><td>Moves data between apps and runs workflows</td><td>Zapier, Make, n8n</td></tr>
<tr><td>Back office</td><td>Bookkeeping, receipts, invoicing, contracts</td><td>QuickBooks, Xero, Dext, e-signature tools</td></tr>
</tbody></table></div>
<p>You do not need every layer on day one. A solo consultant might run on the base layer plus a meeting recorder for a year. A 20-person e-commerce brand will want the front door and glue layers early, because that is where the repetitive hours are.</p>

<h2>The order matters more than the brand</h2>
<p>Teams that succeed with AI tend to add layers in roughly this order.</p>
<ol>
<li><strong>The assistant first.</strong> It costs little, everyone can use it, and it builds the habit of handing first drafts to AI. Give the team a shared set of prompts from day one so results are consistent. Our <a href="{P}prompts.html">prompt library</a> is a starting point.</li>
<li><strong>Then the biggest bottleneck.</strong> Look at where the most repetitive hours go. For service businesses that is usually customer questions and scheduling. For agencies it is reporting and content. For stores it is product content and support.</li>
<li><strong>Then the glue.</strong> Once two or three tools are in daily use, connect them. The glue layer is where AI moves from saving minutes to saving hours, because it removes the hand-offs between apps.</li>
<li><strong>Back office last.</strong> Finance automation pays well but carries more risk if something goes wrong, so add it once the team trusts AI output and has review habits.</li>
</ol>

<h2>How to choose a tool inside each layer</h2>
<p>For each layer, shortlist two tools and test them for two weeks on real work. Judge them on five questions:</p>
<ul>
<li><strong>Does it fit how we already work?</strong> A tool that lives inside an app you use daily beats a better tool in a separate tab.</li>
<li><strong>Can a non-technical person set it up?</strong> If only one person can maintain it, you have created a single point of failure.</li>
<li><strong>What happens to our data?</strong> Check whether your inputs are used for training, where data is stored and whether there is a business plan with stronger terms.</li>
<li><strong>Does it connect to the glue layer?</strong> A tool with no integrations becomes an island.</li>
<li><strong>What does it cost at our size in a year?</strong> Per-seat pricing grows fast. Multiply by your headcount twelve months from now.</li>
</ul>
<p>The <a href="{P}compare.html">compare page</a> lays out pricing models and fit side by side, and the <a href="{P}tools.html">directory</a> lets you filter by budget and skill level.</p>

<h2>What should an AI stack cost?</h2>
<p>For a small business, a useful rule is to keep AI software under 10% of the value of the time it saves. If the stack saves 40 hours a month and an hour is worth $40, the time is worth $1,600 a month, so up to $160 in subscriptions is easy to justify. Run your own numbers in the <a href="{P}roi-calculator.html">ROI calculator</a>.</p>
<p>Budget for setup time too. Expect 10 to 30 hours of setup and training for the first two layers. That time is the real investment, and it is the main reason stacks fail when nobody owns it.</p>

<h2>Three example stacks</h2>
<h3>Local service business (plumber, salon, clinic)</h3>
<p>Assistant for quotes and replies; a website chat tool that answers hours, prices and availability and books appointments; a review-reply prompt set; accounting software with automatic receipt capture. Biggest win: fewer phone interruptions and faster quotes.</p>
<h3>Online store</h3>
<p>Assistant for product descriptions; an image tool for product photos and backgrounds; a support chatbot grounded in shipping and returns policies; an automation that tags orders, updates the spreadsheet and sends review requests. Biggest win: support tickets answered instantly around the clock.</p>
<h3>Agency or consultancy</h3>
<p>Assistant for drafts and research; a meeting recorder that sends summaries and action items to the CRM; a presentation tool for proposals; an automation layer for client reporting. Biggest win: hours of reporting and note-taking returned to billable work.</p>

<h2>Common mistakes</h2>
<ul>
<li><strong>Buying before mapping.</strong> If you cannot name the task and the hours it takes, you cannot tell whether a tool worked.</li>
<li><strong>Rolling out to everyone at once.</strong> Start with one team and one workflow, then copy what works.</li>
<li><strong>No owner.</strong> Someone needs a few hours a week to maintain prompts, automations and access.</li>
<li><strong>No review step.</strong> Anything customer-facing or financial needs a human check until the error rate is known.</li>
</ul>
""",[("five-step-ai-automation-method","The 5-step AI automation method"),("measure-ai-roi","How to measure AI ROI"),("choosing-an-ai-assistant","Choosing an AI assistant for your team")],
[("What is the first AI tool a small business should buy?","A general AI assistant on a business plan. It is inexpensive, everyone can use it, and it builds habits that make every later tool more useful."),
 ("How many AI tools does a small business need?","Usually three to five: an assistant, one or two tools for the biggest bottleneck, an automation tool to connect them, and later a back-office tool.")])

guide("measure-ai-roi","How to measure AI ROI without fooling yourself",
"Baselines, hidden costs and the one metric that tells you whether an AI tool is paying off.","Finance",8,
"""
<p>Vendors quote dramatic productivity numbers. Your accountant wants to know whether the subscription is worth renewing. The honest answer sits between those two and you can find it with a simple method: a baseline, a pilot, and a comparison that counts every cost.</p>

<h2>Step 1: Set a baseline before you change anything</h2>
<p>Pick one workflow, for example replying to customer emails, writing weekly social posts or reconciling receipts. For one normal week, record:</p>
<ul><li>How many times the task happens</li><li>How long each takes, on average</li><li>Who does it and their loaded hourly cost (wage plus taxes and benefits)</li><li>Quality signals: errors, rework, customer complaints, response time</li></ul>
<p>A shared spreadsheet is enough. Without this baseline, every result afterwards is a guess.</p>

<h2>Step 2: Run a time-boxed pilot</h2>
<p>Use the AI tool on the same workflow for two to four weeks. Keep recording the same numbers. Expect the first week to be slower while people learn; judge the tool on weeks two to four.</p>

<h2>Step 3: Count every cost</h2>
<p>The subscription is usually the smallest cost. Include:</p>
<div class="tablewrap"><table><thead><tr><th>Cost</th><th>How to estimate</th></tr></thead><tbody>
<tr><td>Subscriptions</td><td>Seats × monthly price, at the headcount you will have in a year</td></tr>
<tr><td>Setup</td><td>Hours to configure, connect and write prompts × hourly cost</td></tr>
<tr><td>Training</td><td>Hours per person to learn the tool</td></tr>
<tr><td>Review time</td><td>Minutes spent checking AI output, per task</td></tr>
<tr><td>Maintenance</td><td>Hours per month to fix broken automations and update prompts</td></tr>
</tbody></table></div>

<h2>Step 4: Do the math</h2>
<p>The core formula is simple:</p>
<div class="callout"><strong>Monthly net savings</strong> = (hours saved per month × loaded hourly cost) − monthly tool costs − monthly review and maintenance time.<br><strong>Payback period</strong> = one-time setup cost ÷ monthly net savings.</div>
<p>Example: a support assistant cuts average reply time from 6 minutes to 2 minutes on 600 emails a month. That is 40 hours saved. At $30 an hour, $1,200 of time. Subtract $150 in subscriptions and 6 hours of review ($180), and the net is $870 a month. With 15 hours of setup ($450), payback is just over two weeks.</p>
<p>The <a href="{P}roi-calculator.html">ROI calculator</a> does this for you and shows every step.</p>

<h2>The metric that matters: where did the hours go?</h2>
<p>Saved time only becomes money when it goes somewhere useful: more sales calls, more billable work, less overtime, or a hire you can delay. If the saved time disappears into a slightly calmer week, that has value, but count it at a lower rate. Ask each person in the pilot what they did with the reclaimed time.</p>

<h2>Signals that the numbers are wrong</h2>
<ul>
<li><strong>Savings with no change in output.</strong> If the team says it is faster but nothing more gets done, re-check the baseline.</li>
<li><strong>Quality slipped.</strong> Rising complaints or rework can wipe out the time saved.</li>
<li><strong>Only one enthusiast uses it.</strong> Adoption below half the team usually means the tool does not fit the workflow.</li>
</ul>

<h2>Revenue gains are upside</h2>
<p>Faster replies can lift conversion, and better content can bring more traffic. These gains are real but hard to attribute. Keep them out of the core ROI number and report them separately, so the decision rests on what you can measure.</p>

<h2>When to cancel</h2>
<p>If after a month the net savings are negative, or adoption is under half the intended users, either fix the workflow or cancel. Sunk setup time is not a reason to keep paying.</p>
""",[("how-to-build-an-ai-stack","How to build an AI stack"),("ai-customer-support-playbook","The AI customer support playbook"),("ai-bookkeeping-admin-automation","Automating bookkeeping and admin")],
[("What is a good ROI for AI tools?","For workflow tools in a small business, aim for payback within three months and net savings at least three times the subscription cost."),
 ("How long should an AI pilot run?","Two to four weeks on one workflow. Ignore the first week, when people are still learning.")])

guide("ai-customer-support-playbook","The AI customer support playbook for small businesses",
"Automate the repeat questions, keep humans on the hard ones, and protect your reputation while you do it.","Support",9,
"""
<p>Customer support is usually the single biggest source of repetitive work in a small business. The same twenty questions arrive every week: hours, prices, shipping times, returns, how to reset a password. AI handles those well. The goal is not to remove humans from support. It is to free them for the conversations where a human makes the difference.</p>

<h2>Step 1: Sort your tickets</h2>
<p>Export or skim the last 100 to 200 customer messages and sort them into three buckets:</p>
<ul>
<li><strong>Answerable from facts:</strong> hours, prices, policies, order status. AI can answer these on its own.</li>
<li><strong>Needs judgment:</strong> refunds outside policy, complaints, custom quotes. AI can draft; a human decides.</li>
<li><strong>Needs a human:</strong> upset customers, legal or safety issues, high-value accounts. Route straight to a person.</li>
</ul>
<p>In most small businesses, the first bucket is 40 to 70 percent of volume. That is your automation target.</p>

<h2>Step 2: Write the knowledge base the AI will use</h2>
<p>An AI support agent is only as good as the information you give it. Collect your policies, prices, product details and common answers into clear, short articles. Write them in the words customers use, not internal jargon. The <a href="{P}prompts.html">prompt library</a> includes a prompt that turns your existing notes into question-and-answer pairs.</p>
<div class="callout">Rule of thumb: if a new employee could not answer the question from your knowledge base, the AI cannot either.</div>

<h2>Step 3: Choose where the AI works</h2>
<div class="tablewrap"><table><thead><tr><th>Setup</th><th>Best for</th><th>Risk</th></tr></thead><tbody>
<tr><td>Suggested replies for agents</td><td>Teams starting out, sensitive industries</td><td>Low: a human sends every reply</td></tr>
<tr><td>Website chatbot for factual questions</td><td>Stores and local services with high volume</td><td>Medium: needs good knowledge base and hand-off</td></tr>
<tr><td>Fully automated email replies</td><td>Mature teams with tested content</td><td>Higher: monitor closely</td></tr>
</tbody></table></div>
<p>Start with suggested replies or a chatbot limited to factual questions. Expand only when you have a few weeks of data showing answers are accurate.</p>

<h2>Step 4: Design the hand-off</h2>
<p>The worst support experience is a bot that will not let you reach a person. Make sure that:</p>
<ul><li>Customers can ask for a human at any point and get one.</li><li>The human sees the full conversation, so the customer does not repeat themselves.</li><li>The bot tells customers when to expect a human reply.</li><li>Certain words, such as refund, cancel, complaint or lawyer, route to a person automatically.</li></ul>

<h2>Step 5: Set guardrails</h2>
<ul>
<li>The bot must never promise refunds, discounts or delivery dates it cannot verify.</li>
<li>It must say it does not know rather than guess.</li>
<li>It must not ask for passwords or full card numbers.</li>
<li>It should state clearly that the customer is talking with an automated assistant.</li>
</ul>

<h2>Step 6: Measure weekly</h2>
<p>Track the share of conversations resolved without a human, customer satisfaction on bot conversations versus human ones, first response time, and the questions the bot failed to answer. That last list is gold: each failure is a missing knowledge-base article.</p>

<h2>What results to expect</h2>
<p>A well-set-up chatbot usually resolves a meaningful share of factual questions in the first month and improves as the knowledge base fills in. First response times drop from hours to seconds for those questions. Human agents spend their time on the complex cases, which tends to improve satisfaction scores for those conversations too.</p>
<p>Browse <a href="{P}tools.html?cat=support">customer support tools</a> to compare options.</p>
""",[("how-to-build-an-ai-stack","How to build an AI stack"),("ai-policy-for-small-business","Writing a simple AI use policy"),("ai-sales-lead-follow-up","AI for sales and lead follow-up")],
[("Will customers be annoyed by a chatbot?","They are annoyed by bots that trap them or give wrong answers. A bot that answers factual questions instantly and hands off quickly is usually welcomed."),
 ("Do I need to tell customers they are talking to AI?","It is good practice everywhere and required by law in some places. Label the assistant clearly.")])

guide("five-step-ai-automation-method","The 5-step AI automation method",
"Map the week, pick one bottleneck, choose one tool, write the playbook, measure and stack. A repeatable way to add AI without the mess.","Method",10,
"""
<p>The fastest way to waste money on AI is to start with the tools. The fastest way to get value is to start with the work. This five-step method is the backbone of everything on 67805.com. It works for a one-person business and for a team of fifty, and it keeps every AI decision tied to hours and dollars you can see.</p>

<h2>Step 1: Map the week</h2>
<p>For one normal week, list every task that repeats. Do not filter yet. Include small things: forwarding invoices, renaming files, chasing approvals, answering the same question in Slack. Next to each task, note roughly how many hours it takes per week and who does it.</p>
<p>Most teams are surprised by the total. It is common to find that a quarter or more of the working week is repetitive work.</p>
<div class="callout">Shortcut: ask each person to list their five most boring recurring tasks. That list usually covers most of the opportunity.</div>

<h2>Step 2: Pick one bottleneck</h2>
<p>Score each task on two axes: hours per week, and risk if AI gets it slightly wrong. The best first target has high hours and low risk. Drafting internal summaries is low risk. Sending invoices automatically is higher risk.</p>
<div class="tablewrap"><table><thead><tr><th></th><th>Low risk</th><th>High risk</th></tr></thead><tbody>
<tr><th>Many hours</th><td><strong>Start here.</strong> Meeting notes, first drafts, FAQ replies, social posts</td><td>Do second, with review steps. Customer emails, quotes</td></tr>
<tr><th>Few hours</th><td>Quick wins for later</td><td>Leave for now. Payments, contracts, compliance</td></tr>
</tbody></table></div>

<h2>Step 3: Choose one tool</h2>
<p>Match the task to a category in the <a href="{P}tools.html">directory</a>, shortlist two tools, and trial one for 14 days on real work. One tool, one task, one owner. Running five trials at once makes it impossible to tell what worked.</p>
<p>Check three things before you commit: data handling, whether it connects to your existing apps, and the cost at your headcount a year from now.</p>

<h2>Step 4: Write the playbook</h2>
<p>A tool without a playbook produces inconsistent results. Write down:</p>
<ul><li>The exact prompts or settings that worked</li><li>The inputs the tool needs and where they come from</li><li>The review step: who checks the output and what they check for</li><li>What to do when it fails</li></ul>
<p>Store it where the team works. This is what turns one enthusiast’s trick into a team capability.</p>

<h2>Step 5: Measure, then stack</h2>
<p>Compare the hours and quality against your baseline from step 1. If the pilot paid off, make it standard and move to the next bottleneck on your list. Each new layer builds on the last. After three or four cycles, connect the tools with an automation layer so data flows without hand-offs. That is when savings jump from minutes to hours.</p>
<p>Use the <a href="{P}roi-calculator.html">ROI calculator</a> for the measurement and the <a href="{P}stack-builder.html">stack builder</a> to plan the next layers.</p>

<h2>Worked example: a five-person marketing agency</h2>
<ol>
<li><strong>Map:</strong> the team finds 22 hours a week on client reports, 9 on meeting notes and 12 on first drafts of social posts.</li>
<li><strong>Pick:</strong> meeting notes are low risk and painful, so they go first.</li>
<li><strong>Choose:</strong> they trial a meeting recorder that sends summaries to the CRM.</li>
<li><strong>Playbook:</strong> the account lead reviews each summary before it goes to the client.</li>
<li><strong>Measure:</strong> note-taking drops from 9 hours to about 2. They move on to social drafts, then to automating report data collection.</li>
</ol>

<h2>Why the order matters</h2>
<p>Each step protects against a common failure. Mapping prevents buying tools for problems you do not have. Picking one bottleneck prevents scattered pilots. One tool at a time makes results measurable. The playbook makes results repeatable. Measuring keeps everyone honest about what is worth paying for.</p>
""",[("how-to-build-an-ai-stack","How to build an AI stack"),("measure-ai-roi","How to measure AI ROI"),("prompt-writing-for-business-teams","Prompt writing for business teams")],
[("How long does the 5-step method take?","A first cycle takes about three to five weeks: one week to map and pick, two to four weeks to pilot and measure."),
 ("Do I need technical skills?","No. Steps one to four need no technical skills. Connecting tools in later cycles is easier with no-code automation tools.")])

guide("ai-marketing-content-workflow","An AI content workflow that does not sound like AI",
"How to use AI to plan, draft and repurpose marketing content while keeping your voice and your facts.","Marketing",8,
"""
<p>AI can cut content production time dramatically. It can also flood your channels with bland, interchangeable posts that readers skip. The difference is workflow. Used as a first-draft engine inside a clear process, with your expertise feeding it, AI helps you publish more of what only you can say.</p>

<h2>The workflow at a glance</h2>
<ol>
<li><strong>Capture raw material</strong> that only you have.</li>
<li><strong>Plan</strong> topics around real customer questions.</li>
<li><strong>Draft</strong> with AI, using your material as the source.</li>
<li><strong>Edit</strong> for voice, accuracy and a clear point of view.</li>
<li><strong>Repurpose</strong> one piece into many formats.</li>
<li><strong>Measure</strong> and feed the results back into planning.</li>
</ol>

<h2>1. Capture raw material</h2>
<p>Generic input produces generic output. Feed AI things it cannot find elsewhere: recordings of sales calls, answers you gave customers, notes from projects, your opinions on industry trends. A ten-minute voice memo about a client problem you solved contains more original material than any keyword list.</p>

<h2>2. Plan from real questions</h2>
<p>Collect the questions customers ask in emails, calls and reviews. Group them into themes, then ask an AI assistant to turn each theme into article, video and social ideas. Add search data from an SEO tool to prioritize topics people actively look for.</p>

<h2>3. Draft with your material as the source</h2>
<p>Give the assistant your notes or transcript and tell it to use only that material. Ask for a structure first, approve it, then ask for the draft. Constraints help: word limits, reading level, phrases to avoid, and an instruction to mark anything it is unsure of.</p>
<div class="callout">Useful instruction: “Use only the facts in my notes. Where you need a fact that is not there, write [NEEDS SOURCE] instead of inventing one.”</div>

<h2>4. Edit like a human</h2>
<p>This is where your brand is protected. In each draft:</p>
<ul><li>Cut the first paragraph if it only warms up.</li><li>Add one specific example, number or story from your experience.</li><li>Take a clear position. Bland balance reads as filler.</li><li>Check every fact, name and statistic.</li><li>Read it aloud. Rewrite anything you would not say to a customer.</li></ul>

<h2>5. Repurpose one piece into ten</h2>
<p>A single strong article or video can become a newsletter section, three short social posts, two short-video scripts, a carousel and a quote graphic. AI does this conversion well because the ideas and facts are already approved. The <a href="{P}prompts.html">prompt library</a> includes a repurposing prompt.</p>

<h2>6. Measure what matters</h2>
<p>Track the content that produces leads and replies, not just views. Each month, ask which pieces drove inquiries, and plan more of those. Over time this loop matters more than any tool.</p>

<h2>Tools for each step</h2>
<div class="tablewrap"><table><thead><tr><th>Step</th><th>Tool type</th><th>Examples</th></tr></thead><tbody>
<tr><td>Capture</td><td>Recording and transcription</td><td>Descript, Otter.ai, Fathom</td></tr>
<tr><td>Plan</td><td>Assistant and SEO research</td><td>Claude, ChatGPT, Semrush, Ahrefs</td></tr>
<tr><td>Draft and edit</td><td>Assistant and editing</td><td>Claude, ChatGPT, Grammarly</td></tr>
<tr><td>Visuals</td><td>Design and video</td><td>Canva, CapCut, OpusClip</td></tr>
<tr><td>Distribute</td><td>Scheduling</td><td>Buffer, Hootsuite</td></tr>
</tbody></table></div>

<h2>A note on search</h2>
<p>Search engines reward content that is helpful, original and written for people, however it is produced. Mass-produced pages with no original value are a risk. Use AI to publish better content faster, not to publish more thin pages.</p>
""",[("prompt-writing-for-business-teams","Prompt writing for business teams"),("how-to-build-an-ai-stack","How to build an AI stack"),("ai-sales-lead-follow-up","AI for sales and lead follow-up")])
print("a done")
