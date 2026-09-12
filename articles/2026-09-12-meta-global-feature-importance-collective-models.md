---
id: meta-global-feature-importance-collective-models
title: "Collective Wisdom of Models: Advanced Feature Importance Techniques at Meta"
source: "Analytics at Meta (Medium)"
url: "https://medium.com/@AnalyticsAtMeta/collective-wisdom-of-models-advanced-feature-importance-techniques-at-meta-1a7a8d2f9e27"
published: "2025-04"
added: "2026-09-12"
category: research-foundational
tags: [feature-selection, feature-importance, model-aggregation, meta]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Collective Wisdom of Models: Advanced Feature Importance Techniques at Meta

**Source:** [Analytics at Meta (Medium)](https://medium.com/@AnalyticsAtMeta/collective-wisdom-of-models-advanced-feature-importance-techniques-at-meta-1a7a8d2f9e27) · Published 2025-04 · Added 2026-09-12
**Category:** Research & Foundational · **Tags:** `feature-selection`, `feature-importance`, `model-aggregation`, `meta`

## TL;DR

Meta built a "Global Feature Importance" score that aggregates feature-importance results logged across many different models, tasks, and time periods, on the observation that a feature which scores well in one model in a shared feature universe tends to score well in related models too — giving teams a more robust importance signal than trusting any single model's assessment.

## 1. Business context

At Meta's scale, ML engineers routinely have access to thousands of candidate features per model, and manually exploring which ones are worth including becomes impractical once you're doing it across many models and product surfaces rather than just one. Any individual model's feature-importance run is also just one noisy sample — a feature might look unimportant in one run due to interaction effects, data slice quirks, or that specific model's architecture, even if it's genuinely valuable. The problem Meta set out to solve was less "how do we compute feature importance" (a solved problem) and more "how do we get a trustworthy signal about a feature's value when the honest answer requires looking across many models at once."

## 2. Technical details

The approach leans on a practical empirical observation: within the same **feature universe** (a shared pool of candidate features available to a family of related models), a feature that performs well in one model tends — though not always — to perform well in other models drawing from that same universe. Meta operationalizes this by:

- Continuously logging feature-importance results from every feature-importance run across the organization — both scheduled runs and ad hoc ones engineers kick off during model development — capturing the feature, the model, the task, the date, and the feature universe it belongs to.
- Aggregating those logged importance scores across models sharing a feature universe into a single **Global Feature Importance** score per feature, rather than relying on the importance score from any one model's run in isolation.
- Using that aggregated score as a more robust prior when engineers are exploring or vetting a feature for a *new* model — effectively letting a new model benefit from what every other related model has already learned about that feature's value, instead of starting the importance assessment from scratch.

The write-up frames this as tapping the "collective wisdom" of all the models that have ever touched a given feature universe, turning what used to be siloed, per-model importance analysis into a shared, continuously-growing organizational asset.

## 3. Impact — potential & realized

**Realized:** the write-up describes Global Feature Importance as deployed practice at Meta for guiding feature exploration and selection decisions across models sharing a feature universe; it does not report a specific headline metric (e.g., an offline or online lift figure) for adopting the aggregated score over single-model importance.

**Potential:** the pattern — continuously logging every importance run and aggregating across models sharing an input space — generalizes to any organization running many related models against overlapping feature sets, where the real bottleneck is that no single model's importance run is a fully trustworthy signal on its own, and cross-model aggregation is cheap once the logging infrastructure exists.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sensible aggregation idea, more an organizational practice than a new technique

The statistical technique underneath this — aggregating importance scores across models — isn't novel by itself; ensembling and pooling feature-importance estimates has precedent in the ML literature. What's genuinely useful here is treating feature-importance logging as *permanent organizational infrastructure* rather than a disposable byproduct of each individual training run, so importance signal compounds across every model built over time instead of evaporating after each project. That's a good practice more than a research advance, and the lack of a reported quantitative lift makes it harder to judge how much better the aggregated signal actually is than a well-regularized single-model importance estimate.

### Similar / related work

- [**Meta's Ranking Engineer Agent (REA)**](2026-09-10-meta-ranking-engineer-agent-rea-ads.md) (in this bank) — a different Meta system automating a different part of the ML lifecycle (model architecture search rather than feature selection), but part of the same broader Meta pattern of building organization-wide infrastructure that lets many models learn from each other's history.
- **Aggregate Models, Not Explanations: Improving Feature Importance Estimation** — a closely related research thread (arXiv:2602.11760) arguing for aggregating at the model level rather than the explanation level, a useful academic counterpoint to Meta's cross-model aggregation approach.
- **Ensemble feature selection (general ML literature)** — the broader, well-established statistical practice of combining multiple feature-importance estimates to get a more stable ranking; not tied to one canonical paper.

### Jargon buster

- **Feature importance** — a score assigned to each input feature of a trained model estimating how much that feature contributes to the model's predictions.
- **Feature universe** — the shared pool of candidate input features available to a family of related models (e.g., all models built for a given product surface), as distinct from the smaller subset any one model actually uses.
- **Feature selection** — the process of deciding which candidate features to actually include in a model, typically to reduce complexity, training cost, or overfitting risk while preserving predictive power.
