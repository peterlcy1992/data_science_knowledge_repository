---
id: arxiv-randomization-protects-average-chance-covariate-imbalance
title: "Randomization protects the average, not the trial: chance covariate imbalance and a calibration of balance P values at the design stage"
source: "UMass Lowell / Boston Children's Hospital (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.21425"
published: "2026-11"
added: "2026-11-17"
category: experimentation-causal
tags: [covariate-imbalance, conditional-bias, ancova, cuped, balance-tests, p-value-calibration, non-collapsibility, stratified-randomization, trial-design]
novelty: 3
sourced_via: "full-text fetch"
---

# Randomization protects the average, not the trial: chance covariate imbalance and a calibration of balance P values at the design stage

**Source:** [UMass Lowell / Boston Children's Hospital (arXiv stat.ME)](https://arxiv.org/abs/2611.21425) · Published 2026-11 · Added 2026-11-17
**Category:** Experimentation & Causal Inference · **Tags:** `covariate-imbalance`, `conditional-bias`, `ancova`, `cuped`, `balance-tests`, `p-value-calibration`, `non-collapsibility`, `stratified-randomization`, `trial-design`

## TL;DR

Randomization makes the unadjusted estimate unbiased over allocations, not in the trial you actually ran. Given the realized allocation, the bias in standard-error units is ρ·Z_bal — the covariate–outcome correlation times the balance z-statistic — so it does not shrink as trials grow. Pre-specified ANCOVA removes it, change scores reverse it, and the paper calibrates design-stage balance P values: any balance P ≥ 0.317 keeps the two-sided conditional type I error of the unadjusted test at or below 5% for every ρ.

## 1. Business context

Trial-design software simulates thousands of allocations under candidate schemes (complete randomization, permuted/stratified blocks, urn designs, minimization) and scores each by the distribution of baseline balance P values against a cut-off. Yet what such P values imply for bias and error rates is seldom stated, and the literature criticizing baseline significance tests (Senn; CONSORT 2025: "should not be reported") has rarely been linked to this design-stage use. The paper combines a targeted narrative review (reported against SANRA criteria) with derivations under a linear model with one normal prognostic covariate, checked by simulation. The setting is clinical trials, but the algebra is the same one behind CUPED and regression adjustment in online A/B tests.

## 2. Technical details

- **Conditional bias.** Under Y = μ + τT + βX + ε, E[τ̂ | A] = τ + βΔ_X. In outcome-SD units bias = ρd (ρ=0.5 and a 0.2-SD imbalance give 0.1 SD, half a conventional small effect); in SE units bias/SE = ρZ_bal, and Z_bal is standard normal at every n.
- **Analysis choice decides the sign.** Final-value analysis carries βΔ_X; change scores carry (β−1)Δ_X, opposite in sign when 0<β<1; ANCOVA removes it. In 20,000 simulated trials (100/arm, ρ=β=0.5) fitted slopes were 0.493, −0.507 and −0.006.
- **Binary outcomes.** Crude risk-difference bias = (π_H,T − π_H,C)(r_H − r_L): 10 points more high-risk patients with a 0.30 risk gap gives 3 points of bias.
- **Non-collapsibility is different.** In logistic/Cox models, omitting a prognostic covariate attenuates toward the null even under perfect balance (two balanced strata, control risks 0.10/0.60, conditional OR 8.0 → marginal OR 4.27); it estimates a different estimand rather than a biased one.
- **Calibrating balance P values.** Uses the Sellke–Bayarri–Berger bound B(P) = −eP ln P, which reaches 1 at P = 1/e — proposed as a worst-balance threshold. Under complete randomization the worst of *k* independent balance P values falls below 1/e with probability 1 − (1 − 1/e)^k (0.99 for k=10).

## 3. Impact — potential & realized

**Derived / reviewed:**
- Balance P ≥ 0.317 keeps two-sided conditional type I error ≤ 5% for every ρ; at P = 1/e the one-sided error in the favoured direction is at most 4.1%, versus 13–33% at P = 0.05.
- With 10 covariates tested at 0.05, the chance at least one is "significant" is 40% at any n.
- Reviewed evidence: adjusting for known prognostic covariates raised median power from 80% to 92.6% across 12 outcomes from 8 trials, with a worst loss of 1.5 points for a non-prognostic covariate; ignoring stratification factors made unadjusted SEs 2.3–17.4% too large (type I error 2.2–4.3%); only 26% of 258 trials in 2010 adjusted for all balancing factors. Case studies: MIST2 (adjustment cut the estimate 38%), NINDS rt-PA (a 2022 adjusted re-analysis removed significance for 3 of 7 results), MARS.

**Recommendations:** benchmark design-stage balance scores against complete randomization, weight them by external prognostic strength, and report them alongside allocation predictability and a pre-specified covariate-adjusted analysis plan. Post hoc adjustment chosen because of an observed imbalance is a sensitivity analysis, not a rescue.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A crisp, citable argument for pre-registered adjustment

Most of the algebra is classical (Senn made the "imbalance matters as much for large trials" point in 1989), and the authors are clear about which results are derived versus quoted. The new pieces are the design-stage calibration (0.317, 1/e) and the tidy ρ·Z_bal framing. For experimentation teams the takeaway is the one CUPED already implies: don't eyeball baseline balance tests; pre-specify adjustment on strongly prognostic covariates and treat "the groups look balanced" as uninformative about bias.

### Similar / related work

- [**Ensuring Trustworthy Online A/B Testing: Addressing Five Key Questions on CUPED**](2026-10-02-arxiv-cuped-five-questions-bytedance.md) (in this bank) — the online-experiment face of ANCOVA-style adjustment.
- [**Optimal Variance Reduction in Randomized Experiments**](2026-11-09-arxiv-optimal-variance-reduction-randomized-experiments-najmi-keselman.md) (in this bank) — efficiency theory for the adjustment this paper recommends.
- [**Rerandomization to improve covariate balance in experiments**](https://arxiv.org/abs/1207.5625) (Morgan & Rubin) — design-stage balance control quoted in the review.

### Jargon buster

- **Conditional bias** — the bias of an estimate given the particular allocation drawn, as opposed to averaged over all possible allocations.
- **ANCOVA** — regressing the outcome on treatment plus baseline covariates; in A/B testing, CUPED is a close relative.
- **Non-collapsibility** — odds and hazard ratios change when you add a prognostic covariate even if it's perfectly balanced, because conditional and marginal versions are different quantities.
- **Sellke–Bayarri–Berger bound** — a lower bound on the Bayes factor implied by a P value, used to translate P values into evidence.
