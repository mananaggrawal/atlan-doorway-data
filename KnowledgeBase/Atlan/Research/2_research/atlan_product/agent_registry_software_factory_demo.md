# Atlan agent registry: Software Factory Demo

**URL:** https://youtu.be/u6x5WBkh8Cs
**Speaker/Channel:** Rohan (Product @Atlan)
**Duration:** 1:43 (103 seconds)
**Date accessed:** 2026-09-05

## Description

What happens after a developer opens a pull request?
This demo follows one PR review bot through the complete workflow:
- GitHub Actions starts the review.
- Skills stored with the code define how the bot reviews the change.
- Daytona gives the bot a controlled workspace.
- Atlan gives the bot an identity, shows the Skills synced from GitHub, and records what happened.
- Developers use trace history to propose better Skills, with human approval before the next review.

The demo uses synthetic code and data.

## Transcript

This is the software factory demo. One pull request, one governed agent, and its [music] evidence.
A developer changes the software and opens a pull request. [music] The governed agent reviews that code.
This pull request starts a PR review bot in CI. The bot follows review skills stored beside the code [music] so the team can inspect and change the review policy through the same Git workflow.
[music]
Daytona gives the PR review bot a clean [music] workspace. It reads the change, applies those skills, and returns a
changes requested decision with evidence. The review runs away from the developer's laptop. So each pull request
starts from [music] the same controlled environment.
After the review, Atlin gives the bot a durable identity. Overview shows what [music] it does and where it runs.
Relationships shows the same skills synced from GitHub, so anyone can see which review policy the bot [music] depends on.
Usage connects the CI result back to the bot. The trace shows the [music] review steps in order, which skills ran, and why the bot requested changes that gives
the team an audit trail when a review needs investigation or improvement.
[music]
A developer can pull this trace history through the ATLAN API and look for repeated misses across reviews. Those [music] patterns can become a proposed
skill update, but never an automatic rule change. [music] A human reviews the change and the next pull request uses the approved version.
[music]
