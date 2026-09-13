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
| Contacted | `4119723760` | **the prospect has engaged with us — replied, or otherwise responded.** Sending a DM or connect request does NOT move a deal here on its own; only a reply does. (Corrected 24 Aug 2026 per Manan, who found deals being moved to Contacted purely on send — "contacted" means engaged/replied, no one else. Only `linkedin-check-connect-request` moves this stage.) |
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

All five are **single-line text**, not dropdowns or date pickers. Write the literal string;
never convert dates to epoch millis.

| Property | Values |
|---|---|
| `linkedin_status` | `Sourced` · `Connect Request Sent` · `Connected` · `Connect Declined/Expired` · `DM Sent` · `Replied` · `No Connect Option` · `Disqualified` |
| `linkedin_connect_sent_date` | `YYYY-MM-DD` |
| `linkedin_connected_date` | `YYYY-MM-DD` |
| `linkedin_first_dm_date` | `YYYY-MM-DD` |
| `linkedin_last_reply_date` | `YYYY-MM-DD` |

Because they are text, HubSpot cannot filter them by date range — keep `hs_lead_status`
(a real enum, so lists and filters work) in lockstep:

| `linkedin_status` | `hs_lead_status` |
|---|---|
| Sourced | `NEW` |
| Connect Request Sent | `ATTEMPTED_TO_CONTACT` |
| Connected | `CONNECTED` |
| DM Sent | `IN_PROGRESS` |
| Replied | `OPEN_DEAL` |
| Connect Declined/Expired, No Connect Option, Disqualified | `UNQUALIFIED` |

Never write a date you don't actually know. Leave it blank and say so in the note instead.

## Deal rollup fields

Same names, on the Deal, also single-line text: `linkedin_status` (the **furthest-along**
state across that deal's contacts), `linkedinoutreachvertical` (`Real Estate` / `Education`),
`linkedin_connect_sent_date`, `linkedinconnecteddate`, `linkedinfirstdmdate`,
`linkedinlastreplydate`. Refresh the rollup whenever a contact under it changes state.

## Conversations

Every message — connection note, DM, and every reply received — is logged as a **Note on the
Contact** (`hs_note_body` HTML, `hs_timestamp` epoch millis string, associated to the CONTACT).
Quote the actual text sent or received; a status field alone is not a record of a conversation.
Add **one summary Note on the Deal per batch**, not one per message.

## Standing rules

- `manage_crm_objects` caps at **10 objects per call** — always chunk.
- Search by LinkedIn profile **slug** (`/in/<slug>`), not raw URL equality — the portal stores
  the same profile under `www.`, `in.`, `ae.` and `sa.` hosts inconsistently.
- Before creating a Contact, Company or Deal, search for an existing one. Duplicate records for
  the same account are a recurring trap here. Three known duplicate deal pairs are unresolved
  and flagged in notes: PhysicsWallah, T.I.M.E., Kalpataru.
- **Never fabricate an email address.** The sheets' emails were pattern guesses and were
  deliberately NOT migrated into the `email` field — they sit in contact notes marked
  UNVERIFIED. Verified emails come from Apollo when Manan turns it on; until then, leave
  `email` empty rather than guessing.
- Never trust HubSpot state at face value when the question is "did we actually reach them" —
  cross-check LinkedIn and Gmail before reporting outreach status.