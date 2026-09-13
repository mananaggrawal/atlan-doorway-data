# Community Signals: Reddit (live browser pass)

Pull date: 2026-09-05. Method: real logged-in-capable Chrome (via the Claude-in-Chrome extension driving the user's own browser), since old.reddit.com now hard-requires login and Claude's built-in Browser pane / all HTTP-fetch tools hard-block reddit.com by policy. www.reddit.com works fully logged-out. All entries below marked **[verified]** were read directly in that browser.

24 distinct queries run across r/ClaudeAI, r/ClaudeCode, r/claude, r/claudeskills, r/ExperiencedDevs, r/ChatGPTCoding, r/cursor, r/devops, r/programming, r/OpenAI, r/LocalLLaMA, plus site-wide searches. Reddit's own search is weak/loose (title: filters and exact-phrase quoting frequently return zero or irrelevant results even when a matching thread is known to exist — see Null Results). Most of what's below was surfaced by following a thread's own "Related posts" rail, which was far more reliable than the search box.

---

## B1 — SHARING (highest priority)

**[verified]** zwaantjuh (OP), r/ClaudeCode, "Best way to update and maintain organization skills in a team environment?":
> "currently for every update I have to manually re upload the ZIP files als org skills. Is there a way to do this more smoothly? Ideally it'd be a Github that I can commit / push new changes to that automatically sync with everyone's claude environments."
Permalink: https://www.reddit.com/r/ClaudeCode/comments/1vgb33u/best_way_to_update_and_maintain_organization/ (posted ~2026-08-05)
Why it matters: this is the single closest verbatim match to Atlan's registry pitch found anywhere in this pass — a small-finance-team Claude admin, given full ownership of the team's Claude subscription, hand-rolling "org skills" via ZIP re-upload because there is no push/sync path. Thread itself only has 6 upvotes / 11 comments — precise but low-visibility.

**[verified]** zwaantjuh (OP), same thread, reply comment:
> "Organization skills is the most direct / easy solution currently but maintaining & updating is the issue."
Permalink: https://www.reddit.com/r/ClaudeCode/comments/1vgb33u/comment/p1vsnxo/
Why it matters: OP names the gap precisely — the sharing mechanism exists (native "organization skills"), the maintenance/update loop does not.

**[verified]** troelskn, same thread:
> "Claude config files are just software/config like everything else. You need some kind of system for automatically pushing updates to your colleagues machines. That's typically an IT task and depends heavily on your specific setup/OS."
Permalink: https://www.reddit.com/r/ClaudeCode/comments/1vgb33u/best_way_to_update_and_maintain_organization/ (comment-level permalink not resolvable via accessibility tree; thread permalink given)
Why it matters: a second practitioner independently frames skill distribution as a software-config-management problem with no first-party tooling — validates "this needs real IT/ops tooling," not another prompt trick.

**[verified]** ayeryn, same thread (walking OP through a DIY GitHub-marketplace-as-plugin workaround):
> "Every time the plugin is updated (version bumped), user needs to go into their desktop or cli setup to update the plugin installed."
Permalink: https://www.reddit.com/r/ClaudeCode/comments/1vgb33u/comment/p1vs7sb/ (posted 2026-08-05)
Why it matters: confirms Claude Code's native plugin/marketplace mechanism has no push-update — every seat has to manually pull, which is exactly the "sync across machines" gap Atlan would close.

**[verified]** macbig273, same thread (posting a working `extraKnownMarketplaces` / `settings.json` config snippet):
> "Make a prive repo, look for the term "marketplace" and maintain the skill there. You can create "plugins" that can pack agents, skills etc ... people register it as a marketplace and they get auto update."
Permalink: https://www.reddit.com/r/ClaudeCode/comments/1vgb33u/comment/p1vpury/ (posted 2026-08-05)
Why it matters: a real, working, but fully DIY private-repo-as-marketplace pattern, pushed via `settings.json` — practitioners are already assembling Atlan's core mechanic out of raw primitives.

**[verified]** MeshugaTech, r/ClaudeCode, "If you aren't creating skills for your own project, start now." (489 upvotes / 99 comments):
> "Skills/rules are portable across tools. A well-written guardrails skill for Claude Code translates almost 1:1 to a .cursor/rules/*.mdc file with alwaysApply: true. The mental model is the same — you're writing onboarding docs for an AI coworker who has amnesia every session."
Permalink: https://www.reddit.com/r/ClaudeCode/comments/1rerqqd/comment/o7fimuu/ (2026-02-26)
Why it matters: names cross-harness portability (Claude Code <-> Cursor) as a real, already-practiced pattern — a registry that is harness-agnostic has an audience articulating exactly that need.

**[verified]** Sufficient_Ant_3008, r/ExperiencedDevs, "Recently was asked to become AI Lead for my team..." (75 upvotes / 40 comments):
> "he just implemented a claude-plugin using the idea of agent skills. It seems like nothing but it almost has 60k stars on it, so it's made a huge difference."
Permalink: https://www.reddit.com/r/ExperiencedDevs/comments/1ueibp5/comment/otqpykt/ (2026-06-25)
Why it matters: [note — "60k stars" is the commenter's own unverified claim about github.com/DietrichGebert/ponytail, not independently checked]. Still useful: a newly-appointed team AI lead being pointed at a public GitHub skill repo as the answer to "how do I bring my team up to speed" — informal, ad hoc sharing via random GitHub stars, not a governed registry.

**[verified]** Abu_BakarSiddik (OP), r/claudeskills, "Skill hell is real: 140+ installed skills made my agents worse at triggering, so I built a free app to manage the mess" (26 upvotes / 0 comments):
> "your skills live in ~11 different folders (~/.claude/skills, ~/.agents/skills, ~/.cursor/skills, ~/.gemini/skills...) with no shared view."
Permalink: https://www.reddit.com/r/claudeskills/comments/1w2a45r/skill_hell_is_real_140_installed_skills_made_my/ (2026-08-30)
Why it matters: independent builder shipping a free desktop "Skill Manager" (Tauri+React, open source) to solve cross-tool/cross-machine skill fragmentation — third-party confirmation the exact problem (skills scattered per-tool, no shared view) is real enough to build for, even with zero-comment traction.

---

## B2 — SPRAWL

**[verified]** Abu_BakarSiddik, same "Skill hell is real" post:
> "every skill you install rides along in your context, and its description competes for attention. Past a certain count — especially with overlapping skills — triggering gets visibly worse."
Permalink: https://www.reddit.com/r/claudeskills/comments/1w2a45r/skill_hell_is_real_140_installed_skills_made_my/
Why it matters: names the exact mechanism (context/description competition) behind "wrong skill fires" — a precise technical articulation of B2, from the subreddit built specifically around this pain.

**[verified]** MeshugaTech, r/ClaudeCode ("If you aren't creating skills..." thread):
> "tracking which rules actually prevent errors vs which ones Claude ignores, then pruning the ignored ones. Smaller, tighter rule sets work better than comprehensive ones."
Permalink: https://www.reddit.com/r/ClaudeCode/comments/1rerqqd/comment/o7fimuu/
Why it matters: describes manual, ad hoc "does this skill still earn its keep" pruning — exactly the staleness/quality-signal gap a registry with usage/eval data would remove.

**[verified]** Necessary_Abroad6632 (OP), r/ClaudeCode, "Nobody reviews the skills their agent installs. I built a CI gate for it." (1 upvote / 4 comments):
> "Everyone's .claude/skills/ folder is filling up with stuff pulled from marketplaces, gists, npx skills, random repos. On a team, those files land in the repo and nobody reviews them the way they'd review a dependency bump."
Permalink: https://www.reddit.com/r/ClaudeCode/comments/1vmwmfn/nobody_reviews_the_skills_their_agent_installs_i/ (2026-08-12)
Why it matters: dual B2/B3 — sprawl (folder fills up from many uncoordinated sources) compounding directly into an unreviewed-dependency trust problem. The linked tool (baselane-sh/agpm, "the approval and audit layer for agent skills") had 0 stars / 2 contributors at read time — a real but very early, unproven point solution.

---

## B3 — TRUST

**[verified]** Necessary_Abroad6632, same post:
> "A skill is just instructions your agent will follow and it changes silently."
Permalink: https://www.reddit.com/r/ClaudeCode/comments/1vmwmfn/nobody_reviews_the_skills_their_agent_installs_i/
Why it matters: crisp one-line statement of the exact supply-chain/drift risk a governed registry (pinned versions, review-gated updates) is built to close.

**[verified]** iamrolari, r/ClaudeAI, "Do I gatekeep these skills or share with wider team?" (96 upvotes / 87 comments) — top comment at 99 upvotes:
> "what keeps you valuable keeps you hired . 2) never train your potential or actual replacement unless you are leaving in your terms. I have about 30 more of these fyi"
Permalink: https://www.reddit.com/r/ClaudeAI/comments/1tzlq8w/comment/oqbqbws/ (2026-06-08)
Why it matters: the single highest-upvoted comment in the thread is an explicit argument AGAINST sharing skills with a team — job-security/ownership anxiety is a real, popular, and largely unaddressed objection to any "share your skills" pitch. Strong discovery-interview signal.

**[verified]** OkAerie7822, same thread (76 upvotes, the leading counter-argument to gatekeeping):
> "Gatekeeping buys you 3-6 months before someone else builds something similar. Sharing with you as the architect who runs the implementation makes you the internal AI expert for a process that touches senior leadership."
Permalink: https://www.reddit.com/r/ClaudeAI/comments/1tzlq8w/comment/oqbtlfe/ (2026-06-08)
Why it matters: the "share it, but own the rollout / document what it can't catch" camp — this is closer to how a registry with clear ownership and audit trail would be pitched internally, in the community's own words.

**[verified]** BullfrogRoyal7422 (OP), r/ChatGPTCoding, "How do you know your AI audit tool actually checked everything? I was fairly confident that my skill suite did. It didn't." (18 upvotes / 53 comments):
> "It had reported its findings with confidence, I'd acted on them, and more than half the actual problems were invisible to it."
Permalink: https://www.reddit.com/r/ChatGPTCoding/comments/1s6cjaq/how_do_you_know_your_ai_audit_tool_actually/ (~2026-04)
Why it matters: adjacent trust angle — not "trusting someone else's skill" but "trusting your own skill's correctness" once it's silently doing review work for you. Relevant to any pitch that a registry's quality signal (evals, review) is what makes a skill safe to rely on, not just safe to install.

---

## B4 — COUNTER-EVIDENCE (hunted deliberately)

**[verified]** Time-Dot-1808, r/ClaudeCode, "Am I using Claude Code wrong? My setup is dead simple while everyone else seems to have insane configs" (193 upvotes / 106 comments) — top comment, 117 upvotes:
> "Most of the elaborate setups solve one of two things: reducing the cost of re-establishing context across sessions, or automating feedback loops. If you're not hitting friction on either, the elaborate setup just adds overhead without real benefit."
Permalink: https://www.reddit.com/r/ClaudeCode/comments/1rovknm/comment/o9gm33l/ (2026-03-09)
Why it matters: the strongest direct counter-argument found — the community's own top-voted answer to "is minimal enough?" is "yes, unless you're hitting two specific frictions," which cuts squarely against always needing more skill tooling. (Note: replies underneath, e.g. FWiTU's "Skills actually change this game a lot" at 17 upvotes, push back — this is a live disagreement, not a settled consensus.)

**[verified]** Remarkable_Mud9885 (OP), r/claude, "Is there still any point in installing a bunch of skills?" (8 upvotes / 47 comments):
> "I'm not a huge fan of just installing existing skills; I much prefer figuring things out and exploring on my own."
Permalink: https://www.reddit.com/r/claude/comments/1vvfhw0/is_there_still_any_point_in_installing_a_bunch_of/ (2026-08-22)
Why it matters: direct rejection of the premise that pre-made/shared skills are inherently desirable — some practitioners see personal skill-building as the point, not a chore to outsource to a registry.

**[verified]** iamrolari's 99-upvote "never share" comment (see B3) doubles as B4: it is the top-voted answer in an 87-comment thread arguing the opposite of "share with your team" — per the thread's own auto-generated recap, "the overwhelming gut reaction is to gatekeep. Hard." (mod-bot TL;DR, not a user quote, so not counted as a verbatim finding, but useful framing).

No one was found stating outright "a git repo is enough for this" or using the word "overkill" about skills/registries in any indexed result — see Null Results. The counter-evidence that did surface is more "minimalism is underrated" and "sharing carries career risk" than "registries are unnecessary infrastructure."

---

## B5 — SIGNAL SHAPE

Subreddit activity (Reddit's own "weekly visitors" / "weekly contributions," read from each community's sidebar, 2026-09-05):

| Subreddit | Weekly visitors | Weekly contributions | Created |
|---|---|---|---|
| r/ClaudeAI | 1.6M | 24K | 2023-01-23 |
| r/ClaudeCode | 745K | 17K | 2025-02-24 |
| r/claude | 377K | 4.9K | 2013-12-06 |
| r/programming | 231K | 2.6K | -- |
| r/ExperiencedDevs | 212K | 4.8K | -- |
| r/devops | 124K | 2.2K | -- |
| r/ChatGPTCoding | 105K | 1.0K | 2022-12-06 |
| r/cursor | 105K | 2.7K | 2024-02-21 |
| r/claudeskills | 66K | 872 | 2025-10-19 |

Note: r/claudeskills is a dedicated subreddit for exactly this topic ("Skills are folders of instructions, scripts, and resources that Claude loads dynamically...") -- small in absolute terms next to r/ClaudeAI, but far denser in on-topic content per post than any general sub.

Thread-level engagement, on-topic threads found (upvotes / comments):
- "If you aren't creating skills for your own project, start now." -- 489 / 99 (r/ClaudeCode)
- "Top Agent Skills Repositories" -- 752 / 33 (r/claudeskills)
- "Which single skill has been the biggest game changer for you?" -- 360 / 92 (r/claudeskills, title only, not opened)
- "my agent skills stack in 2026, actually copy-pasteable" -- 529 / 22 (r/claudeskills, title only)
- "Do I gatekeep these skills or share with wider team?" -- 96 / 87 (r/ClaudeAI)
- "I don't use any skills, what am I missing on?" -- 48 / 93 (r/ClaudeCode, title only)
- "Recently was asked to become AI Lead for my team..." -- 75 / 40 (r/ExperiencedDevs)
- "Am I using Claude Code wrong?..." -- 193 / 106 (r/ClaudeCode)
- "How do you know your AI audit tool actually checked everything?..." -- 18 / 53 (r/ChatGPTCoding)
- "Is there still any point in installing a bunch of skills?" -- 8 / 47 (r/claude)
- "Best way to update and maintain organization skills in a team environment?" -- 6 / 11 (r/ClaudeCode) -- the single most precisely on-topic B1 thread found, and also the lowest-engagement
- "Skill hell is real: 140+ installed skills..." -- 26 / 0 (r/claudeskills)
- "Nobody reviews the skills their agent installs. I built a CI gate for it." -- 1 / 4 (r/ClaudeCode)

Reading of the shape: general-purpose engagement (funny/venting/showcase posts) dwarfs anything team-governance-shaped by 10-50x in upvotes. The precise "how do we sync/govern skills across a team" question exists, is asked earnestly, and gets real practitioner answers with working config snippets -- but it's a minority thread type that tops out in the single-to-low-double-digit upvotes, not the hundreds. The team-sharing pain is real but niche relative to Reddit's overall skills conversation, which skews toward personal productivity and showcase content.

---

## NULL RESULTS (queries that returned nothing on-topic)

- `skills.sh` (site-wide) -- no relevant results; all unrelated (legal/entertainment threads).
- `"skills registry"` (site-wide, exact phrase) -- surfaced only OpenClaw/ClawHub content (a different, unrelated tool ecosystem, not Claude Code/Codex) -- not counted as evidence here.
- `"skill sprawl"` (site-wide, exact phrase) -- no relevant results under that exact phrasing (the on-topic "Skill hell is real" post was found via a different query).
- r/ClaudeCode, `title:"I don't use any skills"` (exact quoted title incl. apostrophe) -- 0 results; the real thread exists but only surfaces under looser phrasing.
- `"skills versioning"` (site-wide, exact phrase) -- 0 relevant results.
- `"team skills library"` (site-wide, exact phrase) -- 0 relevant results.
- r/cursor, `skills sharing team` -- 0 relevant results; r/cursor's discourse doesn't use "skills" framing for this at all (Cursor's equivalent is `.cursor/rules/*.mdc`, referenced only in passing on r/ClaudeCode, not discussed as its own governance topic on r/cursor itself).
- r/devops, `claude skills` -- 0 team-sharing-specific threads; only general devops/AI-tooling content.
- r/programming, `claude skills` -- only one thin, low-engagement thread (0 votes / 12 comments, about a Neovim integration).
- r/OpenAI, `codex skills team` -- 0 relevant results.
- r/LocalLLaMA, `agent skills sharing` -- 0 relevant results.
- `skills "just use a git repo"` (site-wide) -- 0 relevant results.
- `skills "overkill" claude` (site-wide) -- 0 relevant results.

Reddit's search is unreliable for this kind of long-tail, technical query -- exact-phrase and `title:` filters routinely return zero even for threads known (via a "related posts" rail) to exist. Anyone repeating this pass should lean on subreddit-scoped browsing and "related posts" rails, not the search box alone.

---

## Channel viability read

- **Access is the first finding**: Claude's own Browser pane and every HTTP-fetch/WebFetch tool hard-block all of reddit.com by policy (confirmed via repeated `request_access` failures, not just an unapproved-site prompt). old.reddit.com now requires a login for every page, including search and comments. www.reddit.com works fully logged-out and was the only viable path, reached only via a real Chrome browser under the Claude-in-Chrome extension. This is worth flagging to whoever owns the research pipeline: without this workaround, Reddit is invisible to this stack.
- **The exact pain is real but thin**: the most precisely-worded "team skill governance" thread found (zwaantjuh's) has single-digit upvotes. The community is not organizing around this problem in one visible place inside the big general subs.
- **A purpose-built niche exists**: r/claudeskills (created Oct 2025, 66K weekly visitors) is a dedicated home for exactly this conversation and produces much higher on-topic engagement per post (up to 752 upvotes) than the general subs manage for the same topic -- this is plausibly the single best-targeted Reddit surface for both listening and eventual distribution.
- **Both camps are loud**: sharing/registry-shaped asks (B1) and anti-sharing, job-security-driven pushback (B3/B4) both draw real upvotes in the same threads -- any GTM message needs to address "why sharing doesn't cost you your job" as directly as it addresses "how do we sync updates."

## Discovery-interview candidates (Reddit usernames, public posts only)

- **zwaantjuh** (r/ClaudeCode) -- finance-team Claude admin, hand-rolling org-skill ZIP re-uploads, explicitly wants GitHub-style push/sync. Best single candidate found.
- **Abu_BakarSiddik** (r/claudeskills) -- built a free open-source cross-tool "Skill Manager" desktop app to solve his own 140+-skill sprawl problem.
- **Necessary_Abroad6632** (r/ClaudeCode) -- built `agpm`, an "approval and audit layer for agent skills" CI gate, from lived pain about unreviewed skill drift on a team.
- **Dijerati** (r/ExperiencedDevs) -- newly asked to become "AI Lead" for their team's Claude Code/CLI rollout, actively looking for how to do this well.
- **Natural-Round8762** (r/ClaudeAI) -- wrote a skill at work, is actively weighing gatekeeping it vs. formalizing and sharing it with the wider team.
