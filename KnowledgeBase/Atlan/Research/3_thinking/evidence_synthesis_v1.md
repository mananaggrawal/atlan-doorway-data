# Evidence synthesis v1 — what the public record actually says
2026-09-05. Sources: `2_research/community/*`, `2_research/numbers/*`. Every number below survived an independent verification pass (`2_research/numbers/verification_log.md`) unless flagged.

## Headline

The pain is real, specific, and dated. It is **not** undiscovered — at least a dozen teams are already building point solutions against it, one of them launched a blog post the same day we searched. So the opening is not "nobody has noticed." The opening is that **everyone is building the shelf, and nobody is building the evidence.**

---

## B1 — The sharing moment: REAL, and better documented than expected

The single best artifact in the whole sweep:

> **"My team would like to share SKILLS we write within the team. We created a repo to keep them central."**
> — robosung, 25 Feb 2026, [anthropics/claude-code#28327](https://github.com/anthropics/claude-code/issues/28327) · **[verified]** · 7 reactions · **CLOSED as not_planned**

Two separate issues (#33530, #39403) were auto-closed as duplicates of it. One of them:

> **"there's no clean native way to share a common skill library without resorting to symlinks or duplicating skill files everywhere."**
> — pablo-aviles-ruiz, 26 Mar 2026, [#39403](https://github.com/anthropics/claude-code/issues/39403) · **[verified]**

**Why this matters more than any survey:** Anthropic was asked, repeatedly, to solve team skill sharing natively — and closed it `not_planned`. That is a documented, dated vacancy in the platform, not our opinion.

Supporting, all [verified]:
- **The threshold is ~5 engineers, not 50.** *"ran into the friction point pretty fast on our end at ~5 engineers... adding a new skill means everyone re-syncs manually"* — latentloop07, 13 May 2026, [anthropics/skills#1132](https://github.com/anthropics/skills/issues/1132). Zero replies in four months.
- **The value is stranded, not missing.** *"We had built a library of proprietary skills... All of that value was stranded on individual machines."* — Justin Trugman, 15 Jun 2026, betterfuturelabs.com.
- **The onboarding failure is vivid.** *"None of it travels. New hires inherit a blank `.claude/` folder and a Slack thread of partial screenshots."* — claudefa.st, 2026.
- **Fragmentation is native to Anthropic's own surfaces.** *"A user has to register the same GitHub repo three separate times, through three separate flows, to use the same skills everywhere."* — deepumukundan, 25 Aug 2026, [#89413](https://github.com/anthropics/claude-code/issues/89413).
- **The org-scale ask exists too.** *"most teams still treat skills as static artifacts... Skills are duplicated, and updates never roll out... Skill knowledge grows stale"* — Guy Podjarny (Snyk founder, now Tessl), HN. And a practitioner reply asking unprompted for *"a CI integration where you can pin a skill version and fail builds if eval scores drop."*

## B2 — Sprawl and decay: REAL, and now mainstream enough that Anthropic ships a tool for it

- **The mechanism is documented and confirmed:** the skill listing *"scales at 1% of the model's context window"* and each description is *"capped at 1,536 characters regardless of budget"* — code.claude.com [verified]. Past a few dozen skills, sprawl actively degrades invocation.
- **The most credible voice said it this week.** Eric Provencher (@pvncher, Codex DX at OpenAI, 37.9K followers), 5 Sep 2026: *"Many people default to downloading a lot of skills into their projects, but that's a mistake... when you add too many skills, Codex starts shortening their descriptions to fit."* **1.5M views, 3.5K likes.** [verified]
- **Anthropic already ships `/skill-doctor` for pruning — and its numbers are contested.** *"/skill-doctor's per-skill token/usage table is misleading enough to actively mislead pruning decisions"* — shrek1ee, 5 Sep 2026, [#92327](https://github.com/anthropics/claude-code/issues/92327). A shipped-but-broken diagnostic is an unusually clean opening.
- Practitioner diary: *"If you have too many skills, they get silently truncated. More is not better"* — shimo4228, dev.to, Feb 2026, who audits every 1-3 days.

## B3 — Trust: the most mature bucket, and the most enterprise-legible

- **NVIDIA scanned 42,447 skills: 26.1% contain at least one vulnerability; 5.2% show likely malicious intent.** Released an open-source scanner, SkillSpector. [verified — note: an earlier summary of this said "nearly 1 in 4 could compromise a system", which conflates the two figures. Use the two numbers separately.]
- **Red Hat published enterprise governance guidance, Aug 2026:** *"the marketplace runs on an implicit trust model: no centralized vetting, no code signing, no runtime sandboxing."* [verified]
- SentinelOne (Jan 2026) demonstrated dependency hijack via an installed skill; PromptArmor showed malicious marketplaces listed *"within an hour."*
- Scanners disagree with each other: on skills.sh, three scanners returned Safe / no alerts / Critical for the same skill ([vercel-labs/skills#1722](https://github.com/vercel-labs/skills/issues/1722)).
- ⚠️ **Do not use** the "552 malicious out of ~96,000 scanned" figure without heavy caveat — it is a self-reported claim by a vendor in an open feature request, with no linked audit.

## B4 — Counter-evidence: thin, but the honest baseline is real

Nobody credible argues "skills are overrated." The real do-nothing case is narrower and stronger:

> *"Every few weeks we rediscover that the thing people actually keep is a folder of markdown in git, and then we build a registry in front of it."* — parasxos, HN [verified]

> *"I have a folder called reports, plans, and code-reviews in each repo... voila they're in the cloud along with my source code in git... I've failed to see the need over what I already have."* — Sammi, HN [verified]

**The baseline to beat is not "nothing." It is "a git repo plus Anthropic's native plugin marketplace, assembled DIY."** Any pitch that doesn't answer "why not just git" loses to it.

## The crowded-space problem (the most important strategic fact)

The wedge is not unclaimed. Already shipping or launching against it:
- **shareskills.ai** — "Your team's skills, in sync." Blog post *"Sharing is not a library"* dated **5 Sep 2026** — the same day we searched. [verified]
- **Tessl** (Guy Podjarny, Snyk founder) — skills lifecycle.
- **JFrog AgentSecOps** — Agent Packages registry inside Artifactory.
- **NVIDIA SkillSpector**, plus independent scanners Vett, Skillcop, Aguara, SkillSpec, Socket, AgentSeal.
- **AWS Agent Registry** — GA 31 Aug 2026 (preview 9 Apr 2026); old `bedrock-agentcore` namespace retires 17 Sep 2026.
- A dozen "package manager for agent skills" Show HNs since Jan 2026 (Ingot, Askill, Skill.Fish, Enact, SkillCatalog, ArteSync, APM, skillregistry.io, noriskillsets.dev). **No winner. Mostly single-digit HN points.**

Read: the *shelf* is commoditising fast. What nobody has is what AWS explicitly deferred and Atlan already demos — **usage, traces, evals, dependencies.** Differentiation is evidence, not storage.

## The gap nobody has filled — and our opening

**Nobody has published how many skills a typical developer or team actually has.** Three independent researchers hunted for it; all came back empty. It is the number that decides every ICP threshold in this market, and it does not exist publicly.

That is not just a research gap. It is an artifact, a campaign and a distribution loop in one.

## Market size sanity check [all verified]

| Fact | Figure | Source |
|---|---|---|
| `@anthropic-ai/claude-code` npm downloads | 80,220,622 / month · 21,450,823 / week | api.npmjs.org |
| `skills` (skills.sh CLI) npm downloads | 38,365,913 / month · 9,363,514 / week | api.npmjs.org |
| Developers using AI coding agents weekly / daily | 90% / 68% (n > 15,000) | JetBrains dev survey, Aug 2026 |
| Claude Code adoption, global / US | 39% / 47% | JetBrains, Aug 2026 |
| skills.sh all-time installs | 1,320,673 (site's own top skill claims 3,267,851 — the site's numbers contradict each other) | skills.sh |
| `anthropics/skills` GitHub | 174,457 stars · 20,662 forks | api.github.com |
| Agent Skills launch | 16 Oct 2025 | anthropic.com/engineering |

## Channel read from the evidence

- **X** — the conversation is real and daily, but diffuse: most on-topic posts get under 500 views, with rare 1M-view spikes from insiders. Good for listening, discovery and messaging validation. Not an acquisition channel on its own.
- **LinkedIn** — "AI Enablement" is a real, named job title at Toyota, Ford, Deloitte, Eightfold. The buying centre exists. But expert posts get 4-5 reactions while beginner explainers get 400. Right persona, wrong energy for a launch.
- **GitHub** — the highest-precision surface we found. The people in those five duplicate issues have the exact pain, are named, and are reachable. Small n, very high intent.
- **Reddit** — blocked from every tool in this session. Logged as a gap, not as silence.
- **Google search** — the category name itself ("agent registry") gets ~140 searches/month; nobody is searching for what Atlan calls itself. But "claude code skills," "claude skills marketplace" and a how-to long tail get real, growing, uncontested volume. Not a substitute for GitHub/Reddit as the Wave-1 channel — see addendum below — but a real second-wave SEO candidate.

---

# Addendum — Reddit (added 2026-09-05, after the surface was reopened)

Reddit was unreachable from every research tool and was later read through the user's own browser. It confirmed more than it surprised, but it carried two things no other surface did.

**B1 — the sharing ask, in an admin's own words** [verified]:
> *"currently for every update I have to manually re upload the ZIP files als org skills... Ideally it'd be a Github that I can commit / push new changes to that automatically sync with everyone's claude environments."*
> — zwaantjuh, r/ClaudeCode, [thread](https://www.reddit.com/r/ClaudeCode/comments/1vgb33u/best_way_to_update_and_maintain_organization/)

The replies are people hand-assembling Atlan's mechanic out of raw parts: private-repo-as-marketplace, `extraKnownMarketplaces` entries pushed through `settings.json`, manual per-seat plugin updates. Six upvotes, eleven comments — precise, and almost invisible.

**B2 — sprawl, quantified by someone who hit it** [verified]: a practitioner built and open-sourced a "Skill Manager" after reaching 140+ skills across ~11 folders *"with no shared view"*, reporting visible triggering degradation. r/claudeskills.

**B3 — trust, framed as a dependency problem** [verified]:
> *"Everyone's .claude/skills/ folder is filling up with stuff pulled from marketplaces, gists, npx skills, random repos... nobody reviews them the way they'd review a dependency bump."*
> — Necessary_Abroad6632, r/ClaudeCode

**B4 — the two objections that matter most, and only Reddit had them:**
> *"If you're not hitting friction on either, the elaborate setup just adds overhead without real benefit."* — 117 upvotes, r/ClaudeCode

> *"what keeps you valuable keeps you hired... never train your potential or actual replacement"* — 99 upvotes, r/ClaudeAI

The first is a conditional objection, which makes it answerable: name the frictions and show where the threshold sits. The second is skill hoarding as career strategy, and it is the strongest argument yet for leading with the **individual** payoff — your own agent gets better — rather than with team altruism.

**B5 — channel shape:** r/ClaudeAI (~1.6M weekly visitors) and r/ClaudeCode (~745K) are showcase-dominated; a governance pitch will not cut through. r/claudeskills is small (~66K, created Oct 2025) but purpose-built and dense, with 750+ upvote posts on exactly this topic. Viable for a well-crafted "I built X to solve Y" post, not for a positioning argument.

**Method note:** Reddit's own search is weak — exact-phrase and `title:` queries returned zero even for threads known to exist. Most of the above came from following "Related posts" rails rather than the search box.


---

# Addendum — Google search demand (added 2026-09-05, Semrush pull)

Full data and read in `2_research/numbers/search_demand_semrush.md`. Summary:

**The category term is dead.** "agent registry" (140/mo), "ai agent registry" (50/mo), "agent skill registry" (10/mo) — nobody searches the name any of us, or AWS, use for this. Consistent with B1 above: the pain lives in GitHub issues and forum threads, not search bars.

**Real, growing demand exists, just under different words.** "claude code skills" (8,100/mo, $5.26 CPC, commercial intent), "claude skills marketplace" (2,900/mo, $7.84 CPC, climbing hard the last two months), "context engineering" (3,600/mo, one of the fastest-climbing terms in the whole pull). Underneath that, actual developer query language is procedural — "how to add skills to claude code" (320/mo), "how to create custom skills for claude code" (170/mo) — low-competition, unclaimed long tail nobody appears to be targeting with content.

**New competitive fact, not previously in this file:** two registry-adjacent search spikes — "mcp registry" (1,600/mo) and "claude code plugin marketplace" (880/mo) — trace directly to Anthropic's own launches (MCP donated to a new Agentic AI Foundation with an official registry; Anthropic's own plugin marketplace, ~Feb 2026), not organic category pull. Folded into `2_research/market/registry_landscape.md` as dated updates. **Read: Anthropic itself is now the fastest-growing source of "registry"-adjacent demand.** This sharpens rather than changes D4 (differentiation = evidence, not storage) — the shelf is being commoditised by the platform vendor itself, not just by a dozen startups.

**Enterprise buyer language is real but expensive and top-down-flavored:** "ai agent security" ($28.21 CPC), "ai agent governance" ($15.79 CPC, just hit its 12-month peak), "agentic ai governance" ($22.50 CPC) — matches Atlan's existing CDO motion (D3), not the bottom-up ask.

**Does not change the channel decision (D10).** Google volume for a feature this new is a lagging, low-n signal, and most of the "claude code skills" volume is plausibly generic curiosity rather than acute sharing/governance pain. It surfaces one candidate second-wave lever worth naming alongside `3_thinking/path_to_100.md`'s repeating-loop model: a lightweight SEO-facing asset (e.g. a "State of Claude Code Skills" page) targeting the terms above would meet real, currently-uncontested organic traffic without competing with the Wave-1 GitHub/Reddit channel — a candidate for `the_campaign.md`'s second wave, not a change to the Wave-1 bet itself.
