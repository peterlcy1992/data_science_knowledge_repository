---
id: instacart-agentic-machine-learning-modeling
title: "Agentic Machine Learning Modeling at Instacart"
source: "Instacart Tech Blog (tech-at-instacart)"
url: "https://tech.instacart.com/agentic-machine-learning-modeling-at-instacart-fb3ecd295ee7"
published: "2026-09"
added: "2026-09-15"
category: llm-genai
tags: [agentic-ai, ml-engineering, coding-agents, applied-science, safety, sandboxing]
novelty: 3
sourced_via: "web search"
---

# Agentic Machine Learning Modeling at Instacart

**Source:** [Instacart Tech Blog](https://tech.instacart.com/agentic-machine-learning-modeling-at-instacart-fb3ecd295ee7) · Published 2026-09 · Added 2026-09-15
**Category:** LLMs & Generative AI · **Tags:** `agentic-ai`, `ml-engineering`, `coding-agents`, `applied-science`

## TL;DR

Instacart's ML engineers ran a series of exercises turning coding agents loose on the actual modeling work behind production systems — not just scaffolding or glue code, but exploring features, architectures, and hyperparameters for mature, already-optimized models. The headline finding: agents proved themselves competent modeling collaborators, with the most promising runs delivering 3–5% offline improvements in held-out error on models that had already been heavily tuned by humans — alongside real safety and process lessons about giving agents that much latitude.

## 1. Business context

Applied ML teams have mostly absorbed AI-assisted coding into the software-engineering parts of their job — writing pipelines, tests, and infrastructure code. What's less settled is whether agents can meaningfully help with the actual modeling work: picking features, trying architectures, tuning a model that a team has already spent months optimizing by hand. That's a harder bar, because mature production models are exactly the case where the "easy wins" have already been found, and further gains typically require either genuinely novel ideas or a lot of tedious, wide-net experimentation that a human modeler doesn't have time to run exhaustively. Instacart's ML engineering team set out to see whether agentic tools could productively take on that exploration work across a variety of model types and business contexts, rather than treating agents as limited to writing code around models that humans design.

## 2. Technical details

The post frames this as a shift in what an ML engineer's time goes to: agents proving themselves as modeling collaborators changes the modeling process itself, not just the surrounding tooling. Concretely, the team ran exercises letting agents explore feature sets, modeling approaches, and tuning choices against production baselines — including some of Instacart's most mature, already-optimized models, which is a deliberately hard test since there's less low-hanging fruit left to find. The write-up treats this as an emerging paradigm shift in how the team thinks about the modeling loop, not a one-off experiment: agents functioning as genuine collaborators in the exploration phase that used to be almost entirely a human researcher's job.

The team is explicit that agent-produced modeling gains can't just be trusted at face value: any offline improvement has to clear a battery of randomization checks before it's credible enough to take to a full online A/B test — a discipline that matters more, not less, when the "researcher" proposing the change is a model that can generate a plausible-looking result without the same instinct for spurious correlations a human modeler builds over time.

## 3. Impact — potential & realized

**Realized:** Some of the agent-assisted runs delivered 3–5% offline improvements in held-out mean absolute error (MAE) against the strongest baseline — reported as being among the most promising results, on models that were already mature and optimized. More broadly, across a range of model types and business contexts, agents functioned as competent modeling collaborators rather than just code generators.

**Potential:** If agentic tools can reliably extend the exploration budget a modeling team has — trying more features, architectures, and tuning combinations than a human researcher has time for — that changes the shape of applied-ML work generally, not just at Instacart. But the post is equally clear about the other side of that potential: broad agent permissions in a modeling environment are a genuine safety surface, not a hypothetical one, and the team explicitly recommends sandboxing an agent's environment even though their own exercises only ran into minor problems. There's also a compliance dimension called out directly — an agent exploring model changes may not be aware of legal or contractual limitations on what a model is allowed to use or optimize for, which is a constraint a human modeler on the team would typically already know to respect.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A believable, honestly-reported early result, not a breakthrough

The core idea — pointing coding agents at modeling exploration instead of just surrounding code — is an obvious next step now that agentic coding tools are mainstream, and Instacart isn't claiming otherwise. What makes this worth reading is the honesty about the bar being "some of the most promising runs," not "every run," on models chosen specifically because they were already hard to improve, plus a genuine safety callout (sandboxing, compliance blind spots) instead of a pure win narrative. That's a useful production-first data point for any team wondering whether this is worth trying on their own mature models.

### Similar / related work

- [**Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender Systems**](2026-09-13-meta-auto-recsys-autonomous-research-agents.md) (in this bank) — a more architecturally elaborate take on the same underlying idea (agents doing ML research work), built specifically for recommender-system experimentation at Meta, with explicit infrastructure for distributed async execution and cross-session memory.
- [**NetEase — AutoLR: Automating the Path from Research to Launch Review in Industrial Recommender Systems**](https://arxiv.org/abs/2609.04871) — another industrial case of agents running the modeling-to-launch pipeline, with a notable self-audited failure mode (the "KEEP ratchet") that's a useful cautionary companion to Instacart's own safety concerns here.
- **AI-assisted feature/hyperparameter search literature (AutoML, Bayesian optimization)** — the classical, non-agentic version of "search the modeling space faster than a human can," which this work is effectively extending with an LLM-driven, more open-ended search process.

### Jargon buster

- **Held-out MAE (mean absolute error)** — A model's average prediction error measured on data it wasn't trained on, used here as the offline metric agent-proposed models were compared against.
- **Randomization checks** — Statistical sanity checks run before trusting an observed offline improvement, designed to catch results that look real but are actually artifacts of how data was split or sampled.
- **Sandboxing** — Running an agent (or any program) in an isolated environment with restricted permissions, so that mistakes or unintended actions can't affect production systems or data.
- **A/B test** — A controlled online experiment that randomly splits real users between a baseline and a candidate change to measure its actual effect on business metrics, the standard final validation step before a model change ships broadly.
