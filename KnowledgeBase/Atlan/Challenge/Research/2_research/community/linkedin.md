# LinkedIn evidence: how teams manage, share and govern AI agent "skills"
Research date: 2026-09-05. Method: `linkedin.com/search/results/content/?keywords=...` read via browser, scanned with get_page_text/read_page. All entries below were read live in the browser this session — marked [verified].

**Tooling limitation, disclosed up front:** LinkedIn's search-results DOM does not expose a feed post's own permalink (`/feed/update/urn:li:activity:...`) to the accessibility tree or page text without either (a) clicking "Copy link to post" and reading the OS clipboard, or (b) opening each post individually — neither was worth the added device-clipboard permission or per-post cost for a scan of this breadth. Where the author published a linked Pulse/newsletter article, that article's own stable URL is given (it carries the same claim). Where there is no such article, the citation is the author's profile URL plus the exact search query the post surfaced under — sufficient to relocate the post, not a raw activity permalink. This is noted per entry.

---

## B1 — SHARING (most important): rollout, shared skill libraries, onboarding, versioning/ownership

**1. [verified] John McCann — Head of Product, ComplyFlow**
> "A company's know-how shouldn't live in one vendor's menu, owned by whoever typed it first, with no review and no history. It needs a library the organisation owns, that anyone can improve under rules, that keeps its history, and that runs wherever the work happens."
Posted ~18h before capture (≈2026-09-04). Query: `shared skills library Claude Code team`. Profile: https://www.linkedin.com/in/johnmccann1/ — linked article (his own): https://shareskills.ai/blog/sharing-is-not-a-library
Also in the same post: > "sharing a skill and running a skill library are different jobs. The difference doesn't show up at skill number three. It shows up around skill number forty."
Why it matters: **This is a direct competitor.** McCann is building "shareskills.ai," a governed-skill-library product, explicitly positioned against Anthropic's native in-app skill sharing (no review, no version history, view-only copies, admins can't see contents). This is the closest thing found to another vendor pitching the exact same wedge as the work sample. Only 5 reactions — an early, low-volume post, not yet a proven category.

**2. [verified] Abhisheik Deo — Hands-on Architect, 19+ yrs, Multi-tenant SaaS + AI-powered systems; runs Claude Code + OpenAI Codex across a 20-engineer team**
> "A shared skill library — workflows promoted from one engineer's terminal to the team's. A hundred-developer audit this year logged ~1,400 weekly skill invocations at steady state, with eight skills carrying ~78% of the load."
Posted 3w before capture. Query: `Claude Code rollout engineering team`. Profile: https://www.linkedin.com/in/abhisheikdeo/ (post permalink not resolvable — see limitation note)
Also: > "Teams stall when the dashboard reads green while every repo still ships with the default CLAUDE.md, no shared skills, no hooks." And: "Hooks wired in tiers — global, squad, personal."
Why it matters: The single most concrete B1 datapoint found — real usage numbers (1,400 weekly invocations, 8 skills = 78% of load) from someone running Claude Code + Codex across a named team size (20 engineers), describing promotion-to-shared-library and tiered hooks as the maturity signal, explicitly contrasted with vanity seat-count metrics. Exactly the persona and problem framing a registry pitch would target. Only 5 reactions.

**3. [verified] Rizwan Saudagar — Engineering Leader | Agentic AI | FDE | AI Platform & Cloud Infrastructure**
> "Larger team (5+): skill catalogs, MCP server library, plugins" — following "Small team (2-5): shared CLAUDE.md, shared skills, agent teams."
Posted 3w before capture. Query: `shared skills library Claude Code team`. Profile: https://www.linkedin.com/in/rizwan-saudagar-1043437/
Why it matters: An engineering leader independently sketches a maturity curve where skill catalogs are the explicit next rung above ad hoc shared skills once a team passes ~5 people — corroborates Deo's account of a "shared skills → catalog" progression as a real, recognized stage. 4 reactions.

**4. [verified] Rajiv Selvaraj — B2B partner/connector (non-technical persona)**
> "Skills live in your project, get reused automatically, and stay consistent across your whole team."
Posted 2w before capture. Query: `SKILL.md`. Profile: LinkedIn search result for "SKILL.md" (permalink not resolved — see limitation note).
Why it matters: Not a practitioner, but by far the highest engagement of any B1 post found (343 reactions, 54 comments) — shows the *concept* of team-shared skills has broad appetite as explainer content, even though the people actually running shared libraries (Deo, Saudagar) post to near-zero engagement. Engagement and expertise are inversely correlated in this sample.

