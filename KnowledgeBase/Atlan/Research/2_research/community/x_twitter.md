# X (Twitter) Evidence: How Developers/Teams Manage & Share AI Agent Skills
Research date: 2026-09-05. Method: X search (`f=live` and `f=top`), 26 distinct queries, permalinks verified in-browser. All quotes verbatim, ≤50 words, [verified] = read directly in browser this session.

---

## B1 — SHARING (getting a skill to a teammate, team rollout, internal libraries, sync across machines, versioning/ownership)

**Christina (@truffle)** — indie/dev, community skill user. Sep 1, 2026.
> "My Claude user directory is a git repo that auto installs my plugins. Most of my skills are in my plugin repo. I keep my work environment and git repos in sync across four machines."
https://x.com/truffle/status/2094800747904806924 — [verified]
Why it matters: exact multi-machine sync pain point named in the brief, solved today with a personal git-repo hack — no team-facing ownership/versioning layer.

**The Startup Ideas Podcast / quoting Remy "AI with Remy" (@startupideaspod)**. Aug 20-21, 2026.
> "How to turn his AI skills into a plugin his whole team installs ... Most people build a great skill, then trap it on..."
https://x.com/startupideaspod/status/2090559506317201692 — [verified] (11.9K views)
Why it matters: names the exact failure mode a registry fixes — a good skill "trapped" on one person's machine instead of installed by the whole team.

**Dan Kornas (@DanKornas)** — builds/promotes dev tools. Sep 5, 2026.
> "Suede Creator Skills is an open-source collection of agent skills for builders using Claude Code, Codex, or other skills-compatible agents. It helps you add reusable workflows to an..."
https://x.com/DanKornas/status/2096236659574477166 — [verified] (778 views)
Why it matters: another public "skill pack" distributed as a repo — sharing today means a GitHub repo, not a managed registry.

**Rich Steinmetz (@RichStoneIO)**. Sep 3, 2026.
> "If you rely on global Claude skills on your local machine, make sure they don't irreversibly change their behavior... One useful thing I started doing a while ago is versioning my global Claude..."
https://x.com/RichStoneIO/status/2095549976461951408 — [verified] (137 views)
Why it matters: unprompted, self-initiated versioning of skills — organic demand for the exact feature a registry provides natively.

**49Agents IDE (@49agents)**. Aug 31, 2026.
> "are you versioning skills as plain markdown files in git or something structured? i keep hitting stale instructions with claude code, too many CLAUDE.md files with overlapping rules."
https://x.com/49agents/status/2094198834880504077 — [verified] (292 views)
Why it matters: explicit ask for a structured (non-git-file) versioning approach; names staleness/overlap as the failure mode.

**DarkHorseDelta (@0MeissnerState)**. Sep 3, 2026.
> "AWS made Agent Registry generally available: a shared catalog of agents, tools and skills. Useful, because the fifth team building the same internal agent is not innovation."
https://x.com/0MeissnerState/status/2095481937058021784 — [verified] (2 views)
Why it matters: names duplicate-build-across-teams as the core waste a shared registry solves — and flags AWS is already shipping this (competitive signal, see B4/B5).

**DannielDevOps (@DannielDevOps)**. Sep 5, 2026.
> "Skills.sh as a search and install catalog for agent skills beats copying another skill.md by hand."
https://x.com/DannielDevOps/status/2096228201982992474 — [verified] (9 views)
Why it matters: explicitly frames "copying a skill.md by hand" as the bad default that a catalog replaces.

**코지베어 CozyBear (@cozybearlog)**. Jul 28, 2026.
> "Matt Pocock shipping his skills as a Claude Code plugin feels like a small thing but it signals a real shift... Now there's a package manager for it. Aliases, versioning, the whole deal."
https://x.com/cozybearlog/status/2082031639228805541 — [verified] (45 views)
Why it matters: a known dev-education influencer's skill-pack release is read by observers as evidence of an emerging "package manager for prompts" category — market naming itself.

