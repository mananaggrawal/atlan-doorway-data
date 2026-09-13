# Hypotheses and kill criteria
Written 2026-09-05. Each hypothesis was stated before its evidence was gathered where possible; where evidence already existed at the time of writing, that is noted. Status updated in place, with dates.

---

## H1 — The sharing moment is a real, felt, current pain
**Statement:** Developers publicly and repeatedly ask how to get a skill to a teammate, and no native answer exists.
**Kill criterion:** Fewer than three independent, dated public instances; or Anthropic has shipped a native answer.
**Status: SURVIVED (2026-09-05).** Five independent GitHub issues over six months, the canonical one closed `not_planned`. Threshold reported at ~5 engineers, not 50. See `analysis/evidence_synthesis_v1.md` B1.

## H2 — Sprawl degrades the product, so governance has a selfish payoff
**Statement:** Past a few dozen skills, invocation quality measurably drops, so an individual — not just an org — benefits from curation.
**Kill criterion:** The context budget turns out to be generous enough that nobody notices; or no practitioner articulates it in their own words.
**Status: SURVIVED (2026-09-05).** Budget confirmed at 1% of context, 1,536 chars per description. Articulated this week by OpenAI's Codex DX lead to 1.5M views. Anthropic ships `/skill-doctor`, and its numbers are publicly contested.

## H3 — Trust is the enterprise-legible version of the same problem
**Statement:** Fear of running someone else's skill is documented and quantified, making governance purchasable rather than merely tidy.
**Kill criterion:** No credible security research; no enterprise guidance published.
**Status: SURVIVED (2026-09-05).** NVIDIA scanned 42,447 skills — 26.1% with at least one vulnerability, 5.2% likely malicious. Red Hat published enterprise guidance Aug 2026.

## H4 — The do-nothing alternative is weak
**Statement:** Teams have no workable status quo.
**Kill criterion:** Credible practitioners describe a git-based setup that works fine for them.
**Status: WEAKENED (2026-09-05).** They do. The real baseline is "a git repo plus Anthropic's native plugin marketplace, DIY," defended by credible engineers. **Any pitch must answer "why not just git" directly.** This is now a required slide, not an afterthought.

Reddit sharpened it further. The best-argued objection is conditional rather than absolute — *"If you're not hitting friction on either, the elaborate setup just adds overhead without real benefit"* (117 upvotes, r/ClaudeCode) — which is falsifiable and therefore answerable: name the two frictions and show the threshold. And one objection no other surface carried at all:

> *"what keeps you valuable keeps you hired... never train your potential or actual replacement"* — top comment, 99 upvotes, r/ClaudeAI

Skill hoarding as career strategy is a real GTM obstacle, and it argues for making the individual payoff (your own agent gets better) load-bearing rather than leading with team altruism.

## H5 — The wedge is unclaimed
**Statement:** Nobody is building a governed home for skills yet.
**Kill criterion:** Two or more credible products already shipping against it.
**Status: KILLED (2026-09-05).** shareskills.ai (blog post dated the same day we searched), Tessl, JFrog AgentSecOps, NVIDIA SkillSpector, AWS Agent Registry GA, plus ~12 "package manager for skills" Show HNs since January. **Consequence: differentiation cannot be "we store your skills." It has to be the evidence layer — usage, traces, evals, dependencies — which is exactly what AWS deferred and what Atlan already demos.**

## H6 — There is no public baseline for how many skills a team has
**Statement:** The number that decides every ICP threshold in this market does not exist publicly.
**Kill criterion:** Any published figure from a credible source.
**Status: SURVIVED (2026-09-05).** Three independent researchers hunted; all came back empty. **This is our opening: the missing number is simultaneously a research artifact, a campaign and a distribution loop.**

---

## Open, not yet tested

