---
id: meta-ladder-of-evidence
title: "Ladder of Evidence in Understanding Effectiveness of New Products"
source: "Analytics at Meta"
url: "https://medium.com/@AnalyticsAtMeta/ladder-of-evidence-in-understanding-effectiveness-of-new-products-part-i-ad8dee70906c"
published: "2025-10"
added: "2026-09-01"
category: experimentation-causal
tags: [ab-testing, causal-inference, decision-framework, measurement]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Ladder of Evidence in Understanding Effectiveness of New Products

**Source:** [Analytics at Meta](https://medium.com/@AnalyticsAtMeta/ladder-of-evidence-in-understanding-effectiveness-of-new-products-part-i-ad8dee70906c) · Published 2025-10 · Added 2026-09-01
**Category:** Experimentation & Causal Inference · **Tags:** `ab-testing`, `causal-inference`, `decision-framework`

## TL;DR

Meta's analytics team lays out a "ladder of evidence": a decision framework
for choosing how much rigor a product-effectiveness question actually needs,
running from randomized A/B tests at the top down through quasi-experiments,
counterfactual estimation, and plain descriptive statistics at the bottom —
and a set of rules for when it's legitimate to step down the ladder.

## 1. Business context

Not every product decision at Meta's scale can or should be validated with
a full randomized controlled trial: some features can't be cleanly
randomized (e.g. network effects, infrastructure changes, features with
long delayed effects), and running a rigorous experiment for every question
is not always worth the engineering and analyst time. Teams need a shared
way to decide which methodology a given decision actually warrants, and to
be explicit about how much confidence that choice buys them — rather than
defaulting either to expensive experiments everywhere or to hand-wavy
observational claims presented with unwarranted confidence.

## 2. Technical details

The ladder orders methods by strength of causal evidence, trading rigor for
practicality as you descend:

1. **A/B tests (randomized controlled trials)** — the top rung and the
   gold standard: random assignment removes confounding by construction,
   giving the clearest evidence of a causal effect.
2. **Quasi-experiments** — difference-in-differences, matching, and
   controlled regression designs used when true randomization isn't
   available; a reasonable but weaker level of evidence than an RCT.
3. **Counterfactual / full observational causal-inference estimation** —
   estimating what would have happened absent the change from existing data
   alone, without any experimental variation; the weakest rung that still
   claims to estimate a causal effect.
4. **Descriptive statistics** — correlational analysis of existing data;
   at the bottom of the ladder, providing no direct evidence of a causal
   relationship on its own.

The framework's core discipline is procedural rather than statistical: as
the reach and stakes of a decision grow, the expected rigor of the
evidence backing it should grow correspondingly, and analysts should be
explicit about which rung they're standing on and what that implies about
how much to trust the resulting number — rather than presenting a
correlational read as if it settled the question.

## 3. Impact — potential & realized

- **Realized:** an internal decision framework reportedly used at Meta to
  standardize how data scientists choose a measurement method and how much
  confidence to attach to the resulting estimate; no specific product
  decisions, feature rollouts, or quantified error-rate reductions are
  disclosed in the source.
- **Potential:** a template other applied-analytics orgs can adopt to make
  "how sure are we, really" an explicit, shared vocabulary across data
  science and product teams — rather than an implicit judgment call each
  analyst makes independently and inconsistently.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — a clean restatement of a well-known evidence hierarchy

The levels-of-evidence idea (RCT > quasi-experiment > observational
inference > correlation) is standard applied-causal-inference practice, not
new to this piece. The value here is organizational, not methodological: a
crisp internal name and shared framework for a hierarchy analysts already
know, used to standardize how teams talk about confidence levels rather
than to introduce a new estimator or technique. Worth banking as a
reference for how a large analytics org operationalizes evidence
standards, but it isn't advancing the state of the art.

### Similar / related work

- **DeepMind's double-blind AI evaluations** ([in this
  bank](2026-09-01-deepmind-double-blind-ai-evaluations.md)) — a different
  axis of the same underlying concern (how much can you trust a measurement
  and its result) applied to model benchmarking rather than product
  experimentation.
- General causal-inference hierarchy literature (RCT vs. quasi-experimental
  vs. observational methods) — this piece is a production-team
  restatement of that established body of work rather than a citable single
  source.

### Jargon buster

- **Quasi-experiment** — a study design that approximates random assignment
  (e.g. by comparing similar groups before/after a change) when a true
  randomized experiment isn't feasible.
- **Counterfactual estimation** — estimating what would have happened to a
  metric if a change had *not* been made, using only observational data and
  no experimental variation.
- **Difference-in-differences** — a quasi-experimental method that compares
  the change over time in a treated group against the change over time in
  an untreated comparison group to isolate an effect.
