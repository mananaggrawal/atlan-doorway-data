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

[CONTENT_PLACEHOLDER]