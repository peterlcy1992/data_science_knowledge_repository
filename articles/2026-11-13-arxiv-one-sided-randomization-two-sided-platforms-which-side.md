---
id: arxiv-one-sided-randomization-two-sided-platforms-which-side
title: "One-Sided Randomization in Two-Sided Platform Experiments: Which Side Should be Randomized?"
source: "arXiv stat.ME (Ramesh Johari & Anushka Murthy)"
url: "https://arxiv.org/abs/2611.16406"
published: "2026-11"
added: "2026-11-13"
category: experimentation-causal
tags: [marketplace-experiments, interference, two-sided-platforms, randomization-unit, bias-variance, difference-in-means, logit-choice]
novelty: 4
sourced_via: "full-text fetch"
---

# One-Sided Randomization in Two-Sided Platform Experiments: Which Side Should be Randomized?

**Source:** [arXiv stat.ME (Ramesh Johari & Anushka Murthy)](https://arxiv.org/abs/2611.16406) · Published 2026-11 · Added 2026-11-13
**Category:** experimentation-causal · **Tags:** `marketplace-experiments`, `interference`, `two-sided-platforms`, `randomization-unit`, `bias-variance`, `difference-in-means`, `logit-choice`

## TL;DR

Marketplace teams often believe that randomizing the larger side (e.g. listings when there are many more listings than customers) buys lower variance at the cost of more interference bias. In a first-come, first-served booking model with heterogeneous preferences, the authors prove there is no such trade-off asymptotically: randomizing the **short** (smaller) side eliminates first-order interference bias while long-side randomization can keep it, and short-side randomization's variance is of no larger order — because the number of matches is capped by the short side.

## 1. Business context

Two-sided platforms A/B test features such as listing designs or search algorithms, aiming to estimate the global average treatment effect (GATE) on the number of matches — global treatment vs global control. The usual practice is Bernoulli randomization of one side (customers or listings) plus a difference-in-means (DM) estimator, which is biased by interference because treated and control units compete for the same counterparties. Prior work (Johari, Li, Liskovich & Weintraub, 2022) showed in a Markovian queueing model that randomizing the short side reduces bias; the common counter-argument is that the long side gives a larger sample and hence less variance. Practical guidance has been unclear.

## 2. Technical details

**Model.** Customers arrive sequentially and book at most one unit-capacity listing, choosing the highest-utility acceptable listing still available (FCFS; bookings are final within a "matching cycle"). Preferences are one-sided (listings accept any booking), can be heterogeneous and correlated through customer- and listing-level random primitives, and the treatment can change which listings are acceptable and how they are ranked. The framework accommodates, but does not require, the consideration-set logit model of Johari et al. (2022). Two designs: customer randomization (a treated customer sees all listings under treatment) and listing randomization (a customer may compare treated and control listings). The DM estimator is rescaled by the randomized side's market share so both designs target the same GATE.

**Asymptotic regime.** Both sides grow but the short side's share s_n → 0; since matches ≤ short-side size, |GATE| ≤ s_n, so bias is judged relative to s_n and variance relative to s_n/n.

**Bias results.**
- *Near saturation* (Prop. 3.1): if almost all short-side participants match under global treatment, global control and short-side randomization, short-side bias is o(s_n). This arises naturally when listings are scarce; Prop. 3.2 gives a sufficient condition (each listing is enough customers' first choice) with an exponentially small unmatched fraction.
- *Bounded concentration* (Assumption 3.3, Prop. 3.4): when customers are scarce and no listing attracts a disproportionate share of their first choices, short-side bias is O(m_n²/(nℓ_n)) = O(s_n²) plus an exponentially small term.
- *Long side* (eq. 15): long-side DM bias includes a term for how treatment **redistributes** matches between treated and control units, which need not match its effect on total matches — so it can be Θ(s_n).
- *Logit example* (Prop. 3.5): under bounded consideration probabilities, utility weights and outside-option weight, short-side randomization has o(s_n) bias in both scarcity cases; with a sign-consistency condition (treatment raises every pair's attractiveness by at least γ), long-side randomization keeps strictly positive first-order bias.

**Variance results.** Prop. 4.1: under the general FCFS model, either design has Var = O(m_n/n²) = O(s_n/n), because changing one participant's primitives changes at most two customers' and two listings' match status. Theorem 4.4: under extra conditions — scarce customers who don't concentrate choices and enough demand for both arms (Assumption 4.2), or scarce listings where treatment changes any booking probability by at most a constant factor and a constant fraction of listings book (Assumption 4.3) — long-side variance is Θ(s_n/n). So Var(short) = O(Var(long)). Corollary 4.5 verifies these conditions under the logit model.

## 3. Impact — potential & realized

**Realized.** Theoretical: no simulations or platform data are reported. The conclusion is that, under conditions the authors call relatively mild and likely satisfied by most real platforms (ruling out highly concentrated preferences and nearly deterministic allocation of matches between arms), short-side randomization has lower-order bias and no worse variance rate.

**Potential.** A default for marketplace experimentation: randomize the scarce side. The authors flag practical methods for choosing the side from observable market characteristics as future work.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Removes the "long side = more power" argument with a clean mechanism: matches, not participants, are the effective sample.

The punchline is intuitive once stated: if only m customers can ever book, randomizing a million listings doesn't give you a million informative outcomes — most listings never match. That reframing is useful well beyond this model (any capacity-limited outcome). The results are rates, not constants, so in a moderately imbalanced market you'd still want a simulation or a meta-experiment to size the gain; and the outcome is match count only, not revenue or match quality. Also note the model has one-sided preferences and FCFS allocation — closer to lodging/e-commerce inventory than to ride-hailing dispatch.

### Similar / related work

- [**The Double Diagonal Estimator: Reducing Bias in Two-Sided Marketplace Experiments**](2026-11-03-arxiv-double-diagonal-estimator-two-sided-marketplace-experiments.md) — in this bank: cited by the authors; a two-sided-randomization alternative to choosing one side
- [**Using Marketplace Marginal Values to Address Interference Bias**](2026-09-11-lyft-marketplace-marginal-values-interference-bias.md) — in this bank: Lyft's shadow-price approach to the same interference bias
- [**Choosing Online Experiment Designs under Interference in Ads, Recommendations, and Member-Experience Systems**](2026-10-13-arxiv-experiment-design-under-interference-robust-selector.md) — in this bank: design selection under interference from a practitioner angle
- [**When does interference matter? Decision-making in platform experiments (Johari, Li, Murthy & Weintraub)**](https://arxiv.org/abs/2410.06580) — cited predecessor on how interference bias affects launch decisions

### Jargon buster

- **Short side / long side** — The side of the market with fewer / more participants (e.g. listings vs customers).
- **GATE** — Global average treatment effect: outcome if everyone were treated minus outcome if no one were.
- **Interference bias** — Bias when one unit's treatment changes another's outcome, e.g. treated customers booking listings control customers would have booked.
- **FCFS booking** — First-come, first-served: each arriving customer takes their best available option, removing it for later arrivals.
- **o(s_n) vs Θ(s_n)** — Asymptotic notation: bias that becomes negligible relative to the effect size vs bias of the same order as the effect.
