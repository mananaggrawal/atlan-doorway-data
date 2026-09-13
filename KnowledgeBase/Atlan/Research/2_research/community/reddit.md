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

[CONTENT_PLACEHOLDER]