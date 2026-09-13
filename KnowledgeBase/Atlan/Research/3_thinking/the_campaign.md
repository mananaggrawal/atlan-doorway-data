# The campaign
**Status: DRAFT, built around a candidate channel — not yet decided** (`the_bet.md`, `decision_log.md` D10 — AI analysis pending Manan's confirmation). Ready to execute once ICP/channel are confirmed jointly. The scanner + report itself is deliverable 2 and lives in `4_build/` — this file is the campaign around it, not the software.

## Audience
~70 named individuals who publicly expressed this exact pain, already sourced in `../2_research/prospects/prospect_candidates.md`: GitHub issue authors and commenters (highest intent, named, reachable), a handful of Reddit posters (r/ClaudeCode, r/claudeskills), and anyone visibly active in the sprawl/trust conversation on X. Not a segment description — a list.

## Offer
Run one command against your local Claude Code / Codex skills folder(s). Get back, in under a minute, a personal "Skill Health Report": total skill count, likely duplicates, skills untouched in N days, skills with no listed owner, skills declaring risky permissions, and how much of your context budget they're eating. No signup for the solo report; nothing leaves the laptop at this stage.

## Channel-native acquisition asset
The report itself, plus a short "why this matters" writeup citing the same evidence already gathered in `../2_research` and `evidence_synthesis_v1.md` — the 1,536-character description budget, the NVIDIA vulnerability numbers, the GitHub issue closed `not_planned` — so a skeptical reader can verify the claims rather than take a vendor's word for it.

## Destination / activation experience
Solo run → report, framed around the individual payoff first ("your own agent gets better" — see `the_bet.md` on why altruism is the wrong opener) → the report itself ends with an invitation to compare against a teammate's → a second scan into a shared workspace is the point at which team-level claims (actual duplication across people, a skill with a second user, a named owner) become both possible to compute and honest to state. This is deliberately the same point where `the_bet.md`'s activation definition — 3+ people, named owner, version, second-user — becomes reachable, not before. See `decision_log.md` O3 for why the solo report must not overclaim team-level findings.

## Call to action
For the ~70 named people: a direct, personalized message referencing their own GitHub issue, Reddit post, or X thread, offering the tool as a direct answer to the thing they already asked for in public. For the wider audience: post the scanner to r/claudeskills as "I built X to solve Y" — per `rejected_alternatives.md`, that sub is viable for exactly this framing, not for a governance argument. GitHub issue threads are treated as one-to-one outreach, never a broadcast.

## Launch mechanics
**Manan's working direction, 2026-09-07 (decision_log.md D13) — not yet signed off.** This is what he's directing execution toward, not a locked decision; treat it as the operating plan until he revisits it. Sequenced, not simultaneous:

1. **Direct outbound** to the ~58 named Tier 1/2 prospects — ships Tue 8 Sep, non-negotiable. Highest intent, and it lets the report get fixed before a wider audience sees it.
2. **r/claudeskills post** ("I built X to solve Y," not a governance pitch) — after outbound, folding in whatever the first replies surface.
3. **Second-wave subreddits** (r/ClaudeCode, r/ClaudeAI) — explicitly gated on initial feedback and users from steps 1-2, not run in parallel with them. Larger, more general audiences; only worth the post once the tool and framing are proven.
4. **Show HN** — Manan's direction is that this is worth doing, for two things: the scanner itself, and the broader Atlas story (a self-hostable registry that includes skill sharing/governance, not just the CLI). Sequenced after Reddit validates the framing, same reasoning as step 3 — HN's "package manager for skills" category already has 12+ entries since January, most in the 0-9 point range, so this reads better as a proven tool than a cold pitch. Two candidate framings, likely two posts spaced apart: "Show HN: skillscan — a one-command health report for your Claude Code skills" (the free tool) and, once Atlas is presentable, "Show HN: Atlas — a self-hosted registry for agent skills, forked from Hexis."
5. **SEO/AEO** — Manan's direction is that this is the sustained-effort channel once the above waves are running. Target the uncontested demand already sized in `../atlan_keyword_search_demand.md` (`claude code skills` 8,100/mo, `claude skills marketplace` 2,900/mo and climbing, the how-to long tail). The aggregate "State of Agent Skills" report doubles as this asset once enough scans have run — it's both a content piece and the H6 benchmark.

**Manan's direction, not yet signed off: no paid spend anywhere in this plan.**

**Manan's direction, not yet signed off: leave alone for this exercise** — the AWS Agent Registry partner motion and Atlan's existing enterprise customer base as a channel — both already argued against in `rejected_alternatives.md` (partner motions run on quarters not weeks and are account-scoped to the wrong population; the installed base would prove conversion, not distribution, which is a different question than the brief asks).

Let X and LinkedIn pick up organically rather than posting there first — the channel research reads both as validation/listening surfaces, not primary acquisition (`evidence_synthesis_v1.md`, channel read).

## Additional channels — considered 2026-09-07, GitHub-native and directory listings
Raised by Manan: are there other free channels, e.g. GitHub-native moves, Product Hunt. Analysis below; none of these replace the sequence above, they run alongside it at near-zero cost.

**Recommended — GitHub-native, compounds forever, matches the ICP exactly:**
- A public comment on `anthropics/claude-code#28327` (the "team skill sharing" issue closed `not_planned`, with duplicates folded into it) once skillscan exists — not a DM, a comment on the thread itself. This is evergreen, high-intent search traffic: everyone who later hits the same wall and searches finds it, not just the people already reached by name.
- Repo topics/tags (`claude-code`, `mcp`, `agent-skills`, `ai-agents`) on the skillscan and Atlas repos, so both surface in GitHub's own topic search and "explore" pages. Costs minutes.
- PRs adding skillscan (and later Atlas) to the live "awesome-claude-code" curated lists — several exist and are actively maintained: `subinium/awesome-claude-code`, `rohitg00/awesome-claude-code-toolkit` (which explicitly catalogues an "ecosystem entries" section), `jqueryscript/awesome-claude-code`, `alvinunreal/awesome-claude`. These are Claude-Code-specific, meaning whoever browses them is already the ICP — a tighter match than the general MCP directories below. Zero cost, permanent, worth doing for both tools.

**Worth doing, low effort, but treat as hygiene not a growth channel:**
- MCP server directories — `glama.ai/mcp/servers`, the official `modelcontextprotocol.io/registry`, `mcp.so`, and the generic `awesome-mcp-servers` lists (punkpeye's is the largest). Atlas already ships a `glama.json` (inherited from the Hexis fork, still pointing at the old maintainer — needs updating before submission), so listing there is a five-minute fix, not new work. But glama alone now indexes 83,000+ servers — being listed is table stakes, not a discovery lever on its own, so don't spend real time here beyond the housekeeping.

**Analyzed and not recommended: Product Hunt.** The audience skews indie-hacker/general-SaaS discovery rather than "engineer already running 50-300 Claude Code skills" — the same mismatch that already ruled out general subreddits and LinkedIn as launch surfaces in favor of purpose-built communities. A PH listing costs little and could be added opportunistically once the tool exists (a free backlink), but it shouldn't be resourced as a real channel or allowed to substitute for the r/claudeskills post or the GitHub-native moves above.

## Measurement plan
Primary metric, tied directly to H8's kill criterion: of all solo reports generated, what fraction convert to a second person scanning into the same workspace within a set window. Installs or reports alone are a vanity number — the product only proves anything once a second person shows up, which is also literally the activation definition.

See `path_to_100.md` for the full numeric model this metric feeds: Wave 1 (58 named prospects + one r/claudeskills post) plausibly yields ~6-40 activated teams on a 12% `[assumption]` solo-to-second-person rate — the first real number from this campaign replaces that assumption and rescales the whole path to 100.

## The signal that would make us continue, change, or stop
**Continue:** a meaningful fraction of solo scanners bring in a second person within roughly a week. **Change:** installs and reports happen but nobody shares (H8's own kill criterion) — that's a CTA/framing problem, fix the invitation step, not the tool. **Stop:** the report tells people nothing they didn't already suspect (H8's other kill criterion) — that would mean the "missing benchmark" bet (H6) was wrong about being *valuable*, not just under-published, which is a real possibility worth taking seriously rather than explaining away.

## Open before this can actually run
- The scanner needs to exist — tracked in `4_build/`, not here.
- Exact wording of the personalized outreach to the ~70 named people — draft once the tool produces a real report to point to, not before.
