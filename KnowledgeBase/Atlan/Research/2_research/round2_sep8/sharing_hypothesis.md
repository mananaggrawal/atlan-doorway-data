# The sharing hypothesis, pressure-tested
Research run 2026-09-08. Hypothesis under test: "users are asking for the ability to share skills
across their team." Manan's own instinct going in: not convinced. The evidence agrees with him.

## VERDICT
Sharing is the WORD people use. It is not the JOB. Ranked by every quantitative signal reachable,
sharing is the 4th-5th strongest ask. It is also already solved five ways over (git, plugin
marketplace, symlinks, Dropbox, rsync). The GOVERNED half of the ask - version history, review,
rollback, "who changed this", "which of these 183 skills is dead" - is real, rising, and is where
the vendor itself is now moving.

Coverage gap, stated plainly: Reddit was network-blocked for this run (SITE_BLOCKED / PROXY_REJECTED),
no X or Discord archives. Everything below is GitHub, Hacker News, vendor docs, named practitioners.
Treat the Reddit-shaped hole as unmeasured, not absent.

## Ranked asks (GitHub reaction counts, pulled 2026-09-08) [verified]
TIER 1 - PORTABILITY ACROSS HARNESSES, overwhelming
- claude-code#6235 "Support AGENTS.md" = 6,592 reactions (Aug 2025). Highest-reacted feature request
  in the repo's history. ~44x the top sharing issue.
- claude-code#31005 (5 Mar 2026) = 473. Verbatim: "Developers don't use just one tool. We switch
  between Claude Code, Cursor, Codex, Copilot... Maintaining duplicate files is error-prone (they
  drift apart immediately)." And: "Six issues. Seven months. Over three thousand community upvotes.
  Two hundred and twenty four comments. Zero responses from anyone at Anthropic."
- claude-code#16345 "Support .github/skills/" = 40.

TIER 2 - DISCOVERY + "DOES THE SKILL EVEN FIRE?", ~510 reactions across #10238 (168), #9716 (75,
69 comments - most-discussed skill issue), #18949 (74), #18192 (65), #14836 (51), #26489 (48), #15178 (33).
  THE HARD NUMBER: Vercel's public eval, 524 HN points / 196 comments, 27 Jan 2026 -
  skills were NEVER INVOKED IN 56% OF EVAL CASES, producing ZERO improvement over baseline
  (53% pass rate with and without skills). With explicit instructions, invocation rose to 95%+ and
  pass rate to 79%. An AGENTS.md docs index scored 100%.
  vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals [verified]
  Corroborating: "Half the time Claude Code still doesn't invoke it" (msp26, HN 30 Jan 2026);
  "I'm still trying to figure out why some skills are used every day, while others are constantly
  ignored" (KingMob); "I wish I knew why my skills are never called" (testfrequency);
  anthropics/skills#556 - literal 0% trigger rate under `claude -p`.

TIER 3 - CONTEXT BUDGET. claude-code#14920 (89), #26838 (44). On CODEX the #1 skills issue by
reactions is context budget: codex#19679 "Make skills metadata context budget configurable instead
of hardcoded 2%" (36). anthropics/skills#1486: "claude-api skill balloons context" - reporter cites
"$3.50 API costs just to load the skill."

TIER 4 - SYNC ACROSS MACHINES. claude-code#20697 "Sync Skills between Claude Desktop and Claude Code
CLI" = 161 reactions (25 Jan 2026).

TIER 5 - SHARING. claude-code#28729 "Link a source control repo as the source for organization
skills" = 151, the highest-voted sharing-adjacent issue. READ THE BODY - it is a GOVERNANCE request:
  "Once you get to 20-30+ skills with multiple contributors, it becomes difficult to manage - there's
  no version history, no review process, and no easy way to roll back a bad change."
  "Today someone edits a skill locally, uploads it through the admin console, and nobody reviews the
  change. If something breaks, we piece together what happened through Slack."
Explicit sharing asks are tiny: claude-code#33530 "/share-skill" CLOSED AS DUPLICATE;
anthropics/skills#228 "Enable org-wide skill sharing" = 8 reactions.

