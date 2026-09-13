# Alternatives analyzed
**AI analysis, not decisions.** What the analysis argues against, with the strongest honest case for each kept intact rather than dismissed — presented for Manan's call, not settled by AI. Feeds the evidence appendix — the brief asks for this explicitly.

---

## Analysis argues against: pitch the registry as a governed home for skills (storage positioning)
**The case for it:** it is what the product literally is, it is how Atlan's own demo opens, and the pain is real and documented.
**Why the analysis leans against it:** the position is crowded and commoditising. shareskills.ai, Tessl, JFrog's Agent Packages registry, AWS Agent Registry (GA 31 Aug 2026), Google's Gemini skill registry, and roughly a dozen "package manager for agent skills" Show HNs since January are all claiming it, none of them winning. Storage is table stakes within two quarters.
**What we do instead:** lead with the evidence layer — usage, traces, evals, dependencies — which AWS's own launch blog defers to roadmap and which nobody currently ships for skills.

## Analysis argues against (for now): enterprise AI-enablement leader as the first ICP
**The case for it:** the title exists and is named at Toyota, Ford, Deloitte, Mubadala and Eightfold; they own budget; they have the reporting pain the product's dashboard is built for.
**Why the analysis leans against it as *first*:** on LinkedIn, expert posts about skill governance get 4-5 reactions while beginner explainers get 400. The persona is real but the moment isn't. They are the budget owner for the expansion, not the wedge.
**Revisit when:** individual and small-team adoption produces the usage data that makes the enterprise conversation concrete.

## Analysis argues against: Atlan's existing enterprise customer base as the channel
**The case for it:** warm, fast, high conversion, immediately available.
**Why the analysis leans against it:** it would prove nothing about distribution. The brief asks explicitly for dramatic distribution *before* optimising for a traditional enterprise sales motion. Using the installed base answers a different question than the one being asked.

## Analysis argues against: a public skills directory or marketplace play
**The case for it:** it is the obvious analogue, the install loop is proven, and the brief lists it as a prompt.
**Why the analysis leans against it:** skills.sh already has 1.32M all-time installs and 30K+ GitHub stars behind Vercel's distribution. We cannot out-distribute that in a week. More importantly, a directory does not create the arrow we need — from one person's skill to a second person using it — and the existing directories are already criticised for exactly the thing a directory cannot fix: *"Skills.sh has no quality control. Anyone can create a skill, host it on GitHub, and tell people to install it."*

## Analysis argues against: growth-hacking the AWS Agent Registry launch
**The case for it:** the brief raises it, AWS just went GA (31 Aug 2026), the old namespace retires 17 Sep 2026 forcing migration, and their roadmap gaps are publicly documented.
**Why the analysis leans against it:** partner motions run on quarters, not weeks; the audience is AWS-account-scoped, which excludes teams whose skills live on laptops and in GitHub; and it would make Atlan a line item in someone else's roadmap. Worth revisiting as a second-wave motion with a genuine technical integration.

## Analysis argues against: sending Atlan thirty clarification questions
**The case for it:** thoroughness, and the brief does invite questions.
**Why the analysis leans against it:** the role is for someone who moves without a complete playbook. Six questions that change what gets built, and stated assumptions for the rest, is the stronger signal.

## Held open, not rejected: Reddit as a launch surface
r/claudeskills is small (66K) but dense and purpose-built, with 750+ upvote posts on exactly this topic, while the large general subs are showcase-dominated. Viable for a well-crafted "I built X to solve Y" post, not for a governance pitch.
