# The submission plan — exact strategy, exact outputs, exact sequence
**Written 2026-09-05. Status: RECOMMENDATION for Manan's confirmation** (per the decision_log process correction — AI analyses, Manan decides).
This file supersedes nothing; it is the assembly plan that turns `the_bet.md`, `the_campaign.md` and `path_to_100.md` into four shippable deliverables by Thu 10 Sep.

---

## 1. The strategy, stated in five sentences

1. **ICP:** the person on an AI-native engineering team who has already built a homegrown point-fix for skill sync, versioning, approval or dedup — revealed preference, not stated preference (D9 + D11).
2. **Channel:** a free, one-command, open-source tool that reads their own machine and hands back evidence about their own skills — the product's own activation mechanic, shipped as the acquisition asset (D10).
3. **Positioning:** not storage — **evidence**. Usage, traces, dependencies, drift. Storage is what a dozen competitors and AWS already claim; the evidence layer is what AWS deferred to roadmap and what Atlan already demos (D4).
4. **Activation:** 3+ people in one workspace with at least one skill that has a named owner, a version, and a second user (D1).
5. **Path to 100:** Wave 1 (58 named prospects + one r/claudeskills post) is modelled at ~6–40 activated teams; 100 comes from that loop repeating on renewable supply, not from one bigger wave (D12).

## 2. The one change I am recommending to the plan as it stands

**The scanner as currently specified is a diagnostic, and diagnostics do not create distribution loops.**

`path_to_100.md` correctly identifies Stage 2 — solo scan → second person — as the number the whole model is most sensitive to, and assumes 12%. But look at why it is low: a report that tells you "you have 47 skills and 6 look like duplicates" makes you feel something. It gives you nothing to *send*. The invite is an act of altruism, and H4/B4 (the 99-upvote "never train your replacement" comment) says a real slice of this audience will decline altruism on principle. A 12% assumption on an invitation with no payload is, if anything, generous.

**Fix: make the share the payoff, not the diagnosis.** The tool ends not with an invite link but with a packaged, installable bundle of the user's own best skills plus a one-line install command for a teammate. The teammate gets something useful on their first interaction — working skills, installed in one command — and *that install event is the second-person signal.* The mechanic converts Stage 2 from "will they accept an invite" (weak, altruistic, ~10-25% at best) to "will they send a colleague something the colleague actually wants" (strong, self-interested, and natively measurable).

Three consequences, all good:
- It answers H8's kill criterion — "installs but nobody shares" — structurally rather than by hoping.
- It is the smallest honest instantiation of Registry itself: identity, version, owner, usage, distributed into a harness. The demo *is* the product thesis in miniature.
- It gives the readout a defensible answer to "why not just git": git moves files; this moves files *with the evidence attached*, and the evidence is what tells you which five of your forty skills are worth sending.

## 3. The second change: read sessions, not just skill files

Atlan's own activation mechanic scans **skills and sessions**. Almost every competitor scans files. Session data is where the evidence layer actually lives, and it is the one thing a solo scan can honestly produce without any team present — which also resolves open decision **O3**.

`[assumption — verify on day 1]` Claude Code writes session transcripts to `~/.claude/projects/**/*.jsonl`; Codex has an equivalent. If invocations are recoverable from those, the report's headline stops being a file count and becomes:

> *47 skills. 12 have never been invoked. 3 account for 78% of your invocations. Your never-invoked skills are consuming 38% of your skill-listing context budget.*

That is a number the user did not know, cannot get from git, cannot get from skills.sh, and which no competitor currently ships — and it directly closes H8's other kill criterion ("the report tells people nothing they didn't already suspect"). If the transcripts turn out not to carry it, fall back to file mtime + a manual `--usage` flag, and say so in the readout as a known limitation. Do not fake it.

**O3 resolved:** the v1 solo report claims *personal* facts only — my skills, my invocations, my context cost, my near-duplicates, my declared permissions. It states its own boundary in the report body: cross-person duplication and true team ownership are unknowable from one laptop and appear only once a second person joins. The report's honesty about that boundary is itself part of the pitch.

## 4. The four deliverables — exactly what to produce

### D1 · Decision document
**Format:** one HTML page, published with a URL (consistent with `evidence_brief.html`, already built). Not a PDF deck — the readout is a scroll with anchors, and a link survives the session. ~1,800 words + the demo = the 15-minute core.

