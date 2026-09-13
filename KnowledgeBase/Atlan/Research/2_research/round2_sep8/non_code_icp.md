# Non-code skill builders: sales, marketing, pre-sales, ops
Research run 2026-09-08, testing the Atlan CEO's signal that registry usage is driven by people
working on things EXTREMELY UNIQUE TO THE COMPANY - marketing, sales, pre-sales - not only coding.

## THE HEADLINE NUMBER THAT VALIDATES THE CEO
Anthropic's own Claude Cowork usage data, reported 7 Jul 2026:
  91.3% OF COWORK USAGE IS NON-CODING. Software development is 8.7%.
  Business process & operations 33.4% | Content creation & copywriting 16.4% | DevOps 7.0% |
  Research & intelligence 6.4% | Data analysis & BI 5.8% | Document processing 4.1% |
  SALES & REVENUE OPS 4.0% | Personal assistance 3.8%
  Anthropic's framing: "People are using it for a variety of tasks that aren't necessarily the
  hallmark of a specific role, but instead represent the connective work around a role."
  [verified] venturebeat.com/technology/anthropic-brings-claude-cowork-to-mobile-and-web-...
USABLE FRAMING: engineering leads on SPEND, but on AGENT USAGE engineering is a rounding error.
The people generating 91% of the volume have none of the governance infrastructure engineering
built for itself (git, PR review, CI, code owners).

Corroborating spend view - Menlo Ventures, State of GenAI in the Enterprise, Dec 2025:
departmental AI spend $7.3B, up 4.1x YoY. Coding $4.0B (55%) | IT Ops $700M (10%) |
MARKETING $660M (9%) | Customer Success $630M (9%) | Design ~7% | HR ~5%. Sales is not broken out.
Marketing is the #1 non-technical function; marketing+design (~$1.15B) is the #2 cluster. [verified]
Anthropic Economic Index Mar 2026: coding 35% of Claude.ai conversations; management occupations
rose 3% -> 5%; "sales enablement and lead qualification workflows showed at least 2x growth." [verified]
WRITER 2026 survey: "11% of super-users have built their own AI agents, tools, or workflows";
"75% of executives admit their AI strategy is 'more for show' than actual guidance." [reported]

## SEGMENT 1 - GTM ENGINEERS / REVOPS / SALES ENABLEMENT. STRONGEST.
### Hard proof they build skills as reusable artifacts [verified, GitHub API]
| Repo | Author | Metrics | Contents |
|---|---|---|---|
| coreyhaines31/marketingskills | Corey Haines (Conversion Factory, Swipe Files) | 44,769 STARS, 7,026 FORKS, 391 watchers. Created 15 Jan 2026, updated 18 Aug 2026 | 58 marketing skills: CRO, copywriting, SEO, ads, ad-creative, analytics, A/B testing, churn, pricing, sales enablement, revops |
| Cold-IQ/ColdIQ-s-GTM-Skills | Sacha, ColdIQ | 269 stars, 85 forks | 6 master + 43 sub-skills + 31 standalone: 137 sales triggers, 34 email templates, 11 GTM plays, Clay enrichment |
| manojbajaj95/claude-gtm-plugin | Manoj Bajaj | - | 166 skills: SEO, outbound, CRM, ads, analytics |
| getaero-io/gtm-eng-skills | Aero | - | waterfall email enrichment, TAM building, signal discovery, job-change detection |
| GTM Agents | - | ~96 stars | 92 agents + 52 skills |

*** THE SINGLE MOST ON-THESIS FACT IN THE WHOLE RESEARCH ***
The marketingskills README says its skills reference "a foundational product-marketing context file
that other skills check first, allowing you to customize agent behavior based on your company's
unique positioning, audience, and product details" - and offers "Fork and customize" as the official
install path. 7,026 FORKS = 7,026 PEOPLE WHO TOOK A GENERIC SKILL LIBRARY AND PRIVATELY OVERWROTE IT
WITH THEIR OWN COMPANY'S CONTEXT. That fork count IS the CEO's "unique to the company" insight,
quantified, in public, with names attached. [verified]

