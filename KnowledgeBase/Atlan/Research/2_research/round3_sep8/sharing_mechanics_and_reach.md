# Sharing as a MECHANIC (not a demand), and who broadcasts hardest
Round 3, 2026-09-08. Manan's correction: round 2 tested whether users ASK for sharing (weak).
The real question is whether the ACT of sharing manufactures a second user. It does - but only
through specific mechanics, and almost never through an invite button.

## *** THE ONE NUMBER TO DESIGN AROUND ***
NO VENDOR PUBLISHES solo-to-second-person-in-same-org conversion. Searched OpenView/Insight,
boldstart, Growth Unhinged, Lenny's, Mixpanel, Userpilot, Amplitude, Reforge. Every one DEFINES the
metric and NONE publishes it. Lenny's lists it verbatim as a metric to track and gives no threshold.
Anyone quoting a crisp number here is making it up.

Best verified anchor: OpenView dev-tool benchmarks via boldstart - 5% of product-driven leads come
from referrals/invites for developer tools, rising to 9% for freemium. NOTE: that is a SHARE OF LEAD
SOURCE, not a per-user rate. Self-reported founder survey; the author flags accuracy limits himself.
Figma S-1: 70% of deals >$10k ARR started with a single user on a Professional plan; NDR 132-134%.
Survivor-biased. AGENTS.md reached ~60,000 open-source repos in 12 months with NO registry, NO
invite, NO install step.

TRIANGULATED ESTIMATE [assumption]:
| Stage | Estimate | Basis |
|---|---|---|
| Invite SENT by an activated solo user, 90d, free dev tool, sharing optional | 5-15% | bounded above by the 9% freemium referral-lead share |
| Invite ACCEPTED + activated | 30-50% | intra-org acceptance, sender is a known colleague |
| **Net solo -> second person same org, 90d** | **2-7%, centre ~4%** | product of the above, +/-3pp |
| **Same metric when the recipient MUST OPEN A SHARED ARTIFACT TO DO THEIR OWN JOB** | **40-70%** | Figma/Slack/Loom class - the "invite" is a URL blocking their work |

*** THE RATIO, NOT THE LEVEL, IS THE POINT: forcing the artifact into the recipient's obligatory path
is worth roughly 10-20x an invite button. Build the plan on that ratio. ***

## WHAT ACTUALLY FORCES A SECOND INSTALL - internal, cheapest first
In EVERY case that worked, the second person NEVER PERFORMED AN INSTALL DECISION AT ALL.
1. PROVISIONING - an admin turns it on and it appears. Anthropic finance: ~150 skills in a
   version-controlled GitHub repo shipped as workspace plugins; NEW HIRES GET THE FULL LIBRARY ON
   DAY ONE. Tim Ross: "Your best preparer writes the procedure down once in plain language and it
   runs the same way for everyone, every time."
2. THE REPO - the config is a committed file; adoption is a side effect of `git clone`. 60,000
   repos, zero install events, $0. THIS IS THE REAL COMPETITOR.
3. A REVIEW THE SECOND PERSON MUST PERFORM - a PR, an approval, a governance sign-off. The reviewer
   MUST open the thing.
4. A HANDOFF ARTIFACT with a URL the recipient must open to do their job. Figma class.
5. A METRIC the second person is accountable for.
6. Slack link / screen share / "can you send me that" / invite button - THIS IS THE 4% CEILING.
ALTRUISM APPEARS NOWHERE IN THE EVIDENCE. Neither does discovery.

Negative evidence, OzBrain Show HN (93 points), top-voted objection:
  "I have a folder called reports, plans, and code-reviews in each repo. I put my md files for
   agents there, and voila they're in the cloud along with my source code in git... No mcp or special
   server needed. Am I missing something?"
  And: "NO GIT REPO - NO SHARING - JUST ANOTHER SIGN UP AND BE AMAZED PAGE."

Best practitioner case study with numbers - group.one via Mathieu Lamiot [reported]:
  Claude Code generating "hundreds of thousands of lines of accepted code per month, growing roughly
  30% month over month"; Copilot agentic prompts from near-zero in Feb to hundreds/day by May.
  Adoption was BIMODAL - some went deep immediately, others "barely touched the tools", "averages
  were almost meaningless." What spread it: a Slack channel with multiple posts daily, Show & Tell
  sessions, and GAS - AN INTERNAL AI SKILLS MARKETPLACE distributed via Claude plugins, with three
  user tiers (beginners use as-is, intermediates customise, power users contribute back).
  His closing line is the thesis: "THE CONSTRAINT HAS SHIFTED FROM TOOLING TO COORDINATION."