**Sections, in this order:**
1. **The bet, in one screen** — ICP · channel · activation definition · the number (6–40 from Wave 1, not 100) — readable in 60 seconds.
2. **The tension, named first** — Atlan sells top-down to CDOs at ~$50K ACV; the brief asks for dramatic distribution first. Registry is the free wedge that earns the right to sell the context layer (D3). Leading with this is what signals the candidate read the company, not just the brief.
3. **Who, and the trigger** — not a segment, a revealed-preference behaviour: they already built the point-fix. Named examples from Tier 1.
4. **Why not storage** — H5 killed, the competitive field, the move to the evidence layer (D4).
5. **Why not just git** — required slide (D5). Answer: git moves files, not evidence; and name the two frictions and the threshold, since the best public objection is conditional and therefore answerable.
6. **The channel, and why it beats the two strongest alternatives** — public directory (H5/skills.sh) and AWS partner motion (slow, account-scoped, wrong population). One paragraph each, steelmanned then answered.
7. **The campaign, ready to run** — audience (58 named), offer, asset, activation path, CTA, launch sequence, measurement.
8. **The loop** — scan → report → pack → teammate installs → shared workspace → owner + version + reuse.
9. **The arithmetic** — the funnel table from `path_to_100.md`, every rate tagged `[assumption]`, and the honest statement that Wave 1 does not reach 100 and is not meant to.
10. **What ran, and what came back** — real Wave 1 results as of the freeze. This is the section that separates this submission from a strategy deck.
11. **Next three experiments**, with kill criteria.
12. **Six questions for Atlan** (already drafted) and the assumptions taken instead of asking.

### D2 · The build
**Ship:** a public GitHub repo, one-line run, no signup, nothing leaves the laptop unless the user opts in.

- `npx skillscan` → scans `~/.claude/skills`, project `.claude/skills`, Codex equivalents; parses frontmatter; computes near-duplicates, context-budget cost, declared permissions, staleness, and invocation counts from session transcripts.
- Output: terminal summary + a standalone HTML **Skill Health Report** written to disk.
- `npx skillscan pack` → bundles the top-N skills into a shareable folder/gist with a one-line install command.
- `npx skillscan install <url>` → the teammate side. This is the second-person event.
- Opt-in anonymous aggregate submission (`--contribute`), which is how "The State of Agent Skills" dataset accumulates. Consented and visible from day one, or the benchmark never exists (H6).
- README with run instructions, a sample report checked into the repo, and an explicit limitations section.

**Design it to be changed live.** The brief's session includes 10 minutes to extend one part together. Keep the checks as separate, obvious modules so a new check can be added on the call in a few minutes. Say so in the readout and name the check you would add.

### D3 · Evidence appendix
Largely already built (`evidence_brief.html`). Confirm it carries: every load-bearing number with source + pull date + confidence tag; the verification log including the two corrections; null results with exact queries; hypotheses H1–H10 with dated status; rejected alternatives with the steelman intact; the 58-prospect list.

### D4 · AI work log
Four required parts, with the two hard ones answered as follows:

- **Where AI was wrong:** the NVIDIA skill-security figure, originally rendered as "nearly 1 in 4 could compromise a system" — a conflation of two separate statistics that overstated the security case roughly 5x, caught by an independent verification pass, alongside a second figure downgraded to unusable because it was a vendor self-report in an unresolved issue. Concrete, dated, self-caught, and it *weakened* the pitch rather than strengthening it — which is the point.
- **The decision AI could not make:** the ICP and channel calls themselves. Earlier AI work in this project wrote D1–D12 into the decision log as settled decisions; that was caught and every row was downgraded to "recommendation, pending confirmation," with a standing rule that AI analyses and Manan decides. That correction is dated and visible in the file history. It is a better answer than any modelling assumption, because it is about who owns the call, not about which number to pick.
- **Systems built:** the folder discipline itself — hypotheses before evidence with kill criteria, confidence tags on every claim, null results logged with exact queries, blocked-source retry rule, research filed by the agent that found it. Plus the reusable prospect-harvesting-as-a-byproduct-of-research pattern that produced 68 named people at no extra cost.

## 5. Sequence — Sat 5 Sep to Thu 10 Sep

| Day | Do |
|---|---|
| **Sat 5** | Confirm ICP / channel / activation. Send the six questions to Atlan (especially Q5: what may be said publicly). Verify the session-transcript assumption. |
| **Sun 6** | Build scanner v0 — scan, parse, dedupe, context cost, usage. Run on own machine. First real report. |
| **Mon 7** | `pack` / `install` / `--contribute`. Publish repo. Run against 3–5 friendly users to debug before strangers see it. |
| **Tue 8** | **Outreach ships.** Tier 1 (6) individually written, naming their own tool's actual gap. Tier 2 (52) referencing their own issue or post by name. Every message states it is a candidate exercise. |
| **Wed 9** | r/claudeskills post live ("I built X to solve Y"). Start assembling D1, D3, D4 against real data. |
| **Thu 10** | Freeze. Write "what ran and what came back." Submit all four. |

**Non-negotiable:** outreach ships Tuesday. A campaign with real replies in it is the entire difference between this submission and a strategy deck — the brief's floor is "ready to run," and the ceiling is "already ran."

## 6. What would make me abandon this plan
- Atlan answers Q5 with "nothing public" → the tool stays private-beta and Wave 1 becomes network-only outreach; the loop and the artifact are unchanged, only the Reddit leg dies.
- Session transcripts do not carry invocation data and no fallback works → the report loses its headline, the evidence-layer claim gets thinner, and the honest move is to say so rather than dress up a file count.
- Tier 1 outreach shows the not-invented-here resistance H10 warned about strongly enough that nobody engages → the ICP narrows to Tier 2 (documented pain, no fix built) and the readout says why.