### Role size
GTME Pulse, Mar 2026 (3,342 postings analysed + n=228 survey, 32 countries): "3,000+ open roles",
205% YoY growth 2024->2025, Dec 2025 the single biggest monthly spike. Median salary $132K;
senior/lead $180-250K+. 69% OF GTM ENGINEER POSTINGS MENTION CLAY, ~40% Apollo, 35% HubSpot. [reported]
Apollo people-database, live query 8 Sep 2026: 1,918 people hold the exact title "GTM Engineer";
546 companies currently hiring one. [verified]
Clay raised $100M Series C at $3.1B, Aug 2025, explicitly framed as fuelling GTM Engineering roles. [verified]

### Their stack and their AI adoption [reported, n=228]
"71% AI coding tool adoption. Cursor and Claude Code lead."
"Claude cited as the most exciting tool (39 mentions). Followed by Cursor (11) and n8n (8)."
State of GTM Engineering 2026: "GTM Engineering is becoming increasingly self-made, with engineers
building their own solutions using tools like Claude Code to move faster and stay autonomous" and
"tools won't be the bottleneck. Well-structured, retrieval-ready context" is what matters.

### The breakdown they describe
- TEAM-OF-ONE IS STRUCTURAL, not incidental. Maja Voje, 6 Mar 2026, n=228, 30+ countries: "most GTM
  Engineers operate as a team of one, responsible for designing automation systems, maintaining the
  data layer, supporting sales workflows." Only 45% say their org clearly understands what they do.
  Bandwidth is the #1 bottleneck (25%). [reported]
- NO AUDIT: "nobody planned the end state, nobody got buy-in, and nobody's auditing what's actually
  running." [reported, yourmarketingminds.com on why Clay workflows fail]
- NAMED FAILURE MODES, GTME Pulse: "Trigger collisions. Two skills have overlapping triggers and the
  agent picks the wrong one." / "Stale instructions. A skill was written when the CRM had different
  field names. The CRM changed. The skill silently fails or writes to the wrong field."
  Their prescribed fix is literally a registry: "Version history on every skill (who changed what,
  when). Code review on changes (a new skill or a tweak goes through a PR like any other code)." [reported]
- "Personal skills in ~/.claude/skills/ only work for you." [reported, agensi.io 7 May 2026]
- "Integration issues are the top frustration."

### Named practitioners with documented builds [reported, The Signal, 15 Apr 2026]
- Eric Fitz, AE at Zendesk - built "Zendesk Sales Brain", a Claude Skill on the company Help Center;
  used it across his 1,800 accounts; 99.8% deliverability across ~5,000 emails.
- Josh Nelson, RevOps/GTM Eng at Nooks - "drowning in ad hoc data requests"; DIY Postgres warehouse
  with ETL from HubSpot, Mixpanel, product DB, ChiliPiper, Subskribe.
- Sam Gong, SVP Marketing at WorkSpan - "I would not have bought this tool without the MCP."
  (direct willingness-to-pay attributed to the context layer)
- Jiquan Ngiam, CEO MintMCP - "1-to-5 human-to-agent ratio across entire business", 25 agents.
- Anis Bennaceur, CEO Attention - "your best messaging is not written, it's found."

### Where they congregate [verified sizes]
Clay Community 30,000+ active, "new posts every 10 minutes, even during holidays", with a DEDICATED
private #GTM-engineering channel | RevGenius 60,000+ Slack | Modern Sales Pros 35,000+ |
RevOps Co-op 19,000+ Slack | Sales Assembly 6,000+ | Pavilion 5,000+ | MarketingOps.com 3,500+ |
Revenue Operations Alliance 3,000+ | Wizards of Ops (private) | Claymation newsletter 6,000+ subs |
r/gtmengineering ~1,000
CAUTION: Clay's GTM-engineering channel enforces "Business & Systems Only", "High Signal, No Noise",
explicitly prohibiting "spam, personal advertisements, or self-promotion." Contribution-first only.

### Reachability: VERY HIGH. Aggressively public and named.
Corey Haines, Sacha/ColdIQ, Manoj Bajaj, Maja Voje, Brendan Short, Alex Lindahl all publish under
real names with newsletters and public repos. Fork lists, stargazers and issue threads are
enumerable via the GitHub API. Maja Voje's LinkedIn post about GTM Claude Code skills reportedly
drew 1,500 people asking for them. [reported]

