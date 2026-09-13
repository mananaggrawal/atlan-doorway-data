# Atlan Doorway — this knowledge base

This is the data behind a live [Atlan Doorway](https://atlan-doorway.onrender.com/) instance: a git-backed home for the team's documents, AI-agent skills, and tools, all version-controlled and access-controlled in this same repository.

## In one paragraph

Everything an AI agent (or a person) can read or do here is a file in this repo. Documents live under `KnowledgeBase/`, agent instructions live under `Skills/` (grouped into `Plugins/`), and who can see or change what is declared in `access.md` files alongside the content they govern. Every change is a git commit, so history, blame and revert work exactly as they do for code.

## What's here right now

| Path | What it is |
| --- | --- |
| `KnowledgeBase/` | Documents. Currently just the default "How to get started" page — no team content has been added yet. |
| `Skills/` | Agent skills. Empty so far. |
| `Plugins/` | Groupings of skills/tools with their own owners and sharing. Empty so far. |
| `AGENTS.md` | Platform-maintained reference for how agents should use this workspace. Leave as-is. |
| `access.md` | Root access-control rules — who can read/write/download by default. |
| `mcp-description.md` | The org-specific text every connected agent is told at the start of a session. Still the default placeholder — not filled in yet. |
| `roles.yaml` | Role definitions used by `access.md` grants. |

## Try it

The live instance is at **https://atlan-doorway.onrender.com/**. Sign in, open **Knowledge** to browse/edit these files with a UI instead of raw git, or **Skills & Tools** to manage plugins.

## Next steps

This KB is still the out-of-the-box starter — nothing team-specific has been written into it yet. To make it useful:

1. Fill in `mcp-description.md` so connected agents know what this KB actually holds (it's currently the commented-out template and is not sent to agents until that comment wrapper is removed).
2. Add real documents under `KnowledgeBase/`.
3. Create a plugin under **Skills & Tools** and add the team's first skill or tool.

See `KnowledgeBase/How to get started.md` for the full walkthrough.
