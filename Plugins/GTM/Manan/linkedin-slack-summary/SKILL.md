---
name: linkedin-slack-summary
description: Posts a daily status update for the AI-video LinkedIn lead-gen campaign to the #ai-video-linkedin-agent Slack channel — new leads sourced today and connection-request/DM activity (sent/pending/connected/dm'd), all stemming strictly from the sheets in the "LinkedIn AI Video Agent Leads" Drive folder, with a link to today's sheet. Scope is this LinkedIn campaign only — no HubSpot, no other outreach campaigns, no general deal/actionable review. This is a summary/reporting skill, not an action skill — it never sources leads, never sends connection requests or DMs, and never writes to the Sheet. Use when Manan says "push today's summary to Slack," "send the status update," "/linkedin-slack-summary," or references this by name. On first use in a session, or whenever Manan hasn't already confirmed the format, show the drafted message in chat and wait for his go-ahead before posting — don't assume approval from a previous day carries forward silently.
---

# AI-video LinkedIn campaign — daily Slack status update

Rolls up today's activity for **this one campaign** — `linkedin-lead-gen` (sourcing),
`linkedin-send-connect-request` (sends), `linkedin-check-connect-request` (status checks),
`linkedin-send-dm` (first pitch DMs) — into one status update, posted to
**#ai-video-linkedin-agent**. Everything stems from the sheets inside the **"LinkedIn AI Video
Agent Leads"** Drive folder — the entire system of record for this campaign.

Out of scope, deliberately: HubSpot (this campaign doesn't touch it at all), any other outreach
campaign or vertical, and general deal/actionable/anomaly review.

This skill only reads and posts to Slack. It never sources a lead, never sends a connection
request or DM, and never writes to the Sheet.

## Step 0 — Pin down "today"

Confirm the current IST (Asia/Kolkata) date/time with `date` rather than assuming.

## Step 1 — Gather what happened today

1. **Today's dated Google Sheet(s)** in the Drive folder — the primary source. Read the
   `Request Status` column for live counts (`Sent`, `Already Connected`, `Already Pending`,
   `Skipped - Company` / `Skipped - Low Fit`, `Connected`, `No Longer Pending - Not Connected`,
   or blank). Check `DM Sent (Y/N)` if present. Grab the sheet's real shareable link.
2. **Project docs** dated today that belong to this campaign specifically — for narrative
   detail the sheet alone doesn't carry.
3. If a whole category had no activity today, say so explicitly rather than dropping the section.

Don't fabricate a number — write "not reconfirmed this run" instead of guessing.

## Step 2 — Compose the message

Use Slack mrkdwn. Keep bullets to one line where possible. Structure:

```
:bar_chart: *AI-Video LinkedIn Campaign — Status Update ([Day, D Mon YYYY], as of [H:MM AM/PM] IST)*

*Sourcing*
• [new leads captured today, posts covered, or "no sourcing run today"]
• Sheet: <[sheet url]|[sheet name]>

*Connection requests*
• [sent today / total pending / total connected / no-longer-pending, or "no send or check activity today"]
• [batch awaiting Manan's go-ahead, if any]

*DMs*
• [first-pitch DMs sent today / total Connected leads still awaiting a DM, or "no DM activity today"]

*Flags*
• [partial captures, invite-cap standing, blocked sends, low-fit leads worth a second look — omit if nothing outstanding]

Sheet: [today's leads sheet link]
```

Adapt to what Step 1 actually found — a template, not a fill-every-blank form.

## Step 3 — Show the draft before posting (interactive runs)

Show the fully composed message (as a fenced code block) and wait for explicit go-ahead before
posting. Don't infer standing approval from a prior day's run.

**Exception — the scheduled 5:30pm IST daily run posts directly, no preview.** That standing
scheduled task exists specifically so it goes out unattended. An on-demand chat request goes
back to the normal preview-first behavior.

## Step 4 — Post to Slack

Post to **#ai-video-linkedin-agent** via `slack_send_message`, using the exact confirmed text.
Confirm back to Manan that it posted, with a link if the tool returns one.

## Gotchas

- Sheet links must point at the actual document (`/edit` URL), not the folder.
- List each sheet with a one-line label if more than one is relevant on a given day.
- Keep it to one post per run — each run reflects the delta/current state, not a repeat.