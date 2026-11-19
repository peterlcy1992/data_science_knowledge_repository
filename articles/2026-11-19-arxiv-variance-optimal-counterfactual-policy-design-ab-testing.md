---
id: arxiv-variance-optimal-counterfactual-policy-design-ab-testing
title: "Variance-Optimal Counterfactual Policy Design for Sample-Efficient Online A/B Testing"
source: "Gupta (Microsoft) & Maji (DeepL) (arXiv cs.LG / cs.IR)"
url: "https://arxiv.org/abs/2611.24757"
published: "2026-11"
added: "2026-11-19"
category: experimentation-causal
tags: [ab-testing, variance-reduction, off-policy-evaluation, optimal-design, control-variates, logging-policy, policy-overlap, recsys-experiments]
novelty: 4
sourced_via: "full-text fetch"
---

# Variance-Optimal Counterfactual Policy Design for Sample-Efficient Online A/B Testing

**Source:** [Gupta (Microsoft) & Maji (DeepL) (arXiv cs.LG / cs.IR)](https://arxiv.org/abs/2611.24757) · Published 2026-11 · Added 2026-11-19
**Category:** Experimentation & Causal Inference · **Tags:** `ab-testing`, `variance-reduction`, `off-policy-evaluation`, `optimal-design`, `control-variates`, `logging-policy`, `policy-overlap`, `recsys-experiments`

## TL;DR

When an A/B test compares two stochastic ranking policies, actions both policies pick with similar probability add noise and carry no information about the difference. The authors derive a closed-form, variance-optimal action-level logging policy: sample each action in proportion to |π_t − π_p| times its residual reward uncertainty. They pair it with a control variate learned from historical logs. In simulations it matches balanced A/B's MSE with 39–51% of the traffic.

## 1. Business context

Teams shipping recommendation or ranking changes test them online, but incremental policy updates have small effects and heavily overlapping policies. A standard A/B test then needs a lot of traffic and time. The usual variance reducers (CUPED, regression adjustment, ML-based adjustment) improve the *estimator* after the randomization scheme is fixed. Recent overlap-aware designs (Jeunen, 2026) tune only a single traffic split between the two policies. The authors (work done outside their employers, Microsoft and DeepL) treat data collection itself as a design choice: which action to show, per context, so that each observation is as informative as possible about the treatment–production difference.

## 2. Technical details

- **Estimand and estimator.** The ATE is the difference in expected reward between a fixed treatment policy π_t and production policy π_p. Instead of first assigning a unit to an arm, each interaction samples its action from a separate **logging policy q**. The reward is weighted by (π_t − π_p)(a|x)/q(a|x), building on pairwise off-policy evaluation (Δ-IPS; Jeunen & Ustimenko, 2024). A **control variate** (baseline reward prediction) is subtracted inside the weight and added back in expectation, which keeps the estimator unbiased.
- **Key result (closed form).** For any fixed control variate m, the variance-minimizing logger is **q*(a|x) ∝ |π_t(a|x) − π_p(a|x)| · √s_m(x,a)**, where s_m is the residual second moment E[(Y − m)² | x,a]. It favours actions where the policies disagree and the leftover reward noise is high. Actions with equal probability under both policies get no traffic. With no overlap and a perfect control variate this recovers contextual Neyman allocation.
- **Partial minimization.** Because the optimal q is known in closed form for each m, only the control variate is optimized: a **scalar** baseline ("Scalar joint") or a **logistic model-based** one ("Model-CV"). The model is fit to minimize the ATE estimator's variance, not prediction loss, using Adam on historical logs.
- **Safety and validity.** A uniform backoff mixes q with ε/K exploration (ε = 0.05) to keep full support. A two-stage procedure (design on historical logs, then freeze) keeps the estimate unbiased even if the reward model is misspecified. Inference is a t-test conditional on the frozen design.
- **Simulation.** Gaussian contexts (D = 25), overlapping softmax policies, Bernoulli rewards, and a true ATE calibrated to about 0.005. K ∈ {25, 50, 75} actions, 10k or 30k historical interactions, and 1k–10k evaluation interactions, giving 60 settings × 500 replications. Baselines are Standard A/B (difference in means), Balanced A/B (pairwise IPS), Overlap-aware A/B (Jeunen 2026 policy mixture plus optimal scalar control variate) and Reward-aware A/B.

## 3. Impact — potential & realized

**Measured (simulation only):**
- **MSE.** Scalar joint and Model-CV beat all four baselines in every panel and at every evaluation size. Geometric-mean MSE ratio vs Balanced A/B: **0.49–0.53** (Scalar) and **0.39–0.51** (Model-CV). Since MSE scales with 1/n, Model-CV needs **39–51% of the traffic** for equal accuracy. Against the better policy mixture the ratios are 0.73–0.77 and 0.59–0.74, a 26–41% MSE reduction for Model-CV. Against Standard A/B, Model-CV cuts MSE by **81–88%**.
- **Power** at 10k observations: Balanced A/B reaches about 0.15–0.20 and the new designs 0.21–0.38. Model-CV has 1.5–2.1× Balanced A/B's power and 3.1–3.9× Standard A/B's. The authors note that absolute power stays below 0.40, so the experiments don't show that 10k observations would suffice for 80% power.
- **Wrong-sign selection** at 10k: Balanced A/B 0.15–0.23 vs Model-CV 0.05–0.13 (a 42–63% reduction).
- **Model vs scalar control variate.** Model-CV wins on MSE in 58 of 60 settings, power in 53 and selection error in 51. More historical data helps Model-CV (28 of 30) but barely Scalar joint (13 of 30).

**Potential and limits:** it applies wherever the platform can choose the action-sampling policy per request. The authors list repeated users, action restrictions, adaptive (online-updated) loggers and ranked lists, where it is unclear whether an action is a whole list or an item, as open extensions. There is no production test.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Moves variance reduction upstream, from the estimator into the design

This is the natural next step after policy-overlap A/B testing. Once you accept an off-policy estimator for an online test, the logger is yours to design, and the optimum has a clean, intuitive closed form. The practical upshot for experimentation teams is a recipe that stacks with CUPED-style thinking: fit a reward model on historical logs, solve for the control variate, freeze the logger, run.

My caveats: everything is synthetic with a tiny ATE and Bernoulli rewards. Showing users a mix that is neither the treatment nor the production policy is an operational and product-risk question the paper doesn't address. Slate-level ranking, where most real recsys tests live, is left open. Platforms already running Δ-OPE-style tests are best placed to try it.

### Similar / related work

- [**Accelerating A/B-Tests with Counterfactual Estimation: Reducing Variance through Policy Overlap**](2026-10-01-arxiv-policy-overlap-accelerating-ab-tests.md) (in this bank) — Jeunen (2026), the single-mixing-weight overlap design used as the main baseline here.
- [**Design-Driven Inference for Online Experiments**](2026-10-07-arxiv-design-driven-inference-online-experiments.md) (in this bank) — another argument for optimizing the experimental design, not just the analysis.
- **Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data (CUPED)** — Deng et al. (2013), the estimator-side variance reduction this complements.
- [**Doubly Robust Policy Evaluation and Learning**](https://arxiv.org/abs/1103.4601) — Dudík, Langford & Li (2011), the control-variate/DR foundation of the estimator.

### Jargon buster

- **Logging policy** — the probability distribution actually used to pick which action (item) a user sees during data collection.
- **Off-policy evaluation (IPS)** — estimating how a policy would perform using data collected by a different policy, by reweighting rewards by probability ratios.
- **Control variate** — a predicted baseline subtracted from each outcome (and corrected for in expectation) to cut variance without adding bias.
- **Neyman allocation** — assigning more samples to arms with noisier outcomes, in proportion to their standard deviation.
- **Partial minimization** — solving one block of variables in closed form so the optimization runs only over the rest.
