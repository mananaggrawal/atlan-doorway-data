# Community Signals: Skills Sharing, Sprawl, Trust, Counter-Evidence
Pulled 2026-09-05. Verbatim quotes only (<=50 words), tagged [verified] (fetched directly) or [reported] (from search snippet/secondary summary, not independently opened).

## B1 — SHARING (team skill management, internal libraries, onboarding, versioning)

### Zachary Proser — "Claude Skills as Self-Documenting Runbooks/Processes" — personal blog (zackproser.com) — Oct 21, 2025 — https://zackproser.com/blog/claude-skills-internal-training — [verified]
> "Most teams are quietly rediscovering the same AI workflows in parallel... that tribal knowledge lives in DMs, personal notes, or one-off scripts."
> "The same artifact that a human can read (SKILL.md) is the one Claude executes—reviewable in PRs, testable in CI, and distributable to the whole team."
> "When someone figures out a useful workflow... they can package it up and share it. The entire team levels up together, building a shared library."
> "If you can write a README and some basic code, you can create a skill. And once you do, you've got a distributable asset that makes your entire team more capable."
Why it matters: earliest (Oct 2025, days after launch) explicit framing of skills as a team-knowledge-sharing mechanism, not just a personal productivity trick. Strong discovery-interview target.

### Claude Fast blog (byline unclear; site linked to @AbdoMobayad on X) — "Claude Code Plugins: From Personal Setup to Org Standard" — claudefa.st — date not shown on page — https://claudefa.st/blog/tools/mcp-extensions/plugins-distribution — [verified]
> "The pattern shows up in every team that adopts Claude Code seriously... None of it travels. New hires inherit a blank `.claude/` folder and a Slack thread of partial screenshots."
> "A plugin bundles skills, hooks, MCP server configs, sub-agents, slash commands, and LSP definitions into one installable package... a teammate's harness becomes yours, versioned, namespaced, and updatable."
> "One engineer builds a working personal setup... Package as a plugin... Roll out to one team... Expand based on feedback... Standardize."
> "Set it [explicit semver version], and users only receive updates when you bump the version. Omit it (and host in git), and the commit SHA becomes the version, so every push counts as a new release."
> "A harness that lives on one developer's machine is a liability. A harness that installs in one command is leverage."
Why it matters: names the exact failure mode (blank .claude/ folder for new hires) a governed registry fixes, and lays out a full personal-to-org lifecycle with explicit versioning mechanics (semver vs. commit-SHA-as-version).

### kiannidev — "Team Onboarding With Claude Code Plugins and Skills" — HeyClaude (heyclau.de) — June 14, 2026 — https://heyclau.de/entry/guides/team-onboarding-with-claude-code-plugins-and-skills — [verified]
> "A curated plugin bundle gives new hires the same skills, hooks, commands, and MCP integrations veterans use, reducing workflow variance in AI-assisted work."
> "Storage location determines who can use a skill. Standardize on the scope each onboarding skill belongs to before rollout."
> "Day-one setup, week-one exercises, and month-one governance checkpoints keep adoption measured rather than chaotic."
> "Project skills capture review norms, testing commands, and domain vocabulary so new contributors do not rediscover conventions through trial and error."
> "Champion kit materials identify advocates who answer workflow questions, collect feedback, and escalate policy exceptions through proper channels."
Why it matters: closest thing found to a formal team rollout playbook, with explicit "governance checkpoints" language — mirrors what a governed registry product would sell against.

## B2 — SPRAWL (duplicates, wrong invocation, context budget, staleness)

### shimo4228 — "15 Days of Skill Sprawl in Claude Code — Lessons from 3 Audits" — DEV Community — Feb 22, 2026 — https://dev.to/shimo4228/15-days-of-skill-sprawl-in-claude-code-lessons-from-3-audits-27em — [verified]
> "If you have too many skills, they get silently truncated. More is not better."
> "Swift skills and Python skills, same folder."
> "As long as you keep developing, skills keep growing. So auditing has to be recurring too."
> "Zenn textlint workarounds sitting in global are useless for other projects."
Why it matters: first-hand, dated account of truncation at the Discovery stage (skills silently dropped from context), duplicate/misplaced skills across languages, and a claim that manual audits every 1-3 days were needed — a concrete personal-cost data point for the sprawl thesis. Discovery-interview target (documents 3 self-run "audits").

