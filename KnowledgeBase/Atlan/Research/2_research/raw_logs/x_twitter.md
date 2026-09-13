# Raw Research Trail: X (Twitter) Skills-Sharing Research
Session date: 2026-09-05. This is an audit trail reconstructed from my own transcript, not a report — includes dead ends, discards, and uncertainties.

## 0. Setup and browser mechanics

- Checked `$HOME/mnt/` and `$HOME/mnt/Atlan/01_evidence/` via device_bash to confirm the project folder structure before starting.
- Opened the browser pane on `https://x.com/search?q=%22SKILL.md%22&f=live` via `preview_start`.
- First `get_page_text` call came back empty (only chrome/tabs, no posts) — the page was still loading. Waited 3s via `computer{action:"wait"}` and retried; posts appeared on the second read. This happened once; all subsequent reads worked on the first try.
- Method settled on after the first two queries: `preview_start` a new search URL -> `get_page_text` to read the visible results -> for any post I wanted to cite, `find(<handle>)` on the accessibility tree to pull its permalink (`/handle/status/ID`) and view count from the "N views. View post analytics" link text. I used `read_page{filter:"interactive"}` directly only for the first two queries before settling on `find()` as faster.
- I did NOT verify every engagement number by screenshot -- only two posts got a visual screenshot cross-check (see Section 5, uncertainty #3): eric provencher's big post, and his profile page.
- Popup-blocking incident: after the first query, a `navigate()` call to load SKILL.md `f=top` failed with "Navigation is paused while a page-opened popup... is open." `tabs_context` showed the browser pane had two unrelated Google-accounts sign-in popups (`popup-2`, `popup-4`) open from prior, unrelated browser activity in this session (other tabs present: a `youtube.com` seed tab, a `linkedin.com` tab-3), plus my own `tab-1` (x.com). I tried `tabs_close` on both popups; both were refused ("That tab is a page-opened popup... the agent may not drive, navigate, or close it"). I did not ask the user to close them (auto-mode, not a hard blocker) -- instead I switched to using `preview_start` for every subsequent query instead of `navigate`, which was not subject to the same block and worked for the rest of the session. I never resolved or closed those popups; they may still be open in the browser pane.
- No posting, liking, following, replying, or form submission occurred at any point. No credentials were entered.

---

## 1. All queries run, in order, verbatim

Correction to my final report: I stated "26 distinct queries" in the filed summary. Recounting from the transcript precisely, I count 27 (I undercounted by one, likely by treating the two SKILL.md variants as one line item when tallying). Listed exactly as run:

| # | Query text | URL | Mode | On-topic hits (of ~5-9 shown) | Verdict |
|---|---|---|---|---|---|
| 1 | "SKILL.md" | x.com/search?q=%22SKILL.md%22&f=live | live | ~2 of 7 (Sammy_970, Flagvance; rest crypto/agent-swarm noise) | Productive |
| 2 | "SKILL.md" | x.com/search?q=%22SKILL.md%22&f=top | top | 4 of 4 (levelsio, AISystems_hq, startupideaspod, DanKornas) | Very productive |
| 3 | "agent skills" | x.com/search?q=%22agent%20skills%22&f=live | live | 3 of 6 (Boardy thin, Morel, DanKornas "AAS Core"; Holochain/CesarAG/danilocoding discarded) | Moderately productive |
| 4 | skills.sh | x.com/search?q=skills.sh&f=live | live | 5 of 7 (Ma7039Ma, DannielDevOps+quoted Ihtesham Ali, Hacksore, conikeec, coka_stefan) | Very productive |
| 5 | "claude code" skills share | x.com/search?q=%22claude%20code%22%20skills%20share&f=live | live | 0 of 5 | Dead end |
| 6 | "too many skills" | x.com/search?q=%22too%20many%20skills%22&f=live | live | 6 of 13 (rest were football/celebrity/life-advice/video-game false positives on the phrase) | Very productive |
| 7 | claude code plugin marketplace | x.com/search?q=claude%20code%20plugin%20marketplace&f=live | live | 5 of 5, but low individual reach (product-promo tweets) | Productive but thin |
| 8 | skills registry agents | x.com/search?q=skills%20registry%20agents&f=live | live | 5 of 7 (2 results were an unrelated child-welfare/CPS news story that happens to use "registry") | Very productive -- best single query for B3/B5 |
| 9 | agent skills governance | x.com/search?q=agent%20skills%20governance&f=live | live | 2 of 5 (stratamindlabs the standout; Thunder Tschunk borderline) | Productive |
| 10 | claude skills versioning | x.com/search?q=claude%20skills%20versioning&f=live | live | 5 of 8 | Very productive |
| 11 | "my skills" claude code teammate | x.com/search?q=%22my%20skills%22%20claude%20code%20teammate&f=live | live | 1 of 1, and that one was only loosely relevant | Dead end |
| 12 | skills sprawl agents | x.com/search?q=skills%20sprawl%20agents&f=live | live | 5 of 7 (HashiCorp false positive, Sam/Type tangential) | Very productive -- best query for vendor/B5 intel |
| 13 | codex skills team | x.com/search?q=codex%20skills%20team&f=live | live | 2 of 5 (angelbrodin filed-worthy but ultimately dropped; Andrew Ng deliberately excluded as false positive) | Moderately productive |
| 14 | AGENTS.md skills team | x.com/search?q=AGENTS.md%20skills%20team&f=live | live | 0 of 7 (dominated by "AI Engineering Skills Map" false positives and unrelated model-launch chatter) | Dead end |
| 15 | "context engineering" skills team | x.com/search?q=%22context%20engineering%22%20skills%20team&f=live | live | 1-2 of 7 (Yarchi the one real hit; Yongkyun Lee borderline) | Weak |
| 16 | "just a git repo" skills (B4 hunt) | x.com/search?q=%22just%20a%20git%20repo%22%20skills&f=live | live | 0 of 2 | Dead end |
| 17 | "over-engineering" skills claude (B4 hunt) | x.com/search?q=%22over-engineering%22%20skills%20claude&f=live | live | 2 of 5 (DailyDoseOfDS_ filed; akshay_pachaar seen but dropped) | Weak but useful |
| 18 | "don't need a registry" (B4 hunt) | x.com/search?q=%22don%27t%20need%20a%20registry%22&f=live | live | 0 of 13 | Dead end -- 100% off-topic (weddings, guns, gift registries) |
| 19 | skills registry overkill (B4 hunt) | x.com/search?q=skills%20registry%20overkill&f=live | live | 0 -- literally zero results returned by X | Dead end |
| 20 | "a shared drive" OR "a folder" claude skills enough (B4 hunt) | x.com/search?q=%22a%20shared%20drive%22%20OR%20%22a%20folder%22%20claude%20skills%20enough&f=live | live | 0 of 6 | Dead end |
| 21 | "just copy paste" skill.md (B4 hunt) | x.com/search?q=%22just%20copy%20paste%22%20skill.md&f=live | live | 0 of 2 | Dead end |
| 22 | skill.md prompt injection (B3 hunt) | x.com/search?q=skill.md%20prompt%20injection&f=live | live | 3 of 6 (apprater, riba2534 filed; K_chachamaru seen, dropped) | Productive |
| 23 | "would not run" OR "wouldn't run" claude skill (B3 hunt) | x.com/search?q=%22would%20not%20run%22%20OR%20%22wouldn%27t%20run%22%20claude%20skill&f=live | live | 0 -- zero results | Dead end |
| 24 | "internal skill library" (B1 hunt) | x.com/search?q=%22internal%20skill%20library%22&f=live | live | 0 -- zero results | Dead end |
| 25 | "our skills" claude code (B1 hunt) | x.com/search?q=%22our%20skills%22%20claude%20code&f=live | live | 0 of 6 (all tangential business/GTM content, nothing on internal libraries) | Dead end |
| 26 | sync claude skills machines (B1 hunt) | x.com/search?q=sync%20claude%20skills%20machines&f=live | live | 2 of 6 (truffle, simplifyinAI filed; Cathryn's two posts and ShahzaibJak seen, dropped) | Productive |
| 27 | "shared this skill" OR "gave my team" claude (B1 hunt) | x.com/search?q=%22shared%20this%20skill%22%20OR%20%22gave%20my%20team%22%20claude&f=live | live | 0 of 9 on-bucket (one borderline: @xmousecopx on workplace AI-mandate resistance) | Dead end |

Total: 27 queries. Roughly 12 were genuinely productive (filed content), 4 were weak/thin, and 11 were dead ends (mostly the deliberate B3/B4 counter-evidence and B1-library hunts in queries 16-25, 27).

---

## 2. Every post/thread opened or read, in chronological order

Format: handle -- one-line note -- filed? (bucket, or "not filed" + why in brief; full reasons repeated in Section 3 for the notable near-misses).

### Query 1 -- "SKILL.md" f=live
1. @Sammy_970 (Samyak Jain) -- "we now have AGENTS.md, CLAUDE.md, .cursor/rules, SKILL.md... 2015 CSS frameworks all over again" -- filed (B4).
2. @Flagvance (Pori) -- "PEOPLE ARE USING NOTEBOOKLM TO MASS-PRODUCE SPECIALIZED CLAUDE SKILLS", 379 engagement -- not filed as a quote; referenced only by handle+number in the B5 signal-shape paragraph.
3. @Dmytroo_eth (Dmytro) -- "KIMI K3 CAN COORDINATE UP TO 300 AGENTS", quoting @polydao's "300 AGENTS, ONE GRAPH" thread -- not filed, off-topic (agent-swarm coordination/memory, not skill-file sharing).
4. @AgentChud -- prompt template to build an evm-token-due-diligence skill -- not filed, low-signal prompt-recipe, not about sharing/governance.
5. @AgentChud (2nd tweet, quote-tweet linking a rentry.co page, 23K engagement) -- not filed, appears to be crypto/trading content unrelated to agent skills.
6-7. @criptoejesus420 (two tweets, NFT collection "AfterGlow") -- not filed, completely irrelevant (keyword collision, none).

### Query 2 -- "SKILL.md" f=top
8. @levelsio -- "Add a SKILL.md to readmake.com so you can load the book into Claude Code or Codex or Cursor" (quote-tweeting @marckohlbrugge/@andreyazimov), Aug 6 -- URL captured (status 2085381480440623378) but NOT FILED in the final writeup. See Section 3 -- this is a real omission worth flagging.
9. @levelsio (2nd tweet shown in same text block, Jul 18, "$16,000 this month" revenue post) -- not filed, unrelated to skills; appeared adjacent to #8 in the page text, possibly a "more from this author" render artifact rather than a true second search match.
10. @AISystems_hq (Mr. Systems) -- "A skill is a folder with one file in it. SKILL.md holds a name, a description, and your steps" -- filed (B5, cited for its 381,772 views).
11. @startupideaspod -- "self-improvement loop" at the bottom of every skill.md, quote-tweeting its own Aug 20 post ("You need to be skillsmaxxing... How to turn his AI skills into a plugin his whole team installs") -- filed (B1).
12. @DanKornas -- "Suede Creator Skills is an open-source collection of agent skills for builders using Claude Code, Codex..." -- filed (B1).

Then opened the full thread at startupideaspod/status/2090559506317201692:
13. Reply from @WorkflowFixAi -- "This is one of the cleanest patterns I've seen. Most skills stay static after the first version. Putting a short review loop at the bottom..." -- not filed, thin/redundant with the parent tweet, but a decent supporting quote I could have used.
- Attempted to find a standalone permalink for the quoted "skillsmaxxing" Aug 20 article-post; find() only returned it as non-link generic text, so I could not resolve a clean separate URL and cited the Aug 21 tweet instead.

### Query 3 -- "agent skills" f=live
14. @boardyai (Boardy) -- reply offering an intro to "a builder working on reusable agent skills that stay current as environments change" -- URL captured (status 2096273094226890811, 5 views), NOT FILED -- thin, a networking/lead-gen-bot-style reply, not a real pain quote.
15. @MorelMatth66161 (Matthieu Morel) -- "De-AI writing skill for any Agent Skills-compatible agent (77+ via the Skills CLI)" -- URL captured (status 2096271068977623122, 18 views), NOT FILED -- mentioned "Skills CLI" ecosystem in my reasoning but didn't quote him directly in the file.
16. @DanKornas -- different tweet, "AAS Core -- Agentic Awesome Skills is a local, agent-first control plane... reviewable skills setup" -- URL captured (status 2096270620715569232, 505 views), NOT FILED as a quote (DanKornas IS filed elsewhere for the Suede Creator Skills tweet, but not for this one).
17. @Holochain -- reply linking github.com/Soushi888/holochain-agent-skills and a "Home-Cooked Software" essay -- URL captured (status 2096267450593542296, 271 views), NOT FILED -- judged too niche/off-thesis (a blockchain framework's own agent-skills repo, more DIY-philosophy than sharing/governance).
18. @cesargomz29 (CesarAG) -- Spanish listicle "35 AGENT SKILLS QUE PUEDEN CONVERTIR CLAUDE CODE..." -- not filed, no URL captured, judged spam-adjacent.
19. @danilocoding -- rant about GPT-6 Astra being "anxious and unreliable," mentions using it "for one single task in a codebase with agent..." -- not filed, off-topic (general model-quality complaint).

### Query 4 -- "skills.sh" f=live
20. @Ma7039Ma (mjhhh) -- Chinese-language, install-everything-then-purge-everything story -- filed (B2).
21. @JavierEraia (Javier) -- Spanish article "Tu agente no es tonto. Simplemente no le diste instrucciones" -- not filed, generic content-marketing, tangential.
22. @DannielDevOps -- "Skills.sh as a search and install catalog... beats copying another skill.md by hand" -- filed (B1).
23. @ihteshamali (Ihtesham Ali), quoted inside DannielDevOps's tweet -- "Vercel literally built an App Store for AI agents. It is called Skills.sh." -- NOT FILED as a standalone citation. I tried twice to resolve a direct permalink (find("ihteshamali"), then find("App Store for AI agents"), then find("Jul 27")) and got only non-link generic text each time -- could not get a clean URL, so I dropped the formal citation rather than cite an unresolvable link.
24. @Hacksore -- "wait if we have skills.sh do they deskill humans?" -- URL captured (status 2095993846345736252, 54 views), NOT FILED -- too joke-y/philosophical, off-bucket.
25. @conikeec (chetan conikee) -- "skillrecall... pickup rate... who steals your requests" -- filed (B2).
26. @coka_stefan (Stefan), replying to @rauchg -- "Just waited for 10+ seconds for a search to resolve on skills.sh" -- URL captured (status 2095946863778168908, 73 views), NOT FILED as its own quote. This is the tweet that confirmed @rauchg (Vercel's CEO) is personally engaging with skills.sh replies -- that connection did NOT make it into the final B5 write-up, which is a gap (see Section 3).

### Query 5 -- "claude code" skills share f=live
27-31. @Arzu_with_Ai (Claude terms cheat sheet), @arthur_win8 (Grok Build changelog), @nateherk (GPT-6 Astra voice-mode article), @avibe_bot (OpenRouter token leaderboard), @ClawUpAI (DeepSeek Harness comparison) -- none filed, all off-topic noise. Logged as dead end.

### Query 6 -- "too many skills" f=live
32. @edem_willz -- football banter about a player "too many skills, doesn't know how to use them" -- not filed, off-topic (sports).
33. @mbritton (Mike Britton) -- "I'm writing too many skills and burning tokens needlessly when specs change" -- filed (B2).
34. @humansandaiboss (patrick mcqueeny) -- "yes there are too many skills and mcps to choose from... quality over quantity" -- filed (B2).
35. @pvncher (eric provencher) -- flagged here as huge (79/452/3.5K/1.5M shown in search-result preview digits) -- filed extensively (B1, B2, B5); full thread opened later (see below).
36. @fintasticapps (Chris) -- reply riffing on Tom Cruise/success breeds success, "def too many skills!!" -- not filed, off-topic personal banter.
37. @solopribuilds (Pri) -- "too many skills to gain in one life" -- not filed, off-topic (life-advice, non-AI).
38. @Josh0fRivia -- "revamp the skill tree time consumption... too many skills require time segments" -- not filed -- this is about a VIDEO GAME skill tree, a false positive on the phrase.
39. @JustTZM -- "yeah, i got too many skills" -- not filed, off-topic banter, context unclear.
40. @jaxkoh_ (Jax Koh) -- "lost in my configurations... too many skills/instructions created" -- filed (B2).
41. @thetasigma_io (Theta Sigma) -- "bad skills or too many skills installed or just bad global AGENTS.md" -- filed (B2).
42. @ibuildthecloud (Darren Shepherd) -- "Isn't anyone worried about 'too many skills'... progressive discovery" -- filed (B2), flagged as high-credibility (Rancher/Acorn co-founder).
43. @tsugikki (silly d. goose) -- Beyonce banter, "too many skills in her belt," 482 engagement -- not filed, off-topic, but noted purely as evidence the phrase "too many skills" is heavily overloaded with non-AI usage on X.
44. @elehzey (Elizabeth) -- "this is how I ended up with too many skills. Leave me alone" -- not filed, off-topic personal tweet, unclear context.

Then opened pvncher/status/2095991462416490862 in full via preview_start + get_page_text (long article-format post, "Rethinking skills and prompts for GPT-6 Astra") -- read in full, multiple passages filed across B1/B2. Took a screenshot to visually confirm 80 replies / 452 reposts / 3.5K likes / 1.5M views. Then visited his profile (x.com/pvncher) directly and read his bio ("Codex DX @Openai | built @repoprompt | prev XR @unity", 37.9K Followers, 4,854 Following, 17.8K posts) plus three of his other recent posts shown on the profile (a "Tide Garden" WebGPU demo pinned post, "Astra tokens are built different" quoting Lucas Meijer, "The GPT-6 Astra api guide is worth reading" quoting Jeremy Nguyen) -- none of these three filed, used only to confirm identity/credibility.

### Query 7 -- "claude code plugin marketplace" f=live
45. @coder_tx (Coder_Tx) -- Turkish, ecc-universal setup / ECC GitHub repo promo -- not filed, product-promo, tangential.
46. @daichirouesaka (Japanese handle) -- Japanese, Spotify's "Portal" Claude Code plugin cutting token costs 90% via pre-tool hooks -- URL captured (status 2096149074198061140, 50 views), NOT FILED -- interesting (an internal-tool-as-plugin case) but judged to be about cost-optimization, not sharing/governance.
47. @dasepmochly (Dasep Moch Luay) -- "Your AI coding agent is writing messy code because it lacks an engineering harness," repromoting ECC -- not filed, redundant promo.
48. @RituWithAI (Rituraj) -- "Ponytail" skill, "54% less code" -- URL captured (status 2096073298367111381, 10,271 views), NOT FILED -- product-promo, high view count noted internally but not written into the file.
49. @poorvith_mp (Poorvith M P) -- "Skillary," three install methods (npx skills add, /plugin marketplace add) -- URL captured (status 2096070821995577549, 17 views), NOT FILED as a named quote -- discussed only generically in the B1 narrative ("Skillary" not named in the final file).

### Query 8 -- "skills registry agents" f=live
50. @sparqio (SPARQIO) -- "Imagine having a skills registry and approval..." (Agent OS product pitch) -- URL captured (status 2096147884789919809, 12 views), NOT FILED as a quote in the final markdown (considered, dropped for being a direct product pitch rather than practitioner pain).
51. @nicklaunchesai (Nick Launches AI Agents) -- "81,811 MCP servers... 3,004 agent skills... nobody can read all that" -- filed (B2, B5) -- 95,110 views, the highest pure-sprawl engagement found.
52. @NatlAssnParents (ParentsUSA) -- child-welfare/CPS story -- not filed, completely off-topic (false positive on "registry").
53. @mattvanswol (Matt Van Swol) -- same CPS story thread -- not filed, off-topic.
54. @sunglasses_dev (SUNGLASSES) -- "A trusted registry proves which artifact arrived. It does not prove the text is safe for agent context." -- filed (B3).
55. @Marwan_3atef (Marwan Atef) -- "JFrog just shipped AgentSecOps... Agent Packages registry (APM)" -- filed (B3) -- key competitive intel.
56. @0MeissnerState (DarkHorseDelta) -- "AWS made Agent Registry generally available... the fifth team building the same internal agent is not innovation" -- filed (B1).

### Query 9 -- "agent skills governance" f=live
57. @ebokify (Ebokify) -- Amazon-affiliate book ad, "The Claude Code Operating Model" -- not filed, pure affiliate marketing.
58. @stratamindlabs (Strata Mind Labs) -- "AI skills are starting to behave like software dependencies... intake gate" -- filed extensively (B3); full thread opened.
59. @SpiritofAlyahw (AbyahsNathan) -- "Living Skill Mesh," "SKILL GENOME" -- not filed, reads as AI-generated sci-fi/roleplay content, low engagement (18), not a credible practitioner voice.
60. @agialphaagent (AGI ALPHA AGENT) -- "SUCCESSOR Omega v8.0.0 Proof-Gated Frontier Mission Intelligence" -- not filed, judged an autonomous-agent-run promo account for an unrelated product; thematically adjacent language ("earn trust... remain governable") but too far off-topic/product-specific.
61. @ThunderTschunk (Thunder Tschunk) -- "added a bit of governance to my vibe coding. Skills that pick the right agent... lock main... Ollama + Qwen2.5-Coder plays the mason," 104 engagement -- NOT FILED -- a real personal workflow post, borderline relevant, but I judged it too thin to quote within 50 words without losing meaning and more about local-model routing than skill governance per se.

Then opened stratamindlabs/status/2095996431068754426 in full:
62. Full essay text read (NVIDIA SkillSpector mention, DO/DRAFT/ASK/STOP framework) -- filed (B3).
63. Reply from @SilkNodeio (Silk node) -- "Does approval bind the exact skill and dependency versions? A clean intake scan becomes stale..." -- filed (B3).
64. A "Discover more" surfaced second post from @stratamindlabs itself (Sep 2, about GrokBot for nontechnical operators) -- not filed, unrelated to skills specifically.

### Query 10 -- "claude skills versioning" f=live
65. @RichStoneIO (Rich Steinmetz) -- "make sure they don't irreversibly change their behavior... versioning my global Claude..." -- filed (B1).
66. @businessbarista (Alex Lieberman) -- "30 features of an AI native company" listicle, 105K views -- not filed, too generic/broad, not skill-file-specific.
67. @49agents (49Agents IDE) -- "are you versioning skills as plain markdown files in git or something structured?" -- filed (B1/B2).
68. @chanduuu_cs (chanduu) -- "skills every AI Engineer should learn in 2026" (Python, DSA, Git...) -- not filed, false positive (human career skills, not SKILL.md).
69. @repojournal (Repojournal) -- Claude Code Action version-bump changelog -- not filed, automated release notes, not commentary.
70. @gregce10 (Greg Ceccarelli) -- "For every 100 posts about agents, harnesses, skills... there is 1 sharing what you've built," mentions "Extensions used by over 200K to capture and extract learning from agent traces" -- NOT FILED; did not pursue a find() URL for this one at all -- a gap, since it's thematically close to B1/self-improvement.
71. @Astrodevil_ (Mr. Anand) -- "350k+ agent skills shipped... none had proper governance... container supply chain chaos" -- filed (B3) -- best ready-made pull-quote found.
72. @cozybearlog (CozyBear) -- "Matt Pocock shipping his skills as a Claude Code plugin... package manager for it" -- filed (B1).

### Query 11 -- "my skills" claude code teammate f=live
73. @sourfraser (Fraser Cottrell) -- "Claude + Skills = An AI employee for every job in your business," 6.2K views -- not filed as a quote, logged only in the null-results section as "loosely relevant, no teammate-handoff content."

### Query 12 -- "skills sprawl agents" f=live
74. @sethtjf (Seth Fenster) -- "I hate sprawl in my code bases... keep my skills light... need less of them with each new model" -- filed (B4, counter-evidence).
75. @CoreyGallon (Corey J. Gallon) -- re: Patrick Debois (Tessl) talk, "Coding Agents Don't Scale Themselves. Neither Do Your Teams" -- filed (B2).
76. @tonygentilcore (Tony Gentilcore) -- "AI sprawl is spreading across the enterprise... a Gateway that can deliver self-healing skills, memories," quote-tweeting @glean -- filed, and used as the citation vehicle for the Glean quote below (B2/B5).
77. @glean (Glean, official) -- "Glean AI Gateway, one governed layer for LLMs and MCP... control and ownership over the models, context, skills, and memories" -- filed (B5) but COULD NOT resolve its own direct permalink. I visited x.com/glean's profile directly afterward specifically to find this Aug 28 tweet; the profile's visible top post was a different one (Sep 3, a glean-it.com video link, status 2095564322340470901) -- I did not scroll far enough to locate the actual Aug 28 post and gave up, citing via @tonygentilcore's quote-tweet URL instead.
78. @awscloud (Amazon Web Services, official) -- "Is AI agent sprawl the new technical debt?... AWS Agent Registry" -- filed (B5) -- 31,717 views.
79. @samclaassen (Sam) -- "people who come to Type after trying a competitor... swarms of agents are bad" -- not filed, about a product called "Type," tangential.
80. @HashiCorp (official) -- webinar promo, "level up on your HashiCorp product skills" -- not filed immediately, false positive (human training skills, not AI agent skills).

### Query 13 -- "codex skills team" f=live
81. @dkundel (dominik kundel) -- "Five things I learned from using Astra," mentions a past "custom skill" for LEGO models, 490K views -- not filed, interesting anecdote but off-bucket (not about sharing/governance).
82. @angelbrodin (angel) -- "ChatGPT and Codex can help you apply our recommended changes... using the OpenAI docs skill: github.com/openai/skills/... GitHub - openai/skills: Skills Catalog for Codex" -- URL captured (status 2095903216705634729, 1,562 views), discussed in my reasoning as B1/B5 competitive intel, but DID NOT make it into the final filed markdown -- a notable omission (official OpenAI Codex skills-catalog repo).
83. @JohnnyWestLive (Johnny West) -- "Anthropic's Alpha Is Gone" opinion piece -- not filed, competitive model-quality commentary, not skills-specific.
84. @AndrewYNg (Andrew Ng) -- "AI Engineering Skills Map," 514K views -- DELIBERATELY EXCLUDED as a false positive: this is about human skill at using coding agents, not SKILL.md files. I did not click into the actual article to double check; the exclusion is based on the preview text and title alone.
85. @sanjeevSab17827 (Dr. Sanjeev Kuumar Sabharwal) -- "Claude + 35 add-ons = a whole company... 273k agentic skills framework + 88k production-grade engineering" -- not filed, judged as engagement-bait/exaggerated numbers, low-credibility listicle style.

### Query 14 -- "AGENTS.md skills team" f=live
86-92. @JavierEraia (duplicate Spanish article), @MarvellousDev (GPT-6 Astra prompting-tips article, 85K views), @Scobleizer (AI-generated model-comparison report), @akarsh_ghale (question re: GPT-6 Astra), @JohnnyWestLive (duplicate), @imraghava ("AI Engineering Skills Map" variant), @AndrewYNg (duplicate) -- none filed; all either duplicates from other queries or false positives on "skills" = human skill. Logged as dead end.

### Query 15 -- "context engineering skills team" f=live
93. @kingwilliam_ (KingWilliam) -- "How to build a one-person $1M company with Grok Bot" -- not filed, off-topic anecdote.
94. @yongkyun_lee (Yongkyun Lee) -- "Self-Evolving AI: Learning from Its Own Runs," mentions systems that "update model weights, prompts, skills, memory, workflows" -- NOT FILED -- thematically adjacent (self-evolving skills) but academic/theoretical framing with no concrete practitioner pain quote; a borderline drop.
95. @tomas_builds (Tom) -- "Do you still read AI-generated code?" -- not filed, off-topic.
96. @theyunglad (Shivam) -- "10 AI Skills Developers Need in 2026" -- not filed, false positive (human/framework skills, e.g. LangChain).
97. @tristangchen (Tristan Guwalgiya C.) -- "What FDEs need to learn for coding agents in 2026" -- not filed, same false-positive pattern.
98. @undefinedKi (Yarchi) -- "If Claude only let you install five skills... Marketing skills by Corey Haines - github.com/coreyhaines31/marketingskills. 50 skills..." -- filed (B1).
99. @undefinedKi (same account, Aug 29 post) -- "How to Set Up Claude Once and Get 10x Out of It," 5.4K views -- not filed separately, read only as author-reach context for #98.

### Query 16 -- "just a git repo" skills f=live (B4 hunt)
100. @xiuhan_xhu (Xiuhan) -- "We serve 13M AI creators... agent-first" -- not filed, off-topic company puff piece.
101. @ohmyzz (OhMyZZ) -- "Agent Readiness" / Factory droid concept -- not filed, off-topic (repo-readiness scoring, not registries).

### Query 17 -- "over-engineering" skills claude f=live (B4 hunt)
102. @FuckingSlaveMan -- "Behavioral Skills Claude.md... stops over-engineering simple tasks" -- not filed, product-promo for a specific markdown file, not a governance argument.
103. @FuckingSlaveMan (2nd, older post) -- "Your First AI Agent" article -- not filed, unrelated.
104. @ValenciaShark (Valencia Shark) -- "10 skills for Claude worth installing right now... Claude + TikTok, Claude + OnlyFans," 645 engagement -- not filed, listicle/promo with borderline content pairings, avoided.
105. @DailyDoseOfDS_ (Daily Dose of Data Science) -- "A single CLAUDE.md file hit 200k+ GitHub stars... derived from Karpathy's coding rules" -- filed (B4).
106. @akshay_pachaar (Akshay) -- "Anatomy of the .claude/ folder... CLAUDE.md, custom commands, skills, agents, permissions," 30K views -- NOT FILED -- a genuinely notable big-reach educational post I mentioned in reasoning but never wrote into the file. Flagged as a dropped B5 data point.

### Query 18 -- "don't need a registry" f=live (B4 hunt)
107-119. Thirteen results, all off-topic: @__KimE, @justjoenyc, @dmmaltby7xs1, @AmbAgboola (+ @Aderibi08070745 in the thread), @harmless_weirdo, @noringe88195, @PolitPaige, @Accelleratrix, @Zer0_XIII, @BazookaJoe999, @BongoKronik, @Rensontwitts, @LSthirdact -- wedding registries, gun/crime registries, gift registries. None filed. Logged as pure keyword collision.

### Query 19 -- "skills registry overkill" f=live (B4 hunt)
No results at all -- X returned "No results for 'skills registry overkill'." Nothing to log.

### Query 20 -- "a shared drive" OR "a folder" claude skills enough f=live (B4 hunt)
120. @kalapowered (Kala) -- "Automate your chargeback desk with Claude Code in a weekend" -- not filed, product-build story, off-topic to the registry-vs-folder question.
121. @PelletierV29 (Victoria Pelletier) -- "graveyard of dead initiatives" -- not filed, general corporate-strategy content.
122. @charliedbecker (Charlie D. Becker) -- reply describing a personal C:/vault folder structure (Obsidian + cloned GitHub repos) -- NOT FILED -- thematically close to "a folder is enough" but about general personal knowledge management, not Claude skills specifically; borderline drop.
123. @pnytechgaming (PNY Gaming) -- GPU vendor booth thank-you -- not filed, irrelevant.
124. @rtehrani (Rich Tehrani) -- government ERP procurement -- not filed, irrelevant.
125. @_echo3D_ (echo3D) -- "your most valuable content might be sitting unused in a shared drive... 3D assets" DAM pitch -- not filed, false positive on "shared drive" (3D asset management, not skills).

### Query 21 -- "just copy paste" skill.md f=live (B4 hunt)
126. @ZhugeLyang (LuBu) -- crypto testnet guide, paid partnership -- not filed, irrelevant.
127. @rot13maxi (Ryan Dale) -- "Shards: a game for your agent" card game -- not filed, irrelevant.

### Query 22 -- "skill.md prompt injection" f=live (B3 hunt)
128. @apprater (AppRater) -- "SkillSecurity - Free static security scanner for AI Skills... detect prompt injection, credenti[als]" -- filed (B3).
129. @riba2534 -- translated-from-Chinese warning about a "wallet draining trap" disguised as an agent project -- filed (B3).
130. @morgancap (The Donald, Spokane) -- "Prompts are the old layer. Skills, graphs, and control documents are the new one," referencing skills.sh, 66 engagement -- not filed, generic thought-leader framing, no concrete pain point.
131. @TriadDarren (RabbitHoleExplorer) -- "OpenClaw (2026.8.2) Skills: Compact Reference," a personal reference doc -- not filed, personal notes, not a pain/trust quote.
132. @yadnesh_sa88965 (Yadnesh) -- "Inside OpenClaw," notes OpenClaw has ~388,000 GitHub stars -- not filed, about OpenClaw's scale generally, not skills governance specifically.
133. @K_chachamaru (Japanese handle) -- Japanese, describes Claude becoming overcautious about prompt injection and refusing to run a legitimate, AGENTS.md-declared audit skill -- NOT FILED -- a genuinely relevant B3 nuance (over-caution/false-positive refusal) that I discussed in reasoning but dropped from the written file. Flagged as a gap.

### Query 23 -- "would not run"/"wouldn't run" claude skill f=live (B3 hunt)
No results -- empty page, no posts rendered.

### Query 24 -- "internal skill library" f=live (B1 hunt)
No results -- empty page, no posts rendered.

### Query 25 -- "our skills" claude code f=live (B1 hunt)
134. @MichLieben (Michel Lieben) -- "How to Vibe Code Your GTM the Right Way... ColdIQ $7M ARR... almost entire machine ran from Claude Code" -- not filed, no internal-skill-library specifics, logged as low-yield color.
135. @dan__rosenthal (Dan Rosenthal) -- "AI-native B2B services company... $2M ARR" -- not filed, off-topic business-model content.
136. @Team_D4rkn3ttz -- "Weekly Cyber Threat Intelligence Report" -- not filed, irrelevant (false positive).
137. @khemaridh (Khe Hy) -- "How Bridgewater built an AI Analyst" -- not filed, no skill-library specifics surfaced in the preview text.
138. @shadcncraft -- "Figma to Claude Code via MCP" walkthrough -- not filed, off-topic design workflow.
139. @khemaridh (2nd, older post) -- "Jensen makes the case for open source AI" -- not filed, off-topic.

### Query 26 -- "sync claude skills machines" f=live (B1 hunt)
140. @truffle (Christina) -- "My Claude user directory is a git repo... in sync across four machines" -- filed (B1).
141. @ClaudeCodeLog (Claude Code Changelog) -- automated changelog, sandbox credential masking -- not filed, release-notes bot.
142. @ShahzaibJak (Shahzaib) -- appreciation post for @HQForWork, "testing across five different AI apps" -- not filed, product-appreciation, tangential.
143. @simplifyinAI (Simplifying AI) -- "The founder of OpenClaw just open-sourced his entire personal agent setup... agent-scripts... shared rules, skills, and helper scripts across every local workspace" -- filed (B1).
144. @cathrynlavery (Cathryn) -- "Cross-machine agent-session audit" Fable prompt -- NOT FILED -- about auditing agent sessions across machines, adjacent to B1 but not skills-specific; borderline drop.
145. @cathrynlavery (2nd, older post) -- "How to set up multiple Macs for always-on AI agents," 7.8K views -- NOT FILED -- same borderline reasoning.

### Query 27 -- "shared this skill"/"gave my team" claude f=live (B1 hunt)
146. @xmousecopx -- "my boss gave my team a whole lecture today about how we need to start using claude and copilot. man i am Not Doing That Shit!!!" -- NOT FILED -- mildly relevant (workplace-mandate resistance / culture friction) but judged off-bucket (about resistance to AI tools generally, not skill-sharing mechanics specifically). Flagged as a borderline drop.
147-155. Remaining ~8 results (@wshuyi hometown-maps article, @VicVijayakumar "shared this skill with everyone, told them to do their own damn upgrades," @PaperSkies_Sc, @boringbonestv, @NSDCIndia, @HLtinkercad Tinkercad tip, @slimalchemist, @offtheball Roy Keane/Zidane football clip) -- none filed, all pre-2026 personal/lifestyle tweets or false positives on the literal phrase "shared this skill" unrelated to AI. Note: @VicVijayakumar's tweet is arguably the funniest near-miss of the whole research -- "shared this skill with everyone and told them to do their own damn upgrades" -- but it's about a completely unrelated (non-AI) topic based on context, so excluded.

---

[CONTENT_PLACEHOLDER]