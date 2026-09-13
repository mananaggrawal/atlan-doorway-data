# AI work log
Deliverable 4. Written as the work happened. Last updated 2026-09-05.

---

## 1. Approach

The operating principle was **parallel specialised research with adversarial verification**, not a single conversation with an assistant.

Instead of asking one model to "research the market," each research question was written as a standalone brief — with explicit evidence buckets defined *before* searching, a quoting standard (verbatim, ≤50 words, author + date + URL), a requirement to log null results, and a requirement to hunt for counter-evidence against our own thesis — and handed to a separate agent with its own isolated context. Ten such runs, mostly in parallel, produced ~1.56M tokens of reading that never entered the main working context. What came back was a report; what got filed was a structured evidence file with links.

The most important design choice: **every research brief included a bucket called "counter-evidence, hunt this deliberately."** Research agents are agreeable by default. If you don't commission the argument against your thesis, you won't get it, and you'll walk into the pushback round undefended.

The second: **a dedicated verification pass** whose only job was to try to refute the twelve most load-bearing claims, going to primary sources and refusing search snippets as confirmation. That pass paid for itself (see §4).

**Models and harnesses:** Claude Opus as the orchestrator holding strategy and judgment; Claude Sonnet subagents for research execution. Two browser surfaces — Claude's built-in browser pane and the Claude-in-Chrome extension against the user's real Chrome — plus a shell on the user's Mac and a cloud container. Google Drive and the local filesystem for source material.

## 2. Reusable systems built

1. **A five-bucket evidence schema** (sharing / sprawl / trust / counter-evidence / signal shape) fixed before any searching. Every one of six independent researchers filed against the same schema, which is what made ten separate runs comparable instead of ten separate essays.
2. **A research-brief template** — purpose, beat, buckets, quoting rules, null-result logging, output paths, and an explicit instruction to say "this is thin" when it is thin. Reused verbatim across all runs.
3. **A confidence-tagging convention** — `[verified]` / `[reported]` / `[assumption]` — applied per line, not per document, so a strong file can carry a weak sentence without contaminating the rest.
4. **A verification pass as a distinct role**, adversarial to the researchers, with authority to correct the record in place.
5. **A file-first discipline.** Findings are written to the project folder by the agent that found them, so nothing survives only in a chat transcript. This log, the run log and the evidence files are all outputs of that rule.

## 3. Where the AI was wrong, shallow, or misleading

Three, in increasing order of how much damage they would have done.

**a) Wrong, and caught.** A research agent reported that NVIDIA's skill scan found *"nearly 1 in 4 skills could potentially compromise a system."* Verification against the primary source showed two separate figures had been conflated: **26.1% contain at least one vulnerability**, and separately **5.2% show likely malicious intent**. "Could compromise a system" maps to the 5.2%, not the 26.1%. Presented as briefed, it would have overstated the security case by roughly 5x — in front of people who will have read the same source.

**b) Unusable, and nearly used.** Another agent surfaced "552 confirmed malicious out of ~96,000 skills scanned" as a hard base rate. The quote was accurate. The source was a self-published claim by a vendor promoting their own scanner, inside an unresolved GitHub feature request, with no linked audit. The number is now flagged in the evidence file as not usable without heavy caveat. The lesson isn't that the agent lied — the quote was real — it's that **a verbatim quote and a reliable number are different things**, and only a second pass whose job is doubt will separate them.

**c) Shallow by default.** The first landscape pass reported GitHub star counts read off summarised pages, including an implausible figure it flagged as "likely inflated." It turned out to be correct (174,457 stars) — but the agent had no way to know, because it had summarised a page instead of calling the API. Once instructed to use `api.github.com` directly, the same question produced exact, dated, reproducible numbers. Research agents default to reading *about* a source rather than *from* it, and will keep doing so unless the brief names the endpoint.



**d) Overstepped, and corrected on instruction.** Earlier in this project, the AI treated ICP and channel as things it could decide and reject alternatives for, unilaterally — writing files with headers like "Status: DECIDED" and "Rejected: [alternative]," and a decision log that read as settled rather than proposed. The brief frames this exercise around *"you are responsible for early go-to-market"* — Manan, not the AI. When asked directly, the correction was: analyze and recommend, but ICP/channel/campaign decisions get made jointly, not by the AI alone. Every affected file (`the_bet.md`, `the_campaign.md`, `decision_log.md`, `rejected_alternatives.md`, `hypotheses.md`, both READMEs) was relabeled from decided/rejected/adopted to candidate/recommended/pending-decision — no evidence or reasoning was deleted, only the claimed decision authority. The deeper lesson: an AI that produces confident, well-evidenced analysis will default to *acting* on that confidence unless explicitly told the line between "recommend" and "decide" is not its call to draw.

There was also a fourth, structural failure worth recording: **the first Reddit sweep concluded Reddit was unreachable, and it was — from that toolset.** A later run reached it through a different browser. Had we accepted the first result as final, we'd have quietly dropped the surface that produced the single most inconvenient finding in the whole project (the 99-upvote comment arguing *against* sharing skills on job-security grounds). Tool failure reads exactly like absence of evidence, and the difference has to be enforced by process, because the model will not flag it on its own.

## 4. The decision the AI could not make

**Which fact is load-bearing.**

The research produced a large amount of true, well-sourced material pointing in several directions. Every agent, asked to summarise, produced a defensible summary. None of them could tell me which single finding the entire go-to-market bet should hang on — because that is a judgment about what an audience will find persuasive and what a company can actually execute, not a fact retrievable from a source.

Three concrete calls the models could not make:

- **Killing our own best hypothesis.** The evidence supported "teams need a governed home for skills." It also showed a dozen products already claiming that exact position, one of which published a manifesto the same day we searched. The models reported both. Deciding that this *kills* the storage pitch and forces differentiation onto the evidence layer — usage, traces, evals, dependencies — was a strategic call, not a summarisation.
- **Treating a missing number as an asset.** Three agents independently reported "could not find how many skills a typical team has" as a research failure. Reading the same absence as the opening — a number nobody owns, which is simultaneously an artifact, a campaign and a distribution loop — is not something a retrieval process arrives at, because retrieval is optimised to find things, not to notice what nobody has.
- **Choosing a narrower target than the evidence demands.** The evidence supports several viable ICPs. The brief rewards picking one and defending it. Nothing in the data tells you where to cut; that comes from a view about what can actually be executed in a week.

The models were extraordinary at breadth, recall and structure. They were of no help at all in deciding what to be wrong about — and this exercise is graded on that.

## 5. What I would do differently

- Name the primary endpoint in the brief from the start (`api.github.com`, `api.npmjs.org`, the Algolia API), rather than letting agents read summaries of pages.
- Run the verification pass *concurrently* with the research rather than after it, so corrections land before the synthesis is written.
- Treat "blocked" as a task state that must be retried through a different surface before it is ever written down as "nothing found."
