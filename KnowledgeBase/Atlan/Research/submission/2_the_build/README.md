# Deliverable 2 — The thing built

The shipped artifact isn't inside this folder — it lives at the repo root as its own project, because it's a real standalone repo, public on GitHub:

- **`../../pulse/`** — Atlan Pulse, the skill-health CLI. This is the submission. Zero-dependency Node ESM tool: `npx github:mananaggrawal/atlan-pulse` scans a machine's Claude Code/Codex skills and writes a shareable report (duplicates, stale skills, missing owners, risky permissions). Public repo: https://github.com/mananaggrawal/atlan-pulse. Landing page live at https://atlan-pulse.onrender.com.
- **`../../4_build/atlas/`** — Atlas, a fork of Bevel's Hexis used as an internal reference build / competitor comparison (same product category as Atlan Agent Registry). Not the submission itself — see `../../4_build/README.md` and project memory `atlas_fork.md` for what it is and why it exists.

See the root `README.md` deliverables table for the full picture.
