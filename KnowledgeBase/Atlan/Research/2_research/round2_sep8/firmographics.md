# Firmographics: who is AI-native, and how to enumerate them
Research run 2026-09-08. Purpose: make the ICP TARGETABLE, not just describable.

## 1. AI penetration by function - testing "coding > voice > GTM"
CODING, deepest by every instrument:
- JetBrains DES 2026, n>15,000 professional devs, fielded May-Jul 2026: 90% USE AI CODING AGENTS AT
  WORK WEEKLY, 68% DAILY. Tool share: Claude Code 39% global / 47% US; Copilot 21%; Codex 16%;
  Cursor 12%; OpenCode 7%; Antigravity 6%. Claude Code is the PRIMARY tool for 31%. [verified]
- Claude Code went 18% -> 39% globally in ~7 months (JetBrains Jan 2026 -> Aug 2026). [reported]
- Menlo: coding = $4.0B of $7.3B departmental AI spend (55%), the largest single application category
  in the entire ecosystem. Anthropic holds ~54% share in coding vs OpenAI 21%. [verified]
- McKinsey State of AI, fielded 4 May - 8 Jun 2026, n=1,719, 97 countries: 31% OF >$1B ENTERPRISES ARE
  SCALING SOFTWARE CODING AGENTS - the single most common agent deployment. [verified]
- Stack Overflow 2026, n=49,000+: 84% of devs use AI tools but ONLY 31% USE AGENTS; 38% have no plans. [reported]

VOICE - ranks high in SPEND, near-zero in CONTEXT SPRAWL. This is the important correction:
Menlo's departmental spend table contains NO VOICE LINE AT ALL - zero mentions in the full report.
[verified] Voice appears instead as VC funding ($315M 2022 -> $2.1B 2024, ~7x) and as a vertical
market, and inside healthcare's $1.5B vertical spend (scribes).
THE LOAD-BEARING POINT: a voice deployment's context lives inside a VENDOR'S platform - Sierra,
Decagon, Parloa - where prompts, flows and guardrails are configured in someone else's console.
NOBODY ACCUMULATES 50 SKILL.MD FILES BUILDING A VOICE AGENT. And the humans who do build voice
agents are engineers running Claude Code, so voice collapses back into the coding motion anyway.
(The "97% of enterprises have adopted voice AI" figure circulating via Mordor is not credible. Do not use.)

GTM - third, and thin: ICONIQ Q2 2026 (n=305 software execs) productivity gain at high-growth
companies: coding 48%, customer service 30%, sales 25%, FP&A 21%. [verified via secondary summary]
Ramp AI Index Aug 2026: spend is extremely concentrated - top 1% of businesses spend a median $7,400
per employee on AI; the MEDIAN FIRM SPENDS $11.95. [verified]

REVISED ORDERING FOR OUR PURPOSES: coding >> GTM > voice, where the ranking metric is
"does a human accumulate reusable, portable context artifacts", not "how much does the function spend."

## 2. Company profiles - an inverted-U
| Segment | Agent deployment | Read |
|---|---|---|
| <$100M ARR | 40% actively deploying, 30% piloting | fast, but too few people to hit 50+ skills |
| $100-500M ARR | 49% ACTIVELY DEPLOYING | SWEET SPOT |
| >$500M ARR | 56% deploying, 31% still piloting | have the sprawl, have procurement |
| >$1B revenue | 40% scaling agents (up from 27%); 22% for smaller orgs, flat YoY | budget exists, zero-budget bottom-up won't land |
[ICONIQ Q2 2026, McKinsey May-Jun 2026, verified]
DX Q4 2025 (435 companies, 85,350 devs): <50-dev orgs at 80% weekly AI usage vs ~70% for 50-200-dev
orgs. [reported] Penetration is HIGHER in small orgs, but sprawl needs headcount x time.
INTERSECTION: 50-500 employees with 30-150 engineers.

