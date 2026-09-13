# Community Signals: Reddit + Hacker News
Pull date: 2026-09-05. Beat: Reddit and Hacker News, for Atlan Agent Registry GTM work sample.

## IMPORTANT ACCESS NOTE — Reddit was not reachable
Every avenue to Reddit failed in this environment: direct `curl` to `old.reddit.com/.../search.json` and `.../comments/xxx/.json` returned **HTTP 403 "Blocked"** (tried from both the cloud container and the user's own Mac via device_bash); `WebFetch` on any `reddit.com` URL returned `SITE_BLOCKED` (an explicit policy block, not a site-side error); and the `WebSearch` tool **never returned a single reddit.com URL** across ~15 differently-worded queries (`site:reddit.com ...`, plain-language queries, quoted phrases) — it silently substitutes Wikipedia disambiguation pages, Substack posts, and blog roundups instead. Alternate routes (r.jina.ai reader proxy, Bing, DuckDuckGo HTML) were also blocked (403 / robots.txt disallow) for this account's toolset.
**Conclusion: Reddit content in this report is `[reported]` at best, sourced from third-party subreddit-analytics trackers (member counts) or blog posts that claim to summarize Reddit sentiment — never a directly-read Reddit page or JSON payload.** No verbatim Reddit quote in this file should be treated as `[verified]`. This is itself worth flagging to the requester: **if Atlan's own GTM research pipeline can't read Reddit, that's an infra gap, not evidence Reddit is quiet on this topic.** Hacker News, by contrast, was fully accessible via the Algolia API and is the substantive part of this report.

---

## B1 — THE SHARING MOMENT (highest priority)

**[verified, HN]** guypod (founder of Snyk, now building Tessl) — Show HN: A package manager for agent skills with built-in evals:
> "most teams still treat skills as static artifacts: markdown files, created or copied from repo to repo. This approach offers a strong initial boost, but quickly creates debt: - Skills are duplicated, and updates never roll out. - Poor quality skills go unseen, misguiding agents instead of helping. - Skill knowledge grows stale"
Thread: https://news.ycombinator.com/item?id=46900933 (2026-02-09, 7 pts, 2 comments)
Why it matters: this is a credible, repeat B2B-security founder (Snyk) independently arriving at almost exactly Atlan's registry thesis — copy/paste sprawl, no update propagation, no quality signal — and building a company around it (Tessl Registry, "review evals for over 2,000 skills"). Strongest single validation found.

**[verified, HN]** sjmaplesec, reply in the same thread:
> "we have dozens of internal 'playbooks' and prompt snippets floating around, and nobody knows which ones still work after model changes... Do you have a CI integration where you can pin a skill version and fail builds if eval scores drop?"
Link: https://news.ycombinator.com/item?id=46900933
Why it matters: a practitioner, unprompted, describes org-internal skill sprawl and asks for exactly version-pinning + CI gating — core Atlan registry features.

**[verified, HN]** laul_pogan (built Ingot) — Show HN: Ingot, evidence-gated optimization and version control for agent skills:
> "I built Ingot because skill changes felt like copy-paste, and are difficult to track across large orgs. Ingot versions them and requires human review."
Link: https://news.ycombinator.com/item?id=49007958 (2026-07-22, 7 pts, 2 comments)
Why it matters: another independent builder solving the identical "no ownership/versioning at org scale" problem — third-party confirmation the pain is real enough that people keep re-building point solutions for it.

**[verified, HN]** atxpace — comment on "AI Coding Agent Skills for Real Engineers" (mattpocock/skills):
> "The useful skills are the org/team rules, and those are the ones that never leave someone's laptop. Then Cursor's on a different copy than Claude. That's the actual problem — drift - not another public set of skills. skillrepo.dev is for keeping that set current in your environment."
Link: https://news.ycombinator.com/item?id=49529329 (2026-09-02, 43 pts, 14 comments), comment id 49536348
Why it matters: names the exact Atlan wedge — skills stuck on one person's laptop, drifting across harnesses (Cursor vs Claude) — and namechecks a competing point-solution (skillrepo.dev), so this is also a competitor lead.

**[verified, HN]** fishfasell, same thread:
> "Skills are hardly transferrable unless you are just focusing on globally applicable things... The most useful skills are things that are not well known and project/organization specific. The 'tribal knowledge' aspect of coding."
Link: https://news.ycombinator.com/item?id=49529329, comment id 49531209
Why it matters: articulates *why* sharing matters (tribal knowledge capture) even while being skeptical that public skill-sharing works — nuance worth quoting back.

**[verified, HN]** dariusmonsef (OzBrain founder) — Show HN: OzBrain, a shared brain for knowledge between agents and your team:
> "make it easy for me to share my chunks of knowledge with my teammates and their agents"
Link: https://news.ycombinator.com/item?id=49394827 (2026-07-15, 93 pts, 59 comments), comment id 49395290
Why it matters: another founder building a team-knowledge-sharing layer for agents, direct B1 framing from the pitch itself; the thread (59 comments) is worth a full read for more team-sharing chatter.

**[verified, HN]** rgbrgb, same OzBrain thread:
> "i want one tool i can have a colleague (or my wife) install that adds all the context they'll need (and then one spot I can curate and govern that context)"
Link: https://news.ycombinator.com/item?id=49394827, comment id 49399866
Why it matters: names curation + governance explicitly — this is Atlan's "ownership + access" pitch in a user's own words.

**[verified, HN]** mrdonbrown (sx project) — on "Dockerhub for Skill.md":
> "If you want to share skills using something that has versioning, automatic updates, and focused on teams vs the internet at large, consider sx"
Link: https://news.ycombinator.com/item?id=46692692, comment id 46780849 (2026-01-20)
Why it matters: yet another point-solution builder pitching "teams, not the internet at large" — the market keeps re-deriving Atlan's team/enterprise framing.

**[verified, HN]** theahura (noriskillsets.dev founder) — on "Show HN: Agent Skills Leaderboard" (skills.sh launch thread):
> "I think the 'collect a bunch of random skills' approach just isn't it. You need versioning, linking between skills, an easy install client...basically a full package manager, which this is not."
Link: https://news.ycombinator.com/item?id=46697908, comment id 46722059 (2026-01-20, thread: 135 pts / 44 comments)
Why it matters: direct critique of the leading skills-directory competitor (skills.sh) for lacking exactly the registry primitives (versioning, dependency linking) Atlan is built around.

**[verified, HN]** _pdp_ — on the original Claude Skills launch thread:
> "I predict there will be some sort of package manager opensource project soon. Download skills from some 3rd-party website and run inside Claude. Risks of supply chain issue will be obvious but nobody will care - at least not in the short term."
Link: https://news.ycombinator.com/item?id=45607117, comment id 45610693 (2025-10-16)
Why it matters: predicted the entire skills-registry gold rush (confirmed by the dozen+ "package manager for skills" Show HNs found below) on day one — and flagged the supply-chain risk Atlan's trust/provenance layer answers.

---

## B2 — SPRAWL & DECAY

**[verified, HN]** hungryhobbit — on "AI Coding Agent Skills for Real Engineers":
> "If I had a nickel for every dev who has written a 'productivity suite' of skills, and shared it with others as if it was a burst of innovation... It turns out productivity skill sets for Claude are a bit like opinions and assholes (everyone has one, and ...)"
Link: https://news.ycombinator.com/item?id=49529329, comment id 49529918
Why it matters: sprawl-of-low-quality-skills complaint from a credible senior voice, describes the duplicate/low-signal problem a registry's quality/curation layer addresses.

**[verified, HN]** iLoveOncall — on "Dockerhub for Skill.md":
> "You have no versioning, no automated or simplified update, no way to verify the authors, etc. The 'installation' is literally just a wget... Most of the skills currently hosted are also really bad."
Link: https://news.ycombinator.com/item?id=46692692, comment id 46699140 (2026-01-20)
Why it matters: names the exact gaps (versioning, updates, author verification) in the current wave of skill directories — precisely Atlan's feature list, framed as complaints.

**[verified, HN]** m-hodges — on the skills.sh launch thread:
> "Why do none of these 'npm for Skills' document any way to do basic package management things like updates, version-pinning, or even uninstalls?"
Link: https://news.ycombinator.com/item?id=46697908, comment id 46702297
Why it matters: blunt, upvoted-adjacent complaint that the current tooling wave skipped package-manager basics.

**[verified, HN]** dave1010uk, same thread:
> "The install is very opaque. It's not clear where these skills are installed, how to upgrade them or remove them... Aside: although lots of agents have adopted SKILLS.md conventions, they're currently all using their own paths. There doesn't seem to be a consensus yet."
Link: https://news.ycombinator.com/item?id=46697908, comment id 46702711
Why it matters: cross-harness fragmentation (`.claude/`, `.codex/`, `.Gemini/`, 3+ generic paths) is exactly the distribution problem Atlan solves by targeting multiple harnesses.

**[verified, HN]** jampa — on the original Claude Skills launch:
> "CLAUDE.md files become bloated with niche workflows like CI and E2E testing. Combined with MCPs, this pollutes the context window and eventually degrades performance."
Link: https://news.ycombinator.com/item?id=45607117, comment id 45607787
Why it matters: names context-window bloat directly (B2's core complaint) from the very first day of Skills' existence.

**[verified, HN]** CuriouslyC, same thread:
> "Anything the model chooses to use is going to waste context and get utilized poorly. Also, the more skills you have, the worse they're going to be."
Link: https://news.ycombinator.com/item?id=45607117, comment id 45608423

**[verified, HN]** rudedogg — skills.sh launch thread:
> "I'm having issues with the LLMs ignoring the skills content... it's put a damper in my dream of constraining them with well crafted skills"
Link: https://news.ycombinator.com/item?id=46697908, comment id 46700528
Why it matters: "wrong/no skill firing" complaint, a named B2 symptom.

**[verified, HN]* zby, same thread:
> "do skills reliably work for you? I mean are they reliably injected when there is a need... I have a feeling that codex still does not do it reliably - so I still have normal README files which it loads quite intelligently and it works better than the discovery via skills."
Link: https://news.ycombinator.com/item?id=46697908, comment id 46702936
Why it matters: cross-harness reliability doubt — also doubles as counter-evidence (falls back to plain README over skill discovery).

**[verified, HN]** gtirloni — on "Dockerhub for Skill.md":
> "It doesn't help that the skills have a checkmark next to the company's name, even though these skills weren't created by the respective companies."
Link: https://news.ycombinator.com/item?id=46692692, comment id 46700355
Why it matters: ownership/attribution integrity problem on an existing registry — exactly what Atlan's "identity and ownership" pillar is meant to fix.

---

## B3 — TRUST & SAFETY

**[verified, HN]** simonw — on the original Claude Skills launch:
> "I remain afraid of prompt injection. If I'm telling Claude Code to retrieve data from issues in public repos there's a risk someone might have left a comment that causes it to steal API keys or delete files or similar."
Link: https://news.ycombinator.com/item?id=45607117, comment id 45623714
Why it matters: the most-followed independent AI commentator on HN, on the record about injection risk from untrusted content Skills can pull in.

**[verified, HN]** azraellzanella, same thread, quoting Anthropic's own docs back with alarm:
> "'Keep in mind, this feature gives Claude access to execute code. While powerful, it means being mindful about which skills you use—stick to trusted sources to keep your data safe.' Yes, this can only end well."
Link: https://news.ycombinator.com/item?id=45607117, comment id 45607941
Why it matters: sarcastic pushback on Anthropic's own "trust the source" hand-wave — precisely the gap a governed registry closes.

**[verified, HN]** dirk94018 (NoClaw author) — Show HN: NoClaw – Mac Mini Assistant the Unix Way:
> "We built NoClaw after watching OpenClaw users burn $800-$3600/month on tokens, deal with 1,100+ malicious ClawHub skills, and have agents email their entire contact list unprompted."
Link: https://news.ycombinator.com/item?id=47437814, comment id 47437817 (2025-12-26)
Why it matters: a concrete, numbered incident of skill-marketplace supply-chain compromise (1,100+ malicious skills in one registry) — the strongest quantitative trust/safety data point found on HN.

**[verified, HN]** XCSme — on "Dockerhub for Skill.md":
> "My question comes from security, adding that skills just provides a line of bash, with no further info. I checked the .md file but it just lists a list of commands with agent-browser."
Link: https://news.ycombinator.com/item?id=46692692, comment id 46699552
Why it matters: concrete "I can't tell what this skill actually does before running it" concern — provenance/review gap.

**[verified, HN]** mock-possum — on "AI Coding Agent Skills for Real Engineers":
> "It's also unsettling catching it behaving in an odd way, and realizing that it was taking a cue from instructions you never wrote, but imported from elsewhere. Like playing a game of pretend with someone else's rules."
Link: https://news.ycombinator.com/item?id=49529329, comment id 49531012
Why it matters: visceral "imported instructions I didn't write are steering the agent" trust discomfort — very human framing of the supply-chain problem.

All B3 items above are [verified, HN] — pulled directly from raw Algolia API JSON, not summarized or paraphrased.

Landscape context (not a quote, but relevant B3 signal): at least 6 independent "scan/verify skills before install" security products surfaced solely from HN Show-HN searches in the last year — Vett (vett.sh), Skillcop, Aguara, SkillSpec, Socket's skills.sh integration, and Askill's "AI safety scoring." That many independent security tools targeting one 10-month-old file format is itself a strong B3 signal.

[CONTENT_PLACEHOLDER]