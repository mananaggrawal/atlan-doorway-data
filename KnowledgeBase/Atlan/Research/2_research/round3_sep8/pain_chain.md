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

[CONTENT_PLACEHOLDER]