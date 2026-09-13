# HubSpot data model — Real Estate & Education LinkedIn pipeline

**As of 24 Aug 2026, HubSpot is the single source of truth for the Real Estate and Education
verticals. The Google Sheets ("Frameo CRM — Real Estate/Education Targets v4 (feed)") are
retired. Never create a new tracking sheet for these verticals, and never read the old ones.**

Portal `246972404`. Manan's owner id `167115392`. Pipeline "Frameo Sales Pipeline" `2478746329`.

## Objects

**Company** — the target account. `industry` is the binary campaign tag:
`REAL_ESTATE` or `EDUCATION_MANAGEMENT`. Collapse every sub-vertical into these two; do not
get more granular even though HubSpot's enum offers finer options.

**Deal** — exactly one per company. Name: `<Company> – Frameo - Real Estate` or
`<Company> – Frameo - Education` (spelled out in full — two-letter codes don't surface in
HubSpot search). Owner `167115392`.

Stage ids:

| Stage | Id | Means |
|---|---|---|
| Sourced | `4196044499` | researched, no outreach yet — includes accounts we've sent a connect request or DM to but that haven't engaged back |
| Contacted | `4119723760` | **the prospect has engaged with us — replied, or otherwise responded.** Sending a DM or connect request does NOT move a deal here on its own; only a reply does. |
| Discovery done | `4119723762` | |
| Sample sent | `4119723761` | |
| Demo Done | `4119723763` | |
| Trial Active | `4119723764` | |
| Closed Won - Paid | `4119723765` | |
| Closed Lost | `4119723766` | |
| Parked | `4119733984` | stalled / deliberately deprioritised |

**Contact** — the stakeholder. Always set `firstname`, `lastname`, `jobtitle`,
`hs_linkedin_url`, `hubspot_owner_id`. Associate to **both** the Deal and the Company.

## LinkedIn tracking fields (Contact)

All five are **single-line text**. Write the literal string; never convert dates to epoch millis.

| Property | Values |
|---|---|
| `linkedin_status` | `Sourced` · `Connect Request Sent` · `Connected` · `Connect Declined/Expired` · `DM Sent` · `Replied` · `No Connect Option` · `Disqualified` |
| `linkedin_connect_sent_date` | `YYYY-MM-DD` |
| `linkedin_connected_date` | `YYYY-MM-DD` |
| `linkedin_first_dm_date` | `YYYY-MM-DD` |
| `linkedin_last_reply_date` | `YYYY-MM-DD` |

Keep `hs_lead_status` (a real enum) in lockstep:

| `linkedin_status` | `hs_lead_status` |
|---|---|
| Sourced | `NEW` |
| Connect Request Sent | `ATTEMPTED_TO_CONTACT` |
| Connected | `CONNECTED` |
| DM Sent | `IN_PROGRESS` |
| Replied | `OPEN_DEAL` |
| Connect Declined/Expired, No Connect Option, Disqualified | `UNQUALIFIED` |

Never write a date you don't actually know — leave it blank and say so in the note instead.

## Deal rollup fields

`linkedin_status` (furthest-along state), `linkedinoutreachvertical`, `linkedin_connect_sent_date`,
`linkedinconnecteddate`, `linkedinfirstdmdate`, `linkedinlastreplydate`.

## Conversations

Every message is logged as a Note on the Contact, quoting the actual text. One summary Note on
the Deal per batch.

## Standing rules

- `manage_crm_objects` caps at 10 objects per call — always chunk.
- Search by LinkedIn profile slug, not raw URL equality.
- Search for an existing Contact/Company/Deal before creating one.
- Never fabricate an email address — leave `email` empty rather than guessing.
- Never trust HubSpot state at face value — cross-check LinkedIn and Gmail before reporting outreach status.