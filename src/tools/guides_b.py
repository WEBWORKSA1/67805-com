import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guide import guide

guide("ai-bookkeeping-admin-automation","Automating bookkeeping and admin with AI, safely",
"Which back-office tasks AI handles well, where to keep a human check, and how to set it up without risking your books.","Finance",8,
"""
<p>Admin is the work that keeps a business legal and paid: receipts, invoices, reconciliations, payroll inputs, reminders. It is also the work owners most want gone. AI and automation can take a large share of it, but finance is where mistakes cost real money, so the setup needs more care than a content workflow.</p>

<h2>What AI handles well in the back office</h2>
<div class="tablewrap"><table><thead><tr><th>Task</th><th>How AI helps</th><th>Human check</th></tr></thead><tbody>
<tr><td>Receipt and invoice capture</td><td>Reads documents and extracts supplier, date, amount and tax</td><td>Spot-check a sample weekly</td></tr>
<tr><td>Transaction categorization</td><td>Suggests categories from past patterns</td><td>Review new or unusual items</td></tr>
<tr><td>Invoice reminders</td><td>Sends scheduled, polite reminders</td><td>Approve the templates once</td></tr>
<tr><td>Expense policy checks</td><td>Flags out-of-policy spending</td><td>Decide on each flag</td></tr>
<tr><td>Cash-flow summaries</td><td>Explains changes in plain English</td><td>Confirm with your accountant</td></tr>
</tbody></table></div>

<h2>What to keep human</h2>
<ul><li>Approving payments and transfers</li><li>Tax positions and filings</li><li>Payroll changes</li><li>Anything involving a legal or regulatory judgment</li></ul>
<p>AI can prepare these, summarize them and flag issues. A qualified person should make the decision.</p>

<h2>A safe setup in five moves</h2>
<ol>
<li><strong>Start inside your accounting software.</strong> Modern accounting platforms include AI categorization and document capture. Using built-in features keeps data in one system with its existing audit trail.</li>
<li><strong>Add document capture.</strong> Route receipts and supplier invoices to a capture tool by email forwarding or photo upload.</li>
<li><strong>Automate reminders.</strong> Set up a reminder ladder for overdue invoices: friendly at 3 days, firm at 14, final at 30. The <a href="{P}prompts.html">prompt library</a> has a template.</li>
<li><strong>Use an assistant for explanations, not entries.</strong> Paste a monthly summary into an AI assistant and ask it to explain what changed and what to ask your accountant. Do not paste bank account numbers or full customer details.</li>
<li><strong>Review weekly.</strong> Fifteen minutes a week checking flagged items and a sample of automated entries keeps errors from compounding.</li>
</ol>

<h2>Data security basics</h2>
<ul><li>Use business plans of AI tools, which typically offer stronger data terms.</li><li>Turn on two-factor authentication everywhere financial data lives.</li><li>Limit who can connect apps to your accounting system.</li><li>Keep an up-to-date list of every integration with access to financial data.</li></ul>

<h2>What to expect</h2>
<p>Businesses that move receipt capture and categorization into automated flows often cut monthly bookkeeping time substantially and close their books faster. The bigger benefit is often visibility: up-to-date numbers every week instead of a scramble at month end.</p>
<p>Explore <a href="{P}tools.html?cat=fin">finance and admin tools</a>, or estimate savings with the <a href="{P}roi-calculator.html">ROI calculator</a>.</p>
""",[("measure-ai-roi","How to measure AI ROI"),("ai-policy-for-small-business","Writing a simple AI use policy"),("five-step-ai-automation-method","The 5-step method")],
[("Can AI replace my bookkeeper?","It can remove much of the data entry, but you still need a qualified person for review, judgment and tax matters. Most businesses use AI to make their bookkeeper faster."),
 ("Is it safe to paste financial data into an AI assistant?","Summaries and anonymized figures are generally fine on business plans. Never paste account numbers, passwords or full customer details.")])