**eric provencher (@pvncher, Codex DX @OpenAI, 37.9K followers)**. Sep 5, 2026.
> "Repository skills also guide other contributors' agents, which may use different models. Guidance that helps Sol or Luna may overconstrain GPT-6 Astra, so consider which models will use the instructions you leave behind."
https://x.com/pvncher/status/2095991462416490862 — [verified] (1.5M views, 3.5K likes, 452 reposts, 80 replies)
Why it matters: an OpenAI Codex DX staffer, writing to a 1.5M-view audience, names cross-model / cross-contributor compatibility as a live problem for repo-shared skills — directly adjacent to a governed registry's job.

**Yarchi (@undefinedKi)**. Aug 30, 2026.
> "If Claude only let you install five skills, I know exactly which five. Marketing skills by Corey Haines - github.com/coreyhaines31/marketingskills. 50 skills covering ads, email, pricing, SEO, cold outreach."
https://x.com/undefinedKi/status/2094027112394944633 — [verified] (5.4K views)
Why it matters: another public, unmanaged skill pack (50 skills in one repo) being recommended — shows appetite for curated skill collections and a total absence of vetting/versioning around them.

---

## B2 — SPRAWL (too many skills, wrong one fires, context budget, duplicates, staleness)

**eric provencher (@pvncher, Codex DX @OpenAI)**. Sep 5, 2026. Same "Rethinking skills and prompts for GPT-6 Astra" article as above.
> "Many people default to downloading a lot of skills into their projects, but that's a mistake... when you add too many skills, Codex starts shortening their descriptions to fit."
https://x.com/pvncher/status/2095991462416490862 — [verified] (1.5M views)
> "descriptions can contradict each other or have too much 'pick me' energy, leading the model to load instructions that don't actually help the task."
same URL — [verified]
Why it matters: the single highest-reach post in this entire research is a detailed, practitioner-authored teardown of skill sprawl (wrong-skill-firing, context burn, description bloat) — as close to a thesis-validating post as this research found.

**Darren Shepherd (@ibuildthecloud)** — Rancher/Acorn co-founder, infra-credible voice. Sep 3, 2026.
> "Isn't anyone worried about 'too many skills' The issue is that I can easily make the LLM to progressive discovery and not have to load all the skills at once, but if I want the skills for the user (they type /foo) I have to separate them out."
https://x.com/ibuildthecloud/status/2095555415971143695 — [verified] (1,140 views)
Why it matters: a credible infra builder naming the exact "too many skills" problem publicly and getting real engagement (1.1K) — high-credibility, on-topic voice.

**Mike Britton (@mbritton)**. Sep 4, 2026.
> "I'm writing too many skills and burning tokens needlessly when specs change. It feels wrong. The creative momentum is tempting."
https://x.com/mbritton/status/2096115952089710600 — [verified] (8 views)
Why it matters: names staleness (specs change) plus token-burn as concrete costs of unmanaged skill proliferation.

**patrick mcqueeny (@humansandaiboss)**. Sep 4, 2026.
> "yes there are too many skills and mcps to choose from, no focusing on tools is not the wrong path, quality over quantity, better tooling is the most efficient axis of advancement from here."
https://x.com/humansandaiboss/status/2096109356156592467 — [verified] (9 views)

**Jax Koh (@jaxkoh_)**. Sep 3, 2026.
> "I spent so much times on configuring my AI setup and ended up lost in the my configurations. I can't remember which session did what, where to point my agent, too many skills/instructions created."
https://x.com/jaxkoh_/status/2095578862877073792 — [verified] (52 views)
Why it matters: describes losing track of what skill/config did what — a discoverability and ownership problem, not just a volume one.

**ΘΣ (@thetasigma_io)**. Sep 3, 2026.
> "most of cases are caused by bad skills or too many skills installed or just bad global AGENTS.md... i fixed all issues with adaptive development, auto switching between skip SDD, lean SDD and strict SDD."
https://x.com/thetasigma_io/status/2095562823380418710 — [verified] (13 views)

**Nick Launches AI Agents (@nicklaunchesai)**. Sep 4, 2026.
> "81,811 MCP servers in one registry. 3,004 agent skills in another. Nobody can read all that. So most people pick an agent for what it does, then find out it can't reach the one tool they actually needed."
https://x.com/nicklaunchesai/status/2096131257407324642 — [verified] (95,110 views)
Why it matters: ecosystem-scale sprawl number with the highest engagement of any pure-sprawl post found (95K views) — evidence the "too many, ungoverned" framing resonates broadly, not just among security wonks.

