# Atlan Pulse v2 — build plan

Written 13 Sep 2026, revised twice the same day. Supersedes `skill_health_plan.md` and demotes `pulse/`
(the npm CLI) from "the build deliverable" to the funnel.

**Locked:** the portal is the build deliverable · Dedupe and Security Scan are **Phase 1**, as agent-run audit
skills · Usage is **Phase 1** (the plumbing already exists — §4.5) · the facts-only reporting rule from the CLI
era is **retired**; the product may state a score.

---

## Build status — 13 Sep 2026

**Phase 1 is built.** Milestones M1–M5 landed in `4_build/atlas`, plus the four skills. Green across the board:
typecheck clean on all seven packages, **3,985 tests passing** (core-backend 2,162 · core-frontend 1,602 ·
atlas-mcp 136 · mcp-core 85), design-system ratchet passing with its counts *down*.

Validated on real data: **Manan's 19 account skills score 83/100** (119% of the listing budget; found the same
`linkedin-send-connect-request` ↔ `linkedin-send-dm` duplicate pair the old CLI found), **Anthropic's 33 example
skills score 73/100** (157% of budget, two with no description at all), **Pulse's own four skills score 100/100.**

Not done: M0 (Manan's to do — push, rename the Render service), M6 (landing page + submission rewrite), and the
two items under "Open after the build" at the end of this file. Nothing is committed or pushed; the working tree
is left for review.

---

## 0. The codebase

| | |
|---|---|
| Local | `~/Atlan/4_build/atlas` |
| GitHub | `mananaggrawal/atlan-pulse-app` |
| Live | https://atlas-xwwr.onrender.com (slug still says "atlas") |
| Stack | Node 22 · Postgres 17 · Drizzle · React/Vite · Docker |
| Scale | 176k lines TS/TSX, 810 files, 310 test files, 23 backend modules |
| Verified | 3,825 tests passing, typecheck clean, boots on Postgres 17, OAuth AS discovery live |

Everything below is built on this. It is a working product already — the job is to add the sync layer, the audit
engine and the share mechanic, and to surface two features that exist but aren't presented as features.

---

## 1. What already exists

Verified by reading the modules, not assumed.

| Requested feature | Status | Where |
|---|---|---|
| **Trail / Change Management** | **Built** | `modules/workflow` (review-workflow, pending-commits, event-bus, git), `modules/diff` — every write is a commit; change requests with review and merge |
| **Share / Access Management** | **Built** | `modules/access` + `modules/access-model` — per-file `roles.yaml` grammar, groups, creator access, join requests, `Plugins/<name>/access.md` scoping |
| **MCP server + OAuth 2.1** | **Built** | `modules/mcp` (+ `oauth/`), `packages/atlas-mcp`, `packages/mcp-core` |
| **Skill registry** | **Built** | `modules/skills`, `modules/plugins`, `/skills-and-tools` |
| **Usage telemetry** | **Plumbing built, no surface** | `skill_invocations` table + `SkillInvocationRecorder` (buffered, 90-day retention) wired into `createToolHandlerFactory`. Event carries `userId, sessionId, toolName, skillName, skillVersion, outcome, errorKind, latencyMs` — and *by construction* cannot carry call arguments or skill content. |
| **Skill health** | **Partial — being replaced** | `modules/skill-health` Tier 0/1 checks + one `skill_health` MCP tool |

**Net-new:** skill sync in either direction (the `plugins` module is access-scoped folders, **not** Claude
plugins — there is no `marketplace.json` anywhere in the repo); the three audit skills; the Pulse Score; the card
and `skill.health`; the Usage dashboard; and Trail/Access as named IA.

---

## 2. Product shape

**Atlan Pulse — the control plane for the skills your agents run.**

### Phase 1 — build now

1. **MCP Connection** — connect Claude once; skills move both ways
2. **Health** — agent-run audit: context cost, structure, freshness, trigger quality
3. **Dedupe** — agent-run audit: redundancy and intent overlap across the selected set
4. **Security Scan** — agent-run audit: secrets, injection surface, declared tool access
5. **Usage** — invocation reporting from `skill_invocations`
6. **Trail / Change Management** — exists, needs surfacing
7. **Share / Access Management** — exists, needs surfacing

### Phase 2 — coming soon

The **continuous, policy-grade** versions of the same things:

- **Security gate at commit time** — block a merge that introduces a credential, rather than reporting it after
- **Scheduled re-audits and drift alerts** — "this skill's score dropped 14 points since Tuesday"
- **Dedupe as a consolidation workflow** — merge, deprecate, redirect, with the change request wired up
- **Usage economics** — cost per run, per-team rollups, adoption curves over time
- **Org rollups** — one score for a team, not a person

Phase 1 answers "what is true about my skills right now." Phase 2 answers "keep it true without me asking."
That line holds up under questioning, which matters more than the feature count.

---

## 3. The flow, end to end

### 3.1 Connect

1. Portal → **Connect Claude**. The MCP endpoint and OAuth 2.1 already exist, and the snippet already renders.
2. Claude Code: `claude mcp add --transport http atlan-pulse https://<host>/api/mcp`
   Claude desktop / Cowork: paste the URL into Connectors.

Net-new: a real first-run screen instead of a dialog buried in a sidebar.

### 3.2 Push — skills go up

The agent does this, not a file picker. Selection is explicit, never a silent slurp.

```
Claude ──enumerate local + shared skills──► (user selects) ──push_skills(MCP)──► Pulse
   └─ Plugins/personal-<user-id>/<skill>/SKILL.md · one commit per push · authored as the user
```

| New MCP tool | Purpose |
|---|---|
| `list_synced_skills` | what Pulse holds, with content hashes, so the agent diffs before pushing |
| `push_skills` | `{ skills: [{ name, origin, content, files[] }], target }` → per-skill status |
| `pull_skill` | SKILL.md + supporting files, for the agent to write locally |
| `diff_skill` | local vs Pulse — so "to and fro" never silently overwrites |

**The one correctness decision that matters:** a push that would overwrite a *newer* Pulse version does not
force-write — it **opens a change request**, which `modules/workflow/review-workflow` already does. The hardest
sync problem becomes a live demo of Trail/Change Management. Do not build a separate conflict resolver.

**Origin tracking.** Every synced skill records `personal` / `shared-with-me` / `project` / `plugin`. That is what
makes "skills shared with me via Claude" a real thing in the dashboard instead of an undifferentiated blob.

### 3.3 Appear in the dashboard

`/skills-and-tools` already lists the catalog. Additions: source badge, origin, last-synced, **Sync now**, and
per-skill **Trail** and **Access** tabs (M5).

### 3.4 Audit

Two entry points, one endpoint (`POST /api/audits/runs`):

- **Portal** — "Run audit", with checkboxes for which skills and which of the three audits
- **Claude** — "run a security scan on my skills" → the matching audit skill

A portal-triggered run gets the deterministic layer only. A Claude-triggered run also gets the model layer,
because the model is what is running the skill. The report says which layers ran; a portal run does not pretend
to judgment it never received.

### 3.5 Output

- **The card** — public, shareable, Twitter-shaped: `skill.health/s/<slug>`. Numbers only, never skill content.
- **The report** — private, in-portal, per-skill detail. Everything.

### 3.6 Pull — skills come back down

- **Claude Code:** `pull_skill` writes the files directly.
- **Claude desktop / Cowork:** the agent cannot write to the local skills directory, so pull runs through a
  **Claude plugin marketplace** Pulse serves — `/plugin marketplace add <pulse-url>`, then `/plugin install`.
  The manifest is generated from the plugin folders the caller can access, so **access control decides what is
  installable**. Share/Access becomes the distribution channel rather than a settings page.

### 3.7 The loop

```
card posted ──► visitor ──► skill.health ──► connect Claude ──► push ──► audit ──► their card
```

Every card footer: *Audited with Atlan Pulse — skill.health*.

---

## 4. The audit engine

Not a local script. Three **skills** the agent runs against the skills you selected, each writing findings into
one shared run record.

### 4.1 Three skills, one run

| Skill | Answers |
|---|---|
| `atlan-pulse/skill-health` | What do these skills cost me, and are they well-formed? |
| `atlan-pulse/skill-dedupe` | Am I carrying two skills that do the same job? |
| `atlan-pulse/skill-security` | Is there anything in here I would not want shipped? |

"Run a full audit" is all three. Each can also run alone — which matters for distribution, because
*"run a security scan on my skills"* is a sentence someone types unprompted, and "run a health check" is not, yet.

### 4.2 Layer A — deterministic measurement (server-side)

Reproducible, versioned, identical for every user. **The only layer the score is built on.**

**Health**
- *Listing cost* — tokens in `name` + `description`, the part loaded into every prompt, per skill and catalog-total against a stated budget. The headline number.
- *Body cost* — tokens in the full SKILL.md: what invoking it actually costs.
- *Structure* — missing description, missing owner, a description that states no trigger, broken relative file refs, oversized body.
- *Freshness* — last **commit** date. Git-backed, so the CLI's "mtime lies in a fresh clone" caveat is gone.

**Dedupe**
- *Description similarity* — pairwise trigram score, then embeddings where available, over the selected set → candidate pairs above a stated threshold.
- *Trigger collision* — two skills whose descriptions would fire on the same request.
- *Body near-duplication* — normalised shingles, catching a copy-paste fork with a renamed heading.

**Security**
- *Secret shapes* — high-entropy strings plus known credential prefixes (`AKIA…`, `sk-…`, `ghp_…`, JWT, PEM headers). Reports **file + line + pattern class, never the value.**
- *Declared tool access* — which skills declare shell, network or delete capability, and which of those also read untrusted input.
- *Remote-fetch instructions* — a skill that tells the agent to fetch a URL and follow what it finds is the prompt-injection surface. Flag it structurally, before any model looks.
- *Egress hints* — hardcoded hosts, webhooks, mail endpoints.

### 4.3 Layer B — model judgment (runs in Claude)

The upgrade over a script, and the reason these are skills. Fixed rubric, structured output, one mandatory
`evidence_quote` per finding so the model stays anchored to the file.

- **Trigger clarity** — would this description fire on the right request and *not* on others? The most common real failure mode of a skill, and invisible to regex.
- **Instruction ambiguity or self-contradiction**
- **Intent overlap** — semantic duplication that trigram scoring misses (feeds Dedupe)
- **Injection reachability** — does untrusted content actually reach an instruction boundary? (feeds Security)
- **Missing guardrails** on destructive operations

Posted back via `submit_audit_findings`. These appear in the report as **Reviewer notes**, clearly labelled as
model-written, and **never enter the score**.

### 4.4 The score — Pulse Score

The facts-only rule is retired, so the product may say something. It should still only say what it can defend.

**Pulse Score, 0–100, computed from Layer A only, stamped with an engine version.**

| Component | Weight | Built from |
|---|---|---|
| **Context efficiency** | 35 | listing-token cost against budget; penalty scales with overage, not a cliff |
| **Hygiene** | 25 | structure checks passed, as a proportion; freshness as a modifier |
| **Uniqueness** | 20 | share of the selected set not in a duplicate pair above threshold |
| **Safety** | 20 | secret findings and unjustified destructive tool access, weighted by severity class |

Bands: **90+ / 75–89 / 60–74 / below 60.** The three sub-scores show alongside the total so the number is
readable rather than oracular — a 72 that reads "safety 20/20, context 12/35" tells you what to do; a bare 72
does not.

Three rules keep it honest:

1. **Every card carries `engine v1`.** A score is only comparable within an engine version. When the engine
   changes, the version changes, and old cards keep saying what they measured.
2. **Layer B never touches the score.** Non-deterministic input would make two runs of the same catalog disagree.
3. **Percentile is suppressed until N ≥ 30 published runs.** A percentile over four runs is a lie. Write the rule
   before the first card exists, not after someone screenshots the wrong one.

The method gets a public page — `skill.health/method` — showing the weights and the checks. That page is what
turns a number into a benchmark instead of a vanity metric, and it is the answer to the first sceptical reply.

### 4.5 Usage — Phase 1, with its limits stated

**Feasible now**, because the hard part exists: `skill_invocations` is in the schema, and
`SkillInvocationRecorder` (buffered flush, 90-day retention, fire-and-forget so telemetry can never fail a tool
call) is wired into `createToolHandlerFactory`. The event carries `skillName`, `skillVersion`, `outcome`,
`errorKind` and `latencyMs`, and structurally cannot carry arguments or skill content. What is missing is only a
reporting surface.

Ship: invocations per skill over a window · top-N concentration ("3 skills are 78% of calls") · never-invoked
list · error and denial rate · p50/p95 latency · unique callers.

**The limit, printed on the dashboard rather than buried:** this counts calls that go **through Pulse's MCP**.
A skill installed locally and invoked without touching Pulse is invisible here. Do not let a chart imply
otherwise — a stated limitation reads as credibility, not weakness.

Deferred to Phase 2: cost per run, team rollups, trends over time.

### 4.6 Distribution of the skills themselves

The three audit skills ship as the **first plugin in Pulse's own marketplace**. The first skill you install from
Atlan Pulse is the one that audits your skills. That is the demo beat, and it exercises the pull path on day one.

---

## 5. The card and skill.health

**Ship a URL and an image, because Twitter needs the URL in order to unfurl the image.**

- `skill.health/s/<slug>` — public HTML, no auth, brand-carrying, with the CTA and a link to `/method`.
- `skill.health/s/<slug>/card.png` — 1200×630, referenced as `og:image` / `twitter:image`, `summary_large_image`.
- Render with **satori + resvg-js** — no browser dependency, small, deterministic. The public route should not be
  launching headless Chromium.
- The PNG is immutable per run: render once, cache forever.

**Card v1 content**

> `atlan | Pulse`
> **Pulse Score 78** · context 24/35 · hygiene 22/25 · uniqueness 16/20 · safety 16/20
> 38 skills · 4,180 tokens loaded on every prompt · 2 duplicate pairs · 0 secrets found
> `engine v1 · skill.health`

**Privacy contract — written as a test, not a convention.** A published card may contain counts, aggregate token
numbers, sub-scores, percentile, run date, engine version and a display handle. It may **never** contain skill
bodies, skill descriptions, secret findings, file paths, or — by default — skill names. Showing skill names is a
separate explicit toggle.

**Publishing is an action.** Runs are private by default; "Publish card" is a button and unpublish works.

**Domain.** `.health` is a real ICANN TLD but a premium one — budget roughly $70–110/yr and **check availability
at a registrar before the name reaches any copy** (it could not be verified from this environment). Fallbacks, in
order: `skillhealth.dev`, `skillhealth.com`, or `pulse.<existing-domain>/s/<slug>`. For the assignment itself a
path on the existing Render host is sufficient — the domain is a launch nicety, not a dependency.

---

## 6. Milestones

### M0 — Unblock (0.5d)
- Push local `master` (`f951558`); GitHub is behind and `README.md` is uncommitted.
- Rename the Render service off `atlas-xwwr`.
- CLI: keep `npx atlan-pulse` alive as the no-signup try-it path, ending by pointing at the portal.

### M1 — MCP connection and sync (3–4d)
- `modules/skills`: `push_skills`, `pull_skill`, `diff_skill`, `list_synced_skills`, registered on both manuals
  via `toolDef` like the existing skill tools.
- Conflict → change request, reusing `modules/workflow/review-workflow`.
- Origin metadata on synced skills.
- Frontend: Connect Claude screen, source badges, last-synced, Sync now.
- `atlan-pulse/skill-sync` SKILL.md.

### M2 — Audit engine (5–6d)
- New package `packages/skill-audit` — pure detectors, no express/db dependency, reusable by a CLI or CI action.
- Three detector families: health, dedupe, security (§4.2).
- `modules/skill-health` → `modules/audits`, around a `runs` table: run id, user, skill set, audits requested,
  engine version, Layer A results, Layer B findings, score, published flag, public slug.
- MCP tools: `start_audit({ skills[], audits[] })` → run id + rubric; `submit_audit_findings`; `finish_audit` → URLs.
- Keep the existing `skill_health` tool as a thin read-only view over the latest run so nothing already calling it breaks.
- Portal: Run audit (catalog / selection / single skill), run history, report view.
- Three SKILL.md files: `skill-health`, `skill-dedupe`, `skill-security`.

### M3 — Score, card and skill.health (3d)
- Scoring module with the weights in §4.4, versioned, unit-tested against fixture catalogs.
- `modules/public-card`: `GET /s/:slug`, `GET /s/:slug/card.png`, unauthenticated, rate-limited.
- `/method` page.
- OG/Twitter meta, satori render, immutable cache, privacy-contract test.

### M4 — Usage dashboard (1.5d)
- Read surface over `skill_invocations` (§4.5) plus the stated-limit banner.
- Phase 2 items appear in nav as "coming soon" with their real shape. **No fake data anywhere.**

### M5 — Surface Trail and Access (1–2d)
- **Trail** tab per skill: commit history, change requests, diffs (`modules/diff` + `modules/workflow`).
- **Access** tab per skill: resolved `roles.yaml` verdict — who can read, write, own, and how to request access.
- Marketplace manifest generated from access-visible plugin folders, closing the loop from §3.6.

### M6 — Landing and submission rewrite (2–3d)
- Landing page on the Atlan system; pink accent permitted here.
- Deck and evidence appendix rewritten around the portal, closing the four gaps in
  `problems_solutions_map_sep12.md` §3.

**Rough total: 16–20 working days solo.**

---

## 7. Brand

Atlan's system, already partly applied in `packages/core-frontend/src/shared/theme/tokens.css`.

| Token | Value | Use |
|---|---|---|
| Persian Blue | `#2026D2` | the one interactive colour in the app; primary in marketing |
| Blue hover | `#1D22BC` | |
| Pink | `#F34D77` | marketing only — card, landing, skill.health. **Not** in the app. |
| Cyan | `#62E1FC` | secondary marketing accent |
| Ink | `#252530` / `#141517` | text |
| Grey | `#77778E`, `#DDDDE3`, `#E9E9F0` | secondary text, rules |
| Surface | `#FFFFFF`, `#F9F9FC`, `#F8F8FA` | |

Established rules worth keeping: **exactly one interactive colour inside the app**; every palette change runs
against the repo's own WCAG contrast test.

**No brand-guidelines artefact exists anywhere in `~/Atlan`** — the palette above was reverse-engineered from
`tokens.css` and the CLI report. Source the real thing before M6.

**Decided: the public card does not carry Atlan's actual wordmark.** The app already made this call deliberately —
using Atlan's mark would misrepresent affiliation — and a public, indexable, shareable page is a *stronger* claim
than a local PDF ever was. The card carries a "Pulse" lockup set in Atlan's type and colour system. Atlan's real
mark appears only in the submission deck, where the context is unambiguous.

---

## 8. Decisions, made

| # | Decision | Call |
|---|---|---|
| 1 | Score or facts-only? | **Pulse Score 0–100**, deterministic only, with sub-scores, an engine version, and a public `/method` page. Facts-only retired. |
| 2 | Atlan's wordmark on the public card? | **No.** "Pulse" lockup in Atlan's type/colour system; real mark in the deck only. |
| 3 | CLI — keep or archive? | **Keep**, rewired as the no-signup top of funnel pointing at the portal. |
| 4 | Domain | Verify `skill.health` at a registrar; `skillhealth.dev` is the fallback. For the assignment, a path on the existing host is enough. |
| 5 | Phase 2 in the nav? | **Show**, with real shape and no fake data — communicating the product's shape is half the point of a work sample. |
| 6 | Dedupe and Security in Phase 1? | **Yes**, as two of the three agent-run audit skills. |
| 7 | Usage in Phase 1? | **Yes** — `skill_invocations` and its recorder already exist; only the read surface is missing. Coverage limit stated on the dashboard. |

---

## 9. Risks

1. **Score comparability.** Mitigated by the engine-version stamp and `/method`; without those, "we made the number up" is a fair hit.
2. **Percentile before corpus.** Suppressed until N ≥ 30.
3. **Model findings drifting into the score by accident.** One careless merge in Layer C and two runs of the same catalog disagree. Guard with a test, not a comment.
4. **Claude desktop cannot write local files** — pull there is marketplace-only; Claude Code gets both paths.
5. **Manan's own Mac has no local skills and no readable session history** (`~/.claude/sessions` holds only `.key` files). His skills live in his Claude account, which the new design handles — but the demo must run through the account, not the filesystem.
6. **Usage coverage.** Only traffic through Pulse. Stated, not hidden.
7. **Secret scanning must never echo a secret.** The CLI learned this the hard way when a debug census printed `.key` paths that ended up in a screenshot. Count and locate; never open, never name, never quote.
8. **Two repos named Pulse** — `mananaggrawal/atlan-pulse` (CLI) and `-app` (this). M0 resolves the naming.

**Deployment note, not a risk here:** Render's free tier spins a service down after ~15 minutes idle, so the first
request to a cold instance takes 30–60 seconds. That would matter for a product whose growth runs through public
links; for an assignment it does not. Warm the instance before a demo or review, and if this ever goes genuinely
public, a ~$7/month always-on instance plus serving published cards from static storage removes it entirely.

---

## 10. Verification

Drawn from what has already gone wrong on this repo.

- **Privacy contract test** — assert no skill body, description, file path or secret value can reach a published card object.
- **Score determinism test** — same catalog, same engine version, N runs, identical score. Layer B findings present but excluded.
- **Round-trip test** — push → audit → pull → `diff_skill` returns clean.
- **Conflict test** — a stale push opens a change request and writes nothing.
- **Live click-through after any routing or `CORE_APPS` change.** Two separate blank-page bugs here were invisible to 1,587 passing frontend tests and were caught only by loading the deploy.
- **Render the card and look at it** — stage the PNG, screenshot it, read it. Then run the real URL through X's card validator.
- **Pack and run** — nothing counts as shipped until it runs from a fresh clone on a real machine.


---

## Open after the build

Two things the build deliberately left to a decision rather than settling on its own.

1. **The OG image is an SVG, so links will not unfurl with a picture.** X and LinkedIn do not render SVG in a
   preview card. Fixing it means rasterising server-side, which means two dependencies — `satori` and
   `@resvg/resvg-wasm`. Both are pure JS/WASM (no native binary, so no risk of a lockfile that works on this Mac
   and breaks on Render's linux-x64), but adding them needs a `pnpm install`, which is the one operation on this
   repo with a history of breaking the Render build. Left for Manan to green-light rather than run mid-build.
   Everything else about the card works today: the page, the image, the method page, the privacy contract.

2. **Plugin marketplaces are git-shaped, not URL-shaped.** Clients generally expect to clone a repo; a plain
   HTTPS endpoint returning marketplace JSON works on some and not others. So the marketplace is built as the
   best-effort half of a pair — `pull_skill` writes a skill into the caller's directory and always works, and
   the Connect screen says which is which. If the URL route turns out not to work on the client Manan demos, the
   honest fix is to point the marketplace at a git remote rather than to pretend.

And one thing that could not be done from here at all: **nobody has loaded the running app.** The Render deploy
serves old code, and this device VM kills background processes between calls, so the server could not be booted
and clicked through. Two separate blank-page bugs on this repo were invisible to a full green suite and were
caught only by opening the deploy — so that check still has to happen, by hand, after the first deploy.
