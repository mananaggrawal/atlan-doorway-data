---
name: linkedin-send-dm
description: "Updates the deal-stage handling to the 31 Aug 2026 three-stage policy: a DM send now moves a deal from Sourced to Contacted if it hasn't already been moved (previously DMs never touched deal stage)."
---

# First pitch DM (HubSpot-driven)

The step after a connection request is accepted and before any reply has come back.

**Read `references/hubspot-model.md` first.** Note: as of 31 Aug 2026 the deal-stage table
there is stale (still shows the pre-31-Aug two-stage rule and mislabels stage `4119723761`) —
trust this skill's Step 3 below over that table until the reference doc is corrected.

**Scope boundary:**
- DMs only. No connection requests, no comments, no InMail to non-connections.
- **Every batch needs Manan's explicit go-ahead in chat**, with the actual draft text approved —
  not just the recipient list. A DM is a real message from Manan in his own voice; he signs off
  on the words. This holds regardless of any HubSpot write confirmation he's waived.
- One DM per person from this skill. Follow-ups and chase messages are a separate, deliberate
  decision — don't loop.

## Step 0 — Build the batch from HubSpot

Search CONTACT where `linkedin_status` EQ `Connected` (not `DM Sent`, not `Replied`) and
`hs_linkedin_url` HAS_PROPERTY. Retrieve name, `jobtitle`, `linkedin_connected_date`, and the
associated deal.

For each candidate, read the **deal's account research note** — that's where the dated trigger
and the Frameo use case live, and the DM is built from them. A DM written without opening that
note will be generic, which is the one thing that reliably fails here.

Skip: anyone whose deal is `Closed Lost` or `Parked`, anyone whose note flags them as departed,
and anyone connected so long ago that the trigger is stale — for those, refresh the trigger
first or tell Manan the account needs re-researching.

## Step 1 — Draft

Use the `outreach` skill for voice and the `frameo-pitch-insights` facts. Non-negotiables:

- Short. Two to four sentences. If it needs scrolling on a phone, it's too long.
- Open on **their** specific situation — the dated trigger from the account note, in their
  words where possible — not on Frameo.
- One concrete, low-pressure ask. No calendar link in the first DM unless Manan says otherwise.
- No hype adjectives, no "quick question", no fake familiarity, no attachments.
- Vary genuinely per person. Same-company personas must not receive near-identical messages —
  they talk to each other.

Present every draft to Manan as a table (name, company, trigger used, the full message text)
and get approval on the batch before sending any of it. Edits he makes to one draft usually
apply to the rest — carry the correction across and re-show.

## Step 2 — Send

Per person: open the thread, confirm you're 1st-degree and that no message already exists
(HubSpot can be stale, and Manan sometimes messages people himself), paste the approved text,
send, and confirm it appears in the thread.

Volume: 15–25 DMs per sitting, paced naturally. On any LinkedIn warning, restriction or
CAPTCHA, stop the batch immediately and tell Manan. Never attempt to solve or bypass a CAPTCHA.

If a thread already has messages in it, **do not send** — that person belongs in a follow-up
conversation, not a first-touch batch. Record it and raise it.

## Step 3 — Write to HubSpot

Chunk at 10 objects per call.

- Contact: `linkedin_status` = `DM Sent`, `hs_lead_status` = `IN_PROGRESS`,
  `linkedin_first_dm_date` = today.
- **Note on the contact quoting the DM verbatim.** This is the point of the whole exercise —
  the conversation lives in HubSpot, not in LinkedIn's inbox. Include the trigger it was
  built on so a later reply can be read in context.
- **Deal stage — DO move it here if needed (changed 31 Aug 2026).** By the time a DM goes out
  the deal should already be `Contacted` (the earlier connect-request send should have moved
  it), but if you find it still in `Sourced` — e.g. Manan connected with someone himself before
  this pipeline touched them — move it to `Contacted` (`4119723760`) now. A DM send is outreach,
  not engagement, so never move it past `Contacted`. Only `linkedin-check-connect-request`, on
  finding a genuine reply, advances it to `Engaged / Replied` (`4119723761`).
  (History: 24 Aug 2026 this skill was corrected to never move stage on send. 31 Aug 2026 Manan
  refined the model to three stages, so a send can now advance Sourced→Contacted but never
  further — don't revert to the 24–31 Aug never-move behavior.)
- Deal rollup: `linkedin_status` to the furthest-along state on the account,
  `linkedinfirstdmdate` to the earliest DM date there.
- One summary note per deal per batch.

## Step 4 — Report and hand off

Report: sent, skipped with reasons, and any thread that already had history (those need Manan's
judgment). Then say when to check for replies — `linkedin-check-connect-request` sweeps replies
as well as acceptances, and 3–5 days out is the usual cadence.

Never send a follow-up from this skill, however tempting the silence.