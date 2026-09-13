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

And in the last decade, uh we have compounded on one of those parameters.
Uh intelligence has thousandxed in the last decade. Just in the last 6 months, we have 2xed on that axis. On the other
hand, context, the situated knowledge of your business, that's barely moved.
We've moved some data to the cloud uh but that's about it. It's otherwise logged in dashboards and Slack threads
and uh the head of that analyst who might be leaving next week. Um and so the question ahead of us and I
really believe this is the next frontier is how do we help AI build context about our business? Um, and every time I'm
faced with a question about how do we help AI do this, I always like to go back and understand how did we help humans do this? Uh, so I'm going to take
Chapter 5: The Human Learning Model: Lessons from Maya
you into the life of, you know, a u exemplar employee Maya. Uh, let's say she's a data analyst at Mech Context
Burgers because I thought I was going to be creative and I'm not very creative.
Um, and you know, let's say she's that analyst that everybody, you know, pings in your company. Uh, right? She's the
person that everybody sends a message to every morning when they're trying to solve a problem. So, let's say this morning, uh, there's a franchisee owner
who sends her a message and says, "Why is my drive-thru time up this week? Why is this metric up this week?" Sounds
like a really simple question. Um, but it's actually a really complicated question to ask.
Just to answer this one very simple question, Maya first needs to know uh what is drive-through time uh and who's
asking? Is it finance or is it you know my ops team? And it might mean different things. Uh but not just that, what does
this week mean? Is the cutoff period Monday to Sunday? Is it Pacific time? Is it Eastern time? Uh that's knowledge.
Like that's facts. That's the map of the business. Um but not just that. Uh there's expertise uh right there's um
you know a diagnostic playbook. What what does a great analyst do? They know that you know quarter 3 is a season seasonal quarter because of weather
patterns and they know to go check if the reason there's a spike is because of seasonality. They also know that the
company launched a product uh just that previous quarter and so they know to check if that's why the root cause
analysis failed. Uh this is expertise and skills that people pick up over time as they learn on the job. Uh and then
there's norms, right? Um there's, you know, persona scoping. Who's asking the question? How do I answer this question?
Um and Maya, she's one of those like cool people. She nails it. She sends an answer not just with the answer, but with the why and the root cause, and she finds the reason for it.
How did Maya learn to do this? Um she just joined the company a year ago. Um first Maya you know has for like she
joined and she got some training like all of us do but that's not where any of us learn right in our companies. How do we learn? We learn because you shadow
like the best teammate and then you see why they're doing something and then you learn from that and then you make a mistake. Who here has learned more from
a mistake than anything else? Right? You make a mistake and then you learn. uh
your manager gives you feedback and you learn not to do that again. You deal with an edge case and then you learn from that. That's how all of us humans learn at work.
And so then the question is how do you help build the agent Maya? Uh and now I want to walk you through our experiments
Chapter 6: Evolution of Agent Architecture at Atlan
and learnings as we've built this at Atlan um era one and this was roughly about 18 months ago now. Um we uh
started on the the track of bootstrapping agents. Um and the way we went about it was and we started this
with our customer experience team. Uh and we did this jobs to be done analysis map, right? And so we said, hey, if you
are someone on our customer experience team, what are all the things that you do on a day-to-day basis? And then we made some hypothesis. We we said, you
know, for example, one part of the job is documentation and meeting prep. Uh we said well AI could probably do that job
pretty well. Uh and so we build a scaling factor. So on the other hand relationship management is something that our customer experience team does
and we said hm that doesn't sound like something AI is going to be able to do anytime soon. And so we built a scaling factor [snorts] and then we basically
started bootstrapping these individual agents that were like built for that specific topic. Uh our team got
creative. So we had Hermione who is our health intelligence lead and then we had you know money penny who was our financial risk analyst and we just made
that particular agent really good at doing that one thing. Um and that worked
for some time um but then we realized there were some challenges with this approach. The first context engineering
uh we got to the point by middle of last year where building an agent was really easy took like 5 minutes. uh but giving it the business context that it took to
actually get it to be accurate took forever. Uh quality of the agent often dependent uh on the quality of context
engineering and that led to a lot of weird lost trust cases with our stakeholders. [snorts] Um then as we
started taking this into production we started seeing that these agents basically were kind of like living on their own island. Uh now imagine for
example if you're in a human team and your marketing changes positioning on your you know and then they come to the town hall and they tell you that they
changed positioning and so then you know the SDR on your team or your sales development rep they know that they should use that new positioning. This is
like the infrastructure that we've built for humans inside our organizations.

Agents didn't have them. So our marketing team had these agents and they started making changes to that and then our SDR agent on our website was still
pitching the old version. Uh we had no idea how any of these things were even connected. So we didn't even know how to
like run this as as a team of agents. Uh when an agent gets something wrong, this is hard. Uh it was really hard to like
Chapter 7: The Challenges of Isolated Agent Systems
trace back what happened. Was it the model? Was it the agent? Was it the context? Like where how do we even go back and fix this? Um and over time we started dealing with uh context sprawl.
Uh we had the the the hard part about this was agents all had their own memory systems to a certain extent. So they
were learning they were all learning separately and they were learning differently. Uh it became very very difficult very quickly to say okay what
does the single version of truth here look like? Um and then over time we actually went through in the last 12 months we've gone through cycles of at
the agentic layer about 12 months ago we were using one of these no code type builders uh called relevance we went
from there into Google ADK then we tried glean uh start of this year we moved to cloud code now we are kind of like 50/50
claude and codeex um and every single time as these changes happened uh our context got trapped in each of these
individuals systems. Um, so started this year as general purpose agents started to become a thing, we
Chapter 8: Transitioning to General Purpose Agents
said, what if there was a different approach with general purpose agents.
Um, again going back to the human world, well Maya, she's not an individual star.
She's part of a team, right? And you know, you talk about these dream teams like Maya and someone who runs customer support and someone who launches ads.
These people work really well together.
And often these dream teams are built on shared context, right? Uh they have a shared language. Uh they have a shared
picture of what's true today. They have shared playbooks. Uh they have shared norms, who's allowed to make what decision. Uh and then they learn
together. I think this is the most important part of it. They have compounding learning loops of what good looks like. uh and they have shared memory that you know oh we launched this
thing last quarter and it like was terrible and we're not going to make that mistake again right and so we said is there a way to bring that into the
way we think about AI in our companies and so the mental model we started working on was we said okay we have
these teams of humans and they're across the board and can these people essentially start building domain skills
so each of them is responsible for a certain set skills. All of this goes into this common one place which is this
one company brain of sorts, right? I like to think of this as the context layer. Uh and then this has a bunch of retrieval mechanisms which then talks to
the general purpose agent across the ecosystem.
So then we started an experiment. Uh this is some version of what our marketing team ended up building. So you'll see on the left those are all the
Chapter 9: Marketing Team Case Study: The Context Layer
systems that our marketing team uses. So data systems, our social and community platforms, our ad platforms, our
analytics platforms. Um and then you'll see this agent block. Uh we built this very specifically for um having
openness. [snorts] So we had claw code and co-work. We also had our own claw that we deployed which has you know essentially talks in our slack channels.
Um and then we used some external products like qualified and artisan.
[snorts]
Uh in the middle is kind of this context layer that our team started building. So think of it as our best SEO person was
building their SEO skill. Uh our best competitive intel person was building the best competitive intel skill and that kind of became this common repo
that we were building into and pulling out from. [snorts] This sort of became our living brain.

[CONTENT_PLACEHOLDER]