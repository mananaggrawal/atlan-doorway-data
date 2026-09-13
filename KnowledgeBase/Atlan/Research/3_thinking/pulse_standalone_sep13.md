# Atlan Pulse, standalone — skill health only (13 Sep 2026)

Scope: Pulse spun out of the Atlan Challenge build as its own project. One job: you connect
Claude, Pulse audits your skills, you get a PDF and a card you can post. No sync product, no
registry, no governance surfaces.

---

## 1. The problems, mapped to what the product checks

Every line is tagged: [VERIFIED] primary source read · [CORROBORATED] 2+ independent ·
[ABSENT] checked and confirmed missing · [WEAK] surfaced but unproven.

### P1 — The always-loaded description tax → **token optimisation**
- [VERIFIED] Anthropic docs: `description` + `when_to_use` are **truncated at 1,536 characters
  in the skill listing "to reduce context usage"**; descriptions load into context every request,
  bodies only on invoke. `SKILL.md` under 500 lines.
- [VERIFIED] Anthropic's own `skill-creator`: **"Metadata (name + description): ~100 words always
  loaded."**
- [CORROBORATED] Two independent practitioner measurements: ~270–340 tokens per skill description,
  **~1,490 tokens every turn**, **11% of a 2.1M-token session spent on three skills that never
  fired** (removing them cut input tokens 11%); and a second author taking the same task from
  **$3.60 → $2.64 (-27%)** and 17m10s → 9m12s by trimming skill metadata — *"the single most
  expensive token you own."* Single-author blog benchmarks: direction solid, exact % indicative.
- Our own data: Manan's 19 account skills burn **2,380 listing tokens (119% of a 2,000 budget)**;
  Anthropic's 33 example skills, **3,138 (157%)**.
- **The unowned tension:** `skill-creator` tells authors to be *"a little bit 'pushy'"* and
  enumerate triggers (to stop under-firing) — which inflates the very budget the docs cap.
  [ABSENT] **Nobody publicly reconciles trigger recall against context cost.** That trade-off is
  Pulse's POV and belongs on `/method`.

### P2 — Trigger collision and wrong-skill firing → **dedupe**
- [VERIFIED] *"The description is 90% of the skill… Claude reads the list of available skills
  (just name + description) and picks."*
- [VERIFIED] The dominant failure is **under**-triggering, not over-triggering; authors hand-write
  negative "NOT for" clauses specifically to stop their own adjacent skills colliding.
- [VERIFIED] Anthropic's eval method targets exactly this: ~20 queries per skill, 8–10
  should-trigger and 8–10 **near-misses** — *"the most valuable ones are the near-misses."*
- Our own data: `linkedin-send-connect-request` ↔ `linkedin-send-dm` at 57% similarity;
  Anthropic's own `built-in-browser` ↔ `chrome-browser` at 56%.
- [ABSENT] **No existing tool checks cross-skill overlap or trigger collision.** Verified against
  both serious linters (below). This is the clearest open lane in the category.

### P3 — Unsafe third-party skills → **security + vulnerability**
- [VERIFIED] Snyk "ToxicSkills" (5 Feb 2026), 3,984 skills audited: **36% contain security flaws**,
  534 critical, **76 confirmed malicious payloads**, 8 still live at publication; *"91% of malicious
  skills combine prompt injection with traditional malware."* Static scanning hit **90–100% recall
  at 0% false positives** on confirmed-malicious.
- [VERIFIED] Anthropic's own guidance: *"install skills only from trusted sources… thoroughly audit
  it before use"* — the vendor is telling users to do manually what Pulse automates.
- [VERIFIED] `allowed-tools` frontmatter lets a skill execute commands **without showing the user
  a permission prompt** (Reversec Labs, 5 May 2026). Trivially static check: wildcard `Bash(*)`,
  `permissionMode: bypassPermissions`.
