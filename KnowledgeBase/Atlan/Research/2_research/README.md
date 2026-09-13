# Research
Everything we looked at, how we looked at it, and what we could not reach. Compiled 2026-09-05.

```
atlan_product/   Atlan's own materials — full transcripts of all three videos,
                 product understanding, company briefing
market/          AWS · Google · OpenAI · skills.sh · MCP registry — what each governs and doesn't
community/       Verbatim practitioner quotes by surface, with null-result logs
numbers/         Hard figures with pull dates, plus the independent verification log
prospects/       ~70 named people who publicly expressed the pain
```

## Coverage

| Source | Method | Status | Output |
|---|---|---|---|
| Atlan AI Engineer talk (Prukalpa, 20:53) | Browser transcript extraction | Full transcript | `atlan_product/ai_engineer_talk_context_layer.md` |
| Agent Registry product demo (6:50) | Same | Full transcript | `atlan_product/agent_registry_product_demo.md` |
| Software Factory demo (1:43) | Same | Full transcript | `atlan_product/agent_registry_software_factory_demo.md` |
| Atlan strategy memo (Google Doc) | Drive connector + WebFetch | **BLOCKED — HTTP 401.** Access requested | — |
| "Internal recordings" named in the brief | — | **Not received.** Asked | — |
| Atlan company, funding, positioning | WebSearch + WebFetch | Done | `atlan_product/atlan_company_briefing.md` |
| AWS Agent Registry · Google skill registry · OpenAI Skills · skills.sh · Claude Code docs · MCP registry | WebFetch of primary docs | Done | `market/registry_landscape.md` |
| GitHub — issues, discussions, topics, READMEs, REST API | WebSearch + WebFetch + api.github.com | Done | `community/github.md` |
| Hacker News | Algolia API + thread reads | Done | `community/reddit_hn.md` |
| Reddit | Blocked from every HTTP tool and the built-in browser; **resolved** via the user's own Chrome. 24 queries, 11 subreddits | Done | `community/reddit.md` |
| X (Twitter) | Browser, signed in, 26 queries, read-only | Done | `community/x_twitter.md` |
| LinkedIn | Browser, signed in, 19 searches, read-only | Done | `community/linkedin.md` |
| Blogs, newsletters, vendor security research | WebSearch + WebFetch | Done | `community/blogs_and_press.md` |
| npm API · GitHub API · skills.sh · JetBrains survey | Direct API and live page fetches | Done | `numbers/quantitative_baseline.md` |
| Independent verification of 12 load-bearing claims | Primary sources only | Done | `numbers/verification_log.md` |
| Semrush Keyword Analytics — search volume, CPC, trend for 40+ terms across category/product/how-to/enterprise language | Semrush API pulls | Done | `numbers/search_demand_semrush.md` |

## Rules applied to every file here

- Verbatim quotes only, ≤50 words. Nothing paraphrased into a claim.
- `[verified]` means the primary source was opened and read; `[reported]` means secondary. Nothing is upgraded without a second look.
- Numbers carry a pull date. Live counters drift, and we say so.
- Contradictions are preserved, not smoothed — skills.sh's homepage reports fewer total installs than its own top skill, and that is recorded rather than averaged away.
- Where a claim failed verification, the file says so in place rather than being quietly deleted.
- Every community file ends with a null-results log: the exact queries that returned nothing.

## Known gaps
1. **The strategy memo and internal recordings** — 401 and not-received. Questions 6 in `../1_brief/questions_for_atlan.md`.
2. **How many skills a typical developer or team has** — three independent researchers hunted; the number does not exist publicly. This is the gap we intend to turn into the artifact.
3. **Public repo prevalence of `.claude/skills/`** — needs authenticated GitHub code search. See `../5_logs/access_and_blockers.md`.
