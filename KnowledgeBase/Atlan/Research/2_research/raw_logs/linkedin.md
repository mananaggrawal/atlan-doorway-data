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

[CONTENT_PLACEHOLDER]