- [VERIFIED] Weaponised Claude Skill → MedusaLocker ransomware (Cato CTRL, 2 Dec 2025) — trojanised
  Anthropic's own GIF Creator skill with a hidden `post_save`.
- [VERIFIED] First real malicious MCP server shipped to users: `postmark-mcp` 1.0.16, 1,643
  downloads, silently BCC'd every email (Koi Security, Sep 2025).
- [VERIFIED] Tool poisoning + rug pulls (Invariant Labs) and line jumping (Trail of Bits): *"tool
  descriptions themselves are prime vectors for prompt injection"*, and an explicit recommendation
  to *"use automated scanning… to detect and filter suspicious tool descriptions."*
- [VERIFIED] Users are asking for this by name: claude-code issue #30727 — *"No way to verify
  publisher identity or code integrity / No security review or malware scanning."*
- **[VERIFIED] The honesty constraint:** SkillCloak (HKUST, Jul 2026) evaded **all eight tested
  scanners >90%** of the time by hiding payloads in skipped directories. Pulse must never claim a
  skill is *safe*. It reports what is visible in the text you ship. That sentence goes in the PDF.
- [ABSENT] No CVE exists for the SKILL.md format itself; no official OWASP entry names skills.
  Don't claim either.

### P4 — No enforced authoring standard → **improvement ("improvisation")**
- [VERIFIED] Two real linters exist. `agent-ecosystem/skill-validator`: frontmatter schema, naming,
  code-fence integrity, link resolution, keyword-stuffing, density metrics, token counts.
  `claudelint` skills validators: 43 rules, mostly schema + `skill-dangerous-command`.
- [ABSENT] **Neither checks cross-skill overlap, trigger ambiguity, or scores a library as a set.**
  Every linter grades one file. **Pulse grades your library.** That is the one-line wedge.

### P5 — No public proof point → **the card**
- [ABSENT] Zero competitors publish a "how good is this skill library" number.
- [VERIFIED, r/agency + ICP work] The publisher wants the *result* public and the *source* private.
  See §7 — this forces a storage decision, not just a UI one.

**Ranking for the landing page:** lead with P1 (measurable, has a dollar figure, nobody argues with
it), prove with P2 (nobody else can do it), escalate with P3 (the 36% number), close with P5.
P4 is the body of the report, not the hook.

---

## 2. "One click" — what it can honestly mean

Hard constraint: an MCP server **cannot read your local filesystem**. Skills live on the user's
machine; the server only sees what the agent hands it. So "everything happens automatically" is an
*agent* behaviour, not a server capability. Three delivery routes, ranked:

**Route A — the plugin (primary).** One command:
`/plugin marketplace add pulse.<domain>` then `/plugin install atlan-pulse`. A Claude Code plugin
bundles both the skills **and** the MCP server config, so install wires the connection and drops the
audit skills in one step. Then one sentence — *"audit my skills"* — and the skill discovers, pushes,
audits, and hands back a URL. Effectively: one install, one sentence.

**Route B — connector only (the true zero-install path).** User pastes the Pulse URL into
Connectors, OAuth, done. No skills installed — so ship the same instructions as **MCP prompts**,
which surface as slash commands (`/pulse:audit`). One text, two delivery mechanisms: `SKILL.md` for
plugin users, MCP prompt for connector users. Keep them generated from a single source file so they
cannot drift.

**Route C — `npx atlan-pulse` (no signup, top of funnel).** Writes the MCP entry, drops the skills,
runs locally, prints a score. Keeps the CLI's acquisition value without keeping the CLI product.

**Auth must not be a form.** Device-code / one-click browser approve. The user should never type a
password into a terminal or copy a token.

**The auto-run question.** The shipped skills currently *ask* which skills to audit before doing
anything — a deliberate privacy guard. "Everything happens automatically" conflicts with that.
Proposed resolution: **discover everything, show the list, run immediately, and say in one line how
to exclude** ("say 'skip X' and I'll re-run"). Non-blocking, still consented. Needs your call.

