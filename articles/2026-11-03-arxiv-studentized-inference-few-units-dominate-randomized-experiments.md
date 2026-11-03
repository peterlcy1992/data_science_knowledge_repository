---
id: arxiv-studentized-inference-few-units-dominate-randomized-experiments
title: "Studentized inference in randomized experiments when a few units dominate the outcome variation"
source: "arXiv math.ST (Chen, Kiesel, Woody, Mississippi State)"
url: "https://arxiv.org/abs/2611.03561"
published: "2026-11"
added: "2026-11-03"
category: statistical-modeling
tags: [randomization-inference, heavy-tails, wald-interval, coverage, design-based, lin-estimator]
novelty: 4
sourced_via: "full-text fetch"
---

# Studentized inference in randomized experiments when a few units dominate the outcome variation

**Source:** [arXiv math.ST (Chen, Kiesel, Woody, Mississippi State)](https://arxiv.org/abs/2611.03561) · Published 2026-11 · Added 2026-11-03
**Category:** statistical-modeling · **Tags:** `randomization-inference`, `heavy-tails`, `wald-interval`, `coverage`, `design-based`, `lin-estimator`

## TL;DR

With heavy-tailed outcomes such as revenue or spending, a few units can carry a share of the residual variation that does not vanish as N grows. The paper shows the studentized difference in means (and Lin's regression-adjusted estimator) then has a nonnormal limit, and the conventional Wald interval has an explicit asymptotic coverage floor under balanced allocation of about 0.42 at nominal 0.95 (about 0.84 when each unit's two potential residuals are equal). Without balanced allocation, coverage can fall to the smaller of the treated and control proportions.

## 1. Business context

Randomized experiments are routinely analysed with a difference in means or Lin's interacted regression, plus a Neyman-type variance estimator and a Wald interval, justified by a finite-population central limit theorem that requires negligibility: no unit carries a non-vanishing share of the outcome variation. Outcomes like revenue, spending and medical charges are often heavy-tailed. The paper cites Young (2019) that in published experiments, deleting a single observation can make about a third of results significant at the 0.01 level insignificant, and notes that in the RAND Health Insurance Experiment one person carries about a third of the residual variation of second-year medical spending.

## 2. Technical details

Setting: a fixed finite population with covariates and both potential outcomes per unit, complete randomization is the only randomness, and the estimand is the sample average treatment effect. The estimators are the studentized difference in means and Lin's interacted estimator with covariates whose leverage vanishes. Without negligibility, Theorem 3.2 gives the limit law of the studentized statistic in terms of the limits of the normalized residual pairs of the dominant units; it is nonnormal in general and depends on how the two potential residuals of each dominant unit are paired, not only on the marginals, so populations with the same marginal distributions can have different limiting coverage (Proposition 3.5). If errors have a heavy-tailed law with tail index between one and two, the randomization law converges to a random limit determined by the largest realized residual pairs (Proposition 3.4). Under balanced allocation the Wald interval has coverage floor about 0.42 at nominal 0.95 for every population (Proposition 4.1) and about 0.84 when the two potential residuals of each unit are equal (Theorem 4.2); the paper says both floors are close to the best possible, and neither holds at the nominal level when 40% of units are treated. Without balanced allocation coverage can fall to the smaller of the treated and control proportions (Proposition 4.3). Simulations use N = 20,000 populations; the data application imputes missing potential outcomes under a constant or a proportional effect and redraws 100,000 assignments at π = 0.5 and 0.2.

## 3. Impact — potential & realized

Realized (per the paper): in three public experiments, RAND Health Insurance (N = 5,477), Oregon Health Insurance ED charges (N = 19,619) and the Hillstrom retail e-mail experiment (N = 42,613), with imputed outcomes the Wald interval's coverage was above 0.95 in every population under balanced allocation, well above the floors. With 20% treated, coverage fell below 0.95 in the RAND population (e.g. 0.937 under a constant effect), more under a proportional effect, while Oregon (about 0.947) and the retail population (about 0.945) stayed close to 0.95. In RAND the largest residual pair carries about a third of the residual variation (0.329 and 0.338 for the two estimators), versus 0.016 in Oregon and 0.026 in retail. The covariate (log of lagged outcome) changed the largest share only slightly and the two estimators had nearly the same coverage. The authors conclude the largest loss of coverage occurred under unbalanced allocation in the population where a few units dominate. Open items they list: the best universal floor, a floor for fixed allocation other than 1/2, and an interval with guaranteed coverage for every population. Potential: a concrete diagnostic (the share of residual variation in the largest units, plus allocation balance) for when to distrust a standard Wald interval.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A theory paper, but with a very practical message for anyone running experiments on revenue-like metrics: when a handful of whales carry the variance, the textbook interval can undercover badly, and balanced allocation matters.

A theory paper, but with a very practical message for anyone running experiments on revenue-like metrics: when a handful of whales carry the variance, the textbook interval can undercover badly, and balanced allocation matters. Note the real-data result is mild (coverage stays near 0.95 except in the RAND population at 20% treated), and relies on imputed potential outcomes, so the floors are worst-case, not typical, behaviour. Practitioners often winsorize or switch to permutation/bootstrap; this paper does not evaluate those fixes.

### Similar / related work

- [**Regression Adjustment for Ratios of Treatment Effects in Randomized Experiments**](2026-10-27-arxiv-regression-adjustment-ratios-treatment-effects.md) (in this bank) — another design-based look at regression adjustment in randomized experiments
- Lin (2013) and Li & Ding (2017) — the design-based regression-adjustment and finite-population CLT results the paper builds on; not in this bank
- Young (2019) — evidence that single observations can flip significance in published experiments; cited by the paper

### Jargon buster

- **Studentized statistic** — An estimate divided by its estimated standard error; Wald intervals assume this is approximately normal.
- **Negligibility** — The condition that no single unit carries a non-vanishing share of the variance, needed for finite-population CLTs.
- **Design-based inference** — Treats potential outcomes as fixed and treatment assignment as the only source of randomness.
- **Coverage floor** — A lower bound on how often a nominal 95% interval actually contains the truth.
