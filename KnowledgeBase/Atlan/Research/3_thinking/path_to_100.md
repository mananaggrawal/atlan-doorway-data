# Path to 100 — the funnel, the supply, and the arithmetic
**Status: FIRST MODEL (2026-09-05).** Not previously written down — `the_campaign.md` specifies the mechanism (audience, offer, CTA) but not the numbers. This file supplies them, tagged `[assumption]` wherever no data exists yet, so the model is falsifiable rather than a vibe. Per `../1_brief/understanding_v1.md` §7: "the goal is a validated, evidenced path to 100 with the first experiments actually run — not 100 signups during the exercise." This is that path, not a claim that Wave 1 hits 100 on its own.

## The funnel (from the candidate activation definition in `the_bet.md` / `understanding_v1.md` §3 — pending decision)

`install → solo scan (individual value) → invite one teammate → second person scans into the same workspace → 3rd person + one skill gets a named owner, a version, and reuse = activated team`

Two hinges matter. The first — solo scan happening at all — is low-friction by design (one command, no signup). The second — a second person actually joining the workspace — is untested and is where this whole model is most sensitive. `the_campaign.md`'s measurement plan already names this as the primary metric for exactly this reason.

## Supply: who Wave 1 actually reaches

From `../2_research/prospects/prospect_candidates.md` (counted directly, not the rounded "~70"):

| Pool | Count | Source |
|---|---|---|
| Tier 1 — already built a fix | 6 | zwaantjuh, Necessary_Abroad6632, Justin Trugman, Abu_BakarSiddik, Abhisheik Deo, Dijerati |
| Tier 2 — documented pain, named and reachable | 52 | GitHub issue authors/commenters, HN, X, LinkedIn, blogs, Reddit — excluding Tier 3 |
| **Direct-outreach pool** | **58** | Tier 1 + Tier 2 |
| Tier 3 — competitors, excluded from outreach | 10 | Not counted below; leverage/press only |
| Reddit launch surface | r/claudeskills, ~66K members | Not individually named — a post, not a list |

## Wave 1 arithmetic

Every rate below is `[assumption]` — none is measured yet. Each is anchored to something in the research rather than picked blind, and each is exactly the kind of number the campaign's own measurement plan exists to correct.

**Stage 1 — personalized outreach → solo scan**
- Tier 1 (n=6): highest relevance, message names their specific tool's actual gap. `[assumption]` 50% reply, 70% of repliers run it → **≈2 solo scans**.
- Tier 2 (n=52): stated pain, not built. `[assumption]` 22% reply (well above generic cold-outreach baselines because the message references their own GitHub issue or post by name), 50% of repliers run it → **≈6 solo scans**.
- **Direct outreach subtotal: ≈8 solo scans.**

**Stage 1b — r/claudeskills post ("I built X to solve Y")**
The highest-variance number in the model, deliberately not disguised as precise:
- `[assumption]` a well-crafted post in a sub with a documented history of 750+upvote posts on this exact topic reaches 15,000–40,000 impressions.
- `[assumption]` 3–6% click through; of clickers, 35–45% run a one-line CLI with no signup.
- **Range: ≈160–1,080 solo scans. Planning midpoint: ≈200.**

**Wave 1 solo scans, combined: ≈208, planning range ≈170–1,090.**

**Stage 2 — solo → second person joins the workspace**
No data exists; this is the number the whole campaign is designed to learn. Anchored two ways, both pulling toward caution:
- PLG tools with a genuine in-product "compare with a teammate" moment typically see invite-acceptance in the 10–25% range when it's curiosity-driven rather than gated.
- Reddit's own strongest counter-finding — skill-sharing read as "training your replacement" (99 upvotes, r/ClaudeAI) — means a real slice of solo users will deliberately *not* invite anyone. That pulls the estimate to the low end, not the middle.
- `[assumption]` **12%** of solo scanners bring in a second person within the test window.
- → **≈208 × 12% ≈ 25 two-person workspaces.**

**Stage 3 — two-person workspace → full activation (3rd person, owned+versioned+reused skill)**
- `[assumption]` **50%** of two-person workspaces cross to a third person and actually claim ownership/pin a version on a reused skill within the window — mechanical once two people are already comparing skills, if the report/tool makes "claim ownership" and "pin version" one-click actions.
- → **≈25 × 50% ≈ 12–13 activated teams from Wave 1.**

## Wave 1 honestly does not reach 100 — and it isn't supposed to

Range, depending mostly on how Stage 1b performs: **roughly 6 to 40 activated teams from one outreach wave plus one Reddit post.** That is the number to defend in the readout, not 100 — the brief explicitly does not ask for 100 signups inside the exercise. What it asks for is a credible, testable *path*, which is the loop below, not a bigger single wave.

## What compounds Wave 1 into a path to 100

None of these are counted in the arithmetic above, on purpose — they're why this is a repeating loop, not one campaign that has to hit 100 alone:

1. **Tier 2 supply is structurally renewable.** Five independent duplicate GitHub issues appeared over six months in the sweep alone. Each new one is a same-day outreach target, not a pool that depletes.
2. **The aggregate report is its own second wave.** Once enough runs accumulate, "The State of Agent Skills 2026" is a publishable benchmark — H6's entire bet — with its own HN/press/LinkedIn pickup, seeded by Wave 1's own output data.
3. **Second-wave channels open once the tool is proven.** r/ClaudeCode (~745K) and r/ClaudeAI (~1.6M) were argued against for *launch* in the analysis — showcase-dominated, wrong energy for a cold governance pitch — but become viable once the post can say "N teams already run this" instead of pitching from zero.
4. **Activated-team members are a distribution channel themselves.** Each one is an engineer who moves between companies and side projects, and re-triggers the same solo-scan mechanic wherever they land next — uncounted here.
5. **The enterprise AI-enablement persona reopens.** Argued against as the *wedge* (real title, wrong moment — see `rejected_alternatives.md`), not argued against as real. Real usage data turns an abstract governance pitch into "here's what teams like yours are already doing."
6. **An SEO-facing asset could open a genuinely uncontested lane.** Added 2026-09-05, from `2_research/numbers/search_demand_semrush.md`: "claude code skills," "claude skills marketplace," and a how-to long tail ("how to add skills to claude code," etc.) carry real, growing, currently-unclaimed Google search volume — unlike the literal category term "agent registry" (~140/mo, dead). A page like "The State of Claude Code Skills" (item 2 above) targeted at that vocabulary rather than "registry" language would meet that traffic directly, feeding the same activation funnel without competing with Wave 1's GitHub/Reddit channel. Uncounted here, same as items 1-5 — a candidate, not yet a decision.

## The single number this entire plan is most sensitive to

Stage 2 (solo → second person) at 12% instead of, say, 5% is the difference between a campaign worth scaling and one that needs its invitation step rebuilt before anything else. Nothing in the desk research pins this number — it can only come from running Wave 1 and watching what `the_campaign.md`'s measurement plan actually reports back. Flagged here as a strong candidate for "the decision AI could not make" in the AI work log: this file supplies a defensible starting assumption, not a validated one.

## What would change this model
- Atlan naming a different activation bar (D1's reversal condition) rescales every stage below it.
- Real Wave 1 data replaces every `[assumption]` rate above with a measured one — that's the point of running it.
- If Stage 1b (Reddit) badly underperforms the low end of its range, the model leans much harder on Tier 2 renewal and the second-wave channels in section "What compounds," which are slower to arrive than a single post.
