# Skill Health — development plan

Written 2026-09-06. Status: recommendation pending Manan's confirmation on the
sequencing question in §1.

## 1. The sequencing decision (read this first)

Manan asked for skill health as a feature **inside Atlas**, scoped Tier 0 + Tier 1,
as the Atlan **submission artifact**. Those three choices collide:

| Constraint | Source | Conflict |
|---|---|---|
| Outreach ships Tue 8 Sep, non-negotiable | submission_plan.md | Build lands Fri 11 at the earliest |
| Freeze Thu 10 Sep | submission_plan.md | Build lands after freeze |
| ~~Core understandable in 15 min~~ | the brief | **RESOLVED 2026-09-06** — hosted on Railway, a reviewer clicks a URL |
| Funnel Stage 1 = "install → solo scan" | path_to_100.md | Cannot ask 58 strangers + a subreddit to deploy Postgres |
| Tier 1 needs weeks of traffic | this plan, §4 | Fresh instance shows zeros; demoing it means fabricating data |

**Recommendation: one engine, two adapters.**

- The engine consumes a normalised `SkillFact[]` and emits `Finding[]`. It knows
  nothing about where facts came from.
- **Local adapter** (filesystem + `~/.claude/projects/**/*.jsonl`) → `npx skillscan`.
  Zero install, personal payoff, ships Tue 8, feeds the campaign. This is the
  submission artifact.
- **Atlas adapter** (Postgres + git) → the feature below. Same engine, same checks,
  same output shape. Accumulates real telemetry from day one of internal use, so the
  numbers are real by the time anyone asks.

Cost of doing both this way: ~15% over either alone, because the engine and every
check is written once. The "add a check live" moment in the session's final 10
minutes then works on both surfaces.

Everything below specifies the Atlas side.

## 2. Where it plugs in

New module `packages/core-backend/src/modules/skill-health/`, following the
existing convention: `skill-health.service.ts`, `.routes.ts`, `.contract.ts`,
`.tools.ts`, `index.ts`, `__tests__/`.

**Instrumentation point: `tool-helpers/tool-handler.ts`, inside
`createToolHandlerFactory`.**

Not `mcp.service.ts`. Skills are HTTP tool endpoints (`POST /agent/tools/get_skill`)
that MCP proxies to over the loopback bearer — instrumenting MCP would miss the
in-process agent and direct API-token callers, and would double-count if both were
instrumented. `createToolHandlerFactory` is the one wrapper every tool from every
caller path passes through, and it already holds `auth` (identity), `args` (skill
name), `sessionId`, and the try/catch around `handler(args, ctx)`.

Three rules for the recorder:
1. **It must never break a tool call.** Fire-and-forget, wrapped in its own
   try/catch. A telemetry failure that fails an agent's `get_skill` is worse than
   no telemetry.
2. **Buffer, don't write per call.** In-memory buffer flushed on size or interval.
   Copy the retention-sweep pattern already used by `session_ontology_touches`
   (`byTouchedAt` index + cutoff delete).
3. **Names and outcomes only, never content.** No arguments, no skill bodies. This
   is an enterprise product; "we log what your agents do" needs a defensible
   boundary. Gate it: `ATLAS_SKILL_TELEMETRY=off|counts|detailed`, default `counts`.

## 3. Tier 0 — computable today, no new ingestion

Sources already in the box: `git.service.ts` (history/blame), the per-file owner
model in `access-control.service.ts`, `pr_file_approvals`, `change_requests`,
`pr_merge_log`, and `manual-failure-memo.ts` (already tracks per-user tool failures).

Checks:
- **orphaned** — skill file with no owner
- **stale** — not modified in N days (default 180)
- **unreviewed** — landed without a change request
- **churning** — edited more than X times in the window
- **bus-factor** — one person owns more than Y% of the catalogue

Tier 0 works from commit one, which is what makes the page useful on a fresh
instance while Tier 1 is still filling.

## 4. Tier 1 — invocation telemetry

Migration, table `skill_invocations`:

    id            uuid pk
    user_id       fk users
    session_id    text
    tool_name     text          -- 'get_skill' | 'list_skills' | any tool
    skill_name    text null     -- from args when tool_name = 'get_skill'
    skill_version text null     -- git sha of the file at call time
    outcome       text          -- 'ok' | 'error' | 'denied'
    error_kind    text null
    latency_ms    integer
    invoked_at    timestamptz default now()

