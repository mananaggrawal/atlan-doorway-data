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

[CONTENT_PLACEHOLDER]