### What they already pay for [reported]
GTM engineering agency retainers median $5-8K/mo, range $1-33K. Clay builds $2-5K/mo; managed
outbound $5-10K/mo; full-stack GTM $10-20K/mo; advisory $200-400/hr. 55% of agency GTM engineers
spend $5-25K/yr on tools; agency operators run 6-8 tools vs 4-5 in-house.

## SEGMENT 2 - PERFORMANCE MARKETING / CREATIVE OPS. HIGH ACTIVITY, LOW PUBLIC FOOTPRINT.
Higgsfield ships an official MCP for Claude/ChatGPT; marketers generate "UGC-style product videos,
static visuals, talking avatars, and voiceovers" and "ad creatives directly from a Claude or ChatGPT
chat" (17 Aug 2026). [verified] Adobe shipped a GenStudio Performance Marketing MCP server. [verified]
`ad-creative` is a first-class skill in the 44.8k-star marketingskills repo. [verified]
Volume: We Are Amnet 2026 Industry Voices (~8 senior in-house production leads) - Kerry Matto,
Just Eat Takeaway: "On average we have around 2000 briefs a year" / "172 briefs a month" /
"you need systems that are simple to use where data can be easily uploaded." Report: fewer than 30%
of orgs have internal expertise to evaluate/govern AI effectively; only 36% of employees received
training; pain named as "inconsistency and approval delays without clear AI governance" and "teams
adopting AI through trial-and-error rather than structured training." [reported]
Creative testing velocity: 2-6 iterations/month -> 10-20 with AI. [reported]

*** HONEST NULL RESULT ***
Not one verbatim quote from a NAMED performance marketer describing a skill-governance failure.
The flagship Higgsfield MCP article contains ZERO mentions of teams, sharing, standardization or
handoff - it is entirely single-user framed. [verified null] No creative-ops community with a
published member count is findable; nearest hub is Motion (motionapp.com) with no disclosed size.
INTERPRETATION: they build heavily but PRIVATELY, inside agencies, under NDA, and don't publish to
GitHub. Hard to reach at zero budget and hard to evidence. Real strike against this segment as the
PRIMARY, even though the underlying pain is probably severe. This matches Manan's own marketing user.

## SEGMENT 3 - PRE-SALES / SOLUTIONS CONSULTING. NEAR-NULL.
Community is large and defined: PreSales Collective Slack = "15,000+ presales pros". [verified]
PSC publishes AI content, so the topic is live. BUT: no evidence of pre-sales professionals building
or publishing custom agent skills as artifacts. No repos of demo-script / discovery-framework /
POC-plan skills. No named SE describing an encoded playbook. No AI channel in PSC's channel list.
The AI conversation in presales is entirely VENDOR-MEDIATED - AutoRFP.ai, Iris AI, Arphie,
Inventive.ai, Vendict, Navattic do it FOR you. [verified null]
INTERPRETATION: presales has the MOST company-unique content (your demo, your security posture, your
RFP answers) and the LEAST DIY skill-building culture. They buy RFP-automation SaaS. Reachable, but
we would be creating the category rather than meeting demand.

## SEGMENT 4 - OPS / FINANCE / LEGAL / HR. BEST-DOCUMENTED PAIN, LOWEST VOLUME.
*** THE BEST EVIDENCE IN THE WHOLE RESEARCH, AND IT COMES FROM INSIDE ANTHROPIC ***
Anthropic's finance team runs ~150 SHARED CLAUDE SKILLS (from Anthropic webinar "How Finance Teams
Use Claude Cowork", Jun 2026; Tim Ross, Finance AI Product Lead, and Lisa To, Head of Finance
Systems). [verified via cfoconnect.eu]
- "Domain experts - accountants and FP&A analysts - write the skills themselves, not IT."
- Tim Ross: "Your best preparer writes the procedure down once in plain language and it runs the
  same way for everyone, every time."  <- one person's play, encoded and transferred, stated exactly
- THE REGISTRY QUOTE: skills are "stored in a GitHub repo and distributed as workspace plugins
  available to every finance team member" and "SKILLS ARE VERSIONED, NOT LOST WHEN SOMEBODY MOVES ON."
  <- the Atlan pitch, articulated by the customer, about a NON-CODE team
- Use cases: AR sub-ledger->GL reconciliation, FP&A reporting, ERP migration validation
  (20 SECONDS VS HUNDREDS OF HOURS), master data governance.