Indexes: `(skill_name, invoked_at)`, `(user_id, invoked_at)`, `(invoked_at)`.

Checks unlocked:
- **never-invoked** — in catalogue, zero invocations in window
- **concentration** — top-3 share of all invocations
- **failing** — error rate per skill, cross-referenced with `manual-failure-memo`
- **drift risk** — heavily invoked AND not modified in 6 months
- **wasted maintenance** — recently edited AND never invoked

**Cold start is real and must be stated in the UI, not engineered around.** The page
shows Tier 0 immediately and marks Tier 1 metrics as "collecting — N days of data"
until the window is meaningful. A `--seed-demo` path may generate synthetic
invocations for demos, clearly labelled, never mixed with real rows.

## 5. The headline metric

`buildGetSkillDef` inlines a live "Currently available skills: …" line into the tool
description every connected agent receives. So context cost is directly measurable
rather than estimated:

> Your `list_skills` description is **N bytes**. **M%** of it is skills nobody has
> invoked in 90 days.

Anchor from research (2026-09-05, verified): the Claude Code skill listing gets ~1%
of the context window, 1,536 chars per description. Cite it as the external
benchmark; the Atlas number is measured, not inferred.

## 6. Surfaces

1. `GET /api/skill-health/summary`, `GET /api/skill-health/skill/:name` — REST.
2. `packages/core-frontend/src/modules/skill-health/` — a page, following the
   existing frontend module pattern.