**chetan conikee (@conikeec)**. Sep 4, 2026 (open-sourced "skillrecall").
> "Most agent skills lose requests to a competitor the author has never heard of ... When my skill sits next to 40 others in any harness, how often does the host pick it for a..."
https://x.com/conikeec/status/2095951157361598550 — [verified] (325 views)
Why it matters: a builder shipped an actual open-source tool to measure "wrong skill fires" / pickup-rate competition among installed skills — direct evidence sprawl causes measurable selection failures, not just clutter.

**mjhhh (@Ma7039Ma)**, Chinese-language, Sep 3, 2026.
> "还记得当时刚接触agent的时候啥都不懂 一碰到skills.sh上的感觉用得到的skills就无脑装 ... 后来终于意识到不对了 ... 然后删了半天 再接着学聪明了只装需要的"
(approx.: "When I first got into agents I mindlessly installed every skill on skills.sh that looked useful... eventually realized this was wrong... spent ages deleting them... learned to only install what I need.")
https://x.com/Ma7039Ma/status/2096232462632321445 — [verified] (52 views)
Why it matters: a first-person install-everything-then-purge-everything arc — the sprawl lifecycle in miniature.

**Corey J. Gallon (@CoreyGallon)**, re: Patrick Debois (Tessl) talk. Sep 1, 2026.
> "Coding Agents Don't Scale Themselves. Neither Do Your Teams... Patrick is a Member of Technical Staff at Tessl, and he spends the whole talk on..."
https://x.com/CoreyGallon/status/2094791348700266704 — [verified] (139 views)
Why it matters: names organizational (not just technical) scaling as the real bottleneck — a Tessl staffer's conference talk on the exact team-scaling problem a governed registry addresses.

---

## B3 — TRUST (running someone else's skill, prompt injection, secrets in skills)

**Strata Mind Labs (@stratamindlabs)**. Sep 5, 2026. [The single strongest B3 find.]
> "AI skills are starting to behave like software dependencies. And most organizations do not yet have an intake gate for them."
https://x.com/stratamindlabs/status/2095996431068754426 — [verified] (67 views)
> "A clean scan should not automatically mean 'install.' Security asks: Is it safe? Policy asks: Is it permitted? Governance asks: Who decides?"
same URL — [verified]
Why it matters: this is close to a verbatim articulation of the governed-registry thesis — supply-chain framing, intake gate, and a three-part security/policy/governance split — plus it name-checks NVIDIA's SkillSpector scanner as existing competitive infrastructure.

**Silk node (@SilkNodeio)**, replying to the above. Sep 5, 2026.
> "Does approval bind the exact skill and dependency versions? A clean intake scan becomes stale when either changes. The useful failure test is whether an updated package loses its old execution authority until it is reviewed again."
https://x.com/SilkNodeio/status/2096001185358458917 — [verified] (46 views)
Why it matters: independently arrives at the versioning-is-part-of-trust argument — approval must be pinned to a version or it decays.

**SUNGLASSES | Agentic AI Security (@sunglasses_dev)**. Sep 4, 2026.
> "AI coding agents now consume packages, skills, context files and MCP servers at machine speed. A trusted registry proves which artifact arrived. It does not prove the text is safe for agent context. You need both checks."
https://x.com/sunglasses_dev/status/2095628886520590669 — [verified] (29 views)
Why it matters: sharp, correct distinction (provenance vs. content-safety) that a credible registry pitch needs to address head-on.

**Marwan Atef (@Marwan_3atef)**. Sep 4, 2026.
> "JFrog just shipped AgentSecOps so coding agents stop yoinking random skills/MCPs/plugins like it is 2015 npm. Artifactory gets an Agent Packages registry (APM), scans agent assets, and policy-gates which tools and deps an agent can pull."
https://x.com/Marwan_3atef/status/2095605159300608019 — [verified] (71 views)
Why it matters: direct competitive intel — JFrog Artifactory now has a governed agent-artifact registry product live.

