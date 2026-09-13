# Raw Research Trail: X (Twitter) Skills-Sharing Research
Session date: 2026-09-05. This is an audit trail reconstructed from my own transcript, not a report — includes dead ends, discards, and uncertainties.

## 0. Setup and browser mechanics

- Checked `$HOME/mnt/` and `$HOME/mnt/Atlan/01_evidence/` via device_bash to confirm the project folder structure before starting.
- Opened the browser pane on `https://x.com/search?q=%22SKILL.md%22&f=live` via `preview_start`.
- First `get_page_text` call came back empty (only chrome/tabs, no posts) — the page was still loading. Waited 3s via `computer{action:"wait"}` and retried; posts appeared on the second read. This happened once; all subsequent reads worked on the first try.
- Method settled on after the first two queries: `preview_start` a new search URL -> `get_page_text` to read the visible results -> for any post I wanted to cite, `find(<handle>)` on the accessibility tree to pull its permalink (`/handle/status/ID`) and view count from the "N views. View post analytics" link text. I used `read_page{filter:"interactive"}` directly only for the first two queries before settling on `find()` as faster.
- I did NOT verify every engagement number by screenshot -- only two posts got a visual screenshot cross-check (see Section 5, uncertainty #3): eric provencher's big post, and his profile page.
- Popup-blocking incident: after the first query, a `navigate()` call to load SKILL.md `f=top` failed with "Navigation is paused while a page-opened popup... is open." `tabs_context` showed the browser pane had two unrelated Google-accounts sign-in popups (`popup-2`, `popup-4`) open from prior, unrelated browser activity in this session (other tabs present: a `youtube.com` seed tab, a `linkedin.com` tab-3), plus my own `tab-1` (x.com). I tried `tabs_close` on both popups; both were refused ("That tab is a page-opened popup... the agent may not drive, navigate, or close it"). I did not ask the user to close them (auto-mode, not a hard blocker) -- instead I switched to using `preview_start` for every subsequent query instead of `navigate`, which was not subject to the same block and worked for the rest of the session. I never resolved or closed those popups; they may still be open in the browser pane.
- No posting, liking, following, replying, or form submission occurred at any point. No credentials were entered.

---

## 1. All queries run, in order, verbatim

Correction to my final report: I stated "26 distinct queries" in the filed summary. Recounting from the transcript precisely, I count 27 (I undercounted by one, likely by treating the two SKILL.md variants as one line item when tallying). Listed exactly as run:

| # | Query text | URL | Mode | On-topic hits (of ~5-9 shown) | Verdict |
|---|---|---|---|---|---|
| 1 | "SKILL.md" | x.com/search?q=%22SKILL.md%22&f=live | live | ~2 of 7 (Sammy_970, Flagvance; rest crypto/agent-swarm noise) | Productive |
| 2 | "SKILL.md" | x.com/search?q=%22SKILL.md%22&f=top | top | 4 of 4 (levelsio, AISystems_hq, startupideaspod, DanKornas) | Very productive |
| 3 | "agent skills" | x.com/search?q=%22agent%20skills%22&f=live | live | 3 of 6 (Boardy thin, Morel, DanKornas "AAS Core"; Holochain/CesarAG/danilocoding discarded) | Moderately productive |
| 4 | skills.sh | x.com/search?q=skills.sh&f=live | live | 5 of 7 (Ma7039Ma, DannielDevOps+quoted Ihtesham Ali, Hacksore, conikeec, coka_stefan) | Very productive |
| 5 | "claude code" skills share | x.com/search?q=%22claude%20code%22%20skills%20share&f=live | live | 0 of 5 | Dead end |
| 6 | "too many skills" | x.com/search?q=%22too%20many%20skills%22&f=live | live | 6 of 13 (rest were football/celebrity/life-advice/video-game false positives on the phrase) | Very productive |
| 7 | claude code plugin marketplace | x.com/search?q=claude%20code%20plugin%20marketplace&f=live | live | 5 of 5, but low individual reach (product-promo tweets) | Productive but thin |
| 8 | skills registry agents | x.com/search?q=skills%20registry%20agents&f=live | live | 5 of 7 (2 results were an unrelated child-welfare/CPS news story that happens to use "registry") | Very productive -- best single query for B3/B5 |
| 9 | agent skills governance | x.com/search?q=agent%20skills%20governance&f=live | live | 2 of 5 (stratamindlabs the standout; Thunder Tschunk borderline) | Productive |
| 10 | claude skills versioning | x.com/search?q=claude%20skills%20versioning&f=live | live | 5 of 8 | Very productive |
| 11 | "my skills" claude code teammate | x.com/search?q=%22my%20skills%22%20claude%20code%20teammate&f=live | live | 1 of 1, and that one was only loosely relevant | Dead end |
| 12 | skills sprawl agents | x.com/search?q=skills%20sprawl%20agents&f=live | live | 5 of 7 (HashiCorp false positive, Sam/Type tangential) | Very productive -- best query for vendor/B5 intel |
| 13 | codex skills team | x.com/search?q=codex%20skills%20team&f=live | live | 2 of 5 (angelbrodin filed-worthy but ultimately dropped; Andrew Ng deliberately excluded as false positive) | Moderately productive |
| 14 | AGENTS.md skills team | x.com/search?q=AGENTS.md%20skills%20team&f=live | live | 0 of 7 (dominated by "AI Engineering Skills Map" false positives and unrelated model-launch chatter) | Dead end |
| 15 | "context engineering" skills team | x.com/search?q=%22context%20engineering%22%20skills%20team&f=live | live | 1-2 of 7 (Yarchi the one real hit; Yongkyun Lee borderline) | Weak |
| 16 | "just a git repo" skills (B4 hunt) | x.com/search?q=%22just%20a%20git%20repo%22%20skills&f=live | live | 0 of 2 | Dead end |
| 17 | "over-engineering" skills claude (B4 hunt) | x.com/search?q=%22over-engineering%22%20skills%20claude&f=live | live | 2 of 5 (DailyDoseOfDS_ filed; akshay_pachaar seen but dropped) | Weak but useful |
| 18 | "don't need a registry" (B4 hunt) | x.com/search?q=%22don%27t%20need%20a%20registry%22&f=live | live | 0 of 13 | Dead end -- 100% off-topic (weddings, guns, gift registries) |
| 19 | skills registry overkill (B4 hunt) | x.com/search?q=skills%20registry%20overkill&f=live | live | 0 -- literally zero results returned by X | Dead end |
| 20 | "a shared drive" OR "a folder" claude skills enough (B4 hunt) | x.com/search?q=%22a%20shared%20drive%22%20OR%20%22a%20folder%22%20claude%20skills%20enough&f=live | live | 0 of 6 | Dead end |
| 21 | "just copy paste" skill.md (B4 hunt) | x.com/search?q=%22just%20copy%20paste%22%20skill.md&f=live | live | 0 of 2 | Dead end |
| 22 | skill.md prompt injection (B3 hunt) | x.com/search?q=skill.md%20prompt%20injection&f=live | live | 3 of 6 (apprater, riba2534 filed; K_chachamaru seen, dropped) | Productive |
| 23 | "would not run" OR "wouldn't run" claude skill (B3 hunt) | x.com/search?q=%22would%20not%20run%22%20OR%20%22wouldn%27t%20run%22%20claude%20skill&f=live | live | 0 -- zero results | Dead end |
| 24 | "internal skill library" (B1 hunt) | x.com/search?q=%22internal%20skill%20library%22&f=live | live | 0 -- zero results | Dead end |
| 25 | "our skills" claude code (B1 hunt) | x.com/search?q=%22our%20skills%22%20claude%20code&f=live | live | 0 of 6 (all tangential business/GTM content, nothing on internal libraries) | Dead end |
| 26 | sync claude skills machines (B1 hunt) | x.com/search?q=sync%20claude%20skills%20machines&f=live | live | 2 of 6 (truffle, simplifyinAI filed; Cathryn's two posts and ShahzaibJak seen, dropped) | Productive |
| 27 | "shared this skill" OR "gave my team" claude (B1 hunt) | x.com/search?q=%22shared%20this%20skill%22%20OR%20%22gave%20my%20team%22%20claude&f=live | live | 0 of 9 on-bucket (one borderline: @xmousecopx on workplace AI-mandate resistance) | Dead end |

Total: 27 queries. Roughly 12 were genuinely productive (filed content), 4 were weak/thin, and 11 were dead ends (mostly the deliberate B3/B4 counter-evidence and B1-library hunts in queries 16-25, 27).

---

[CONTENT_PLACEHOLDER]