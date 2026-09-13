# ICP — final crystallisation (13 Sep 2026)

Supersedes `icp_crystallised_sep8.md` as the reference version — same lock, same population, now written to the depth and narrowness the HR/CEO feedback asked for, and reconciled against everything found through 12 Sep (`problems_solutions_map_sep12.md` confirms nothing since 8 Sep has moved this). This is the ICP that `pulse-standalone` (the audit + shareable card product, built 13 Sep) is built to serve.

## The one sentence

A solo builder or 2–10 person early-stage team who has already published their own working Claude Skills as a **public GitHub repo, for a reason that has nothing to do with Atlan** — building an audience, proving credibility, or teaching — and who now has forks and strangers depending on a repo only they maintain, with no way to show anyone (including themselves) which of those skills actually still work.

## The exact profile — every attribute that narrows it

Read this as a checklist. Someone has to clear all seven to be in-ICP; missing even one moves them into an adjacent, weaker segment.

1. **Has a public GitHub repo of Claude Skills already live**, not "is thinking about publishing one." Pre-publish intent is not observable and not targetable; a live repo with a star/fork count is.
2. **Solo, or a named individual inside a team of ≤10**, not a team-wide initiative. There is no IT department, no procurement step, no manager who approves tool spend — the person who wrote the skill is the same person who decides whether to keep maintaining it. This is what makes them reachable without a sales cycle.
3. **BYO-agent by construction**: pays for Claude personally, on a founder/startup card, or via a free tier — never behind a centrally-negotiated enterprise seat. There is no admin console standing between them and trying a new CLI tool.
4. **Uses Claude Code or Cowork as a daily driver for their actual paid work** — shipping a product, doing client work, producing content/courses — not as a side experiment. The skills in the repo are their real accumulated "how I work" instructions, refined over months, not written as a demo for the repo.
5. **The repo already has outside dependents**: measurable forks, and ideally comments/issues from strangers, not just stars. Stars alone signal attention; forks signal that someone else's workflow now silently depends on a file this person alone maintains. This is the load-bearing tension the product resolves.
6. **Publishing is instrumental to a separate monetisable goal** — a course, a consulting practice, a newsletter, a personal brand, hiring/credibility for their startup — never publishing for its own sake or out of pure altruism. This is what makes "prove this repo is good" a want, not a nice-to-have.
7. **Reachable at a specific moment**: the repo is either currently gaining traction (dozens to hundreds of forks and climbing) or about to be published/relaunched. That is the moment their attention is actually on the repo's credibility and quality — not evergreen, a window.

## Explicitly who this is NOT (the narrowing-by-exclusion)

- **Not an enterprise AI-enablement lead** (the Toyota/Ford/Deloitte-titled role) — real persona, real budget, wrong moment: their own LinkedIn posts on this topic get 4–5 reactions while beginner explainers get 400×. They're the eventual expansion buyer, not the wedge (`rejected_alternatives.md`).
- **Not a marketing/creative agency selling AI workflows to clients** — the strongest single pain point found ($4,000/mo client offer, r/agency) but the community's own top-voted advice is *against* handing over the raw skill file, and a funded competitor (agentman.ai) already ships the "use-only, redacted sharing" mechanic this exact fear requires. That population is real but belongs to a different product motion (see Adjacent segments, below).
- **Not a private/internal team repo.** If the skills never left the org's own GitHub, there is no stranger depending on them and no public credibility at stake — the wedge (the badge/card) has nothing to attach to.
- **Not legal, HR/recruiting, or CX/support practitioners** — checked directly (not inferred): r/LawFirm returned zero results for any skill-sharing search, r/humanresources is a confirmed absence, and no named governance incident exists for CX/voice teams. All three ruled out on evidence, not by elimination.
- **Not a large (50+ person) engineering org with an internal platform team.** That's Atlan's actual $50K-ACV enterprise registry motion — a different buyer, different sales cycle, explicitly out of scope for this bottom-up bet per the CEO/HR reframe.

## Two concrete, named anchor examples

**1. The indie technical educator** — in the shape of **mattpocock/skills** (≈257k GitHub stars, ≈19k forks, pulled live 8 Sep 2026). A solo developer/educator who publishes the Claude Skills they use in their own TypeScript workflow, promotes them to an audience they already own, and monetises separately through a course, consulting, or sponsorship. No company, no team — just their GitHub handle and their name on the repo.

