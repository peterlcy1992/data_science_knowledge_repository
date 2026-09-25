---
id: amazon-ppi-persona-llm-ab-testing
title: "Augmented Hypothesis Testing with Persona-Based LLM Simulations"
source: "arXiv (Amazon)"
url: "https://arxiv.org/abs/2609.24629"
published: "2026-09"
added: "2026-09-25"
category: experimentation-causal
tags: [ab-testing, prediction-powered-inference, llm-simulation, sample-size-reduction, hypothesis-testing]
novelty: 4
sourced_via: "web search"
---

# Augmented Hypothesis Testing with Persona-Based LLM Simulations

**Source:** [arXiv (Amazon)](https://arxiv.org/abs/2609.24629) · Published 2026-09 · Added 2026-09-25
**Category:** Experimentation & Causal Inference · **Tags:** `ab-testing`, `prediction-powered-inference`, `llm-simulation`, `sample-size-reduction`, `hypothesis-testing`

## TL;DR

Amazon researchers show how to fold uncertain-quality ML/LLM predictions of a treatment effect into standard A/B-test hypothesis testing to shrink the sample size needed for a statistically valid result, without inflating false-positive rates if the predictions turn out to be wrong. They validate the method using "persona-based" LLM simulations — AI agents role-playing user personas to predict how a real person would respond to a treatment — across four real datasets.

## 1. Business context

A/B tests are the gold standard for causal decisions, but they're expensive: reaching statistical significance can require large sample sizes, long run times, or both, especially for effects that are real but small. Meanwhile, teams increasingly have access to predictions — from ML models or, more recently, LLM agents simulating how a "persona" would behave — that hint at what an experiment's outcome will be before it's run. The problem is that naively trusting those predictions is dangerous: if the model or the LLM persona is wrong, treating its output as ground truth corrupts the statistical validity of the test. The paper's goal is a framework that captures the sample-size savings when predictions are good, while remaining statistically safe (no inflated false-positive rate) when they aren't.

## 2. Technical details

The authors propose two complementary methods depending on the granularity of the available prediction. For coarse, population-level directional signals (e.g., "the model predicts this treatment increases the metric"), they use an asymmetric hypothesis test built on the learning-augmented algorithms paradigm, with proven consistency and robustness bounds — the test's behavior degrades gracefully rather than catastrophically as prediction quality declines. For fine-grained, individual-level predictions, they introduce "Generalized PPI++" (GPPI), which extends Prediction-Powered Inference (PPI) — a framework for combining a small amount of labeled experimental data with a larger amount of predicted data — to handle nonlinear prediction errors via higher-dimensional transformations, something the original PPI/PPI++ methods don't natively support. Both methods are validated using persona-based LLM simulations: LLM agents assigned specific user personas generate predicted individual-level responses to a proposed treatment, which are then fed into the GPPI framework alongside a smaller real experimental sample, tested across four real-world datasets.

## 3. Impact — potential & realized

The paper reports that its methods substantially reduce experimental costs (i.e., required sample size / run time) while preserving rigorous statistical validity — the whole point being that a team can lean on LLM-persona predictions to get a faster read without abandoning the guarantees a standard significance test provides. The broader potential is significant given how fast "AI agents predicting user behavior" is being adopted as a pre-experiment triage or amplification tool: this gives that practice a statistically principled harness instead of an ad hoc "trust the LLM's guess" approach, and the GPPI extension is reusable for any nonlinear individual-level prediction source, not just LLM personas specifically.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A genuine methodological extension addressing a real, fast-growing failure mode

Prediction-Powered Inference is an active, well-regarded line of statistics research, and extending it to handle nonlinear individual-level predictions (GPPI) is a real technical contribution, not just a rebrand. What makes this especially timely is the target application: LLM-persona simulation of user behavior is being adopted in industry (marketing research, UX testing, even pre-experiment power estimation) much faster than anyone has built rigorous statistics around it, so a framework that explicitly keeps the false-positive rate bounded even when the LLM's predictions are bad is exactly the kind of guardrail this space needs before it becomes a source of quietly-wrong product decisions.

### Similar / related work

- [**Decoding Causal Incrementality in E-Commerce: Leveraging Bayesian Structural Time Series Model with a Real-World Example**](2026-09-19-walmart-bayesian-structural-time-series.md) (in this bank) — a different route (Bayesian structural time series) to the same underlying goal of getting a trustworthy causal read with less reliance on a full randomized rollout.
- [**Beyond the A/B Test: Experiment Designs for Your Toughest Questions**](2026-09-25-statsig-beyond-ab-test-designs.md) (in this bank) — a practitioner's survey of alternative experiment designs for cases where a standard A/B test is hard to run; this paper is a complementary statistical technique for shrinking the sample size a standard A/B test needs in the first place.
- **Prediction-Powered Inference (Angelopoulos et al.)** — the original PPI framework this paper's GPPI method extends; foundational reading for understanding why combining labeled and predicted data needs a careful statistical treatment rather than naive pooling.

### Jargon buster

- **Prediction-Powered Inference (PPI)** — a statistical framework for combining a small amount of gold-standard labeled data with a larger amount of ML-predicted data to get a more precise (smaller sample size) estimate, while still producing statistically valid confidence intervals even if the predictions are imperfect.
- **Persona-based LLM simulation** — using an LLM prompted to role-play a specific user persona (demographics, preferences, behavior patterns) to predict how that kind of user would respond to a product change, as a cheap substitute or supplement for real user data.
- **Learning-augmented algorithms** — a design paradigm for algorithms that use a possibly-unreliable prediction to improve performance when the prediction is good, while guaranteeing a fallback worst-case performance bound when the prediction is bad.