## The three strongest pieces of evidence AGAINST sharing
1. The top sharing issue is 44x smaller than the top portability issue - and it is not about sharing.
   6,592 vs 151. Distribution is not the pain; CHANGE CONTROL is.
2. Sharing is already solved, loudly, by free tools - and the market voted 9:1 for SYNC over SHARING.
   On the Show HN for a dedicated sharing product (Sx 2.0, 44 pts / 33 comments, 13 Jul 2026) the
   modal response was "What's wrong with git?" / "we're sharing skills with rsync" / "Why not a
   private GitHub repo?" / "each person's ~/.claude/skills is symlinked to a shared Dropbox folder."
   In stars: runkids/skillshare (framing: cross-tool SYNC) = 2,629, zero team-sharing feature requests
   in its issue tracker. sleuth-io/sx (framing: "Skill sharing made easy") = 287.
   When Anthropic itself shipped org skill distribution (289 HN points, 170 comments, 18 Dec 2025),
   NOT ONE COMMENT celebrated finally being able to share.
3. A shared skill that doesn't fire is worthless, and 56% of the time it doesn't fire (Vercel).
   Meanwhile teams that DO share are asking to turn shared skills OFF BY DEFAULT -
   codex#34328, 20 Jul 2026, iOS monorepo, 20+ contributors: "a repo-wide skill set that
   force-activates for everyone is noisy and eats the ~2% skills context budget on every session."

## What DOES break when people share (the real, narrow pain)
btown, HN, who does share via Dropbox symlinks: "The one place I've seen this break down on teams is
when a skill gets improved or adjusted. If everyone is copying it you end up not knowing which is the
best and most accurate." [verified]
detkin: "I can't think of anything worse than sharing skills via Dropbox. The version management and
AIBoM problems that generates is extremely painful." [verified]
Joe Karlsson, 7 Apr 2026, personal skills repo that became internal tooling: "this repo is not done.
There is no done." / "Name an owner before you share the repo with anyone" - otherwise "something
breaks and stays broken." [verified, n=1]

## INSTRUMENTATION - and the four-day-old event that changes the Pulse calculus
NATIVE SURFACE TODAY:
- /skill-doctor SHIPPED IN CLAUDE CODE 2.1.261 ON 4 SEPTEMBER 2026 - FOUR DAYS AGO.
  Official docs (code.claude.com/docs/en/skills): "Run /skill-doctor to see what each of your skills
  costs and how often it gets used... It flags skills in the listing that have never been invoked and
  says where to turn them off. It also lists plugins you haven't used recently." [verified]
  >>> THIS IS SUBSTANTIALLY WHAT ATLAN PULSE DOES, SHIPPED BY THE VENDOR, LAST WEEK. <<<
- /context and /doctor report skills-listing context cost and biggest contributors.
- OpenTelemetry: claude_code.skill_activated events (invocation_trigger, skill.source),
  claude_code.cost.usage and token.usage tagged with skill.name.
- Mature third-party OTel stacks: ColeMurray/claude-code-otel, SigNoz, Dash0.
- BUT: claude-code#76957 (12 Jul 2026) - skill_activated MASKS skill.name to the literal string
  "custom_skill" while api_request and cost metrics export it verbatim in the same session.
  "Masking the skill name here breaks per-skill adoption analysis (which skills does the team use,
  and how often)." "No actual privacy: anyone with telemetry backend access already sees the real
  skill name in api_request events and metrics." [verified]

THE BEST-ARTICULATED DEMAND ARTIFACT IS ALSO THE WEAKEST BY VOTES:
claude-code#35319 "Skill invocation tracking and usage analytics" (17 Mar 2026) - near-verbatim
statement of Atlan's thesis: org grew FROM 67 TO 183 SKILLS IN 4 WEEKS; no way to identify unused
skills for deprecation; cannot measure adoption; cannot detect duplicates; no data to justify context
window budget allocation; skill authors receive no feedback on usage. Proposes queries for "skills
with zero invocations in 90 days" and "skills used by only 1 person (bus factor risk)".
IT WAS CLOSED. 7 comments. Companion bugs #82644, #92326 sit at 0 reactions.

