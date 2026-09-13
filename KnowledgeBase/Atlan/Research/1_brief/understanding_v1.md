# Atlan Agent Registry — Assignment Understanding (v1)
Manan Aggrawal · 2026-09-05 · supersedes v0 (`manan_understanding_v0.md`, kept for the record)

---

## 1. What this exercise is actually testing

The brief is 4 pages and reads like it wants breadth. It doesn't. Stripped down, it tests three things:

1. **Can I pick one thing and defend it under pushback?** One ICP, one channel, and a real argument for why *this* pairing works *now* — including why it beats the two strongest alternatives.
2. **Can I ship something runnable in a week?** Not a mockup. Something they can click, run, or put in front of a user. The brief says it outright: *"A polished mockup with no path to evidence is weaker than a rough working system that teaches us something."*
3. **Is my operating style with AI better than a conventional one?** Not tool count. Whether the way I work produces more, faster, with better judgment — and whether I can show the one place AI was wrong and the call it couldn't make for me.

**The trap is breadth.** A submission that surveys five ICPs, lists eight channels and asks thirty questions is a submission from someone waiting for a playbook. The role is explicitly for someone who *creates momentum without waiting for a complete playbook*. So: narrow hard, decide in public, and be willing to be wrong in a specific direction rather than vague in every direction.

**Corollary for how I engage the team.** I ask a small number of questions — only the ones whose answers change what I build. Everything else I decide myself and state as an assumption in the deck. Asking is cheap; asking a lot is a signal.

---

## 2. What the product is (in one paragraph)

A governed, cross-harness home for the *context* behind agents — skills, instructions, tools, knowledge, permissions. It gives each object a stable identity plus owners, versions, dependencies, access, usage and traces, and distributes them into Claude Code, Codex and ChatGPT through plugins and MCP. It is **not** an agent builder and **not** a harness, so adopting it requires switching nothing. The activation mechanic is a desktop app that, on first run, **scans the skills and sessions already on your laptop** — value arrives from a scan, not a migration. Individual value on day one (see your own skills, spend, traces); team value on day two (dedupe, dependencies, governed distribution). Detail and sources: `2_research/atlan_materials/product_understanding.md`.

The pain it removes appears at roughly 50–300 skills, not at 5. Atlan built ~300 skills and 40 agents internally in six months and broke on dependency drift, unclear ownership, secrets in env files, and losing context every time they switched harness.

---

## 3. What "the first 100 teams" means

Atlan hasn't defined "team" or "activated." Defining them is part of the work, not a question to send back. My definition, which I'll defend:

> **An activated team = 3+ people in one workspace where at least one skill has a named owner, a version, and usage by someone other than its author.**

Why this bar: it is the first point at which the product is doing something a folder of files cannot. One person with 40 skills is a user, not a team. Three people sharing one *owned, versioned, reused* skill is the smallest unit where governance and distribution both start to matter — and it is the exact moment the account becomes expandable.

That definition also sets the funnel the campaign has to move people through:

`install → scan (individual value) → share one skill with one teammate → second person uses it → workspace`

The hinge of the whole exercise is the third arrow. Everything before it is a solo utility. Everything after it is a land-and-expand motion.

---

## 4. The strategic tension I have to reconcile out loud

- Atlan today sells **top-down to CDOs at ~$50K ACV**. The brief asks for *"dramatic distribution before we optimize for a traditional enterprise sales motion"* — a bottom-up motion Atlan has never run.
- Atlan's own public content (three posts, 1 Sep 2026) argues that **registries alone are not enough** — buy the context layer. I'm being asked to take a registry to market.

Both resolve the same way, and this is the spine of the readout: **the registry is the free, viral wedge that earns the right to sell the context layer.** It is the first Atlan product an individual can adopt without a procurement conversation. That is the point of it.

---

## 5. The decisions I'm making (not asking about)

| Decision | Status |
|---|---|
| Definition of "team" and "activated" | **Decided** — see §3 |
| Which workload leads: coding / knowledge-worker / operational | **Leaning coding**, pending evidence |
| Primary channel | **Leaning a free open-source tool that exposes the product's own scan as a distribution loop**, pending evidence |
| What I build | Follows from the channel |
| Whether skills is the right wedge | **Accepting it**, but with a stated falsification test |

Each of these gets written as a dated hypothesis with kill criteria in `02_hypotheses/` *before* the evidence goes in, so the deck can show what was rejected and why.

---

## 6. The questions I'm actually asking Atlan

Six. Each one changes what I build; nothing else does.

1. **Can I put the desktop app in front of a real user this week — and in what state?** If yes, the campaign is a real activation funnel. If no, I build the funnel around a standalone artifact and treat Registry as the destination.
2. **Is there a public repo, an OSS component, or a slice of the ~300 internal skills I can use as a distribution seed?** A registry with nothing in it doesn't spread. Seed content is the difference between a directory and a ghost town.
3. **What does Atlan count as an activated team?** I've defined it (§3). I want to know if that's the number the company will be steered by, because the campaign optimises to it.
4. **What would falsify "skills is the wedge" for you?** The brief invites rejecting the starting thesis. I want to know what evidence would actually move you, so my experiment produces that evidence rather than decoration.
5. **What can I say publicly?** The product isn't announced. I need to know the line between "run a real campaign to real people" and "run it to my own network under NDA," because it changes the channel.
6. **Access to the strategy memo and the internal recordings** — the Google Doc 401s and I'm not sure I received the recordings the brief refers to.

---

## 7. Assumptions I'm taking rather than asking about

Stated in the deck, not sent as questions:

- Team = a group inside a company; multiple teams in one company count separately (that is how the product's workspaces work).
- Target teams both *build* and *use* skills; the ones who only consume aren't the wedge.
- The goal is a **validated, evidenced path** to 100 with the first experiments actually run — not 100 signups during the exercise.
- Pricing is not part of this. Free-to-adopt is assumed for the wedge.
- Atlan's existing enterprise customer base is **not** the channel. Using it would prove nothing about distribution.

---

## 8. What I'll submit

1. **Decision document** — ICP, channel bet, campaign, distribution loop, activation definition, next experiments. Understandable in 15 minutes.
2. **The thing built** — runnable, with instructions.
3. **Evidence appendix** — sources, discovery notes, assumptions, rejected alternatives, with confidence tags on every claim.
4. **AI work log** — approach, reusable systems built, one place AI was wrong, one decision AI couldn't make. Written as the work happens, not reconstructed.

---

## 9. What would make this submission bad (my own guardrails)

- A deck with no artifact behind it.
- An ICP that is a list of departments rather than a group with a trigger.
- A channel chosen because it sounds non-linear, with no evidence the audience behaves that way.
- Numbers in the deck I can't trace to a source with a date.
- An AI work log that reads like a tool inventory.
