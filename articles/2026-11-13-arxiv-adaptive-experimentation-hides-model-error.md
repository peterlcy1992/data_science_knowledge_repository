---
id: arxiv-adaptive-experimentation-hides-model-error
title: "Adaptive Experimentation Can Hide Model Error: Detection Limits and Falsification Budgets"
source: "arXiv stat.ME (Ramnarayan Choudhary, MBZUAI)"
url: "https://arxiv.org/abs/2611.07529"
published: "2026-11"
added: "2026-11-13"
category: experimentation-causal
tags: [adaptive-design, expected-information-gain, model-misspecification, falsification, e-values, anytime-valid, llm-experimenters]
novelty: 3
sourced_via: "full-text fetch"
---

# Adaptive Experimentation Can Hide Model Error: Detection Limits and Falsification Budgets

**Source:** [arXiv stat.ME (Ramnarayan Choudhary, MBZUAI)](https://arxiv.org/abs/2611.07529) · Published 2026-11 · Added 2026-11-13
**Category:** experimentation-causal · **Tags:** `adaptive-design`, `expected-information-gain`, `model-misspecification`, `falsification`, `e-values`, `anytime-valid`, `llm-experimenters`

## TL;DR

An experiment can pin down a working model's parameters precisely while saying almost nothing about whether the model is wrong — and expected-information-gain (EIG) adaptive design can make that worse by repeatedly sampling settings where the wrong model fits. The paper bounds the power of *any* valid model-adequacy test by the experimenter's own sampling distribution, separates information never collected from information lost by a weak detector, and proposes reserving part of the design budget for falsification. It reports its empirical results as openly mixed.

## 1. Business context

Adaptive designs (Bayesian optimization, EIG-driven sampling, bandits, and increasingly LLM "agent" experimenters) are used to learn efficiently. The paper's simple example: a straight-line model interpolates two endpoints, the truth has an interior bump, and an experimenter who only samples the endpoints can never detect the error however much data it collects. The same logic applies to any adaptive allocation that concentrates traffic where the working model already looks good.

## 2. Technical details

**Own-design power ceiling (Theorem 1).** For any valid adequacy test at level α and any policy, rejection probability ≤ kl⁻¹_α{T·D(ν_T)}, where D(ν) = inf_θ Σ_a ν(a)·KL(P(·|a) ‖ p_θ(·|a)) is the best-case discrepancy between truth and working model *on the settings the policy actually visits*. If some null member matches the truth on every visited setting, power is at most α at every horizon. A two-setting Bernoulli example shows detection can require *combining* settings, each of which is individually matched by some null parameter.

**Detector.** Universal-inference e-process E_t = Q_t / sup_θ L_θ,t (anytime-valid via Ville's inequality). log E_t splits into realized truth-vs-null signal minus *numerator regret* — so a poor alternative model can waste signal that good acquisition collected, while a perfect numerator can't reveal error absent from the data.

**Diagnostic.** Relative to a declared model expansion, B_t = U_t + D_t: disagreement among represented alternatives plus their average disagreement with the working model. It is a certificate relative to declared alternatives, not a universal adequacy check (a wrong singleton expansion gives B_t = 0).

**Falsification budget (Algorithm 1).** Before rejection, take an expected-discrepancy-maximizing action when B_t ≥ b or a predictable coin with probability 0.5/√(t+1) succeeds; otherwise follow the base designer. The frozen gate b = 0.1 was later revised to log(1/α)/T, declared as a secondary arm.

## 3. Impact — potential & realized

**Realized (as the paper reports, including failures).**
- In several settings greedy EIG rarely detects a planted error while targeted discrimination recovers substantial detection.
- The independently specified primary study fails detection eligibility; a later numerator diagnostic fails its improvement criteria; the frozen rule fails on fresh continuous-null panels at longer horizons.
- Revised rule: detects 35.8% of misspecified campaigns vs 31.7% for a class-separation control at T = 240, with no resolved advantage at T = 480.
- Corrected 289-unit measured drug-combination replay (127 low-p units): revised rule 14.16% vs random 3.42%, class-discrimination EIG 17.37%, separation 16.02% — better than random (+10.74 pts), worse than class EIG (−3.21 pts).
- LLM experimenters: selected frontier-model pilots concentrate their designs and detect much less often than random sampling (the paper reports two providers' frontier reasoning models catching the error in 6–9% of campaigns), but campaigns are few and selected. A harness that reserves actions for falsification raised detection to ~79–81% in small pilots; wrapping plain greedy and random designers on the same worlds gave 76.3% and 76.9% (vs 0.1% and 57.3% unwrapped).

**Potential.** The paper's stated support is narrow: separate parameter learning, model checking and detector performance as distinct endpoints. It explicitly does not claim a universally superior design policy.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — The ceiling theorem is a sharp, portable warning; the intervention's evidence is (by the author's own account) mixed.

The transferable point for experimentation teams is Theorem 1's intuition: you can't falsify a model on data you never collect, so any adaptive allocator that maximizes learning *within* a model needs a reserved exploration budget for checking the model itself. That applies to bandit-driven traffic allocation and to AI agents running analyses. The write-up is unusually candid about registered failures and revisions, which is commendable but makes the practical recipe hard to extract; I'd take the principle, not the specific gate constant.

### Similar / related work

- [**Anytime-Valid Inference in Linear Models with Clustered Outcomes: Exact Multivariate Tests and Cluster-Robust Confidence Sequences**](2026-10-20-arxiv-anytime-valid-clustered-linear-models.md) — in this bank: anytime-valid inference, the validity layer used by the detector here
- [**From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?**](2026-10-22-arxiv-prompts-to-posteriors-llm-bayesian-inference.md) — in this bank: another look at LLMs as statistical reasoners
- **Box & Draper (1959) and the design-for-inadequacy literature** — classic work on designing experiments that can reveal a wrong model, which the paper builds on

### Jargon buster

- **Expected information gain (EIG)** — How much a candidate measurement is expected to reduce uncertainty about model parameters.
- **Model misspecification** — The true data-generating process is outside the model family being fit.
- **Universal inference** — A way to build valid tests from a likelihood ratio with a data-split or predictive numerator, without regularity conditions.
- **e-process** — A running evidence measure that can be monitored continuously while keeping false-rejection control.
- **Falsification budget** — Measurements reserved for checking whether the model is wrong rather than refining its parameters.
