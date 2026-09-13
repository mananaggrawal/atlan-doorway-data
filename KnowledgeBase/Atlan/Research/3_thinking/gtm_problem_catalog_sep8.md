# GTM problem catalog — every persona pain found in research, sourced
Compiled 2026-09-08, revised to mark evidence type on every line. Goal: a SMALL wedge -> distribution loop -> funnels into Atlan Pulse.

Evidence-type key used throughout:
- [VERIFIED PRIMARY] — a real quote/incident/number read directly from the primary source (a forum thread, a court filing, a live product page, an official stats body).
- [CORROBORATED] — reported consistently across 2+ independent secondary sources, but not read from the primary source ourselves.
- [VENDOR CONTENT] — from a company selling into or around this pain; directionally useful, treat claims/figures with caution, no independent verification.
- [INFERENCE] — a plausible connection we are drawing, not something anyone in the persona has stated. Flagged explicitly so it is never mistaken for voice-of-customer.
- [CONFIRMED ABSENT] — we went and looked (not just failed to find via a limited tool) and found nothing. An actual data point, not a gap.

## PART A — Persona-by-persona problem catalog

### 1. Individual BYO-agent engineers (original ICP)
**P1 — Skill drift/silent degradation as model versions shift.**
Persona: engineers running personal Claude Code skill libraries.
Source: round3_sep8 research, ICP-B pain-wedge writeup.
Evidence type: [INFERENCE] — structurally plausible, explicitly flagged in round3 as having "no named incident exists publicly, so we'd have to produce the first one."

**P2 — Truncation/discovery limits.**
Source: Anthropic's own documentation of the skill-listing context budget; `/doctor` and `/skill-doctor` shipped in Claude Code 2.1.261, 4 Sep 2026.
Evidence type: [VERIFIED PRIMARY] this is SOLVED, not a live problem — do not pitch it as one. Any claim of "your skills silently disappear" would be factually wrong as of this date.

**P3 — Versioning/handoff when an engineer leaves.**
Source: round2_sep8 research — git already handles this for engineers specifically (implicit in the round2 finding that AGENTS.md/portability issues vastly outweigh sharing issues on GitHub).
Evidence type: [INFERENCE] from round2's broader finding, not a direct engineer quote.

**P4 — Duplicate skills, nobody can find what exists.**
Source: agent_registry_product.md — Atlan's own internal experience building ~300 skills/40 agents in six months.
Evidence type: [VERIFIED PRIMARY] — this is Atlan's own stated origin story for the product, from their internal demo.

### 2. GTM/RevOps teams
**P5 — "Your agent has more permission than your rep."**
Persona: RevOps admin, HubSpot forum.
Source: round3_sep8 research, pain_chain writeup — "the HubSpot RevOps forum thread, May–Jul 2026, four named practitioners... a verified incident (a rep closed lost a deal that was already in closed won… unable to do it in the UI but the mcp connector had permissions)."
Evidence type: [VERIFIED PRIMARY] — read from the forum thread directly per round3 notes, one specific verified incident.

**P6 — Admin can't set connector-level permissions; P7 — bulk-update safeguards bypassed by looping.**
Source: same HubSpot RevOps forum thread as P5.
Evidence type: [VERIFIED PRIMARY], same thread, but only 4 named practitioners total — thin sample size, flagged as such in round3.

### 3. Marketing/creative agencies, dev shops, MSPs, boutique consultancies
**P8 — "Clients are starting to ask if they can just buy access to our AI workflows instead of hiring us."**
Persona: mid-sized agency owner, r/agency.
Source: read directly via Claude in Chrome, 8 Sep 2026, thread by u/tjrobertson-seo, r/agency, posted Jun 8 '26, 62 comments, 11 upvotes. Direct quotes pulled from the full comment tree.
Evidence type: [VERIFIED PRIMARY] — full thread read, not a secondhand summary. OP directly confirms in a reply: "Most do not, but it's not necessarily the cheap ones asking. We have clients paying $4,000/month who have asked."

**P9 — The agency community's own advice is DON'T expose the raw file.**
Persona: multiple agency owners replying in the same thread.
Source: same r/agency thread as P8. Specific quotes: u/Longjumping_Gur_3852 ("the second u sell access to the workflow u just turned ur moat into a sku," 5 upvotes at capture); u/RonnieDubbs ("don't tell people how the sausage is made" — describes a client reverse-engineering their workflow into an open-source project after a handoff); u/Upbeat_Opinion_3465 ("I would not sell the raw prompt library as the product").
Evidence type: [VERIFIED PRIMARY] — all direct quotes from the same read thread.

