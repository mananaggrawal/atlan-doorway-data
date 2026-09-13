# Research findings (public evidence, pulled 2026-09-05)

Research across GitHub, Hacker News, Reddit, X, LinkedIn, blogs and vendor security research, with an independent verification pass.

## Four findings that shape the bet

1. **The sharing pain is real and documented — and Anthropic declined to fix it.** `anthropics/claude-code#28327` asks for team skill sharing, has two duplicate issues, and was itself closed `not_planned`. The reported friction threshold is roughly 5 engineers, not 50.
2. **The wedge is not unclaimed — this hypothesis was killed.** shareskills.ai, Tessl, JFrog Agent Packages, NVIDIA SkillSpector, AWS Agent Registry (GA 31 Aug 2026), Google's skill registry, plus roughly a dozen "package manager for agent skills" Show HNs since Jan 2026 — none winning. Consequence: differentiation can't be storage; it has to be the evidence layer (usage, traces, evals, dependencies), which AWS explicitly defers to its roadmap and Atlan already demos.
3. **The do-nothing case is real.** The baseline is "a git repo plus Anthropic's native plugin marketplace, DIY." The sharpest objection is conditional and answerable: elaborate tooling only pays off past a specific friction threshold. A 99-upvote Reddit comment argued against sharing skills at all on job-security grounds — which argues for leading with individual payoff, not team altruism.
4. **Nobody has published how many skills a typical developer or team has.** Three researchers looked; it doesn't exist publicly. Treated as an asset (a number Atlan could own), not a gap to apologize for.

## Verified anchor numbers (pulled 2026-09-05)

- Claude Code skill listing takes 1% of the context window; 1,536 characters per description.
- `@anthropic-ai/claude-code`: 80.2M npm downloads/month.
- JetBrains Aug 2026 survey (n>15,000): 90% of developers use AI coding agents weekly; Claude Code at 39% global / 47% US.
- skills.sh: 1,320,673 all-time installs. `anthropics/skills`: 174,457 GitHub stars.
- NVIDIA scanned 42,447 skills: 26.1% with at least one vulnerability, 5.2% likely malicious.

Two corrections caught during verification: the NVIDIA figure was originally miscited as "nearly 1 in 4 could compromise a system" (conflated two statistics, overstating the security case ~5x), and a "552 malicious of 96,000 scanned" figure is a vendor's unverified self-report in an open GitHub issue — unusable without heavy caveat.

## Channel read

GitHub is the highest-precision surface: small n, very high intent, named people. X is listening/discovery, not acquisition — most on-topic posts get under 500 views. LinkedIn has the right persona ("AI Enablement" roles at Toyota, Ford, Deloitte, Eightfold) but the wrong energy — expert posts get 4-5 reactions. r/claudeskills is small (~66K members) but dense and purpose-built.