# Quantitative Baseline: AI Agent Skills — Numbers with Sources
Compiled 2026-09-05 for the governed-skills-registry work sample. Every row cites its exact source URL and pull date. No estimated figures are presented as measured facts — estimates are explicitly labeled.

## 1. skills.sh (Vercel Labs' open agent-skills directory)

| Metric | Value | Source | Pull date | Status |
|---|---|---|---|---|
| Launch date | Jan 20, 2026 | https://rywalker.com/research/skills-sh (independent research post, published June 11, 2026) | 2026-09-05 | [reported, secondary] |
| Total all-time installs (homepage counter) | 1,320,673 | https://skills.sh/ | 2026-09-05 | [verified, live fetch] |
| #1 leaderboard skill | find-skills (vercel-labs) — 3.3M installs | https://skills.sh/ | 2026-09-05 | [verified, live fetch] |
| Total skills catalogued, third-party estimate | ~669,670 (as of June 2026) | https://rywalker.com/research/skills-sh | 2026-09-05 | [reported — NOT independently confirmed; skills.sh's own homepage does not display a single "total skills" counter, only a ranked leaderboard, so this figure could not be cross-verified] |
| Agents/clients supported | 20+ tracked directly, CLI claims 70+ compatible | https://rywalker.com/research/skills-sh | 2026-09-05 | [reported] |

### Top skills.sh leaderboard entries with installs (live pull, [verified])
Source: https://skills.sh/ — pulled 2026-09-05. Note: ranks 9-11, 15-36, 43-45 were not rendered in the fetched view; table below lists only the ranks/rows the page actually returned.

| Rank | Skill | Author | Installs |
|---|---|---|---|
| 1 | find-skills | vercel-labs | 3.3M |
| 2 | grill-me | mattpocock | 1.1M |
| 3 | grill-with-docs | mattpocock | 909.0K |
| 4 | improve-codebase-architecture | mattpocock | 871.8K |
| 5 | frontend-design | anthropics | 856.6K |
| 6 | tdd | mattpocock | 843.8K |
| 7 | agent-browser | vercel-labs | 791.9K |
| 8 | setup-matt-pocock-skills | mattpocock | 778.5K |
| 12 | vercel-react-best-practices | vercel-labs | 690.9K |
| 13 | anti-ui-slop | uizze.com | 681.9K |
| 14 | lark-doc | open.feishu.cn | 659.9K |
| 37 | grilling | mattpocock | 630.0K |
| 38 | lark-markdown | open.feishu.cn | 624.1K |
| 39 | web-design-guidelines | vercel-labs | 609.2K |
| 40 | lark-vc-agent | open.feishu.cn | 602.5K |
| 41 | teach | mattpocock | 599.7K |
| 42 | ai-video-generation | skills-101 | 586.3K |
| 46 | microsoft-foundry | microsoft | 572.8K |
| 47 | domain-modeling | mattpocock | 572.8K |
| 48 | lark-apps | open.feishu.cn | 568.4K |

Dominant categories/publishers by install volume: **Matt Pocock's collection** (mattpocock) dominates with multiple entries; **Vercel Labs** (find-skills, agent-browser, vercel-react-best-practices, web-design-guidelines); **open.feishu.cn (Lark/ByteSpin)** — multiple doc/collab skills; **Anthropic** (frontend-design). By publisher totals (per one secondary summary, [reported]): Microsoft/azure-skills ~7.3M, larksuite/cli ~4.3M, open.feishu.cn ~15.1M total installs across its skill set — these publisher-total figures came from an AI-generated summary of the page and were NOT independently re-verified line by line; treat as directional only.

Discrepancy note: separate secondary sources gave different install counts for the #1 skill (find-skills) at different times — 2.0M (rywalker.com, June 2026), ~3M (skillselion.com listing), 3.3M (live pull, Sept 2026). This is consistent with genuine growth over time, but it means any single install figure is a snapshot, not a stable constant — worth stating explicitly in any pitch material.

## 2. NPM download data (api.npmjs.org, [verified] — live API pulls)