**2. The solo growth/marketing consultant** — in the shape of **coreyhaines31/marketingskills** (≈48k stars, ≈6.9k forks and still climbing as of 8 Sep 2026; the #2 repo in the space by *installs* at 4.7M, ahead of anthropics/skills and superpowers, per the round-3 broadcast-propensity research). A marketing operator publishing the skills they use for content and campaign work, feeding a newsletter, community, or consulting practice. This is the sub-segment that answers the CEO's "marketing/sales, not just coding" signal without inventing a second ICP — it's the same profile, same product, same loop.

A third, weaker-but-real shape sits alongside these two: the solo/small-team OSS maintainer in an adjacent category (e.g. nimrodfisher/data-analytics-skills — 345 stars, 69 forks, explicitly marketed "portable across any org") — smaller in reach but structurally identical, useful for showing the ICP isn't cherry-picked to two outlier repos.

## Why this is the locked ICP — the justification, evidence-tagged

Evidence tags follow the project's own standard: **[VERIFIED]** read directly from the primary source, **[CORROBORATED]** consistent across 2+ independent secondary sources, **[CONFIRMED ABSENT]** actually checked and found nothing, **[INFERENCE]** a connection we're drawing, flagged so it's never mistaken for voice-of-customer.

**The population is counted, not estimated.** [VERIFIED] Three named repos with live star/fork counts pulled directly (shields.io, 8 Sep 2026): 257k/19k, 211k/—, 48k/6.9k. This is a countable, growing, directly-observable population — not a modelled TAM like every rejected alternative required.

**The problem is the one thing git, stars and forks cannot answer.** [VERIFIED — problems_solutions_map_sep12.md, ranked #1] Once strangers fork a repo, the publisher has no way to show — to themselves or to a fork — which skills still work, are stale, or duplicate each other. This is specifically *not* solved by version control, which is why "why not just git" (a required objection-handling slide for the engineer-only framing) doesn't apply here: git tracks history, not health.

**The motive is provable and self-interested, not altruistic.** [VERIFIED, r/agency + the crystallised profile itself] The repo is content marketing for the publisher's real business. They want a public, quantified proof point exactly when the repo is gaining traction — which is why the product's mechanic (a scored, shareable card) is a want, not a favor being asked of them.

**The distribution loop is observed, not guessed.** [CORROBORATED] shields.io badges already sit in 1.2M READMEs and serve 1B+ requests/month — the closest real-world analogue to "score card in a README," and it is mechanical, not persuasion-dependent: a fork copies the README, badge included, without anyone deciding to share anything. This matters because 23 "package manager for skills" Show HNs scored ~47 combined points *because they asked people to visit a destination* — the rule extracted from that graveyard is that a loop must be a byproduct of work already happening, never a new destination (`round3_research.md`, `rejected_alternatives.md`).

**The IP-exposure objection that kills the agency ICP doesn't apply here.** [VERIFIED, r/agency 62-comment thread + product design] Agencies and consultancies were ruled out specifically because the market's own advice is "never expose the raw skill file" — and a funded competitor (agentman.ai) already ships redacted, use-only sharing for exactly that fear. The publisher ICP doesn't have this problem: the whole point is that the repo is *already public*. The product only ever needs to expose a **score**, never the skill body — `pulse-standalone`'s card mechanic is built ephemeral-by-design (skill bodies are never persisted, only findings/counts/a hash) specifically so this generalizes cleanly.

**It answers the CEO's signal without splitting the ICP.** The CEO's usage data point — 91.3% of Cowork usage is non-coding — is satisfied by anchor example #2 (marketing) without needing a second, separately-designed product for marketing/sales personas. Same profile, same mechanic, different subject matter in the skills themselves.

**BYO-agent removes the sales cycle entirely.** There is no procurement step to design a GTM motion around — reachability is a GitHub notification, a comment, a DM, or a post the person sees, not a meeting with an admin.

**What was checked and explicitly ruled out**, so this isn't an ICP-by-elimination: legal (r/LawFirm, zero results), HR/recruiting (r/humanresources, confirmed absent), CX/support (no named incident found), enterprise AI-enablement leaders (real budget, wrong moment — 4–5 LinkedIn reactions on governance posts vs. 400 on beginner content), and the agency/consultancy segment (strongest single pain point, but the loop is borrowed by analogy and a funded competitor already owns the specific fix that segment needs).

## Sizing, honestly

No combined/deduplicated TAM has been computed (flagged open in `atlan_gtm_problem_catalog_sep8.md`, P45) — what exists is three named, live, growing repos serving as the observable core of the population, plus an unknown but non-zero number of smaller repos shaped the same way (the nimrodfisher example, 345/69, shows the pattern isn't limited to the two headline repos). Anyone using this ICP in a deck should present the three named repos as **the demonstrated core**, not the full addressable market, and say so explicitly rather than implying a modelled TAM this research never produced.

## The one open risk worth naming

This ICP is validated by public artifacts (stars, forks, community threads) and by analogy to a proven loop mechanic (shields.io), but — unlike the agency segment's r/agency thread — there is no direct primary-source quote of a repo publisher saying "I wish I had a way to prove my skills still work." The pain is inferred from the structural fact of the accountability gap (#1 in the problems map) plus the publisher's stated motive (credibility), not from a quoted complaint. Worth surfacing as the honest caveat if asked "how do you know they want this," rather than overstating it as directly voiced demand.

## How to apply

Use this file, not `icp_v2.md` (the agency/"firm that bills for a repeatable deliverable" framing, now Problem 1/monetisation story only) or the shorter `icp_crystallised_sep8.md`, as the reference for any deck, pitch, cohort quote, or outreach copy describing who `pulse-standalone` is built for. Cohort quotes, "who" sections, and channel copy should be written against the two named anchor examples above, not the pre-reframe engineer/team ICP that `problems_solutions_map_sep12.md` flagged as still needing a pass.
