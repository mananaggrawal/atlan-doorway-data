# AI distribution loops, 2024 - mid 2026
Research run 2026-09-08. Question: what loops sat ON TOP of a core product and produced dramatic
distribution at near-zero cost? Extract the mechanic, not the story.

## Archetypes, ranked by cost to produce a SECOND user (cheapest first)

| # | Archetype | Marginal cost of 2nd user | Requires | Compounds |
|---|---|---|---|---|
| 1 | Forced output-embed (Gamma, Lovable, Canva) | ~$0, impression is a byproduct of work already being done | a human-visible output shared as the job-to-be-done | yes |
| 2 | Metadata badge (shields.io, coverage/CI) | ~$0.000x, an SVG endpoint | a public surface the user controls + a number worth boasting | yes |
| 3 | One-click reproduce (Deploy button, npx, Run in Postman) | ~$0, third parties paste your install line into their docs | a copy-pasteable install primitive + a namespace | yes |
| 4 | Third-party directory / awesome-list | $0 to you, someone else does the labour | a category worth curating | until saturated |
| 5 | Public artifact + remix (Artifacts, Lovable gallery, Figma Community) | low, hosting per artifact | the object must be SAFE TO PUBLISH | yes |
| 6 | Contributed template library (n8n, Zapier) | medium, moderation + creator incentives | scrubbable templates + creator payment or status | slowly |
| 7 | Comparative scorecard - grader / leaderboard / Wrapped | medium-high, real scoring engine + credibility | data you already hold + defensible methodology | grader+leaderboard yes; Wrapped no (burst) |

## The one pattern that recurs in every loop that worked
The shared object must be independently useful to the RECIPIENT, and the recipient's FIRST ACTION
on it must require an account. Not "see our logo" - "click here and this thing becomes yours."
Vercel's Deploy button creates the repo AND the account in one click. Postman's Run button forks
the collection into the recipient's workspace. Claude remix opens an editable copy.
Corollary: the best loops are parasitic on a task the user was going to perform anyway
(publishing a deck, shipping an app, writing a README). Loops that require a NEW altruistic act
need paid incentives to run at all - which is why n8n pays creators and Zapier built the pages itself.

## The recurring reason loops fail
The shared object carried something the user did not intend to share, and the operator killed
its own loop. OpenAI removed indexable ChatGPT share links Aug 2025 after ~4,500 shared
conversations surfaced in Google, some with personal detail. [reported, multi-source]
shadcn has to warn users to audit third-party registry code. [verified]
Second failure mode: neutrality collapse - a leaderboard run by the vendor selling the scored thing
gets discounted (LMArena and SWE-bench work partly because they are not vendors).
Third: non-compounding attention (Cluely - outrage marketing, founder's own word "rage bait", not a loop).

## THE CONSTRAINED CASE: the object is sensitive and will NOT be shared
Rules out #1 and #5 outright. Surviving precedents, strongest first:

(a) SCORE WITHOUT ASSET
- shields.io: 1.2M public GitHub READMEs carry a badge; >1B badge requests/month; 40M+ in one day
  at peak; ~2TB/month; funded by donations. [verified, primary: github.com/badges/shields/discussions/8867]
  The badge is a claim about POSTURE. Nobody sees your test suite, they see "coverage 94%".
- ccusage + viberank: `npx ccusage` parses on-disk logs from 18+ coding agents locally;
  `npx viberank-cli` uploads ONLY cost/token totals to a public leaderboard - code and prompts
  never leave the machine. ccusage 18.4k stars / 819 forks. Viberank: 1.2K devs, $13.2M tracked
  spend, 15.1T tokens. [verified] Small in absolute terms, but exactly the right SHAPE, and it is
  the 2026 AI-native proof that developers will publish work metadata when extraction is provably local.
- Vanta trust centers: an entire B2B category for publishing "we are compliant" without publishing
  the SOC 2 evidence. [verified product exists]
- HubSpot Website Grader: 2M+ URLs graded. [reported, company blog] Still the dominant B2B free-tool
  shape in 2026 (Semrush AI Search Visibility Checker). [verified]

(b) SHAPE WITHOUT CONTENT
n8n 12,145 community workflow templates [verified live count]; Postman public collections.
Both are "here is the wiring, bring your own keys." A skill's shape - trigger conditions, tool list,
permission scope, review status, file layout - is publishable when its body is not.

(c) CONTRIBUTION-GATED AGGREGATE
levels.fyi: multi-million-user product out of individually sensitive salary data by making
contribution the price of access. DORA quartiles do the same for engineering telemetry.
Mechanic: no single org's data is legible, the aggregate is, and you must contribute to see where you sit.

(d) RANK ON A SHARED BENCHMARK
LMArena 3.5M+ human preference votes, 1M+ unique visitors/mo, $100M seed at $600M val May 2025
(a16z + UC Investments). [reported/verified] The labs, not the users, do the amplification.

## B2B / dev-tooling loops that hit dramatic distribution at near-zero cost
1. shields.io badges - 1.2M READMEs, >1B req/mo, run on donations. [verified]
2. npx one-liners - ccusage to 18.4k stars from one copy-pasteable command. [verified]
3. Awesome-lists - punkpeye/awesome-mcp-servers 90.9k stars / 13.2k forks;
   hesreallyhim/awesome-claude-code 53.1k stars / 4.6k forks. [verified, Sep 2026]
   Third parties built the entire MCP discovery layer for free.
4. Deploy / Run-in-X buttons - Netlify 2016, Vercel Nov 2019, Postman. Mechanics verified;
   NO vendor has ever published button-attributed signups. [verified absence]
5. n8n 12,145 templates [verified]; Zapier integration-page SEO (mechanic verified, traffic numbers
   are growth-blog reconstructions only - do not cite).
6. shadcn/ui registry + CLI: `npx shadcn add @<registry>/<component>`, third-party registries built
   into the CLI with no configuration. Closest structural analogue that exists today, and its own
   stated weakness - "Community registries are maintained by third-party developers. Always review
   code on installation" - is the governance wedge. [verified]

NOT ONE of these six publishes the customer's proprietary content. They publish a number, a button,
a link, or a scrubbed template.

## Numbers to be careful with
- Gamma "50% of subscriber growth from word of mouth" - company-stated, relayed via Business Insider,
  no primary Gamma source found. $100M ARR / 70M users / $2.1B val (10 Nov 2025) is a press release. [reported]
- Lovable $200M ARR, 8M users, 60M projects, 900M monthly visitors to Lovable-built sites (Aug 2026)
  - all press-relayed company figures. [reported] The 900M is the badge-impression volume, and is
  the load-bearing one if citing the badge loop.
- Spotify Wrapped 2025: 200M engaged users in ~24h, ~500M "shares" - all Spotify-claimed, and their
  share definition includes screenshots. No independent lift figure exists. [reported]
- Sora invite-code launch: topped US App Store 3 Oct 2025 [reported, CNBC headline]. Scarcity converts
  existing demand, it does not create it. Low transferability.
- Perplexity Pages, NotebookLM Audio Overviews, Loom, HeyGen, ElevenLabs, Suno, Clay: mechanics
  well-known, every growth number reachable is a growth-blog reconstruction. Do not cite as evidence.
