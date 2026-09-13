# WTF Is the Context Layer? The Missing Infrastructure for Production Agents

**URL:** https://www.youtube.com/watch?v=8G_1-3IO4ZQ
**Speaker:** Prukalpa Sankar, Founder & Co-CEO, Atlan
**Channel:** AI Engineer
**Duration:** 20:53 (1253 seconds)
**Date accessed:** 2026-09-05

## Description

In the last two years, models have gotten exponentially smarter. Two years ago they couldn't pass the bar. Today, top 1% of test scorers. And yet most agents still can't answer a simple business question correctly. You ship a demo that works. You deploy it. The business abandons it in a month.

The missing variable is context: the business definitions, procedural knowledge, and operational norms that make a human expert valuable.

Drawing on hundreds of production deployments, Prukalpa Sankar will break down what it actually takes to give agents contextual intelligence — and get them past the demo stage.

She'll walk through the architecture of a context layer: how context repos work (versioned, testable, portable), how simulation environments catch failures before deployment, how agent traces compound back into shared context, and why context engineering scales where fine-tuning and prompting don't. She'll also cover why your context needs to be open (MCP, Iceberg, deploy to any framework) — and what happens when it isn't.

### Speaker: Prukalpa Sankar
Founder & Co-CEO, Atlan. X/Twitter: https://x.com/prukalpa · LinkedIn: https://www.linkedin.com/in/prukalpa

Prukalpa Sankar is the Founder & Co-CEO of Atlan, the context layer for AI. She's been early to a defining idea of the AI era: context is king. AI systems are only as good as the business context behind the data they rely on. Under her leadership, Atlan has become a Leader in the Gartner Magic Quadrants for both Data & Analytics and Metadata Management, serves 300+ enterprises including Mastercard, GM, JPMorgan Chase, and Nasdaq, and has raised $200M+ from Sequoia, GIC, and Salesforce Ventures. Before Atlan, Prukalpa co-founded SocialCops, the world's largest government data lake powering the UN's SDG monitoring — recognized by the New York Times and the World Economic Forum. She's been featured in Forbes 30 Under 30 and Fortune 40 Under 40.

### Timestamps / Chapters
- 0:12 Introduction: The Context Moment
- 1:51 Why AI Agents Struggle with Business Context
- 3:19 Performance = Intelligence + Context
- 4:27 The Human Learning Model: Lessons from Maya
- 7:20 Evolution of Agent Architecture at Atlan
- 10:00 The Challenges of Isolated Agent Systems
- 11:06 Transitioning to General Purpose Agents
- 12:43 Marketing Team Case Study: The Context Layer
- 14:36 The Challenges of Context Engineering
- 15:31 Defining the Context Layer: The GitHub for Context
- 16:43 Compounding Learning Loops and Traces
- 17:18 How to Start Building Your Company Brain
- 18:07 Defining the Context Layer Architecture
- 19:31 Conclusion: Context is IP

## Transcript

[music]
Chapter 2: Introduction: The Context Moment
Hi everyone. Uh my name is Praalpa. I'm the founder of Atlan. Um and uh today I'm going to talk about this thing where
context is having its moment. Uh and so my goal today is to talk about like WTF
is the context layer. Um, just before I start, and I promise this is the last time.
Um, I don't know if the clicker is working.
Atlin, we it's it's working. Yeah. Thank you. Um the problem we solve is we say AI doesn't know your business. We fix
that. We work with an incredible group of companies around the world ranging from GitLab and Zoom and Discord and Affirm to large enterprises like
Mastercard and General Motors. Um and about a year ago, uh my co-founder and I
went on stage and we said, uh at the dawn of the internet era, Bill Gates had written this very famous blog post and
it said content is king. Um and as we or the dawn of the agentic era, context
will be king. Um since then it feels like 2026 is the year of context.
context graphs anyone um uh you know every every two days you see some version of context uh popping up and so
what is going on um I believe the answer to this kind of is in this reality distortion field that we
Chapter 3: Why AI Agents Struggle with Business Context
live in uh I live here in the Bay Area every day or two I have conversations with people which kind of go like how
far are we from AGI and we have a debate and we're like well one year three years so on uh There is no doubt that the models are getting exponentially smarter
by the day. Uh two years ago they couldn't pass the bar. Today if they were to take the bar it was they're the top 1% of test scorers. On the other
hand they're not exponentially more useful by any benchmark. Uh one out of five you know AI use cases actually make
it to production. U you know 56% of CEOs say that there's zero financial benefit from AI today.
So what's going on? I believe hidden in plain sight is actually um how performance is measured in the human
world. Uh cognitive intelligence doesn't really determine real world effectiveness. Uh in fact only 10% of
job performance variance is explained by IQ. Like just think about it. Would you say your smartest um you know teammate
who scored the highest on the SATs is also your best teammate or would you say no it's the person who works the most
and takes the most feedback and learns the fastest in the real world we care about
performance and performance is outcomes that you deliver in the real world and performance is a function of two things it's a function of intelligence which is
Chapter 4: Performance = Intelligence + Context
cognitive horsepower that's what the model benchmarks measure every day But it's also a function of context. This is what they say in the human world as
learning on the job, right? Knowledge and skills and expertise that you learn over time.

[CONTENT_PLACEHOLDER]