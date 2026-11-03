---
id: arxiv-double-diagonal-estimator-two-sided-marketplace-experiments
title: "The Double Diagonal Estimator: Reducing Bias in Two-Sided Marketplace Experiments"
source: "arXiv econ.EM (Chawla & Syrgkanis, Stanford)"
url: "https://arxiv.org/abs/2610.41294"
published: "2026-10"
added: "2026-11-03"
category: experimentation-causal
tags: [marketplace-experiments, interference, two-sided-randomization, mean-field, bias, a-b-testing]
novelty: 4
sourced_via: "full-text fetch"
---

# The Double Diagonal Estimator: Reducing Bias in Two-Sided Marketplace Experiments

**Source:** [arXiv econ.EM (Chawla & Syrgkanis, Stanford)](https://arxiv.org/abs/2610.41294) · Published 2026-10 · Added 2026-11-03
**Category:** experimentation-causal · **Tags:** `marketplace-experiments`, `interference`, `two-sided-randomization`, `mean-field`, `bias`, `a-b-testing`

## TL;DR

In two-sided marketplace A/B tests, treated listings can steal bookings from control listings, so naive estimates are biased. Building on two-sided randomization (TSR), the paper proposes the Double Diagonal (DD) estimator, which contrasts treated-treated and control-control customer/listing pairs and uses the off-diagonal pairs to correct for interference. In a mean-field market model it proves DD has smaller bias than the standard naive TSR estimator whenever the outside option is at most about twice as attractive as platform options, and the two err in opposite directions.

## 1. Business context

Platforms such as lodging marketplaces, freelancing sites and ride-hailing routinely A/B test interventions that change how buyers and sellers interact. Because listings are depletable inventory, a more attractive treated listing can "steal" bookings from control listings and inflate the apparent effect; the paper cites prior work reporting naive bias of a factor of two or more (Blake & Coey). Earlier mean-field work (Johari et al., 2021) showed customer-side randomization is unbiased only in highly demand-constrained markets and listing-side randomization only in highly supply-constrained ones, and introduced two-sided randomization (TSR) with a naive estimator (TSRN). The open question the paper takes up is which TSR estimator to prefer in the balanced markets common in practice.

## 2. Technical details

The paper adopts the Johari et al. mean-field market: customer types choose among available listings with choice probability proportional to a matching propensity times available listing mass, with an outside-option parameter for not booking; listings are depleted when booked and return at a turnover rate. Under TSR, customers and listings are independently randomized, giving four cohorts (treated/control customer × treated/control listing) with observable booking rates Q00, Q01, Q10, Q11. The Double Diagonal estimator is a specific linear combination of these four cohort-level rates. Its motivation is an asymmetry: listings are depletable inventory while customers are a flow, so the global treatment effect can be written as the difference in steady-state availability of control vs treated listings; DD approximates that availability difference (each rescaled by its population share) under the experimental dynamics. Theory is given for a simplified homogeneous market in the small-treatment-effect regime: DD underestimates and TSRN overestimates the true effect, and a unique threshold a*(αL) exists below which |Bias_DD| < |Bias_TSRN|; at listing-treatment share αL = 1/2, a* ≈ 2.34. Numerics span 40 simulated scenarios (heterogeneous treatment effects, supply-demand imbalance, varied market structures) comparing DD, TSRN, customer-side (CR) and listing-side (LR) randomization, and two interpolating TSR estimators (TSRI1, TSRI2). The DD estimator can be expressed in the Multiple Randomization Design framework of Masoero et al. (2026), so its finite-sample inference tools could in principle apply.

## 3. Impact — potential & realized

Realized (per the paper, simulation only, no field experiment): DD had the lowest absolute bias in 35 of 40 scenarios (TSRI2 in the other 5). Median relative bias was 20.5% for DD versus 117.1% for TSRN, 140.7% for CR, 151.2% for LR, 105.0% for TSRI1 and 63.6% for TSRI2; 90th-percentile relative bias was 87.1% for DD versus 794.4% for TSRN. DD was within 25% relative bias in 28 of 40 scenarios and above 100% in 3 of 40, whereas TSRN was above 100% in 32 of 40. DD was not uniformly best: with opposing treatment effects it showed 44.5% bias versus 34.5% for TSRN, and when outside options dominate it underestimated by 42.3% versus 22% overestimation for TSRN. Stated limitations: theory covers a homogeneous market with parameter restrictions; the analysis is about bias and ignores variance (so it is most relevant in large-sample regimes); and the model assumes the intervention affects matching propensities only, not arrival rates or occupancy times. Potential: a drop-in estimator for existing TSR designs that needs no change to the experiment.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A narrow, well-posed estimator question: given TSR is already running, which linear combination of the four cohort rates is least biased? The opposite-signed bias of DD and TSRN is a practical bonus, since the two bracket the truth in the regime covered.

A narrow, well-posed estimator question: given TSR is already running, which linear combination of the four cohort rates is least biased? The opposite-signed bias of DD and TSRN is a practical bonus, since the two bracket the truth in the regime covered. The evidence is a mean-field model plus simulation inside the same model family, with no variance analysis or real platform data, so treat the 35/40 headline as a property of the simulator. Marketplace experimentation teams already running two-sided designs are the natural adopters.

### Similar / related work

- The Double Diagonal builds on Johari, Li, Liskovich & Weintraub (2021/2024), the mean-field two-sided randomization framework — not an in-bank article
- [**Using Marketplace Marginal Values to Address Interference Bias**](2026-09-11-lyft-marketplace-marginal-values-interference-bias.md) (in this bank) — a different, shadow-price-style interference correction
- [**Bias-Aware Guardrail Selection Under Network Interference**](2026-10-28-arxiv-esguard-bias-aware-guardrail-selection-network-interference.md) (in this bank) — interference bias in experiment decisions on networks
- [**Randomization Inference in Two-Sided Market Experiments**](https://arxiv.org/abs/2504.06215) — inference for spillovers on two-sided platforms

### Jargon buster

- **Interference (SUTVA violation)** — One unit's treatment changes another unit's outcome, so the control group is not a clean counterfactual.
- **Two-sided randomization (TSR)** — Independently randomizing both customers and listings to treatment/control, giving four customer×listing cohorts.
- **Mean-field model** — A large-market approximation where individual randomness is averaged out and the market is described by steady-state fractions.
- **Outside option** — The value to a customer of not booking anything on the platform.
