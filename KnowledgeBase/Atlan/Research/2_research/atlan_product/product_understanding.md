# What Atlan Agent Registry actually is — from the three internal videos
Written 2026-09-05 from full transcripts in this folder. Every claim below is traceable to a transcript.

## One-line
A governed, cross-harness home for the *context* behind agents — skills, instructions, tools, knowledge, permissions — giving each object a stable identity plus owners, versions, dependencies, access, usage, evals and traces, and distributing them into Claude Code / Codex / ChatGPT through plugins and MCP.

## The origin problem (AI Engineer talk, Prukalpa, 20:53)
- Framing: performance = intelligence x context. Intelligence 1000x'd; context barely moved. *"AI doesn't know your business. We fix that."*
- Cited: ~1 in 5 AI use cases reach production; 56% of CEOs report zero financial benefit from AI today. **[unverified — need original sources before reusing]**
- Atlan's own three eras:
  1. Named single-purpose agents per function. Building took 5 minutes; context engineering took forever. Agents lived on islands, each with its own memory. No traceability.
  2. General-purpose agents + a shared context layer. Domain experts author skills (best SEO person writes the SEO skill). **300 skills, 40 agents in 6 months.**
  3. Problems at scale — the actual product spec: dependency management (comp-intel skill → positioning skill → battle-card skill; one change breaks downstream), skill drift and staleness, unclear ownership and quality accountability, security (secrets in ENV files, people downloading public skill repos), and portability across harnesses (Relevance → ADK → Glean → Claude Code → Codex; context trapped and lost at each switch).
- Her name for the answer: **"GitHub for context."** Lifecycle, collaboration, versioning; skill profiles, self-learning loops, quality management, security posture, dependency graphs with maintainers and approvers; every trace feeding back into a compounding loop.

## The product, screen by screen (product demo, "Rohan", 6:50)
1. **Desktop app** that integrates with the harnesses and, on first run, **scans the skills and sessions already on your laptop** — you don't start from an empty registry. (This is the activation mechanic. It matters enormously for GTM: time-to-value is a scan, not a migration.)
2. **Workspaces** — Personal (private) plus department workspaces (Sales, Marketing, CS, Engineering). Access-scoped; you only see yours.
3. **Reporting** for an "AI transformation leader": spend, runs, active agents, cost per run, token use, trends; rank agents by spend or highest-cost run; for Claude Code / Codex seats, which users are active and how often sessions use *governed* skills.
4. **Agent 360** — instructions, files, tools, sessions and setup for one agent, plus **Relationships** (which skills/agents it depends on, so "changes do not happen in the dark") and **Usage** (behaviour, cost, users, models over time). Drill into a run and improve the agent from your harness.
5. **Discovery / search** — the stated reason: *"when people cannot find what already exists, they create duplicate skills."* Also people lookup: a new joiner can see which tools, models and skills a teammate actually uses.
6. **Skill detail (example: a GTM deck skill)** — what it does, when it triggers, who uses it ("gives me trust before I adopt it"). *"Source is more than a prompt"* — instructions plus theme files, colours, fonts, brand assets.
7. **Versioning** — every update creates a version; map usage to a version; pin an agent to a stable release; spot outdated instructions still in use.
8. **Dependencies** — the deck skill depends on a marketing-owned messaging skill.
9. **Consolidation** — discovery surfaces a near-duplicate slide skill so maintainers merge instead of letting both drift.
10. **Usage + MCP loop** — query these insights from inside your harness via Atlan's MCP; open a real trace instead of guessing.
11. **Roadmap, explicitly "in development": automated security scanning** of every new/updated skill for prompt injection and hard-coded credentials.
12. **Distribution** — *"Atlan distributes workspace skills through plugins, so users keep their chosen harness without installing every skill by hand."* Same governed GTM deck skill available in Codex and Claude Code, access scoped by workspace, one governed source.

Opening quote worth reusing: *"Context is a team sport. No single team holds the whole truth."* And: *"Atlan is a multi-harness company. We use Claude Code, Codex, ChatGPT, and the recently launched Grok bot."*

## The software factory demo (1:43) — the developer/CI story
One PR, one governed agent, its evidence:
1. PR opens → GitHub Actions starts a PR review bot in CI.
2. The bot follows **review skills stored beside the code**, so review policy changes through the same Git workflow.
3. **Daytona** provides a clean sandbox — the review runs away from the developer's laptop, so every PR starts from the same environment.
4. Atlan gives the bot a **durable identity**: Overview (what it does, where it runs), Relationships (the skills synced from GitHub, so anyone sees which review policy it depends on), Usage (CI result linked back), Trace (steps in order, which skills ran, why it requested changes) — *"an audit trail when a review needs investigation."*
5. Improvement loop: pull trace history via the **Atlan API**, find repeated misses, and those patterns *"can become a proposed skill update, but never an automatic rule change"* — human approval gated.

## What this tells us for GTM
- **The product is a governance/observability/distribution layer across harnesses people already use.** It is not an agent builder and not a harness. It does not ask anyone to switch tools — a very low-friction adoption story.
- **The activation moment is the laptop scan.** Individual value on day one (find your own skills, see your spend), team value on day two (dedupe, dependencies, distribution).
- **The pain is felt at ~50-300 skills**, not at 5. So the ICP is a team already deep in Claude Code/Codex, not a team starting out.
- **Three distinct personas already visible in the demo**: AI transformation leader (spend/adoption ROI), maintainer (quality, dependencies, drift), end user (find and trust a skill). Plus the developer in the software factory story.
- **Named integrations to date:** Claude Code, Codex, ChatGPT, Grok; GitHub + GitHub Actions; Daytona; MCP; Atlan API; plugins as the distribution mechanism.
- **No pricing mentioned anywhere.**