3. **MCP tool `skill_health`** — registered via `registry.registerExternalTool` /
   `registerInternalTool` like the skills tools. This is the important one: the
   evidence layer becomes queryable by the agent itself ("which of my skills are
   dead weight?"), which is how it gets used without anyone opening a browser, and
   it is the most on-brand thing an MCP-native product can do with this data.

## 7. Tests

The codebase carries 3,825 passing tests across 310 files; a module that ships
without tests will not match its bar. Minimum:
- recorder unit tests, including **"a telemetry write failure does not fail the
  tool call"** as an explicit case
- aggregation tests against a seeded database, one per check
- a route test and an MCP tool-definition test
- a Tier 0 test that runs against a real temp git repo (the workspace tests already
  do this — copy the harness)

## 8. Sequence

| Step | Work | Est |
|---|---|---|
| 1 | Engine + `SkillFact`/`Finding` contract, checks as pure functions | 1d |
| 2 | Local adapter → `npx skillscan` (**ships Tue 8, submission artifact**) | 1d |
| 3 | Tier 0 adapter: git + owners + change requests | 1d |
| 4 | Migration + recorder in `tool-handler.ts` + buffer/sweep | 0.5d |
| 5 | Aggregation service + the five Tier 1 checks | 1d |
| 6 | REST + MCP tool + frontend page | 1d |
| 7 | Tests | 0.5–1d |

Steps 1–2 serve the submission. Steps 3–7 are the Atlas feature and run after the
Thu 10 freeze, on their own clock.

## 9. Risks

- **Upstream collision.** Usage analytics is the most obvious gap in Hexis. If Bevel
  ships it, this becomes a diverging patch against a repo that took 826 commits in
  five weeks. Keep the module self-contained and the `tool-handler.ts` change to a
  few lines, so a rebase is cheap.
- **Every metric here sits on code we do not own.** See ATLAS-HANDOVER.md §licence.
- **Duplicate detection is deliberately out of v1.** Near-duplicate skill detection
  (lexical shingling or embeddings) is the most expensive check and the least
  certain. Atlan demos duplicate consolidation, so it matters — but it is v1.1.


## 10. Step 0 — Railway deploy (do this first)

Decided 2026-09-06: Atlas is hosted, not run locally. This resolves the
15-minute inspectability constraint in §1 and, more importantly, **starts the
Tier 1 telemetry clock** — point it at your own skills and connect your daily
agents this week, and the session demo shows measured numbers instead of an
empty page. That is the whole fix for the cold-start problem in §4.

### Prerequisites
- A **private GitHub repo for the knowledge base**. Atlas ships no git server;
  setup will not complete without a reachable remote. Create it first.
- A PAT with `repo` scope for that repo.
- Railway project with two services: managed **Postgres**, and the app.

### Build
Point Railway at the Atlas repo and build from **`Dockerfile`**, not
`docker-compose.yml`. Railway terminates TLS itself, so the compose file's
`caddy` service is unnecessary and only adds a failure mode.

### Environment
| Var | Value | Why |
|---|---|---|
| `ADMIN_EMAIL` / `ADMIN_PASSWORD` | yours | seeds the first account |
| `JWT_SECRET` / `SECRETS_ENC_KEY` | 32-byte hex each | required to boot |
| `DATABASE_URL` | `${{Postgres.DATABASE_URL}}` | Railway reference variable |
| `PORT` | Railway injects it | `CoreConfig` reads `PORT`; confirm the bind |
| **`TRUST_PROXY=1`** | **required** | see below |
| `PUBLIC_FRONTEND_URL` | `https://<railway-domain>` | issuer + link generation |
| `KB_REPO_URL` / `GIT_TOKEN` / `GIT_USERNAME` | the KB repo + PAT | KB clone |
| `KB_DIR_NAME` | `knowledge-base` | default is fine |

**`TRUST_PROXY` is the one that will bite.** `.env.example` documents it as
defaulting to 1 only when `DOMAIN` is set (for the bundled Caddy) — which does
not apply on Railway, so it arrives unset. Without it Express sees `http`,
`req.ip` resolves to the proxy (mis-firing the per-IP login rate limit), and the
OAuth issuer is built as `http://` — which the deployment-settings validator
rejects (`deployment-settings.service.ts:122` requires https) and MCP clients
refuse.

### Volume
Railway allows one volume per service. Mount it at the **workspaces** path
(`/app/apps/server/workspaces` in the compose layout). That is the git working
tree, and `file_locks` / `pending_commits` rows in Postgres point into it — wiping
it on redeploy leaves stale rows against a tree that no longer has the work.
`backups` and `spills` are derived; let them be ephemeral.

### Post-deploy verification — in this order
1. `GET /api/health` → 200
2. `GET /.well-known/oauth-authorization-server` → issuer is **`https://<domain>/`**.
   If it says `http://`, `TRUST_PROXY` is not taking effect — stop and fix before
   anything else, because every MCP connection depends on it.
3. Admin login returns a JWT
4. Complete the setup screen — the KB repo clones (where `GIT_TOKEN` problems show)
5. Connect a real agent over MCP and call `list_skills` — proves the OAuth round
   trip survives the proxy. This is the real smoke test, not the health endpoint.
6. Redeploy once and confirm the workspace volume persisted

### Hardening before the URL is shared
- **No open signup.** Lock `allowedEmailDomains`; provision the reviewer's account
  by hand.
- Set the KB's main branch **protected**, so visitors propose and owners approve —
  the same read-mostly shape upstream runs at `demo.bevel.software`. Config, not code.
- **Do not put real third-party credentials in the secrets vault on this instance.**
- `execute_command` is `internalOnly: true`, so external MCP agents cannot reach it —
  but any *signed-in* user can through the in-app chat agent. That is the reason
  signup stays closed, and it is not a tool-boundary problem to engineer around.

## 11. Multi-tenancy — decided NO (2026-09-06)

Asked directly; answered no. Recorded here so it is not relitigated.

**Cost in this codebase:** none of the 14 tables carries a tenant column, so it is
a schema plus query change nearly everywhere. `TENANT_ID` exists in
`core-config.ts` but as a single process-wide env value — one tenant per
deployment is the design intent. `kb-fs` clones one git working tree, so N tenants
means N clones with per-tenant disk and memory. The 1,819-line
`access-control.service.ts` would need a full re-audit for tenant leakage.

**Risk:** an isolation bug in a system holding other teams' proprietary skills and
an encrypted secrets vault is a breach, not a bug — shipped as a job application.

**Strategic:** touching every table and query permanently forks us from upstream on
the deepest axis, destroying the cheap-rebase property in §9 against a repo doing
826 commits in five weeks.

**And it buys nothing.** The funnel it would serve does not convert: a registry
requires migration before it shows value (the opposite of "time to value is a
scan"), and the "never train your replacement" finding says this audience will not
upload proprietary skills to a stranger's instance. Multi-tenancy would only let
more people experience an empty registry at once.

**Therefore the build is limited to:** one deployment, one KB repo (Manan's own,
real skills, real telemetry); the skill-health module at Tier 0 + Tier 1; reviewer
access by provisioned account. Explicitly excluded: multi-tenancy, open signup, and
any path that lets a stranger write into the workspace. Distribution stays with the
CLI — hosting solves demo-ability, not distribution.
