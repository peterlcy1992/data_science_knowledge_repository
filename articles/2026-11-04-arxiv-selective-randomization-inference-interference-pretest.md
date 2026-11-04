---
id: arxiv-selective-randomization-inference-interference-pretest
title: "Selective Randomization Inference for Interference"
source: "arXiv econ.EM (Takahide Yanagi, Kyoto University)"
url: "https://arxiv.org/abs/2611.02443"
published: "2026-11"
added: "2026-11-04"
category: experimentation-causal
tags: [interference, spillover, selective-inference, randomization-test, randomized-saturation-design, pretest]
novelty: 3
sourced_via: "full-text fetch"
---

# Selective Randomization Inference for Interference

**Source:** [arXiv econ.EM (Takahide Yanagi, Kyoto University)](https://arxiv.org/abs/2611.02443) · Published 2026-11 · Added 2026-11-04
**Category:** experimentation-causal · **Tags:** `interference`, `spillover`, `selective-inference`, `randomization-test`, `randomized-saturation-design`, `pretest`

## TL;DR

Teams often test for spillover first and then pick the analysis (spillover-aware or no-spillover) based on the result. That data-dependent choice can distort the later test. The paper builds a two-stage randomization-inference procedure for randomized saturation designs that conditions on the first-stage outcome and proves finite-sample control of the selective Type I error rate for each second-stage test.

## 1. Business context

Experiments in which one unit's treatment can affect others (cash transfers, school programs, marketplaces, social products) are usually analysed after a pretest or robustness check for interference. If the pretest rejects, researchers move to a model that allows spillover; if not, they study direct effects assuming no spillover. The paper's point is that this data-dependent selection of the model and hypothesis can compromise the validity of the subsequent inference unless it is accounted for, as the post-selection/selective-inference literature highlights.

## 2. Technical details

Setting: finite population of N units in C clusters, analysed under the randomized saturation design - clusters are first completely randomized to saturation labels (target treated proportions), then units within clusters are completely randomized conditional on the label. Stage 1 tests the null of no spillover with a conditional randomization test (CRT) that holds the assignments of a first-stage 'focal subpopulation' fixed so potential outcomes are imputable (the null is not sharp). If stage 1 rejects, stage 2 tests zero exposure contrast under a pre-specified exposure mapping (own treatment plus cluster saturation), assumed correctly specified; if it does not reject, stage 2 tests the sharp-style null of no direct effects assuming no spillover. Both stage-2 tests are selective randomization tests (SRTs): the reference distribution is restricted to counterfactual assignments that would reproduce the observed first-stage result. The key difficulty the paper addresses is reconstructing that first-stage result under the stage-2 null, which requires jointly choosing focal subpopulations and imputable assignment sets. P-values are computed by Monte Carlo over the restricted assignment set.

## 3. Impact — potential & realized

Realized (per the paper): proofs that the first-stage CRT controls conditional Type I error and each second-stage SRT controls selective Type I error in finite samples. Monte Carlo (40 clusters of 3 units, saturation labels 1/3 and 2/3, 10,000 replications per configuration) reports empirical Type I error close to nominal levels and adequate power. Empirical illustration: a subset of the Baird et al. (2011) Malawi cash-transfer experiment (18 enumeration areas, 334 baseline schoolgirls, 155 offered transfers); the first-stage test did not reject no-spillover at the 10% level for any of four outcomes (e.g. p = 0.110 for currently enrolled), so direct effects were then tested conditional on that non-rejection. Potential: a template for valid inference after interference pretests in cluster-randomized product and policy experiments; the paper itself focuses on randomized saturation designs and says extensions to other designs are possible.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Valid inference after an interference pretest - sound but narrow

A careful methods paper on a real but narrow workflow problem: pretest-then-analyse for interference. The result is finite-sample validity, not a power or efficiency gain, and the experimental design is restricted to randomized saturation. Simulations are small (cluster size 3) and the empirical example is a restricted subset; useful mainly to methodologists running cluster experiments with possible spillover.

### Similar / related work

- Selective randomization inference for adaptive experiments (Freidling et al., 2026) and Gao (2025) on data-dependent subgroups - the selective-randomization line this paper extends; not in this bank
- [The Double Diagonal Estimator: Reducing Bias in Two-Sided Marketplace Experiments](2026-11-03-arxiv-double-diagonal-estimator-two-sided-marketplace-experiments.md) (in this bank) - another interference-aware experiment analysis, but an estimator rather than a test
- Basse, Feller & Toulis (2019) - conditional randomization tests for interference in two-stage designs; cited by the paper as prior CRT work

### Jargon buster

- **Interference / spillover** — One unit's treatment affects another unit's outcome, breaking the usual no-interference assumption.
- **Randomized saturation design** — Two-stage design: randomize clusters to a treated share, then randomize units within clusters to match.
- **Selective inference** — Inference that accounts for the fact that the hypothesis or model was chosen using the same data.
- **Conditional randomization test** — A randomization test whose reference distribution is restricted to assignments that keep part of the data fixed so the null becomes testable.
