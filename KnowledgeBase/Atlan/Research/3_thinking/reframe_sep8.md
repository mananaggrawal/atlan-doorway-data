# Reframe, 8 Sep 2026 - what Atlan HR and the CEO actually said
Status: OPEN. Nothing below is signed off. This supersedes the emphasis in the_bet.md and
the_campaign.md, it does not yet replace them.

## THE FEEDBACK
FROM ATLAN HR: the submission deviated from the purpose of the assignment. The purpose is
(a) A CRYSTAL-CLEAR ICP and (b) A CAMPAIGN WITH AN INSTALLATION FLOW / DISTRIBUTION LOOP.
"The solution came too early." -> we jumped to Atlan Pulse before the ICP work justified it.

FROM THE ATLAN CEO:
1. She told the story of the company's inception and how the Registry came to life.
2. THE AGENT REGISTRY IS ONLY BEING USED INTERNALLY. There is no real customer base and no
   good-quality demand signal from it. EVERYTHING IS THEREFORE A BET ON PUBLIC INFORMATION.
   -> our research is the right instrument; go deeper on it, and say plainly that it is a bet.
3. USAGE OF A PRODUCT LIKE THIS IS HEAVILY DRIVEN BY PEOPLE WHO WORK ON THINGS EXTREMELY UNIQUE TO
   THE COMPANY. Named examples: marketing teams, sales teams, pre-sales teams. Not only coding.
4. Coding is the deepest penetration of AI in orgs, followed by voice. So registry-like products may
   see high usage in AI-native orgs.
5. THE OBJECTIVE IS THE MOST DRAMATIC DISTRIBUTION POSSIBLE.
6. Overall signal: the direction was good.

## WHAT THE ROUND-2 RESEARCH DID TO THAT FEEDBACK (see 2_research/round2_sep8/)
CONFIRMED, HARD: 91.3% of Claude Cowork usage is NON-CODING; software dev is 8.7%. Anthropic's own
data, Jul 2026. The CEO's instinct is not a hunch, it is measurable.
CONFIRMED, HARD: coreyhaines31/marketingskills = 44,769 stars and 7,026 FORKS. The repo's own README
says skills read "a foundational product-marketing context file... your company's unique positioning"
and the install path is "fork and customize." 7,026 forks IS "extremely unique to the company",
quantified, in public, with names attached.
CONFIRMED, HARD: Anthropic's own FINANCE team runs ~150 shared Claude skills, written by accountants
and FP&A analysts, not IT - and the customer's own words are "skills are versioned, NOT LOST WHEN
SOMEBODY MOVES ON." A non-code team stating the Atlan pitch.
CORRECTED: "coding then voice" is right on SPEND and wrong on SPRAWL. Voice context lives inside a
vendor's console (Sierra, Decagon, Parloa). NOBODY ACCUMULATES 50 SKILL FILES BUILDING A VOICE AGENT.
Menlo's departmental spend table has no voice line at all. Reorder to: coding >> GTM > voice, where
the metric is "does a human accumulate portable context artifacts."
KILLED: the sharing hypothesis, as worded. Top sharing issue 151 reactions vs 6,592 for portability.
skillshare (sync framing) 2,629 stars vs sx (sharing framing) 287. The modal reply to a dedicated
sharing product on HN was "what's wrong with git?". Manan's instinct was right.
NEW AND URGENT: /skill-doctor SHIPPED IN CLAUDE CODE 2.1.261 ON 4 SEP 2026. It reports per-skill cost
and invocation counts and flags never-invoked skills. THAT IS SUBSTANTIALLY ATLAN PULSE, SHIPPED BY
THE VENDOR, FOUR DAYS AGO. This must be resolved before Pulse is defended in a readout.

## CONSTRAINTS AND PERMISSIONS SET BY MANAN, 8 SEP 2026
- NO DEADLINE. Atlan has not scheduled the session. Optimise for the quality of the bet, not speed.
- ONE PRIMARY ICP plus an expansion map. Not two co-equal ICPs.
- The fate of Atlan Pulse is DEFERRED until the ICP work lands.
- The ICP must be crystallised DEEPLY: tools they use today, software, team size, and so on.
- BYO-agent orgs (people choose their own agents, no central enterprise plan), typically startups.
- Authorised forward assumptions: models keep getting better; AI needs to go multiplayer.
- No further primary interviews planned; the existing n=4 stands (see manan_primary_interviews.md).

## THE THREE OPEN QUESTIONS THIS REFRAME CREATES
Q1. Which ICP is primary - the GTM/sales-enablement builder (differentiated, matches the CEO,
    reachable, but ~2k people) or the coding team (largest, most evidenced, but crowded and
    partially served by /skill-doctor)?
Q2. If sharing is not the wedge, what is - portability across harnesses (loudest, provable),
    change control (what the sharing issues actually say), or instrumentation (vendor-validated,
    not user-voiced)?
Q3. What loop survives the constraint that the object is proprietary and will NOT be shared?
    The surviving archetypes are: metadata badge, one-click reproduce of scrubbed shape, and
    contribution-gated aggregate. See 2_research/round2_sep8/distribution_loops.md.
