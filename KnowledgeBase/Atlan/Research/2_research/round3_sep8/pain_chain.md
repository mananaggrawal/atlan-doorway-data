# The pain chain, sequenced by when each pain bites
Round 3, 2026-09-08. Two candidate ICPs. Every pain scored on severity x frequency x how badly served.

## *** READ THIS FIRST: THE TRUNCATION PAIN IS NOW SOLVED FREE ***
The "silent truncation at ~16,000 characters" that anchored our Week 2-4 story HAS BEEN
SUBSTANTIALLY CLOSED BY ANTHROPIC, FOR FREE, BETWEEN MAY AND SEPTEMBER 2026.
Official Claude Code docs now state [verified, code.claude.com/docs/en/skills]:
  "The listing always contains every skill name, but if you have many skills, Claude Code shortens
   descriptions to fit the listing's character budget... The budget scales at 1% of the model's
   context window. When the listing overflows, Claude Code drops descriptions starting with the
   skills you invoke least, so the skills you use most keep their full text."
  "Run /doctor for an estimate of the listing's context cost and its biggest contributors. To find
   skills worth turning off, run /skill-doctor. When the listing exceeds its budget, Claude Code also
   writes a warning to the debug log."
Plus settings `skillListingBudgetFraction`, `skillListingMaxDescChars` (default 1,536/entry),
`SLASH_COMMAND_TOOL_CHAR_BUDGET`, `skillOverrides: "name-only"`. Startup now shows a
"Skill listing will be truncated" warning. /context's Skills row fixed in v2.1.196.
TIMELINE: budget setting v2.1.129 (~May 2026) -> /context fix v2.1.196 -> /skill-doctor in 2.1.261,
4 SEP 2026, FOUR DAYS BEFORE THIS RESEARCH.
Three original grievances are now FALSE: no longer silent (there's a warning), no longer undocumented
(it's in the docs), no longer unconfigurable (two settings + an env var).
*** LEADING A SEPTEMBER 2026 CAMPAIGN WITH "YOUR SKILLS ARE SILENTLY DISAPPEARING" WILL GET YOU
CORRECTED BY THE FIRST ENGINEER WHO READS IT. ***

## THE ORIGINAL TRUNCATION SOURCES, for the record [verified]
GitHub issue anthropics/claude-code#13099, alexey-pelykh, 4 Dec 2025, closed:
  "The available_skills section in Claude Code's system prompt has an undocumented character budget
   of approximately 15,500-16,000 characters. When users install many skills, some become completely
   invisible to the agent without any warning about why."
  "With 63 installed skills, the system prompt showed: <!-- Showing 42 of 63 skills due to token
   limits --> This means 21 skills (33%) were hidden."
  His gist: 63 skills = 16,577 chars; 42 shown = 11,071; 21 hidden = 5,506; per-skill overhead ~109
  chars. "Truncation is cumulative, not individual." "No configuration exists."
shimo4228, "15 Days of Skill Sprawl in Claude Code", DEV, 31 Jan - 14 Feb 2026:
  16 active skills on 1/31 -> by 2/14, 15 ACTIVE AND 33 DISABLED, ~63 total across four scopes.
  Three separate audits in five days. "if you have too many skills, they get silently truncated.
  More is not better." Recommendation: "audit when any single layer exceeds 10 skills."
  NOTE THE REAL STORY: 33 of 63 were DISABLED, NOT DELETED - the residue of "nobody knows which
  version is best / is anyone using this."

## SKILLS THAT DON'T FIRE - the deepest, least-solved authoring pain
*** THE STRONGEST SINGLE PIECE OF EVIDENCE IN THE WHOLE CORPUS *** - Vercel first-party engineering
eval, Jude Gao, 27 Jan 2026 [verified, vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals]:
  "In 56% of eval cases, the skill was never invoked. The agent had access to the documentation but
   didn't use it."
  Baseline 53% pass | skill (default) 53% - ZERO IMPROVEMENT | skill + explicit instruction 79% |
  AGENTS.md 100%.
  "For general framework knowledge, passive context currently outperforms on-demand retrieval."
  Fragility: "invoke first" vs "explore first" wording "produced dramatically different outcomes."
Issue #30387, wujekbogdan, 3 Mar 2026, CLOSED AS NOT PLANNED:
  "Previously, the same instructions lived in CLAUDE.md and worked reliably. After moving them to
   skills (following the docs), Claude frequently ignores them."
  "This happens ~50% of the time for skills that overlap with Claude's trained behaviors (git, shell)."
  "Budget is NOT the issue (~25% usage)." "Forcing skill usage via CLAUDE.md with caps-lock
   instructions doesn't work."
  KEY DISTINCTION: skills for NOVEL tools (Jira) fire reliably; skills that OVERRIDE TRAINED
  BEHAVIOUR (git, shell, formatting) fail ~50%. That is exactly the class engineers write skills for.
Issue #20986, 26 Jan 2026, closed as duplicate: "Claude assumes it 'knows how to do it' and proceeds
  with its own interpretation instead of using the defined skill."

## COST OF THE PAIN, QUANTIFIED
Issue #29971, Ryan4n6, 2 Mar 2026, "Claude Code Context Bloat", CLOSED AS NOT PLANNED, consolidates
15 issues [verified]: #27721 skill duplication 37 skills -> 74 entries (3,000-5,000 tokens/session) |
#28660 160 SKILLS = ~25K TOKENS PER TOOL CALL, i.e. ~1.25M TOKENS WASTED IN A SINGLE SESSION |
#27757 sandbox mode 607K-token system prompt against a 200K limit | #12241 single Docker MCP = 125K
tokens | #21966 /context shows 13% while hiding ~40K tokens. His ask #6: "Credit for wasted context."
Issue #14882, atournayre, 20 Dec 2025: "With multiple plugins installed, skills alone consume 50k+
  tokens before any conversation starts." (And the official plugin-dev "Skill Development" skill is
  5.5k tokens while instructing "Keep SKILL.md lean: Target 1,500-2,000 words.")
The New Stack on Anthropic's own /claude-api skill: "a one-line question could consume roughly
  200,000 tokens before Claude started answering." Fixed in v2.1.234 by on-demand loading:
  200,000 -> ~25,000 tokens (85.7% reduction).
Naqeeb ali Shamsi, Medium, 31 Mar 2026 [reported, self-measured, single practitioner]: inventory of
  49 plugins (46 disabled), 4 user-scope MCP servers, 18 custom agents, 58 slash commands, 30
  projects, ~690KB debug logs. Post-cleanup: sessions before rate-limiting 3-4 -> 5-7 daily; time
  lost to context resets ~15-20 min/day -> ~5 min; startup 8-12s -> 2-3s. Estimated $200-400/month
  recovered productivity, $75-375/month API savings.
RUNAWAY-SPEND INCIDENT - Sattyam Jain, Tech Lead (GenAI) at Attri.ai, "The Agent That Burned $4,200
  in 63 Hours", 14 Apr 2026 [reported, single-company postmortem]:
  "The agent had no concept of its own cumulative cost... Every iteration was a fresh start from its
   perspective." "He wasn't a bad engineer. He had followed my docs."
  Cause: "keep trying until it works" + no budget ceiling. ~4,800 retries/hour on 429s, over a weekend.
*** THE "$3.50 TO LOAD THE SKILL" FIGURE COULD NOT BE VERIFIED. Four targeted searches found no such
quote. DO NOT PUT IT IN A CUSTOMER-FACING ASSET without finding the original. *** The closest
verifiable equivalents are the 200,000-token pre-answer load, the 1.25M-tokens-per-session figure,
and Anthropic's own in-product warning that raising the budget costs ~"3k tokens for skills every
session."

## DRIFT / DECAY - the weakest-served pain in the corpus, and therefore the most interesting
Lucas Hendrich, CTO, Forte Group, 12 May 2026 [reported - consultancy selling agentic services, BUT
describing his own team's operations, which is the strongest form this weak evidence class takes]:
  "Every one of them has required revision, sometimes because the underlying tooling changed,
   sometimes because we learned through usage that the instructions produced subtly wrong outputs,
   and sometimes because a downstream process shifted and the skill simply stopped matching reality."
  *** "A STALE SKILL IS THE CONTEXT ENGINEERING EQUIVALENT OF SILENT DATA CORRUPTION IN A DATABASE:
   the system keeps running, the outputs look plausible, and nobody raises an alarm." ***
  "A stale skill can run for weeks before anyone notices the output quality has slipped."
  HE CITES NO CASE STUDY. None found anywhere.
Joe Karlsson, CloudQuery, 6 Apr 2026 [verified, first-person]: "Skills drift... someone needs to be
  watching for that." "This is infrastructure, not a project you ship and walk away from."
Sean Lynch, cofounder of Census, 8 Mar 2026 [verified, credible unaffiliated practitioner]:
  "Skills require manual upload and updates, unlike plugins' auto-update feature."
  "Anthropic appears to be shipping their org chart at the moment" - on Cowork / Claude.ai / Code
  having "complete disconnected behaviors."
GTME Pulse names the exact mechanism ("Stale instructions - CRM field changes break skills silently")
but is vendor-adjacent content with ZERO named practitioners and no case study [weak].
*** HONEST VERDICT: DRIFT IS UNIVERSALLY ASSERTED AND ALMOST NEVER DOCUMENTED WITH AN INCIDENT. That
is an opportunity (nobody has claimed the narrative) AND a risk (we would have to produce the proof
ourselves - a customer story or our own instrumented before/after). ***

## ============ ICP A: THE GTM ENGINEER / REVOPS BUILDER ============

### Day 1-7 - authoring
A1. THE SKILL SILENTLY NEVER FIRES AND THERE IS NO ERROR.
  "A skill with a vague description is a skill that never fires, and the failure is silent." [vendor]
  Katya Tarapovskaia, Youstellar (Revenue AI/ABM), 17 Apr 2026 [reported]:
   "Undertriggering (skill doesn't load when it should): Users ask 'why isn't it working?'"
   Then the consequence: "USERS DISABLE IT."
  *** That two-step - doesn't fire -> user disables it -> skill graveyard - IS THE DAY-1 FAILURE LOOP
  FOR ICP A, and it is the seed of the Week-2 accumulation problem. ***
  Solved free? Partially - skill-creator exists, docs cover descriptions. But nothing tells a
  non-engineer WHY their skill lost the trigger race against Claude's trained behaviour (#30387 shows
  this is a model-level precedence problem, not a docs problem).
A2. YAML / naming friction (name capped at 64 chars, lowercase, cannot contain "anthropic"/"claude").
  A real wall for someone who doesn't use git. LOW INTENSITY, LOW DIFFERENTIATION - DO NOT LEAD.

### Week 2-4 - accumulation
A3. THE SKILL COUNT OUTRUNS DISCOVERY. Tightest ICP-A artifact found:
  sidchaudhary/gtm-skills - 78 GTM SKILLS ACROSS 7 GTM ROLES, by Sid Chaudhary, founder of Intempt
  [verified]. Its own README carries the warning verbatim:
   *** "Don't install all 78 on day one. You'll use nine of them and forget the rest." ***
   "You don't need to be technical. If you can type a sentence, you can use these."
  78 skills x ~109 chars overhead + descriptions is comfortably past a 16,000-char budget. THE
  FLAGSHIP GTM SKILL PACK, ON INSTALL, IS THE TRUNCATION EVENT.
  Solved free? YES, largely, as of Sept 2026. Do not lead with it.
A4. COST/CONTEXT BURN. ICP A has NO instrumentation at all - subscription, hits limits, no /context
  habit. [assumption - NO ICP-A-specific token-spend testimony exists. All quantified cost evidence
  in this space comes from engineers. HONEST EVIDENCE GAP.]

### Month 2-3 - drift
A5. THE CRM CHANGED AND THE SKILL NOW WRITES PLAUSIBLE GARBAGE.
  *** COULD NOT FIND A SINGLE VERBATIM, NAMED ACCOUNT of a Claude skill writing to the wrong CRM
  field after a schema change. Searched five ways. *** What exists: the mechanism named by vendor
  content; Forte Group's CTO on silent corruption; and STRONG ANALOGOUS evidence from the same
  buyer's world - Salesforce/Marketo/Zapier INVALID_FIELD sync threads, and an Adobe Experience
  League thread literally titled "The silent breakdown of automated workflows no one notices until
  it's too late."
  REAL, UNSERVED, AND UNDOCUMENTED.

### The moment a SECOND PERSON gets involved
A6. "CAN YOU SEND ME THAT" AND THERE IS NO ANSWER THAT ISN'T A COPY.
  For ICP B the answer is "clone this repo." *** ICP A CANNOT SAY THAT. THAT ASYMMETRY IS THE WHOLE
  ICP-A WEDGE. ***
  Karlsson, 6 Apr 2026 [verified]: "When a coworker said 'hey, can you show me how you do that
   LinkedIn thing?' - the answer wasn't a Notion doc or a prompt to paste somewhere. It was
   'clone this repo.'"
  What happens when the answer IS a Notion doc - Laura Klein, NIELSEN NORMAN GROUP, 31 Oct 2025
  [verified - research org, STRONGEST NON-VENDOR SOURCE ON THIS MOMENT]:
   "They've accumulated massive collections of multistep prompts that MIGHT AS WELL BE MAGIC SPELLS."
   "This knowledge could be valuable to other members of the team, but it's TRAPPED IN INDIVIDUAL
    PRACTITIONERS' HEADS."
   *** "everybody ends up with their own PRIVATE SPELLBOOK rather than anything shared and, more
    importantly, TESTED." ***
   "we can't even see what others are doing... We can't build on each other's approaches because we
    can't easily share our AI-assisted work."
   "Making everyone figure out AI alone creates chaos and risk."
  The divergence cost - Jessica Jess, Enterpret, 30 Jun 2026 [reported, VENDOR MARKETING, illustrative
  only]: "five different PRD formats, five different ways of citing customer evidence, and five
   different definitions of 'done'." "without versioning you'll spend an hour debugging before
   realizing they're on different versions." "The work doesn't compound; it spreads."
  AND THE STRONGEST EVIDENCE THAT THE PROMPT-LIBRARY WORKAROUND FAILS - Brad Wilkins, VP of People
  and Organization at Cognite [verified - NAMED EXECUTIVE, NON-VENDOR]:
   "Prompts are the opening move. They are not the unit of work."
   *** "Had I known this earlier, I would have SKIPPED THE MONTHS OF PROMPT-LIBRARY CURATION that
    everyone in our field has been doing and gone directly to skill design." ***
  Solved free? NO, NOT FOR ICP A. git (they don't use it), shared Drive/Notion (no versioning, no
  sync into the agent, Wilkins says it wastes months), plugin marketplace (requires publishing a git
  repo). Anthropic's org skill provisioning requires an ADMIN to upload - it gives a team-of-one NO
  way to hand a skill to one colleague.

### The moment a THIRD+ PERSON or a MANAGER gets involved
*** A7. THE CRM PERMISSION MODEL DOES NOT SURVIVE THE AGENT. THE SHARPEST VERIFIED ICP-A FINDING IN
THE ENTIRE RESEARCH, AND IT IS AN ACTUAL INCIDENT. ***
  HubSpot Community, "HubSpot Connector for Claude - Permissioning Needs", RevOps Discussions forum
  [verified - real named practitioners on a first-party vendor forum]:
  alijensen, 5 May 2026: "We're experiencing two critical issues with the Claude-HubSpot connector
   that pose serious DATA INTEGRITY RISKS." "As a HubSpot admin, I have NO WAY TO SET CONNECTOR-LEVEL
   PERMISSIONS (e.g. read-only vs manage objects) on a per-user basis. The connector simply inherits
   each user's existing HubSpot permissions." "HubSpot allows admins to restrict bulk CRM updates to
   a maximum of 10 records at a time - intended as a safeguard against mass data changes. However,
   THIS LIMIT IS TRIVIALLY BYPASSED BY INSTRUCTING CLAUDE TO LOOP THE UPDATE FUNCTION."
  JTolley, 6 May 2026: "I believe you're correct on those two issues... ADMINS HAVE NO CONTROLS -
   I've heard other Admin/RevOps folks complaining about the same permission structure."
  *** cc-revops, 9 Jun 2026 - THE INCIDENT: "a rep CLOSED LOST a deal by accident that was already in
   CLOSED WON... The rep was UNABLE TO DO IT IN THE UI but the MCP CONNECTOR HAD PERMISSIONS." ***
  mwx-Marcus, 8 Jul 2026: "The bulk update limit exists for a reason, and 'just tell Claude to loop
   it' shouldn't be a bypass."
  THE ARC: May -> Jun -> Jul, FOUR different practitioners, escalating, a HubSpot moderator who had
  no answer ("I don't see any mention of these specific limits"), and by 22 Jul A THIRD-PARTY VENDOR
  SHOWED UP IN THE THREAD SELLING GRANULAR MCP PERMISSIONS. A MARKET FORMING IN PUBLIC, IN A REVOPS
  FORUM, OVER TEN WEEKS.
  WHO: the manager / RevOps admin / the org. THE FIRST PAIN IN THE CHAIN A BUDGET HOLDER FEELS.
  Solved free? NO. Neither HubSpot nor Anthropic had shipped a fix. Anthropic's Apr 2026 admin
  controls (groups, spend caps, managed Claude Code policies, usage analytics) cover tools/files/MCP
  at POLICY level and do NOT provide per-skill permission, per-skill usage, or cost attribution.
  Intensity: "WE HAD AN INCIDENT." HIGHEST IN THE CORPUS FOR ICP A.
A8. "IS ANYONE EVEN USING THESE, AND WHAT DID THEY COST?" /skill-doctor answers this for ONE PERSON'S
  LOCAL SESSION, not a team. It "records whether a skill ran during a session but NOT WHETHER THE
  SKILL IMPROVED THE RESULT" - making valuable rarely-used procedures indistinguishable from dead
  ones. AND: ICP A IS NOT IN CLAUDE CODE. They are in Claude.ai / Cowork, WHERE /skill-doctor DOES
  NOT EXIST.

## ============ ICP B: THE ENGINEER AT AN AI-NATIVE STARTUP ============
B1. THE SKILL LOSES THE TRIGGER RACE TO TRAINED BEHAVIOUR (~50% on git/shell/formatting). #30387.
  Solved free? NO - closed as "not planned", caps-lock enforcement doesn't work. But YOU CANNOT SELL
  A FIX FOR THE MODEL'S TRIGGER PRECEDENCE. Great hook, unsellable.
B2. TOKEN/CONTEXT BURN. SOLVED FREE as of Sept 2026. Occasionally an incident when it triggers
  premature compaction mid-task (#15377: compacting at ~65% because 246K tokens of MCP context).
B3. *** SKILL DRIFT - instructions silently stop matching reality. THE ONLY PAIN IN THE ICP-B CHAIN
  THAT GIT DOES NOT TOUCH. Git tells you what changed in the skill. IT CANNOT TELL YOU THE WORLD
  CHANGED UNDERNEATH AN UNCHANGED SKILL. *** Compounded by MCP config drift - tool schemas change
  under the skill. /skill-doctor measures INVOCATION, NOT CORRECTNESS.
B4. HANDOFF / VERSIONING - *** SOLVED FREE. NEVER MENTION IT TO ENGINEERS. ***
  Karlsson: "Updating the brand voice is a PR. One PR, and every skill picks it up on the next
  git pull." What git does NOT solve, and he names it himself:
   "WHO OWNS THIS WHEN YOU'RE ON VACATION?" / "There's an owner (me, for now, ideally not just me
   forever) who watches for regressions and reviews PRs." / "NAME AN OWNER BEFORE YOU SHARE THE REPO
   WITH ANYONE." / "I didn't set out to build internal tooling. I built a few Claude Code skills for
   myself because I was tired of copy-pasting."
  THE RESIDUAL PAIN IS OWNERSHIP AND REGRESSION-WATCHING, NOT STORAGE OR DIFFING.
B5. NO PER-SKILL ACCOUNTABILITY AT ORG LEVEL. Anthropic's org skills shipped 18 Dec 2025 - admin
  central provisioning, enabled-by-default, user toggle-off, a skills directory with Notion/Canva/
  Figma/Atlassian. EXPLICITLY NOT INCLUDED: skill versioning, approval workflows, usage analytics,
  drift detection, per-skill permissions. Apr 2026 admin controls added spend caps and Claude Code
  usage analytics - but analytics are "lines of code accepted, suggestion accept rate, session
  volume", NOT per-skill usage or cost attribution.
DEPARTURE: mitigated for ICP B because skills live in a repo that survives the person. BUT
  ~/.claude/skills/ (global scope) does NOT, and shimo4228 found engineers keep a large global layer
  - 17 global skills at his peak, and his top recommendation was "Don't put project-specific skills
  in global." THE GLOBAL LAYER IS THE ICP-B BUS-FACTOR SURFACE.

THE MANAGER'S FOUR QUESTIONS, mapped:
  Which version is canonical? -> solved by git for B, UNSOLVED for A
  Who owns it? -> UNSOLVED FOR BOTH (Karlsson's "who owns this when you're on vacation")
  Is it safe? -> UNSOLVED FOR BOTH, and demonstrably dangerous (the HubSpot bulk-limit bypass)
  What did it cost / is anyone using it? -> partially solved, per-session per-individual only,
    via /skill-doctor. ZERO ORG-LEVEL ROLL-UP.

## ============ DEPARTURE / REORG - better evidence than round 2, still thin ============
1. DIRECT SURVEY DATA - the closest thing to a hard number. Kolmogorov Law via Pollfish, n=500
   employed US adults, 8 Jul 2026 [verified - named survey, named sample]:
   "38% admitted they have entered at least one type of work information into a personal AI account"
   "36.8% [use AI for work] at least partly through a personal account"
   On leaving employment with work chats in a personal AI account: *** 16.2% WOULD KEEP THE ACCOUNT
   UNCHANGED, BELIEVING "THE CHATS ARE MINE"; 31.6% HAD NEVER CONSIDERED THIS SCENARIO; *** 19%
   would ask their employer for guidance. Framing: could "walk out the door by default."
2. LEGAL FRAMING - M. Adil Yaqoob, Akerman LLP, 9 Jun 2026 [verified, law-firm client alert]:
   employers should ask departing workers to certify they haven't "retained AI-generated summaries of
   company information, STORED COMPANY PROMPTS OR OUTPUTS IN PERSONAL ACCOUNTS"; preserve "prompts,
   outputs, chat histories, and memory exports." BUT: "COURTS HAVE NOT YET DIRECTLY ADDRESSED"
   whether AI-generated summaries of trade secrets constitute misappropriation. NO CASES CITED.
3. *** THE BEST ANALOG, AND IT IS A VERY GOOD ONE *** - KomuraSoft, "Power Automate Key-Person Risk
   and Flow Handover", 18 Jul 2026 [verified - consultant quoting client engagements verbatim]:
   "We had an employee who was good with Power Automate, and they automated all sorts of processes
    around the company. NOW THEY'RE LEAVING NEXT MONTH, AND NOBODY KNOWS WHAT ANY OF THE FLOWS
    ACTUALLY DO."
   The later-stage version: "the person has already left, and 'ORDER NOTIFICATION EMAILS STOPPED
    ARRIVING LAST MONTH AND THERE'S NOBODY WHO CAN FIX IT'."
   The author notes this consultation type has "visibly increased lately."
   MECHANISM: "Connections used to run it (the authentication to SharePoint, Outlook and so on) are
   TIED TO THE ACCOUNT OF THE PERSON WHO CREATED THEM", and "even a co-owner cannot change the
   credentials of a connection someone else created." Microsoft's own term: "ORPHANED FLOW."
   *** THAT MECHANISM MAPS EXACTLY ONTO ICP A: OAuth to HubSpot/Gmail/Gong IS BOUND TO THE
   INDIVIDUAL'S ACCOUNT. When they leave, the skill file may survive but THE CONNECTION DOES NOT. ***
VERDICT: still no first-person "my colleague left and the skills broke" account for AI skills.
Likely because the install base is ~12 months old and the cohort hasn't turned over yet. THE PAIN IS
AHEAD OF THE MARKET, NOT ABSENT FROM IT. The Power Automate analog is what this looks like at T+5
years. USE IT AS A PREDICTION, FRAMED HONESTLY, NOT AS A CLAIMED OBSERVATION.

## ============ WORKAROUNDS AND WHAT THEY COST ============
| Workaround | Who | Cost |
|---|---|---|
| Mass-disable skills (33 of 63) | ICP B | nobody knows if disabled = dead or dormant; no record of why |
| Repeat audits (3 in 5 days) | ICP B | direct time, recurring forever |
| Manual cleanup of plugins/MCPs/agents | ICP B | a full session; recovers $75-375/mo API + $200-400/mo productivity |
| git repo + PR review | ICP B | FREE AND IT WORKS - but creates "who owns this on vacation" |
| Notion/Drive prompt library | ICP A | Wilkins: "months of prompt-library curation" wasted |
| Everyone builds their own | ICP A | "private spellbook", untested, unshareable, invisible |
| Keep CLAUDE.md under 5KB | ICP B | deliberate under-specification to limit re-injection blast radius |
| Daily human review of agent output | ICP A / manager | see Lemkin below |
| Third-party MCP permission layers | ICP A org | a vendor appeared selling this in the HubSpot thread, 22 Jul 2026 |

JASON LEMKIN, SaaStr, worth quoting in full for the MANAGER persona [verified]:
  "Managing these agents is now 30% OF OUR CHIEF AI OFFICER'S TIME."
  "Every single agent requires weeks of training and daily management. There's no 'set it and forget it'."
  "Can only absorb 1.5 NEW AGENTS PER MONTH without overwhelming our team."
  "ALL AGENTS HAVE HALLUCINATED. The key is constant calibration, not perfection."
  "Effective cost is also OVER $500,000 A YEAR, and far more than the tools they 'replaced'."
  "We failed spectacularly for the first 30 days. Generic messaging. Terrible response rates.
   Prospects clicking 'spam'." / "The first 1,000 emails were manually reviewed. Every. Single. One."
  "10X TIMES ZERO IS STILL ZERO."

## ============ RANKING AND THE WEDGE ============
Score = severity x frequency x how badly served (10 = totally unserved).

ICP A:
| # | Pain | Sev | Freq | Unserved | Score | Verdict |
|---|---|---|---|---|---|---|
| A7 | Agent bypasses CRM permissions; writes what the human couldn't | 10 | 4 | 9 | 360 | *** WEDGE *** |
| A6 | Second person asks; no non-git way to hand it over | 6 | 8 | 7 | 336 | Strong #2 |
| A5 | Skill drifts after schema change, fails silently | 8 | 6 | 10 | 480* | see note |
| A1 | Skill never fires; user disables it | 4 | 9 | 6 | 216 | entry-level |
| A8 | Manager: is anyone using this, what did it cost | 5 | 3 | 8 | 120 | bundle with A7 |
| A3 | 78 skills installed, discovery truncates | 4 | 7 | 3 | 84 | SOLVED FREE |
| A2 | YAML / naming friction | 2 | 5 | 4 | 40 | ignore |
*A5 scores highest on paper but is MARKED DOWN IN PRACTICE because NOT A SINGLE NAMED INSTANCE could
be verified. A campaign built on an unevidenced pain is one the buyer nods at and doesn't act on.
TREAT A5 AS THE MESSAGE AND A7 AS THE PROOF.

*** ICP A SHARPEST WEDGE: A7 - "YOUR AGENT HAS MORE PERMISSION THAN YOUR REP DOES." ***
1. The only ICP-A pain with a VERIFIED, DATED, FIRST-PERSON INCIDENT from a real practitioner.
2. The only one that reaches a BUDGET HOLDER. A1-A6 are felt by a team of one with no budget.
   A7 is felt by a RevOps admin who owns the CRM and answers to a CRO.
3. PROVABLY UNSERVED BY BOTH VENDORS. HubSpot's own moderator had no answer; four practitioners
   across ten weeks confirmed each other; no fix shipped.
4. IT CARRIES A5 AND A6 AS CONSEQUENCES. Once you have the permissions conversation, "and by the way
   this skill was written against last quarter's field names, and three people have divergent copies"
   lands without needing separate proof.
5. IT INTERCEPTS AT A MOMENT - the first time a manager discovers the agent did something the UI forbade.
DO NOT LEAD ICP A WITH: truncation/context bloat (solved free, and they aren't in Claude Code
anyway), YAML friction, or generic "AI governance."

ICP B:
| # | Pain | Sev | Freq | Unserved | Score | Verdict |
|---|---|---|---|---|---|---|
| B3 | Skill drift - instructions silently stop matching reality | 8 | 7 | 10 | 560 | *** WEDGE *** |
| B1 | Skill loses trigger race to trained behaviour (~50%) | 6 | 9 | 8 | 432 | strong #2, unsellable |
| B5 | No org-level per-skill ownership/usage/cost/approval | 6 | 4 | 8 | 192 | manager-side |
| B2 | Token/context burn | 5 | 8 | 2 | 80 | SOLVED FREE |
| B4 | Handoff / versioning | 4 | 6 | 1 | 24 | SOLVED FREE - NEVER MENTION |
| - | Departure | 7 | 1 | 8 | 56 | too rare to campaign on |

*** ICP B SHARPEST WEDGE: B3 - THE STALE SKILL AS SILENT DATA CORRUPTION. ***
1. THE ONLY PAIN IN THE ICP-B CHAIN GIT DOES NOT TOUCH. Git tells you what changed in the skill; it
   cannot tell you the world changed underneath an unchanged skill. A genuinely new problem class.
2. Everything else is either already free (B2, B4) or an Anthropic model-behaviour problem you cannot
   fix (B1). B1 is a great HOOK - most viscerally annoying - but you cannot sell a fix for trigger
   precedence.
3. Vercel's 56% gives a credible, quotable, NON-VENDOR number, pointing at the same truth: THE GAP
   BETWEEN WHAT THE AGENT WAS TOLD AND WHAT IT ACTUALLY DOES IS UNMEASURED. Drift is that gap over time.
4. Forte Group's CTO already wrote the headline, unprompted.
5. THE CATCH, STATED PLAINLY: WE WOULD HAVE TO PRODUCE THE FIRST REAL DRIFT INCIDENT STORY OURSELVES.
   It does not exist publicly. Strongest argument for owning it; biggest execution risk in the plan.
DO NOT LEAD ICP B WITH: versioning, sharing, git-shaped anything, context/token bloat, or
/skill-doctor-adjacent "find your unused skills." All four are free, shipped, and one shipped 4 days ago.

## RESIDUAL EVIDENCE GAPS - state these honestly in the appendix
1. No verified "$3.50 to load the skill" quote. Replace it or find the original.
2. No named CRM-drift incident. Asserted by vendors, reasoned by practitioners, never documented.
3. No AI-specific departure story. Best available: a Power Automate analog, a Pollfish survey, and a
   law-firm alert that explicitly notes NO CASE LAW EXISTS. Use as a closing line, never standalone.
4. No GitHub reaction counts on the issues in this file - fetches did not surface them. Engagement
   figures here are limited to thread post counts, dates, and duplicate-report counts.
5. No ICP-A token-spend testimony. Every quantified cost figure comes from an engineer in Claude Code.
   If cost is part of the ICP-A pitch, it is currently an ASSUMPTION.
