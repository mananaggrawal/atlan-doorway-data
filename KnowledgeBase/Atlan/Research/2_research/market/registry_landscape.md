# Registry & skill-distribution landscape — first pass
Researched 2026-09-05 via web. Confidence tags: [verified] = read the primary source today; [reported] = secondary/AI-summarised, not API-verified; [assumption] = inference.

## AWS Agent Registry (the loudest competitor)
- [verified] Launched preview ~31 Aug 2026; now GA under an `agent-registry` namespace. The preview `bedrock-agentcore` namespace retires **17 Sep 2026**. https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-concepts.html
- [verified] Registers 4 record types: `MCP` (server + tool schemas), `AGENT` (A2A agent cards), `SKILL` (name, description, optional package/repo, optional markdown docs), `CUSTOM` (arbitrary JSON).
- [verified] Data model: `name` + `recordVersion` as dedup key; records live in a per-account registry with auth + approval config; tags for cost allocation/access.
- [verified] Discovery: `SearchDiscoverableRegistryRecords` (semantic/keyword), list/get browse APIs, and `InvokeRegistryMcp` so any MCP client can query the registry as a tool.
- [verified] Governance: IAM/JWT inbound auth, OAuth/IAM outbound for sync, lifecycle Draft → Pending Approval → Approved/Rejected → Deprecated. Consumers see only approved records.
- [verified] **No usage tracking, no evals, no execution traces** in the concepts doc. The launch blog explicitly lists as *future*: security vulnerability scanning, compliance evals, automated dedup detection, invocation-time policy enforcement, cross-org/public registries, "enhanced observability and dependency graphs." https://aws.amazon.com/blogs/machine-learning/manage-agents-tools-and-skills-at-scale-with-aws-agent-registry/
- [verified] Named IDE integrations: Kiro and Claude Code. Customers named in launch: Sony, Mitsubishi Electric, Southwest, PepsiCo, Syngenta, Amdocs.
- **Read:** AWS registers and approves. It does not evaluate, trace, or measure. That gap is exactly where Atlan's demo lives (usage, traces, dependency graph, cost). Also: it is AWS-account-scoped, so it does nothing for a team whose skills live on laptops and in GitHub.