guide("prompt-writing-for-business-teams","Prompt writing for business teams: a practical guide",
"A simple four-part pattern, the constraints that remove filler, and how to build a shared prompt library your team will use.","Skills",8,
"""
<p>The quality gap between people who get great results from AI and people who give up is rarely the tool. It is the prompt. The good news: writing effective prompts is a learnable business skill, closer to writing a clear brief for a freelancer than to programming.</p>

<h2>The four-part pattern</h2>
<ol>
<li><strong>Role:</strong> who the AI should act as. “You are an experienced B2B copywriter.”</li>
<li><strong>Context:</strong> who you are, who the audience is, what good looks like. Paste source material here.</li>
<li><strong>Task:</strong> one clear job. “Write three subject lines for this email.”</li>
<li><strong>Format:</strong> length, structure, tone. “Under 60 characters each, as a numbered list.”</li>
</ol>
<p>Most weak prompts skip context. The AI fills the gap with generic assumptions, and the output reads generic.</p>

<h2>Constraints that remove filler</h2>
<ul>
<li><strong>Length limits.</strong> “Under 120 words” forces focus.</li>
<li><strong>Banned words.</strong> List the clichés you never want to see.</li>
<li><strong>Source limits.</strong> “Use only the facts below” reduces invented details.</li>
<li><strong>Uncertainty flags.</strong> “If you are unsure, say so” makes errors visible.</li>
<li><strong>Options.</strong> “Give three versions” is faster than editing one.</li>
</ul>

<h2>Iterate like an editor</h2>
<p>Treat the first answer as a draft. Give specific feedback: “Shorter. More direct. Replace the second paragraph with a customer example.” Two or three rounds usually beat starting over. When you find a prompt that works, save it.</p>

<h2>Build a shared prompt library</h2>
<p>A team prompt library turns individual tricks into consistent results. Keep it simple:</p>
<div class="tablewrap"><table><thead><tr><th>Field</th><th>Example</th></tr></thead><tbody>
<tr><td>Name</td><td>Follow-up after no reply</td></tr>
<tr><td>Use when</td><td>A prospect has not replied for 5+ days</td></tr>
<tr><td>Prompt</td><td>The full text with [brackets] for variables</td></tr>
<tr><td>Owner</td><td>Who maintains it</td></tr>
<tr><td>Last tested</td><td>Date and tool</td></tr>
</tbody></table></div>
<p>Our free <a href="{P}prompts.html">prompt library</a> has 30 starting points organized by team.</p>

<h2>Examples: before and after</h2>
<h3>Weak</h3>
<p><em>“Write a post about our new service.”</em></p>
<h3>Strong</h3>
<p><em>“You are a social media manager for a family-owned HVAC company in a mid-size city. Our audience is homeowners aged 35–65. We just launched same-day furnace repair with a 2-hour arrival window. Write three Facebook posts under 80 words each. Lead with the customer’s problem, not our name. No exclamation marks. End each with a question that invites comments.”</em></p>

<h2>Common mistakes</h2>
<ul><li>Asking for everything in one prompt. Split big jobs into steps.</li><li>Accepting the first answer.</li><li>Pasting sensitive data into tools without approved data terms.</li><li>Not saving what works.</li></ul>
""",[("ai-marketing-content-workflow","An AI content workflow"),("choosing-an-ai-assistant","Choosing an AI assistant"),("ai-policy-for-small-business","Writing a simple AI use policy")])