Anthropic, "Deploying Claude Across Your Organization" PDF, 29 Apr 2026: [verified, primary]
- LEGAL: one markdown Legal plugin, "built by product lawyer in an afternoon using existing memos,
  risk frameworks, policy documents - no engineering required", with "The Legal Constitution baked in."
- SALES: five core skills (morning briefing, call prep, post-call follow-up, competitive intel, asset
  creation). "INDIVIDUAL REPS ALSO AUTHOR CUSTOM SKILLS" - one rep built an auto-updating Salesforce
  skill. Individual skill authorship inside a sales org, at Anthropic.
- FINANCE: "Development velocity moved from weeks to hours. Non-technical team members build
  interactive dashboards without filing a ticket."

Enterprise governance gap: SAP News 3 Aug 2026 - "98% of companies have already deployed AI agents or
plan to"; LESS THAN HALF have visibility into their AI agent inventory. Gartner: "By 2028, the
average global Fortune 500 enterprise will have more than 150,000 AI agents in use, yet only 13% of
organizations believe they have the right governance in place." SAP CTO Philipp Herzig: "Almost no
one has a consistent picture - no central governance, no clear view of what each agent does." [reported]
Correlation One, State of AI Enablement 2026: "Enterprises typically hold 2-3x more AI licenses than
trained, active users." Case: a multinational airline group where "40 non-technical employees built
11 production AI agents in seven weeks", one saving ~80 hours/month. [reported]

Named non-engineer skill creators (39 skills, 23 creators, Jan 2026 roundup):
Daria Cupareanu (content) "Every time you write a newsletter, you paste the same instructions to
Claude." | Zain Haseeb (biz ops) | Alex Willen (e-comm ops, 9 brands).
CAVEAT [verified]: NONE of these 23 mentioned sharing or versioning pain. They describe the AUTHORING
problem, not yet the GOVERNANCE problem.

SUPPORT ENABLEMENT: null. Only vendor product pages. [verified null]

## RANKING
| | Segment | Pain intensity | Volume of skill creation | Zero-budget reachability | Genuinely company-unique | Overall |
|---|---|---|---|---|---|---|
| 1 | GTM eng / RevOps / sales enablement | High - team-of-one structural, trigger collisions, stale CRM fields, nobody auditing | VERY HIGH - 44.8k stars / 7k forks, 5+ public repos, 71% AI adoption | VERY HIGH - named, loud, GitHub+LinkedIn+Substack; 30k Clay + 60k RevGenius | High - ICP, verbiage, triggers, CRM schema all bespoke | #1 |
| 2 | Ops / finance / legal / HR | HIGHEST and best-articulated - "versioned, not lost when somebody moves on"; 150 skills at Anthropic finance | Medium, concentrated in few sophisticated orgs | LOW-MED - surfaced via vendor webinars, practitioners don't post | HIGHEST - close process, legal constitution, comp bands | #2 |
| 3 | Performance marketing / creative ops | Probably high, UNDOCUMENTED publicly | High activity, near-zero public artifacts | LOW - no sized community, work is inside agencies | Med-high - brand voice, offer library, winning hooks | #3 |
| 4 | Pre-sales / solutions consulting | Medium, being absorbed by RFP SaaS | NEAR ZERO public | Med-high - 15k PSC Slack, named SEs | HIGHEST but they BUY rather than build | #4 |

WHY #1 AND #2 DIFFER IN KIND: GTM engineers give VOLUME AND ACCESS. Finance/legal give THE LANGUAGE
OF THE PAIN. Strongest move: lead with GTM engineers as the wedge, cite Anthropic's own finance and
legal teams as proof of where it goes.

## SOURCE-QUALITY WARNING
Much of the 2026 "GTM engineering statistics" web recycles ONE underlying survey (State of GTM
Engineering 2026, n=228, fielded Q4 2025-Q1 2026). GTME Pulse, syncgtm, reachly, lagrowthmachine all
repeat it - treat repeated figures as ONE source, not corroboration. The load-bearing independent
sources are: the GitHub API, Anthropic's own PDF and Economic Index, VentureBeat's Cowork breakdown,
Menlo Ventures, SAP/LeanIX, WRITER, and Tightknit's Clay case study.
