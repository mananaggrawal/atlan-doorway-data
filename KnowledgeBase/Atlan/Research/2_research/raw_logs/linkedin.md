# Raw research trail — LinkedIn skills-governance scan
Session date: 2026-09-05. This is the audit trail behind `01_evidence/community_signals/linkedin.md` — every search, every post/profile opened, what was kept, what was thrown out, and why. Reconstructed from my own tool-call transcript, in the order it happened.

Tool notes up front, because they shaped what got captured:
- Reading was done two ways: `get_page_text` (fast, gives post body text and reaction/comment counts, no hrefs) and `read_page` (accessibility tree, gives hrefs for profiles/articles/companies but is slower and its `filter:"interactive"` mode truncated unpredictably on some pages — the full/default filter with a large `max_chars` and, on long pages, an `offset`, was the reliable way to get hrefs). `find` was used to locate a specific person's ref numbers on a page.
- I tried to get exact post permalinks (`/feed/update/urn:li:activity:...`) by clicking a post body (did nothing), then by opening a post's "Open control menu" → "Copy link to post" (this exists and presumably copies the link to the OS clipboard). Reading that clipboard requires `computer_read_clipboard`, which errored asking to enable full "computer use" / device control access. I judged that broader permission out of scope for a read-only LinkedIn scan and did not request it. Net effect: for any post that did NOT link out to the author's own Pulse article or an external blog, I have no exact activity-level permalink — only the author's profile URL and the exact search query the post surfaced under. This affects roughly a third of the filed findings (flagged individually below and in the findings file itself).
- One accidental exception: a repost inside the "Anthropic Claude" LinkedIn group had a `highlightedUpdateUrn` query parameter embedded in its group link, which exposed a real activity URN (`urn:li:activity:7501045268587581440`) for that one post. I did not otherwise encounter this.
- Relative timestamps ("4w", "3w", "1d", "18h", "2d") are LinkedIn's own display, not something I converted precisely — where the findings file says "posted ~18h before capture (≈2026-09-04)" that's me subtracting the displayed relative time from the capture date of 2026-09-05; it's an approximation, LinkedIn does not show exact publish time on the search-results card.
- Reaction/comment/repost counts below are point-in-time as viewed during this session and will have changed since.

---

## 1. All 19 searches, verbatim, in order

**1. Content search: `Claude Code skills team`**
URL: `https://www.linkedin.com/search/results/content/?keywords=Claude%20Code%20skills%20team`
3 posts read on page 1 (did not scroll/load more). Productive: 1 of 3 posts filed (token-bloat post). Mixed — mostly recruiter/explainer noise.

**2. Content search: `agent skills governance`**
URL: `https://www.linkedin.com/search/results/content/?keywords=agent%20skills%20governance`
3 posts read. Productive: 1 of 3 filed (Harendra Dogra, B3). One (Mehmet Suat Bilgiç repost) read in full but not filed as a numbered finding — too abstract/general-governance-philosophy, not skill-file specific.

**3. Content search: `SKILL.md`**
URL: `https://www.linkedin.com/search/results/content/?keywords=SKILL.md`
3 posts read. Productive: 2 of 3 filed (Murali K. → B4; Rajiv Selvaraj → B1). Good query.

**4. Content search: `AI agent registry`**
URL: `https://www.linkedin.com/search/results/content/?keywords=AI%20agent%20registry`
3 posts read. Productive: 1 of 3 filed (Sujit Dhanuka → B3). One (Ranjita M, containment architecture) read in full, judged adjacent-but-not-skill-specific, not filed as numbered finding.

**5. Content search: `context engineering skills`**
URL: `https://www.linkedin.com/search/results/content/?keywords=context%20engineering%20skills`
4 posts read. Productive: 0 of 4 filed. Dead end — results were campus recruiting, a leadership-coach repost chain, and two generic "prompt engineering vs context engineering" career-explainer Pulse articles, none touching team rollout or governance.

**6. Content search: `skills sprawl AI agents`**
URL: `https://www.linkedin.com/search/results/content/?keywords=skills%20sprawl%20AI%20agents`
5 posts read. Productive: 1 of 5 filed (Marius Bene, "Agent Sprawl" → B2). Rest was unrelated: a leadership-coach repost chain (Bernard Ablola → Dr. Wanda Walker), a fintech product-analyst comment, and a sponsored Bernard Marr/AWS infrastructure-race post.

**7. Content search: `internal AI skills library`**
URL: `https://www.linkedin.com/search/results/content/?keywords=internal%20AI%20skills%20library`
3 posts read. Productive: 0 of 3. Complete dead end — a student's IBM SkillsBuild certificate post, an academic librarian's peer-reviewed research article on AI use in STEM librarianship, and a "Google AI Essentials" course ad. Logged as a full null result.

