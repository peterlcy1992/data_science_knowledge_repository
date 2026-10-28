---
id: arxiv-experiment-reservoir-surrogate-long-term-effects
title: "Many Hands Make Light Work: Long-Term Effect Inference for the Experiment Reservoir"
source: "arXiv econ.EM (Hartog, Lei, Rahurkar, Sahni & Tang; DoorDash data)"
url: "https://arxiv.org/abs/2610.36352"
published: "2026-10"
added: "2026-10-28"
category: experimentation-causal
tags: [surrogate-index, long-term-effects, experimentation-platform, historical-experiments, local-linear-regression, matching]
novelty: 4
sourced_via: "full-text fetch"
---

# Many Hands Make Light Work: Long-Term Effect Inference for the Experiment Reservoir

**Source:** [arXiv econ.EM (Hartog, Lei, Rahurkar, Sahni & Tang; DoorDash data)](https://arxiv.org/abs/2610.36352) · Published 2026-10 · Added 2026-10-28
**Category:** experimentation-causal · **Tags:** `surrogate-index`, `long-term-effects`, `experimentation-platform`, `historical-experiments`, `local-linear-regression`, `matching`

## TL;DR

The Experiment Reservoir Surrogate (ERS) predicts a new experiment's long-term average treatment effect by regressing long-term ATEs on short-term ATEs across a reservoir of historical long-term experiments, matched to experiments with similar short-term trends. It avoids the surrogacy assumption of the surrogate index, relaxes comparability, and needs only aggregate per-period data. On 196 DoorDash experiments it is reported to improve RMSE over an arm-wise surrogate baseline.

## 1. Business context

Decision-makers care about long-term effects (months) but want to decide within weeks, so long-term effects must be estimated from short-term outcomes. The modern standard, the surrogate index of Athey et al. (2025), depends on surrogacy (long-term outcome independent of treatment given the short-term index) and comparability (the short-to-long relationship in training data matches the target experiment). The authors argue both can fail: continued exposure to treatment can affect units after the short-term window, and outcome relationships vary across contexts and time. Large experimentation platforms already hold a database of completed long-term experiments that the standard method does not exploit.

## 2. Technical details

ERS treats historical experiments in the reservoir as the units of a regression. It differs from the surrogate index in three ways: (a) it works on aggregated per-period data rather than individual-level data (so storage and compute are much lighter; the authors contrast seconds-to-minutes with hours-to-days for user-level analyses); (b) it fits a horizontal regression directly on aggregated short-term and long-term ATEs rather than on outcome values; (c) it matches the target experiment to similar reservoir experiments, using Euclidean distance on the normalised short-term ATE vector so matching is on trend rather than magnitude, followed by local-linear regression. Comparators are Aggregate Surrogate (AggS) and Armwise Surrogate (ArmS), aggregate-data analogues of the surrogate index, plus matched variants, and ERS+ which adds short-term control means as covariates. Theory: via an MSE decomposition, ERS without matching has a smaller bound on reducible error than AggS and ArmS, AggS is generally biased unless an experiment-level surrogacy condition holds, and under a smoothness/local-structure assumption ERS has zero approximation error; ERS matches on t0 covariates while ERS+ matches on 2*t0, which gives ERS the faster rate when the assumption is plausible.

## 3. Impact — potential & realized

Realized: 196 DoorDash experiments (metrics as time series of daily ATEs; metrics within one parent experiment are dependent), short-term cutoff t0 = 20 days (days 6-19 used, d = 14 observations), long-term target T = 55 days. Experiments are ordered chronologically; reservoirs of n = 50 to 140 (steps of 10) predict the next 50 experiments, and RMSE is compared. The number of matches k is chosen by leave-one-out cross-validation capped at a third of the reservoir, and hovers around 25%. The paper reports (Figure 5) a substantial percent RMSE improvement of ERS over ArmS, with AggS also worse than the ERS variants; specific percentages are shown only in the figure and are not restated here. Potential: platforms can turn their accumulated experiment history into a long-term-effect predictor without user-level data. Stated future work: prediction intervals, choosing the short-term cutoff, and dimension reduction for the local regression.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Treating the experiment, not the user, as the unit of analysis is a sensible bet exactly where platforms have hundreds of finished long-running experiments; it trades individual-level surrogacy for an experiment-level exchangeability-ish assumption that is only partly tested (chronological hold-out on one company's data).

Treating the experiment, not the user, as the unit of analysis is a sensible bet exactly where platforms have hundreds of finished long-running experiments; it trades individual-level surrogacy for an experiment-level exchangeability-ish assumption that is only partly tested (chronological hold-out on one company's data). No prediction intervals yet, which is what decision-makers would need. The empirical case is a single company's reservoir.

### Similar / related work

- [**Lifetime-valid decisions by continually evolving AI analysts**](2026-10-23-arxiv-lifetime-valid-continual-validation-ai-analysts.md) (in this bank) — decisions drawn from accumulated evidence across experiments
- **Athey et al., The Surrogate Index (referenced by the paper)** — the surrogate-index framework that ERS modifies

### Jargon buster

- **Surrogate index** — A prediction of the long-term outcome built from short-term measurements and used to estimate long-term treatment effects.
- **Surrogacy** — The assumption that treatment affects the long-term outcome only through the surrogate.
- **Comparability** — The assumption that the short-to-long-term relationship in the training data matches the target experiment.
- **Local-linear regression** — A regression fitted only to nearby (matched) points, so it adapts to non-linear relationships.
