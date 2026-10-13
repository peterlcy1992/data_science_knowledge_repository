---
id: arxiv-experiment-design-under-interference-robust-selector
title: "Choosing Online Experiment Designs under Interference in Ads, Recommendations, and Member-Experience Systems"
source: "arXiv stat.ML (Shekhar & Howard)"
url: "https://arxiv.org/abs/2605.25290"
published: "2026-05"
added: "2026-10-13"
category: experimentation-causal
tags: [interference, experiment-design, switchback, cluster-randomization, minimax]
novelty: 3
sourced_via: "web search"
---

# Choosing Online Experiment Designs under Interference in Ads, Recommendations, and Member-Experience Systems

**Source:** [arXiv stat.ML (Shekhar & Howard)](https://arxiv.org/abs/2605.25290) · Published 2026-05 · Added 2026-10-13
**Category:** experimentation-causal · **Tags:** `interference`, `experiment-design`, `switchback`, `cluster-randomization`, `minimax`

## TL;DR

When you don't know what kind of interference (budgets, inventory, graph spillover, carryover) contaminates an experiment, this paper treats choosing the randomisation design as a robust decision and picks among six designs by worst-case planning risk.

## 1. Business context

In ads, recommendation and member-experience systems, units affect each other, so naive user-level A/B tests can be biased. The interference mechanism is often unknown when the experiment must be planned, yet the design (user, cluster, switchback, etc.) must be chosen up front.

## 2. Technical details

A selector compares six implementable designs on worst-case planning risk over an ambiguity set of exposure mechanisms. Risk combines exposure bias, assignment-unit variance, minimum detectable effect, contamination/carryover, operational cost and estimand mismatch. Theory (per the abstract): a design-bias bound via Wasserstein distance to the launch exposure distribution, minimax tight under Lipschitz exposure response; finite-catalog approximation; a robust-selector theorem with excess-risk control; exact recovery under separation; and certified shortlists when the risk surface is flat. Output is either a justified design or an uncertainty shortlist.

## 3. Impact — potential & realized

Realized (public-data illustrations): Criteo ads → user randomisation (robust risk 1.295); Open Bandit → switchbacks (2.105; propensities from 0.00006 to 0.594, 5.17% IPS effective-sample share); KuaiRand → cluster randomisation (2.240). The takeaway is that the recommended design differs by dataset. These are planning-risk numbers, not measured business effects. Potential: a principled, auditable way to justify experiment design.

*Sourced from web search / abstract-level content; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Design choice under interference is usually argued by habit; making it an explicit minimax decision with an honest 'uncertain, here is a shortlist' output is the useful part.

Design choice under interference is usually argued by habit; making it an explicit minimax decision with an honest 'uncertain, here is a shortlist' output is the useful part. Whether the ambiguity set is easy to specify in practice is the open question, and the evidence is from public datasets rather than live experiments. Note it was posted in May 2026, outside the usual one-week window, and was surfaced by search.

### Similar / related work

- [**Robust Sequential Experimental Design for A/B Testing**](https://arxiv.org/abs/2605.12899) — companion robust-design work
- [**Unlocking 66% Faster Experiments with Covariate Adjustment: Power Analysis for Clustered Data, Ratio Metrics, and OLS Regression**](2026-10-12-instacart-covariate-adjustment-power-analysis-clustered-data.md) (in this bank) — clustered-data inference

### Jargon buster

- **Interference** — One unit's treatment affecting another unit's outcome, violating the no-spillover assumption (SUTVA).
- **Switchback** — Randomising by time blocks within a market rather than by user.
- **Minimax** — Choosing the option whose worst-case loss is smallest.