Anthropic's own PDFs contain NO adoption percentages. Doctrine only: "bottom-up discovery, top-down
scale"; start with 2-3 champion teams; pilot group of 20-50 developers; kickoff hackathon over
phased rollout.

## EXTERNAL SHARING - where skills cross company boundaries, with volumes
GitHub, fetched 8 Sep 2026 [verified]:
| Repo | What | Stars | Forks | Installs (skills.sh) | Inst/star |
|---|---|---|---|---|---|
| obra/superpowers | one person's methodology | 282,771 | 25,341 | 3.1M | 11.0 |
| mattpocock/skills | one educator's .agents dir | 252,940 | 21,345 | **21.1M** | 83.4 |
| anthropics/skills | the vendor's official pack | 174,896 | 20,708 | 3.1M | 17.7 |
| garrytan/gstack | YC president | 131,419 | 19,714 | 40.8K | 0.3 |
| nextlevelbuilder/ui-ux-pro-max | design | 125,667 | 13,444 | - | - |
| addyosmani/agent-skills | Chrome DX lead | 92,299 | 9,838 | 746.9K | 8.1 |
| kepano/obsidian-skills | prosumer | 47,499 | 3,411 | 365.6K | 7.7 |
| **coreyhaines31/marketingskills** | one marketer | **47,314** | 7,374 | **4.7M** | **99.3** |
| wshobson/agents | dev | 39,459 | 4,208 | 2.1M | 53.2 |
| **microsoft/apm** (agent package manager) | vendor infra | **3,700** | 350 | - | - |
| kostja94/marketing-skills | marketing | 941 | 130 | 193.5K | **205.6** |
| sachacoldiq/ColdIQ-GTM-Skills | sales vendor | 269 | 85 | 4.1K | 15.2 |
| extruct-ai/gtm-skills | GTM | 106 | 23 | - | - |
| sales-skills/sales | sales | 89 | 10 | 13.4K | 150.6 |
| manojbajaj95/claude-gtm-plugin | GTM | 76 | 25 | - | - |
| **LaGrowthMachine/gtm-system** | funded sales-tooling co | **35** | 5 | - | - |
| stakpak/paks | package manager + registry | 62 | 5 | - | - |

*** COHORT 2 (GTM/SALES/REVOPS) HAS EFFECTIVELY NO GITHUB PRESENCE. Every dedicated sales/GTM skill
repo sits between 35 and 1,176 stars. A funded sales-tooling company's official repo has 35 STARS.
The skills.sh top-8 by install is 100% DEVELOPER skills. ***
Independent index: 1,998 skills / 401 publishers / ~19.2M cumulative weekly installs, hard power law
- top 8 publishers hold ~60%. Author's conclusion: "the discovery layer is the actual moat."
Other cross-org channels: n8n 12,145 templates with an affiliate program; Clay ~115 templates from
~20 NAMED creators (curated, status-driven); 48+ Claude Code plugin marketplace repos indexed.

## VELOCITY: WHAT TRIGGERED THE ONE BIG SPIKE
obra/superpowers published 9 Oct 2025. SIMON WILLISON WROTE IT UP 10 OCT 2025 - ONE DAY LATER -
calling Jesse "one of the most creative users of coding agents" and reproducing the two-line install.
From that day: 282,771 stars in ~11 months. THE TRIGGER WAS A SINGLE WRITEUP BY ONE HIGH-TRUST
PERSON. Not a registry, not a launch, not a marketplace listing.
Its second growth vector: PORTABILITY - superpowers now installs across 13+ agent platforms
(Claude Code, Cursor, Devin, Gemini, Copilot, Grok Build, Kimi, OpenCode, Pi, Hermes). Cross-tool
portability, not any one platform's store, is what compounded it.
Fork-to-star ratio as an "acts not applause" proxy: superpowers 8.9%, anthropics/skills 11.9%,
marketingskills 15.6%, ColdIQ 31.6%. Higher = smaller but more operational audience.