## Google — Gemini Enterprise Agent Platform "Skill Registry"
- [reported] Mutable `Skill` + immutable `Skill Revision` snapshots (real version history, stronger than AWS's flat versioning). Required `SKILL.md`, 500MB uncompressed / 10MB compressed limits, async validation, plus a `gcp-skill-registry` meta-skill so agents can manage skills themselves. https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/skill-registry
- **Read:** second hyperscaler shipping a skills-specific registry. Cloud-locked.

## OpenAI — Skills + Plugins
- [verified] "Skills" = reusable shareable workflows, authored in chat / editor / upload, living in ChatGPT's Plugin Directory > Skills tab. Gated to Business/Enterprise/Healthcare/Edu. Admin toggles: enable skills, enable uploading, publish to workspace. https://help.openai.com/en/articles/20001066
- [verified] Plugins package skills + connected apps + templates; admins can **import a plugin marketplace from a public/private GitHub repo with daily sync** — effectively an enterprise registry mirror. https://help.openai.com/en/articles/20001256
- **Read:** closest architectural analog (identity + permissions + workspace publishing) but closed, single-vendor, workspace-local; no cross-tool identity, no versioning language, no evals/traces disclosed.

## skills.sh (Vercel Labs) — the distribution precedent
- [verified] Launched 20 Jan 2026. Install is one command: `npx skills add <owner/repo>`. Directory + leaderboard (all-time / trending / hot) across many agent platforms. https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem | https://skills.sh/
- [reported] Site claims ~1.31M total installs; top skill ("find-skills") ~3.3M installs; several past 500K. `vercel-labs/skills` reported ~30.4k GitHub stars — **not API-verified, treat as directional.**
- [verified] No approval, no versioning, no ownership, no governance layer. Skills are just GitHub repos.
- **Read:** proves the distribution loop works at scale and that a one-command install is the unit of adoption. It is the opposite end of the spectrum from AWS: all distribution, zero governance.

## MCP Registry — the closest precedent for how big an open registry gets
- [verified] Preview launched 8 Sep 2025, announced with ~9 companies; open OpenAPI spec permitting public sub-registries and private enterprise mirrors; denylist-based moderation; no data-durability guarantee in preview. https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/
- [reported] `modelcontextprotocol/registry` ~6.9k stars. Third-party server counts vary wildly (12,000 to 20,100+) across PulseMCP/Smithery/Glama — no authoritative figure.
- [reported] **Update, 2026-09-05:** MCP has since been donated to a new Agentic AI Foundation, with the registry standing as an official surface at modelcontextprotocol.io/registry/about. Google search interest in "mcp registry" (1,600/mo) and "mcp server registry" (260/mo) spiked in this same window — `../numbers/search_demand_semrush.md` §4. Not independently re-verified against Anthropic's own announcement with a quote/date the way the rest of this file's [verified] claims are; flagged for a second pass before it enters the deck.
- **Read:** the sub-registry / mirror pattern is the interesting precedent for Atlan — be the governed private mirror of a public commons. The precedent just got more load-bearing, not less: the public commons it describes is now actively growing and getting search demand, which strengthens rather than weakens the case for someone governing the private slice of it.

## Claude Code skills — the mechanics that constrain any distribution loop
- [verified] A skill = `SKILL.md`: YAML frontmatter (`name`, `description` used for auto-invocation matching, `allowed-tools`, `context`, `paths`, `hooks`, `model`, `agent`, etc.) + markdown instructions, with `!`command`` injection and `$ARGUMENTS` substitution. https://code.claude.com/docs/en/skills
- [verified] Precedence: Enterprise (managed settings) > Personal `~/.claude/skills/` > Project `.claude/skills/` > Plugin `<plugin>/skills/` (namespaced `/plugin:skill`) > nested project.
- [verified] Plugins bundle skills/commands/agents and are distributed via **marketplaces** — a first-party distribution mechanism that already exists. This is almost certainly how "Atlan distributes workspace skills through plugins" in their demo works.
- [reported] **Update, 2026-09-05:** Anthropic shipped its own Claude Code plugin marketplace (~Feb 2026). "claude code plugin marketplace" search volume (880/mo, $9.43 CPC) spiked off that launch specifically — `../numbers/search_demand_semrush.md` §4. Read: the first-party distribution mechanism above is no longer dormant, it is an actively marketed surface competing for the same "where do I get skills" demand any Atlan-branded distribution loop would want.
- [verified] **Skill listing budget: ~1% of context window, 1,536 chars per skill.** Too many ungoverned skills measurably degrades auto-invocation. This is the single best technical argument for curation/governance — sprawl is not just messy, it makes the agent worse.
- [verified] Format fragmentation: Claude Code's frontmatter is a superset of the open Agent Skills spec (agentskills.io) used by claude.ai/Skills API, which only allows `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. Claude-Code-only fields hard-fail there.

## Where the white space is
1. **Nobody ships distribution + governance together.** skills.sh has millions of installs and zero governance. AWS/Google have governance and zero distribution ergonomics, locked to one cloud. OpenAI has permissions but is a walled garden. **Caveat added 2026-09-05:** Anthropic's own plugin marketplace + relaunched MCP registry are the entrants most likely to close this gap first, since they own the distribution surface already — see the two "Update" notes above and `../numbers/search_demand_semrush.md`.
2. **Nobody ships evals + usage + traces for skills.** AWS explicitly defers it. That is the substance of Atlan's demo.
3. **Format normalisation across dialects** (Claude Code superset vs Agent Skills spec vs OpenAI vs Google) is an unglamorous but real technical wedge.
4. **The context-budget problem** is a concrete, felt, today pain for anyone with >20 skills — a rare case where governance has an immediate selfish payoff for an individual, not just a compliance payoff for an org.

## Unverified / to re-check before anything enters the deck
- All GitHub star counts (skills.sh 30.4k, anthropics/skills reported 168.9k — implausible, likely wrong).
- skills.sh install numbers and skill count.
- MCP server totals.

## Distribution × governance × intelligence, compressed (added 2026-09-05)
A one-glance version of "Where the white space is" above, for deck use:

| Product | Distribution | Governance | Usage / evals / traces |
|---|---|---|---|
| skills.sh | Strong (millions of installs) | None | None |
| AWS Agent Registry | Account-scoped only | Yes (approval workflow) | Explicitly deferred to roadmap |
| Google Gemini skill registry | Account-scoped only | Yes (versioned, revision history) | Not disclosed |
| OpenAI Skills / Plugins | Workspace-scoped | Yes (admin gating) | Not disclosed; closed ecosystem |
| Atlan's opening | Unproven — this is what the campaign has to earn | Yes | **The differentiator — nobody ships this for skills today** |

This doesn't change the conclusion already reached in this file; it just compresses it into the shape a slide actually needs.
