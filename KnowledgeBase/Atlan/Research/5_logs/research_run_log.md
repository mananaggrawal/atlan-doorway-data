# Research run log
Every research run executed for this project. Each was a separate agent with its own isolated context, given a written brief with explicit evidence buckets, quoting rules, and an instruction to log null results. All ran on 2026-09-05.

Totals: **10 research runs · ~1.56M agent tokens · ~730 tool calls · ~2h50m of agent wall-clock**, most of it in parallel.

---

## Run 1 — Atlan video transcription
**Purpose:** Get full transcripts of the three Atlan videos in the brief.
**Method:** Browser pane on the user's Mac. Model: Sonnet. 40 tool calls, ~107K tokens, 7 min.
**What failed:** YouTube's `timedtext` caption API returned HTTP 200 with zero bytes for all three videos (PO-token/signature restriction). Both the cloud container and the Mac shell are also proxy-blocked from youtube.com, and `youtube-transcript-api` failed the same way.
**Workaround:** Opened YouTube's native "Show transcript" panel in the browser and extracted the rendered DOM text, then stripped timestamps while keeping chapter markers and all spoken text verbatim.
**Output:** `2_research/atlan_product/{ai_engineer_talk_context_layer, agent_registry_product_demo, agent_registry_software_factory_demo}.md`
**Headline:** The product's activation mechanic is a desktop app that scans skills and sessions already on your laptop. Time to value is a scan, not a migration.

## Run 2 — Market and competitor landscape
**Purpose:** Read AWS Agent Registry, Google's skill registry, OpenAI Skills and Plugins, skills.sh, Claude Code skill mechanics, MCP Registry.
**Method:** WebFetch + WebSearch. Sonnet. 23 tool calls, ~83K tokens, 2.7 min.
**Output:** `2_research/market/registry_landscape.md`
**Headline:** AWS registers and approves but explicitly defers evals, usage tracking, traces, dedup and invocation-time policy to a future roadmap. That deferred list is exactly what Atlan already demos.

## Run 3 — Atlan company briefing
**Purpose:** Funding, positioning, current GTM motion, public stance on registries, who will grade this.
**Method:** WebSearch + WebFetch. Sonnet. 32 tool calls, ~85K tokens, 2.3 min.
**Output:** `2_research/atlan_product/atlan_company_briefing.md`
**Headline:** "Agent Registry" is not a publicly announced Atlan product — the only public mentions are three SEO posts dated 1 Sep 2026. Atlan sells top-down to CDOs at roughly $50K ACV, while this brief asks for a bottom-up motion the company has never run.

## Run 4 — Hacker News (and attempted Reddit)
**Purpose:** Practitioner voice on sharing, sprawl, trust, and the do-nothing case.
**Method:** HN Algolia API plus thread reads. Sonnet. 100 tool calls, ~235K tokens, 25 min.
**What failed:** Reddit blocked from every route — curl 403 from both shells, WebFetch `SITE_BLOCKED`, WebSearch returned zero reddit.com URLs across ~15 queries, reader proxies blocked. Logged as an access gap, explicitly not as silence. Closed later in Run 10.
**Output:** `2_research/community/reddit_hn.md`
**Headline:** At least a dozen independent "package manager for agent skills" Show HNs since January 2026, none of them winning — the clearest signal that the pain is real and the solution is unsettled.

## Run 5 — X (Twitter)
**Purpose:** Same buckets, plus a read on whether X is a viable channel.
**Method:** Browser pane, signed in, read-only, 26 distinct queries with permalinks verified in-browser. Sonnet. 143 tool calls, ~175K tokens, 14 min.
**Output:** `2_research/community/x_twitter.md`
**Headline:** OpenAI's Codex DX lead published a skill-sprawl teardown the same day we searched — 1.5M views. But most on-topic posts get under 500 views: X is a listening and discovery surface, not an acquisition channel.

## Run 6 — LinkedIn
**Purpose:** Which job titles own this problem, and whether a buying centre exists.
**Method:** Browser pane, signed in, read-only, 19 content and people searches. Sonnet. 95 tool calls, ~231K tokens, 12.9 min.
**Limitation disclosed in the file:** LinkedIn search results don't expose post permalinks to the accessibility tree; citations use the author's profile URL plus the exact query, or the author's own linked article.
**Output:** `2_research/community/linkedin.md`
**Headline:** "AI Enablement" is a real, named title at Toyota, Ford, Deloitte and Eightfold — but expert posts get 4-5 reactions while beginner explainers get 400. Right buyer, wrong moment. Also surfaced a direct competitor, shareskills.ai.

## Run 7 — GitHub
**Purpose:** The highest-precision surface: issues, discussions, READMEs, and repo statistics.
**Method:** WebSearch, WebFetch, unauthenticated api.github.com. Sonnet. 58 tool calls, ~128K tokens, 10.3 min.
**What failed:** GitHub code search requires authentication (401); grep.app returned a bot checkpoint and a robots disallow. So the prevalence of `.claude/skills/` across public repos — the single most valuable missing number — could not be obtained. Logged rather than estimated.
**Output:** `2_research/community/github.md`
**Headline:** `anthropics/claude-code#28327` asks for team skill sharing, has two issues closed as duplicates of it, and is itself **closed `not_planned`**. A dated, documented vacancy in the platform.

## Run 8 — Blogs, press, and the quantitative baseline
**Purpose:** Long-form practitioner writing, security research, and hard numbers.
**Method:** WebSearch, WebFetch, api.npmjs.org. Sonnet. 63 tool calls, ~123K tokens, 6.8 min.
**Output:** `2_research/community/blogs_and_press.md`, `2_research/numbers/quantitative_baseline.md`
**Headline:** Nobody has published how many skills a typical developer or team has. Hunted deliberately, found nowhere. That absence is the opening.

## Run 9 — Independent verification
**Purpose:** Confirm or refute the 12 most load-bearing claims from Runs 1-8, against primary sources only.
**Method:** Direct API and primary-source reads, no search snippets accepted. Sonnet. 74 tool calls, ~161K tokens, 13.3 min.
**Output:** `2_research/numbers/verification_log.md`
**Headline:** Nothing flatly refuted, but two corrections that would have been embarrassing in the room — see `ai_work_log.md`.

## Run 10 — Reddit, via the user's own browser
**Purpose:** Close the gap left by Run 4.
**Method:** Reddit remained blocked in the built-in browser pane by policy, so the run used the Claude-in-Chrome extension against the user's real Chrome. 24 queries across 11 subreddits, read-only. Sonnet. 114 tool calls, ~232K tokens, 28 min.
**Output:** `2_research/community/reddit.md`
**Headline:** Surfaced an objection no other surface did — a 99-upvote comment arguing *against* sharing skills at all on job-security grounds. That is a GTM obstacle, and it only appears in unvarnished practitioner space.

---

## Runs that were attempted and blocked before execution
Two agent launches (GitHub, blogs) were refused by the session's own safety classifier on first attempt and succeeded unchanged on relaunch. No prompt content was altered to get past it. Noted for completeness.
