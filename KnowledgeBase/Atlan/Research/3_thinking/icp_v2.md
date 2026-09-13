# ICP v2 - narrowed for DRAMATIC REACH
Status: RECOMMENDATION, 2026-09-08. Not signed off. Supersedes the ICP framing in the_bet.md.
Evidence: 2_research/round2_sep8/ and round3_sep8/.

## THE REACH EQUATION, WITH THE NUMBERS WE NOW HAVE
reach = population x pain density x reachability x PROPENSITY TO BROADCAST x BRANCH FACTOR
Round 3 supplied the last two terms, which we had never measured.
- EXTERNAL sharing beats INTERNAL by 3-4 orders of magnitude. One publishing act by an
  audience-holder = 10^5 (superpowers: 282,771 stars from ONE Simon Willison writeup, one day after
  launch). One internal sharing act = 10^0-10^2.
- A skill pack CONVERTS EXISTING TRUST; IT DOES NOT CREATE IT. Corey Haines turned a 77,000 owned
  audience into 4.7M installs (61x). ColdIQ, with a paywall and no owned audience, got 269 stars.
  So we must reach people who ALREADY HAVE AUDIENCES - we cannot manufacture one.
- Solo -> second-person-in-same-org is ~4% with an invite button, and 40-70% WHEN THE RECIPIENT MUST
  OPEN THE ARTIFACT TO DO THEIR OWN JOB. That 10-20x ratio is the only number worth designing around.
- Highest measured broadcast intensity of ANY cohort: AGENCY OPERATORS. ColdIQ turned 24 employees
  into 581 LinkedIn posts in 90 days -> 71,603 engagements -> 27 clients, $151K new MRR.
  0.27 posts/person/day SUSTAINED. No engineering org has a measured equivalent.

## THE RECOMMENDATION
*** PRIMARY ICP: THE FIRM THAT BILLS FOR A REPEATABLE DELIVERABLE. ***
Marketing and creative agencies · GTM/outbound agencies · dev shops · MSPs · boutique consultancies.
5-80 people. BYO-agent (no central enterprise plan). Serving 10-50 client organisations.

THE UNIFYING PROPERTY: they sell the SAME PROCESS to MANY CUSTOMERS, so their skills are
simultaneously their MARGIN and their INVENTORY. Nobody else on earth has that property.

## WHY THIS WINS ON REACH, SPECIFICALLY - five structural properties
1. *** THE PRIVACY CONSTRAINT INVERTS. *** Every other ICP refuses to let the skill travel - that is
   what killed the badge/score/scrubbed-run loop options. THE AGENCY WANTS ITS SKILLS TO LEAVE THE
   BUILDING, branded, versioned and metered, because that is a SALE. The sensitive object travels BY
   DESIGN, and the registry is what makes it safe to travel. This is the only cohort where the loop
   and the value proposition are the same thing.
2. *** BRANCH FACTOR AT THE FIRM LEVEL, NOT THE SEAT LEVEL. *** One agency is a hub to 10-50 client
   orgs plus 5-80 staff plus a public audience. Every agency->client handoff CREATES A NEW
   ORGANISATION on the registry. Compare: 500 engineers x 4% invite = 20 second seats.
   500 agencies x 5 clients = 2,500 NEW ORGS, each with their own internal spread to follow.
3. *** THEY ARE THE ICP AND THE CHANNEL SIMULTANEOUSLY. *** They broadcast harder than any cohort
   measured, and they do it UNPROMPTED, because publishing their workflow IS their lead generation.
   Clay's entire growth ran on exactly this and DELIBERATELY WITHHELD affiliate payouts until $5M ARR
   - "paying converts an evangelist into a contractor and kills the credibility that made the
   broadcast work."
4. *** GOVERNANCE IS STRUCTURALLY FORCED, NOT SOLD. *** Multi-tenant from day one: per-client skill
   variants, a contractual obligation to prove what context touched whose data, and staff churn far
   above product-company rates. Everything Atlan sells top-down to a CDO at $50K, an agency needs on
   day one to keep a client. We are not persuading them governance matters - their contract already did.
5. *** THEY SPAN CODE AND NON-CODE, so the CEO's signal is satisfied WITHOUT splitting the ICP. ***
   A marketing agency IS a marketing team, at higher intensity and with the incentive fully aligned.
   The unit of analysis becomes the FIRM, not the function - which is what lets us keep ONE ICP.