---

## 3. The engine — five dimensions, two layers

Layer A is deterministic and server-side; **only Layer A scores.** Layer B is model judgment done
by the skill inside Claude, every finding requiring an `evidenceQuote`, shown as "Reviewer notes"
and excluded from the score. That separation is what makes the number defensible.

| Dimension | Layer A (scored) | Layer B (reviewer notes) |
|---|---|---|
| **Token cost** | listing tokens vs 1,536-char / ~100-word budget, per skill and summed; body tokens vs 500-line rule; reference-file weight; "loaded but never invoked" tax | is this description as short as it can be *without* losing the near-miss? |
| **Dedupe** | description trigram + shingle similarity; body near-duplicate; name collision | intent overlap two skills describe in different words — the case measurement cannot catch |
| **Security** | credential shapes (never echo the value), `allowed-tools` breadth, `bypassPermissions`, fetch-and-follow instructions, declared egress, destructive tool + remote content combined | injection reachability: does fetched content actually reach a point treated as instruction? |
| **Vulnerability / supply chain** | referenced scripts and their imports, install/`curl | sh` lines, unpinned dependencies, dead or off-domain links, files referenced but missing | does the skill do something the description does not disclose? |
| **Improvement** | structure: missing description, no trigger phrasing, no owner, staleness by git date, >500 lines, no progressive disclosure when >300-line refs exist | the rewrite: propose a concrete shorter description and a concrete structural fix, quoting the line |

**Score** stays 0–100 with published weights on `/method`, sub-scores always shown, `engine v1`
stamped on every artifact, percentile suppressed under N=30 runs. Bump `ENGINE_VERSION` on any
change to a check, weight or threshold.

**New, and worth it:** a **$ estimate**. Listing tokens × turns/day × input price = "these skills
cost you ~$X/month before one of them fires." It is an estimate, must be labelled one, and it is the
single most quotable line in the report. Precedent exists ($3.60 → $2.64), so the mechanism is real.

---

## 4. The skills that do the audit — the part to get right

Pulse's credibility dies if its own skills are mediocre. Rules:

**4.1 One skill, not four.** Today there are four sibling skills whose descriptions all begin "Use
when the user asks for a … of their skills." That is exactly the `description-similarity` finding
Pulse ships. Collapse to **one `pulse-audit` skill** (~120 lines) plus reference files loaded only
when needed: `references/rubric-security.md`, `rubric-dedupe.md`, `rubric-tokens.md`,
`rubric-improvement.md`. Progressive disclosure is Anthropic's documented pattern and it drops the
always-on cost to one description.