### Luis Chavez-Mattos, Director of Product — "Context Rot: Claude Code Skills, Bloated Files" — MindStudio blog — March 24, 2026 — https://www.mindstudio.ai/blog/context-rot-claude-code-skills-bloated-files — [verified]
> "Context rot — a gradual degradation in agent performance caused by skill files that have grown too large, too dense, or too cluttered with information the agent doesn't actually need at any given moment."
> "A 500-token `CLAUDE.md` costs you 500 tokens on every single inference. A 12,000-token skill file costs 12,000 tokens — every time."
> "If your skill files consume 20,000 tokens out of a 200,000-token context, that's 10% of total capacity gone before a single line of code is read."
> "A practical rule of thumb is to keep it under 2,000-3,000 tokens (roughly 1,500-2,000 words)."
Why it matters: quantifies the context-budget cost of skill bloat in concrete token math, which is the mechanism behind "wrong skill invocation" and discovery truncation.

### Michael Jovanovich — "Scaling Claude Code Skills Without Burning Context" — Substack (responseawareness.substack.com) — Nov 27, 2025 — https://responseawareness.substack.com/p/scaling-claude-code-skills-without — [verified]
> "Every skill's title and description is always in Claude's context. Five skills? Fine. Twenty skills? You're burning tokens showing Claude options it doesn't need for the current task."
> "With built-in skills, adding more expertise costs more context on every task. With semantic discovery, adding more expertise costs nothing until it's relevant."
Why it matters: pins "twenty skills" as the informal point where naive discovery starts to hurt — an early, specific threshold claim relevant to sizing an ICP. Note: article's own numbers (10/50/100 skills) are stated as illustrative scenarios, not a measured typical count — flagged, not used as a hard baseline.

## B3 — TRUST (security: prompt injection, secrets, supply chain, review)

### SentinelOne — "When Your AI Coding Plugin Starts Picking Your Dependencies: Marketplace Skills and Dependency Hijack in Claude Code" — Jan 6, 2026 — https://www.sentinelone.com/blog/marketplace-skills-and-dependency-hijack-in-claude-code/ — [verified]
> "These same skills often run with extremely high privilege and very little transparency on how they make decisions or where the code and dependencies are coming from."
> "When the developer asks the agent to install a common Python library, that skill quietly redirects the install to an attacker-controlled source, ensuring a trojanized version of the library is pulled into the project."
> "Marketplace plugins are not one-off interactions. Once enabled, their skills remain available across sessions and will continue to shape how the agent behaves in the future."
> "If your coding assistant can fetch and execute code on your behalf, every plugin installed joins your trust boundary."
> "Plugin marketplaces and third-party skills are now part of the software supply chain whether teams realize it or not."
Why it matters: names a concrete attack (silent dependency-source hijack via an installed skill), and frames unreviewed skill installs as a supply-chain expansion — core justification for a governed registry.

### PromptArmor — "Hijacking Claude Code via Injected Marketplace Plugins" — Substack (promptarmor.substack.com) — Oct 16, 2025 — https://promptarmor.substack.com/p/hijacking-claude-code-via-injected — [verified]
> "The Plugin bypasses Claude's human-in-the-loop protections using a malicious hook."
> "A user installs a malicious Marketplace and Plugin, typically after finding it via a registry [such as claudecodemarketplaces.com]."
> Malicious marketplaces appear in registries almost immediately — "they will list a malicious Marketplace within an hour of an attacker making it public."
Why it matters: earliest dated (within days of the plugin/marketplace feature shipping) proof-of-concept that unmoderated marketplaces get weaponized fast — directly supports "review before adoption."

### Benjamin Kapner — "Securing Claude Code Plug-ins: Best Practices for Repository Security" — Red Hat Developer — Aug 18, 2026 — https://developers.redhat.com/articles/2026/08/18/securing-claude-code-plug-ins-best-practices-repository-security — [verified]
> "Installing a plug-in gives third-party code full access to your terminal, local files, and environment variables."
> "The marketplace runs on an implicit trust model: no centralized vetting, no code signing, no runtime sandboxing."
> "At least one other person reviews every pull request, and no one is exempt."
> "Review the change, not the description. Read what the code does, paying attention to anything touching credentials."
> "A plug-in with one contributor and no reviews has exactly one account standing between you and compromise."
Why it matters: a large enterprise vendor (Red Hat) publishing internal-repo governance practices (branch protection, mandatory review) for Claude Code plugins as of Aug 2026 — signals this has become a recognized enterprise engineering concern, not a niche worry.

### Datadog Security Labs — Nick Frichette, Ryan Simon — "Malicious Coding Agent Skills and the Risk of Dynamic Context" — May 11, 2026 — https://securitylabs.datadoghq.com/articles/malicious-skills-supply-chain-risks-in-coding-agents-with-dynamic-context/ — [reported: byline/date confirmed, full body text not retrievable via fetch]
Title alone (per page metadata) references "malicious Claude Code skills abusing dynamic context commands to bypass prompt injection defenses" — logged as a named, dated source to revisit with a direct browser render; no verbatim quote captured because the fetch returned only page chrome, not article body.

