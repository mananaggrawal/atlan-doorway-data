---
name: meta-ads-library-teardown
description: Pull a full breakdown of any brand's ads on Meta (Facebook/Instagram/Messenger/Threads) straight from the Ad Library — every active creative, deduplicated, broken down by format, platform, cadence, product/portfolio, messaging patterns, language and geography, plus a gaps-and-opportunities read and a polished shareable report. Use this whenever the user wants to look at, pull, analyze, audit, or "go through" a brand's Meta/Facebook/Instagram ads or Ad Library, wants a competitor ad teardown, asks what ads a brand is currently running, wants creative or messaging analysis of an advertiser, or needs ammunition for outreach/pitching based on what a prospect's live ad account reveals — even if they don't say "Ad Library" by name and just name a brand and ask to see their ads.
---

# Meta Ads Library Teardown

Pulls every active ad a brand is running on Meta, straight from the source, and turns it into
an analysis someone can actually act on — not a screenshot dump. The reason this is worth
having as a skill rather than redoing from scratch each time: the Ad Library's own UI only
shows ~10-20 ads before you're endlessly scrolling and manually reading cards, and its
headline "~N results" figure is inflated (it counts placement/text variants of the same
creative separately). There's a faster, more complete path — the same internal API the page
itself uses — and it's easy to get wrong on tool timeouts and rate limits if you're
improvising it. This skill documents the working recipe.

## What you'll produce

1. A full, deduplicated inventory of the brand's live creative on Meta
2. A breakdown by format, platform/placement, launch cadence, product/portfolio, recurring
   messaging devices, and language/geography
3. A "gaps & opportunities" read — always include this. The account tells you where it's
   weak just by what's *not* there (see step 5)
4. A polished HTML report, designed fresh for the brand's category (never reuse a generic
   template unchanged — see step 6)
5. Direct, working links to any specific ads you call out by name

## Prerequisites

You need a browser automation tool with JavaScript execution and page-text reading. Check
`ToolSearch` for whichever is available in this session — usually `mcp__claude-in-chrome__*`
(load `javascript_tool`, `get_page_text`, `navigate`, `tabs_context_mcp`, `computer`) or the
device-bridge equivalent `mcp__remote-devices__Claude_Browser__*`. Everything below refers to
`javascript_tool` and `get_page_text`; substitute the equivalent calls if you're on the other
tool family.

If an `Artifact` tool is available, load the `artifact-design` skill before building the
report in step 6 — it's how the report gets a real design pass instead of a generic look.

## Workflow

### 1. Find the advertiser's page(s)

Go to `https://www.facebook.com/ads/library/` (or navigate straight to a filtered URL — see
below), type the brand name into the search box, and read the **Advertisers** section of the
typeahead dropdown rather than just hitting enter on the keyword search. Keyword search
returns every page that *mentions* the brand — resellers (Amazon, regional distributors),
fan pages, unrelated namesakes. The Advertisers list is the actual pages.

A brand often runs more than one legitimate page — a global page and a country-specific
subsidiary are common (follower counts and "Games/toys"-style category tags help tell them
apart from resellers). Click into each real one you find; don't assume there's only one.
Note each page's follower count and its own "~N results" figure — you'll need to explain the
gap between that figure and your deduplicated count later.

Clicking an advertiser sets `view_all_page_id=<id>` in the URL — keep that page ID, you need
it for step 2.

### 2. Pull every active ad via the internal GraphQL endpoint

Don't try to get a complete picture by scrolling and reading `get_page_text` — it's slow, it
misses structured fields (dates, CTA type, exact platform list, clean link URLs), and you'll
run out of patience before you run out of ads. Instead, hook the page's own network calls and
drive its `ad_library_main` GraphQL query directly, paginating yourself. Full technique,
copy-pasteable code, and the gotchas (tool timeouts, output blocking, rate limits) are in
`references/extraction.md` — read it before you start pulling. In short:

- Capture one real request's `variables` payload by hooking `fetch`/`XHR` while the page loads
  more results (scroll or wait for lazy-load)
- Reuse that payload as a template, swapping `viewAllPageID`, `countries`, `first`, and
  `cursor`, generating a fresh `sessionID`/`collationToken` per page like the real UI does
- Run the pagination loop as a **backgrounded async function**, not a single `javascript_tool`
  call — a full pull runs longer than the ~45s tool timeout. Kick it off, then poll a
  `window.__prog` progress object across several follow-up calls
- Expect a rate limit (`"Rate limit exceeded"`, code 1675004) somewhere around 100-150 paged
  calls on a large account. When you hit it, wait several minutes before retrying — don't
  retry immediately, it won't succeed

Pull `activeStatus: "ACTIVE"` by default. If the user wants historical/paused ads too, rerun
with `"ALL"` and say clearly which set the report covers.

