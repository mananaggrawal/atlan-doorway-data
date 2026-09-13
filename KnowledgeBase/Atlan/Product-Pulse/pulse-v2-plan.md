# Atlan Pulse v2 — build plan

The current spine for the Pulse build, replacing the earlier CLI-first scoping.

**Locked decisions:**
1. Sync is agent-push + plugin-pull: Claude calls Pulse MCP tools to push; Pulse serves a Claude plugin marketplace to pull back.
2. The health engine is built from scratch, invoked via MCP against selected skills. Output is a shareable, Twitter-optimised card plus detailed per-skill feedback.
3. The portal (web app) is the build deliverable — it replaces the standalone CLI as the primary artifact.
4. Phase 1 is three agent-run audit skills: `skill-health`, `skill-dedupe`, `skill-security`, each writing into one shared run record. Usage tracking is also Phase 1.
5. The earlier "facts only, no score" reporting rule is retired — the product may state a score.
6. Render cold starts are a two-sentence deployment note, not a launch blocker, for this assignment.

**Phase framing:** Phase 1 = "what is true right now." Phase 2 = "keep it true without me asking" (commit-time security gate, scheduled re-audits and drift alerts, dedupe-as-consolidation workflow, usage economics, org rollups).

**Engine design (three layers):** Layer A is deterministic, server-side, and is the *only* layer the score uses — listing/body token cost, structure, git-commit freshness, trigram + shingle dedupe, secret shapes, declared tool access, remote-fetch instructions, egress hints. Layer B is model judgment in Claude (trigger clarity, ambiguity, intent overlap, injection reachability, missing guardrails), each finding requiring an evidence quote, shown as "Reviewer notes," and explicitly excluded from the score. Layer C is composition.

**Pulse Score (0-100):** context efficiency 35, hygiene 25, uniqueness 20, safety 20; bands at 90+/75-89/60-74/<60; sub-scores always shown alongside the total. Honesty rules: every card is stamped `engine v1`, Layer B (model judgment) never touches the score, and percentile is suppressed until at least 30 published runs exist. A public `/method` page publishes the scoring weights, which is what makes it a benchmark rather than a vanity metric.

**Other design decisions:** push conflicts open a change request rather than force-writing — turning the hardest sync problem into a demo of the existing review workflow. Access control decides what is installable (the marketplace manifest is generated from access-visible plugin folders). The share card is a URL *and* an OG image. The usage dashboard states its own coverage limit on the dashboard — only traffic through Pulse's MCP is counted. No Atlan wordmark appears on the public card (Pulse's own lockup in Atlan's type/colour is used instead; the real Atlan mark appears only in the deck).