## THE EVIDENCE THIS RESTS ON
- THE QUOTE (r/agency, 8 Jun 2026, 62 comments) [verified]: "our people are still our number one
  asset, but honestly THE NUMBER TWO ASSET AT THIS POINT IS OUR CLAUDE SKILLS... we've put THOUSANDS
  OF HOURS into them now... lately I'm getting CLIENTS STRAIGHT UP ASKING IF THEY CAN JUST HAVE THE
  AI... I DON'T REALLY HAVE A GOOD WAY TO DO THAT RIGHT NOW, but even if I did I HAVE NO CLUE HOW I'D
  PRICE IT." Top reply (21 upvotes): "Training or handing over materials that allow them to get your
  work... is worth an astronomical amount."
- THE COHORTS THAT ACTUALLY SHOW UP ON REDDIT ARE EXACTLY THIS SET [verified]: r/consulting (435
  upvotes / 115 comments), r/msp (72/128), r/agency (11/62), r/revops. NULL results in r/marketing,
  r/sales, r/PPC, r/FPandA, r/accounting. The cohorts that engage are the ones who BILL FOR A
  REPEATABLE DELIVERABLE.
- AND THEIR DEMAND GOES UNFILLED [verified]: on the 435-upvote r/consulting thread, of the top 25
  comments, NOT ONE contains a skill, a repo or a file. "I can share but easier to just build your
  own." "share skill pls" - unanswered.
- BROADCAST INTENSITY [verified]: ColdIQ 24 people / 581 posts / 90 days / $151K MRR.
- THE STRUCTURAL PRECEDENT: Clay. A technical product sold to non-engineers who broadcast to win
  their own clients, which INVENTED THE JOB TITLE OF ITS OWN BUYER. GTM-engineer postings +205% YoY
  with Clay named in 55%. ~$100K ARR (2021) -> $100M (Q4 2025).

## THE EXPANSION MAP (one primary, others sequenced - per Manan's instruction)
1. The agency's CLIENT ORG - arrives already holding a governed pack, pre-sold by someone they pay.
2. The in-house team that behaves like an agency - RevOps, sales enablement, internal creative studio.
   Same repeatable-deliverable shape, one internal client instead of many.
3. Engineering at those same orgs - arrives when the pitch is DRIFT and PORTABILITY, never versioning.
4. Finance / legal / ops - best-articulated pain (Anthropic's own finance team, ~150 skills,
   "versioned, not lost when somebody moves on"), worst reachability. Arrives via case study.

## HONEST RISKS - all of these must be in the readout
R1. POPULATION IS UNSIZED. We have no credible count of agencies/MSPs/consultancies deep enough in
    agent skills to qualify. Every other ICP candidate has at least a modelled TAM. This one does not
    yet. MUST BE FIXED BEFORE THE READOUT.
R2. LOW ACV, FAR FROM ATLAN'S MOTION. Agencies are the opposite of a $50K CDO sale. The defence is
    that the brief explicitly asks for dramatic distribution BEFORE optimising for enterprise sales -
    but the tension is real and should be named, not hidden.
R3. IP PARANOIA IS UNTESTED. Whether an agency will let its most valuable asset sit on a vendor's
    registry is an ASSUMPTION, not a finding. It is the single biggest kill risk in this bet and
    it is the thing to design the first experiment around.
R4. THE CEO NAMED marketing/sales/pre-sales TEAMS, not agencies. Agencies are adjacent, arguably a
    purer instance, but it is a reinterpretation of her signal and must be presented as one.
R5. "AGENCY" MAY READ AS TOO SMALL/UNSERIOUS to an enterprise data-governance company. Framing it as
    "the firm whose product is repeatable expertise" - which includes Big-4-adjacent consultancies
    and MSPs - is the mitigation.

## WHAT THIS MAKES THE WEDGE
NOT "help me share" and NOT "find your dead skills" (/skill-doctor shipped 4 Sep 2026).
*** "MY CLIENTS ARE ASKING TO BUY MY AI AND I HAVE NO WAY TO HAND IT OVER." ***
The only pain found in any cohort where THE SUFFERER IS TRYING TO MAKE MONEY, not save time.
And it is a distribution loop by construction: every handoff creates a new organisation, and the
recipient's first action - installing the pack to do work they are already paying for - lands in the
40-70% band rather than the 4% band.
