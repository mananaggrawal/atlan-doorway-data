# Prospect candidates
Named people who publicly expressed this pain. See `README.md` for the full picture; this file is sorted so the highest-intent tier is read first, not scattered through the raw research rows below.

## Tier 1 — highest intent: already built or maintaining a homegrown fix (revealed preference)
These people didn't just describe the pain, they spent real engineering time patching one slice of it themselves — sync, governance/audit, or manual usage measurement. That makes them the most qualified, most convertible conversation available, and the first outreach priority. See `../../3_thinking/hypotheses.md` H10. Full rows and links are in the tables below; this is the reading order, not a duplicate list.

1. **zwaantjuh** (Reddit, r/ClaudeCode) — hand-rolls ZIP re-uploads to sync org skills; explicitly wants GitHub-style push/sync.
2. **Necessary_Abroad6632** (Reddit, r/ClaudeCode) — built `agpm`, a CI approval/audit layer, after concluding nobody reviews the skills their agent installs.
3. **Justin Trugman** (blog, betterfuturelabs.com) — built an internal skills marketplace after finding value "stranded on individual machines."
4. **Abu_BakarSiddik** (Reddit, r/claudeskills) — open-sourced a cross-tool "Skill Manager" after hitting 140+ skills and visible degradation.
5. **Abhisheik Deo** (LinkedIn) — runs a shared skill library across a named 20-engineer team and ran a hundred-developer manual usage audit.
6. **Dijerati** (Reddit, r/ExperiencedDevs) — newly appointed "AI Lead," not yet built anything but actively about to be tasked with exactly this; worth catching before they build their own fix instead of adopting one.

**Named risk before trusting this tier:** sunk-cost / not-invented-here resistance is real — see Sammi's HN comment in the counter-evidence bucket below. Outreach to each of these needs to name that specific builder's actual gap, not a generic pitch.

## Tier 2 — documented pain, not yet building: the GitHub issue authors and commenters
Highest-intent by the original read (multi-paragraph technical specs, several offered to help draft docs) but stated rather than revealed preference. Still strong — robosung, pablo-aviles-ruiz, Shyamfc, latentloop07, deepumukundan, and the other GitHub rows below.

## Tier 3 — leverage, not prospects: founders of competing point-solutions
Built the *same kind* of fix as a funded or public product rather than an internal tool: mrdonbrown (sx), alex_metacraft (Askill), laul_pogan (Ingot), theahura (noriskillsets.dev), dariusmonsef (OzBrain), rgbrgb (setoku), conikeec (skillrecall), Pethuraj M (AgentSeal), guypod (Tessl), John McCann (shareskills.ai). These are competitive intelligence and, at most, partnership or press conversations — not the outreach list. Pitching a rival founder as a customer would be a mistake; they're evidence for H5, not the ICP.

---

## Full research rows

