# Atlan Pulse v2 — what shipped

Backend and frontend are complete and green: 2,167 backend tests, 1,602 frontend tests, typecheck clean across all 7 packages.

**Backend:** an `audits` module (a pure scoring engine with 8 checks plus the Pulse Score; a service layer; MCP tools `start_audit` / `submit_audit_findings` / `finish_audit` / `skill_usage`; a public-card privacy filter; SVG/HTML card rendering plus the `/method` page). A `skill-sync` module (`push_skills` / `pull_skill` / `diff_skill` / `list_synced_skills`, with conflicts opening a change request). A `marketplace` module (HMAC capability-URL manifest plus zipped plugin archives). New database tables for audit runs and synced skills.

**Frontend:** the Skill Health surface was rebuilt with tabs for Audits / Usage / Connect Claude, an overview page, an audit-run panel, a report page, a publish panel, a usage page, a Connect-Claude page, score and finding-list components, plus a Governance section (Trail and Access) on the skill page.

**Skills:** four `SKILL.md` files ship inside the product itself, with access rules granting read to everyone and write/owner to Admin — every description carries trigger phrasing so the product passes its own audit check.

**Decisions baked into the code worth remembering:** an `ENGINE_VERSION` constant is stored on every run row and must be bumped on any change to a check, weight or threshold. A model-judgment finding can never reach the score — enforced by an assertion, not just convention. Percentile is suppressed below 30 published runs. The secrets check never echoes a matched value. Slugs use a fixed 32-character alphabet rather than base64url, because stripping `-`/`_` after base64url encoding produced variable-length, more guessable ids (caught by a test). Unpublishing clears a share slug; republishing mints a new one. Marketplace URLs are capability URLs (an HMAC of the user id sits in the path, since plugin clients can't send an auth header) — access control *is* the distribution list.

**Real-data validation:** Manan's own 19 real account skills scored 83/100 (119% over the token budget, 19 skills with no owner, one duplicate pair). Anthropic's 33 example skills scored 73/100 (157% over budget, 2 with no description, one duplicate pair). Pulse's own four skills scored 100/100.

**Known gaps:** the OG share image is currently SVG, which X/LinkedIn won't unfurl — needs a PNG rendering step. Plugin marketplaces are git-shaped, not URL-shaped, so a bare HTTPS marketplace URL only works on some clients; the `pull_skill` tool is the guaranteed path. No live click-through validation has been done yet after the last deploy.