**4.2 The description is the product.** Written to win near-misses in the fewest tokens — our own
stated position on the recall-vs-cost tension. Target: under ~60 words, naming the artifacts
("skill health", "audit my skills", "what do my skills cost", "are my skills safe", "duplicate
skills") and one explicit *not-for* clause.

**4.3 Evidence discipline, in the skill text.** Every Layer B finding must carry a quote from the
file. No finding without a quote is submitted. The skill must never read a matched secret value,
never restate deterministic findings (they are already in the report), and never invent a score.

**4.4 Fail loudly, degrade gracefully.** If skills are missing, say which. If the server returns
nothing, say so rather than narrating success.

**4.5 Dogfood as a CI gate.** Pulse's own plugin runs Pulse's engine in CI and **must score 100**.
A regression in our own skills fails the build. This is also the best slide in any deck.

**4.6 Eval it the way Anthropic says to.** 20 queries — 8–10 should-trigger, 8–10 near-miss — run
3× via `claude plugin eval`, on a held-out set. "We evaluated our own skills with the published
method" is a defensible claim and nobody else in this category makes it.

---

## 5. The PDF

Keep **one HTML template** as the source of truth for both the web report and the PDF — the
brand-styled report at `pulse/atlan-pulse-report.html` is already the design. Add print CSS
(`@page`, running headers, `break-inside: avoid`) and render with headless Chromium in the existing
Docker image. Generate async per `runId`, cache the file, serve it from the run page.

Alternatives considered: `@react-pdf/renderer` (pure JS, flows and paginates well, but a second
template that will drift from the web report); `satori + resvg + pdf-lib` (pixel-exact, already
planned for the card PNG, but hand-rolled pagination — wrong tool for a 20-page flowing document);
Typst (beautiful, but a third language in the stack). **Recommendation: Chromium in Docker for the
PDF, satori/resvg for the card.** Cost: ~+400MB image and a slower cold start, which was already
accepted as non-blocking.

**Report structure (~15–25 pages):**
1. Cover — score, band, skill count, engine version, date
2. The number that matters — listing tokens vs budget, and the $/month estimate
3. Executive summary — five dimension scores, the three things to fix first
4. One section per dimension — deterministic findings, then Reviewer notes, visibly separated
5. Per-skill appendix — one card per skill: tokens, flags, suggested description rewrite
6. Method — weights, thresholds, what each check does, `engine v1`
7. **What this does not prove** — static analysis is evadable (SkillCloak); a clean report is not a
   safety guarantee. Non-negotiable page.

---

## 6. The shareable artifact

Unchanged from the v2 plan and still right: a public card at a URL with a PNG OG image, score +
sub-scores + engine stamp, **no skill names, no skill content, ever**. `toPublicCard` stays the only
constructor, field-by-field, never a spread. The line to own publicly: **"share the score, you never
share the skill."** Second artifact once N accumulates: an aggregate *State of Claude Skills* report
— the first public benchmark in a category that has none.

---

## 7. The storage decision this forces

The IP-paranoia finding says the publisher will refuse anything that asks them to hand over the
skill file. So make it true in the architecture, not just in the copy: **ephemeral mode** — Pulse
analyses in memory and persists only findings, counts and content hashes, never bodies. Retaining
bodies buys re-audit-without-re-push and drift alerts; not retaining them buys the objection
handler. Recommendation: **ephemeral by default, retention opt-in per run.** Your call, and it is
the single decision with the most downstream code impact.

---

## 8. Brand

Reuse the kit already shipped in the report HTML: `--blue #2026D2`, `--cyan #62E1FC`,
`--pink #F34D77`, ink ramp `#141517 / #252530 / #3E4C59`, page `#F9F9FC`; Funnel Display (display),
Inter (body), JetBrains Mono (numerals and findings). Grid background, 1px rules, no shadows. The
open question is the lockup: as a standalone project, is this **"Pulse, by Atlan"** or an
independent mark that merely inherits the design language? Prior decision was no Atlan wordmark on
the public card; a spin-out is the moment to revisit.

---

## 9. Build shape

The audit engine is pure and already tested, so it ports unchanged. Two routes:
- **Carve-out** — strip sync/marketplace/access/trail/repo-browser from atlas. Fastest to a running
  thing, but inherits 7 packages, Node 22.x pinning and an `isolated-vm` native addon this project
  has no use for.
- **New thin repo (recommended)** — Node + Express + Postgres + MCP SDK + the copied
  `engine/` and its tests. Est. 3–4 days to a running shell because the hard part is already
  written and green. Leaves the challenge submission untouched in atlas, which is the point of
  calling this a separate project.

Name/domain still unverified at a registrar (`skill.health`, fallback `skillhealth.dev`) — check
before the name enters any copy.

---

## 10. Open decisions

1. **Standalone repo or carve-out?** (recommend standalone)
2. **"Pulse by Atlan" or independent mark?**
3. **Ephemeral by default, or retain skill bodies?** (recommend ephemeral)
4. **Auto-run everything, or confirm the selection first?** (recommend run-and-offer-to-exclude)
5. **Chromium in Docker for the PDF — accept the image size?** (recommend yes)
6. **Does the $/month estimate ship?** (recommend yes, clearly labelled an estimate)