**P10 — No existing pricing model for licensing an AI workflow.**
Source: same r/agency thread — the OP's own stated problem ("I don't have an answer, it's just one of those open questions").
Evidence type: [VERIFIED PRIMARY].

**P11 — Consultancy variant: the moat is "partner-only knowledge," not generic AI output.**
Persona: strategy consultant (OP) + commenters, r/consulting.
Source: read directly via Claude in Chrome, 8 Sep 2026, thread "As a strategy consultant, Claude Code and Cowork scares the shit out of me," u/ConsultingBro97, r/consulting, ~1 month old at capture. Top comment quoted: u/CarbonHero — "if you need anything internal, hidden, within partner-only knowledge bases, or screenshot on a zoom call, they won't be indexed... the high-value information that really gets you ahead is all somewhat hidden and non-obvious." Also: "Easy to spot a Claude deck from a mile away — everyone is using it."
Evidence type: [VERIFIED PRIMARY] — full thread read directly. No evidence yet in this thread of the specific "client wants to buy our workflow" ask (that part is [INFERENCE] carried over by analogy from the agency thread).

**P12 — MSP variant: more open peer-sharing culture, but thin direct signal.**
Source: read directly via Claude in Chrome, r/msp search results, 8 Sep 2026 — "We Built an 'Awesome List' of n8n Nodes for MSPs" (56 upvotes), "Open-source automation tool for the community, looking for feedback" (27 upvotes), "Built an AI ticket triage workflow that standardizes escalation prep" (0 votes, 14 comments).
Evidence type: [VERIFIED PRIMARY] for the vote/comment counts themselves; [INFERENCE] that this generalizes to strong AI-skill-sharing behavior specifically, since the one directly on-point post scored almost nothing.

### 4. Data/analytics teams & boutique data consultancies
**P13 — AI agent with valid credentials deleted a production database and its backups in 9 seconds.**
Source: persona_deepdive_sep8 agent research, citing Zenity (zenity.io/blog), Eon (eon.io/blog), plus HackerNoon, Security Magazine, Jamf coverage of the "PocketOS/Replit" incident.
Evidence type: [CORROBORATED] — multiple independent outlets covering the same named incident, but not read from a court filing or the company's own postmortem directly; treat the "9 seconds" figure and "no exploit" framing as reported, not independently re-verified by us.

**P14 — Portable skill-sharing already happening organically in data/analytics.**
Source: github.com/nimrodfisher/data-analytics-skills — 31 skills, 345 stars, 69 forks, marketed "portable across any org," per persona_deepdive_sep8 agent (checked GitHub directly).
Evidence type: [VERIFIED PRIMARY] — GitHub stats are checkable facts, not a claim.

### 5. Finance & accounting firms
**P15 — "Versioned, not lost when somebody moves on."**
Persona: Tim Ross, Anthropic Finance AI Product Lead.
Source: persona_deepdive_sep8 agent research, citing CFOConnect.eu secondary writeup of Anthropic's own case study (undated, ~2025/2026).
Evidence type: [CORROBORATED] — quote attributed via a secondary write-up, not read from Anthropic's own primary source directly; the "75% of CPAs nearing retirement" and "84% of finance leaders report talent shortages" stats cited alongside were explicitly flagged by the researching agent as not independently re-verified.

**P16 — No organic sharing/client-buy-our-AI dynamic found in accounting.**
Source: persona_deepdive_sep8 agent — searched Gumroad, blogs, and attempted r/accounting/r/CPA/r/taxpros (blocked at the time via WebSearch tooling).
Evidence type: [INFERENCE from an incomplete search] at the time this was written — the direct-Reddit follow-up pass (which worked for r/consulting, r/msp, r/humanresources, r/LawFirm) was NOT yet run against r/accounting/r/CPA specifically. This is a genuine open gap, not a confirmed absence — flagged for a follow-up pass.

### 6. HR/recruiting & staffing agencies
**P17 — Recruiter playbook/pipeline IP dispute, but courts favored the recruiter.**
Source: AMN Healthcare, Inc. v. Aya Healthcare Services, Cal. Ct. App., Nov. 1, 2018 — via RecruitingDaily secondary coverage.
Evidence type: [CORROBORATED] — a real, citable, dated court case, read via a legal-industry blog's summary, not the court opinion itself.

