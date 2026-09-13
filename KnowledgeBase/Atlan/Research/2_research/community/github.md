# GitHub Community Signals: How Developers Manage & Share AI Agent Skills

Research date: 2026-09-05. Scope: GitHub issues, discussions, topic pages, and repo READMEs for
anthropics/claude-code, anthropics/skills, vercel-labs/skills, openai/codex, modelcontextprotocol/registry,
plus community skill/plugin-marketplace repos. All quotes verbatim, <=50 words, tagged [verified] (page read
directly) or [reported] (summarized via a fetch tool without full manual cross-check).

---

## B1 — SHARING: asking how to share a skill with a teammate / roll out to a team (MOST IMPORTANT)

**Verdict: real, not thin.** At least seven distinct GitHub issues on anthropics/claude-code, filed by
different people between Feb and Aug 2026, ask for the same missing capability (install/sync a shared team
skill library). GitHub's own duplicate-bot merged them into one thread and then auto-closed it for
inactivity — it was never resolved by a shipped feature, only by staleness. That pattern (recurring demand,
no resolution, closed by bot not by fix) is itself strong signal.

1. **Quote:** "My team would like to share SKILLS we write within the team. We created a repo to keep them
   central." — workaround: "we have to clone the repo and copy the skill files manually w/ a script."
   **Author:** robosung | **Date:** 2026-02-25 | **Link:** https://github.com/anthropics/claude-code/issues/28327
   **Bucket:** B1 | **Why it matters:** Canonical ask — a team already centralizes skills in a repo but has
   no install path, only manual copy. 7 upvotes, 4 comments, closed as stale not fixed. [verified]

2. **Quote:** "Cross-company shared skill libraries... teams end up duplicating effort or missing out on
   skills other teams have built." **Author:** pablo-aviles-ruiz | **Date:** 2026-03-26
   **Link:** https://github.com/anthropics/claude-code/issues/28327#issuecomment (comment on #28327)
   **Bucket:** B1 | **Why it matters:** Same person filed a design sketch (skillsDirectories in settings.json)
   for cross-repo sharing at a consultancy/multi-team org. [verified]

3. **Quote:** "there's no clean native way to share a common skill library without resorting to symlinks or
   duplicating skill files everywhere." **Author:** pablo-aviles-ruiz | **Date:** 2026-03-26
   **Link:** https://github.com/anthropics/claude-code/issues/39403 | **Bucket:** B1
   **Why it matters:** Formal feature request for `skillsDirectories`; auto-closed as duplicate of #28327,
   citing two more duplicates (#26489, #38981) — at least 5 separate filings of the same ask. [verified]

4. **Quote:** "Using common skills which are used by my team members too. so i would want to develop a
   feature to share skills to team members." Priority marked "Critical - Blocking my work."
   **Author:** Shyamfc | **Date:** 2026-03-12 | **Link:** https://github.com/anthropics/claude-code/issues/33530
   **Bucket:** B1 | **Why it matters:** Self-rated business-blocking severity for a sharing gap, not a bug. [verified]

5. **Quote:** "ran into the friction point pretty fast on our end at ~5 engineers. everyone wants the same
   set of skills available, but ~/.claude/skills/ is per-machine so adding a new skill means everyone
   re-syncs manually." **Author:** latentloop07 | **Date:** 2026-05-13
   **Link:** https://github.com/anthropics/skills/issues/1132 | **Bucket:** B1
   **Why it matters:** Names three attempted patterns (git submodule, dotfiles sync, self-hosted registry
   poller) and says all three have failure modes; asks Anthropic for official guidance. 0 comments after
   4 months — unanswered. [verified]

6. **Quote:** "Manually backing up Claude Code config into a cloud-sync folder is fragile... cloud sync
   clients generally can't sync symlinks... so the sync silently fails or corrupts the client's internal
   sync state." **Author:** adamstallard | **Date:** 2026-08-16
   **Link:** https://github.com/anthropics/claude-code/issues/87068 | **Bucket:** B1
   **Why it matters:** Explicitly requests Anthropic-run settings/skills sync akin to VS Code Settings Sync,
   framing the current state (Dropbox/iCloud symlink hacks) as broken. [verified]

7. **Quote:** "Anyone working on the same project from more than one machine (shared repo, Dropbox,
   work/home laptops) loses it: the project syncs, its memory does not."
   **Author:** g-i-o-r-g-i-o | **Date:** 2026-08-28 | **Link:** https://github.com/anthropics/claude-code/issues/90394
   **Bucket:** B1 | **Why it matters:** Adjacent to skills — same underlying gap (per-user-profile storage of
   project-scoped state) applied to memory; proposes storing state inside `<project>/.claude/`. [verified]

8. **Quote:** "A user has to register the same GitHub repo three separate times, through three separate
   flows, to use the same skills everywhere." **Author:** deepumukundan | **Date:** 2026-08-25
   **Link:** https://github.com/anthropics/claude-code/issues/89413 | **Bucket:** B1
   **Why it matters:** Shows that even Anthropic's own three first-party surfaces (CLI, Desktop, Cowork)
   don't share one skill/marketplace registry — the fragmentation is native, not just cross-vendor. [verified]

9. **Quote:** "We had built a library of proprietary skills for our own development, and individual
   engineers had their own skills on top of the standard ones. All of that value was stranded on
   individual machines." **Author:** Justin Trugman | **Date:** 2026-06-15
   **Link:** https://betterfuturelabs.com/insights/internal-skills-marketplace-claude-code-github
   **Bucket:** B1 | **Why it matters:** A practitioner's stated reason for building an internal GitHub-based
   marketplace — direct motivation quote for a governed registry. [verified]

