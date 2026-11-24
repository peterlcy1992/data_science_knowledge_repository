---
id: arxiv-level-invariant-anytime-valid-risk-model-monitoring
title: "Which Loans, Not How Many: Exactly Level-Invariant, Anytime-Valid Monitoring of Deployed Risk Models"
source: "Carnegie Mellon University (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.28342"
published: "2026-11"
added: "2026-11-24"
category: statistical-modeling
tags: [model-monitoring, calibration-slope, anytime-valid, e-values, confidence-sequences, conditional-likelihood, change-detection, credit-risk]
novelty: 3
sourced_via: "full-text fetch"
---

# Which Loans, Not How Many: Exactly Level-Invariant, Anytime-Valid Monitoring of Deployed Risk Models

**Source:** [Carnegie Mellon University (arXiv stat.ME)](https://arxiv.org/abs/2611.28342) · Published 2026-11 · Added 2026-11-24
**Category:** Statistical Modeling · **Tags:** `model-monitoring`, `calibration-slope`, `anytime-valid`, `e-values`, `confidence-sequences`, `conditional-likelihood`, `change-detection`, `credit-risk`

## TL;DR

A refinancing wave can change *how many* mortgages prepay without changing *which* loans the model ranks as likely to prepay. In a logistic recalibration model, conditioning on the monthly event count removes the calibration intercept, so the likelihood of which loans prepay depends only on the calibration slope. The paper builds three anytime-valid monitors on this fact: a slope e-process, a level monitor and a slope change-point rule. On Freddie Mac loans, resampling at a fixed slope reproduces 78% of the maintained model's monthly AUC variance in development and 70% in the holdout.

## 1. Business context

When mortgage rates fall, more borrowers refinance, and a portfolio can prepay faster than its model predicts. A monitoring team then has to decide whether updating the predicted level is enough, or whether the association between the model's scores and prepayment has changed. The paper says this distinction matters for the model reviews required in banking (it cites the Fed/OCC/FDIC model risk guidance, ECB validation instructions and Siddiqi 2017).

The standard dashboard (AUC, Gini, stability indices, calibration checks) mixes the two. The author notes that attainable AUC also depends on the intercept and the score distribution, so AUC alone cannot isolate changes in the score–outcome association. The goal is a monitor whose slope test is exactly invariant to level shifts and valid at every monthly look.

## 2. Technical details

- **Model.** Write θ for the model's scored log-odds. Cox's logistic recalibration gives P(Y=1) = σ(α_t + β_t·θ), with calibration intercept α_t and calibration slope β_t. Loan outcomes are modelled as independent given the past, the current book and the month's intercept. The intercept may be unobserved.
- **Conditional reduction (classical).** Conditional on the month's count M of prepayments, the probability of the observed event set is a one-parameter exponential family in β with sufficient statistic T (the sum of prepayers' logits). It is free of α. A log-space elementary-symmetric recursion computes the normaliser in O(n·m_max) time.
- **Monitor 1: fixed-start slope product.** It multiplies monthly conditional likelihood ratios to test the lower bound H₀: β_t ≥ β₀ for all t. Under the null it is a nonnegative supermartingale, so by Ville's inequality the chance it *ever* crosses threshold 20 is at most 5%. The paper notes that each monthly factor is a conditional (COND) e-variable in the sense of Hao & Grünwald.
- **Monitor 2: restarted level sum.** It uses the count factor with the slope pinned at 1 (the model's stated scale) to track departures from an intercept tolerance |α_t| ≤ 0.10. It signals at 20.
- **Monitor 3: restart-intersection rule.** It intersects slope confidence sequences started at each past month and alarms when they share no slope. The newer binding set gives the direction of change. With a constant slope, the mean time to false alarm is at least 1/α, or 20 months at α = 0.05 (following Shekhar & Ramdas).
- **Prior for the confidence sequence.** A discrete slope grid leaves an "off-grid width floor": when the truth falls between nodes, the width stays positive. The author recommends a continuous uniform prior on [0.20, 1.60], computed with chord lower bounds that give an outer confidence set. The mortgage runs use an equal-weight 29-node grid on the same range.
- **Diagnostic: pinned-slope excess-variance share ρ.** Each month's event set is redrawn at a fixed slope, keeping the real book and real count. ρ = 1 − Var_null/Var_obs is the share of a dashboard statistic's month-to-month variance *not* explained by that benchmark.
- **Data.** Freddie Mac Single-Family Loan-Level Dataset: 26 vintages (1999–2024) of 50,000 loans each, 1.3M loans and 69.3M loan-months through 2025. Monitored books have 20,000 loans per month. Models are LightGBM retrained each January on a trailing ten-year window ("maintained"), a spline-logistic GLM, and "frozen" variants that keep the scoring function from a named year.
- **Design.** Commissioning was January 2001–December 2003, development January 2004–December 2015, and the holdout January 2016–August 2025. Windows, the tolerance δ = 0.10 slope units and the hypotheses were registered before the loan-level data were downloaded. The LightGBM commissioning slope is 0.759 (SE 0.007), which gives an alarm boundary of 0.646.

## 3. Impact — potential & realized

**Measured (Freddie Mac panel and simulations):**
- **Dashboard noise.** The fixed-slope benchmark reproduces 78% of the maintained model's realized-AUC variance in development (95% interval 57–100%) and 70% in the holdout (48–100%). Monthly slope fits have excess shares of 62% (maintained) and 76% (frozen2003).
- **Intercept-fixed ablation.** Holding the intercept at its commissioned value makes the slope fit correlate −0.963 with the estimated intercept, and −0.962 even in the slope-one benchmark. An intercept constraint can produce apparent slope variation at a fixed slope.
- **Development alarms.** At boundary 0.646, the fixed-start slope product crosses only on the spline GLM (May 2007). It stays below 20 on the other five paths. The restarted level sum crosses on all six paths.
- **Holdout alarms.** The level sum first crosses in January 2018 on both paths. The slope product stays below threshold on both. The restart-intersection rule signals downward for frozen2015 in April 2018, and upward for the maintained model in a supplementary run in August 2019.
- **Interval width (simulation).** At look 240 with slope 0.875 (off the grid), the continuous prior gives median width 0.0439, versus 0.0580 for the 29-node prior. Both mixtures have 97.0–99.6% every-look coverage across settings at look 240. In a stress test, the 29-node width stays at 0.04995 while the continuous prior reaches 0.00166.
- **Preregistered outcomes were mixed.** H1 (model-based concordance explains most AUC variance) was not met. H2 (no slope alarm on maintained, alarm on frozen) was met in development but not in the holdout. H3(ii) on detection speed was not met: for a break to slope 0.55, the restarted slope sum's median delay is 45 months, versus 16 for a score CUSUM. That CUSUM, however, alarms on 81% of paths under a pure intercept shift, while the slope sum alarms on none. The fixed-start slope product was named the primary statistic *after* the panel outcomes were available.

**Potential:** A monitoring split that sends level problems to recalibration and slope problems to model review, with error guarantees that hold at every monthly look. The code is to be released with the published version.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Classical conditional logit meets e-processes, carefully applied to a real credit book

Every ingredient is known: Cox's conditional likelihood, Ville's inequality, mixture confidence sequences and restart-based change detection. The useful step is to put them together so the slope test is *exactly* blind to level shifts. That fits a real pain point, because refinancing waves and macro shocks trip AUC and PSI charts that model-risk teams then have to explain. The fixed-slope resampling diagnostic is the most portable piece: it tells you how much of your AUC wobble is just book and count noise.

The paper is unusually candid about its preregistration. Several hypotheses failed, the slope monitor is slow (45 vs 16 months), and the primary statistic was chosen after seeing outcomes. The guarantees also rest on within-month conditional independence and a linear logit link, and the paper's own tests reject linearity in 16 of 144 maintained development months. Expect bank validation teams to try the excess-variance diagnostic before they adopt the full alarm stack.

### Similar / related work

- [**Sequential Conditional Paired-Sample Testing with Applications to Online Monitoring**](2026-11-19-arxiv-sequential-conditional-paired-sample-testing-monitoring.md) (in this bank) — anytime-valid, nonparametric calibration monitoring; it tests the full conditional distribution rather than a single slope parameter.
- [**Anytime-Valid Inference in Linear Models with Clustered Outcomes: Exact Multivariate Tests and Cluster-Robust Confidence Sequences**](2026-10-20-arxiv-anytime-valid-clustered-linear-models.md) (in this bank) — confidence-sequence machinery for regression parameters in experiments.
- [**When Your Model Stops Working: Anytime-Valid Calibration Monitoring**](https://arxiv.org/abs/2603.13156) — Farran's PITMonitor, a mixture e-process on PITs with changepoint estimation; this paper contrasts it as not intercept-invariant.
- [**E-backtesting**](https://arxiv.org/abs/2209.00991) — Wang, Wang & Ziegel; e-processes for sequentially rejecting risk forecasts on market data.

### Jargon buster

- **Calibration slope** — the multiplier on the model's log-odds in a recalibration fit; 1 means the scores separate outcomes as strongly as stated, below 1 means they over-separate.
- **Calibration intercept** — the shift in overall predicted level; a refinancing wave moves this without necessarily touching the slope.
- **Conditional likelihood (on the count)** — the probability of *which* units had events given *how many* did; the intercept cancels out of it.
- **E-process / anytime-valid** — an evidence measure you can check at every look; under the null its chance of ever exceeding 1/α is at most α.
- **Confidence sequence** — a sequence of intervals that contains the true parameter at all times simultaneously with the stated probability.
