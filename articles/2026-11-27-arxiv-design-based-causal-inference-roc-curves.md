---
id: arxiv-design-based-causal-inference-roc-curves
title: "Design-based causal inference for ROC curves"
source: "Tsinghua University (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.34057"
published: "2026-11"
added: "2026-11-27"
category: experimentation-causal
tags: [roc-curve, distributional-treatment-effects, design-based-inference, rank-based-inference, covariate-adjustment, simultaneous-confidence-bands, tail-inference, randomized-experiments]
novelty: 3
sourced_via: "full-text fetch"
---

# Design-based causal inference for ROC curves

**Source:** [Tsinghua University (arXiv stat.ME)](https://arxiv.org/abs/2611.34057) · Published 2026-11 · Added 2026-11-27
**Category:** Experimentation & Causal Inference · **Tags:** `roc-curve`, `distributional-treatment-effects`, `design-based-inference`, `rank-based-inference`, `covariate-adjustment`, `simultaneous-confidence-bands`, `tail-inference`, `randomized-experiments`

## TL;DR

Li and Yu define a causal ROC curve for completely randomized experiments. For each level α, R(α) is the share of treated potential outcomes that beat the top-α quantile of the control distribution. Their estimator needs only pooled outcome ranks. It comes with Neyman-type conservative CIs, a covariate adjustment that keeps the estimand and never increases asymptotic variance, simultaneous bands, and a tail-slope estimator for the extreme upper tail. In simulations, adjustment cut pointwise CI length by 18.2%–20.9%. On an Ecuador online-learning experiment, a lottery raised the share of students above the top 5% and 10% of placebo study time.

## 1. Business context

Randomized experiments are usually summarized by the average treatment effect (ATE). Often the question is about the distribution instead. The authors' example: what share of treated students outperform the median, upper quartile or top decile of the control group? Such comparisons matter most when outcomes exist only as rankings, where outcome models do not apply.

Existing tools each leave a gap:
- **Quantile treatment effects (QTE)** compare outcome values at a common percentile. They need numerical outcomes.
- **Distributional treatment effects (DTE)** compare exceedance probabilities at a fixed outcome threshold y. They also need numerical outcomes.
- **AUC / Mann–Whitney** needs only ranks but collapses everything into one scalar, which can mask heterogeneous effects across outcome levels.
- **Covariate adjustment** for the ATE (Lin 2013; Li & Ding 2017) relies on numerical outcomes. Model-based ROC regression (Brumback et al. 2006) imposes assumptions on outcome distributions.

The paper asks two questions. Can design-based inference cover the whole outcome distribution using only ranks? And can baseline covariates make it more efficient?

## 2. Technical details

- **Framework.** Finite population of n units, n₁ treated completely at random. Potential outcomes are fixed; the assignment is the only randomness. No outcome model. The treated share pₙ converges to p ∈ (0,1).
- **Estimand.** R(α) = G₁{G₀⁻¹(α)}, where G is the survival function. A finite population has discrete distributions, so ties at the threshold are counted fractionally with weight λₙ(α). This makes the control exceedance exactly α. If the two marginals coincide, R(α) = α for all α. Deviations from the diagonal show distributional differences.
- **Links to other estimands.** For continuous limits, R(α) − α = DTE{q(α)}. The difference is that the DTE uses a fixed numerical threshold, while the ROC threshold is an unknown control quantile estimated from data. AUC = ∫R(α)dα. In a N(0,1) control vs N(1,9) treatment example: ATE = 1, QTE(0.1) = −1.56 and QTE(0.9) = 3.56, R(0.9) = 0.777, R(0.5) = 0.631, R(0.1) = 0.463, AUC = 0.624.
- **Estimator.** A plug-in: estimate the control quantile and tie weight from the control arm, then compute the treated exceedance share. Proposition 1 shows that it is identical when computed from pooled ranks. So it is invariant to any common strictly increasing transformation.
- **Asymptotics (Theorem 1).** A linear expansion has two terms. One is treated-arm sampling noise at the true threshold. The other is control-quantile uncertainty scaled by the local ROC slope r(α) = f₁/f₀. √n(R̂ − R) is asymptotically normal.
- **Variance.** The cross-term S_δδ is not identifiable, as both potential outcomes are never seen together. Following Neyman, it is dropped, giving a conservative bound. Its limit is R(1−R)/p + r²α(1−α)/(1−p).
- **Slope estimators.** A density-ratio version uses symmetric differences of the empirical survival functions with bandwidth bₙ = c_b/√n. A rank-based version differences the empirical ROC curve. The authors prefer the rank-based one: it needs only ranks and avoids density estimation.
- **Covariate adjustment.** Adjusting the outcomes directly could reorder units and change the ROC curve. Instead they adjust the estimator: R̂ − βᵀ(X̄₁ − X̄₀). The adjustment term has mean zero for any fixed β. The optimal β is a (1−pₙ, pₙ)-weighted average of regressions of the two linearization terms on X. Theorem 3: the adjusted variance is never larger than the unadjusted one, and the CIs are asymptotically no wider. With the rank-based slope, everything still depends only on ranks.
- **Simultaneous bands (Theorem 4, Algorithm 1).** A functional CLT holds on an interior interval [ε, 1−ε]. The conservative kernel has a "two-Brownian-bridge" form. Bands come from simulating Gaussian vectors on a grid and taking the (1−η) quantile of the max standardized deviation. If the diagonal lies inside the band, the uniform null of no distributional effect is not rejected. Covariate adjustment extends to the bands (details in the supplement).
- **Tail inference (Theorem 5).** For αₙ → 0, the √n-bandwidth slope estimators fail. The authors assume R is regularly varying at 0 with index γ. γ < 1 means a heavier treated upper tail; γ > 1 means a lighter one. They estimate γ̂ = [log R̂(αₙ) − log R̂(αₙ/2)]/log 2 and use the tail slope r̂ = γ̂R̂(αₙ)/αₙ. This is relatively consistent, including when n⁻¹ ≪ αₙ ≲ n⁻¹/². It is also rank-based. Pareto, Student-t and, by rank invariance, exponential families satisfy the conditions.

## 3. Impact — potential & realized

**Measured — simulations.** Finite populations of n ∈ {1,000, 2,000, 5,000, 10,000}, 2,000 randomizations each, pₙ ∈ {0.3, 0.5}. Outcomes are linear in two t₃ covariates plus t₃ noise, with θ = 1 and different covariate slopes per arm.
- **Pointwise 95% CIs** at α ∈ {0.05, 0.10, 0.25, 0.50, 0.75}: coverage is close to or above nominal in most settings (0.920–0.986 across cells). Adjustment cut average length by 18.2%–20.9%, e.g. 0.111 → 0.088 at n = 1,000, p = 0.3.
- **Simultaneous bands** on a grid of 0.05 to 0.95: pointwise intervals fall below 95% joint coverage at the five α values. The bands achieve conservative joint coverage. Adjustment shortened them by 15.5%–18.2%.
- **Tail CIs** (pₙ = 0.5, three αₙ regimes):
  - αₙ = n⁻¹/³: rank-based and tail slopes both cover validly (0.969–0.984).
  - αₙ = 1.5n⁻¹/²: the density-ratio slope undercovers (0.854–0.929). The rank-based and tail slopes stay at 0.951–0.989.
  - αₙ = 2n⁻²/³: the rank-based slope is undefined, as αₙ ≤ bₙ. The density-ratio slope undercovers (as low as 0.880). The tail slope covers at 0.971–0.996.

**Measured — Ecuador online-learning experiment** (Asanov et al. 2023, PNAS). The original study covers over 45,000 students in 1,151 high schools. This analysis uses Wave 2, lottery vs placebo. The stratified design is *approximated* as complete randomization. Samples: 5,897 students for a study-time index and 5,814 for a knowledge index. The index values have no natural scale, so only pooled ranks are kept. Covariates: baseline platform minutes, active days, and Spanish and English scores.
- **Study time:** R̂(α) − α = 0.026 at α = 0.05 (pointwise CI [0.010, 0.043]; simultaneous band [0.002, 0.051]). It is 0.028 at α = 0.10 (band [0.004, 0.051]). The bands include zero from α = 0.25 onward. The authors read this as lottery benefits being "more evident among students with higher study-time outcomes", beyond the mean effect the original study reported.
- **Tail:** CIs exclude zero at α = 0.05 and 0.03 (0.019, [0.005, 0.033]). At α = 0.01 they touch or include zero ([0.000, 0.015] unadjusted, [−0.001, 0.014] adjusted).
- **Knowledge:** all intervals and bands contain zero at every α.
- Covariate adjustment narrowed intervals only "slightly" here (e.g. a study-time α = 0.05 pointwise CI of [0.009, 0.042] vs [0.010, 0.043]).

**Limitations visible in the paper.** The fetched text has no separate discussion section. Conditions it states:
- Results cover complete randomization only. The application approximates a stratified design.
- Simultaneous bands cover only a fixed interior range [ε, 1−ε]. The extreme tail is handled pointwise.
- Tail inference relies on regular variation and on enough tail observations in both arms (nαₙ → ∞, nR(αₙ) → ∞).
- The Neyman variance is conservative by construction. Simulated coverage often sits at 0.97–0.98, above the 95% nominal level.
- The rank-based slope needs a bandwidth choice; simulations use bₙ = n⁻¹/².

**Potential.** One framework gives pointwise, curve-wide and tail answers to the question "do treated units beat the control's top-k%?". It works on rank-only or arbitrarily scaled outcomes, and it can use covariates without an outcome model.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A clean, rank-only toolkit for "share beating the control's top-k%", assembled from known pieces

The ingredients are familiar. The ROC curve is equivalent to a DTE at a control quantile. The variance is a Neyman-style conservative bound. The adjustment mirrors Lin-type regression adjustment, and the tail work borrows from extreme-value theory. The contribution is putting these together carefully in the finite-population, design-based setting. Two choices are smart. Adjusting the *estimator* rather than the outcomes keeps the estimand intact. The log-ratio tail slope keeps inference valid where bandwidth-based slopes break or fail to exist. The tail-slope result in Table 4 is the most practically useful finding. The evidence is one simulation design and one application, where adjustment helped only marginally.

For A/B testing in industry, this is my extrapolation; the paper studies an education experiment. Many product questions are really distributional. "Did the change grow the share of sessions above last control's p90 watch time?" "Did the share of sellers clearing the control's top-decile GMV move?" Teams answer these today with ad-hoc QTE bootstraps or by thresholding at a fixed value. The ROC framing gives a ready tail-share metric with a CLT. Because it uses only ranks, it is immune to log-vs-raw metric debates and robust to heavy tails. The no-larger-variance guarantee suggests CUPED-style covariates can be carried over. Caveats for that use: the theory assumes complete randomization with no interference, and an analyst scanning many α values must use the simultaneous band, not pointwise CIs.

### Similar / related work

- [**Long-Term Quantile Treatment Effects with Combined Experimental and Observational Data**](2026-11-18-arxiv-long-term-quantile-treatment-effects-combined-data.md) (in this bank) — also targets distributional effects with simultaneous bands, but through quantile effects on numerical outcomes in a superpopulation, double-machine-learning setting rather than rank-only design-based inference.
- [**Variance Reduction for Heavy-Tailed Monetization Metrics in Ranking Experiments via Post-Stratification**](2026-11-09-arxiv-post-stratification-cuped-heavy-tailed-monetization-sharechat.md) (in this bank) — tackles heavy-tailed A/B metrics by stratifying the mean estimate; a rank-based tail-share estimand like R(α) is an alternative way to ask about top spenders.
- [**Design-based theory for covariate adjustment in generalized pairwise comparisons**](https://arxiv.org/abs/2602.18383) — Chen & Li (2026). Design-based covariate adjustment for the Mann–Whitney/AUC-type scalar that this paper generalizes to the full curve.
- **Estimating distributional treatment effects in randomized experiments: machine learning for variance reduction** — Byambadalai, Oka & Yasui (ICML 2024). Covariate-adjusted DTEs at fixed numerical thresholds, the estimand the ROC curve maps onto at control quantiles.

### Jargon buster

- **Causal ROC curve** — for each α, the share of treated outcomes above the control group's top-α cutoff; the diagonal R(α) = α means no distributional difference.
- **Design-based inference** — treats each unit's potential outcomes as fixed and uses only the random treatment assignment as the source of uncertainty, with no outcome model.
- **Distributional treatment effect (DTE)** — the difference between arms in the probability of exceeding a fixed outcome value.
- **Neyman conservative variance** — drops a term that depends on unobservable joint potential outcomes, so the variance estimate (and CI) is too large rather than too small.
- **Local ROC slope** — the ratio of treated to control densities at the control quantile; it controls how error in estimating the cutoff spreads into the ROC estimate.
- **Simultaneous confidence band** — a band that covers the whole curve over a range of α with 95% joint probability, unlike pointwise intervals.
- **Regular variation / tail index γ** — R behaves like a power αᵞ near zero; γ below 1 means the treated arm has a heavier upper tail than control.