SECTORS by density of team-scale Claude Code / Codex deployment:
1. Dev tools & infra - highest. Anthropic's named Claude Code customers skew here: Atlassian, Ramp,
   DoorDash, Spotify, Deepgram, Rocket Money. [verified, claude.com/customers]
2. Fintech - Ramp, Rocket Money, Pictet (Claude Code + Cowork), Stripe. High eng density + compliance
   pressure = governance is felt, not sold.
3. AI-native applied startups (Series A-C, founded 2022+) - highest per-capita intensity, lowest
   budget. Perfect for zero-budget bottom-up.
4. Healthtech - Menlo puts healthcare at $1.5B, 43% of all vertical AI spend. Abridge, League.
5. Consultancies / SIs - Deloitte, IBM, TCS, Cognizant, Capgemini, KPMG all hiring AI-enablement
   titles (Apollo, 8 Sep 2026). Enormous sprawl, slow cycles.
6. Agencies / BPO - see section 6.

## 3. TARGETABLE TITLE SIGNALS - Apollo people-database, live query 8 Sep 2026, strict match [verified]
| Title | Count | Read |
|---|---|---|
| Forward Deployed Engineer | 5,817 | largest, WORST signal - contaminated by Palantir lineage. Filter to companies founded >=2020 |
| Prompt Engineer | 3,864 | DO NOT TARGET. Legacy, freelancer-heavy, not budget-adjacent |
| AI Enablement (exact) | 2,770 | HIGHEST-CORRELATION TITLE. 4,235 with fuzzy match |
| AI Ops | 2,689 | DO NOT TARGET as a string - collides with AIOps/MLOps infra |
| GTM Engineer | 1,918 | small but most homogeneous and highest-intent |
| AI Platform Engineer | 845 | owns the internal platform, therefore owns the registry problem |
| AI Enablement Lead/Mgr/Dir/Specialist combined | 653 | |
| AI Transformation Lead | 623 | skews consultancy and enterprise |
| Agent Engineer | 482 | SMALLEST, PUREST. Nobody holds this title without a large local library |
| Developer Experience Engineer | 132 | |
| Head of DevEx / DPE / Head of Developer Productivity | 96 | |
| Head of AI Enablement | 100 | your named-account list |
| Head of AI Adoption | 48 | |

COMPANY-LEVEL FILTER, live Apollo 8 Sep 2026 [verified]:
2,423 US COMPANIES WITH 51-1,000 EMPLOYEES currently have an open posting for AI Enablement,
AI Engineer, Forward Deployed Engineer or GTM Engineer. THIS IS THE ADDRESSABLE, FILTERABLE TARGET
LIST AND IT IS ONE APOLLO QUERY AWAY.
Breakdown: 1,917 companies hiring FDEs | 762 hiring AI Enablement | 546 hiring GTM Engineers.

## 4. OBSERVABLE PUBLIC ARTIFACTS THAT MARK AN ICP - the enumeration method
1. GitHub org-scoped code search: `path:.claude/skills`, `path:CLAUDE.md`, `path:AGENTS.md`,
   `path:.claude/commands`, filtered to org: accounts not personal. BEST SIGNAL - a company with
   .claude/skills in a PUBLIC repo is near-certainly running many more privately.
2. Fork graph of anthropics/skills - 168.9k stars, 20.1k FORKS (Sep 2026). [verified]
   Forks are a far stronger intent signal than stars: a fork usually means "we are building our own
   library." Dedupe forks to organization accounts.
3. skills.sh publisher list - 401 unique publishers across 1,998 indexed public skills. [reported]
4. MCP registries - ~9,400 servers mid-Apr 2026, +38% from ~6,800 at end-2025, aggregated across
   PulseMCP, registry.modelcontextprotocol.io, Smithery, mcp.so. [reported, directional only]
5. Anthropic's own customer directory and partner skill directory - pre-qualified, publicly attributed.
6. DNS-record inference: bloomberry detects 94,093 COMPANIES ON CLAUDE TEAM/ENTERPRISE as of
   7 Sep 2026, ~1,844 in a renewal window in the next 3 months, filterable by industry/size/geo.
   [reported - DNS inference, a detection estimate not a customer list]
