---
id: doordash-eta-multitask-probabilistic
title: "Improving ETAs with Multi-Task Models, Deep Learning, and Probabilistic Forecasts at DoorDash"
source: "DoorDash Engineering"
url: "https://careersatdoordash.com/blog/improving-etas-with-multi-task-models-deep-learning-and-probabilistic-forecasts/"
published: "2024-11"
added: "2026-08-30"
category: forecasting-timeseries
tags: [eta, deep-learning, mixture-of-experts, multitask, probabilistic-forecast, feature-embeddings]
novelty: 4
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Improving ETAs with Multi-Task Models, Deep Learning, and Probabilistic Forecasts at DoorDash

**Source:** [DoorDash Engineering](https://careersatdoordash.com/blog/improving-etas-with-multi-task-models-deep-learning-and-probabilistic-forecasts/) · Published 2024-11 · Added 2026-08-30
**Category:** Forecasting & Time Series · **Tags:** `eta`, `mixture-of-experts`, `multitask`, `probabilistic-forecast`
_Surfaced via the Snacks Weekly on Data Science podcast._

## TL;DR

DoorDash moved ETA prediction from tree-based models to a neural
**MLP-gated mixture-of-experts** with three specialized encoders (DeepNet,
CrossNet, transformer), trained **multi-task** and producing **probabilistic**
forecasts rather than point estimates — for a **~20% relative** accuracy
improvement.

## 1. Business context

Estimated time of arrival is a load-bearing number across DoorDash: it shapes
consumer expectations, dispatch, and Dasher routing, and errors are expensive in
both directions (too optimistic frustrates customers; too conservative loses
orders). Tree-based ETA models had plateaued on accuracy, robustness, and
generalization across the many contexts a delivery passes through (store,
traffic, handoff). DoorDash wanted world-class predictions that also express
**uncertainty**, because a single point estimate hides the real-world variance
that operations must plan around.

## 2. Technical details

- **Architecture change.** Replaced tree-based models with neural networks for more
  accurate, robust, generalizable predictions.
- **MLP-gated mixture of experts (MoE).** A gating MLP routes each input to a blend
  of **three specialized encoders** — **DeepNet**, **CrossNet**, and a
  **transformer** — so the model adapts to diverse scenarios and captures different
  kinds of feature interaction.
- **Feature embeddings.** Feature-embedding techniques encode **high-cardinality**
  inputs, sharpening the model's ability to discern patterns specific to
  particular segments.
- **Multi-task learning.** Training several related ETA tasks together improves
  consistency across scenarios and enables **knowledge transfer** between tasks.
- **Probabilistic forecasts.** The model predicts a distribution, not just a point,
  so downstream systems can reason about uncertainty (e.g. choose conservative vs.
  expected ETAs by context).

## 3. Impact — potential & realized

- **Realized:** a **~20% relative improvement in ETA accuracy**, improving
  operational efficiency and the reliability of ETAs shown to customers.
- **Potential:** the pattern — MoE with heterogeneous encoders + multitask +
  distributional outputs — transfers to most large-scale spatiotemporal
  prediction problems (dispatch, supply/demand, wait times).

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a strong, specific applied-ML recipe with a real number

The individual pieces (MoE, DeepNet/CrossNet, transformers, multitask,
probabilistic heads) are known, but assembling them into a single ETA model with
a **gated blend of three complementary encoders** and reporting a clean **20%**
relative gain is exactly the kind of concrete, reusable applied-ML write-up worth
capturing. The move from point to **probabilistic** forecasts is the part most
teams under-invest in and the most transferable idea here. A 4: excellent
engineering, not a new method.

### Similar / related work

- [**Databricks Feature Store: Sub-Second Freshness**](2026-08-30-databricks-feature-store-subsecond-freshness.md) (in this bank) — the feature
  infrastructure side of serving models like this in real time.
- [**UME: A Unified Meta-Generalization Framework for Cross-Domain ETA**](https://arxiv.org/abs/2606.00979)
  (arXiv 2606.00979) — a research take on generalizing ETA across domains.
- **DoorDash "Precision in Motion"** — a companion post on deep learning for ETA.

### Jargon buster

- **Mixture of experts (MoE)** — a model with several sub-networks ("experts") and a
  gate that decides how much each contributes per input, so different experts
  specialize in different situations.
- **DeepNet / CrossNet** — DeepNet is a standard deep MLP; CrossNet explicitly models
  feature *crosses* (interactions) efficiently; together they capture both
  nonlinearities and interactions.
- **Multi-task learning** — training one model on several related objectives at once,
  so shared structure transfers and each task regularizes the others.
- **Probabilistic forecast** — a prediction of a full distribution (with uncertainty),
  not a single number, enabling risk-aware decisions.
- **High cardinality** — a feature with very many distinct values (e.g. store IDs);
  hard for models to use raw, which is why they're embedded.
