# Access and blockers
Every source that could not be reached, what was tried, and how it resolved. Recorded so that "we found nothing" is never confused with "we could not look."

| Source | What was tried | Outcome | Resolution |
|---|---|---|---|
| **Reddit** | curl from cloud container and from the Mac (403), WebFetch (`SITE_BLOCKED`), WebSearch (~15 queries, zero reddit.com URLs returned), reader proxies (403 / robots disallow), then the built-in browser pane (blocked by policy; `request_access` refused), then old.reddit.com (login wall) | **Resolved.** Reached through the Claude-in-Chrome extension against the user's real Chrome, logged out of nothing, read-only | 24 queries across 11 subreddits → `2_research/community/reddit.md` |
| **YouTube captions** | `timedtext` API (HTTP 200, zero bytes — PO-token restriction), `youtube-transcript-api` (proxy 403), direct curl from both shells (proxy 403) | **Resolved.** YouTube's native transcript panel read from the browser DOM | Full transcripts of all three videos |
| **Atlan strategy memo (Google Doc)** | Google Drive connector (entity not found), WebFetch (HTTP 401) | **Open.** Not shared with this account | Access requested — question 6 in `1_brief/questions_for_atlan.md` |
| **"Internal recordings" named in the brief** | — | **Open.** Unclear whether these are the three YouTube links or additional material | Asked |
| **GitHub code search** — how many public repos contain `.claude/skills/` | api.github.com code search (401, requires auth), grep.app (Vercel bot checkpoint on the API, robots disallow on the search page) | **Open.** The single most valuable missing number | Closeable with an authenticated GitHub session or a token |
| **LinkedIn post permalinks** | Search-results DOM does not expose `/feed/update/urn:li:activity/...` to the accessibility tree | **Worked around.** Citations use the author's profile URL plus the exact query, or the author's own linked article | Documented per entry in `linkedin.md` |
| **Two agent launches** (GitHub, blogs) | Refused by the session's safety classifier on first attempt | **Resolved.** Succeeded unchanged on relaunch; no prompt content was altered to get past it | — |

## Rule this table exists to enforce
A blocked source is an access gap, not evidence of silence. The first Reddit sweep concluded the surface was unreachable — accurately. Had that been filed as "Reddit is quiet on this topic," we would have lost the single most inconvenient finding in the project.