7. Conference talks, engineering blogs, r/claudeskills post authorship with employer in bio.

ESTIMATE: 3,000-6,000 companies leave at least one enumerable public artifact; ~300-500 are
hand-curatable top-tier targets. [assumption]

## STARTER LIST - 24 named companies with evidence
Published agent skills via Anthropic's partner directory: Atlassian, Ramp, Stripe, Notion, Figma,
Cloudflare, Sentry, Canva, Zapier.
Top skills.sh publishers by install volume: Vercel Labs (owns 3 of the top 5 skills incl. find-skills),
Microsoft (azure-skills), HeyGen, Remotion, Lark/Feishu, LarkSuite CLI.
Named Claude Code deployments (claude.com/customers): DoorDash, Spotify, Deepgram, Rocket Money,
League (healthtech), Pictet (private bank, Claude Code + Cowork, Artefact as delivery partner),
Spellbook (legaltech), EvenUp (legaltech), DXC.
Public repos with substantial CLAUDE.md indicating house practice: Vercel (next.js), Supabase,
LangChain (langgraph), LlamaIndex, Microsoft (autogen), SST (opencode), Getzep (graphiti).
HIGHEST-CONVICTION SUBSET for zero-budget bottom-up (mid-size, AI-native, engineer-led, publishing):
Ramp, Vercel, Supabase, Sentry, Deepgram, Rocket Money, Spellbook, EvenUp, Remotion, HeyGen, Zapier, League.

## 5. SIZE OF THE ADDRESSABLE POOL - modelled, not measured
STEP 1 - people using agentic coding at all:
- npm @anthropic-ai/claude-code: 81,476,585 downloads 8 Aug - 6 Sep 2026; 14,825,815 trailing week.
  [verified - queried api.npmjs.org directly]
- @openai/codex: 76,016,785/month same window. [verified] Codex is at ~93% of Claude Code's npm
  volume, so any Claude-only sizing UNDERSTATES the pool by roughly half.
- npm downloads are not users (CI matrices, container rebuilds, devcontainers, auto-update checks).
  Assumption ~25 download events per active user per month -> 81.5M/25 ~= 3.3M Claude Code users.
- Cross-check A: Stack Overflow 2026 puts Claude Code at 9.7% IDE share across 49,000+ respondents;
  against ~30M global professional devs -> ~2.9M.
- Cross-check B: JetBrains' 39% measures "used at work weekly" among engaged devs who answer
  JetBrains surveys - right number for PENETRATION, wrong denominator for POPULATION.
- CONVERGING: 2-4M Claude Code users; ~5-7M across Claude Code + Codex + Cursor, deduped. [assumption]

STEP 2 - orgs running it at team scale: bloomberry 94,093 companies on Claude Team/Enterprise
(DNS, 7 Sep 2026) [reported]; Anthropic reports 300,000+ business customers [reported, secondary];
plus Codex/Cursor-primary orgs. Assumption: 150,000-250,000 organizations globally. [assumption]

STEP 3 - what fraction has crossed 50 skills. THE CRUCIAL FINDING: 50 SKILLS IS A LOW BAR, REACHED FAST.
A documented single-practitioner audit went from 16 skills at install (31 Jan 2026) to 63 SKILLS
ACROSS PROJECTS BY 14 FEB 2026 - FIFTEEN DAYS - of which 33 had to be disabled, and discovery
silently truncated at ~16,000 characters so ONLY 42 OF 63 WERE EVER VISIBLE TO THE MODEL. [reported]
If one person hits 63 in two weeks, a 10-person team six months in is at hundreds. Binding
constraints: (a) >=6 months of use, (b) >=5 daily users, (c) more than one repo or team.
Assumption: 25-35% of the team-scale org base clears all three.