guide("ai-policy-for-small-business","How to write a simple AI use policy for a small business",
"One page that tells your team which tools are approved, what data never goes in, and when a human must review the output.","Risk",8,
"""
<p>Your team is probably already using AI tools, approved or not. A short AI use policy does not slow that down. It makes it safe, so you can encourage more of it. You do not need a lawyer to write a first version, though you should ask one to review it if you handle regulated data such as health or financial records.</p>

<h2>What the policy should cover</h2>
<ol>
<li><strong>Purpose:</strong> one sentence on why you use AI and what you expect from it.</li>
<li><strong>Approved tools:</strong> the list of tools and plans staff may use for work.</li>
<li><strong>Data rules:</strong> what may and may not be entered into AI tools.</li>
<li><strong>Review rules:</strong> which outputs need human review before use.</li>
<li><strong>Disclosure:</strong> when to tell customers AI was involved.</li>
<li><strong>Ownership:</strong> who to ask, and who maintains the policy.</li>
</ol>

<h2>Data rules: a simple traffic light</h2>
<div class="tablewrap"><table><thead><tr><th>Level</th><th>Examples</th><th>Rule</th></tr></thead><tbody>
<tr><td>Green</td><td>Public information, marketing drafts, general questions</td><td>Fine in any approved tool</td></tr>
<tr><td>Amber</td><td>Internal documents, anonymized customer feedback, financial summaries</td><td>Only in approved tools on business plans</td></tr>
<tr><td>Red</td><td>Passwords, card and bank numbers, ID numbers, health data, confidential client files</td><td>Never, unless a specific tool has been approved for it in writing</td></tr>
</tbody></table></div>

<h2>Review rules</h2>
<p>Require a human check before AI output is used for anything that is customer-facing, legal, financial, published under your brand, or used to make decisions about people, such as hiring. Internal drafts and summaries can be lighter-touch.</p>

<h2>Disclosure</h2>
<p>Tell customers when they are talking to an automated assistant. Some places have laws about disclosing AI-generated content or automated decisions, so check the rules where you operate.</p>

<h2>A one-page template</h2>
<div class="callout">
<p><strong>[Company] AI use policy</strong> (version 1, [date])</p>
<p><strong>Why:</strong> We use AI to save time on routine work so we can spend more time with customers. People remain responsible for everything we send and publish.</p>
<p><strong>Approved tools:</strong> [list tools and plans].</p>
<p><strong>Never enter:</strong> passwords, payment or bank details, ID numbers, health information or confidential client files.</p>
<p><strong>Always review:</strong> anything sent to customers, published, financial or legal, and anything about hiring or staff.</p>
<p><strong>Be open:</strong> label chatbots as automated; do not present AI output as a personal statement from a named person without their review.</p>
<p><strong>Questions:</strong> ask [owner]. This policy is reviewed every six months.</p>
</div>

<h2>Rolling it out</h2>
<ul><li>Share it in a 20-minute team meeting with examples.</li><li>Put it where people work, not in a forgotten folder.</li><li>Pair it with approved prompts from your <a href="{P}prompts.html">prompt library</a>.</li><li>Review it every six months, because tools and laws change fast.</li></ul>
""",[("ai-customer-support-playbook","The AI customer support playbook"),("prompt-writing-for-business-teams","Prompt writing for business teams"),("choosing-an-ai-assistant","Choosing an AI assistant")],
[("Does a small business need an AI policy?","If anyone on the team uses AI tools for work, yes. A one-page policy prevents the most common risk: sensitive data pasted into tools without proper data terms.")])

guide("choosing-an-ai-assistant","Choosing an AI assistant for your team",
"How to decide between general assistants such as ChatGPT, Claude, Gemini and Microsoft Copilot, using criteria that will still matter after the next update.","Strategy",8,
"""
<p>The base layer of every AI stack is a general assistant. The leading options update constantly, so any feature-by-feature comparison is out of date within weeks. A better approach is to choose using criteria that stay stable, then run a short trial on your own work.</p>

<h2>The main options</h2>
<ul>
<li><strong>ChatGPT</strong> (OpenAI): a broad, popular assistant with a large ecosystem of features and integrations.</li>
<li><strong>Claude</strong> (Anthropic): an assistant with a reputation for long documents, careful writing and coding help.</li>
<li><strong>Gemini</strong> (Google): an assistant closely tied to Gmail, Docs, Drive and the rest of Google Workspace.</li>
<li><strong>Microsoft Copilot:</strong> an assistant built into Word, Excel, Outlook and Teams for Microsoft 365 users.</li>
</ul>
<p>All four are capable. The right one depends more on how your business works than on benchmark scores.</p>

<h2>Five criteria that still matter next year</h2>
<h3>1. Where your work already lives</h3>
<p>If your team lives in Google Workspace, Gemini’s integration is a real advantage. If you run on Microsoft 365, Copilot sits inside the apps you use all day. If your tools are mixed, a standalone assistant that connects to many services may suit you better.</p>
<h3>2. The work you do most</h3>
<p>Test on your actual tasks: long contracts, client emails, data in spreadsheets, code, images. Quality differences show up quickly on real work and rarely show in marketing pages.</p>
<h3>3. Data terms for business</h3>
<p>Check the business or team plans for how your inputs are handled, admin controls, and where data is stored. Consumer plans and business plans often have different terms.</p>
<h3>4. Admin and sharing</h3>
<p>For teams, look at shared workspaces or projects, user management, single sign-on and the ability to share prompts and documents.</p>
<h3>5. Total cost</h3>
<p>Multiply the per-seat price by the number of people who will genuinely use it. Not everyone needs a paid seat on day one.</p>

<h2>Run a fair two-week trial</h2>
<ol>
<li>Pick five real tasks your team does every week.</li>
<li>Write one prompt per task and run it in two assistants.</li>
<li>Have the people who do that work rate the outputs blind, without knowing which tool produced which.</li>
<li>Note time saved and how much editing each output needed.</li>
<li>Choose the winner for the base layer. You can still use others for specific jobs.</li>
</ol>

<h2>Should you use more than one?</h2>
<p>Many teams standardize on one assistant for everyday work and allow a second for specialist tasks. That keeps training and billing simple while leaving room for the best tool per job.</p>
<p>See them side by side on the <a href="{P}compare.html?t=ChatGPT|Claude|Gemini">compare page</a>.</p>
""",[("how-to-build-an-ai-stack","How to build an AI stack"),("prompt-writing-for-business-teams","Prompt writing for business teams"),("ai-policy-for-small-business","Writing a simple AI use policy")])

