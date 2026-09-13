---
name: linkedin-lead-gen
description: Daily LinkedIn sourcing pass for AI-video content. Finds posts about AI video (generation, ad creative, avatars, dubbing, UGC ads, etc.), fully exhausts each post (every reactor + every comment) before moving to the next, checks a cross-run registry first so it never re-processes a post or re-adds a lead an earlier run already captured, and saves the run's leads into a native Google Sheet in Drive. This is a SOURCING-ONLY skill — it stops the moment leads are written to the sheet. It never sends connection requests, never DMs anyone, and never writes to HubSpot (HubSpot only gets touched once a lead actually engages back — see the companion linkedin-send-connect-request skill for why). A separate skill/agent consumes the sheet this produces and does the actual reaching-out. Use when Manan says "run today's LinkedIn campaign," "/linkedin-lead-gen," "find AI video leads," or references this campaign by name.
---

# LinkedIn AI-video content sourcing (daily, sourcing-only)

Finds new leads by surfacing LinkedIn posts about AI video, capturing who wrote them and everyone who engaged, and saving everyone found into a native Google Sheet. **This skill's job stops the moment leads are written to the sheet.** It does not check HubSpot for duplicates, does not send LinkedIn connection requests, does not DM anyone, and does not write any CRM records. A different, separate skill (`linkedin-send-connect-request`) owns turning this sheet into actual outreach — treat that as out of scope here even if it would be easy to bolt on.

**Why HubSpot stays untouched even after outreach starts:** Manan's standing rule is that a lead doesn't get created/touched in HubSpot until it shows real engagement — a reply to a connection note, a DM back, something that signals an actual conversation started. Until that happens, the Google Sheet *is* the system of record.

Runs once a day, but a single run should be scoped to as few or as many posts as it takes to **fully exhaust each post before moving to the next one** (see Step 2). Depth per post matters more than breadth across many shallow posts.

## Step 0 — Find or create today's output location

Output lives in Google Drive. Folder: **Frameo CRM › LinkedIn AI Video Agent Leads**. **Output format: one native Google Sheet per run**, titled `LinkedIn AI Video Agent Leads - YYYY-MM-DD` (append `(2)` for a same-day second run).

**Drive API note (re-tested 21 Aug 2026):** `mcp__Google_Drive__create_file` with `contentMimeType: "text/csv"` and **no** `disableConversionToGoogleType` flag now correctly auto-converts to a native Google Sheet. Pass `textContent` + `contentMimeType: "text/csv"` + `parentId` + `title`.

Sheet columns: `Name, Headline / Role, Person or Company, LinkedIn Profile URL, Engagement Type, Post Author, Post Topic, Post URL, Post Engagement, Date Captured, Notes`. LinkedIn Profile URL is required for every row.

## Step 0.5 — Build the do-not-repeat registry before searching anything

Before any search, pull the do-not-repeat registry from every existing sheet in the Drive folder (all prior runs/days): build two sets — already-processed **Post URLs** and already-captured **Lead URLs**, both deduped across every sheet.

- Post-level: a post already in the processed set has already been fully exhausted — skip it, unless it's clearly picked up meaningfully more engagement since, in which case flag it to Manan as a re-capture candidate rather than defaulting to it.
- Lead-level: when writing rows in Step 3, skip anyone already in the already-captured set from a *previous run*. Count them as "already a lead, skipped" in the report.

## Step 1 — Search LinkedIn for AI-video content

For each term, use **Top Match + `datePosted` past-week** (or past-24h for a tighter window) — not "Latest" alone. Search terms: "AI video", "AI generated video", "text-to-video", "video generation AI", "AI video ads", "AI ad creative", "AI avatar ad", "AI UGC ads", plus tool/product names (Sora, Runway, Veo, HeyGen, Synthesia, Pika, Luma AI, Kling AI video, Opus Clip, InVideo AI, Colossyan, Higgsfield AI) and hashtags (#AIvideo, #GenerativeAI video-filtered).

Check the first 1-2 pages per term. Skip ads, hiring posts, funding/PR announcements, and official company pages unless the page itself is a genuine prospect. Watch for the same post resurfacing across terms — recognize by post URL and queue it once.

Build a ranked queue (highest engagement first), then work through Step 2 one post at a time to completion before returning for more.

## Step 2 — Fully exhaust one post before moving to the next

Capture the *entire* reactor list and the *entire* comment thread per post before starting the next.

**2a.** Get the real post permalink via "..." → "Copy link to post" → the toast's "View post" link, then **call `navigate()` again with the identical URL** to force a hard reload (fixes a shadow-DOM issue that otherwise hides the page from JS queries).

**2b. Capture every reactor.** Click the reaction count (not the Like button, not an avatar). The reactions modal is paginated behind `button.scaffold-finite-scroll__load-button` inside `.artdeco-modal__content.social-details-reactors-modal__content` — loop: scroll the modal container to bottom, click load-more, wait ~1400ms, repeat until 3 consecutive clicks add nothing. To extract: build a `¦`-delimited string per record in-page, stash it in a hidden `<pre>` as the first child of a stable container, then read it back with `get_page_text` (much higher size limit than `javascript_tool`'s own return value), then remove the `<pre>`.

**2c. Capture every comment.** Comments are `<article>` elements; click any "Load more comments" button. Use the same hidden-element + `get_page_text` technique for large threads. Cross-check comments against the reactor list — comment-only engagers need their own row.

**2d.** If a post genuinely can't be fully captured, say so explicitly rather than shipping ambiguous partial data silently mixed with clean rows.

## Step 3 — Dedupe, write to the sheet, no approval gate needed

This skill never sends anything or creates CRM records, so it does not need to pause for approval before writing — the sheet is inert until a human or the outreach skill acts on it.

Dedupe by LinkedIn profile URL, both within this run and against the Step 0.5 registry. A person on multiple posts *this run* gets one row, with the other posts noted. A person already in a *previous run's* sheet gets no new row — count them in the report instead.

Use the Notes column for lightweight fit triage (low-fit vs. high-fit engagers) — a courtesy, not a gate.

## Step 4 — Checkpoint if interrupted

If a run doesn't finish its post queue, write a short checkpoint doc noting what's captured, what was in progress and how far, what remains, and any new gotchas — so a resumed session can pick up mid-post.

## Step 5 — Final report

Short summary: posts fully captured (with counts), posts skipped (already registered), new deduped people added, people skipped as already-a-lead, a link to the sheet, and anything needing a human look. No Slack post from this skill — `linkedin-slack-summary` owns that.

## Gotchas

- Sorting by "Latest" alone surfaces zero-engagement new posts — default to Top Match + past-week.
- Company pages, hiring posts and funding-announcement posts are usually not worth opening.
- The same popular post can resurface across search terms and days — recognize by permalink/author.
- No HubSpot involvement at all in this skill; no connection requests; no DMs; output is always a native Sheet, one per run; LinkedIn Profile URL is a required, dedup-key column.