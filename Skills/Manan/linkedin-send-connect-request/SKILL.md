---
name: linkedin-send-connect-request
description: "Updates the deal-stage handling to the 31 Aug 2026 three-stage policy: a connect-request send now DOES move a deal from Sourced to Contacted (previously it deliberately left it in Sourced)."
---

# LinkedIn connection requests (HubSpot-driven)

The first real outreach step. Everything before this — ICP research, account and contact
creation — leaves no trace outside HubSpot. This does, so it carries stricter guardrails.

**Read `references/hubspot-model.md` first.** Note: as of 31 Aug 2026 the deal-stage table
there is stale (still shows the pre-31-Aug two-stage rule and mislabels stage `4119723761`) —
trust this skill's Step 3 below over that table until the reference doc is corrected.

**Scope boundary:**
- Connection requests only, with an optional note (300 chars). No DMs beyond that note, no
  comments, no follows. The first pitch DM after acceptance is `linkedin-send-dm`'s job.
- **HubSpot is written on every send.** The old "don't touch HubSpot until they engage" rule is
  retired for these two verticals — HubSpot is now the tracker, so a send that isn't logged is
  a lost record.
- **Every batch needs Manan's explicit go-ahead in chat first.** A connection request is
  semi-irreversible and visible to a third party. Get sign-off on the whole batch — who, how
  many, note or no note — before sending any of it. Sign-off on one person is not sign-off on
  the batch. This holds even if he waived HubSpot write confirmations for the session; those
  are different things.

## Step 0 — Build the batch from HubSpot

Ask which vertical, or infer it if unambiguous. Then search CONTACT with:

- `linkedin_status` EQ `Sourced` (this is the dedup key — any other value means this skill has
  already evaluated them, including a skip), and
- `hs_linkedin_url` HAS_PROPERTY, and
- associated to the companies or deals of the vertical in play.

Retrieve `firstname`, `lastname`, `jobtitle`, `hs_linkedin_url`, `linkedin_status`,
`hs_lead_status`.

Drop from the candidate list:
- Anyone whose `hs_linkedin_url` isn't a real `/in/<slug>` profile.
- Contacts on deals in `Closed Lost` or deliberately `Parked`, unless Manan says otherwise.
- Anyone whose account note flags them as departed or stale.

Prioritise by account: a deal in `Sourced` with a fresh, dated trigger beats one whose research
note is months old. If Manan wants a subset ("just the GCC developers", "the top 20"), narrow
before presenting.

Present the count and a sample of names/titles/companies to Manan and get confirmation
**before opening any profile**.

## Step 1 — Volume limits

LinkedIn restricts accounts that invite too fast. Treat as hard constraints:
- 15–25 requests per sitting on a standard account. If Manan asks for more, flag the risk
  rather than silently complying.
- Pace naturally between profiles; don't script a tight loop.
- On any warning, CAPTCHA or unusual friction: **stop the batch immediately** and tell Manan.
  Never attempt to solve or bypass a CAPTCHA.
- One batch per vertical per day by default.

## Step 2 — Send

Per person:
1. Open their profile from `hs_linkedin_url`.
2. Re-verify state on the profile itself — Connect / Pending / Message. HubSpot can be stale.
3. Click **Connect**.
4. Note or no note — **confirm this with Manan in Step 0, don't assume.** No note is the safer
   default at volume. If using a note: short, specific, built on that account's dated trigger
   from the deal's research note, no links, no pitch. Draft with the `outreach` skill's voice
   rules. Never send the same boilerplate to a batch — vary it per person, which the per-account
   triggers make natural anyway. Skip any trigger the research note flags as unverified.
5. Confirm the state actually flipped to **Pending**. A click is not a send.

If there's no Connect button (some profiles only offer Follow or InMail), that's
`No Connect Option` — record it and move on. Don't work around it.

## Step 3 — Write back to HubSpot

Chunk at 10 objects per call.

**Per contact:**

| Outcome | `linkedin_status` | `hs_lead_status` | Dates |
|---|---|---|---|
| Request sent | `Connect Request Sent` | `ATTEMPTED_TO_CONTACT` | `linkedin_connect_sent_date` = today |
| Already 1st-degree | `Connected` | `CONNECTED` | leave `linkedin_connected_date` blank if the date is unknown — don't invent it |
| Already pending from an earlier run | `Connect Request Sent` | `ATTEMPTED_TO_CONTACT` | leave the date blank if unknown |
| No Connect button | `No Connect Option` | `UNQUALIFIED` | — |
| Skipped as stale/departed | `Disqualified` | `UNQUALIFIED` | — |

**Note on each contact who was actually sent something** — quote the note text verbatim, or
state explicitly that it was sent without a note. A status field is not a record of what was
said.

**Deal stage — DO move it here (changed 31 Aug 2026).** `Sourced` (`4196044499`) means never
contacted at all. The moment ANY contact on the deal gets a connect request sent (or is found
already Connected/pending), the deal has been contacted — move it to `Contacted` (`4119723760`)
if it's still in `Sourced`. `Contacted` does not require a reply; it just means outreach has
gone out and we're waiting. Only `linkedin-check-connect-request`, on finding a genuine reply,
moves the deal further to `Engaged / Replied` (`4119723761`). An accepted-but-silent connection
stays in `Contacted`, not `Engaged / Replied`.

**Deal rollup** — set `linkedin_status` to the furthest-along state across that deal's contacts
and `linkedin_connect_sent_date` to the earliest send date on the account.

**One summary note per deal per batch**, not one per contact — who was contacted, with or
without a note, on what date.

## Step 4 — Report

Give Manan: sent, already-connected, already-pending, skipped with reasons, and anything that
looked wrong on LinkedIn (a profile that didn't match the HubSpot record, a title that had
changed, a CAPTCHA). Flag stale records for cleanup rather than quietly fixing them.

Then say when `linkedin-check-connect-request` should run — typically 3–5 days out.