---
id: arxiv-differential-nonresponse-past-election-correction
title: "Correcting for Differential Nonresponse Using Past Election Data"
source: "Columbia University (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.31662"
published: "2026-11"
added: "2026-11-25"
category: statistical-modeling
tags: [differential-nonresponse, mrp, poststratification, survey-weighting, selection-bias, bayesian-hierarchical, calibration, election-surveys, out-of-sample-validation]
novelty: 3
sourced_via: "full-text fetch"
---

# Correcting for Differential Nonresponse Using Past Election Data

**Source:** [Columbia University (arXiv stat.ME)](https://arxiv.org/abs/2611.31662) · Published 2026-11 · Added 2026-11-25
**Category:** Statistical Modeling · **Tags:** `differential-nonresponse`, `mrp`, `poststratification`, `survey-weighting`, `selection-bias`, `bayesian-hierarchical`, `calibration`, `election-surveys`, `out-of-sample-validation`

## TL;DR

In election surveys the chance of responding can depend on the vote being measured, and weighting or MRP on demographics does not remove that bias. The paper estimates a two-parameter shift-and-stretch correction on the log-odds scale against the 2020 U.S. presidential results. It then applies the correction unchanged to 2024 across 436 congressional districts in the Cooperative Election Study. The corrected 95% bands contain the actual 2024 result in 98.2% of districts, versus 91.5% for a share-scale correction. About a third of the curvature and a 1.7-point level shift are specific to 2024.

## 1. Business context

Differential nonresponse occurs when the probability of responding depends on the quantity the survey measures. If one candidate's supporters respond less, they are underrepresented, and the estimated vote share differs systematically from the truth. Weighting and multilevel regression and poststratification (MRP) adjust for observed covariates. In the paper's words, they "do not eliminate this bias when response rates still differ by vote within demographic groups".

A correction can only be estimated where the outcome is known, and elections provide that. Results are published for every geographic unit. So a correction can be estimated on one election and applied to the next. The question is whether the bias is stable enough between elections for the transfer to work, and what the residual shows.

The setting is the Cooperative Election Study (CES), the largest academic election survey (about 60,000 respondents per cycle). Its respondents are validated against voter files. Prior work by Chooi (2026) worked at the state level with Meng's data-defect decomposition. This paper uses districts as units and conditions on demographics through MRP, so its correction is net of sample composition.

## 2. Technical details

- **Data.** 2020 and 2024 CES Common Content, restricted to validated voters (Catalist 2020, TargetSmart 2024) who reported a major-party presidential vote. That leaves 26,951 respondents in 2020 and 22,061 in 2024, with medians of 62 and 50 per district. The weight is the CES design weight (`commonweight`), not the after-the-fact vote-validated weights, because a forecast would only have pre-election information. Respondents pass a composite screen: panel membership, validation and answering the item.
- **Frame.** 120 cells per district (age × gender × race/ethnicity × education) from ACS five-year tables. Margins are treated as independent within district. A separate turnout model converts cells to expected voters. Validation targets are district-level presidential results from The Downballot.
- **MRP.** A Bayesian logistic regression in brms/Stan with demographic effects, region, race-specific slopes on the prior-election state lean and the district's deviation from it, and a district random intercept. Four chains of 2,000 iterations. The lean covariate never carries information about the election being estimated.
- **Two corrections, fit on 2020.**
  - *Share-affine* (in the style of Heidemanns et al., 2020): θ′ = (θ − b̄ − λ/2)/(1 − λ). Estimates: b̄ = −16.07 pp, λ = 0.40.
  - *Logit-affine*: logit θ′ = (logit θ − b)/(1 − λ). (b, λ) are solved so that the regression of bias on the true share and its square has zero linear and quadratic coefficients. Estimates: b = −0.752, λ = 0.275. The motivation is that shrinkage toward a regression surface is a log-odds phenomenon.
- **Validation.** 500 seeded posterior draws are poststratified and pushed through the correction to form 95% posterior predictive bands. The metrics are coverage, miss direction (above vs. below band), RMSE and residual curvature, plus a lineup check. The main bands treat the transferred parameters as fixed.
- **Little–Gelman nonresponse model with districts as groups.** It uses a relative response rate R_j with logit ζ_j = logit π_j + logit R_j + logit R_j^W, where R_j^W is the part of selection the design weights encode. The Beta hyperparameters are estimated on 2020 and transferred to 2024.
- **Two pre-specified cell-level variants.** Variant 1 applies a constant shift inside each cell before aggregation. Variant 2 lets the shift vary with district Black share, with correction-parameter uncertainty from a 500-replicate district bootstrap. Promotion criteria were fixed in advance. Variant 2's covariate had been chosen from 2024 residuals on an earlier frame, so a required 2020 check was specified first.

## 3. Impact — potential & realized

**Measured (uncorrected bias):** in both elections the district MRP understates the Republican two-party share by 16 to 18 points on average (2020 mean bias −16.07). The 2024 median gap is 19 points, larger in more Republican districts (slope −0.352, t = −42).

**Measured (transfer to 2024):**

| | Share-affine | Logit-affine |
|---|---|---|
| Coverage (nominal 95%) | 91.5% | 98.2% |
| Misses above – below | 37 – 0 | 7 – 1 |
| RMSE (pp) | 5.80 | 4.09 |
| In-sample 2020 RMSE (pp) | 5.58 | 4.59 |

- The share-affine misses all sit above the band and cluster in the most Democratic tercile. The 7–1 split under the logit correction is weak evidence on its own (p ≈ 0.07).
- *Curvature decomposition:* 65% of the 2024 curvature was already present in 2020. The logit correction removes 69% of the 2024 curvature and leaves 31%, which the authors call specific to 2024. The mean residual rose by about 1.6–1.7 points between elections (+1.62 under the logit correction, p < 0.001): the level shift.
- Out-of-band districts had a median 2020-to-2024 swing of 4.1 points, versus 2.2 inside. Three (NY-06, FL-26, NY-03) are in the top tenth by swing. The authors "cannot say that small samples alone explain" the misses.

**Measured (selection decomposition):** with the weights ignored, the composite relative response rate is R_comp = 0.375. Republican validated voters enter the sample at about 0.60 times the odds of Democratic voters. The weights alone give R_adj ≈ 0.421, and the residual after weighting is R_res = 0.454. On the logit scale the pieces add up (−0.319 − 0.185 = −0.504 vs −0.511). So the design weights account for about 62% of the selection, close to the 56% Little and Gelman reported for 1988 CBS telephone polls, where the sign was reversed.

**Measured (eight estimators on 2024):** the Little–Gelman model with the transferred prior reaches RMSE 0.078 and 90.1% coverage. MRP plus the logit correction reaches 0.041 and 98.2% (χ² 338 vs 436 df). Its weakness is the level: mean z of +6.9. Neither cell-level variant met its promotion criteria. Variant 1 had worse RMSE (4.35) with a 13–1 miss split. Variant 2 failed its 2020 check (Black-share coefficient −0.11, p = 0.95) and over-adjusted, with all 11 misses below the band and RMSE 4.62.

**Limitations stated:** one pair of elections, spanning a shift in coalition racial composition. The frame uses total population rather than citizen voting-age population. The 2024 ACS frame was published after the election. The outcome is reported vote among validated voters.

**Potential:** the authors propose estimating the relative response rate for every cycle from 2008 to 2024, and testing four transfers instead of one to measure how the correction decays with the gap between elections.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A careful, honest transfer test of a simple correction

The ingredients are known: MRP, the Little–Gelman relative response rate, and Heidemanns-style share corrections. The contribution is the clean out-of-sample design and the decomposition of what transfers and what doesn't. The logit-scale shift plus stretch has a natural reading: one parameter for selection, one for partial-pooling compression. It beats the share-scale version where it matters, in miss direction. The pre-registered variants failing, and the paper explaining *why* (moment conditions only constrain the regression they are written in; the concavity of the logit shift under aggregation), is the most transferable lesson.

How this maps to product survey work (my analogy): NPS or satisfaction surveys where the happiest or angriest users respond more are the same problem. A "known outcome" period, such as a behavioural metric observed for everyone, could calibrate a shift-and-stretch correction for the next wave. Caveats: n = 1 transfer, a 1.7-point level drift, and an over-coverage (98.2%) that comes with a biased level. Coverage alone is not calibration, a point the paper itself makes.

### Similar / related work

- [**The persistent non-response bias in a sample-matched poll for the 2024 U.S. presidential election**](https://arxiv.org/abs/2606.12889) — Chooi (2026). A state-level analysis of the 2024 CES with Meng's decomposition, finding a prior-election correction halves state-level error. Its national shift corresponds to this paper's level parameter without the stretch.
- [**Partial pooling beats synthetic respondents as estimators, not as covariates: a preregistered small-sample tournament**](2026-11-13-arxiv-partial-pooling-vs-synthetic-respondents-small-area.md) (in this bank) — another preregistered comparison of MRP-family survey estimators, on a Korean media panel.
- [**Small Area Causal Inference**](2026-11-19-arxiv-small-area-causal-inference-empirical-best-prediction.md) (in this bank) — mixed-model empirical best prediction for small areas, the same pooling-vs-shrinkage territory.

### Jargon buster

- **Differential nonresponse** — response probability depends on the outcome itself (here, the vote), so demographic weighting can't fix it.
- **MRP** — fit a multilevel model of the outcome on demographics and geography, then reweight cell predictions to the population's known composition.
- **Relative response rate (R)** — one group's response rate divided by the sum of both groups' rates. R = 0.5 means no differential nonresponse.
- **Logit-affine correction** — shift and rescale estimates on the log-odds scale. Here the shift absorbs selection and the stretch undoes partial-pooling shrinkage.
- **Posterior predictive band** — the range of outcomes the fitted model considers plausible. Coverage checks how often reality lands inside it.
- **Lineup check** — hide the real data among simulated datasets and see whether it stands out.