READ THIS CORRECTLY: analytics demand is loud in one voice and silent in aggregate (~15 reactions
across the whole cluster). Anthropic shipped it anyway. The honest claim is NOT "users are asking for
usage analytics" - it is "nobody was asking, the vendor just built it, and practitioners confirmed
the pain within 24 hours." Joe Njenga, 5 Sep 2026: "I Tried (New) Claude Code /skill-doctor (And
Found Most Skills Are Dead Weight)" - "If a skill is loaded but never firing, you're paying for it
every single turn for nothing." [reported, paywalled]
Anthropic's Thariq Shihipar, 24 Jul 2026: the team was "overconstraining the product through its
system prompt, CLAUDE.md files and skills" and removed OVER 80% OF CLAUDE CODE'S SYSTEM PROMPT with
"no measurable loss" on coding evals. [reported, evals not published]

## ANTI-SHARING EVIDENCE
- Job security / personal IP: REAL BUT NEARLY UNSUPPORTED. Ask HN "Am I disloyal for not wanting to
  share my system prompts?" (10 Apr 2026) got 1 POINT, 10 comments. Replies rejected the position
  near-unanimously: "Company time + company resources = company property." The hoarding instinct
  exists and is articulate; it has almost no public constituency. DO NOT BUILD A NARRATIVE ON IT.
  (This retroactively vindicates cutting "never train your replacement" from the deck.)
- Skills-forced-on-me is the STRONGER anti-sharing signal - codex#34328 above.
- Security fear is well-evidenced at industrial scale: the ClawHavoc campaign poisoned OpenClaw's
  ClawHub with 1,184 malicious skills, Jan 2026 - Unit 42, Snyk ("From SKILL.md to Shell Access in
  Three Lines of Markdown"), Antiy Labs, Cybersecurity News. [verified, multi-source]
  xg15, HN 15 Jan 2026: "Treat skill files as executable code; treat third-party skill files as
  third-party executable code, with all the usual security/trust implications." [verified]

## THE ATOMIC UNIT PEOPLE ACTUALLY WANT TO EXCHANGE - evidence is thin and points AWAY from the file
- Vercel: the winning unit was a compressed 8KB AGENTS.md docs INDEX pointing at documentation,
  scoring 100% vs 53% for skills-by-default. [verified]
- detkin, HN: the unit is an encoded PATTERN - "our backend architecture has these hidden patterns,
  that once encoded in a skill, can be followed by full stack devs."
- bberenberg, HN 14 Jul 2026: the unit is an OUTCOME delivered invisibly - "skills should be authored
  by a small set of people who know what they're doing and made available to non technical team
  members 'magically'." The recipient wants the EFFECT, not the artifact.
- m-hodges, HN: "Why do none of these document any way to do basic package management things like
  updates, version-pinning, or even uninstalls?"
READ: people exchange PATTERNS and want to receive OUTCOMES. SKILL.md is a transport format nobody
is attached to and it lacks package semantics. Building a registry around the FILE as the unit is a
bet the evidence does not support.

## THE "LEAVES THE COMPANY" PROBLEM - THINNEST SECTION, treat any pitch on it as UNSUPPORTED
Targeted HN comment search returned 0 hits. Enterprise-AI-governance + IP + departing-employee
searches returned only SEO content marketing; zero primary CISO/CIO/legal commentary. The only
adjacent primary material ran AGAINST the employee. The closest org-side version is engineering-
flavoured, not legal: #35319's "bus factor risk" and Karlsson's "name an owner."
CONCLUSION: continuity/ownership is a NARRATIVE WE WOULD HAVE TO CREATE, not one we can cite.
Legitimate GTM choice, but label it thesis, never voice-of-customer.

## WHERE THE WEDGE SHOULD MOVE TO, in evidence-strength order
1. PORTABILITY / single source of truth across harnesses. 6,592 + 473 + 40 reactions; 2,629 stars on
   the tool that leads with it. Directly matches Atlan's Claude Code / Codex / ChatGPT framing.
   This is the one we can PROVE.
2. CHANGE CONTROL over a growing skill estate - version history, review, rollback, who changed this.
   What #28729's 151 reactions actually say. Sharing is the trojan horse; governance is the product.
3. INSTRUMENTATION, with the caveat. Not user-voiced. Vendor-validated four days ago by /skill-doctor.
   Pitch it as "the problem the vendor just admitted", never as "what users are asking for."