10. **Quote (README, stated reason a team collection exists):** "A collection of Claude Code skills shared
    by the Bytebase team. These skills encode proven workflows, domain knowledge, and best practices to
    help Claude Code assist more effectively with Bytebase-specific tasks."
    **Source:** bytebase/team-skills README | **Date:** n/a (repo, checked 2026-09-05)
    **Link:** https://github.com/bytebase/team-skills | **Bucket:** B1
    **Why it matters:** A real company (Bytebase, an open-source database CI/CD vendor) runs its team skill
    sharing as a plain public git repo — evidence for both B1 demand and the DIY pattern teams fall back to. [verified]

**.claude/ in the repo vs. dotfiles / committed config:** Claude Code's own convention already splits this —
`.claude/settings.json` is shared and git-tracked; `.claude/settings.local.json` is personal and gitignored.
But that split leaks in practice:

**Quote:** "the new rule is being persisted into the shared, git-tracked `.claude/settings.json` instead of
the personal `.claude/settings.local.json`. This leaks per-session, per-user permission entries... into a
file meant for team-wide, reviewed configuration." **Author:** denwitham | **Date:** 2026-09-01
**Link:** https://github.com/anthropics/claude-code/issues/91270 | **Bucket:** B1 (+B3 adjacent)
**Why it matters:** Confirms the "committed vs local" split is the accepted norm for `.claude/`, and that
the tooling itself violates it — evidence the boundary between shared/team and personal config is fragile
even where Anthropic designed for it. [verified]

---

## B2 — SPRAWL: too many skills, wrong skill invoked, context budget, staleness, version confusion

**Verdict: real and actively tooled-for by Anthropic, but the tooling itself is buggy** — Claude Code ships
a `/skill-doctor` command specifically to help users prune skills by token cost, which is itself the subject
of a same-day bug report saying its numbers are wrong. That's strong evidence sprawl is common enough to
need a built-in diagnostic, and that the diagnostic is still immature.

1. **Quote:** "`/skill-doctor`'s per-skill token/usage table is misleading enough to actively mislead pruning
   decisions." **Author:** shrek1ee | **Date:** 2026-09-05
   **Link:** https://github.com/anthropics/claude-code/issues/92327 | **Bucket:** B2
   **Why it matters:** Confirms (a) Anthropic ships a pruning tool because sprawl is common, and (b) a
   session's full token cost gets misattributed to every skill it touched, undermining the very metric users
   need to decide what to delete. [verified]

2. **Quote:** "positional-argument substitution [is] applied to the entire SKILL.md body, rewriting any
   literal $N token... 22/27 skills exposed, 0/27 use argument placeholders."
   **Author:** grantable-chris | **Date:** 2026-09-04 | **Link:** https://github.com/anthropics/claude-code/issues/91957
   **Bucket:** B2 | **Why it matters:** A silent content-corruption bug across most of one real production
   skill library — nobody would know which "version" of the skill actually ran in a given session; the
   issue cross-references 4 other overlapping bug reports (#79859, #78759, #87109, #84212). [verified]

3. **Quote:** "Twenty skills? You're burning tokens showing Claude options it doesn't need for the current
   task." **Author:** Michael Jovanovich | **Date:** 2025-11-27
   **Link:** https://responseawareness.substack.com/p/scaling-claude-code-skills-without
   **Bucket:** B2 | **Why it matters:** Independent practitioner built a semantic (vector-search) skill
   catalog specifically to solve context-budget dilution from too many skill listings. [verified]

---

## B3 — TRUST: hesitancy to install others' skills, prompt injection, credentials, review before adoption

**Verdict: real, and quantified.** skills.sh (vercel-labs/skills) already runs three separate third-party
security scanners per listed skill (Gen Agent Trust Hub, Socket, Snyk) and open issues are actively pushing
for a fourth, purpose-built layer for prompt-injection-style attacks — evidence the marketplace operator
itself treats an unreviewed skill as a live risk, not a hypothetical one.

1. **Quote:** "Across ~96,000 skills scanned (ClawHub, skills.sh, MCP registries), 552 were confirmed
   malicious after manual review." **Author:** eeee2345 | **Date:** 2026-06-30
   **Link:** https://github.com/vercel-labs/skills/issues/1552 | **Bucket:** B3
   **Why it matters:** A hard number for base-rate malicious-skill prevalence across the ecosystem, cited to
   justify adding an agent-threat-specific audit panel (tool poisoning, instruction-override, mapped to
   MITRE ATLAS / OWASP Agentic Top 10) because "a SKILL.md can hijack an agent with zero malicious code and
   no hash to flag" — i.e. existing dependency/malware scanners miss the skill-specific attack surface. [verified]

2. **Quote:** "In ClawHub specifically (9,676 skills), ATR flagged 182 as CRITIC[AL]"
   **Author:** eeee2345 | **Date:** 2026-06-30 | **Link:** https://github.com/vercel-labs/skills/issues/1552
   **Bucket:** B3 | **Why it matters:** ~1.9% critical-flag rate in one large public registry — a concrete
   number for "how much of what's out there is actively dangerous," useful for a governed-registry pitch. [verified]

3. **Quote:** "skills.sh listing... currently shows Gen Agent Trust Hub as Safe and Socket with no alerts,
   while Snyk reports Critical because of E005 and W011." **Author:** zztimur | **Date:** 2026-07-18
   **Link:** https://github.com/vercel-labs/skills/issues/1722 | **Bucket:** B3
   **Why it matters:** Shows three independent scanners can disagree on the same skill — trust signals on
   today's biggest community registry are inconsistent, not a solved problem. [verified]

[CONTENT_PLACEHOLDER]