## H7 — Which workload leads
Coding (Claude Code / Codex-heavy engineering teams) beats knowledge-worker and operational workloads as the first ICP, because the pain is sharpest, the population is measurable, and the artifacts are public.
**Kill criterion:** Evidence that knowledge-worker teams hit the sharing threshold sooner, or that coding teams have already solved it internally.
**Status: RECOMMENDED BY ANALYSIS, PENDING DECISION (2026-09-05).** Not yet chosen by Manan. Favored in the analysis because H1-H3's entire evidence trail — the GitHub issues, the Reddit threads, the 5-engineer friction threshold — comes from exactly this population, while knowledge-worker and operational teams produced zero comparable public evidence in the sweep. See `decision_log.md` D9 and `the_bet.md`. The kill criterion is unchanged and still open to being falsified in discovery interviews. Sharpened further by H10 below: the wedge user within this population is specifically someone who has already built or is maintaining a homegrown point-fix, not merely anyone at a Claude-Code-heavy company.

## H8 — The channel
A free, one-command open-source tool that measures your own skill sprawl — and produces a shareable report — outperforms both a public directory play and an AWS-partner motion, because it *is* the product's own activation mechanic, it generates the missing public dataset, and the report is the advertisement.
**Kill criterion:** The tool gets installs but no sharing; or the report tells people nothing they didn't already know.
**Status: RECOMMENDED BY ANALYSIS, PENDING DECISION (2026-09-05).** Not yet chosen by Manan. Favored in the analysis over a public directory (H5: crowded, no room to differentiate) and an AWS partner motion (too slow, account-scoped, wrong population). The report is also how H6 gets closed — it generates the missing benchmark rather than just describing the gap. See `decision_log.md` D10 and `the_campaign.md` for the activation funnel built on top of this. Kill criteria unchanged.

## H9 — Activation definition
3+ people in one workspace with at least one skill that has a named owner, a version, and usage by a second person, is the smallest unit where the product does something a folder cannot.
**Kill criterion:** Atlan steers by a different number, or teams stall at solo use with no observable path to the second person.

---

## H10 — The highest-intent ICP is revealed by who already built something, not just who complained
**Statement:** Individuals and teams who have already spent real engineering time building a bespoke point-solution for sync, versioning, approval, or dedup — rather than only posting about the pain — are more pained, more qualified, and more convertible than people who merely commented on a GitHub issue or upvoted a Reddit post.
**Kill criterion:** Outreach to named internal-tool builders shows sunk-cost / not-invented-here resistance strong enough that they won't engage in a discovery conversation at all — i.e., they defend their own tool rather than acknowledging its gaps.
**Status: SURVIVED on desk evidence (2026-09-05), not yet tested by outreach.** At least a dozen named individuals across GitHub, Reddit, HN, X and LinkedIn independently built a bespoke fix for one slice of this exact problem: sync (zwaantjuh's manual ZIP re-uploads, Justin Trugman's internal skills marketplace), governance/audit (Necessary_Abroad6632's `agpm` CI approval gate), or manual measurement (Abhisheik Deo's hundred-developer usage audit, Abu_BakarSiddik's open-sourced Skill Manager built after hitting 140+ skills). None of them combined ownership + version + dependency + live usage/eval/trace across harnesses — the same gap AWS's own launch blog defers to roadmap. This is revealed preference, not stated preference: a GitHub comment costs a sentence, a homegrown tool costs real engineering time.

A separate cluster of named people (mrdonbrown/sx, alex_metacraft/Askill, laul_pogan/Ingot, theahura/noriskillsets.dev, dariusmonsef/OzBrain, rgbrgb/setoku, conikeec/skillrecall, Pethuraj M/AgentSeal) built the *same kind* of point-solution as a public product rather than an internal tool. These are competitors and evidence for H5, not outreach prospects — conflating the two would mean pitching a rival founder as a customer. Kept separate in `../2_research/prospects/prospect_candidates.md`.

**Risk to flag explicitly, not paper over:** sunk-cost / not-invented-here resistance is real and is itself named in the evidence — Sammi's HN comment ("I've failed to see the need over what I already have") is the live version of this exact objection, aimed at a very similar pitch (OzBrain). It needs a specific answer per builder (naming their tool's actual gap), not a generic pitch, before this tier of outreach can be trusted to convert.
