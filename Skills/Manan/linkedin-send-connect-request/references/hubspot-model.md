# HubSpot data model — Real Estate & Education LinkedIn pipeline

See `linkedin-icp-identification/references/hubspot-model.md` for the full model (objects,
stage ids, LinkedIn tracking fields, standing rules) — identical content, kept alongside this
skill so it works standalone. Portal `246972404`, owner id `167115392`, pipeline `2478746329`.

Stage ids: Sourced `4196044499` · Contacted `4119723760` · Discovery done `4119723762` ·
Sample sent `4119723761` · Demo Done `4119723763` · Trial Active `4119723764` ·
Closed Won - Paid `4119723765` · Closed Lost `4119723766` · Parked `4119733984`.

`linkedin_status` values: `Sourced` · `Connect Request Sent` · `Connected` ·
`Connect Declined/Expired` · `DM Sent` · `Replied` · `No Connect Option` · `Disqualified` —
all single-line text fields, kept in lockstep with the real-enum `hs_lead_status`.

Standing rules: chunk `manage_crm_objects` at 10 objects; search by LinkedIn slug not raw URL;
search before creating to avoid duplicates; never fabricate an email; never trust HubSpot state
alone — cross-check LinkedIn and Gmail.