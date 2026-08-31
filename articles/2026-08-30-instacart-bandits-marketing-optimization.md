---
id: instacart-bandits-marketing-optimization
title: "Bandits for Marketing Optimization at Instacart"
source: "Instacart Tech (tech-at-instacart)"
url: "https://tech.instacart.com/bandits-for-marketing-optimization-f5a63b9bfaa7"
published: "2024-09"
added: "2026-08-30"
category: experimentation-causal
tags: [multi-armed-bandit, adaptive-experimentation, explore-exploit, marketing, causal, performance-curves]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Bandits for Marketing Optimization at Instacart

**Source:** [Instacart Tech](https://tech.instacart.com/bandits-for-marketing-optimization-f5a63b9bfaa7) · Published 2024-09 · Added 2026-08-30
**Category:** Experimentation & Causal Inference · **Tags:** `multi-armed-bandit`, `adaptive-experimentation`, `explore-exploit`
_Surfaced via the Snacks Weekly on Data Science podcast._

## TL;DR

Instacart runs marketing as an **adaptive experiment**: it injects small random
perturbations into marketing actions to create the **exogenous variation** needed
to estimate performance curves, then shifts allocation from **exploration** to
**exploitation** as those curves sharpen — instead of either a static A/B test or
naive full exploitation.

## 1. Business context

Marketing spend decisions (how much, to whom, which action) are a classic
explore/exploit problem. A fully randomized A/B test is statistically clean but
slow and costly — it keeps pouring traffic into arms already known to be worse. A
"just do what looks best" policy exploits current beliefs but never learns the
true response curve and gets stuck on local optima. Instacart wanted to
**maximize marketing efficiency** while still learning, and to do it continuously
rather than in discrete test cycles.

## 2. Technical details

- **Perturbations for identification.** The system introduces **random
  perturbations** into marketing actions. That randomization is the **exogenous
  variation** required to identify **performance curves** (how outcomes respond to
  the action level) — a causal-inference move, not just optimization.
- **Adaptive allocation.** Rather than fixed per-arm sample sizes, allocation is
  **biased toward better-performing arms** but keeps sampling others — a
  multi-armed-bandit balance between exploration and exploitation.
- **Exploration → exploitation over time.** Early on the policy explores to learn
  the curves accurately; as confidence grows it tilts toward exploitation to
  maximize returns, all within one continuously running system.
- **Contrast with the alternatives.** Fully randomized experiments waste budget on
  known-worse arms; "no experiment" maximally exploits current beliefs but never
  explores. Adaptive experiments occupy the productive middle.

## 3. Impact — potential & realized

- **Realized:** a live adaptive-experimentation system that improves marketing
  efficiency by learning response curves while spending, rather than pausing to
  test.
- **Potential:** the perturbation-for-identification pattern generalizes to any
  continuous decision variable (pricing, budgets, notification frequency) where
  you need both a causal estimate of the response and ongoing optimization.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a clean, well-framed application of adaptive experimentation

Multi-armed bandits and adaptive experiments are textbook; what lifts this above a
recap is the explicit **causal framing** — using deliberate perturbations to
generate exogenous variation and *estimate performance curves*, not just pick the
best arm. That reframing (optimization as identification) is the useful,
transferable idea. It's a 3 because the core techniques are established and the
post is an application rather than a new method.

### Similar / related work

- **"Optimizing Adaptive Experiments: Regret Minimization and Best-Arm
  Identification"** (arXiv 2402.10592) — the theory behind the trade-off Instacart
  operationalizes.
- **Netflix contextual bandits for recommendations** (a Snacks Weekly episode) —
  bandits applied to content selection with reward engineering.
- **Instacart quasi-experimentation / regression-discontinuity work** — the
  causal-inference sibling in the same team's output.

### Jargon buster

- **Multi-armed bandit (MAB)** — a sequential decision problem: repeatedly choose an
  "arm" (option), observe a reward, and balance trying new arms (explore) against
  favoring the best-known one (exploit).
- **Exploration vs. exploitation** — the core tension: learning which option is best
  vs. cashing in on what you already believe is best.
- **Exogenous variation** — variation in the action that is independent of confounders
  (here, injected by randomization), which is what lets you estimate a causal
  response curve.
- **Performance curve** — how an outcome (e.g. conversions) changes as you vary an
  action level (e.g. spend); the object the experiment is trying to learn.
- **Adaptive experiment** — an experiment whose allocation updates as data arrives,
  shifting toward better arms while still sampling others.