**Mr. Anand (@Astrodevil_)**. Aug 3, 2026.
> "350k+ agent skills shipped in starting three months. None of them had proper governance. Same happened with MCP. Developers share MCP servers via git repos and zip files. No versioning. No scanning. No signing. It's the container supply chain chaos all over again."
https://x.com/Astrodevil_/status/2084249065622212618 — [verified] (408 views)
Why it matters: closest thing to a ready-made GTM pull-quote in the whole dataset — states the problem and the historical analogy (containers) unprompted.

**AppRater (@apprater)**. Sep 4, 2026.
> "SkillSecurity - Free static security scanner for AI Skills... Paste, upload, or link a SKILL.md file to detect prompt injection, credenti[als]..."
https://x.com/apprater/status/2095632549502435334 — [verified] (46 views)
Why it matters: yet another point solution (static scanner only, no registry/lifecycle) — competitive landscape is fragmenting into single-purpose tools, leaving the "full governed registry" position open.

**riba2534**, translated from Chinese. Sep 4, 2026.
> "This is an intricately disguised 'wallet draining trap (Wallet Drainer / malicious phishing),' so absolutely do not run any of the code it provides."
https://x.com/riba2534/status/2095590402556621045 — [verified] (1,726 views)
Why it matters: not skill-specific, but concrete evidence that "malicious repo disguised as agent tooling" is an active, circulating threat pattern in this exact community.

---

## B4 — COUNTER-EVIDENCE (a repo is enough / this is over-engineering)

Findings are thin here — this was hunted deliberately across 6 queries and mostly came back null or off-topic (see Null Results). The closest genuine counter-signals:

**Samyak Jain (@Sammy_970)**. Sep 5, 2026.
> "we now have AGENTS.md, CLAUDE.md, .cursor/rules, SKILL.md, and whatever Astra wants next. every agentic coding tool shipped its own config dialect in under a year. feels like 2015 CSS frameworks all over again."
https://x.com/Sammy_970/status/2096274143591502014 — [verified] (8 views)
Why it matters: frames the whole category as fragmentation/fad-cycling rather than a real infrastructure need — a skeptical framing a pitch has to defuse.

**Seth Fenster (@sethtjf)**. Sep 4, 2026.
> "I hate sprawl in my code bases and try to actively clean them up. I also like to keep my skills light bc it's easier to port and I find that I often need less of them with each new model interaction."
https://x.com/sethtjf/status/2095857577133240579 — [verified] (28 views)
Why it matters: an individual practitioner's actual solution to sprawl is discipline + fewer skills, not more tooling — a real "just be minimal" counter-practice, though it is a solo workflow, not a team one.

**Daily Dose of Data Science (@DailyDoseOfDS_)**. Aug 23, 2026.
> "A single CLAUDE.md file hit 200k+ GitHub stars. (derived from Karpathy's coding rules)"
(context tweet, quoting/paraphrasing; big account, 30K-view thread) — [verified]
Why it matters: shows a single plain-text file, no tooling at all, can get enormous organic reach/adoption — the lightweight/no-registry path has real gravity.

No one was found explicitly saying "a registry is overkill, git is enough" in as many words — six targeted queries ("just a git repo" skills, "don't need a registry", skills registry overkill, "a shared drive"/"a folder" ... enough, "just copy paste" skill.md, "would not run"/"wouldn't run" claude skill) returned null or off-topic results (logged below). Read charitably, this is weak evidence either way — it may mean the objection isn't being voiced on X in a findable form, not that it doesn't exist.

---

## B5 — SIGNAL SHAPE (who drives this conversation, reach, and what it implies for channel viability)

Ranked by verified view/engagement count on their most substantive on-topic post:

