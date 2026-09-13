# Skill Health — feature history

Skill Health was built as a feature inside the Atlas/Pulse codebase, instrumented at the single point in the backend that already catches all tool traffic (MCP, in-process, and API-token) without double-counting.

**Two health tiers:** Tier 0 (orphaned/stale/unreviewed/churning/bus-factor) needs no new data collection and works from the very first commit. Tier 1 (never-invoked/failing/drift-risk) needs a minimum volume of real invocations and a minimum time window of real usage data, both configurable via environment variables so the threshold can be relaxed for a demo.

**Rename history:** the product was renamed from "Atlas" to "Pulse," positioned around exactly two named features — Skill Registry and Skill Health. The earlier "Knowledge" framing was dropped from marketing and navigation, though the underlying file/workspace surface stays mounted since both the skill-registry UI and Skills & Tools depend on that route existing. Internal code identifiers were deliberately left as "Atlas" — an intentionally narrower, user-facing-only rename, not a full internal rename.

**Notable bugs caught and fixed post-rename:** removing "Knowledge" from the app's navigation switcher accidentally broke the app's own routing, because the same config array served both the visible menu and the underlying route list — caught by manually checking the live deployed app, not by the test suite, since no existing test exercised real end-to-end routing. A second, related bug meant the root URL and catch-all route still silently landed users on the old "Knowledge" surface even after it was removed from the menu — both redirect targets had to be updated explicitly. A separate, unrelated deploy failure was caused by a lockfile-vs-package.json mismatch masked by build caching in every prior successful deploy.

**Branding:** Atlan's Persian Blue accent color was applied to the app's UI tokens; Atlan's actual logo/wordmark is not used anywhere in the product, to avoid misrepresenting affiliation.

**How to apply:** Skill Health is the direct answer to the differentiation problem in the research findings — storage and governance are commoditised, the evidence layer is not.