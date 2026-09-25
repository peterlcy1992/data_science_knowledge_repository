---
id: arxiv-tie-handling-recsys-evaluation
title: "Tie Handling Is Part of the Evaluation Protocol: An Order-Invariance Audit for Tie-Heavy Recommender Scores"
source: "arXiv (FRAME'26 workshop)"
url: "https://arxiv.org/abs/2609.26977"
published: "2026-09"
added: "2026-09-25"
category: research-foundational
tags: [evaluation-methodology, ndcg, tie-breaking, offline-evaluation, reproducibility]
novelty: 4
sourced_via: "web search"
---

# Tie Handling Is Part of the Evaluation Protocol: An Order-Invariance Audit for Tie-Heavy Recommender Scores

**Source:** [arXiv (FRAME'26 workshop)](https://arxiv.org/abs/2609.26977) · Published 2026-09 · Added 2026-09-25
**Category:** Research & Foundational · **Tags:** `evaluation-methodology`, `ndcg`, `tie-breaking`, `offline-evaluation`, `reproducibility`

## TL;DR

Offline top-K recommender evaluation can swing wildly depending purely on how tied scores get broken: on Amazon Beauty & Personal Care data with a rating-weighted attribute-overlap scorer, NDCG@10 for the exact same model ranged from 0.85 (input-order tie-breaking) down to 0.17 (deterministic hash-based tie-breaking) — a difference caused entirely by tie-handling choice, not model quality. The paper formalizes "row-order invariance" and argues tie-handling must be a documented, mandatory part of any evaluation protocol.

## 1. Business context

Any team that reports offline ranking metrics (NDCG, Hit Rate, MRR) to decide whether a new recommender model is better than the old one is implicitly relying on those metrics being comparable across runs and across models. Many real scoring functions — especially simpler, feature-based, or coarsely-discretized ones — produce exact ties between candidate items far more often than practitioners assume, and how an evaluation pipeline breaks those ties (by input order, by a hash of IDs, by random draw) is usually an unexamined implementation detail rather than a deliberate methodological choice. If that detail alone can swing a headline metric by 5x, then published or internally-reported comparisons between models could be measuring tie-breaking artifacts rather than genuine ranking quality — a silent threat to any decision (ship this model, publish this benchmark result) built on those numbers.

## 2. Technical details

The paper defines an evaluator as "row-order invariant" when permuting the input candidates — without changing their identities, labels, or scores — leaves the final ranking, and therefore the computed metric, unchanged. That invariance breaks down whenever the scoring function produces ties, because different tie-breaking rules resolve the ambiguous ordering differently. The authors demonstrate the effect concretely on Amazon Beauty & Personal Care data using a rating-weighted attribute-overlap scoring method (a scorer prone to producing many exact ties), comparing three tie-breaking approaches: input-order tie-breaking (which happened to favor the relevant item's position, producing NDCG@10 = 0.85), deterministic hash-based tie-breaking on user and item IDs (which broke ties unfavorably, producing NDCG@10 = 0.17), and uniform random tie-breaking averaged across 100 independent seeds (a more defensible middle ground). The authors derive closed-form expected values for Hit Rate and NDCG at a given cutoff k under random tie-breaking, giving practitioners a principled way to report an expectation rather than an arbitrary single tie-breaking outcome, and provide a practical reporting checklist for documenting tie-handling in evaluation protocols going forward.

## 3. Impact — potential & realized

The realized contribution is the audit itself and the mathematical machinery (the row-order invariance definition and the expected Hit Rate/NDCG derivations) plus the reporting checklist — a directly actionable methodology fix any team running offline recommender evaluation can apply immediately. The potential impact is broader: any published benchmark or internal offline-evaluation pipeline that doesn't document its tie-breaking rule is, per this paper, at risk of reporting numbers that aren't comparable to other runs or other papers, which — given how common ties are in tie-heavy scorers — could mean a meaningful slice of reported recsys benchmark results in the wild have this undocumented degree of freedom baked in.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A small, sharp methodology finding with a striking, reproducible number and immediate practical relevance

The 0.85-vs-0.17 gap is the kind of result that's easy to dismiss as an edge case until you internalize how common near-tied or exactly-tied scores are in practice (coarse relevance labels, quantized scores, sparse feature overlap) — this isn't a synthetic pathology, it's a plausible failure mode in a lot of production and benchmark evaluation pipelines that nobody is checking for. It won't reshape model architectures, but it's exactly the kind of "check your evaluation harness" finding that should become a standard item on any recsys team's offline-eval checklist, and it fits squarely in this bank's mandate to prioritize measurement and evaluation rigor over flashier model results.

### Similar / related work

- [**Buy One Get One Free: Promotion-Aware Demand Forecasting for Groceries**](2026-09-23-afresh-promotion-aware-demand-forecasting.md) (in this bank) — a different domain's version of the same underlying lesson: a model or evaluation that looks fine on an aggregate metric can hide a specific, consequential failure mode.
- [**The Forecast Says Zero. The Warehouse Says Otherwise.**](2026-09-25-nixtla-intermittent-demand-zero-forecast-trap.md) (in this bank) — a close methodological cousin in forecasting: a metric that can be "won" by an artifact of the evaluation setup rather than genuine model quality.
- **NDCG and ranking-metric literature generally** — the standard formal definitions of NDCG, Hit Rate, and MRR this paper's invariance property is defined against.

### Jargon buster

- **Row-order invariance** — the property that an evaluation metric shouldn't change if you feed the same candidates into the evaluator in a different order, assuming their scores and labels are unchanged; this paper shows tie-heavy scorers violate this property unless tie-breaking is handled carefully.
- **NDCG (Normalized Discounted Cumulative Gain)** — a standard ranking-quality metric that rewards placing relevant items higher in a ranked list, discounted by position; sensitive to exact ordering, which is why tie-breaking matters so much for it.
- **Tie-breaking rule** — the method an evaluation pipeline uses to decide the relative order of items that received identical scores from a model — e.g., keep their original input order, use a deterministic hash, or break ties randomly.
