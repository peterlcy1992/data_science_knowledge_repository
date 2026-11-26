---
id: arxiv-correcting-upward-bias-calibration-summaries
title: "Simple, general strategies for correcting the upward bias of calibration summaries of prediction models"
source: "University of British Columbia / UNC Chapel Hill (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.33846"
published: "2026-11"
added: "2026-11-26"
category: statistical-modeling
tags: [calibration, integrated-calibration-index, bias-correction, folded-normal, clinical-prediction-models, model-validation, fairness, smoothing]
novelty: 3
sourced_via: "full-text fetch"
---

# Simple, general strategies for correcting the upward bias of calibration summaries of prediction models

**Source:** [University of British Columbia / UNC Chapel Hill (arXiv stat.ME)](https://arxiv.org/abs/2611.33846) · Published 2026-11 · Added 2026-11-26
**Category:** Statistical Modeling · **Tags:** `calibration`, `integrated-calibration-index`, `bias-correction`, `folded-normal`, `clinical-prediction-models`, `model-validation`, `fairness`, `smoothing`

## TL;DR

Scalar calibration summaries such as the integrated calibration index (ICI) average the *absolute* value of a noisy calibration-curve estimate. Where that estimate's sampling distribution crosses zero, the absolute value "folds" it and biases the summary upward. Sadatsafavi, Rezaeianzadeh and Sadatsafavi quantify this "folding bias" with the folded-normal mean. They propose four corrections (local/global plug-in and local/global inversion) that need only each point's smoothed error and its standard error. Global Inversion is their recommended method: it removed the most bias in simulations, e.g. cutting the ICI of a truly calibrated model by 66% with LOESS, at the cost of a slightly higher mean absolute error when bias was small.

## 1. Business context

Calibration matters for clinical prediction models: a miscalibrated model can mislead patients and providers. "Moderate" calibration is usually checked with a flexible calibration curve (LOESS, restricted cubic splines or GAM). Scalar summaries make models and subgroups comparable. The ICI (Austin & Steyerberg 2019) is the density-weighted mean absolute gap between the curve and the diagonal. E50 and E90 are the median and 90th percentile of the absolute errors. In machine learning the analogue is expected calibration error (ECE).

These summaries are biased upward. If a model is perfectly calibrated, the true ICI is 0, but the estimate is always positive. The authors say mitigating this bias for ICI and quantile metrics on flexible curves "has not been sufficiently explored". The closest attempt is a recent cross-validated estimator that applies only to ICI (Berta et al., V-ECE). Prior bias work in meteorology and ML has mostly targeted quadratic errors, where E(ê²) = e² + σ² makes the bias easy to quantify.

The stakes include fairness audits. Reporting guidelines ask for performance in key subgroups. For the same true ICI, the bias is larger in smaller groups. So, in the authors' words, raw ICI gaps "conflate differential calibration with differential sample size". Apparent miscalibration is exaggerated in under-represented groups.

## 2. Technical details

- **Setup.** Binary outcome, validation sample of n iid individuals. The true error is e(X) = g(P̂) − P̂, with g(p) = E(Y | P̂ = p). True ICI = E|e(X)|. A smoother gives êᵢ and its SE σ̂ᵢ. Raw ICI = (1/n)Σ|êᵢ|.
- **Folding bias.** If êᵢ ~ N(eᵢ, σᵢ²), then |êᵢ| is folded normal. The pointwise bias is μ_FN(e, σ) − |e|, where μ_FN(e, σ) = σ√(2/π)·exp(−e²/2σ²) + e[2Φ(e/σ) − 1].
  - The bias depends on the standardized distance e/σ. It peaks sharply near e = 0 and fades in the tails.
  - Illustration: with true error 0.010, E|ê| = 0.025. With true error 0.045, E|ê| = 0.047.
  - The folding bias is relative to the smoother's estimate. Smoother bias (e.g. near the boundaries) can offset or aggravate it.
- **Local Plug-in (LP).** Treat ê as the truth and estimate the bias as b̂ᵢ = μ_FN(êᵢ, σ̂ᵢ) − |êᵢ|. Subtract it and clip each point at 0. Corrected values would be negative whenever |êᵢ| < 0.436σ̂ᵢ.
- **Global Plug-in (GP).** Subtract the biases without pointwise clipping and clip only the final ICI at 0. Unclipped, the plug-in extends Kumar et al.'s correction for binned ECE to flexible curves, with μ_FN replacing their Monte Carlo step.
- **Why invert.** Near e = 0, plugging in ê moves down the bias curve, so the plug-in under-corrects exactly where bias is large. (In the convex tails it overestimates, but bias there is small.)
- **Local Inversion (LI).** Treat the true error as latent. For each point, find kᵢ ∈ [0,1] with μ_FN(kᵢêᵢ, σ̂ᵢ) = |êᵢ|. Set kᵢ = 0 when |êᵢ| is below the noise floor σ̂ᵢ√(2/π). Corrected ICI = mean of kᵢ|êᵢ|. The authors call the inversion methods new, to their knowledge, for miscalibration summaries.
- **Global Inversion (GI).** One shared k: solve Σμ_FN(k|êᵢ|, σ̂ᵢ) = Σ|êᵢ|. Then ICI_GI = k·ICI_raw, with k = 0 if the raw ICI is at or below the mean noise floor. The true error curve is assumed to be a scaled copy of the observed one. This borrows strength across points and needs one univariate root-find.
- **Assumptions.** Normal sampling distribution of each êᵢ (the same CLT assumption behind ±1.96 SE bands). No homoscedasticity assumption and, for ICI, no assumption on the correlation among errors.
- **Quantile metrics.** The exact extension for E50/E90 would need the joint distribution of errors along the curve (covariance matrix or bootstrap). Instead, the authors read E50/E90 off the "mean-matched" corrected error curves built for ICI. These do not target quantile bias directly.
- **Generality.** The methods only need the fitted curve and its pointwise SE. So the authors say they apply to binary, ordinal, censored time-to-event and counterfactual (treatment-benefit) outcomes. Only the binary case is evaluated here.
- **Code.** A base-R `ici_gi()` (using `uniroot` and `pnorm`) is in Appendix 4. On R's 248-subject `infert` data with a fixed-coefficient model and LOESS, raw ICI is 0.055 against a noise floor of 0.043. GI gives k = 0.68 and ICI 0.038, about a third lower.

## 3. Impact — potential & realized

**Measured — simulations.** These adapt Austin & Steyerberg's design. A "quadratic" setting omits a₂x² (a₂ ∈ {0, 0.25, 0.5}). An "interaction" setting omits a₃x₁x₂ (a₃ ∈ {0, 0.5, 1}). Each also has a true-model scenario with ICI = 0. Development n is fixed at 1,000, validation n ∈ {250, …, 4000}, with 1,000 replicates per scenario. Smoothers are LOESS (span 0.75, local quadratic), RCS (4 knots) and GAM (REML).
- Raw ICI shows a large upward bias for calibrated or mildly miscalibrated models, still noticeable at n = 4000. All four methods reduced bias in every scenario and sample size.
- **True model, ICI ×1000 (LOESS):** raw 24.5; LP 18.0 (−27%); LI 14.9 (−39%); GP 13.9 (−43%); GI 8.3 (−66%). RCS: GI −59%. GAM: GI −52%.
- **True model, E90 (LOESS):** raw 46.2; LP −7%; LI −11%; GI 15.0 (−68%). For E90, the local methods were generally indistinguishable from raw.
- **Miscalibrated models, mean absolute bias of ICI (LOESS):** raw 8.7; GI 2.4 (−72%). With GAM, all methods were similar (−42% to −48%).
- **Miscalibrated models, MAE of ICI:** small changes. LOESS GI −2%; GAM GI +10%. At moderate miscalibration GI overcorrected, giving slightly higher MAE.

**Measured — GUSTO-I case study.** Data: 40,830 acute MI patients, 7.0% 30-day mortality. A seven-predictor logistic model is fitted on a "small" development sample (500 patients, EPV ~5) or a "large" one (8,830, EPV ~88). It is frozen and assessed in validation subsamples of 500–32,000 from a fixed pool, over 100 replicates. The estimand is fixed, so any drift with n reflects bias.
- Large-development (well-calibrated) model: raw ICI falls from 13.0 to 4.4 (×10⁻³) as n grows from 500 to 32,000. At n = 500 it is barely distinguishable from the 12.0 noise floor of a perfectly calibrated model. GI gives 6.7 → 3.9 and LP 10.0 → 4.1.
- Small-development (miscalibrated) model: raw 19.4 → 15.9. GI 14.4 at n = 500, and every method gives 15.8 at 32,000. Correction matters much less from n = 2,000 onward.

**Limitations the authors state.** GI can slightly increase MAE when bias is small. Performance for ordinal, survival and counterfactual outcomes needs dedicated study. A binned-k version between LI and GI is untested because it adds a tuning parameter. The coverage of bias-corrected bootstrap CIs is also untested.

**Potential.** Bias-adjusted summaries can come straight from any reported curve and its SE bands. Bootstrap CIs could use GP or GI inside each replicate. Because these can return exactly 0, a percentile CI could then include the null of perfect moderate calibration, which raw-ICI bootstrap intervals never do. The authors also suggest future decision rules for when to invoke a correction.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A small, sharp fix for a widely ignored bias, cheap enough to become a default

The mechanism is textbook: the folded normal and E|X| > |E X|. The plug-in correction is, as the authors say, an extension of Kumar et al. The contribution is twofold. First, the clear diagnosis that plug-in under-corrects exactly where bias is largest. Second, the global inversion trick: one root-find, a ten-line base-R function, and it works with any smoother that reports SEs. That is the kind of method that gets copied because it costs nothing to add next to a calibration plot. The evidence is limited to two simulation designs and one dataset, all with binary outcomes. GI's "scaled copy of the observed curve" assumption is strong, and it overcorrected at moderate miscalibration.

For DS practice outside medicine: anyone comparing ECE or calibration across segments (markets, cohorts, demographic slices for fairness reviews) of very different sizes faces the same artifact. Small segments look worse just because they are small. Reporting the noise floor σ̂√(2/π) next to the raw metric is a free sanity check, even before applying GI. That application is my extrapolation; the paper evaluates clinical risk models only.

### Similar / related work

- [**How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of Post-hoc Calibration**](2026-11-03-arxiv-ctr-recalibration-temporal-evaluation-fresh-data.md) (in this bank) — an empirical study on Avazu ads data that uses binned ECE to judge Platt and isotonic recalibration. Its ECE comparisons are the sort of absolute-error summary this paper says is biased upward in small samples.
- [**Verified Uncertainty Calibration**](https://arxiv.org/abs/1909.10155) — Kumar, Liang & Ma (NeurIPS 2019). Their Monte Carlo debiasing of binned ECE corresponds to the unclipped plug-in method here.
- [**V-ECE: Estimating general expected calibration errors**](https://arxiv.org/abs/2602.24230) — Berta et al. (2026). A cross-validated ECE estimator, the closest prior fix. The authors note it does not extend to quantile metrics or partially observed outcomes, but may be more robust to smoother bias.
- **The integrated calibration index (ICI) and related metrics** — Austin & Steyerberg (Statistics in Medicine 2019). Defines ICI, E50 and E90, and provides the simulation design adapted here.

### Jargon buster

- **Moderate calibration** — predicted risks match observed event rates among people with the same predicted risk (X% of those predicted X% have the event).
- **Integrated calibration index (ICI)** — the average absolute difference between the smoothed calibration curve and the diagonal, weighted by where predictions fall.
- **E50 / E90** — the median and 90th percentile of the absolute calibration errors along the curve.
- **Folding bias** — taking the absolute value of a noisy estimate whose distribution straddles zero pushes its mean up, even if the estimate itself is unbiased.
- **Folded normal** — the distribution of |Z| when Z is normal; its mean has a closed form, used here to compute the bias.
- **Noise floor** — σ√(2/π), the expected absolute error from noise alone when the true error is 0; a raw ICI below it is consistent with perfect calibration.
- **Plug-in vs inversion** — plug-in treats the observed error as the truth to estimate the bias; inversion asks which true error would produce the observed absolute error on average.
- **EPV (events per variable)** — the number of outcome events divided by the number of predictors; low EPV signals an overfit, likely miscalibrated model.
