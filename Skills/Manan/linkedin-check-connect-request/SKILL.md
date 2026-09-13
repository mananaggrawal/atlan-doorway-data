---
name: linkedin-check-connect-request
description: "Updates the deal-stage handling to the 31 Aug 2026 three-stage policy: this skill now advances Contacted → Engaged/Replied on a genuine reply (previously it advanced Sourced → Contacted, since sends used to leave deals in Sourced)."
---

# Connection-request acceptance check (HubSpot-driven)

Closes the loop on `linkedin-send-connect-request`. Read-only on LinkedIn, writes only to
Manan's own HubSpot records, so unlike the sending skills it can run unattended and on a
schedule.

**Read `references/hubspot-model.md` first.** Note: as of 31 Aug 2026 the deal-stage table
there is stale (still shows the pre-31-Aug two-stage rule and mislabels stage `4119723761` as
"Sample sent" — it's actually "Engaged / Replied") — trust this skill's Step 3 below over that
table until the reference doc is corrected.

## Step 0 — Pull the pending set from HubSpot

Search CONTACT where `linkedin_status` EQ `Connect Request Sent`, retrieving `firstname`,
`lastname`, `hs_linkedin_url`, `linkedin_connect_sent_date`, and the associated deal.

Also pull `linkedin_status` EQ `Connected` and `DM Sent` — those are the threads that might
have a **reply** waiting, which matters more than a new acceptance.

If Manan named a vertical, filter to it; otherwise check both.

## Step 1 — Read the acceptance state

Prefer the **connections list** over opening profiles one by one: LinkedIn's "My Network →
Connections", sorted by recently added, tells you in one pass who has accepted since the last
run. Cross-reference against the pending set by profile slug.

Then check **Sent invitations** (My Network → Invitations → Sent) for anything that has
disappeared from pending without appearing in connections — withdrawn or expired.

Only open individual profiles for the residue you can't resolve from those two lists. Profiles
are slow and the two lists usually cover everything.

Watch for: a profile whose name matches but whose **company has changed** since sourcing. That
person is no longer a lead for that account. Flag it rather than silently keeping them.

## Step 2 — Sweep for replies

For every contact at `Connected` or `DM Sent`, check the LinkedIn message thread. A reply is
the single most valuable signal this pipeline produces and it must not sit unrecorded.

Two known traps, both of which have bitten this pipeline before:
- LinkedIn's in-app message search returns "no results" for threads that do exist. A negative
  search result is not proof there's no thread — open or compose to the person directly, which
  shows real thread history.
- The conversation-list preview shows only the **last** message. A reply can be one message
  earlier than the preview suggests. Open the thread.

## Step 3 — Write to HubSpot

Chunk at 10 objects per call.

| Found | `linkedin_status` | `hs_lead_status` | Dates |
|---|---|---|---|
| Accepted | `Connected` | `CONNECTED` | `linkedin_connected_date` = the date shown, or today if the list only says "recently" |
| Still pending | unchanged | unchanged | unchanged — don't touch |
| Withdrawn / expired | `Connect Declined/Expired` | `UNQUALIFIED` | — |
| Replied | `Replied` | `OPEN_DEAL` | `linkedin_last_reply_date` = reply date |
| Changed employer | `Disqualified` | `UNQUALIFIED` | — plus a note naming the new employer |

**Log every reply as a note on the contact, quoting the message.** Paraphrase is not enough —
Manan needs the actual words to judge intent and to write the follow-up.

**Deal stage (changed 31 Aug 2026).** By the time this skill runs, the deal should already be
in `Contacted` (the send skills move it there). This skill is the *only* place a deal advances
past `Contacted`: on a genuine reply, move the deal to `Engaged / Replied` (`4119723761`). If
the reply asks for something concrete (a meeting, "send me details"), raise it to Manan as a
candidate for `Discovery done` — **propose the further stage change, don't make it
unilaterally.** An accepted connection request with **no reply** is *not* engagement — the deal
stays in `Contacted`, it does not advance to `Engaged / Replied`.
(History: 24 Aug 2026 this skill was tightened to only move Sourced→Contacted on a reply, since
sends used to leave deals in Sourced. 31 Aug 2026 Manan split that single jump into two steps —
send now moves Sourced→Contacted in the send skills, and this skill moves Contacted→Engaged/
Replied on reply. Don't revert to moving Sourced→Contacted here.)

**Deal rollup.** Refresh `linkedin_status`, `linkedinconnecteddate` and `linkedinlastreplydate`
on every deal touched.

## Step 4 — Report

Lead with **replies**, then acceptances, then withdrawn/expired, then the data-quality problems
(changed employers, mismatched profiles). Name anyone whose reply asks for something concrete —
those are hot and shouldn't be buried in a count.

Say which contacts are now ready for `linkedin-send-dm`.

Do not send anything from this skill, including a reply to someone who just replied. Drafting a
response is fine; sending needs Manan's explicit go-ahead.