**8. Content search: `Claude Code rollout engineering team`**
URL: `https://www.linkedin.com/search/results/content/?keywords=Claude%20Code%20rollout%20engineering%20team`
3 posts read. Productive: 1 of 3 filed as a numbered finding (Abhisheik Deo → B1/B2, the single best find of the whole scan), 1 more noted as vendor/competitive-landscape color but not filed (Codelitics), 1 irrelevant (Andrew Adams/Wireflow AI video demo). Best query of the session by finding quality.

**9. Content search: `agent governance versioning`**
URL: `https://www.linkedin.com/search/results/content/?keywords=agent%20governance%20versioning`
3 posts read. Productive: 0 of 3 filed as numbered findings. All three were generic enterprise-AI-governance content (an "Agentic AI Governance Engine" teaser, an inter-agent decision-ownership newsletter, a SAP/master-data-governance article) — none addressed skill-file versioning specifically, so logged as a null-ish/generic result.

**10. Content search: `AI coding agent adoption metrics`**
URL: `https://www.linkedin.com/search/results/content/?keywords=AI%20coding%20agent%20adoption%20metrics`
3 posts read. Productive: 1 of 3 filed (Ben Blackmore → B2). 1 more (Mumshad Mannambeth, KodeKloud) read in full and used only for the B5 engagement-pattern observation, not filed as its own numbered finding. 1 irrelevant (Ivee Bhuyan's personal ChatGPT/Copilot reflection).

**11. Content search: `Codex skills team`**
URL: `https://www.linkedin.com/search/results/content/?keywords=Codex%20skills%20team`
3 posts read. Productive: 0 of 3. Complete dead end / name-collision noise — a student hackathon team thanking a coding club literally named "Codex," an Asana job-ad repost, and a "seeking technical co-founder" post that only namedrops Codex/Claude Code/Cursor in passing. Logged as null.

**12. Content search: `agent skills security`**
URL: `https://www.linkedin.com/search/results/content/?keywords=agent%20skills%20security`
3 posts read. Productive: 2 of 3 filed (Aditya Goenka/NVIDIA → B3; Pethuraj M/AgentSeal → B3). 1 irrelevant (vamsi U, a training-course marketing post). Second-best query of the session.

**13. People search: `AI enablement`**
URL: `https://www.linkedin.com/search/results/people/?keywords=AI%20enablement`
10 profile cards read on page 1 of what the page showed as 10 total result pages (I did not page past page 1). Productive: this was the single best query for B5 persona evidence — 7 of 10 cards named and used, naming real enterprises (Eightfold, Mubadala, Toyota North America, Ford, Deloitte, World Wide Technology, Wood, Fluent Software).

**14. People search: `developer productivity AI`**
URL: `https://www.linkedin.com/search/results/people/?keywords=developer%20productivity%20AI`
10 profile cards read on page 1. Productive as a *negative* finding: none of the 10 carried a distinct "developer productivity" or "platform engineering" title — all were individual-contributor AI/ML/GenAI engineer titles. Used in aggregate for the B5 "this title doesn't exist the way AI Enablement does" observation; no individual named in the findings file.

**15. Content search: `shared skills library Claude Code team`**
URL: `https://www.linkedin.com/search/results/content/?keywords=shared%20skills%20library%20Claude%20Code%20team`
3 posts read. Productive: 2 of 3 filed as new numbered findings (John McCann/shareskills.ai → B1, the competitor find; Rizwan Saudagar → B1). The 3rd result on this page was Abhisheik Deo's same post resurfacing (already filed from query 8) — not double-counted. Best query of the session alongside #8 and #12.

**16. Content search: `skills registry overkill just use a repo`** (first pass, via `get_page_text`)
URL: `https://www.linkedin.com/search/results/content/?keywords=skills%20registry%20overkill%20just%20use%20a%20repo`
3 posts read. Productive: 1 of 3 filed (AI Alleyway marketplace-provenance post → B3, a strong find). 1 read but not filed (Raj Bonigala's "Claude Code skill map" — a per-build-stage tool leaderboard sourced from GitHub stars/skills.sh installs; interesting but a curation/directory piece, not a governance argument, so left out of the findings file). 1 irrelevant (John Kleist III/SkillsTX — this is HR "Skills Forensics" for human workforce credentialing, a different meaning of "skills" entirely, not AI agent skills).

**17. Content search: `agent skills are overengineered`**
LinkedIn returned a "Did you mean agent skills are over engineered?" spelling-correction banner. 3 posts read. Productive: 0 of 3, all irrelevant (a Malay/English hiring ad, a fullstack-engineer hiring anecdote about skill-matching being unrealistic, a generic "companies want average people cheap" complaint) — none about AI agents at all. Logged as null, run specifically to hunt for B4 counter-evidence and came up empty.

**18. Content search: `don't need a skills registry`**
URL: `https://www.linkedin.com/search/results/content/?keywords=don%27t%20need%20a%20skills%20registry`
3 posts read. Productive: 0 of 3 as direct AI-agent-skills-registry content, but 1 (Marcelo Calbucci, "you don't need Linear, branches, PRs, CI/CD, or staging until your product has meaningful traction") was kept and quoted in the B4 section of the findings file as the closest adjacent anti-process sentiment found, explicitly flagged there as general startup-process skepticism rather than a skills-registry-specific counter-argument. The other 2 were irrelevant human-career-skills content (a mechatronics engineer on certifications, a government skill-development-office post). Also run specifically to hunt for B4 and came up nearly empty.

**19. Content search: `skills registry overkill just use a repo`** (revisit — same query as #16, same URL, re-navigated)
URL: `https://www.linkedin.com/search/results/content/?keywords=skills%20registry%20overkill%20just%20use%20a%20repo`
Re-ran this exact query a second time, this time reading with `read_page` (accessibility tree) instead of `get_page_text`, specifically to recover the hrefs for AI Alleyway's company page, and incidentally also picked up Raj Bonigala's and John Kleist III's profile/article hrefs in the same pass. No new posts appeared beyond the same 3 from pass #16 — same three authors, same order, same content. Not a new finding, just a second read of the same page for link extraction.

Total: 19 navigations, all against `linkedin.com/search/results/{content|people}/`. No rate limiting, no login wall, no security checkpoint at any point.

---

## 2. Every post and profile read, in order, filed or not

Format per line: **Name — title/company (query it appeared under) — one-line note — FILED (bucket) / NOT FILED (why)**

1. **Keerthan Gowda S** — AI Consultant at MHP-India (`Claude Code skills team`) — CLAUDE.md grew past 400 lines, billing every turn, cites a 45-person team's token-audit (14% user prompts) — **FILED, B2 (#5)**
2. **Rajat D.** — Strategic Hiring Partner for GCCs/Product Companies (`Claude Code skills team`) — recruiting ad for a "Claude Code User" $80-100/hr contract role — **NOT FILED** (recruiting noise, no governance content)
3. **Archita Suneja** — Founder, Quanta Auto AI (`Claude Code skills team`) — Medium explainer on Claude Agent Skills feature (progressive disclosure, skills vs CLAUDE.md/MCP/sub-agents) — **NOT FILED** (generic feature explainer, no team/governance angle)
4. **Ryan Moeller** (reposting) / **Mehmet Suat Bilgiç** — "AI Governance Architect," Balıkesir, Türkiye (`agent skills governance`, inside the "Anthropic Claude" LinkedIn group) — long philosophical post on governance as "executable system architecture," the "Verification Cost Paradox" — **NOT FILED** (too abstract/general, not skill-file specific; kept as background color only)
5. **Osama Hussain** — Hiring Talent @ Infosys (`agent skills governance`) — Infosys Consulting hiring ad, "Principal Consultant – AI Consulting" — **NOT FILED** (recruiting noise)
6. **Harendra Dogra** — AI Security Consultant, Secure Axis Labs (`agent skills governance`) — "10 Red Flags in AI Sec Operations (2026)" incl. 21%-visibility stat — **FILED, B3 (#12)**
7. **Murali K. (Kallem)** — Data & AI Executive, CDO/CAIO Advisor (ex Salesforce/Box/Toyota/GE) (`SKILL.md`) — "SKILL.md Trap": natural language isn't a deterministic state machine, 98% success = failing grade — **FILED, B4 (#13)**
8. **Hassan Bin Tila** — Autonomous & Open Cloud RAN Architect (`SKILL.md`) — SKILL.md as "operating manual" vs 500-word prompt templates, generic explainer — **NOT FILED** (no governance/team angle)
9. **Rajiv Selvaraj** — B2B partner/service-connector (`SKILL.md`) — "Claude Code Skills, explained like a beginner course," 343 reactions/54 comments — **FILED, B1 (#4)**
10. **Ashuta Kaul** — Talent Acquisition Specialist, EU hiring (`AI agent registry`) — GenAI/AI Engineer hiring ad, ThoughtLabs Belgium — **NOT FILED** (recruiting noise)
11. **Sujit Dhanuka** — AI Scientist & Mentor (`AI agent registry`) — registry/gateway/code-scanner all miss unauthorized tool-permission expansion — **FILED, B3 (#10)**
12. **Ranjita M** — Solution Architect, InfoVision Labs (`AI agent registry`) — "AI agents need containment by architecture," references a "2026 OpenAI containment incident" — **NOT FILED** (adjacent — containment/access-control architecture broadly, not skill-file specific; considered but left out)
13. **Tod N.** — "Creative problem solver" (`context engineering skills`) — career-advice post recommending Missy Webb — **NOT FILED** (irrelevant)
14. **Missy Webb** — Engineering Manager, Y-12 National Security Complex (`context engineering skills`) — campus-recruiting repost ("ONE" program via Handshake) — **NOT FILED** (irrelevant, campus recruiting)
15. **Ravi Sanchala** — CEO @ KENKODE (`context engineering skills`) — "prompt engineering is becoming outdated" career-skill explainer — **NOT FILED** (generic, not governance)
16. **Jayesh Vagh** — FEXP @ Handshake AI (`context engineering skills`) — "we are about to overcomplicate AI engineering" context-engineering explainer — **NOT FILED** (generic, not governance)
17. **Marius Bene** — Executive Director, Future WorkForce Global (`skills sprawl AI agents`) — "Agent Sprawl" newsletter, cites Gartner 10:1 agents-to-people by 2028 — **FILED, B2 (#6)**
18. **Bernard Ablola** — "creativity is a weapon" (`skills sprawl AI agents`) — repost recommending Dr. Wanda Walker — **NOT FILED** (irrelevant)
19. **Dr. Wanda Walker** — Leadership Coach & Consultant (`skills sprawl AI agents`) — "Flourishing Leadership" newsletter on human skills vs automation, 365 reactions — **NOT FILED** (about human leadership skills, not AI agent skills — a keyword-collision result)
20. **Maryam Ghodratabadi** — Product & Business Analysis, Fintech (`skills sprawl AI agents`) — comment on AI-infrastructure-race theme — **NOT FILED** (irrelevant)
21. **Bernard Marr** — Author/Keynote Speaker/Futurist (`skills sprawl AI agents`) — sponsored AWS content, Thomson Reuters CTO interview on infra modernization — **NOT FILED** (sponsored, generic infra, not skills-specific)
22. **Saniyamirza Shaik** — Student, Vaagdevi Engineering College (`internal AI skills library`) — personal IBM SkillsBuild AI Fundamentals credential post — **NOT FILED** (irrelevant)
23. **Neil Grimes** — Education & Curriculum Materials Librarian, William Paterson University (`internal AI skills library`) — peer-reviewed research on STEM librarians' AI use — **NOT FILED** (irrelevant, library science)
24. **Business Training Media, Inc.** (company) (`internal AI skills library`) — "Google AI Essentials" course ad — **NOT FILED** (course marketing)
25. **Codelitics** (company page) (`Claude Code rollout engineering team`) — vendor pitch: 30-min fit call, one-repo pilot AI-coding measurement layer, mentions Claude Code/Cursor/Codex/Copilot — **NOT FILED as numbered finding** (kept as vendor/competitive-landscape color only)
26. **Abhisheik Deo** — Hands-on Architect, 19+ yrs, runs Claude Code + Codex across 20-engineer team (`Claude Code rollout engineering team`) — seats-vs-artefacts, 1,400 weekly skill invocations / 8 skills = 78% load — **FILED, B1 (#2)** — best single find of the scan
27. **Andrew Adams** — "Helping Creative Teams Ship Studio Quality Content... Wireflow AI" (`Claude Code rollout engineering team`) — video-generation workflow demo built "in Claude Code" — **NOT FILED** (creative/video-AI demo, not governance)
28. **Srinivas Bommena** — Chief AI Officer @ TechvestGlobal (`agent governance versioning`) — "How to Build Agentic AI Governance Engine" newsletter teaser — **NOT FILED** (generic governance engine, not skill-file specific)
29. **Koushik Lahiri** — Principal Pre-Sales & Client Engagement, Fernsquare (`agent governance versioning`) — "AI Governance Has a Blind Spot" — inter-agent decision ownership — **NOT FILED** (not skill-file versioning)
30. **intelligentMDG** (company page) (`agent governance versioning`) — "What Happens When an AI Agent Creates Your Master Data Record?" SAP MDG governance — **NOT FILED** (master-data governance, not skills)
31. **Ivee Bhuyan** — DotNet/AI/Azure/Product Management (`AI coding agent adoption metrics`) — personal reflection on ChatGPT/Copilot use, embeds a LinkedIn Learning course ad — **NOT FILED** (generic AI-agents-101 reflection)
32. **Ben Blackmore** (profile handle: benripkens) — CTO @ Dash0 (`AI coding agent adoption metrics`) — "several thousand agents in production" = seat count; building "Darkplane" adoption metric — **FILED, B2 (#7)**
33. **Mumshad Mannambeth** — Founder & CEO, KodeKloud (`AI coding agent adoption metrics`) — AI-code-quality stats (1.7x more issues, 91% longer review, 10x vulnerabilities at 4x speed), 456 reactions — **NOT FILED as numbered finding** (about AI code quality/DevOps broadly, not skills governance; used only for the B5 engagement-pattern observation)
34. **Alok Singh Tomar** — IT student (`Codex skills team`) — hackathon project thanking a coding club named "Codex" — **NOT FILED** (name collision, irrelevant)
35. **Elaine Colenbrander** — Creative Director/Writer (`Codex skills team`) — Asana Brand Designer job-ad repost — **NOT FILED** (irrelevant)
36. **Prateek Midha** — Marketing/Branding (`Codex skills team`) — "Seeking a Technical Co-Founder/CTO," namedrops Codex/Claude Code/Cursor once — **NOT FILED** (co-founder-search ad, not governance)
37. **Aditya Goenka** — Founder @ Be10x (`agent skills security`) — NVIDIA scanned 42,000+ skills, ~1-in-4 risky; built "SkillSpector" scanner — **FILED, B3 (#8)**
38. **vamsi U** — Digital Marketing Intern, Visualpath (`agent skills security`) — "what skills to become an AI agent developer" training-course marketing — **NOT FILED** (lead-gen content)
39. **Pethuraj M** — offensive-security practitioner, builder of "AgentSeal" (`agent skills security`) — security toolkit: red-team prompts, MCP-poisoning detection, skill-file scanning — **FILED, B3 (#9)**
40-49. **People-search cards, query `AI enablement`** (10 cards, page 1 only): Cory Eno (Eightfold — Claude enablement, **FILED B5**), Aidan Millar (Mubadala — $100M transformation, **FILED B5**), Shane Kelly (World Wide Technology, **FILED B5**), Kashish Khemka (Wood, **FILED B5**), Ben Gold (Toyota North America, **FILED B5**), Sage Franch (Fluent Software / CLAIR AI Governance Association, **FILED B5**), Ben Ortega (Backbase, VP Strategic AI Enablement — conversational-AI sales focus — **seen, NOT individually named** in the findings file), Srinivas P (Deloitte, **FILED B5**), Karthikeyan Rajendran (Ford, **FILED B5**), Mauro Spigolon (Eva Miller — smaller company — **seen, NOT individually named**).
50-59. **People-search cards, query `developer productivity AI`** (10 cards, page 1 only): Dhruv Gajaria (Microsoft), Sanyasirao Dharmuktula (ServiceNow), Vishnupriya kumaar (Prodapt), George Bocancios (Mojar AI, co-founder), Madeeswaran K. (JetBrains), Swagath Suvarna (Clarivate), Kshitij Agarwal (Bito — building an AI Architect/Code Review Agent, closest of the batch to "dev productivity tooling" but still an IC title), Aniruddha Bhanja Chowdhury (IBM), Ashutosh Vishnoi (Automation Anywhere), Michael Malak (Oracle) — **none individually filed**; used only in aggregate as negative evidence that "developer productivity" is not a distinctly-titled role the way "AI enablement" is.
60. **John McCann** — Head of Product, ComplyFlow (`shared skills library Claude Code team`) — building shareskills.ai; "sharing a skill ≠ running a library" — **FILED, B1 (#1)** — the competitor find
61. Abhisheik Deo — same post resurfacing under this query, already logged at #26 — **not re-filed, not double-counted**
62. **Rizwan Saudagar** — Engineering Leader, Agentic AI, FDE (`shared skills library Claude Code team`) — team-size-based skill/tool complexity model from an "AI-Assisted Development" course review — **FILED, B1 (#3)**
63. **Raj Bonigala** — Software Engineering Manager, AI & Cloud Automation (`skills registry overkill just use a repo`) — "Claude Code skill map," one tool per build stage, sourced from GitHub stars + skills.sh installs — **NOT FILED** (a directory/leaderboard curation piece, not a governance argument; profile and article link captured but left out of final findings)
64. **John Kleist III** — Chief Growth Officer, SkillsTX, "Skills Forensics™" (`skills registry overkill just use a repo`) — "82% role match vs 27% validated evidence" workforce-credentialing content — **NOT FILED** (this is HR/human-workforce "skills" forensics — a different meaning of "skills" entirely, not AI agent skills; a pure keyword collision)
65. **AI Alleyway** (company/publication page) (`skills registry overkill just use a repo`) — manual audit of Anthropic's official skills/plugin catalogue: 291 plugins, 238 external, attribution gaps, commit-SHA pinning — **FILED, B3 (#11)**
66. **Dhanushree Mohan** — Senior Marketing Specialist (`agent skills are overengineered`) — Malay/English hiring ad for junior sales role — **NOT FILED** (irrelevant)
67. **César Otero** — Fullstack Engineer (`agent skills are overengineered`) — anecdote: "100% skill match is silly," hired a data scientist as fullstack engineer — **NOT FILED** (about human hiring/skills-matching, not AI agents)
68. **Pradip Shrivastava** — Marketing manager, textile design (`agent skills are overengineered`) — generic "companies want cheap average people" complaint — **NOT FILED** (irrelevant)
69. **Muhammad Jameel** — Mechatronics Engineer (`don't need a skills registry`) — "you don't need thousands of certifications" career post — **NOT FILED** (human career skills, irrelevant)
70. **Marcelo Calbucci** — Founder, Seattle Flow (`don't need a skills registry`) — "you don't need Linear, branches, PRs, CI/CD, or staging until your product has meaningful traction" — **PARTIALLY FILED** (quoted in the B4 section as the closest adjacent anti-process sentiment found, explicitly flagged as general startup-process skepticism, not skills-registry-specific)
71. **Parth Terkar** — District Skill Development Assistant, Maharashtra State Skill Development Society (`don't need a skills registry`) — generic government skill-development messaging — **NOT FILED** (irrelevant)

(Query #19 was a re-navigation of query #16's exact URL to extract hrefs via `read_page` instead of `get_page_text`; same 3 posts as #63-65 above reappeared, no new posts.)

---

## 3. Seen but not filed — the full discard pile, and why

**Recruiting/hiring noise (largest single category of discards):** Rajat D. ("Claude Code User" contract role, $80-100/hr), Osama Hussain (Infosys Consulting Principal Consultant – AI Consulting), Ashuta Kaul (ThoughtLabs Belgium GenAI Engineer). These surfaced because job ads for AI-adjacent roles now routinely namedrop "Claude Code," "agentic AI," or "AI governance" in the bullet list even when the post has nothing to say about how skills are actually managed. I discarded all hiring posts on sight — they tell you the labor market wants these skills, not how anyone governs them.

**Keyword collisions on "skills" meaning human/HR skills, not AI agent skills:** John Kleist III (SkillsTX, "Skills Forensics™" — auditing whether an *employee's* resume matches their actual validated competence), César Otero (skills-matching in hiring a data scientist as a fullstack engineer), Muhammad Jameel (certifications vs real experience), Parth Terkar (government skill-development office), Dhanushree Mohan and Pradip Shrivastava (generic hiring/complaint posts). "Skills" is a heavily overloaded term on LinkedIn — the HR/workforce-development meaning outnumbers the AI-agent-SKILL.md meaning by a wide margin in raw search volume, especially on any query that didn't include "Claude," "Codex," "agent," or "AI" explicitly.

**Recommendation/repost chains that happened to contain a keyword:** Bernard Ablola → Dr. Wanda Walker (leadership-coach recommendation chain matched "skills sprawl AI agents" only because Walker's newsletter title contains "Skills" and "AI"), Tod N. → Missy Webb (career-advice chain matched "context engineering skills" only on "skills" and "engineering"). These are the LinkedIn-algorithm equivalent of false positives — worth flagging because they ate real turns without yielding evidence.

**Vendor/thought-leadership filler that used the right vocabulary but said nothing specific:** Srinivas Bommena's "Agentic AI Governance Engine" teaser, Koushik Lahiri's "AI Governance Has a Blind Spot" newsletter, intelligentMDG's SAP master-data-governance article, Bernard Marr's sponsored AWS/Thomson Reuters infrastructure piece, vamsi U's Visualpath training-course ad, Ivee Bhuyan's personal ChatGPT-Copilot reflection. All of these use "governance," "agentic," or "AI security" in the caption but are either lead-generation for an unrelated product/course, or generic enough that they'd read the same whether or not Claude/Codex skills existed. I treated "does this name a concrete mechanism, number, or team practice" as the bar for filing; these didn't clear it.

**Close-but-off-bucket — the ones I deliberated over longest:**
- **Mehmet Suat Bilgiç** (via Ryan Moeller's repost) — genuinely sophisticated writing on runtime governance ("capability defines what can be proposed... only the runtime may authorize it"), but it's about autonomous-agent action authorization in industrial/infrastructure contexts, not about managing a library of Claude/Codex skill files. Adjacent field, wrong artifact.
- **Ranjita M** — "AI agents need containment by architecture," a strong, numbers-referencing piece (cites a "2026 OpenAI containment incident") about access-control vs. containment for agent tool use generally. I almost filed this under B3 but held back because it never mentions skills/SKILL.md/skill registries — it's about agent tool permissions broadly, one layer up from the artifact this research is about.
- **Mumshad Mannambeth** (KodeKloud) — the AI-code-quality stats (1.7x more issues, 91% longer review times, 10x more vulnerabilities at 4x speed) are compelling and highly shared (456 reactions), but the post is about reviewing AI-generated *code*, not about managing AI agent *skills* — I used it only as an engagement-pattern data point (see section 4), not as a bucketed finding, to avoid stretching the definition of "skills governance" to include all of AI-assisted-development risk.
- **Codelitics** (company page) — a vendor selling "an AI coding measurement layer" with a low-commitment pilot pitch, explicitly naming Claude Code/Cursor/Codex/Copilot. This is real competitive-landscape information (another company selling into AI-coding-tool rollout measurement) but it's a cold pitch with no concrete claim or number to quote, so I kept it as a one-line competitive note inside the B1 discussion of Abhisheik Deo's post rather than a standalone numbered finding.
- **Raj Bonigala**'s "Claude Code skill map" — legitimately about Claude Code skills specifically, sourced (GitHub stars, skills.sh install counts), and not nothing. I left it out of the final findings file because it's a curated directory/leaderboard of which skill is "best" per build stage, not evidence of how a team shares, versions, or governs skills — closer to a marketplace review than a governance signal. In hindsight this is a defensible but debatable exclusion; it would support a "there's enough noise in the marketplace that people are building curation/leaderboard content" observation if the coordinator wants it added.

**Titles/companies noticed in passing but not written up individually:** Ben Ortega (VP Strategic AI Enablement, Backbase — conversational-AI sales, not coding), Mauro Spigolon (AI Enablement Lead, Eva Miller — smaller/less-identifiable company), and all 10 "developer productivity AI" people-search cards (Dhruv Gajaria/Microsoft, Sanyasirao Dharmuktula/ServiceNow, Vishnupriya kumaar/Prodapt, George Bocancios/Mojar AI, Madeeswaran K./JetBrains, Swagath Suvarna/Clarivate, Kshitij Agarwal/Bito, Aniruddha Bhanja Chowdhury/IBM, Ashutosh Vishnoi/Automation Anywhere, Michael Malak/Oracle) — all real people/titles/companies, all read, none individually quoted because none said anything about skill sharing, sprawl, trust, or governance; they were used only in aggregate as the "no distinct dev-productivity title" negative finding.

---

## 4. Observations that didn't fit a clean bucket

- **The title that owns this problem is "AI Enablement," not "developer productivity," not "platform engineering."** Across two dedicated people-searches, "AI Enablement [Lead/Manager/Head]" produced ten specific, current, named-company hits on the first page alone (Toyota North America, Ford, Deloitte, Mubadala, Eightfold, World Wide Technology, Wood, Fluent Software, Backbase, Eva Miller). "Developer productivity AI" produced zero people with that framing — every hit was a generic "AI/ML Engineer" or "GenAI Developer" IC title. If there's a buying-center title to target, the search evidence points at AI Enablement, not the developer-productivity or platform-engineering framing the research brief suggested trying.
- **Company types skew toward individual consultants/architects and small vendors, not named platform teams at scale-ups.** Every strong governance/sharing insight (Abhisheik Deo, Rizwan Saudagar, Murali K., Sujit Dhanuka) came from an independent architect or consultant describing client work in the first person, not from a company engineering blog. The two references to real named engineering orgs at scale (Ramp, Stripe) were secondhand, inside Abhisheik Deo's post, not first-party posts from anyone at Ramp or Stripe. I did not find a single post from someone at a well-known tech company describing "how we run our internal Claude Code skill library."
- **Engagement is inversely correlated with specificity.** The three most concrete, numbers-bearing posts about actually running shared skills at scale (McCann, Deo, Saudagar) sat at 4-5 reactions each. The posts with hundreds of reactions (Rajiv Selvaraj's 343, Mumshad Mannambeth's 456, Dr. Wanda Walker's 365) were either 101-level explainers or adjacent-but-not-quite-on-topic content. This surprised me — I expected the practitioner posts to at least match the explainer posts given how directly they engage the stated problem.
- **A live, direct competitor surfaced from a single query** (John McCann / shareskills.ai) on the 15th of 19 searches — this wasn't something I was specifically hunting for and easily could have been missed if the scan had stopped earlier or used slightly different phrasing. Worth noting for future research passes: "shared skills library" as a phrase was the one that surfaced it, not any of the more governance/security-flavored queries.
- **A second, adjacent tooling category appeared unprompted: skill-file security scanners.** Both NVIDIA's "SkillSpector" (via Aditya Goenka) and an independent builder's "AgentSeal" (via Pethuraj M) surfaced from the same single query (`agent skills security`), suggesting "scan a skill before installing it" is coalescing into its own small tool category faster than "manage/version/share a skill library" is — the trust/security angle seems more product-ready on LinkedIn right now than the sharing/governance angle.
- **"Skills" as a search term is dominated by human/HR usage, not AI agent usage**, whenever the query doesn't pin down "AI," "agent," "Claude," or "Codex" explicitly. Every query using a bare word like "sprawl," "registry," "overengineered," or "library" alongside "skills" pulled in workforce-development, HR-credentialing, or career-advice content as noise, sometimes as the majority of results (see query 16's John Kleist III, query 17 and 18 entirely).
- **No B4 "just use a repo" post exists, at least not on LinkedIn under these queries.** I ran two dedicated hunts (queries 17 and 18) and got essentially nothing on-topic from either. The one real counter-argument found (Murali K.) is structurally different — it's skeptical of SKILL.md as an enforcement mechanism, not skeptical of the *idea* of organizing/sharing/governing skills. This gap itself seems like a finding: either the "just use a repo" position genuinely isn't being argued publicly, or it's being expressed somewhere LinkedIn search doesn't surface well (private Slack communities, HN, X/Twitter, informal comments rather than posts).
- **Group content behaves differently from feed content.** The one post found inside a LinkedIn Group ("Anthropic Claude," 160 members, via Ryan Moeller's member-spotlight repost of Mehmet Suat Bilgiç) was denser and more technical than almost anything in the open feed, and was also the one case where an actual activity URN leaked into the DOM. Groups might be a richer vein than open-feed search for this kind of content, and weren't explored beyond this one incidental hit.

---

## 5. Flagged as uncertain in what's already filed

- **All relative timestamps are approximate.** "18h before capture," "3w before capture," etc. in the findings file are LinkedIn's own coarse relative-time labels ("18h", "3w", "4d") converted by simple subtraction from the capture date (2026-09-05). LinkedIn does not expose an exact publish timestamp on the search-results card, so e.g. "3w" could be anywhere in roughly a 7-day window around the stated approximate date. None of these are precise, and I did not open any post's own page to check for a more exact date (which likely still wouldn't show finer than the day).
- **Post permalinks are missing for the majority of filed findings.** Only findings that link to the author's own Pulse article, newsletter, or an external blog have a stable, exact URL (McCann/shareskills.ai, Gowda, Kallem/Murali K., Bene, Dhanuka, Ranjita M [not filed], AI Alleyway, Bonigala [not filed]). For posts with no such outbound link — Deo, Saudagar, Selvaraj, Goenka (has one but it's a hashtag/video link not an article), Pethuraj M, Dogra, Blackmore — the citation is the author's profile URL plus the search query the post surfaced under, not a `/feed/update/urn:li:activity:...` permalink. I attempted to get real permalinks via each post's "Copy link to post" control-menu option but that requires OS-clipboard read access, which requires enabling broader "computer use" device control that I judged out of scope for a read-only browse-and-quote task and did not request. This is disclosed in the findings file itself but is worth restating here as the single biggest methodological gap in the evidence base.
- **Titles for the "AI Enablement" and "developer productivity AI" people-search results are LinkedIn-generated summaries, not verbatim self-descriptions.** The one-line "current position" text under each name in people-search results (e.g., "Sr. AI Enablement, Fluency, & Innovation Lead at Eightfold since March 2025, leading Claude enablement and agentic AI workflows") reads like LinkedIn's own AI-generated synthesis of the profile, not something the person typed verbatim as a post or even necessarily as their exact headline — the headline proper (the short line right under the name, e.g. "DATA & AI ENABLEMENT" for Aidan Millar) is more likely self-authored than the longer sentence-form summary beneath it. I did not open any of these ten-plus individual profile pages to verify the sentence-form text against the person's actual "About" or "Experience" sections, so treat those longer summaries as directionally accurate but not confirmed word-for-word self-descriptions the way the feed-post quotes are.
- **Reaction/comment counts are a snapshot**, taken at whatever moment I happened to view each post during this single 2026-09-05 session; they are not final and several (especially the recent ones, like McCann's 18-hour-old post) will very likely have grown since.
- **I did not scroll past page 1 on either people search** (`AI enablement` showed 10 pages total per its own pagination; `developer productivity AI` showed the same "1 2 3 ... 10 Next" pattern) — the persona conclusions in the findings file are based on the first 10 results of each, not an exhaustive read of all ~100+ available profiles per query. A deeper pull of pages 2-10 on `AI enablement` in particular could surface more named companies and might change the specific list of employers cited, though I'd be surprised if it changed the headline conclusion (that "AI Enablement" is a real, recurring title).
- **I did not verify whether "Ben Blackmore" is the person's display name or a pseudonym** — his profile URL slug (`benripkens`) doesn't match the displayed name "Ben Blackmore," which LinkedIn sometimes allows (e.g., a maiden/married name mismatch, a rebrand, or a display-name change without a slug change). I used the displayed name in both the findings file and the interview-candidates file but flagged the slug mismatch here in case it matters for outreach (searching "Ben Blackmore" vs. "Ben Ripkens" could surface different or additional information).
- **The "45-person engineering team" and "hundred-developer audit" figures (Gowda, Deo) are the posters' own unverified claims**, presented in their posts as if from an internal study but with no linked source data, methodology, or company name attached to either number. I filed them as direct quotes (which they are) but did not — and could not, from a search scan — verify the underlying study exists as described.
