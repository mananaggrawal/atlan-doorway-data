# Verification Log — GTM Work Sample Claims

Verification pass conducted 2026-09-05. Every claim was checked against its primary source directly (GitHub API, npm registry API, live site HTML/JSON, vendor docs/blogs) — not against search snippets or secondary summaries. Where a number differed from the claim, the corrected figure is given.

## Summary Table

| # | Claim | Verdict | Corrected value (if different) | Primary source | Date checked |
|---|-------|---------|--------------------------------|-----------------|--------------|
| 1 | GH issue #28327 exists, quote, state, reactions, duplicates | CONFIRMED | Reactions: 7 (+1). State: CLOSED (not_planned). Exactly 2 issues explicitly closed "as a duplicate of #28327": #33530 and #39403. (#69882 mentions it but was closed not_planned, not duplicate.) | github.com/anthropics/claude-code/issues/28327 (via api.github.com) | 2026-09-05 |
| 2 | GH issue #39403 quote | CONFIRMED | Quote exact, character-for-character. Note: #39403 itself is CLOSED, labeled `duplicate`, state_reason `duplicate` — it was auto-closed as a duplicate of #28327, not resolved independently. | github.com/anthropics/claude-code/issues/39403 | 2026-09-05 |
| 3 | Repo stats (5 repos) incl. anthropics/skills stars | CONFIRMED (with drift) | anthropics/skills: **174,457** stars (claimed 174,451 — off by 6, consistent with live counter drift between when the claim was gathered and now; the figure genuinely is that high, not implausible). Full table below. | api.github.com/repos/... | 2026-09-05 |
| 4 | npm downloads: claude-code 80.2M/mo, 21.5M/wk; `skills` 38.4M/mo, 9.4M/wk | CONFIRMED | @anthropic-ai/claude-code: 80,220,622/mo, 21,450,823/wk. `skills`: 38,365,913/mo, 9,363,514/wk. Both match claimed figures closely. `skills` package **is** the skills.sh / vercel-labs CLI (repository: vercel-labs/skills, description "The open agent skills ecosystem") — not an unrelated package, though the npm name was originally registered by a different party in 2016 and later repurposed. | api.npmjs.org, registry.npmjs.org | 2026-09-05 |
| 5 | skills.sh: 1,320,673 all-time installs; find-skills 3.3M installs; internal contradiction | CONFIRMED | Page's own embedded JSON: `"allTimeTotal":1320673` and "All Time (1,320,673)" tab label — exact match. find-skills: `"installs":3267851` (~3.3M) — exact match to claimed 3.3M. The contradiction is real and present in the live site's own data: one skill (3.27M) shows more installs than the site's stated all-time total (1.32M). | skills.sh (page source / embedded JSON) | 2026-09-05 |
| 6 | JetBrains Aug 2026 survey: 90% weekly, 68% daily, Claude Code 39%/47%, n=15,000+ | CONFIRMED | All figures match exactly (see quotes below). | blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/ | 2026-09-05 |
| 7 | NVIDIA scanned 42,000+ skills, "nearly 1 in 4 could compromise a system", open-source scanner "SkillSpector" | PARTIALLY CONFIRMED | SkillSpector is real and open-source (github.com/NVIDIA/SkillSpector). Actual stats per NVIDIA's own README: **42,447 skills** scanned ("42,000+" ✓), **26.1%** "contain at least one vulnerability", **5.2%** "show likely malicious intent". The claim's "nearly 1 in 4 could potentially compromise a system" is a paraphrase, not a quote — 26.1% is technically just OVER 1-in-4, not "nearly" under it, and it conflates NVIDIA's "vulnerability" metric (26.1%) with system compromise; NVIDIA's own higher-severity figure ("likely malicious intent") is only 5.2%. | github.com/NVIDIA/SkillSpector (README); developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents | 2026-09-05 |
| 8 | ~96,000 skills scanned, 552 confirmed malicious, sourced to vercel-labs/skills#1552 | CONFIRMED (quote) but source is WEAK | Issue exists, is OPEN, filed 2026-06-30 by GitHub user "eeee2345". Quote is exact: "Across ~96,000 skills scanned (ClawHub, skills.sh, MCP registries), 552 were confirmed malicious after manual review." **Caveat: this is a self-reported, unverified claim by the issue filer, promoting their own third-party tool ("ATR"/Agent Threat Rules) in a feature-request issue — not an independent audit, not from vercel-labs, and no supporting report is linked.** Treat as unverifiable primary data, not confirmed fact. | github.com/vercel-labs/skills/issues/1552 | 2026-09-05 |
| 9 | Anthropic Agent Skills launched 16 Oct 2025; agentskills.io spec dated 19-20 Dec 2025 | CONFIRMED (9a exact) / PARTIALLY CONFIRMED (9b circumstantial) | Anthropic launch date: exact match — "Published Oct 16, 2025" / "October 16, 2025". agentskills.io: no explicit on-site "launched on X" statement found; corroborated by GitHub repo `agentskills/agentskills` created 2025-12-16, earliest Wayback Machine capture of agentskills.io on 2025-12-18, and contemporaneous coverage (e.g., Simon Willison's post dated 2025-12-19) — consistent with the claimed 19-20 Dec 2025 window but not a direct quote from the spec site itself. | anthropic.com/news/skills; anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills; web.archive.org/cdx for agentskills.io; github.com/agentskills/agentskills | 2026-09-05 |
| 10 | AWS Agent Registry: preview 9 Apr 2026, GA 31 Aug 2026 | CONFIRMED | Preview: "Posted on: Apr 9, 2026". GA: "Posted on: Aug 31, 2026". Both exact matches. Bonus finding: old `bedrock-agentcore` namespace retires/shuts down **September 17, 2026** (migration window closes). | aws.amazon.com/about-aws/whats-new/2026/04/aws-agent-registry-in-agentcore-preview; aws.amazon.com/about-aws/whats-new/2026/08/aws-agent-registry-generally-available/; docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-faq.html | 2026-09-05 |
| 11 | Claude Code skill-listing budget ~1% of context window, 1,536-char cap per skill description | CONFIRMED | Exact quotes: "The budget scales at 1% of the model's context window." and "each entry's combined text is capped at 1,536 characters regardless of budget." Note: this doc was WRONG until recently (GH issue #47627, filed 2026-04-13, since fixed) — it previously said 250 characters, and a separate/different field-level schema limit ("Maximum 1024 characters" for the raw `description` frontmatter field) also exists and should not be confused with the 1,536-char listing-display cap. | code.claude.com/docs/en/skills (current) | 2026-09-05 |
| 12 | shareskills.ai exists — who runs it, claims, blog post | CONFIRMED | Live SaaS product: "shareskills — Your team's skills, in sync." Author/review/install SKILL.md files as a team; versioned folders, role-aware approvals, MCP-native sync to Claude/Copilot/Cursor/MCP tools. Run by legal entity **McBourne Enterprises** (per its Terms of Service); pricing in AUD suggests an Australian operator. Free/Team (A$4 per extra user/month)/Enterprise tiers. The blog post at shareskills.ai/blog/sharing-is-not-a-library **does exist**, dated 5 September 2026 (today), titled "Claude can now share skills between colleagues. Here is the difference between sharing and a library." | shareskills.ai; shareskills.ai/terms; shareskills.ai/blog/sharing-is-not-a-library | 2026-09-05 |


## Claim 3 detail — full repo stats (api.github.com, checked 2026-09-05)

| Repo | Stars | Forks | Open issues | Created | Last push |
|------|------:|------:|------------:|---------|-----------|
| anthropics/skills | 174,457 | 20,662 | 1,208 | 2025-09-22 | 2026-09-03 |
| anthropics/claude-code | 144,149 | 23,027 | 13,894 | 2025-02-22 | 2026-09-04 |
| vercel-labs/skills | 30,452 | 2,613 | 1,184 | 2026-01-14 | 2026-08-18 |
| openai/codex | 121,711 | 18,669 | 15,414 | 2025-04-13 | 2026-09-05 |
| ComposioHQ/awesome-claude-skills | 74,518 | 8,576 | 1,403 | 2025-10-17 | 2026-08-10 |

anthropics/skills is a real, actively-pushed repo ("Public repository for Agent Skills") — the 174K+ star count is unusual for a docs/skills repo but is genuinely what the API returns, not an error or a mis-scraped figure.

## Exact quotes (verbatim, character-for-character)

**#1 (issue #28327 body):**
> My team would like to share SKILLS we write within the team. We created a repo to keep them central.

Confirmed exact match, no paraphrase.

**#2 (issue #39403 body):**
> Right now, skills are scoped to a single project. For organizations that want to standardize Claude workflows across multiple repos and teams, there's no clean native way to share a common skill library without resorting to symlinks or duplicating skill files everywhere.

Confirmed exact match, no paraphrase.

**#6 (JetBrains blog, blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/):**
> As of May–July 2026, 90% of professional developers were using AI coding agents at work at least weekly in one form or another (local agents or remote cloud agents), with 68% using them daily.

> In May–July 2026, around 39% of professional developers worldwide were using Claude Code at work, up from 18% in January 2026. In the United States, its adoption is even higher at 47% – thus, almost half of US developers are using Claude Code at work.

> We recently ran the Developer Ecosystem Survey 2026 – a large-scale, globally representative survey of more than 15,000 professional developers worldwide, currently in its tenth year.

**#7 (github.com/NVIDIA/SkillSpector README):**
> AI agent skills (used by Claude Code, Codex CLI, Gemini CLI, etc.) execute with implicit trust and minimal vetting. Research shows that 26.1% of skills contain vulnerabilities and 5.2% show likely malicious intent.
> - Dataset: 42,447 skills from major marketplaces
> - Vulnerable: 26.1% contain at least one vulnerability
> - High-severity: 5.2% show likely malicious intent

**#8 (issue vercel-labs/skills#1552 body, filed by user "eeee2345", OPEN):**
> Across ~96,000 skills scanned (ClawHub, skills.sh, MCP registries), 552 were confirmed malicious after manual review.
> In ClawHub specifically (9,676 skills), ATR flagged 182 as CRITICAL — instruction-level attacks that signature-based scanning missed.
> A single threat actor accounted for 354 malicious skills, at a 100% malicious rate across their uploads.

**#10 (AWS release notes, docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-faq.html):**
> September 17, 2026 — Migration window closes. The old bedrock-agentcore namespace shuts down on this date. You lose read/write access to the service and any remaining data in the old namespace. After this date, you must use the agent-registry namespace.

**#11 (code.claude.com/docs/en/skills, current version):**
> descriptions into context so Claude knows what's available. The listing always contains every skill name, but if you have many skills, Claude Code shortens descriptions to fit the listing's character budget, which can strip the keywords Claude needs to match your request. The budget scales at 1% of the model's context window. When the listing overflows, Claude Code drops descriptions starting with the skills you invoke least, so the skills you use most keep their full text.

> the combined description and when_to_use text is truncated at 1,536 characters in the skill listing to reduce context usage.
> ...since each entry's combined text is capped at 1,536 characters regardless of budget. The cap is configurable with skillListingMaxDescChars.

Note: prior to a fix (GH issue anthropics/claude-code#47627, filed 2026-04-13, closed), this same doc incorrectly stated a 250-character per-entry cap left over from before the limit was raised in Changelog v2.1.105. The 1,536 figure is current and correct as of 2026-09-05.

## Notes and caveats for the client

- **Weakest sourcing in the deck:** Claim 8 (96,000 skills / 552 malicious) rests entirely on an unverified assertion inside an open, unresolved GitHub feature-request issue filed by a private individual promoting their own scanning tool. The quote is accurate, but the underlying data has no independent audit trail, no linked report, and no corroboration — do not present it to the client as established fact without this caveat attached.
- **Claim 7 (NVIDIA/SkillSpector)** is real and the headline numbers (42,447 skills, 26.1%/5.2%) are correct, but "nearly 1 in 4 skills could potentially compromise a system" over-dramatizes NVIDIA's own framing, which separates "contains a vulnerability" (26.1%) from "likely malicious" (5.2%, the more apt proxy for "compromise"). Recommend rephrasing to NVIDIA's own language if this appears in a client-facing deck.
- **Claim 3** — the anthropics/skills star count is not an error to flag as "implausible"; it independently verified as accurate at both check points. Treat as confirmed, just note the live-counter drift (174,451 claimed vs. 174,457 now).
- **Claim 9b** (agentskills.io spec date) could not be confirmed via an explicit on-site statement; it rests on circumstantial but consistent triangulation (repo creation date, Wayback Machine first capture, contemporaneous external coverage). Flag as corroborated-but-not-primary-sourced if precision matters.
- All GitHub API lookups above were made via an unauthenticated api.github.com session from the user's local device (the cloud sandbox's proxy blocks unauthenticated GitHub API access entirely, returning "GitHub access to this repository is not enabled for this session").