| Package | Last month | Window | Last week | Window | Source | Pull date |
|---|---|---|---|---|---|---|
| @anthropic-ai/claude-code | 80,220,622 | 2026-07-31 to 2026-08-29 | 21,450,823 | 2026-08-23 to 2026-08-29 | https://api.npmjs.org/downloads/point/last-month/@anthropic-ai/claude-code and .../last-week/... | 2026-09-05 |
| skills (vercel-labs' skills.sh CLI, confirmed via npm registry metadata: description "The open agent skills ecosystem", repo github.com/vercel-labs/skills, bins `skills` and `add-skill`) | 38,365,913 | 2026-07-31 to 2026-08-29 | 9,363,514 | 2026-08-23 to 2026-08-29 | https://api.npmjs.org/downloads/point/last-month/skills and .../last-week/skills ; package identity confirmed via https://registry.npmjs.org/skills | 2026-09-05 |

Caveat on the `skills` package number: 38M/month is very large for a skills-directory CLI. It could not be independently explained (e.g. whether it is bundled as a transitive dependency of another popular package, inflating raw download counts, since npm download counts count every CI/install pull, not unique users). Treat as a directly-measured but hard-to-interpret figure — flagging rather than asserting "38M people use skills.sh monthly."

## 3. Ecosystem/spec timeline (official, dated announcements)

| Event | Date | Source | Pull date | Status |
|---|---|---|---|---|
| Anthropic launches Agent Skills (original, Claude-only) | Oct 16, 2025 | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | 2026-09-05 | [verified] |
| Agent Skills becomes a published open standard / spec site (agentskills.io) — adoption noted by Simon Willison | Dec 19-20, 2025 | https://simonwillison.net/2025/Dec/19/agent-skills/ | 2026-09-05 | [verified] |
| agentskills.io lists 45+ adopting clients incl. Claude Code, ChatGPT/Codex, Cursor, GitHub Copilot, VS Code, Gemini CLI, Cline-adjacent tools, JetBrains Junie, Databricks, Snowflake, Kiro, Factory, etc. | current as of pull | https://agentskills.io | 2026-09-05 | [verified, live fetch] |
| skills.sh launches | Jan 20, 2026 | https://rywalker.com/research/skills-sh | 2026-09-05 | [reported] |
| AWS Agent Registry (Bedrock AgentCore) launches in preview | Apr 9, 2026 | https://aws.amazon.com/about-aws/whats-new/2026/04/aws-agent-registry-in-agentcore-preview | 2026-09-05 | [verified] |
| AWS Agent Registry reaches general availability | Aug 31, 2026 | https://aws.amazon.com/about-aws/whats-new/2026/08/aws-agent-registry-generally-available/ | 2026-09-05 | [verified] |

Quote, AWS Agent Registry (both preview and GA pages use near-identical language), [verified]:
> "a private, governed catalog and discovery layer for agents, tools, skills, MCP servers, and custom resources within the organization."
This matters directly: AWS's own positioning for a governed catalog is nearly a template for a "governed skills registry" pitch, and it went from preview to GA in under 5 months (Apr to Aug 2026) — evidence of real enterprise appetite for exactly this category, from a hyperscaler, independent of skills.sh.

Not obtained despite searching: exact official dates for "Google's skill registry" and a distinct "Skills API" announcement as named in the task brief — no such Google-branded artifact was found (see Could Not Obtain section). Gemini CLI supports the Agent Skills open spec (per agentskills.io client list) but no evidence of a separate Google-run public skill *registry* was found.

## 4. Survey/usage data on AI coding agent adoption

### JetBrains — "AI Coding Agents: Adoption Trends" — blog.jetbrains.com/research — Aug 19, 2026 — author Mikhail Bogdanov — https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/ — [verified] — Sample: "more than 15,000 professional developers worldwide," survey period May-July 2026.

| Stat | Value |
|---|---|
| Developers using AI coding agents at least weekly | 90% |
| Developers using AI coding agents daily | 68% |
| Claude Code adoption worldwide | ~39% (up from 18% in Jan 2026) |
| Claude Code adoption, United States | 47% |
| Developers naming Claude Code their primary/most-used tool | 31% |
| GitHub Copilot adoption | 21% (down from 29% a year prior) |
| OpenAI Codex adoption | 16% (up from 3% in Jan 2026) |
| Cursor adoption | 12% (down from 18% in Jan 2026) |
| OpenCode adoption / awareness | 7% / 42% awareness |
| Google Antigravity adoption | 6% |
| JetBrains AI adoption | ~9% |

Why it matters for ICP sizing: this is the most credible, large-sample, dated evidence that agentic coding tools (the substrate skills run on) are now majority-adopted at the individual-developer level (90% weekly) — but it says nothing about *team-level* skill-sharing behavior, which remains the open question (see qualitative section / "could not obtain" below).

### Anthropic Economic Index — "Learning curves" report — anthropic.com/research — March 24, 2026 — https://www.anthropic.com/research/economic-index-march-2026-report — [verified]
> "the share of tasks in this category [coding] has increased by 14% in the API" since August 2025.
> "Long-tenure users are about 5 percentage points more likely to have a successful conversation" (3-4 points after controlling for task type).
> "The top 10 O*NET tasks now account for 33% of traffic," up from 28% since August 2025.
This report does not mention Agent Skills, skill counts, or team-size breakdowns at all — logged as a near-miss (see Could Not Obtain).

## 5. How many skills does a typical user/team actually have? — HUNTED HARD, LARGELY UNRESOLVED

This was searched most aggressively per instructions. Findings:

- No survey, blog post, or vendor report was found stating a measured average or median number of skills per developer or per team. This is a genuine gap in public data as of 2026-09-05.
- The closest proxy numbers found are **vendor/publisher skill-catalog sizes**, not per-user or per-team counts, from a secondary skill-directory site (mcpservers.org/agent-skills), [reported, not independently verified]: Microsoft 1,577 skills, Anthropic 927, OpenAI 746, GitHub 567, Vercel 396, Cloudflare 140, Google Workspace 99, Notion 27, Figma 21, Stripe 18 — these describe how many skills a *vendor publishes*, not how many an individual or team *installs/maintains*.
- A qualitative proxy: Michael Jovanovich's Substack post (responseawareness.substack.com, Nov 27 2025) frames "twenty skills" as the informal point where naive (non-semantic) skill discovery starts wasting meaningful context budget — but this is presented as an illustrative threshold, not a measured typical count. [reported as illustrative only]
- shimo4228's dev.to post (Feb 22, 2026) describes running audits "every 1-3 days" on a personal skill set because "skills keep growing" — implies personal skill counts grow fast enough to need near-continuous pruning, but no absolute count is given.
- CLSkills Hub's "Claude Code Skills Report 2026" (31-page PDF, v1.0, April 2026, author Samarth Bhamare, clskillshub.com/report) catalogs "2,392 skill files" across the ecosystem and breaks enterprise skills down by vendor (e.g. SAP is the largest single enterprise category at 107 skills of 845 catalogued), but explicitly does not report a per-developer or per-team baseline. [reported]

**Conclusion for ICP sizing purposes: there is no public, credible number for "typical skills per user/team." Any ICP threshold based on skill count must be treated as a hypothesis to validate in discovery interviews, not as a documented industry baseline.**

## 6. Could Not Obtain

- A measured average/median "skills per developer" or "skills per team" figure — searched extensively (see Section 5); does not appear to exist in public writing as of this pull.
- A distinct, dated "Skills API" announcement separate from the Oct 16, 2025 Agent Skills launch and the Dec 2025 open-standard/agentskills.io launch — no separate artifact under that name was found.
- A Google-run public "skill registry" as such — only found: Gemini CLI's support for the open Agent Skills spec (listed on agentskills.io/clients), which is adoption of the standard, not a Google-operated registry.
- OpenAI's exact "Skills availability" launch date as a named milestone — what was found instead: Simon Willison's Dec 20, 2025 update noting OpenAI added Skills to Codex docs "days after" the Dec 19 open-standard post, and a separate developers.openai.com/codex/skills/ page exists but no dated OpenAI press announcement was located and fetched.
- A precise, single, stable "total skills listed on skills.sh" figure — the site's own homepage shows a leaderboard and an install counter (1,320,673, verified live) but not an all-up catalog-size counter; secondary sites gave conflicting figures (see Section 1 discrepancy note).
- Any DORA 2026 report content specifically on AI agent/skill adoption — search returned adjacent AI-coding-productivity commentary (e.g. "93% of developers use AI but productivity is only 10%" via ShiftMag/SecondTalent) but no DORA-branded report was directly located and fetched; not included above because it was not verified against the primary DORA source.
- Datadog Security Labs' full article body on malicious skills and dynamic context (May 11, 2026) — page metadata/byline confirmed, but full text could not be extracted via fetch (returned navigation/job-listing chrome only).
