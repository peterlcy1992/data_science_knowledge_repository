---
id: faire-autoscience-agent-driven-ml-exploration
title: "Autoscience: How We Built Agent-Driven ML Exploration at Faire"
source: "The Craft (Faire Engineering Blog)"
url: "https://craft.faire.com/autoscience-how-we-built-agent-driven-ml-exploration-at-faire-f3183e7deb29"
published: "2026-07"
added: "2026-09-17"
category: ml-infra-serving
tags: [agentic-ml, experimentation, model-iteration, guardrails, autoresearch]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Autoscience: How We Built Agent-Driven ML Exploration at Faire

**Source:** [The Craft (Faire Engineering Blog)](https://craft.faire.com/autoscience-how-we-built-agent-driven-ml-exploration-at-faire-f3183e7deb29) · Published 2026-07 · Added 2026-09-17
**Category:** ML Infrastructure & Serving · **Tags:** `agentic-ml`, `experimentation`, `model-iteration`, `guardrails`, `autoresearch`

## TL;DR

Faire built Autoscience, a production system that lets an agent autonomously propose, train, score, and keep-or-revert changes to ML models — inspired by Andrej Karpathy's "autoresearch" loop pattern — but had to add guardrails, self-serve tooling, and institutional-knowledge feedback to make the naive loop actually work at production scale across teams.

## 1. Business context

For any ML team, there are always far more promising things worth trying (feature ideas, hyperparameter changes, architecture tweaks) than the team has capacity to explore. Each iteration demands human attention — deciding what to try next, reviewing results, deciding what to try after that — so in practice teams run only a small fraction of the experiments that would be worth running. Faire's bet was that an agent could run far more of these iterations in the same span of time than a human team could, if it could be trusted to do so reliably.

## 2. Technical details

The starting point is the "autoresearch" pattern: an agent proposes a change, trains the model, scores the result, and decides whether to keep or revert the change — then repeats, far more times than a human team could manage in the same period. Applying that pattern directly to Faire's real ML systems surfaced practical problems the naive loop doesn't handle:

- **Long iteration cycles break raw agent sessions.** ML iteration is inherently slow — individual training jobs can take hours, and meaningful movement in a metric can require many attempts — which doesn't fit cleanly into a single agent session the way faster iteration loops (like code-and-test) do.
- **Reward hacking risk.** Left unconstrained, an agent optimizing for a metric can find shortcuts that make the metric look better without genuinely improving the model (e.g. exploiting evaluation quirks rather than the underlying signal). Faire built explicit guardrails to prevent the agent from finding and exploiting these shortcuts.
- **Scaling beyond one team.** Getting the pattern to work reliably for one use case wasn't the end state — Faire built self-serve tooling so multiple teams could apply Autoscience to their own models, and mechanisms to accumulate institutional knowledge across runs so later experiments benefit from what earlier ones learned, rather than every team's agent starting from zero.

## 3. Impact — potential & realized

**Realized:** Autoscience moved from a Karpathy-style research pattern to a production system used across multiple teams at Faire, with guardrails specifically engineered to prevent metric gaming and self-serve tooling that let teams beyond the original build team adopt it.

**Potential:** The core lesson generalizes well beyond Faire's specific models — any ML team sitting on a large backlog of untried experiment ideas, where the bottleneck is human attention/review capacity rather than compute, is a candidate for this pattern, provided the guardrail and institutional-memory problems are solved rather than assumed away.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A candid, production-tested account of a popular idea's rough edges

The "propose, train, score, keep-or-revert" agentic research loop itself (Karpathy's autoresearch framing) isn't new, and several teams are exploring versions of it. What's valuable here is Faire's honesty about where the naive version breaks in production — slow iteration cycles, reward hacking, and the need for cross-team institutional memory — which are the parts most autoresearch demos gloss over. That makes this a useful engineering account rather than a novel technique.

### Similar / related work

- [**Agentic Machine Learning Modeling at Instacart**](2026-09-15-instacart-agentic-machine-learning-modeling.md) (in this bank) — a close industry parallel: agents autonomously iterating on ML modeling work, with its own guardrail and evaluation design choices worth comparing against Faire's.
- [**Automating Risk Model Retrain Loop with Agentic Skills**](2026-09-17-coinbase-agentic-risk-model-retrain-loop.md) (in this bank) — a narrower, single-pipeline version of agent-driven ML iteration (one retraining loop vs. open-ended exploration), with a similar emphasis on log/result feedback loops for the agent.
- [**Auto-RecSys: Harnessing Autonomous Research Agents for Industry-Scale Recommender Systems**](2026-09-13-meta-auto-recsys-autonomous-research-agents.md) (in this bank) — the same autoresearch pattern applied specifically to recommender-system research at Meta's scale.

### Jargon buster

- **Autoresearch loop** — An agentic pattern (associated with Andrej Karpathy) where an agent repeatedly proposes a change, trains, scores it, and decides to keep or revert — automating the iterate-and-evaluate cycle of ML research.
- **Reward hacking** — When an agent (or model) finds a way to improve its measured score without genuinely improving the underlying thing the score is meant to measure, by exploiting a quirk in how success is evaluated.
- **Guardrails** — Constraints deliberately built into an agentic system to prevent it from taking undesired shortcuts or actions, even if those actions would technically improve its target metric.