## THE SKILL PACK AS LEAD MAGNET - the economics
Matt Pocock: ~20 skills, 252,940 stars, 2.9M+ installs across his top 3 in 8 weeks, driven by a
~60,000-subscriber newsletter. He did not build an audience with the pack; HE SPENT AN AUDIENCE ON
THE PACK, and got install rank above the platform vendor.
Corey Haines: 57 skills, 47,314 stars, 7,374 forks, MIT. README cross-promotes FIVE commercial
properties (Conversion Factory, Swipe Files, AI Marketing Training, Magister, Coding for Marketers)
plus "Contributions welcome! Open a PR."
*** HIS ENTIRE OWNED AUDIENCE IS 77,000 (32K X + 17K LI + 28K newsletter, from his own media kit).
HE CONVERTED IT INTO 4,700,000 INSTALLS - A 61x MULTIPLIER OVER HIS FOLLOWER COUNT. ***
ColdIQ: 80 skills, 137 sales triggers - and 269 stars, because the README's ask is a paywall
("Don't have ColdIQ access yet? Subscribe / get an API key").
THE RULE: free packs from people who ALREADY OWN AN AUDIENCE get 10^5. Free packs from vendors who
want to ACQUIRE an audience get 10^2. Haines and Pocock beat ColdIQ by ~170x and ~940x not because
the content is better but because A SKILL PACK CONVERTS EXISTING TRUST INTO INSTALLS; IT DOES NOT
CREATE TRUST. Publishing one with no audience attached is the ColdIQ outcome.

