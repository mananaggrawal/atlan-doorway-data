# Google Search Demand — Semrush Keyword Pull

Pulled 2026-09-05 via Semrush (Keyword Analytics toolkit, US database). All volumes are monthly US search volume; trend arrays are Semrush's trailing-12-month relative index (0-1, most recent month last). CPC and intent are Google Ads figures, included as a proxy for commercial seriousness of the query, not as an ad-spend recommendation. [verified] = read directly off the Semrush API response today; nothing here is a secondary summary.

## 1. The literal category term has almost no search demand

| Keyword | Volume/mo | CPC | Status |
|---|---:|---:|---|
| agent registry | 140 | $11.29 | [verified] |
| ai agent registry | 50 | $7.53 | [verified] |
| aws agent registry | 110 | $14.72 | [verified] — despite AWS's Aug 31 2026 GA (see `market/registry_landscape.md`) |
| agent skill registry | 10 | $0 | [verified] |
| skill registry | 40 | $0 | [verified] |
| share claude code skills | 10 | $0 | [verified] |

Read: nobody searches the category name — not Atlan's, not AWS's. Consistent with `community/*` finding that this pain surfaces as GitHub issues and forum threads, not search-bar queries. A paid or SEO play built around "agent registry" as a keyword has essentially no organic audience to meet.

## 2. Where real, sizeable, growing demand actually sits

| Keyword | Volume/mo | CPC | Intent | Note |
|---|---:|---:|---|---|
| claude skills | 27,100 | $8.64 | commercial | [verified] |
| claude code skills | 8,100 | $5.26 | commercial | [verified] |
| anthropic skills | 3,600 | $9.76 | commercial | [verified] |
| context engineering | 3,600 | $3.30 | commercial | [verified] — one of the fastest-climbing terms in the whole pull |
| agent skills | 4,400 | $3.89 | commercial | [verified] |
| claude skills marketplace | 2,900 | $7.84 | commercial | [verified] — climbed hard the last 2 months of the trend window |
| mcp registry | 1,600 | $9.23 | navigational | [verified] — spike traces to Anthropic's own MCP Registry launch, see §4 |
| claude code plugin marketplace | 880 | $9.43 | commercial/nav | [verified] — spike traces to Anthropic's own Feb 2026 marketplace launch, see §4 |
| mcp server registry | 260 | $5.77 | informational | [verified] |

Read: real, meaningful, and in several cases still-climbing organic interest exists — just not filed under "registry." "Claude skills marketplace" in particular is a transactional query (people looking for a place to get/manage skills) growing month over month.

## 3. Actual developer query language is procedural, not product-category

| Keyword | Volume/mo | CPC | Status |
|---|---:|---:|---|
| how to add skills to claude code | 320 | $10.88 | [verified] |
| how to create custom skills for claude code | 170 | $0 | [verified] |
| how to use skills in claude code | 140 | $15.28 | [verified] |
| how to install skills in claude code | 110 | $9.57 | [verified] |
| how to use claude code skills | 90 | $8.95 | [verified] |
| what are claude code skills | 90 | $8.62 | [verified] |
| what is a claude code skill | 90 | $9.26 | [verified] |

Read: low-competition, low-volume-individually but numerous, unclaimed long tail. Nobody appears to be targeting this with content (ordinary consumer/how-to competition density in the Semrush data is low relative to CPC).

## 4. Two "registry"-adjacent spikes are Anthropic's own launches, not organic category pull

- "mcp registry" (1,600/mo) and "mcp server registry" (260/mo) both spike in the same recent window that Anthropic donated MCP to a new Agentic AI Foundation and stood up an official registry at modelcontextprotocol.io/registry/about. [reported — confirmed via WebSearch, not independently re-verified against Anthropic's press page with a pull date/quote the way `numbers/verification_log.md` claims are]
- "claude code plugin marketplace" (880/mo) spikes off Anthropic's own plugin marketplace launch (~Feb 2026, per contemporaneous coverage). [reported, same caveat as above]

Read: this is a competitive risk, not just a keyword note. The demand that exists for "a place to get/share skills" is increasingly being met by Anthropic's own first-party surfaces. Atlan's wedge needs to keep leaning on what AWS/Anthropic don't ship — usage, traces, evals, dependency graph, governance (see `market/registry_landscape.md`) — rather than on being "the registry," since the biggest platform in the space is now shipping that itself.

## 5. High commercial-intent enterprise/buyer language exists, but pulls toward the top-down motion

| Keyword | Volume/mo | CPC | Status |
|---|---:|---:|---|
| ai agent security | 880 | $28.21 | [verified] |
| ai agent governance | 320 | $15.79 | [verified] — hit its 12-month trend peak in the most recent month |
| agentic ai governance | 260 | $22.50 | [verified] |
| agent sprawl | 110 | $15.36 | [verified] |
| agentic ai risk management | 140 | $18.65 | [verified] |

Read: real buyer dollars behind CDO/security-team vocabulary (governance, risk, sprawl). This matches Atlan's existing ~$50K ACV top-down motion (see `atlan_product/`), not the bottom-up "distribution before sales motion" the brief asks for — worth naming as a future channel, not the Wave-1 bet.

## How this changes (and doesn't change) the plan

Does not change the channel bet: GitHub issues and r/claudeskills remain the highest-precision signal (`community/github.md`, `community/reddit.md`). Google volume for a feature this new is a lagging, low-n indicator, and most of the 8,100/mo on "claude code skills" is plausibly generic curiosity rather than acute sharing/governance pain specifically.

Does add one candidate second-wave lever to `../../3_thinking/path_to_100.md`'s repeating-loop model: a lightweight SEO-facing asset (e.g. a "State of Claude Code Skills" page, or a small public skills directory) targeting §2 and §3 terms above would meet real, growing, currently-uncontested organic traffic and could feed the same activation funnel without competing for the Wave-1 direct-outreach/Reddit channel.

Also adds one competitive-risk flag to carry into `market/registry_landscape.md` and the readout: Anthropic itself is now the fastest-growing source of "registry"-adjacent search demand, via its own MCP registry and plugin marketplace (§4).
