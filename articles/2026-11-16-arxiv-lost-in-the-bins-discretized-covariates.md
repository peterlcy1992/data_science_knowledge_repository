---
id: arxiv-lost-in-the-bins-discretized-covariates
title: "Lost in the Bins: Treatment Effects with Discretized Covariates"
source: "arXiv econ.EM (Goethe University Frankfurt)"
url: "https://arxiv.org/abs/2611.14789"
published: "2026-11"
added: "2026-11-16"
category: experimentation-causal
tags: [coarsening-bias, mean-independence, matching, sensitivity-analysis, partial-identification, sharp-bounds, placebo-tests, observational-causal]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "arXiv econ.EM listing (backlog stub)"
---

# Lost in the Bins: Treatment Effects with Discretized Covariates

**Source:** [arXiv econ.EM (Goethe University Frankfurt)](https://arxiv.org/abs/2611.14789) · Published 2026-11 · Added 2026-11-16
**Category:** experimentation-causal · **Tags:** `coarsening-bias`, `mean-independence`, `matching`, `sensitivity-analysis`, `partial-identification`, `sharp-bounds`, `placebo-tests`, `observational-causal`

## TL;DR

Mean independence (unconfoundedness in means) given a finely measured covariate need not hold once that covariate is coarsened into bins, so binning can change the **identifying content** of a comparison, not just its precision. The paper decomposes the resulting coarsening bias for the ATT and ATE, introduces a nonparametric relaxation called **c-mean dependence** with sharp bounds and bootstrap inference, and reanalyses Angrist (1998) on voluntary military service.

## 1. Business context

Covariates used for matching or adjustment are often available or used only in coarsened form: age in five-year bands, deciles of lagged employment growth or wages, test scores reported in groups, or cell means released because of data-access restrictions. Practitioners usually assume binning only costs efficiency. This paper shows it can bias the estimand itself — relevant to any analyst who buckets tenure, spend or engagement before a matched comparison or segment-level observational analysis.

## 2. Technical details

- **Setup.** X is the fine covariate, W = g(X) its coarsened version (e.g. bins with origin a and width b). Mean independence given X does not imply it given W.
- **Bias decomposition.** For the **ATT**, the bias is driven by *within-cell composition* in untreated potential outcomes: treated and comparison units in the same bin have different average μ₀(X). For the **ATE**, an additional *treatment-effect heterogeneity* term appears. Sufficient conditions for the terms to vanish are given; the paper also shows bias need not fall monotonically as bins get finer (it depends on whether a jump in the outcome function falls on a bin boundary).
- **c-mean dependence.** A relaxation of exact mean independence at the coarsened level: the unobserved average potential outcome for one treatment group may lie within the range spanned by neighbouring values of the coarsened covariate; c = 0 recovers mean independence and larger c is weaker. The paper derives sharp ATT/ATE bounds under it and proposes sample-analogue estimators with bootstrap inference for the bound functions.
- **Placebo check.** Pre-treatment outcomes (which treatment can't affect) are used to test mean independence given W against c-mean dependence.

## 3. Impact — potential & realized

**Realized (application).** Angrist (1998) data on men aged 17–22 applying to the military, where AFQT scores are reported only in groups and earnings are available as cell means. Placebo tests on pre-application earnings **reject** mean independence given the reported covariates in various comparisons for both white and nonwhite applicants, but reject 1-mean dependence in none. The finding that military service raised **1982** earnings — when veterans' earnings largely reflect military pay — is robust to all values of c for both groups. Later effects on civilian earnings (an apparent loss for white applicants in 1986 and gains for nonwhite applicants in 1986 and 1991) are **not robust**: at c = 1 the evidence on the sign is inconclusive for both groups.

**Potential.** A sensitivity parameter with a concrete meaning (how far across neighbouring bins comparisons may reach), usable whenever only binned covariates are available, plus a placebo-based way to choose it.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sharp, overlooked point with a usable sensitivity knob

"Bins can break unconfoundedness" is intuitive once said, but the formal decomposition (composition vs heterogeneity) and a bin-native sensitivity parameter are genuinely useful. The industry translation: if you match on bucketed tenure or spend, check balance on the *raw* covariate inside buckets and run a pre-period placebo. Limited to binary treatment and mean restrictions.

### Similar / related work

- [**Covariate Selection for Doubly Robust Double/debiased Machine Learning Estimators**](2026-10-01-arxiv-covariate-selection-doubly-robust-dml.md) (in this bank) — which covariates to adjust for; this paper asks what happens to them once binned.
- [**Looking Forward to Constructing Better Causal Comparisons**](2026-11-12-arxiv-looking-forward-better-causal-comparisons-prognostic-scores.md) (in this bank) — another way comparisons silently degrade, via prognostic-score construction.
- Manski / Manski–Pepper partial identification — the bounds tradition c-mean dependence sits in.

### Jargon buster

- **Mean independence** — the average untreated (or treated) outcome is the same for treated and untreated units with the same covariate value.
- **Coarsening** — replacing a fine covariate with bins or groups.
- **Sharp bounds** — the tightest interval for an effect consistent with the data and the stated assumption.
- **Placebo outcome** — an outcome measured before treatment; any "effect" on it signals a broken comparison.
