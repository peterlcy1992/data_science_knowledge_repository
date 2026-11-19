---
id: arxiv-sequential-conditional-paired-sample-testing-monitoring
title: "Sequential Conditional Paired-Sample Testing with Applications to Online Monitoring"
source: "USTC (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.22886"
published: "2026-11"
added: "2026-11-19"
category: experimentation-causal
tags: [anytime-valid, sequential-testing, test-martingales, conditional-two-sample, kernel-discrepancy, model-monitoring, calibration, shadow-deployment]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "catalog backlog (arXiv stat.ME scan)"
---

# Sequential Conditional Paired-Sample Testing with Applications to Online Monitoring

**Source:** [USTC (arXiv stat.ME)](https://arxiv.org/abs/2611.22886) · Published 2026-11 · Added 2026-11-19
**Category:** Experimentation & Causal Inference · **Tags:** `anytime-valid`, `sequential-testing`, `test-martingales`, `conditional-two-sample`, `kernel-discrepancy`, `model-monitoring`, `calibration`, `shadow-deployment`

## TL;DR

SCPT is an anytime-valid, nonparametric test of whether two paired responses have the same conditional distribution given shared covariates, built from sequential conditional kernel discrepancies and test martingales. It covers model-calibration monitoring, generative-model goodness of fit, and shadow-deployment comparisons, with time-uniform type-I error control beyond i.i.d. data.

## 1. Business context

Monitoring problems arrive as streams with no fixed sample size: is a model still calibrated, does a generative model's output match reality, is a shadow-deployed candidate behaving like production on the same inputs? Classical conditional two-sample tests assume fixed samples and i.i.d. data. Re-running them repeatedly inflates false alarms, and Bonferroni corrections over inspection times are conservative. The authors (Zheng & Zhang, USTC) want a procedure you can check continuously and stop as soon as evidence of a conditional discrepancy appears.

## 2. Technical details

- **Hypothesis.** A stream of triples (X_t, Y_t, Z_t), where X and Y are paired responses sharing covariate Z. H₀: X_t | Z_t, F_{t−1} has the same distribution as Y_t | Z_t, F_{t−1} on a region of interest, for every t. Conditioning on the past allows non-stationary, dependent streams.
- **Special cases.** Conditional goodness of fit (draw X_t from the target model F(·|Z_t)); **calibration monitoring** (draw labels from the predicted class probabilities); monitoring conditional generative models from samples; and **online paired comparisons** such as shadow deployment, where candidate and production systems run on the same inputs.
- **Construction.** Sequentially built conditional kernel discrepancy statistics feed a **test martingale**. Reject when it exceeds 1/α (Ville's inequality gives time-uniform validity). Nearest-neighbour coefficients a ∈ {2, 4, 6} are combined in an equally weighted mixture. Extensions use multiple generated samples per covariate (SCPT10 uses ten) and one-versus-many testing.
- **Theory.** Time-uniform type-I error control, plus asymptotic power guarantees under regularity conditions.

## 3. Impact — potential & realized

**Measured (real data, α = 0.05):**
- **MNIST calibration** (a CNN with ECE 0.0027; 500 repetitions of 5,000-image streams). With clean labels all procedures rarely reject. With 1% label swaps between 1↔7, 3↔5 and 4↔9, SCPT10 reaches a 69.4% cumulative rejection rate by about 4,000 observations, higher than Bonferroni-adjusted SKCE baselines over the horizon.
- **Co-located sensors** (low-cost AHT10 vs professional CS215-L, 10,000 pairs, conditional on radiation). The original study reports R² = 0.9992 for temperature, yet SCPT rejects at the 14th monitoring observation for temperature and the 91st for humidity.
- **NYC taxi destination models.** A mixture density network conditioned only on pick-up location is rejected after 75 monitoring observations on day one. It underestimates early-morning trip distances (observed 3.021 km vs predicted 2.467 km) and overestimates daytime ones, even though full-day averages are close.

**Potential:** continuous drift and calibration checks, plus shadow-test comparisons where a conditional discrepancy matters more than average metrics. Simulations also cover non-stationary and dependent streams.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Anytime-valid conditional monitoring, not just average-metric alarms

Two-sample monitoring that ignores covariates misses discrepancies that cancel out in aggregate. The taxi example (close full-day averages, wrong by time of day) is the clearest illustration. For ML-ops and experimentation teams, SCPT is a principled shadow-deployment and calibration check that can be peeked at continuously.

Practical concerns: kernel bandwidth via median heuristic, the cost of nearest-neighbour conditioning in high-dimensional Z, and how quickly it fires on harmless discrepancies at production scale (the sensors example shows it will find *some* difference). Pair it with an effect-size readout.

### Similar / related work

- [**Anytime-Valid Inference in Linear Models with Clustered Outcomes: Exact Multivariate Tests and Cluster-Robust Confidence Sequences**](2026-10-20-arxiv-anytime-valid-clustered-linear-models.md) (in this bank) — anytime-valid inference for experiment metrics.
- [**MOSS: A Production Framework for Monitoring and Diagnosing Semantic Failures in Search and Recommendation Systems**](2026-10-21-arxiv-moss-semantic-failure-monitoring-search-recsys.md) (in this bank) — production monitoring of model behaviour, an application area for SCPT.
- **Testing by betting / test martingales (Shafer, 2021; Ramdas et al.)** — the e-value machinery behind time-uniform validity.
- **Widmann et al. (2019), calibration tests in multi-class classification** — the SKCE calibration statistic used as the fixed-sample baseline.

### Jargon buster

- **Anytime-valid** — a test whose false-alarm guarantee holds no matter when or how often you look or stop.
- **Test martingale** — a running wealth-like statistic that, under the null, does not grow on average; crossing 1/α is evidence against the null.
- **Conditional two-sample test** — checks whether two outcome distributions match at each covariate value, not just on average.
- **Shadow deployment** — running a candidate model on live inputs without showing its output to users, to compare it with production.
