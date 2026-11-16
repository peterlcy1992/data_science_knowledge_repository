---
id: roblox-sitewide-impact-experiment-comparability
title: "Making Experiment Results Comparable through Sitewide Impact Estimation"
source: "Roblox (arXiv stat.AP)"
url: "https://arxiv.org/abs/2611.18411"
published: "2026-11"
added: "2026-11-16"
category: experimentation-causal
tags: [sitewide-impact, coverage-factor, diluted-treatment-effect, ratio-metrics, delta-method, holdouts, prioritization, growth-attribution, segment-recombination]
novelty: 4
sourced_via: "full-text fetch"
---

# Making Experiment Results Comparable through Sitewide Impact Estimation

**Source:** [Roblox (arXiv stat.AP)](https://arxiv.org/abs/2611.18411) · Published 2026-11 · Added 2026-11-16
**Category:** experimentation-causal · **Tags:** `sitewide-impact`, `coverage-factor`, `diluted-treatment-effect`, `ratio-metrics`, `delta-method`, `holdouts`, `prioritization`, `growth-attribution`, `segment-recombination`

## TL;DR

An experiment's lift tells you whether a treatment works for the users it reaches, but it can't be compared across product surfaces that differ in reach and in how much their users contribute to a platform metric. Roblox defines **sitewide impact**: the relative change in a platform aggregate (e.g. total play time) if the treatment reached 100% of its target population, which is experiment lift × a **coverage factor**. It gives estimators for difference-in-means and for variant-level ratio metrics and segment recombination, and validates them with 1,349 A/A periods and a long-term payments holdout. Across 139 significant experiments, the rank correlation between experiment lift and sitewide impact is only 0.20.

## 1. Business context

Roblox runs experiments across very different surfaces: experience discovery, quality of experience, the virtual economy, notifications, creator tools. These differ sharply in **reach** (how many users the treatment touches) and in how much the affected users **contribute** to any sitewide metric. A 5% lift on a niche surface and a 0.5% lift on the home page are not on the same scale, yet strategic decisions (which domain to invest in, how much of year-over-year growth came from shipped products) need them to be. The paper asks for a well-defined counterfactual estimand that puts every experiment on one scale: how much would the platform aggregate move if the treatment reached its full target population during the measurement period?

The authors stress this is **not transportability**. Transportability carries an effect to a population with a different covariate distribution and needs positivity. Here the experiment's arms are already a random sample of the target population a full rollout would treat, so there is no covariate shift to correct. Users outside the affected population simply stay untreated in the counterfactual and contribute zero change, so positivity between them and the affected population (which fails by construction, e.g. users who never open the notification centre) is not required. The idea is closest to the **diluted treatment effect** from trigger analysis (Deng & Hu, 2015), which also rescales a triggered-user effect by the triggered users' share of the metric. The paper's additions: reconstructing the no-treatment sitewide baseline from experiment data, extending it to variant-level ratio metrics, and recombining it across segments.

## 2. Technical details

**Estimand (difference-in-means).** With S the sitewide population and A ⊆ S the target (reachable and eligible) population, sitewide lift L_S = (μ_S|1 − μ_S|0)/μ_S|0. Under SUTVA and the assumption that **reach is unaffected by treatment**, users outside A contribute zero, giving **L_S = L_A · C**, where L_A is the experiment (affected-population) lift and **C = N_A μ_A|0 / (N_S μ_S|0)** is the coverage factor: the affected population's share of the sitewide metric when no one is treated. Example from the paper: a 2% lift in a population holding 10% of the metric is a 0.2% sitewide lift.

**Reconstructing the baseline.** The observed sitewide mean already contains the treatment effect on treated users, so the no-treatment sitewide mean is estimated as μ̂_S|0 = μ_S^obs − (N_T/N_S)(Ȳ_T − Ȳ_C).

**Holding reach fixed** biases the estimate whenever the treatment itself changes reach (a better feature may pull more users onto its surface, biasing downward in that example), but it gives every surface the same reference point, the control state, so results stay comparable.

**Variant-level ratio metrics.** Many platform metrics are ratios of totals (crashes per hour of play). A user-level ratio is a per-user average and takes the same coverage factor; a **variant-level** ratio (total numerator / total denominator) does not, because the affected population holds a different share of crashes than of play time. The estimator reconstructs no-treatment numerator and denominator totals separately, adds each component's effect as if the whole affected population were treated (ΔNum_S = (N_A/N_S)(Num_T − Num_C), likewise for Den), and compares the ratio after with the ratio before. Using a single coverage factor instead gives a median error of 3.5% of the sitewide lift with the denominator's factor (29% or more for one experiment in ten), and 7.2% or more for one in ten with the numerator's. Across 484 experiments ending 8 Sep–29 Oct 2026, the two single-factor answers differ by a median 3.1% of the sitewide lift.

**Segments / heterogeneity.** Each segment (new users, US, frequent Android players…) has its own reach, baseline contribution and lift, hence its own coverage factor. Overall sitewide lift is recombined from segment **totals**, Σ_g N_S,g μ_S,g|1 / Σ_g N_S,g μ_S,g|0 − 1, not by averaging segment lifts. Across 155 experiments, recombining totals cuts the mean absolute error versus the reported overall lift from 1.33 to 0.47 pp for time spent and from 7.01 to 1.68 pp for bookings (not exact because supported segments cover a median 80% of users).

**Intervals.** The platform's 95% interval for the difference in means is divided by the control mean and multiplied by C, treating both as known; the authors note C's sampling error has not been measured, so the interval is slightly too narrow. For daily reads of a holdout they widen it with a Lan–DeMets approximation to an O'Brien–Fleming boundary (z_t = 1.96/√(n_t/n_end)), described as a band for reading results afterwards, not a stopping rule.

## 3. Impact — potential & realized

**Realized (in production at Roblox).** The estimator is integrated into Roblox's internal experimentation platform.
- *Lift ≠ impact:* among 139 A/B tests started and ended in 2026 that were significant on time spent (p<0.05), Spearman correlation between |sitewide impact| and |experiment lift| is **0.20**; 5 of the 10 largest experiment lifts are among the 10 largest sitewide impacts; for top-k lists up to k=50, only 35–50% overlap.
- *A/A validation:* pre-experiment periods of 1,349 experiments closed in 2026 (after dropping 64 with coverage factor >1, flagged as data errors, and 27 with <10,000 users per arm): median sitewide lift 0.00004%, signed-rank p = 0.59. The median coverage factor is 34%; the narrower spread versus experiment lift follows from the scaling and is "not extra precision".
- *Holdout validation:* a payments holdout (20 Jan–18 Mar 2026, six payment surfaces, eight innovations) — the summed sitewide impacts (best-arm upper bound, since the platform doesn't record which arm shipped) end inside the holdout's interval: 0.41% vs holdout 0.50% for bookings, 0.22% vs 0.21% for probability of spending Robux. On time spent and DAU the holdout shows small negative values within noise, consistent with payment changes not moving engagement.

**Potential.** Two strategic uses: **cross-domain prioritization** (rank experiments on different surfaces on one platform metric) and **growth attribution** (decompose year-over-year growth into organic growth, estimated from long-term holdout control groups, and product contribution, as the sum of holdout lifts scaled by one plus the organic growth rate). Stated limitations: SUTVA and fixed reach are strong and untestable from the experiment alone; computation is costly because the baseline is re-aggregated per experiment window; fixed lookback windows fit long-running experiments poorly.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Turns "diluted effect" into a production-grade, cross-surface currency

The core identity (lift × share-of-metric) is the familiar diluted-treatment-effect from trigger analysis, so the statistics are not new. What makes it a 4 is the production-first package around it: reconstructing the counterfactual baseline, the variant-level ratio estimator with quantified error from the naive shortcut, segment recombination by totals, and honest validation against both A/A periods and a real holdout. The 0.20 rank correlation is the number every experimentation team should put in front of leadership the next time a roadmap is ranked by "% lift". Any platform with a portfolio-level experiment review (marketplaces, games, social) will copy it. The weak spot is the fixed-reach assumption — exactly the treatments you most want to find (ones that grow a surface) are the ones it underestimates.

### Similar / related work

- [**Diluted Treatment Effect Estimation for Trigger Analysis in Online Controlled Experiments**](https://dl.acm.org/doi/10.1145/2684822.2685307) (Deng & Hu, WSDM 2015) — the rescaling of triggered-user effects that the coverage factor generalizes.
- [**Many Hands Make Light Work: Long-Term Effect Inference for the Experiment Reservoir**](2026-10-28-arxiv-experiment-reservoir-surrogate-long-term-effects.md) (in this bank) — another way to make portfolio-level claims from many experiments, via surrogates rather than rescaling.
- [**Aggregating treatment effects across multiple outcomes**](2026-11-12-arxiv-aggregating-treatment-effects-multiple-outcomes.md) (in this bank) — the complementary comparability problem: across metrics rather than across surfaces.

### Jargon buster

- **Sitewide impact** — the relative change in a platform-wide total if a treatment were rolled out to everyone it targets, holding everyone else untreated.
- **Coverage factor** — the share of the sitewide metric that the targeted users account for under no treatment; multiplying experiment lift by it gives sitewide lift.
- **Variant-level ratio metric** — a ratio of totals within a variant (all crashes ÷ all play hours), so heavy users count more, unlike the average of per-user ratios.
- **Holdout** — a random share of users kept from a set of launches for months, measuring the cumulative effect of a full rollout directly.
- **O'Brien–Fleming / Lan–DeMets** — group-sequential boundaries that widen intervals on early looks so repeated peeking doesn't inflate false positives.
