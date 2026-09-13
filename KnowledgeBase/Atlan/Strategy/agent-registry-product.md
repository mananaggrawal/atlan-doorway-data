# Atlan Agent Registry — product facts

From Atlan's own internal demos and talks (name not yet publicly announced as of 2026-09-05).

Atlan Agent Registry is a governed, cross-harness home for the context behind agents — skills, instructions, tools, knowledge, permissions. It gives those objects stable identity plus owners, versions, dependencies, access, usage, evals and traces, and distributes them into Claude Code / Codex / ChatGPT via plugins and MCP. Internally described as "GitHub for context." It is not an agent builder and not a harness — it sits across the tools teams already use, so adoption requires no tool switch.

**Activation mechanic:** a desktop app that, on first run, scans the skills and sessions already on your laptop — time to value is a scan, not a migration.

**Product surfaces seen in the demo:** workspaces (personal + department, access-scoped); reporting (spend, runs, cost per run, token use, adoption of governed skills); "Agent 360" (instructions/files/tools/sessions plus a relationships dependency graph and usage); skill discovery and search; versioning with pinning; dependency links between skills; duplicate consolidation; traces; MCP querying from inside the harness; distribution via plugins. Security scanning for prompt injection and hardcoded credentials is explicitly on the roadmap, not shipped.

**Origin:** Atlan built roughly 300 skills and 40 agents internally over six months on Claude Code + Codex, and hit dependency, drift, ownership, security and portability problems at that scale.

**How to apply:** the pain lands at roughly 50-300 skills, not at 5 — so Atlan's own natural ICP is a team already deep in Claude Code/Codex. Personas visible in the product: the AI transformation leader (spend/ROI), the maintainer (quality/drift), the end user (find and trust a skill), the developer (CI/software factory). Strategic tension worth naming: Atlan sells top-down to CDOs at roughly $50K ACV today, but this exercise asks for dramatic bottom-up distribution before optimizing for that traditional enterprise motion — reconciled as: the registry is the wedge into the context layer, not the whole sales motion.