---

## B2 — SPRAWL: too many skills, wrong skill firing, duplicates, staleness, context bloat

**5. [verified] Keerthan Gowda S — AI Consultant at MHP-India**
> "4 MCP servers I hadn't called in over a month. A CLAUDE.md that had quietly grown past 400 lines. Both were billing me on every single turn."
Posted 4w before capture. Query: `Claude Code skills team`. Profile: https://www.linkedin.com/in/keerthangowdas/ — linked article: https://www.linkedin.com/pulse/only-14-your-claude-code-bill-thing-you-actually-typed-gowda-s-ompof/
Also cites a "45-person engineering team" audit: user prompts were only 14% of input tokens; "Skills + CLAUDE.md" was 8% of the remaining context cost.
Why it matters: Concrete evidence that skill/config accumulation has a *cost* dimension (token spend), not just a correctness one — a different sprawl angle (economic, not just quality) that a registry pitch could use.

**6. [verified] Marius Bene — Executive Director, Future WorkForce Global**
> "Drop one onto a fragmented workflow and it doesn't fix the fragmentation — it scales it."
Posted 3w before capture. Query: `skills sprawl AI agents`. Article: https://www.linkedin.com/pulse/agent-sprawl-why-10x-more-ai-agents-wont-mean-productivity-9qo2f/
Cites Gartner: AI agents expected to outnumber people 10:1 by 2028, yet fewer than 40% of respondents say agents made them more productive.
Why it matters: General "agent sprawl" (not skill-file specific) framing from a workforce-transformation consultancy — shows the sprawl argument already has currency one level up the stack (agents, not yet skills specifically). 11 reactions.

**7. [verified] Ben Blackmore — CTO @ Dash0**
> "Several thousand employees have access to Claude Code. That is not agents in production. That is seat count."
Posted 1d before capture. Query: `AI coding agent adoption metrics`. Profile: https://www.linkedin.com/in/benripkens/
Why it matters: A CTO independently makes the same "seats ≠ real adoption" argument as Abhisheik Deo, from a completely different angle (hours-of-agent-runtime vs. artefact count) — two unconnected practitioners converging on the same measurement gap is a stronger signal than either alone. 66 reactions, 24 comments — one of the higher-engagement practitioner (non-explainer) posts found.

---

## B3 — TRUST: security review, prompt injection, secrets in skills, policy/governance language

**8. [verified] Aditya Goenka — Founder @ Be10x ("Helping 3M+ Professionals Get 10X Productive with AI")**
> "NVIDIA analyzed 42,000+ AI agent skills across AI marketplaces and found a worrying security risk: nearly 1 in 4 skills could potentially compromise a system."
Posted 4d before capture. Query: `agent skills security`. Profile: https://www.linkedin.com/in/aditya-goenka/
Also: NVIDIA built "SkillSpector," an open-source scanner to check AI agent skills before install.
Why it matters: The single strongest quantified B3 stat in the whole scan (1 in 4 skills, 42,000+ sample) plus a named vendor (NVIDIA) already shipping a pre-install skill scanner — direct evidence the "scan/review before adoption" layer is already being built by a large player. 53 reactions.

**9. [verified] Pethuraj M — offensive-security practitioner ("I hack for a living")**
> "AgentSeal - A Security toolkit for AI agents. Red-team prompts, detect MCP poisoning, scan skill files, trace toxic data flows."
Posted 2d before capture. Query: `agent skills security`. Profile: https://www.linkedin.com/in/pethu/
Why it matters: A second, independent tool ("AgentSeal") whose feature list explicitly includes "scan skill files" — corroborates Goenka/NVIDIA that skill-file scanning is becoming its own small tooling category. Competitive-landscape signal. 50 reactions.

**10. [verified] Sujit Dhanuka — AI Scientist & Mentor**
> "No registry catches this (it holds a description written before the change), no gateway catches it as a governance matter (permitted and unsanctioned calls look identical on the wire)."
Posted 4w before capture. Query: `AI agent registry`. Article: https://www.linkedin.com/pulse/why-ai-governance-begins-source-code-sentrai-console-7lfif/
Context: an agent's tool permissions silently expand after a merged PR (a support-lookup agent gains `initiate_refund`/`transfer_funds`); nothing in the stack — not the registry, not the gateway, not a code scanner — flags it as unauthorized.
Why it matters: Names the exact failure mode a *static* skills registry doesn't solve on its own (description drift vs. actual runtime capability) — useful as an objection to pre-empt in a registry pitch, not just supporting evidence.