### 3. Extract, clean, and dedupe

For each result, keep: `ad_archive_id`, `start_date`/`end_date` (unix seconds — convert),
`publisher_platform`, `snapshot.display_format`, `snapshot.cta_type`, `snapshot.link_url`
(strip query params), and the copy (`snapshot.title`, `snapshot.caption`, `snapshot.body`) —
strip tracking params from any embedded URLs and collapse whitespace.

**Dedupe by `ad_archive_id`.** Meta's UI-facing "~N results" counts each placement/text
variant of the same creative separately (a `collation_count` field marks these) — your
deduped count is the real inventory size, and it will usually be meaningfully smaller. Always
report both numbers and explain the gap; it's a genuinely useful fact about how the account is
built, not just a technicality.

Two tool-specific gotchas, both covered in `references/extraction.md`: `javascript_tool`
refuses to return any string containing URL-shaped content ("[BLOCKED: Cookie/query string
data]"), so strip query strings *before* you stringify; and for large payloads, don't try to
return them directly from a `javascript_tool` call — write to a `<pre>` element in the page
and read it back with `get_page_text`.

### 4. Aggregate

Run `scripts/analyze_ads.py` on your cleaned JSON dump — it produces format/CTA/platform
counts, a launch-date cadence table, a per-product breakdown (count, format split, first/last
live date), and flags any non-Latin-script copy as a language signal. See the script's
docstring for the exact input shape.

Then **read the actual ad copy yourself** for recurring messaging devices — don't assume any
previous brand's specific devices (a loyalty-points mention, a named festival) apply to
whatever brand you're looking at now. Find *this* brand's own repeated patterns — how they
push a discount, whether they lean on a loyalty/rewards mechanic, how they handle seasonal
tie-ins, how much (if any) is creator/UGC-credited vs. brand-voice, whether they disclose
AI-generated video, whether they use comment-to-buy or other engagement-bait mechanics — and
count each one you actually find. If a device doesn't appear, don't invent it.

### 5. The gaps & opportunities read — always include this

This is the most useful part of the report and it comes from noticing absence, not presence.
Check each of these against what you actually found, and report only the ones that are
genuinely true for this account — don't force all of them, and don't claim one the data
doesn't support:

- **Language/geography coverage** — is there a reachable audience (a language, a market) the
  account writes zero copy for, despite clearly targeting that country?
- **Templated/copy-less inventory** — catalog/DCO ads running with placeholder-style copy
  (literal template variables, or generic autogenerated captions with no real hook) instead of
  a written ad
- **Concept reuse** — the same script, headline, or footage running across multiple distinct
  products, which means they can't tell "the product doesn't convert" from "the film is tired"
- **Unsupported long tail** — products/SKUs carrying exactly one creative with no variation to
  test against
- **Seasonal bolt-ons vs. real productions** — copy changed on top of old evergreen footage
  for a festival/sale, rather than anything actually shot for the occasion
- **Creator/UGC presence** — how much of the account (if any) is creator-whitelisted or
  UGC-styled vs. straight brand voice, and whether that's low for the category

### 6. Build the report

Load the `artifact-design` skill fresh before writing any HTML. `assets/report-template.html`
in this skill is a **structural reference**, not a template to fill in unchanged — it shows a
section order that's worked well (KPI strip → format mix → cadence → placement/destination →
product/portfolio → messaging patterns → language & geography → creator activity → gaps &
opportunities → filterable appendix table of every ad → caveats footer), but the palette,
type pairing, and voice need a real design pass for whatever category this brand is in. A
toy brand and a fintech brand should not produce visually identical reports — see the loaded
`artifact-design` skill for how to make that call.

Publish with the `Artifact` tool if the session has one (gets the user a private, updatable,
shareable link); otherwise write the file and hand it over with `SendUserFile`.

### 7. Direct ad links

Whenever you call out a specific ad by name or ID, give a working deep link:
`https://www.facebook.com/ads/library/?id=<Library ID>` — confirmed reliable, opens straight
to that ad's card with a "Link to ad" popup. Use this for any ad you're recommending someone
look at, reference, or use as a creative-brief starting point.

## Always disclose these caveats in the final report

- Meta's own "~N results" figure counts placement/text variants of the same creative
  separately — state your deduplicated unique count as the headline number and explain the
  gap
- Per-country delivery breakdown is only exposed by Meta for EU-targeted ads; geography for
  any other market is inferred from page identity, landing-page domain, currency/sale
  language, and platform targeting — not directly reported
- Spend and impression figures aren't published for ordinary commercial ads in most markets
  (India included) — only for political/social-issue ads. Don't claim you have spend data
  unless the account is one of those and Meta is actually showing it
- If a secondary or global page gets rate-limited before you finish paginating it, say so
  explicitly in the report and label those numbers a sample, not a complete count