<!-- reddit/hn agent, 2026-09-05 -->
| handle | where | what they said | link | bucket | reachability |
|---|---|---|---|---|---|
| guypod | HN (Tessl founder, ex-Snyk founder) | "most teams still treat skills as static artifacts... Skills are duplicated, and updates never roll out... Skill knowledge grows stale" | https://news.ycombinator.com/item?id=46900933 | B1/B2 | High — public founder, Tessl has a site/contact; strong warm-intro candidate given direct thesis overlap |
| sjmaplesec | HN, comment on Tessl Show HN | "we have dozens of internal 'playbooks'... nobody knows which ones still work after model changes... pin a skill version and fail builds if eval scores drop" | https://news.ycombinator.com/item?id=46900933 | B1/B2 | Medium — HN username only, no public profile linked in thread |
| laul_pogan (Paul-James) | HN (Ingot founder) | "I built Ingot because skill changes felt like copy-paste, and are difficult to track across large orgs" | https://news.ycombinator.com/item?id=49007958 | B1/B2 | High — named founder, GitHub org SlanchaAI/ingot |
| atxpace | HN, comment on mattpocock/skills Show HN | "The useful skills are the org/team rules, and those are the ones that never leave someone's laptop... skillrepo.dev is for keeping that set current" | https://news.ycombinator.com/item?id=49529329 | B1 | Medium — HN username, likely affiliated with skillrepo.dev (competitor/partner lead) |
| dariusmonsef | HN (OzBrain founder) | "make it easy for me to share my chunks of knowledge with my teammates and their agents" | https://news.ycombinator.com/item?id=49394827 | B1 | High — named founder, ozbrain.com |
| rgbrgb | HN, comment on OzBrain thread (building "setoku") | "i want one tool i can have a colleague... install that adds all the context they'll need... one spot I can curate and govern that context" | https://news.ycombinator.com/item?id=49394827 | B1 | Medium — HN username, mentions own project "setoku" |
| mrdonbrown | HN (sx project maintainer) | "If you want to share skills using something that has versioning, automatic updates, and focused on teams... consider sx" | https://news.ycombinator.com/item?id=46692692 | B1 | High — GitHub sleuth-io/sx, named project |
| theahura | HN (noriskillsets.dev founder) | "You need versioning, linking between skills, an easy install client...basically a full package manager, which this is not" | https://news.ycombinator.com/item?id=46697908 | B1/B4-adjacent | High — named founder, noriskillsets.dev |
| iLoveOncall | HN, comment on skillregistry.io Show HN | "You have no versioning, no automated or simplified update, no way to verify the authors... I don't see how anything beyond git is necessary" | https://news.ycombinator.com/item?id=46692692 | B2/B4 | Medium — HN username only |
| m-hodges | HN, comment on skills.sh launch thread | "Why do none of these 'npm for Skills' document any way to do basic package management things like updates, version-pinning, or even uninstalls?" | https://news.ycombinator.com/item?id=46697908 | B2 | Medium — HN username, links to own agent-fecfile GitHub project |
| dave1010uk | HN, comment on skills.sh launch thread | "The install is very opaque. It's not clear where these skills are installed, how to upgrade them or remove them" | https://news.ycombinator.com/item?id=46697908 | B2 | Medium — HN username, likely dave1010 GitHub (active OSS contributor) |
| dirk94018 | HN (NoClaw author) | "watching OpenClaw users burn $800-$3600/month on tokens, deal with 1,100+ malicious ClawHub skills" | https://news.ycombinator.com/item?id=47437814 | B3 | Medium — HN username, linked blog linuxtoaster.com |
| gtirloni | HN, comment on skillregistry.io Show HN | "the skills have a checkmark next to the company's name, even though these skills weren't created by the respective companies" | https://news.ycombinator.com/item?id=46692692 | B2/B3 | Medium — HN username only |
| Sammi | HN, comment on OzBrain thread | "I've been pitched products like ozbrain before, but I've failed to see the need over what I already have. Seems like more complication for no gain to me." | https://news.ycombinator.com/item?id=49394827 | B4 | Medium — HN username only; valuable as a "convince me" interview target |
| alex_metacraft | HN (Askill author) | "I saw the Show HN for skills.sh a few weeks ago and noticed comments asking for version management, proper uninstalls, and more transparency" | https://news.ycombinator.com/item?id=46970692 | B1/B2/B3 | High — named GitHub avibe-bot/askill |
<!-- Added by Claude (X/Twitter skills-sharing research), 2026-09-05 -->
| @truffle (Christina) | X | Syncs Claude skills/plugins across 4 machines via a personal git-repo hack | https://x.com/truffle/status/2094800747904806924 | B1 | Small account, public reply guy, likely responsive |
| @49agents | X | Asks whether to version skills as markdown-in-git or something structured; hits stale/overlapping CLAUDE.md files | https://x.com/49agents/status/2094198834880504077 | B1/B2 | Builds an agentic IDE (49Agents) — practitioner + builder, good discovery-interview target |
| @RichStoneIO (Rich Steinmetz) | X | Started versioning his own global Claude skills to avoid irreversible behavior drift | https://x.com/RichStoneIO/status/2095549976461951408 | B1 | Small account, organic self-starter behavior |
| @mbritton (Mike Britton) | X | "writing too many skills and burning tokens needlessly when specs change" | https://x.com/mbritton/status/2096115952089710600 | B2 | Small account, direct pain quote |
| @humansandaiboss (patrick mcqueeny) | X | "too many skills and mcps to choose from... quality over quantity" | https://x.com/humansandaiboss/status/2096109356156592467 | B2 | Small account |
| @jaxkoh_ (Jax Koh) | X | Lost track of which session/skill did what; "too many skills/instructions created" | https://x.com/jaxkoh_/status/2095578862877073792 | B2 | Developer, evaluating agent-orchestration tools (adalagent) — strong ICP fit |
| @ibuildthecloud (Darren Shepherd) | X | Rancher/Acorn co-founder; publicly worried "isn't anyone worried about too many skills," wants progressive discovery | https://x.com/ibuildthecloud/status/2095555415971143695 | B2 | High-credibility infra builder, harder to reach but high value if responsive |
| @conikeec (chetan conikee) | X | Open-sourced "skillrecall" to measure which skill gets picked among 40+ in a harness | https://x.com/conikeec/status/2095951157361598550 | B2 | Active builder in adjacent tooling space, good interview + potential partner/competitor intel |
| @Ma7039Ma (mjhhh) | X (Chinese) | Installed every skill on skills.sh, had to purge, learned to install only what's needed | https://x.com/Ma7039Ma/status/2096232462632321445 | B2 | Small account, language barrier (Chinese) |
| @stratamindlabs (Strata Mind Labs) | X | "AI skills are starting to behave like software dependencies... most organizations do not yet have an intake gate" | https://x.com/stratamindlabs/status/2095996431068754426 | B3 | Small security-focused account, near-verbatim thesis match — high-value interview |
| @SilkNodeio (Silk node) | X | Asked whether skill approval binds to exact versions; flags staleness of intake scans | https://x.com/SilkNodeio/status/2096001185358458917 | B1/B3 | Small account, sharp technical reply — good interview candidate |
| @sunglasses_dev (Agentic AI Security) | X | "A trusted registry proves which artifact arrived. It does not prove the text is safe for agent context." | https://x.com/sunglasses_dev/status/2095628886520590669 | B3 | Runs a security blog/product (sunglasses.dev) — possible partner or competitor, worth a conversation |
| @Astrodevil_ (Mr. Anand) | X | "350k+ agent skills shipped... none had proper governance... no versioning, no scanning, no signing" | https://x.com/Astrodevil_/status/2084249065622212618 | B3 | Small account, ready-made thesis quote |
| @0MeissnerState (DarkHorseDelta) | X | On AWS Agent Registry GA: "the fifth team building the same internal agent is not innovation" | https://x.com/0MeissnerState/status/2095481937058021784 | B1 | Very small account (2 views) but sharp framing |
| @DannielDevOps | X | "Skills.sh... beats copying another skill.md by hand" | https://x.com/DannielDevOps/status/2096228201982992474 | B1 | Small account |
| @pvncher (eric provencher) | X | Codex DX @OpenAI. 1.5M-view essay on skill sprawl, contradictory descriptions, cross-model repo skills | https://x.com/pvncher/status/2095991462416490862 | B1/B2 | High-profile OpenAI staffer — aspirational interview/press target, unlikely to respond but worth a cold outreach attempt |
| @sethtjf (Seth Fenster) | X | Keeps skills deliberately light/portable; needs fewer with each new model | https://x.com/sethtjf/status/2095857577133240579 | B4 (counter) | Small account — useful for stress-testing the pitch against a skeptic |

[CONTENT_PLACEHOLDER]