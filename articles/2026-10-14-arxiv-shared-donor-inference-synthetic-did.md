---
id: arxiv-shared-donor-inference-synthetic-did
title: "Shared-Donor Inference for Fixed-Set Heterogeneity in Synthetic Difference-in-Differences"
source: "arXiv econ.EM (Hoshino & Nakakita)"
url: "https://arxiv.org/abs/2607.08324"
published: "2026-07"
added: "2026-10-14"
category: experimentation-causal
tags: [synthetic-did, synthetic-control, heterogeneous-effects, simultaneous-inference, bootstrap]
novelty: 3
sourced_via: "web search"
---

# Shared-Donor Inference for Fixed-Set Heterogeneity in Synthetic Difference-in-Differences

**Source:** [arXiv econ.EM (Hoshino & Nakakita)](https://arxiv.org/abs/2607.08324) · Published 2026-07 · Added 2026-10-14
**Category:** experimentation-causal · **Tags:** `synthetic-did`, `synthetic-control`, `heterogeneous-effects`, `simultaneous-inference`, `bootstrap`

## TL;DR

When several synthetic control / synthetic DiD effects are estimated against one shared donor pool, their first-stage errors are correlated through the shared donors. This paper builds joint inference for the whole vector of effects (simultaneous intervals, projection bands, heterogeneity and homogeneity tests) instead of treating each effect's interval in isolation.

## 1. Business context

Policy and geo-experiment evaluations often estimate many unit-level (or group-level) effects with synthetic control or synthetic difference-in-differences, reusing the same untreated donor units each time. Reporting each effect with its own interval ignores that the donor weights are estimated from shared data, so questions such as 'is the effect heterogeneous across jurisdictions?' or 'what is the average across a fixed set?' can get the wrong uncertainty.

## 2. Technical details

The paper characterises three regimes for fixed-set linear summaries of the effects: nonconcentration, root-rate donor exposure and donor negligibility, which determine whether shared-donor covariance matters. For quadratic summaries (e.g. total vs. explained heterogeneity), removing shared-donor uncertainty requires the shared-donor covariance to vanish in every direction that enters the summary. Second-stage inference takes a joint first-order experiment for the effect vector as input and builds simultaneous intervals, a fixed-grid projection band, a centred confidence region, image sets for total and explained heterogeneity and their ratio, and a homogeneity test around the sampling centre. For hard-simplex SDID, an operator-normalised numerical directional bootstrap re-estimates the donor and time weights in every draw, with an exact critical-cone derivative used to check the numerical approximation. Mismatch in the counterfactual that does not vanish is handled separately with deterministic sensitivity regions. (Details here come from the arXiv abstract page summary; full-text proofs and simulation designs were not reviewed.)

## 3. Impact — potential & realized

Realized (as reported): in a Medicaid-expansion application, ignoring off-diagonal covariance understates uncertainty for the equal-jurisdiction mean effect but overstates it for a centred projection on the baseline uninsured rate - i.e. the error goes in both directions depending on the summary. No other numbers were available to us. Potential: a more honest way to report heterogeneity across markets in geo-holdout or staggered-rollout analyses that reuse a common donor pool.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a careful inference refinement for a niche but real setup (many effects, one donor pool); useful for analysts doing multi-market evaluations, incremental rather than a new estimator.

This is methodology polish rather than a new idea: the contribution is recognising and handling cross-effect correlation induced by the shared donors. It matters most when you report heterogeneity across many treated units from one synthetic-control fit. Practitioners running geo-experiments with a common control pool should be aware their per-market intervals may be miscalibrated for aggregate questions. Caveat: I only saw the abstract-level summary, so I can't judge the simulation evidence or how heavy the bootstrap is.

### Similar / related work

- [**Synthetic Control with Weight Uncertainty**](https://arxiv.org/abs/2511.02632) — inference when donor weights are themselves uncertain
- [**Risk-Set Transported Synthetic Control with DiD Adjustment**](https://arxiv.org/abs/2609.20264) — synthetic control for staggered adoption

### Jargon buster

- **Donor pool** — The untreated units whose weighted combination forms the synthetic counterfactual for a treated unit.
- **Synthetic DiD** — Combines synthetic-control unit weights with time weights and a difference-in-differences adjustment.
- **Simultaneous interval** — A confidence band covering all effects jointly at the stated level, rather than each one separately.
