---
id: arxiv-trial-level-surrogacy-ship-on-evals-alone
title: "When Can You Ship on Evals Alone? Trial-Level Surrogacy for Offline Evaluation of LLM Systems"
source: "arXiv stat.ME (Mårten Schultzberg, Spotify)"
url: "https://arxiv.org/abs/2610.10142"
published: "2026-10"
added: "2026-11-02"
category: experimentation-causal
tags: [surrogacy, llm-evals, a-b-testing, measurement-error, ship-decision, llm-as-judge]
novelty: 4
sourced_via: "full-text fetch"
---

# When Can You Ship on Evals Alone? Trial-Level Surrogacy for Offline Evaluation of LLM Systems

**Source:** [arXiv stat.ME (Mårten Schultzberg, Spotify)](https://arxiv.org/abs/2610.10142) · Published 2026-10 · Added 2026-11-02
**Category:** experimentation-causal · **Tags:** `surrogacy`, `llm-evals`, `a-b-testing`, `measurement-error`, `ship-decision`, `llm-as-judge`

## TL;DR

Agreement between an offline eval and human judgment does not tell a team which LLM-product changes can ship without an A/B test; that needs trial-level surrogacy, i.e. eval treatment effects predicting online treatment effects across a class of comparable interventions. The paper derives a noise-corrected estimate from launch logs and a closed-form ship/test/kill rule; on 183 Upworthy headline interventions the illustrative gate sends every change to an A/B test.

## 1. Business context

Offline evals (often LLM judges) increasingly guide iteration on LLM-powered products, but standard validation asks whether judge outputs agree with human labels or whether benchmark scores rank systems like external assessments. A shipping decision asks something different: after a prompt revision, retrieval change, ranking adjustment or model swap, does the change in the eval predict the change in the online outcome? The paper builds a gate that decides, per change, whether to ship, kill, or send it to an A/B test, bounding the probability of shipping a change with a non-positive online effect.

## 2. Technical details

The unit of analysis is the intervention: each has a true eval effect τ_S,i and a true online effect τ_Y,i within a prespecified intervention class. This is trial-level surrogacy in the clinical-trials sense, with each intervention playing the role of a trial. Proposition 1 shows it is logically independent of unit-level (Prentice) surrogacy. In historical launch logs, sampling noise in both effect estimates attenuates the observed relationship; under a bivariate normal working model, subtracting the reported within-intervention variances from the sample covariance recovers the between-intervention covariance (an errors-in-variables / DerSimonian–Laird style correction). The corrected moments give a closed-form ship/test/kill rule. LLM judges add a separate distortion: when the judge is equally accurate on both arms, eval effects are only rescaled, but arm-dependent accuracy can reverse their sign. Pooling heterogeneous intervention classes can manufacture apparent surrogacy (appendix: classes with R² of 0.72 and 0.02 pool to a much higher figure), so the class is part of the estimand. Once a gate ships on evals alone, the eval-to-outcome relationship can no longer be observed in the ship and kill regions, so drift there is undetectable without randomized audit experiments.

## 3. Impact — potential & realized

Realized (per the paper): on the exploratory split of the Upworthy Research Archive (4,873 of 32,487 experiments; 1,050 tests from a documented randomization failure removed) the analysis uses 183 independent interventions across 10 headline-feature classes, with a GPT-4o-mini judge (5 ratings per headline) scoring how clearly the headline communicates what the reader gets, against click-through as the online outcome. Reliability ratios are 0.93 (eval) and 0.74 (outcome); the pooled corrected R² is 0.023, per-class estimates (9–27 interventions each) reach up to 0.15 with bootstrap intervals covering zero, and the fitted shipping threshold at α=0.10 (134pp) exceeds the largest possible eval delta (100pp), so nothing ships and every intervention goes to an A/B test. The authors call this the intended fail-closed behaviour and note a better-matched eval might behave differently. Potential: a principled way to decide when an eval can replace some A/B tests, and a reason to keep randomized audits.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Takes the surrogate-endpoint literature from clinical trials and applies it to the question every LLM-product team faces: when is the offline eval enough? The independence from Prentice surrogacy, the noise correction and the observability argument for audit experiments are the useful parts.

Takes the surrogate-endpoint literature from clinical trials and applies it to the question every LLM-product team faces: when is the offline eval enough? The independence from Prentice surrogacy, the noise correction and the observability argument for audit experiments are the useful parts. Evidence is simulations plus one public illustration where eval and outcome were deliberately mismatched (informativeness vs. clicks), so it shows the machinery works and fails closed rather than that a good LLM eval will clear the gate in practice.

### Similar / related work

- [**The Noise Is the Signal: Correlated Sampling Error Is Rank-Informative for Proxy Metric Selection**](2026-10-07-arxiv-noise-is-the-signal-proxy-metrics.md) (in this bank) — proxy-metric selection from A/B corpora, same noise-aware flavour
- [**Robust A/B Decisions**](2026-09-28-arxiv-robust-ab-decisions-farrell-misra.md) (in this bank) — decision-theoretic framing of ship decisions from experiments
- **Surrogate index (Athey et al.)** — combining short-term proxies into an index; cited by the paper

### Jargon buster

- **Trial-level surrogacy** — Whether the effect of a change on a cheap proxy (the eval) predicts its effect on the real outcome across a set of comparable changes.
- **Prentice surrogacy** — Unit-level condition that the proxy fully captures the treatment's effect on the outcome within a given trial; the paper shows it is independent of trial-level surrogacy.
- **Fail-closed** — The gate defaults to running an A/B test when the eval is not shown to predict online effects.
