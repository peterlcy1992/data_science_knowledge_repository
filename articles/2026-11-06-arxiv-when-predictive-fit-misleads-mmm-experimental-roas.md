---
id: arxiv-when-predictive-fit-misleads-mmm-experimental-roas
title: "When Predictive Fit Misleads: Selecting Marketing Mix Models Using Experimental RoAS Benchmarks"
source: "arXiv stat.AP (Hao Chen, Alvin Lim et al., Measured Inc.)"
url: "https://arxiv.org/abs/2611.06111"
published: "2026-11"
added: "2026-11-06"
category: product-analytics
tags: [marketing-mix-model, roas, model-selection, geo-experiments, calibration, adstock]
novelty: 4
sourced_via: "full-text fetch"
---

# When Predictive Fit Misleads: Selecting Marketing Mix Models Using Experimental RoAS Benchmarks

**Source:** [arXiv stat.AP (Hao Chen, Alvin Lim et al., Measured Inc.)](https://arxiv.org/abs/2611.06111) · Published 2026-11 · Added 2026-11-06
**Category:** product-analytics · **Tags:** `marketing-mix-model`, `roas`, `model-selection`, `geo-experiments`, `calibration`, `adstock`

## TL;DR

Marketing Mix Models are usually chosen by out-of-sample R2/MAPE/RMSE, but the paper shows predictive fit can diverge from recovery of the causal quantity (channel-level return on ad spend, RoAS). In 320 simulated datasets where candidates differ only in saturation form, the highest-R2 model was the RoAS-best model in 17.5% of cases, below the 25% expected from a random pick among four. Selecting against experimental RoAS benchmarks, even imprecise ones, did better.

## 1. Business context

MMMs estimate channel-level RoAS to guide marketing budget allocation, so errors translate into misallocated spend. Controlled experiments such as geo-experiments are credible benchmarks of incrementality but are costly and impractical for continuous measurement, so many teams compare competing MMM specifications on predictive-fit metrics, and widely used workflows (Meta's Robyn, Google's Meridian) include predictive or posterior-predictive diagnostics. The paper's claim is narrow: when the target is channel-level causal RoAS, predictive fit alone is not a sufficient selection criterion; it is not a claim that fit is irrelevant, nor a substitute for identification.

## 2. Technical details

Motivating simulation: 5 locations, 208 weeks, 4 channels, train weeks 1-156 and test 157-208. Model A (correct: adstock + saturation) vs Model B (misspecified, linear with trend). B has better out-of-sample fit (R2 0.93 vs 0.90; MAPE 9.07% vs 10.38%) but worse RoAS recovery (RoAS MAE 4.40 vs 3.12; B overestimates RoAS in all four channels by +172% to +241%), because its trend term absorbs long-term growth and credits it to concurrent spend; absolute errors remain large even for the correct model. Framework: candidate specifications (Hill and Weibull saturation, each C- or S-shaped, with geometric adstock) are fitted by constrained maximum likelihood with non-negative marketing coefficients; RoAS is computed from counterfactual predictions with a channel's spend set to zero, back-transformed from the log-sales scale; the specification minimizing RoAS-MAE against benchmark RoAS (known in simulation, experimental in applications) is selected (Algorithm 1). The paper notes that this RoAS is an average incremental return over the observed spend path, not marginal RoAS. Without benchmarks it proposes reporting RoAS across plausible specifications and a componentwise-median consensus diagnostic, described as descriptive rather than causal.

## 3. Impact — potential & realized

Realized (as reported in simulation): Monte Carlo replication of 40 datasets per DGP/scenario/adstock condition, 320 datasets and 2,560 model fits per condition. With adstock-included candidates differing only in saturation form, the highest-R2 model coincides with the RoAS-best model in 17.5% of datasets (95% CI 13.7-22.0%), Kendall correlation between the R2 ranking and RoAS-accuracy ranking is -0.02, and the R2-selected model has on average 1.47x the RoAS-MAE of the RoAS-best (about 41% vs 29% of mean RoAS error) while its R2 is 0.20 higher. When every candidate omits adstock, agreement rises to 55.3% and the penalty falls to 1.16x, so predictive fit is more informative under severe shared misspecification. The authors report the disagreement persists across media-spend collinearity and noise levels and under a misspecified carryover shape, and that even benchmarks with up to 50% noise picked more accurate models than R2 did. Real-world application (156 weeks, 3 digital channels, experimental RoAS benchmarks): two models with nearly identical R2 differed by 60% in RoAS accuracy against the benchmark. Limits stated by the authors: results are specific to the DGPs, candidate sets and spend processes studied; all candidates use geometric carryover; code and real data are available only on request/confidential. Potential: treat geo-experiment results as calibration targets for model selection, not just as a final check.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — practical, replicated, and directly actionable

Not a new estimator, but a useful reminder, with replicated evidence, that 'best forecast' and 'best causal estimate' are different selection problems; it echoes the prediction-vs-causation tension behind double ML. The result that R2 is uninformative among structurally sound candidates is specific to simulated DGPs, so weigh the magnitudes accordingly. The workflow (calibrate to experiments, otherwise report spread across specifications) is directly actionable for marketing-analytics teams. Authors work at an MMM vendor.

### Similar / related work

- **Chan and Perry, 2017 'Challenges and Opportunities in Media Mix Modeling'** — industry perspective on MMM identification challenges
- **Ebbes et al., 2021 and Dew et al., 2024** — collinearity can give different parameters with similar predictions, with consequences for causal estimation
- [**Trial-level surrogacy: ship on evals alone?**](2026-11-02-arxiv-trial-level-surrogacy-ship-on-evals-alone.md) (in this bank) — related question of when a proxy metric can stand in for the causal target

### Jargon buster

- **RoAS** — Return on ad spend: incremental revenue per dollar spent on a channel.
- **Adstock** — A carryover transform: ad effects persist and decay over following weeks.
- **Saturation (Hill/Weibull)** — Diminishing returns curve: each extra dollar of spend yields less incremental sales.
- **Geo-experiment** — An experiment that randomizes regions to ad exposure to measure incrementality.
