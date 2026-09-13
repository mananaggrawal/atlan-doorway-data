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

[CONTENT_PLACEHOLDER]