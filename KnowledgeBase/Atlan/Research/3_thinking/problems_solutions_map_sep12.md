# Problems → Solutions map — Agent Registry (12 Sep 2026)

Synthesis of everything gathered so far (round 1–3 research, the GTM problem catalog, the crystallised ICP, the decision deck, the channel plan, path-to-100), written as the bridge into the final deck and deliverables. Locked ICP throughout: **the public skill-repo publisher** — a solo builder or very small team who published Claude Skills to a public GitHub repo for reasons unrelated to Atlan (audience, credibility, teaching), and who now has forks and strangers depending on it (`icp_crystallised_sep8.md`).

## 1. Top problems, ranked

Ranked by how directly each one lands on the locked ICP and how strong the evidence is. Tag key: [VERIFIED] read directly · [CORROBORATED] 2+ independent sources · [INFERENCE] our own connection, flagged as such.

1. **No accountability signal once strangers depend on your repo.** [VERIFIED] The publisher has no way to show — to themselves or to a fork — which skills in the repo actually work, are stale, or duplicate each other. This is the load-bearing problem: it's the one thing git, stars and forks don't tell you. Sits underneath all three quoted cohorts in the deck ("we clone and copy skill files manually," "every skill rides along in context," "a skill changes silently").
2. **Credibility is the actual motive, and it's currently unprovable.** [VERIFIED, r/agency + icp_crystallised] The repo is content marketing for the publisher's real business (course, consulting, newsletter, personal brand). They want a public, quantified proof point at the moment the repo is gaining traction — not a private diagnosis.
3. **IP-paranoia / "share the result, never the source."** [VERIFIED, r/agency 62-comment thread, r/consulting] Clients and communities alike want the output, not the raw skill; the community's own top-voted advice is *don't* expose the file. Any mechanic that asks the publisher to hand over the actual skill will be refused.
4. **Discovery/duplication at scale (Atlan's own founding problem).** [VERIFIED, Atlan's internal 300-skill/40-agent build] People can't find what already exists, so they rebuild it. Real, but it bites at 50–300 skills — i.e., team/enterprise scale, not the solo publisher we're building for now.
5. **No published benchmark for skill quality anywhere.** [CONFIRMED ABSENT — checked] Zero competitors publish a "how good is this skill" number. This is what makes #2 winnable rather than table stakes.
6. **The registry-as-destination trap.** [CORROBORATED, 23 Show HNs, ~47 combined points] Every prior "package manager for skills" failed because it asked people to visit somewhere new; git already does versioning/hand-off for free. Not a persona pain so much as a structural constraint on any solution we pick.
7. **Security exposure in shared skills (prompt injection, hardcoded credentials).** [Atlan roadmap, not yet observed as a live incident] Real risk as forking scales, but currently unverified as a felt pain for this ICP — flag, don't lead with it.
8. **Enterprise governance pain (drift, ownership, spend/ROI reporting).** [VERIFIED, Atlan's own product] Real and is the eventual $50K-ACV motion, but explicitly out of scope for this bottom-up bet per the CEO/HR reframe.

## 2. Solutions map

| Problem | Solution mechanic | Status | Feeds |
|---|---|---|---|
| #1 No accountability signal | **Atlan Pulse / skillscan** — local scanner reading both skill files *and* session transcripts, headline stat like "12 skills never invoked; 3 account for 78% of invocations" | Built (v0), unique vs. competitors who only scan files | Deliverable 2 (the build) |
| #2 Credibility unprovable | **`--card` share mechanic**: a rendered, brand-carrying score card (percentile + confession stat + depth credential) the publisher posts themselves | Built | The loop / deck's "why anyone shares" slide |
| #3 Never share the source | Card mechanic is built so it **only ever exposes the score, never the skill file** — "share the score, you never share the skill" | Built, and the phrase already generalises from the engineer ICP to the agency ICP without changing the mechanic | Core differentiation line for the deck |
| #4 Discovery/duplication at scale | Full Agent Registry surfaces (workspaces, Agent 360, dependency graph, search) — this is Atlan's actual enterprise product, positioned as the **expansion path**, not the wedge | Exists as Atlan's product; not what we're building for this submission | Expansion-map slide, not the wedge |
| #5 No published benchmark | The scan report + card *is* the first public benchmark; an aggregated **"State of Claude Code Skills"** report turns individual scans into a category-defining asset once N accumulates | Report built; aggregate version not yet built | Second-wave acquisition asset (path_to_100) |
| #6 Registry-as-destination trap | Ship as a **CLI byproduct of work already happening** (`npx skillscan`), distribute through GitHub-native surfaces (issue comments, repo topics, awesome-list PRs) rather than a site people must visit | Distribution plan set (`atlan_channel_plan.md`), execution partly done | Deliverable 2 + channel plan |
| #7 Security exposure | Not built for this submission; name as roadmap only if asked | Roadmap | AI work log / "what we said no to" |
| #8 Enterprise governance | Full Registry, top-down motion Atlan already runs at ~$50K ACV | Existing product | Explicitly out of scope, named only as the expansion map |

## 3. The one contradiction that has to be closed before the final deck

The deck (`atlan_decision_deck.md`) currently has an internal split: the two newest slides ("ICP identification," "The decision") correctly point at the **public skill-repo publisher**, but everything built 07 Sep — the three cohort quotes, "Who" (58 named prospects), "Where" (r/claudeskills, Show HN, GitHub-issue comment, awesome-lists, SEO), and the 1,708-scan math-to-100 — still describes the **pre-reframe engineer/team ICP**. Before final assembly, each of those needs a pass against the locked ICP:

- **Cohorts** — swap in publisher-shaped quotes (the r/agency IP-paranoia quotes and the OSS star/fork numbers already sourced in the ICP file) in place of the team/power-user/reviewer trio.
- **Who** — recut from "58 named prospects who already built a fix" to the two concrete examples already locked (the mattpocock/skills-shaped educator, the marketingshare-shaped consultant) plus however many similar repos get identified.
- **Where** — GitHub-native channels survive unchanged (they're ICP-agnostic); Reddit/HN framing needs to shift from "I built X to fix Y for engineers" to something that speaks to publishers protecting/proving their repo.
- **Math to 100** — rebuild the funnel around repo-publisher supply (star/fork counts as the addressable population, per `icp_crystallised_sep8.md`'s three named repos) instead of the solo-engineer-scan model. This is the one Manan flagged as still open.

## 4. Recommended next steps

1. Recompute the population/reach numbers for the locked ICP (how many repos look like the two examples — a directory pull, not a guess) so "the math to 100" can be rebuilt honestly.
2. Rewrite the four flagged deck sections against the publisher ICP, keeping the density rule (~30 words/slide) and the existing storyline arc.
3. Re-screenshot the current report/card mechanic (already correct — no rebuild needed there) once the card is validated against a real public repo.
4. Fold this file's problem list directly into the evidence appendix so every deck claim traces back to a tagged source.
