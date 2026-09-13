# Atlan Pulse — landing page conventions

**Standing rule: the page describes a CLI/product that exists, so every claim on it must be checkable by actually running the product.** It has drifted from the real build before — features described that were never shipped (a `--contribute` flag, a downloadable share card) had to be removed once caught. Before editing this page again, run the current product and diff the page's claims against the actual output.

**Copy is deliberately bare, on explicit instruction:** don't name competitors, keep it simple about what the command does, crisp and action-oriented lines. No competitor names, no research citations, no stats from the evidence work anywhere on this page — that material belongs in the submission deck, a different audience, where naming the competitive field is correct.

**Structure:** hero (real terminal output + copy button) → the core pain line → the checks the tool actually runs → three-step usage → a behaviour strip (local & read-only, works with existing folders, nothing to install) → the pack/install share loop → call to action → footer disclosure.

**Design tokens** (extracted from Atlan's own site): Funnel Display for headings, Inter for body text, JetBrains Mono for terminal output; Persian Blue as the primary accent, with a pink accent reserved for exactly one interactive/risk element. Atlan's own logo is not used on this page.