**11. [verified] AI Alleyway (company/publication page)**
> "I counted Anthropic's official catalogue on 2 September: 291 plugins listed, 53 living in the marketplace repository itself, 238 pointing at repositories owned by 182 other organisations."
Posted 2d before capture. Query: `skills registry overkill just use a repo`. Company page: https://www.linkedin.com/company/ai-alleyway/ — article: https://aialleyway.com/claude-skills-marketplace/
Also: of the 53 first-party `plugin.json` files, 23 declare Anthropic as author, 12 name the vendor, 18 name nobody; all 238 external entries are pinned to a 40-character commit SHA (no floating "latest").
Why it matters: The most rigorous, numbers-first provenance/governance audit of an actual Claude skills marketplace found in the scan — a ready-made case study of exactly the ownership/pinning/attribution gaps a governed registry would close.

**12. [verified] Harendra Dogra — AI Security Consultant, Secure Axis Labs**
> "Only 21% of executives report complete visibility into agent permissions, tool usage and data access."
Posted 1w before capture. Query: `agent skills governance`. Profile: https://www.linkedin.com/in/harendra-dogra/
Why it matters: A named, sourced-sounding statistic on the exact "visibility black hole" a registry addresses, from a security-consulting persona actively selling into this problem (title: AI Security Consultant, offers "strategy calls").

---

## B4 — COUNTER-EVIDENCE (hunted deliberately): "this is over-engineering" / "a repo is enough"

**13. [verified] Murali K. — Data & AI Executive; Enterprise Data Strategy & Governance; CDO/CAIO Advisor (Salesforce, Box, Toyota, GE)**
> "Writing 'Always call Tool A before Tool B, and only invoke Tool C if status is APPROVED' in a SKILL.md file does not create a deterministic state machine — it creates a probabilistic suggestion."
Posted 1w before capture. Query: `SKILL.md`. Profile: https://www.linkedin.com/in/muralikallem/ — article: https://www.linkedin.com/pulse/skillmd-trap-why-english-isnt-deterministic-state-machine-kallem-pfmjc/
Also: > "In mission-critical enterprise workflows, a 98% execution success rate is a failing grade."
Why it matters: The clearest counter-argument found — not "a repo is enough" verbatim, but structurally the same objection aimed one level deeper: SKILL.md-as-governance is itself unreliable because natural-language instructions aren't enforceable control flow; his prescription is a hard-coded deterministic spine with skills confined to bounded cognitive tasks. A credible, senior (CDO/CAIO-advisor-level) voice — this is the objection a registry pitch most needs a real answer to. Note: this argues skills *governance-by-file* is fragile, not that governance/registries are unnecessary — no post arguing the latter ("just use a repo, skip the tooling") was found despite two dedicated searches (see null results).

I did not find any post making the plainer over-engineering claim ("a shared repo/README is enough, don't build tooling for this") specific to agent skills — see null-result queries below. The closest adjacent sentiment (not skill-specific, so not logged as a numbered finding) was Marcelo Calbucci, Founder of Seattle Flow: "you don't need Linear, branches, PRs, CI/CD, or staging until your product has meaningful traction" — a general anti-premature-process argument, not about skills/agents.

---

## B5 — SIGNAL SHAPE: who is talking, what titles/companies, engagement, and is there a persona

