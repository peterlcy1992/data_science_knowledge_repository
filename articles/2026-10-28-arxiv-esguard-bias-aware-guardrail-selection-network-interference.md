---
id: arxiv-esguard-bias-aware-guardrail-selection-network-interference
title: "Bias-Aware Guardrail Selection Under Network Interference"
source: "arXiv stat.ME (Kim, Byun & Jang, Yonsei University)"
url: "https://arxiv.org/abs/2610.36702"
published: "2026-10"
added: "2026-10-28"
category: experimentation-causal
tags: [network-interference, guardrail-metrics, safe-policy-selection, marketplace-experiments, bias-aware-inference, switchback]
novelty: 4
sourced_via: "full-text fetch"
---

# Bias-Aware Guardrail Selection Under Network Interference

**Source:** [arXiv stat.ME (Kim, Byun & Jang, Yonsei University)](https://arxiv.org/abs/2610.36702) · Published 2026-10 · Added 2026-10-28
**Category:** experimentation-causal · **Tags:** `network-interference`, `guardrail-metrics`, `safe-policy-selection`, `marketplace-experiments`, `bias-aware-inference`, `switchback`

## TL;DR

ESGuard picks a budget-feasible treatment allocation from randomized experiment logs while bounding the probability of violating a guardrail for a designated group, under network interference. Pooling nearby exposures to estimate sparsely observed treatment-exposure pairs adds allocation-specific bias, so ESGuard adds an explicit bias bound to simultaneous lower confidence bounds. On a NYC ride-hailing simulator it cuts guardrail violations from 16% (point-estimate rule) to 0.06% of selections, at the cost of abstaining in about a quarter of replications.

## 1. Business context

A ride-hailing platform with a limited budget decides which zones get driver incentives. Incentives pull drivers from neighbouring zones, so the allocation that maximises total trips can reduce service where riders wait longest; the platform sets a guardrail limiting that loss for a designated group to a stated tolerance. The same decision appears when marketplaces promote connected sellers or social platforms roll features out by region. The experiment log rarely records the exact treatment-exposure pair a candidate allocation would induce: with six months of simulated rounds, exact-exposure estimates exist for only 17-19% of candidates.

## 2. Technical details

Setting: repeated randomized rounds (time slots, as in switchback experiments) with treatment randomized independently over units of a fixed graph, and an exposure mapping in which a unit's outcome depends on its own treatment and the treated share of its neighbours. Existing safe-policy-selection methods (high-confidence policy improvement, Learn then Test, CSPI-MT) need valid inference per candidate; a variance-only band around pooled estimates ignores the bias from pooling. ESGuard (exposure-stratified guardrail selection): a training half generates candidate allocations (including partial ones that leave budget unspent); on held-out calibration rounds it merges rare exposures into neighbouring bins and fits local lines, each fitted value being a weighted sum of outcomes, which yields a closed-form bias bound under curvature and slope bounds (following Armstrong and Kolesar's bias-aware inference). Unit-level bounds are aggregated over each candidate's guardrail contrasts and subtracted when forming simultaneous lower confidence bounds; a candidate passes if its lower bound is at least minus the tolerance, the passing candidate with the highest positive held-out gain is selected, otherwise the status quo is retained. Guarantees: under randomized rounds, a correct exposure mapping and valid curvature/slope bounds fixed before calibration, the conditional bias bound holds in finite samples; with independent rounds and further regularity conditions, the unconditional probability of selecting an unsafe allocation is asymptotically at most the target level.

## 3. Impact — potential & realized

Realized (simulation only): a simulator built from 3.1 million NYC ride-hailing trips with known guardrails and spillover losses affecting either all zones or only underserved zones. Every smoothing or coarsening estimator tested falls below nominal 95% simultaneous coverage without the bias bound and reaches at least 95% with it. In the underserved-only scenario ESGuard violates the guardrail in 0.06% of its selections (2 of 3,571) versus 16% for the point-estimate rule under the same gain ranking, and abstains in about a quarter of replications; no violations in the all-zone scenario. The paper states that omitted spillovers can invalidate the protection. Not evaluated on a live platform. Potential: a template for making guardrail decisions in marketplaces where interference makes the needed counterfactuals sparsely observed.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Guardrail metrics are usually treated as just another metric with a non-inferiority test; this paper shows that under interference the real threat is smoothing bias that variance-only intervals hide, and gives a way to price it in.

Guardrail metrics are usually treated as just another metric with a non-inferiority test; this paper shows that under interference the real threat is smoothing bias that variance-only intervals hide, and gives a way to price it in. The honest cost is abstention (about a quarter of runs) and dependence on user-supplied curvature/slope bounds and a correct exposure mapping, which are exactly the things practitioners find hard to justify. Simulation-only evidence from one data-derived simulator.

### Similar / related work

- [**A Bayesian machine learning approach to direct and spillover effects in cluster-randomized trials with noncompliance**](2026-10-21-arxiv-bayesian-bart-spillover-cluster-trials-noncompliance.md) (in this bank) — another interference-aware experimentation design
- [**Conformal Policy Selection: When to Deploy AI Decisions for Targeted Intervention**](2026-10-19-arxiv-conformal-policy-selection-fdr-deployment.md) (in this bank) — safe selection of policies for deployment with error-rate control

### Jargon buster

- **Network interference** — One unit's outcome depends on other units' treatment, violating the no-spillover assumption behind standard A/B analysis.
- **Exposure mapping** — A rule summarising how much treatment a unit is exposed to through its neighbours, e.g. the treated share of neighbours.
- **Guardrail** — A metric that must not degrade beyond a tolerance for a launch to be acceptable.
- **Simultaneous lower confidence bound** — A bound valid jointly across many candidates so that picking the best one does not inflate error.
