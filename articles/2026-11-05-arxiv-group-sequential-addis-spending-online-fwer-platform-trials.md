---
id: arxiv-group-sequential-addis-spending-online-fwer-platform-trials
title: "Online Control of the Family-wise Error Rate (FWER) for Multi-stage Platform Trials"
source: "arXiv stat.ME (Yao, Robertson, Jaki; Regensburg / Cambridge MRC BSU)"
url: "https://arxiv.org/abs/2611.06530"
published: "2026-11"
added: "2026-11-05"
category: experimentation-causal
tags: [online-multiple-testing, fwer, alpha-spending, platform-trials, group-sequential, addis]
novelty: 3
sourced_via: "full-text fetch"
---

# Online Control of the Family-wise Error Rate (FWER) for Multi-stage Platform Trials

**Source:** [arXiv stat.ME (Yao, Robertson, Jaki; Regensburg / Cambridge MRC BSU)](https://arxiv.org/abs/2611.06530) · Published 2026-11 · Added 2026-11-05
**Category:** experimentation-causal · **Tags:** `online-multiple-testing`, `fwer`, `alpha-spending`, `platform-trials`, `group-sequential`, `addis`

## TL;DR

Platform trials add and drop arms over time, so the number of hypotheses is unknown at the start and standard multiplicity corrections do not fit. The paper extends ADDIS-Spending, an online FWER-controlling procedure, with interim analyses (group sequential ADDIS-Spending), updating each hypothesis's alpha at every interim as other decisions are made. Simulations show FWER control and power gains in some regimes; validity is proven only under independence.

## 1. Business context

Platform, basket and umbrella trials (master protocols) test several interventions against shared controls and let arms enter at any time. That flexibility raises multiplicity: the total number of arms is not known when the trial starts. FWER (probability of one or more false rejections) is usually the confirmatory standard, and the authors cite arguments that FDR control does not comply with regulatory policy. The same always-on, hypotheses-arrive-over-time structure shows up in continuously running experimentation programs, although this paper is written for clinical trials.

## 2. Technical details

Base: ADDIS-Spending (Tian and Ramdas) for online FWER control, where each hypothesis gets alpha_i = alpha*gamma_i from a non-negative sequence summing to at most 1, with adaptive discarding of hypotheses that look uninformative. The new group sequential ADDIS-Spending lets each hypothesis have interim analyses with early stopping for efficacy or futility and updates error levels of individual hypotheses at all interim analyses whenever formal decisions on other hypotheses are made. Contrast: Greenstreet et al. control FWER in a pre-planned multi-stage platform trial requiring the number of arms to be pre-specified; the conditional error approach of Burnett et al. allows adding arms later but forces decisions at the final time point. Simulation design: continuous endpoint, one-sided tests, normal outcomes with unit variance, equal allocation, concurrent control data only, Z-statistics per stage; half-overlapping arms (each shares control data with its neighbours) plus a completely overlapping case; no, 2- and 3-stage designs; proportion of non-null arms pi1 in {0, 0.1, 0.2, 0.4}; n=60 per arm and effect size 0.53 (90% power in a single comparison); O'Brien-Fleming and triangular boundaries; compared with group-sequential Bonferroni.

## 3. Impact — potential & realized

Realized (as reported): simulations show valid FWER control and power gains at comparable sample size. Performance depends on trial characteristics: the proposal does better when the proportion of non-null hypotheses is high and the maximum number of allowed hypotheses is large, whereas GS-Bonferroni may be superior otherwise (and has higher power at low-to-moderate pi1 when the maximum number of hypotheses equals the actual number, at the cost of flexibility to add arms later). Power was stable with respect to the maximum number of arms, and the loss of power in three-stage designs was minimal. Interim analyses can substantially lower sample size. Caveat from the authors: FWER validity is proven only under independence; with a shared control arm, inflation can appear under extreme settings of the thresholds tau and lambda (Appendix C). Ordering of hypotheses entering the platform and dependence structure are left for future work.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Useful extension for always-on testing; clinical-trial framing and an independence assumption limit direct reuse

A careful, incremental statistics paper: combine two known ideas (online alpha-spending with discarding, group-sequential boundaries). Of interest to experimentation-platform teams as a worked example of FWER control when hypotheses arrive without a known total, but the shared-control dependence caveat is exactly what many product experiment programs have too.

### Similar / related work

- **Online error rate control for platform trials (Robertson et al., 2023)** — earlier online-testing treatment of platform trials without multiple stages; cited in the paper
- **Online control of the familywise error rate (Tian and Ramdas, 2021)** — the ADDIS-Spending procedure this paper extends

### Jargon buster

- **FWER** — Family-wise error rate: the chance of making at least one false rejection among all tests.
- **Alpha-spending** — Dividing a total Type I error budget across hypotheses or looks.
- **Platform trial** — A trial that tests multiple interventions against shared controls and lets arms be added or dropped over time.
- **Group sequential design** — A design with planned interim analyses that permit early stopping.