### Titles that own this problem (People search: "AI enablement", 2026-09-05)
This is a real, recognized job title/function, held at large, brand-name enterprises — not just startups or agencies:
- **Cory Eno** — "Sr. AI Enablement, Fluency, & Innovation Lead at **Eightfold** since March 2025, leading **Claude enablement** and agentic AI workflows." (Claude-specific enablement role.)
- **Aidan Millar** — "Head of AI Enablement at **Mubadala** since December 2021, leading a **$100M** enterprise AI transformation across investment lifecycle and corporate functions."
- **Ben Gold** — "AI Enablement Lead, **Toyota North America**... leading AI strategy, training, tool allocation and measurement for enterprise AI adoption."
- **Karthikeyan Rajendran** — "AI Enablement Manager at **Ford Motor Company** since September 2024, leading SSDA AI adoption through incubation, governance and literacy programs."
- **Srinivas P** — "Manager - AI Training and Enablement at **Deloitte** since June 2023."
- **Shane Kelly** — "Team Lead - AI Enablement Team at **World Wide Technology**... driving AI native tooling adoption and enterprise enablement."
- **Kashish Khemka** — "Technical Lead - AI Enablement at **Wood**... covering AI strategy, enablement, transformation, adoption and agentic AI."
- **Sage Franch** — "Head of AI Enablement at Fluent Software... Founder of **CLAIR AI Governance Association**." (a named, existing AI-governance association — worth a follow-up look outside this scan.)
[verified via LinkedIn People search results, https://www.linkedin.com/search/results/people/?keywords=AI%20enablement]

### Titles that do NOT show up distinctly ("developer productivity AI")
The same people-search discipline applied to "developer productivity AI" surfaced almost no one self-titled around developer productivity or platform engineering specifically — results skewed to individual-contributor "AI/ML Engineer," "GenAI Developer," and "Agentic AI Developer" titles at Microsoft, ServiceNow, IBM, JetBrains, Oracle, Automation Anywhere. **"AI Enablement" is a materially more established, distinctly-titled buying-center role on LinkedIn than "developer productivity."**

### Engagement pattern
- The posts making the *strongest, most specific* claims about shared skill libraries and rollout metrics (Abhisheik Deo, Rizwan Saudagar, John McCann) each sat at only 4-5 reactions — low-volume, practitioner-to-practitioner content.
- The highest-engagement posts in the whole scan were *explainer* content aimed at beginners (Rajiv Selvaraj's "Claude Code Skills, explained like a beginner course," 343 reactions/54 comments; Mumshad Mannambeth's AI-for-DevOps guide, 456 reactions) and one security/vendor stat post (Aditya Goenka's NVIDIA-scanner post, 53 reactions).
- This is a topic still mostly at the "here's what a skill even is" / "here's a scary stat" stage of the conversation on LinkedIn, not yet at the "here's how our 200-person org governs its skill catalog" case-study stage.

### Company types represented across all findings
Individual consultants/architects running client engagements (Abhisheik Deo, Rizwan Saudagar, Murali K.), a named competitor SaaS founder (John McCann/shareskills.ai), an infra-observability CTO (Ben Blackmore/Dash0), enterprise AI-consulting recruiters and Big-4/GCC hiring posts (Infosys, background noise), a security boutique (Secure Axis Labs), an independent security tool builder (Pethuraj M/AgentSeal), and a niche AI newsletter/publication (AI Alleyway). Notably **no large-enterprise engineering blog or named FAANG/scale-up engineering team post was found describing its own internal skills rollout** — Ramp and Stripe are referenced only secondhand, inside Abhisheik Deo's post, not as their own posts.

---

## Null-result queries (logged as run, nothing bucket-relevant found)

1. `internal AI skills library` — returned generic AI/ML skills-training and certification content (IBM SkillsBuild credential, an academic-librarian AI-competence research article, a "Google AI Essentials" course ad). No team skill-sharing or governance hits.
2. `context engineering skills` — returned a school hiring/graduate-recruiting post, a "prompt engineering vs. context engineering" career-advice Pulse article, and an "AI engineering is getting overcomplicated" post not specific to Claude/Codex skills or governance.
3. `agent governance versioning` — returned generic enterprise-AI-governance content (an "Agentic AI Governance Engine" teaser, a master-data-governance/SAP article, an inter-agent decision-ownership newsletter) - none addressed skill-file versioning specifically.
4. `Codex skills team` — name-collision noise: a student hackathon team thanking a coding club called "Codex," an unrelated Asana job ad, a "seeking technical co-founder" post that only mentions Codex/Claude Code/Cursor in passing.
5. `agent skills are overengineered` — zero relevant matches; LinkedIn auto-corrected to "over engineered" and returned unrelated resume/hiring-skills content.
6. `don't need a skills registry` — zero relevant matches; returned generic career-skills and startup-process content, nothing about agent skill registries.
7. `Claude Code skills team` (secondary read) — beyond the one token-bloat post logged in B2, the rest of the page was a recruiter's "Claude Code User" hiring ad and a generic "Skills vs CLAUDE.md vs MCP vs Sub-agents" explainer — no team/rollout content.

## Access note
LinkedIn was fully accessible throughout - no login wall, rate limit, or security checkpoint was encountered on any of the 19 queries run. All reading was done via the search-results content feed and get_page_text/read_page; nothing was posted, liked, followed, or messaged.