guide("ai-sales-lead-follow-up","AI for sales: faster lead follow-up without sounding robotic",
"Speed-to-lead, research, personalized outreach and call notes. Where AI helps sales teams most, and where it hurts.","Sales",8,
"""
<p>In sales, the business that replies first often wins. AI helps small teams respond faster, research prospects in minutes instead of hours, and keep the CRM up to date without anyone typing notes after every call. Misused, it produces mass outreach that damages your reputation. Here is how to get the first without the second.</p>

<h2>1. Speed to lead</h2>
<p>When someone fills in a form on your site, every minute counts. Set up an automation that:</p>
<ul><li>Sends an immediate, personal-sounding confirmation with the next step</li><li>Creates or updates the contact in your CRM</li><li>Alerts the right salesperson with a short AI summary of the inquiry</li><li>Books a call through a scheduling link</li></ul>
<p>This alone often lifts conversion, because the lead hears back while still interested.</p>

<h2>2. Research in minutes</h2>
<p>Before a call, use an AI assistant or research tool to summarize the prospect’s business, recent news and likely priorities. Ask for likely pain points and questions to ask. Verify anything you plan to mention; AI can confuse companies with similar names.</p>

<h2>3. Personalized outreach, at human scale</h2>
<p>AI can draft personalized emails, but personalization only works if it is real. A good rule: each email must reference something specific and true about the recipient, and a person must read it before it is sent. Send fewer, better emails. Bulk unsolicited messages also carry legal requirements in many countries, so follow the rules where you operate.</p>

<h2>4. Call notes that write themselves</h2>
<p>Meeting recorders can transcribe calls, summarize them, extract next steps and push them into the CRM. Tell participants the call is being recorded and follow local consent rules.</p>

<h2>5. Pipeline hygiene</h2>
<p>Use AI to flag deals with no activity for two weeks, draft follow-ups for stalled deals, and summarize the pipeline weekly for the owner.</p>

<h2>Where AI hurts sales</h2>
<ul><li>Fully automated cold outreach at volume: it burns your domain reputation and brand.</li><li>Fake familiarity: “I loved your recent post” when nobody read it.</li><li>Unchecked facts about the prospect.</li></ul>

<h2>A simple sales stack</h2>
<div class="tablewrap"><table><thead><tr><th>Job</th><th>Tool type</th><th>Examples</th></tr></thead><tbody>
<tr><td>CRM with AI features</td><td>Customer records and pipeline</td><td>HubSpot</td></tr>
<tr><td>Prospect data</td><td>Contact and company enrichment</td><td>Apollo.io, Clay</td></tr>
<tr><td>Email coaching</td><td>Writing feedback</td><td>Lavender</td></tr>
<tr><td>Call notes</td><td>Recording and summaries</td><td>Fathom, Fireflies.ai</td></tr>
<tr><td>Glue</td><td>Automations</td><td>Zapier, Make</td></tr>
</tbody></table></div>
<p>Compare options in the <a href="{P}tools.html?cat=sales">sales and outreach</a> category.</p>
""",[("ai-customer-support-playbook","The AI customer support playbook"),("five-step-ai-automation-method","The 5-step method"),("measure-ai-roi","How to measure AI ROI")],
[("Is it legal to send AI-written sales emails?","Who writes the email does not change the rules. Commercial email laws such as CAN-SPAM in the US, CASL in Canada and GDPR rules in Europe still apply, including consent and unsubscribe requirements.")])
print("b done")
