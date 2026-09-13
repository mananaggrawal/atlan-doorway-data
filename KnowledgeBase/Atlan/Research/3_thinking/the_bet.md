# The bet
**Status: ANALYSIS, NOT DECIDED (corrected 2026-09-05).** Everything below is AI-generated analysis and a recommendation — not a decision. ICP, channel and activation get decided jointly with Manan; nothing here is final until he confirms it. `the_campaign.md` is a draft built around these candidates, ready to run once confirmed.

## Leading candidates (pending joint decision)
- **Activated team** = 3+ people in one workspace with at least one skill that has a named owner, a version, and usage by someone other than its author. Rationale in `../1_brief/understanding_v1.md` §3.
- **Differentiation is evidence, not storage** — usage, traces, evals, dependencies. Forced by H5 being killed; see `hypotheses.md` and `decision_log.md` D4.
- **"Why not just git" is a required slide**, not an afterthought. See `rejected_alternatives.md`.
- **Candidate ICP (recommended, not decided): AI-native engineering teams already running Claude Code/Codex at meaningful skill volume — sharpened to specifically whoever has already built or is currently maintaining a homegrown point-fix** for sync, versioning, approval, or dedup (a manual re-upload process, an internal marketplace, a CI approval gate, a usage audit). This is a revealed-preference signal, not a survey answer: a dozen named individuals independently paid real engineering time patching one slice of this exact problem, none combining what a full registry does. Not a top-down AI-enablement leader (already rejected, see `rejected_alternatives.md`), not a knowledge-worker team (no evidence trail), not an AWS-account-scoped audience (wrong population). See D9, sharpened by D11/H10. **Distinct from the founders building the same kind of point-solution as a public product** (Ingot, Askill, noriskillsets.dev, OzBrain, sx, skillrecall, AgentSeal, Tessl, shareskills.ai) — those are competitors and H5 evidence, not the outreach list. **Not yet empirically validated** — this is the working hypothesis to build against, not a confirmed fact.
- **Candidate channel (recommended, not decided): a free, one-command, open-source skill-health scanner + shareable report.** Beats a public directory (crowded — H5) and an AWS partner motion (too slow, wrong audience — see `rejected_alternatives.md`). The report doubles as the acquisition asset and, aggregated across runs over time, as the missing "skills per team" benchmark that closes H6. See D10. Also **not yet validated**.
- **Lead with the individual payoff, not team altruism.** The Reddit finding that skill-sharing reads to some engineers as "training your replacement" (H4/B4) means the funnel has to open with "your own agent gets better," and only *then* invite teammates in. See `the_campaign.md`.

## Still open — execution, not strategy

**Named risk on the ICP call:** sunk-cost / not-invented-here resistance among homegrown-tool builders is real and is itself in the evidence — Sammi's HN comment ("I've failed to see the need over what I already have") is the live version of this objection. It needs a specific, per-builder answer (naming their tool's actual gap), not a generic pitch, before this outreach tier can be trusted. See `hypotheses.md` H10.

| Question | Why it's still open |
|---|---|
| What "duplicate," "unowned," "unused," "risky" can honestly mean when the scanner only ever sees one laptop | A solo scan cannot detect cross-person duplication or true team-level ownership gaps — those only become real once a second teammate scans into the same workspace. The v1 report needs to be explicit about this boundary rather than overclaim. See `decision_log.md` O3. |
| Exact tool / report / campaign naming | Working names only: CLI `atlan-skill-scan`, output "Skill Health Report," aggregate campaign "The State of Agent Skills 2026." Not finalized. |
| Whether to run live discovery interviews | ~70 named candidates already on file (`../2_research/prospects/prospect_candidates.md`); time and Atlan's answer on what we may say publicly are the actual constraints. |

Evidence for the ICP/channel calls: `evidence_synthesis_v1.md`, `hypotheses.md` H6–H9, and a review of the research synthesized externally on 2026-09-05 that sharpened — without contradicting — H7/H8 into an actual decision rather than leaving them open.
