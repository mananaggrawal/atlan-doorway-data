# Atlan Doorway — this deployment

Atlan Doorway is a separate, public open-source project from the Atlan Pulse GTM work — a clean, rebranded fork of an existing open-source project (a self-hosted, git-backed knowledge base with shared skills, tools and MCP access control), built the same week as Pulse. It's unrelated to the Atlan GTM bet itself; it's Manan's own knowledge-base/skills/tools platform, and this very deployment (`atlan-doorway.onrender.com`) is running it.

**What it is:** a self-hosted control plane where an organisation's knowledge, skills and tools live together in one git repository, with per-file access control, change-request review, a secrets vault, and MCP-native connection (OAuth 2.1) so any MCP-capable agent — Claude, ChatGPT, Claude Code, Cursor — can read and write into it.

**Build decisions:**
- Started from a clean upstream base rather than the Atlas/Pulse tree — a separate codebase, not a shared one.
- Attribution and inherited marketing copy were stripped from the shipped public repo, the same call made for Pulse's own lineage (see `Product-Pulse/lineage-and-licensing.md`).
- Hosting supports single-tenant self-hosting (Docker Compose, or a bundled reverse-proxy profile with built-in Google OIDC SSO) plus a one-click Render deploy. A larger multi-tenant "hosted control plane" mode was scoped as a possible future build but was not started for this pass.
- A real finding during the rename: several onboarding-walkthrough screenshots in the original upstream repo were actual captures of the original maintainer's own internal admin workspace, showing real internal hostnames and organisation names. These were removed entirely rather than shipped, and the onboarding walkthrough now uses descriptive text callouts instead of screenshots.

**Verified before shipping:** a full install, typecheck, and test run passed cleanly (4,637 of 4,638 tests green; the one failure is a known flaky test under constrained parallelism, confirmed pre-existing).

**Deliverables beyond the base rename:** a Render deployment blueprint; a full "Getting Started" walkthrough (self-host path, first sign-in, Google Workspace SSO setup, first skill, connecting an agent); a hardened local-run script; a rewritten README (quick-start, SSO, feature summary, FAQ) with the original project's customer references and demo links removed.

**This knowledge base you're reading right now** is the first real content published into a live Doorway deployment — the Atlan GTM work above, structured for any agent connected to this Doorway instance to search and cite.