ARITHMETIC: low 150,000 x 0.25 = 37,500 | high 250,000 x 0.35 = 87,500
-> 40,000-90,000 ORGANIZATIONS WORLDWIDE PLAUSIBLY HAVE 50+ AGENT SKILLS TODAY. Midpoint ~60,000. [assumption, modelled]

STEP 4 - reachable slice: English-language, bottom-up, no procurement gate ~15-20% -> 9,000-12,000 orgs.
Publicly enumerable via section 4: 3,000-6,000. Hand-curatable beachhead: 300-500.
Apollo-filterable today: 2,423 companies. [verified]

SANITY CHECK: skills.sh reports 1,381,768 total installs all-time. At ~15 registry-sourced skills per
team and ~5 machines per team that implies ~18,000 teams active in the public registry alone -
comfortably inside the 40-90k estimate, as it should be, since most 50+-skill teams write their own.
DATA-QUALITY WARNINGS: (i) skills.sh's homepage counter (1,381,768) is INTERNALLY INCONSISTENT with
its own leaderboard (find-skills alone at 3.3M, microsoft/azure-skills 7.4M). Do not cite the two
together. (ii) The ~1.9M "public skills" figure from SkillsMP (Jun 2026) is a GitHub scrape counting
FILES, not adoption. Not comparable to install counts.

## 6. NON-ENGINEERING AI-HEAVY ORGS
These matter because ONE PERSON'S WORKFLOW IS THE COMPANY'S PRODUCT, so per-person context sprawl
converts directly into delivery risk - a sharper pain than an engineering team's tidiness problem.
- AGENCIES / CREATIVE SHOPS: Anthropic maintains named agency case studies incl. Advolve and
  Brand.ai; Artefact is the delivery partner on Pictet. [verified] A visible category of agencies
  publicly committing to Claude Code + Cowork as their operating model exists (e.g. Marketing
  Signals). A whole sub-industry of "Claude Code development agencies" now ranks for that term.
  THESE FIRMS ARE SIMULTANEOUSLY ICP AND CHANNEL.
- CONSULTANCIES / SIs: worst sprawl profile in existence - per-client skill sets, per-consultant
  variation, no shared registry, and a contractual obligation to prove what context touched a
  client's data. Thoughtworks publicly analysed the Jun 2026 Claude outage as an infrastructure-
  dependency event [verified] - a company only writes that post if Claude is load-bearing across many
  delivery teams. STRONGEST GOVERNANCE NARRATIVE, SLOWEST CYCLE. Right for case studies, wrong for a
  zero-budget bottom-up campaign.
- BPO: weakest fit despite loud AI adoption. BPO AI is overwhelmingly voice and CX platform
  deployment, configured in vendor consoles, not accumulated as portable skill files. Deprioritise.
- GTM TEAMS INSIDE PRODUCT COMPANIES: the genuinely underrated non-engineering wedge. 1,918 GTM
  Engineers exist, 546 companies hiring. [verified] Their Clay/Apollo/enrichment playbooks are
  functionally identical to skills - undocumented, personally owned, lost when the person leaves -
  but sit OUTSIDE any engineering governance. Menlo notes sales AI is 78% STARTUP-SHARE, i.e. bought
  bottom-up outside IT. [verified] That is the definition of an ungoverned surface.

## BOTTOM LINE
PRIMARY: US/UK software companies, 50-500 employees, 30-150 engineers, founded 2015-2022,
$100-500M ARR band, dev tools / fintech / healthtech, with an AI Enablement, AI Platform Engineer or
Agent Engineer on staff and a public .claude/skills or CLAUDE.md artifact.
2,423 US companies match the hiring filter in Apollo TODAY; ~300-500 also carry a public artifact.
THE WEDGE CLAIM, and it is defensible: 50+ skills is not an enterprise-scale condition - it is a
TWO-WEEK condition for ONE PERSON, and the tooling silently truncates discovery long before anyone
notices. Roughly 40,000-90,000 organizations are already past that line, and almost none know it.