## B4 — COUNTER-EVIDENCE (git repo is enough / over-engineering / skills overrated)

### vibecoding.app — "Skills.sh Review (2026): One Command, Better AI Agents?" — 2026 — (quoted via secondary fetch of rywalker.com/research/skills-sh) — [reported]
> "Skills.sh has no quality control. Anyone can create a skill, host it on GitHub, and tell people to install it."
Why it matters: a registry/marketplace reviewer itself flags the lack of vetting as the central weakness — the strongest available argument that an unvetted directory does not solve the trust problem, which is exactly the gap a *governed* registry claims to close (double-edged: also usable as counter-evidence that registries as currently built add little).

### @pablocubico (X/Twitter, via Ry Walker research digest) — Jan 2026 — quoted in https://rywalker.com/research/skills-sh — [reported, secondhand]
> "Unpopular opinion: 80% of skills in skills.sh are AI slop. Go for the vendor-provided ones."
Why it matters: an early, blunt community reaction to the open marketplace model — argues the long tail of community-submitted skills is low-value noise and only vendor-curated skills are worth trusting, i.e. an implicit vote for curation/governance over open sharing, but also a knock against "more skills, shared widely" as inherently good.

### Steven Gonsalvez — DEV Community comment, quoted in https://rywalker.com/research/skills-sh — [reported, secondhand]
> "The pattern is right and the directory is growing fast. Worth checking before you write a skill from scratch."
Why it matters: mild counter to NOT building your own — suggests checking existing public skills before authoring, i.e. reuse-over-rebuild without needing team infrastructure.

### NULL RESULT — no direct, explicit "a git repo is all you need, skip the registry/marketplace" essay was found and confirmed by full-text fetch.
Searches run that did not surface a clear, quotable B4 argument (logged per task instructions):
- `"just a git repo" OR "over-engineering" Claude Code skills marketplace unnecessary` — no on-point essay; returned general best-practices roundups.
- `Claude Code skills overrated OR unnecessary OR "don't need" marketplace Hacker News` — surfaced "You don't need MCP. You need Claude Skills." (HN item 45948490) which argues skills > MCP, not skills-are-overrated; HN comment fetch itself returned HTTP 429 and could not be read.
- `"skills.md" OR "SKILL.md" "just use a" README overrated skeptical Claude Code agent skills` — no on-point result.
- `"skills are overrated" OR "skills are a fad" Claude Code Codex agent skills criticism` — no on-point result.
- Lobsters search surfaced general Claude Code threads (e.g. "Taming Claude Code") but no thread specifically arguing against shared/registry-based skill distribution.
Honest read: the strongest counter-signal found is not "skills are unnecessary" but "the current open/unmoderated marketplace model (skills.sh-style) is low-trust and low-quality," which argues for governance rather than against skills sharing per se. No credible writer was found making the harder claim that a shared skill registry (governed or not) is solving a non-problem.

## Other notable dated context (not strictly B1-B4 but load-bearing for timeline)

### Simon Willison — "Agent Skills" — simonwillison.net — Dec 19, 2025 (updated Dec 20, 2025) — https://simonwillison.net/2025/Dec/19/agent-skills/ — [verified]
> "It is a deliciously tiny specification - you can read the entire thing in just a few minutes."
> "It's also quite heavily under-specified - for example, there's a `metadata` field... Clients can use this to store additional properties not defined by the Agent Skills spec."
> "The Agent Skills homepage promotes adoption by OpenCode, Cursor, Amp, Letta, goose, GitHub, and VS Code."
> "Notably absent is OpenAI, who are quietly tinkering with skills but don't appear to have formally announced their support just yet." (Update Dec 20: OpenAI added Skills to Codex docs days later.)
Why it matters: independent, credible technologist's read of the spec becoming a cross-vendor open standard, dated two months after Anthropic's original Oct 2025 launch — useful as a neutral timeline anchor.

## Discovery-interview candidate authors (see also prospect_candidates.md)
- Zachary Proser (zackproser.com) — wrote the earliest explicit "shared skill library" framing.
- shimo4228 (dev.to) — ran 3 self-audits of personal skill sprawl over 15 days.
- Michael Jovanovich (responseawareness.substack.com) — building/writing on semantic skill discovery at scale.
- kiannidev (heyclau.de) — wrote a full team-onboarding playbook for plugins/skills.
- Benjamin Kapner (Red Hat Developer) — publishing enterprise governance practices for Claude Code plugins.
- Ry Walker (rywalker.com) — running an independent research beat tracking skills.sh and the OpenAI skills catalog.