1. **eric provencher (@pvncher)** — Codex DX @OpenAI, 37.9K followers. "Rethinking skills and prompts for GPT-6 Astra": **1.5M views, 3.5K likes, 452 reposts, 80 replies**, posted 2026-09-05 (same day as this research). The single highest-signal artifact found: an OpenAI staffer's practitioner-grade teardown of skill sprawl went viral same-day. https://x.com/pvncher/status/2095991462416490862
2. **Nick Launches AI Agents (@nicklaunchesai)** — 95,110 views on the MCP/skills-registry-scale sprawl post. https://x.com/nicklaunchesai/status/2096131257407324642
3. **Mid-reach AI-influencer accounts** on SKILL.md-adjacent explainer content (@Flagvance 379 engagements, @AISystems_hq 381,772 views on "a skill is a folder with one file").
4. **Official brand accounts actively marketing into this exact space**: **@awscloud** (31,717 views, "Is AI agent sprawl the new technical debt?" launching AWS Agent Registry) and **@glean** (Glean AI Gateway, governed layer for skills/MCP/memories, via quote at https://x.com/tonygentilcore/status/2093093636066136465, 2,148 views on the amplifying quote-tweet). This is the strongest signal that enterprise-platform vendors already see this as a live, budget-worthy category.
5. **Named, credible infra people speaking organically (not marketing)**: Darren Shepherd (@ibuildthecloud, Rancher/Acorn co-founder) — 1,140 views; chetan conikee (@conikeec, shipped skillrecall) — 325 views; Patrick Debois (Tessl) referenced via @CoreyGallon — 139 views.
6. **Long tail of small builder/security accounts** (@stratamindlabs, @SilkNodeio, @sunglasses_dev, @apprater, @Marwan_3atef, @Astrodevil_, @DannielDevOps) each under 500 views but collectively converging, unprompted, on the same vocabulary: "intake gate," "supply chain," "no versioning, no scanning, no signing," "policy-gates."

Read: the loudest voices are (a) a small number of very-high-reach practitioner/insider accounts who occasionally post deep, on-topic essays that spike into hundreds of thousands of views, and (b) official accounts of large platforms (AWS, Glean, JFrog via commentary, NVIDIA via commentary) already shipping competing or adjacent governance products. The steady-state chatter is a long tail of low-reach (dozens to low-hundreds of views) builder and security accounts, in English, Japanese, and Chinese, independently reinventing the same vocabulary.

---

## Null / low-yield queries (logged as instructed)

- `"claude code" skills share` (f=live) — returned unrelated model-comparison/news content, nothing on team sharing.
- `AGENTS.md skills team` (f=live) — dominated by unrelated GPT-6 Astra launch commentary and an "AI Engineering Skills Map" (human skills, not SKILL.md files) from Andrew Ng — false-positive keyword match, excluded.
- `"my skills" claude code teammate` (f=live) — single loosely-relevant result (@sourfraser, "Claude + Skills = an AI employee for every job"), no teammate-handoff content.
- `"just a git repo" skills` (f=live) — 2 results, both off-topic (agent-OS and agent-readiness content, not the "git repo is enough" objection).
- `"over-engineering" skills claude` (f=live) — on-topic-adjacent but no direct counter-argument to a registry; mostly CLAUDE.md/skill-pack promo content.
- `"don't need a registry"` (f=live) — 100% off-topic (wedding registries, gun registries, parody accounts).
- `skills registry overkill` (f=live) — zero results.
- `"a shared drive" OR "a folder" claude skills enough` (f=live) — no on-topic hits.
- `"just copy paste" skill.md` (f=live) — 2 results, both unrelated (crypto guide, an agent card game).
- `"would not run" OR "wouldn't run" claude skill` (f=live) — zero results.
- `"internal skill library"` (f=live) — zero results.
- `"our skills" claude code` (f=live) — mostly GTM/agency case studies, nothing on internal skill libraries specifically.
- `"shared this skill" OR "gave my team" claude` (f=live) — 100% off-topic (unrelated personal/lifestyle tweets from years prior; keyword collision).

---

## Channel-viability read

X surfaces this conversation daily, in real practitioner language, and at least one OpenAI staffer and several infra-credible independents post about it organically with real reach (1.5M and 95K view posts this week alone). But it is also visibly becoming a vendor battleground — AWS, Glean, JFrog, and NVIDIA are already marketing competing or adjacent products into the same feed. Grassroots demand is real but diffuse (dozens of small accounts, tens to low-hundreds of views each); the reach is concentrated in a handful of high-follower insiders, not a movement with many mid-tier voices — so X is viable for finding interview subjects and validating language, but the audience for a paid-acquisition push is thin and increasingly noisy with competitor messaging.