## *** THE REGISTRY GRAVEYARD - 23 launches, ~47 HN points combined *** [all verified via HN Algolia]
Dec 2025 - Sep 2026, every "package manager / registry / marketplace for agent skills" Show HN:
Paks (stakpak) 4 | Sk`/skills-supply 1 | agent-resources "NPM/uv for Claude Code" 1 | AGENTS.lock 6 |
Skill.Fish "NPM-style package manager" 2 | Tessl "package manager with built-in evals" 7 | Askill 1 |
ClawHQ 1 | Vett 3 | Aguara 1 | ArteSync 1 | skillsgate "indexed 45k+ skills" 1 |
*** microsoft/apm - Agent Package Manager - 1 POINT *** | SkillCatalog 2 | Agensi 1 | skill-mgr 1 |
ai-capability-registry 4 | gaia-skill-tree 3 | Clawx 2 | Pharos 1 | SkillWorks 2 | SkillPreflight 1 |
apimatic Context Registry 8
MEDIAN 1-2 POINTS. NONE CLEARED 10. Microsoft, with infinite distribution, scored 1.
Paks - the best-engineered (Rust/TS monorepo, 123 commits, full CLI) - has 62 GitHub stars 9 months on.

THE CONTROL GROUP, same window, same audience:
  OpenWork (open-source Cowork alternative) 231 pts / 60c
  Cq "Stack Overflow for AI coding agents" 225 / 103
  Rowboat (local-first Claude Desktop alternative) 219 / 99
  *** OzBrain "a shared brain for knowledge between agents AND YOUR TEAM" 93 / 59 ***
ONE "SHARED BRAIN FOR YOUR TEAM" OUTSCORED ALL 23 REGISTRIES COMBINED, 93 TO 47.

WHY THEY ALL FAILED:
1. They solved DISTRIBUTION when the bottleneck was AUTHORSHIP AND TRUST. Nobody has 500 skills they
   can't find. People have zero skills they trust. skillsgate indexed 45k skills and got 1 point.
2. GIT ALREADY IS THE PACKAGE MANAGER, AND IT'S FREE. AGENTS.md hit 60,000 repos with no registry.
3. SIGNUP IS A SHARING-KILLER. "No git repo - no sharing - just another sign up and be AMAZED page."
4. VALUE ACCRUES TO THE PUBLISHER, COST TO THE INSTALLER. n8n fixed this with affiliates, Clay with
   named-creator status. The 23 offered neither.
5. THEY SHIPPED CONFORMANCE AND SAFETY BEFORE DEMAND. Five separate "verify skills before installing"
   launches (Vett, Aguara, SkillPreflight, SkillWorks, Skillcop), combined score ~9. A Feb 2026 arXiv
   paper proposing "Skilldex" rests entirely on a logical argument and contains ZERO empirical
   evidence anyone was harmed by the gap. Governance for a harm nobody has felt yet.
WHAT WOULD HAVE TO BE DIFFERENT: the registry must be a BY-PRODUCT OF A JOB THE USER ALREADY HAS TO
DO - the way git history is a by-product of committing - not a destination someone must visit.
The winners (AGENTS.md, workspace plugins, repo-committed CLAUDE.md) all have that property.
The 23 losers all asked someone to go somewhere.

## INTERNAL vs EXTERNAL - the arithmetic
EXTERNAL IS THE BIGGER REACH LEVER BY 3-4 ORDERS OF MAGNITUDE. INTERNAL IS THE ONLY REVENUE LEVER.
They are not substitutes; external produces the seed that internal converts.
- One external publishing act by an audience-holder: 10^5 reach. Haines: 1 person, 1 repo, $0 ->
  47,314 stars + 7,374 forks + 4.7M installs.
- One internal sharing act: 10^0-10^2 reach.
- At 4% solo->second-person, 47,314 externally-acquired stars yields ~1,900 second seats.
  At the 40-70% forced-artifact rate, the same 47,314 yields 19,000-33,000.
THE PLAN: spend external to acquire the wedge user; spend everything else on making that user's
OUTPUT LAND IN A COLLEAGUE'S OBLIGATORY PATH. Do not spend on a registry - 23 teams did that in nine
months and the best of them has 62 stars.

## BROADCAST PROPENSITY BY COHORT - hypothesis MECHANISM CONFIRMED, SUBSTRATE REFUTED
The seed claim (a marketing repo outperforms dev repos) is DIRECTIONALLY WRONG on stars -
marketingskills ranks 10th; six dev repos beat it, three by 2.7-6x. BUT it is #2 by INSTALLS in the
whole set, ahead of anthropics/skills and superpowers.
Install/star is BIMODAL WITHIN the marketing cohort, not cleanly higher: kostja94 205.6,
sales-skills 150.6, coreyhaines 99.3 sit far above the dev median (~14), while ericosiu 0.5,
sergebulaev 0.6, nowork-studio 1.3 sit far below. Medians nearly identical (dev 14.4, mktg/sales 15.2).
CORRECT READING: NON-DEV BROADCAST PRODUCES PUBLIC SIGNAL CHEAPLY BUT CONVERTS TO REAL ADOPTION
UNRELIABLY. Eric Siu has ~40K LI + 187K YT and converted it into 3,472 stars but only 1,600 installs.
Haines has a SMALLER audience and converted it into 4.7M. Reach is not the binding constraint;
ARTIFACT QUALITY IS.

DO ENGINEERS UNDER-BROADCAST? NOT PROVEN - don't build the pitch on it. Engineers dominate every
public artifact measured. They broadcast heavily, just on GitHub, in a currency (stars/forks/installs)
that non-engineering channels never see, and they broadcast ARTIFACTS rather than THEMSELVES.
The defensible narrow version: ENGINEERS UNDER-BROADCAST ON THE SURFACES WHERE BUYING COMMITTEES
AND BUDGET HOLDERS ARE WATCHING.

## THE COHORT THAT BROADCASTS HARDEST: AGENCY OPERATORS
ColdIQ, the best-measured broadcast dataset found [verified]: a sales agency turned 24 EMPLOYEES into
LinkedIn publishers - 581 POSTS IN 90 DAYS, 34,023 new followers gained, 250,000+ combined followers,
43,473 reactions + 28,130 comments = 71,603 engagements, producing 27 NEW CLIENTS AND $151,000 IN NEW
MRR. Fifteen individuals passed 5,000 followers. That is 0.27 POSTS PER PERSON PER DAY, SUSTAINED -
a broadcast intensity with NO measured equivalent in any engineering org. ~1.1 new clients per
broadcaster per quarter.
Exit Five: Dave Gerhardt 191,000 LI followers, 300,000 combined team, 2M monthly LI impressions,
50,000 newsletter, 5,700 paying members, ~60% of signups from LinkedIn.
Maja Voje: post slug is LinkedIn-generated from her own first line - "1500-people-asked-for-my-gtm-
claude-code..." so the 1,500 figure is her own verified claim. Co-authored the 2026 Claude Code GTM
Report with Kyle Poyar: 200 GTM operators surveyed Mar-Apr 2026, 92% saved time, 55% replaced a tool,
32% use Cowork as primary.
Anthropic's own analysis of ~400,000 Claude Code sessions / ~235,000 users (Oct 2025-Apr 2026):
most pronounced growth among NON-SOFTWARE ROLES - management, sales, law. Code modification fell
from 33% to 19% of sessions; document/presentation creation reached 10%.

## THE STRUCTURAL ANALOGUE: CLAY
A technical product (enrichment waterfalls, HTTP APIs, JS formulas) deliberately sold to
NON-ENGINEERS - and in doing so INVENTED THE JOB TITLE OF ITS OWN BUYER. GTM-engineer postings then
grew 205% YoY with Clay named in 55% of them (vs HubSpot 52%, Salesforce 45%, Zapier 39%).
The crossover: technical product -> non-technical operators adopt -> those operators BROADCAST TO WIN
THEIR OWN CLIENTS -> broadcasting creates a job category -> the category makes the tool a hiring
requirement -> the requirement drives enterprise seats.
Agency owners posted Clay workflows on LinkedIn UNPROMPTED, to look expert and win their own clients.
*** CLAY DID NOT PAY FOR TUTORIALS - "the motivation is operator self-promotion." Affiliate payouts
were DELIBERATELY WITHHELD UNTIL AFTER $5M ARR, because paying converts an evangelist into a
contractor and kills the credibility that made the broadcast work. ***
Result: ~$100K ARR (2021) -> $1M (2022) -> $10M (2023) -> ~$30M (2024) -> $100M (Q4 2025);
Slack 200 -> 10,000+ members.
Gamma is the volume analogue: 150+ creators -> 50M+ users, 25% of users from social referrals,
40% word-of-mouth = ~83,000 users per creator. 70% of creator spend went to MICRO-influencers in the
10K-100K band.

## THE AMPLIFIER LIST - people who have ALREADY shipped or promoted agent skills
Corey Haines (32K X, 17K LI, 28K newsletter | marketingskills 47,314*/4.7M installs) ·
Matt Pocock (~60K newsletter | 252,940*/21.1M) · Jesse Vincent/obra (superpowers 282,771*/3.1M) ·
Addy Osmani (Chrome DX | 92,299*/746.9K) · Garry Tan (YC | 131,419*) · Maja Voje (GTM, "1,500 asked")
· Kyle Poyar (Growth Unhinged) · Eric Siu (40K LI, 187K YT | 3,472*/1.6K installs) ·
Sacha + ColdIQ (250K+ combined LI) · kepano/Obsidian (47,499*/365.6K) · Serge Bulaev (1,278*) ·
Elvis Un (newsjack, 666*)
Largest non-dev audiences with a structural reason to care: Neil Patel 1.47M LI · Dharmesh Shah 700K
· Ann Handley 450K · Justin Welsh 550K · Dave Gerhardt 191K · Rand Fishkin 189K · Adam Robinson 140K
· Aleyda Solis 109K · Brian Dean 100K · Lily Ray 80K · Ross Simmonds 80K · Amanda Natividad 50K ·
Peep Laja 30K · Alex Lindahl (Claymation, GTM Eng at Clay) · Eric Nowoslawski · Lenny Rachitsky (1M
subs + 20K Slack)
AI creators spanning cohorts: Alex Hormozi 3.2M YT · Riley Brown 1.5M · Matt Wolfe 800K · Liam Ottley
713K · Skill Leap AI 700K · Matthew Berman 540K · Greg Isenberg 500K · Nate Herk 500K · Wes Roth 293K
· The AI Advantage 260K · Julia McCoy 244K

## CAVEATS
LinkedIn and X are robots-blocked; every LI engagement number here is from a URL slug, a first-party
media kit, or a third-party writeup - never the post itself. ungh.cc vs the GitHub API differ ~5%
(44,769 direct vs 47,314 ungh for marketingskills); the table is internally consistent but treat
absolutes as +/-5%. skills.sh install counts are self-reported by that registry, cover only
`npx skills add`, undercount manual clones and overcount CI re-installs.
