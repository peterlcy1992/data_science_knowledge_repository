---
id: arxiv-bayesjudge-bayesian-meta-evaluation
title: "BayesJudge: Uncertainty-Aware Bayesian Meta-Evaluation of Human and LLM Judgments"
source: "arXiv stat.AP (Zhang, Feng, Meng, He, Hao)"
url: "https://arxiv.org/abs/2610.11116"
published: "2026-10"
added: "2026-10-09"
category: statistical-modeling
tags: [llm-as-judge, bayesian, rater-reliability, position-bias, sequential-monte-carlo]
novelty: 3
sourced_via: "web search"
---

# BayesJudge: Uncertainty-Aware Bayesian Meta-Evaluation of Human and LLM Judgments

**Source:** [arXiv stat.AP (Zhang, Feng, Meng, He, Hao)](https://arxiv.org/abs/2610.11116) · Published 2026-10 · Added 2026-10-09
**Category:** statistical-modeling · **Tags:** `llm-as-judge`, `bayesian`, `rater-reliability`, `position-bias`, `sequential-monte-carlo`

## TL;DR

BayesJudge is an online Bayesian layer that infers a posterior over which of two responses is better, jointly estimating rater-specific confusion matrices and LLM position bias, with tie-open labels and order-swapped judge calls to separate quality from presentation effects. Accepted at NeurIPS 2026.

## 1. Business context

Evaluation of generative models leans on human and LLM judges who disagree. Disagreement can mean an ambiguous item, a vague rubric, an unreliable rater, or an LLM whose verdict flips when answer order is swapped. Teams need to know which, rather than averaging it away.

## 2. Technical details

Per the abstract: a posterior over which of two responses is better relative to the rater panel, with an optional tie/ambiguity state; rater-specific human confusion matrices; an LLM position-bias parameter. Tie-open labels keep ambiguity visible, and order-swapped paired judge calls separate item preference from presentation. The exact online posterior recursion is derived and approximated by a scalable Rao-Blackwellized assumed-density sequential Monte Carlo method. Experiments: synthetic data recover prespecified evaluator parameters; on SummEval it detects systematic order effects, distinguishes expert from crowdworker behaviour without rater metadata, and posterior uncertainty correlates with human disagreement.

## 3. Impact — potential & realized

Realized: parameter recovery on synthetic data and qualitative findings on SummEval (no figures in the abstract). Potential: evaluation pipelines that report uncertainty and flag unreliable raters or biased judges instead of a single agreement score.

*Sourced from the arXiv abstract page; full text not reviewed.*

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A principled statistical treatment of judge noise; the DS value is the explicit measurement model.

This is classic Dawid-Skene-style rater modelling extended with position bias and ties, made online. It complements the GLMM view in the sibling paper in this bank. The test of usefulness will be whether it changes decisions on real eval sets, which the abstract does not show.

### Similar / related work

- [**Trustworthy Method Comparison with AI Judges**](2026-10-07-arxiv-trustworthy-method-comparison-ai-judges.md) (in this bank) — GLMM view of the same order effects; 
- [**Using MemAlign to Improve Evaluation of Traditional Machine Learning in Genie Code**](2026-09-18-databricks-memalign-llm-judges.md) (in this bank) — aligning LLM judges; 
- [**LLM-based Relevance Assessment for Web-Scale Search Evaluation at Pinterest**](2026-10-08-pinterest-llm-relevance-assessment-search-evaluation.md) (in this bank) — LLM judge in a production evaluation setting; 

### Jargon buster

- **Confusion matrix (rater)** — The probabilities that a rater gives each label given the true label, capturing their specific error pattern.
- **Position bias** — The tendency of an LLM judge to prefer the response shown first (or second) regardless of quality.
- **Rao-Blackwellized SMC** — A particle-filter variant that integrates out part of the state analytically to reduce variance.
