# Atlan — company briefing
Researched 2026-09-05. [verified] = primary source read today; [reported] = secondary; [assumption] = inference.

## Company
- [verified] Founded 2018 by Prukalpa Sankar and Varun Banka (Co-founders & Co-CEOs). Singapore-HQ per press, large India engineering base.
- [verified] ~$206M raised. Latest disclosed: **Series C, $105M, 8 May 2024**, led by GIC with Meritech; Salesforce Ventures and Peak XV participating; **$750M post-money**. https://atlan.com/atlan-raises-105m-funding/ — no Series D found publicly as of Sep 2026.
- [reported] Self-reported at Series C: 7x revenue growth over two years, 75% competitive win rate, 400% enterprise sales growth in Q1 2024. Latka estimated ~$46M revenue / 295 employees in 2023. No 2025-26 ARR figure public.
- [verified] Analyst positioning: **Leader, 2025 Gartner MQ for Metadata Management** (24 Nov 2025); **Leader, 2026 Gartner MQ for Data & Analytics Governance Platforms** (Jan 2026, up from Visionary in 2025); **Leader + Customer Favorite, Forrester Wave Data Governance Q3 2025**.
- [verified] Customers named publicly: Cisco, Autodesk, Unilever, Ralph Lauren, FOX, News Corp, Nasdaq, Plaid, HubSpot, Mastercard, Workday, Dropbox, GM, Virgin Media O2, Elastic, NHS, Marriott, GitLab, DigiKey. (Talk also names Zoom, Discord, Affirm, JPMorgan Chase.)

## Product today
- Core data catalog / governance platform (discovery, lineage, glossary, Snowflake tag sync, dbt semantic layer, Databricks Unity Catalog).
- [verified] **Atlan MCP Server** — open source, exposes Atlan metadata/context to Claude, ChatGPT, Cortex, Databricks Genie. https://github.com/atlanhq/agent-toolkit
- [verified] **Context Engineering Studio** — Bootstrap → Simulate → Deploy → Observe workflow for versioned "context repos" consumed via MCP. https://atlan.com/context-engineering-studio/
- [verified] **Context Agents** (nine agents automating 9-12 months of documentation), **Context Lakehouse**, **Enterprise Data Graph**, **Traces & Observation Loops** — per the Activate 2026 page.
- **Key finding — [verified]: "Agent Registry" is NOT a publicly announced Atlan product.** It appears only in three SEO articles under atlan.com/know/ai-agent/ dated 1 Sep 2026, bylined "Emily Winks, Data Governance Expert" (no verifiable individual — likely a house content persona). It is not listed among products on atlan.com. So: unannounced/internal. The demos we were sent are internal materials.
  - https://atlan.com/know/ai-agent/what-is-an-ai-agent-registry/
  - https://atlan.com/know/ai-agent/agent-registry-vs-model-registry/
  - https://atlan.com/know/ai-agent/aws/what-is-aws-agent-registry/

## How Atlan is publicly positioning against registries
Consistent line across the three articles: registries answer *"does this agent/tool exist and is it approved?"* — not *"is the business knowledge it relies on still correct?"* Quote used: an approved record certifies existence, schema validation, workflow clearance, owner and version — *"and it is not the same claim as certifying that the resource is correct."* Atlan positions MCP server + context repos + data graph as the layer **underneath** the approval workflow.
- **Note the tension:** publicly Atlan says "registries are not enough, buy our context layer." The work sample asks us to GTM a registry. Worth reconciling in the readout — the registry is the wedge into the context layer, not a separate bet.

## GTM today
- [assumption→likely] Enterprise, sales-assisted, per-user annual subscription. No self-serve paid checkout.
- [reported] Vendr benchmarks: Free (≤5 users), Team $20-50K/yr, Business $60-100K/yr, Enterprise $100-200K+/yr; median tracked spend ~$49.8K/yr across 43 purchases. https://www.vendr.com/marketplace/atlan
- Buyers: CDOs, VP Data/Analytics, VP AI, AI platform teams, governance teams, data engineers.
- Community surface: GitHub org **atlanhq**, **Humans of Data** community/blog, **The Great Data Debate** (2026 theme: "AI Broke the Data Stack"), **Activate 2026 / Context 26** virtual events.
- **Read:** Atlan today sells top-down to CDOs at large enterprises with a ~$50K ACV. The brief explicitly wants "dramatic distribution before we optimize for a traditional enterprise sales motion" — i.e. a bottom-up motion Atlan has never run. That is the actual strategic tension in this exercise.

## Internal dogfooding (the origin story of the product)
- [verified via interview, 15 Jul 2026] Prukalpa: Atlan built **300 skills and 40 agents in six months**, after evaluating Relevance, Google ADK and Glean, and settling on **Claude Code + Codex** (~50/50). Quotes: *"The quality of the agent is often dependent on the quality of context engineering"*, *"Context kind of needs to be managed like code."* https://finance.biggo.com/news/32a872067717ea9b
- No public repo or artifact from that internal work found — it lives in talks and interviews only. **This is an asset we could ask them to open up: 300 real skills is a distribution seed.**

## People likely in the room
- Prukalpa Sankar — Co-founder & Co-CEO, the public voice on context engineering. linkedin.com/in/prukalpa
- Varun Banka — Co-founder & Co-CEO.
- "Rohan" — Product @ Atlan, narrates both Agent Registry demos.
- No public launch owner for Context Engineering Studio / Agent Registry found.

## Gaps to close
- Current headcount, 2025-26 ARR.
- Activate 2026 vs Context/26 — same event or different, and dates.
- Whether "Agent Registry" ships under that name, and when.
