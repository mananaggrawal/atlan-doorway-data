---
name: linkedin-icp-identification
description: >
  Sources new Real Estate and Education target accounts and their marketing stakeholders for
  Frameo using WebSearch (trade press, appointment announcements, funding and campaign news)
  rather than LinkedIn browsing, then writes everything straight into HubSpot — Company tagged
  by vertical, one Deal per account in the Sourced stage, and a Contact per stakeholder with
  their LinkedIn profile URL and an account research note. HubSpot is the only source of truth;
  this skill never creates or reads a Google Sheet. Use when Manan says "identify our ICP,"
  "find me new real estate / education accounts," "/linkedin-icp-identification," "who should
  we be targeting," "refresh the target list," or asks to expand either vertical's pipeline.
---

# ICP identification and account sourcing (Real Estate & Education)

Frameo (Dashverse's AI ad-creative production tool) runs two account-based verticals: **Real
Estate** and **Education**. This skill finds the accounts and the people inside them, and lands
them in HubSpot ready for `linkedin-send-connect-request` to work.

**Read `references/hubspot-model.md` before writing anything.** It defines the objects, the
stage ids, the LinkedIn tracking fields and the standing rules. Everything below assumes it.

Two things changed on 24 Aug 2026 and override anything you may remember from older runs:

1. **Sourcing is WebSearch-first, not LinkedIn-first.** Find the person through trade press and
   company sources, then resolve their LinkedIn profile — not the other way round. LinkedIn
   browsing has been unreliable and its search-results URLs are not usable outreach targets.
2. **HubSpot is written on every run, from the sourcing step onward.** The old rule ("don't
   touch HubSpot until the lead engages back") is retired for these two verticals.

The AI-video track (`linkedin-lead-gen`, engagement-sourced leads) is parked. Don't mix its
leads into these verticals.

## Step 0 — Scope the run

Confirm with Manan: which vertical (Real Estate, Education, or both), roughly how many new
accounts, and whether he wants net-new accounts or deeper stakeholder coverage on accounts
already in HubSpot. If he's unavailable and the run is scheduled, default to **one vertical,
10 new accounts**, and say so up front.

Then pull what's already there so you don't re-source it: search DEAL where
`hubspot_owner_id` = `167115392` and `dealname` CONTAINS_TOKEN `Estate` (or `Education`),
with `dealname` and `dealstage`. That list is the dedup key for accounts.

## Step 1 — What a good account looks like

Frameo sells volume ad-creative production: one brief re-skinned into many localised,
vernacular, city- or campus-specific video variants, without a production house per variant.
An account is a fit when it has **structural creative repetition** — many properties, campuses,
cities, or languages served by one marketing team.

**Real Estate.** Developers with multi-city or multi-project launch calendars (Indian
developers, GCC developers in Dubai/Abu Dhabi/Riyadh), property portals and brokerages running
always-on performance funnels, proptech and interiors brands, and flex-office operators. The
GCC angle is a specific wedge: large Indian-diaspora buyer bases that receive almost no
Indian-language creative.

**Education.** Test-prep and K-12 chains with hundreds of campuses and an annual admissions
plus results season, higher-ed groups with multi-campus intakes, edtech and upskilling brands
running paid acquisition, and corporate L&D platforms expanding into the Middle East or SEA.

**Titles worth sourcing**, in rough priority: CMO / Chief Brand Officer · VP/Head/Director of
Marketing · Head of Brand or Digital Marketing · Performance / Growth Marketing Manager ·
Marketing Manager. At founder-run or smaller accounts the founder may genuinely own the
creative budget — take them, but note it. Skip anyone whose remit is clearly not marketing.

**Skip**: accounts with no discernible paid-media or brand-campaign activity, and any account
where the only findable contact is a recruiter, an intern, or a franchise-level manager whose
scope is one branch.

## Step 2 — Find the accounts (WebSearch)

Search for accounts through evidence of live marketing motion, because that evidence doubles as
the outreach trigger. Productive query shapes:

- `"<vertical> company" India OR UAE "appoints" CMO OR "head of marketing" 2026`
- `<company> ad spend OR marketing budget OR campaign 2026`
- `<vertical> India funding round 2026 expansion`
- `<company> new campus OR new project OR launch 2026`
- trade press directly: afaqs, Exchange4media, Storyboard18, BestMediaInfo, Campaign India,
  Campaign Middle East, Entrackr, Inc42, Gulf Business, Khaleej Times

For every account, capture a **dated trigger** — an appointment, a funding round, an ad-spend
figure, a campaign, a campus or project launch, an expansion into a new market. A trigger with
a date and a source is the single most valuable thing this skill produces; it's what the
connection note and the first DM are built from. If no dated trigger exists, write the
structural case instead (e.g. "273 campuses, one admissions season") and label it as
structural, not as a trigger.

## Step 3 — Resolve the stakeholders

For each account, find 1–3 marketing stakeholders. Search the person by name plus company, and
resolve a **real LinkedIn profile URL** of the form `linkedin.com/in/<slug>`.

- A `linkedin.com/search/results/people/?keywords=...` URL is **not a profile**. Never record
  one. If the profile can't be resolved, record the gap in the account note instead — that gap
  is useful information, a fake URL is not.
- Corroborate the title from at least two sources where you can (LinkedIn's indexed title,
  the company site, trade press, theorg.com). Note single-source finds as such.
- **Check they still work there.** People change jobs constantly and this pipeline has been
  burned by it repeatedly. If press says they moved, don't create the contact — record the
  vacancy as a research gap and flag it to Manan.

## Step 4 — Write it to HubSpot

Per the model reference. In order, chunking every `manage_crm_objects` call at 10 objects:

1. **Company** — search by name and domain first. Create only if genuinely absent. Set
   `name`, `domain`, `industry` (`REAL_ESTATE` / `EDUCATION_MANAGEMENT`), `city`, `country`.
2. **Deal** — one per company, named `<Company> – Frameo - <Vertical>`, `pipeline`
   `2478746329`, `dealstage` `4196044499` (**Sourced**), `hubspot_owner_id` `167115392`,
   associated to the Company. Search first — an account may already have a deal under a
   slightly different name.
3. **Contacts** — `firstname`, `lastname`, `jobtitle`, `hs_linkedin_url`,
   `hubspot_owner_id`, `linkedin_status` = `Sourced`, `hs_lead_status` = `NEW`. Associate to
   **both** the Deal and the Company. Search by LinkedIn slug before creating.
4. **Account research note on the Deal** — the deliverable that used to be a sheet row. Include:
   segment, HQ, the dated trigger with its source, the Frameo use case, the outreach angle,
   the stakeholders mapped with their status, and every research gap (unresolved profiles,
   departed contacts, vacancies) with the reason.
5. **Deal rollup fields** — `linkedin_status` = `Sourced`, `linkedinoutreachvertical` = the
   vertical.

Manan has waived per-batch confirmation in past sessions but that does not carry across
sessions: show the proposed accounts and stakeholders as a table and get a yes before writing,
unless he waives it again for the current session.

## Step 5 — Report

Tell Manan: accounts created vs. already present, contacts created, and — most importantly —
**the research gaps**: accounts where no stakeholder could be resolved, and roles confirmed
vacant. Those are the follow-up work. Don't bury them under the success count.

Do not send anything. This skill stops at HubSpot. `linkedin-send-connect-request` owns the
first touch, and it needs Manan's explicit go-ahead.