**P18 — "Clients want our AI" pain already absorbed by white-label SaaS.**
Source: X0PA AI, Raffi, NextCommit, getwhitelabelats.com product pages, found by persona_deepdive_sep8 agent.
Evidence type: [VENDOR CONTENT] — these are the vendors' own marketing pages describing their product-market fit; take the existence of the category as real, treat any of their own stated traction numbers with caution (none were quoted).

**P19 — EEOC withdrew AI-hiring guidance in 2025.**
Source: Warden AI blog (2025/2026 content), persona_deepdive_sep8 agent.
Evidence type: [VENDOR CONTENT] reporting on a real regulatory fact — the withdrawal itself is a matter of public record (Warden AI's own business is built on bias audits, so they have a motive to emphasize this, but the underlying regulatory change is independently checkable, not something we re-verified against a primary government source here).

**P20 — Near-zero organic Reddit discussion.**
Source: read directly via Claude in Chrome, r/humanresources search "chatgpt OR claude prompt share," 8 Sep 2026 — top results were single-digit-vote, low-comment, unrelated threads.
Evidence type: [CONFIRMED ABSENT] — we went and looked with a working tool, not just failed to search.

### 7. Legal ops, paralegals, boutique law firms
**P21 — ABA Formal Opinion 512 requires client consent before self-learning GenAI touches client data.**
Source: persona_deepdive_sep8 agent, citing NCBEX Bar Examiner and UNC Law Library summaries of the 2024 opinion.
Evidence type: [CORROBORATED] — a real, named, dated formal opinion, read via two independent secondary summaries, not the ABA's own opinion text directly.

**P22 — LegalOn's "Prompt Workflows" is walled inside each firm's tenant by design.**
Source: Artificial Lawyer coverage, Jul 28 2026, cited by persona_deepdive_sep8 agent.
Evidence type: [CORROBORATED] — trade-press coverage of a real product launch.

**P23 — Zero Reddit results.**
Source: read directly via Claude in Chrome, r/LawFirm search "claude skills OR chatgpt workflow share," 8 Sep 2026 — literally zero results returned.
Evidence type: [CONFIRMED ABSENT].

### 8. Customer support / CX / voice-agent teams
**P24 — Agent logic lives in vendor consoles, not portable files.**
Source: persona_deepdive_sep8 agent, citing an eesel.ai guide describing org-managed, centrally-synced SKILL.md use, plus Anthropic's own Assembled case study (claude.com/customers/assembled).
Evidence type: [VENDOR CONTENT] (eesel.ai, Assembled/Anthropic case study) — both are vendor-authored, not independent practitioner testimony.

**P25 — Vendor-vs-vendor lock-in claims.**
Source: Lorikeet's "Migrating from Sierra AI" guide (lorikeetcx.ai), Agentmelt blog.
Evidence type: [VENDOR CONTENT] — Lorikeet is a Sierra competitor; the cited "4,200 engineering hours to migrate" and "150-200% of ACV" switching-cost figures are unsourced within the vendor's own post. Treat as marketing claims, not data.

**P26 — "53% of orgs have experienced AI agents exceeding permissions."**
Source: Isara.ai blog, citing a Cloud Security Alliance study (April 2026).
Evidence type: [VENDOR CONTENT citing a named study] — the underlying CSA study was not independently pulled and read; the blog itself concedes its own illustrative scenario is "hypothetical."

### 9. PMs / internal no-code-with-AI builders ("shadow AI")
**P27 — Non-engineers building ungoverned AI workflows, framed as a risk to detect/stop.**
Source: IBM, KPMG (Mar 2025 PDF), Netwrix, Torii, mrc's Cup of Joe (Mar 2026) — all cited by persona_deepdive_sep8 agent.
Evidence type: [VENDOR/ANALYST CONTENT] — a genre of security-vendor and analyst content, consistent across multiple independent publishers, but none are practitioner voice-of-customer.

**P28 — Internal prompt libraries rot from an ownership problem.**
Source: Will Kelly, willkelly.substack.com, Jan 22, 2026 — "60% unchanged in 90 days," "90% already dead."
Evidence type: [CORROBORATED-ish] — a single named, credible independent voice (20 years enterprise KM background per his own bio), not vendor content, but still one person's stated figures, not independently audited data.

**P29 — The specific viral mechanic (a PM re-instantiates their library at a new employer) has zero supporting evidence.**
Source: persona_deepdive_sep8 agent's own explicit search attempt and conclusion.
Evidence type: [INFERENCE, explicitly labeled unconfirmed by the researching agent itself] — flagged in the original report as "pure inference... requiring either original user research... or better-targeted search terms."

### 10. Sales engineers / presales (individual level)
**P30 — Individuals packaging and selling their own AI prompt libraries.**
Source: presales.gumroad.com ("Sales Engineer ChatGPT Prompt Guide," self-described "from Sales Engineers"), heystefanos.gumroad.com, novawolfsolutions — found and fetched directly by persona_deepdive_sep8 agent.
Evidence type: [VERIFIED PRIMARY] — these are live, purchasable products with practitioner-authored descriptions, fetched directly, not secondhand reporting.

**P31 — Governance/incident angle inside large SE teams.**
Source: persona_deepdive_sep8 agent's own search.
Evidence type: [CONFIRMED ABSENT — but only within this search pass] — no PreSales Collective Slack content or large-vendor SE team blogs were directly read; this needs its own follow-up before being called a confirmed absence at the level of P20/P23.

### 11. Freelance/independent performance marketers
**P32 — Stays a null result.**
Source: persona_deepdive_sep8 agent, re-testing the original round2/3 in-house-marketer null finding against freelancers specifically; cites AdsByAlvin (a Gumroad seller/agency owner, not a pure freelancer) as the closest positive counter-example found.
Evidence type: [INFERENCE from absence] — the agent explicitly flagged this pass as incomplete ("worth one more pass in freelancer-only communities... before fully closing it out").

### 12. Cohort-based education & accelerator programs
**P33 — Theoretically strong mechanic, zero confirmed cases.**
Source: persona_deepdive_sep8 agent, citing Correlation One's "50 Learners to 20,000" case study and enterprise Coursera "Claude Code in Action" licenses (Leidos, BMG, Orange, CSU pages, fetched directly).
Evidence type: [VERIFIED PRIMARY] for the case studies existing; [INFERENCE] that the viral mechanic itself would work, since both real analogs found explicitly teach frameworks rather than distributing a shared kit — the opposite of what's needed.

### 13. Open-source skill-repo maintainers & forkers (channel, not an ICP)
**P34 — Massive verified viral bases.**
Source: shields.io live badge data, pulled directly 8 Sep 2026 by persona_deepdive_sep8 agent: mattpocock/skills (~257k stars/19k forks), forrestchang/andrej-karpathy-skills (~211k stars), coreyhaines31/marketingskills (~48k stars/6.9k forks). obra/superpowers flagged explicitly as having CONFLICTING counts across sources (41k vs 283k) — unresolved.
Evidence type: [VERIFIED PRIMARY] for the three reconciled numbers (live badge API data); obra/superpowers specifically flagged [UNRESOLVED — do not cite a single number for this one without reconciling first].

**P35 — Every viral repo creates downstream ungoverned sprawl.**
Source: mcp.directory, "Matt Pocock's Skills: The npm Moment" — argues skills lack version pinning, dependency resolution, a security/audit pipeline, a deprecation mechanism.
Evidence type: [CORROBORATED] — an independent analyst's argument, well-reasoned and specific, but it is one publication's interpretation, not a practitioner survey.

**P36 — A live, funded competitor already sells this fix.**
Source: agentman.ai, full site teardown read directly via Claude in Chrome, 8 Sep 2026 (agentman.ai and agentman.ai/agentskills pages); funding/founder background via Google search results (LinkedIn snippet, a Glassdoor job-post snippet describing them as "seed-stage").
Evidence type: [VERIFIED PRIMARY] for the product's own stated features, pricing, and positioning (read directly from their live site). [CORROBORATED, thin] for "seed-stage" and the founder's prior exit — pulled from search-result snippets (LinkedIn, Glassdoor), not a primary funding announcement or press release; no actual funding amount or investor names were found for Agentman itself.

## PART B — Cross-cutting / structural problems (not persona-specific)
**P37 — The sharing hypothesis is dead as a demand signal.**
Source: round2_sep8 research — anthropics/claude-code#6235 (6,592 reactions) vs #28729 (151 reactions) vs #28327 (closed not_planned); Vercel's public eval (skills never invoked in 56% of test cases, zero improvement over baseline; a plain AGENTS.md index scored 100%).
Evidence type: [VERIFIED PRIMARY] for the GitHub reaction counts (checkable, public); [CORROBORATED] for the Vercel eval, cited from Vercel's own published writeup, not independently re-run by us.

**P38 — The wedge is not unclaimed.**
Source: atlan_research_findings (2026-09-05 research pass) — shareskills.ai, Tessl, JFrog Agent Packages, NVIDIA SkillSpector, AWS Agent Registry (GA 31 Aug 2026), Google's skill registry, ~12 Show HNs since Jan 2026; agentman.ai added 8 Sep 2026.
Evidence type: [VERIFIED PRIMARY] — these are named, checkable products/launches.

**P39 — The registry graveyard.**
Source: round3_sep8 research, supply_vs_demand writeup — "23 Show HNs between Dec 2025 and Sep 2026 scored ~47 HN points combined, median 1-2... Microsoft's own Agent Package Manager scored 1."
Evidence type: [VERIFIED PRIMARY] — HN point totals are public and checkable; the causal explanation (git being free, signup killing sharing) is [INFERENCE] drawn from the pattern, reasonable but not something any of the 23 projects' founders stated themselves.

**P40 — Truncation/versioning solved for free.**
Source: same as P2/P3.
Evidence type: [VERIFIED PRIMARY].

**P41 — Two prior stats were corrections.**
Source: atlan_research_findings — NVIDIA's own scan data (42,447 skills scanned, 26.1% with >=1 vulnerability, 5.2% likely malicious) vs. a separate, looser "nearly 1 in 4 could compromise a system" framing that conflated two numbers; a "552 malicious of 96,000" figure flagged as an unresolved vendor GitHub issue.
Evidence type: [VERIFIED PRIMARY] for NVIDIA's own published scan numbers; [CORROBORATED, low confidence] for the "552/96,000" figure, explicitly flagged in the original research as unusable without heavy caveat.

**P42 — Invite-based loops cap at ~4%; 40-70% requires forced use.**
Source: round3_sep8 research, sharing_mechanics_and_reach writeup.
Evidence type: [INFERENCE / TRIANGULATED] — explicitly stated in the original research as "No vendor publishes this metric; it's triangulated from OpenView's dev-tool referral share." This is the single most load-bearing number in the whole ICP argument and it is the least directly sourced — flagging prominently.

**P43 — Only three loop patterns survive when the object is proprietary.**
Source: round2_sep8 research, distribution_loops writeup — shields.io (1.2M READMEs, >1B requests/month), levels.fyi, ccusage+viberank.
Evidence type: [VERIFIED PRIMARY] for the shields.io/levels.fyi scale numbers (public, checkable); [INFERENCE] that these three categories are exhaustive — that's the research team's pattern-read across the loop archetypes studied, not a proven theorem.

**P44 — Atlas/Pulse as built is single-tenant with no use-only mechanism.**
Source: skill_health_feature.md / atlas_fork.md — our own build decisions ("DECIDED — multi-tenancy: NO"), and a direct feature comparison against agentman.ai's live "Use-only" access (P36).
Evidence type: [VERIFIED PRIMARY] — this is our own documented decision, plus a direct side-by-side against a competitor's shipped feature we read ourselves.

**P45 — No population/TAM data exists for the agency/consultancy ICP.**
Source: icp_v2.md, R1 risk — explicitly flagged as unresolved as of the ICP v2 writeup; partially addressed since via IBISWorld figures (118,542 digital ad agencies, ~203,000 web-design/software firms, 50,000+ MSPs, US, 2026) pulled via Google Search 8 Sep 2026.
Evidence type: [VERIFIED PRIMARY] for the three IBISWorld-sourced counts (pulled directly from search result snippets of IBISWorld's own published data, not the full report); still [OPEN GAP] — no combined/de-duplicated TAM specific to "5-80 employee, BYO-agent, repeatable-deliverable firms" has been computed.

## PART C — Wedge brainstorm (unchanged from prior pass; these are proposals, not sourced findings)
1. Skill Health Badge (shields.io mechanic) — proposal, grounded in P43's verified pattern.
2. "Ungoverned fork" checker for mattpocock/skills, karpathy-skills, marketingskills — proposal, grounded in P34/P35/P36's verified evidence.
3. "What /skill-doctor doesn't tell you" — proposal, grounded in P2/P40 (skill-doctor is real and shipped).
4. Skill Provenance Certificate for agencies — proposal, grounded directly in P8/P9/P10 (the r/agency thread's own stated blocker).
5. CI/PR bot for the viral public skill repos — proposal, grounded in P34's audience size; the Dependabot/Codecov playbook itself is [CORROBORATED] general SaaS-growth knowledge, not from this research.
6. Leaderboard / contribution-gated aggregate — proposal, grounded in P43 (verified pattern) and the status-anxiety visible in P8/P11 (both read directly).

All six are proposals synthesized from the sourced problems above — they are not themselves things any persona asked for, and should be labeled as our own idea when presented to Atlan, not attributed to research.
