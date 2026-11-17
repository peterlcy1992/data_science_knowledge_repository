---
id: arxiv-ranker-comparisons-unlinked-dp-item-counts
title: "What Unlinked Aggregates Still Prove: Ranker Comparisons from Exact and Differentially Private Item Counts"
source: "Duke / Stanford (arXiv cs.IR, IEEE BigData 2026)"
url: "https://arxiv.org/abs/2611.20388"
published: "2026-11"
added: "2026-11-17"
category: personalization-recsys
tags: [offline-evaluation, partial-identification, differential-privacy, transportation-lp, missing-data, ndcg, privacy-preserving-measurement, aggregate-data]
novelty: 3
sourced_via: "full-text fetch"
---

# What Unlinked Aggregates Still Prove: Ranker Comparisons from Exact and Differentially Private Item Counts

**Source:** [Duke / Stanford (arXiv cs.IR, IEEE BigData 2026)](https://arxiv.org/abs/2611.20388) · Published 2026-11 · Added 2026-11-17
**Category:** Personalization & Recommender Systems · **Tags:** `offline-evaluation`, `partial-identification`, `differential-privacy`, `transportation-lp`, `missing-data`, `ndcg`, `privacy-preserving-measurement`, `aggregate-data`

## TL;DR

When privacy controls stop an evaluator from linking some users' purchases to the recommendations they'd have seen, a merchant's item-level purchase counts for the cohort still constrain who could have bought what. Bounding the ranker-vs-ranker metric difference over every assignment consistent with those counts — a transportation linear program — narrows the interval in every tested case and sometimes proves which recommender is better, with a differentially private variant that carries one confidence guarantee across all comparisons from a single release.

## 1. Business context

A merchant commissions an offline comparison of two recommenders. The evaluator holds each system's slate for every user but cannot join some purchases to those slates; the merchant still records its own sales and can return how many cohort users bought each item. Common practice wastes that information: complete-case evaluation drops unlinked users (and can reverse when linkage correlates with outcomes), propensity weighting needs a model of who stays linked, imputation needs a model of outcomes, and per-user worst-case bounds ignore the aggregate and are usually too wide to decide anything. The question is when unlinked counts alone identify the better ranker on the full cohort, with no missingness model.

## 2. Technical details

- **Coupling idea.** If exactly three unlinked users bought item *j*, at most three of them can be credited with it — a valid bound can't credit *j* to every user for whom it's most favourable. A two-user Hit@1 example goes from per-user bounds of [−2, 2] to an exact answer of +1 once counts are known.
- **Sharp bounds (Theorem 1).** With exact counts, the min and max of the paired NDCG@k or Recall@k difference over all consistent completions are the optimal values of a totally unimodular transportation LP over users and items; the interval is nested inside the per-user interval, and refining nested exact-count segments never widens it.
- **Scaling.** A reduced network avoids the user × catalog product, with completion checks and lazy refinement to certify that endpoints are attainable.
- **Private release.** Counts released with Laplace noise (scale 2/ε, replace-one adjacency) yield a simultaneous confidence box with coverage ≥ 1−α for every comparison from one release, as post-processing (no extra privacy budget). A bound on the widening shows it grows with *M* ln *M* (number of bins) and shrinks as 1/*n*, favouring coarse releases.
- **Experiments.** Beibei (20,623 users) and Tmall (103,507 users); four rankers with fixed hyperparameters — Pop, ItemKNN (100 neighbours), PureSVD (64 factors), EASE (λ=250) — all six pairs; random, trait-dependent and outcome-dependent linkage; ε ∈ {0.5, 1, 2, 4} (Beibei) and {1, 4} (Tmall).

## 3. Impact — potential & realized

**Measured:**
- Exact cohort-level counts narrowed every ranker-pair interval versus bounds that ignore them; most decisions involved Pop, whose slates concentrate on few items.
- For NDCG@10 on personalized pairs, exact counts settled 14 of 168 settings on Beibei and none of 81 on Tmall. Exact counts broken down by user segment settled both tested Beibei personalized pairs at 90% linkage, at the cost of revealing more about individual purchases.
- Whole-cohort private releases (one count per item) kept much of the narrowing but settled no personalized pair in either cohort; binning less popular items let private counts settle one personalized pair on Beibei.
- For full histograms at ε=1, α=0.05, the worst-case widening bound exceeds the metric range (18.5 on Beibei, 4.7 on Tmall), so the useful private regime is coarse releases or larger cohorts.

**Potential:** a principled, assumption-light way to run offline evaluation under privacy-driven linkage loss — "prove an order when the counts determine one, and quantify the remaining uncertainty otherwise". The estimand is the cohort itself; population claims need a separate sampling argument.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Manski-style bounds meet clean-room measurement

Partial identification isn't new, but pairing it with the exact shape of a privacy-preserving release (item histograms, Laplace noise) and solving it as a transportation LP is a neat, practical construction. The honest results are its strength: on the harder personalized comparisons the counts rarely settle the question, which is exactly what an analytics team needs to hear before trusting a privacy-degraded offline eval. Likely most useful to ads/attribution teams already living with aggregated reporting APIs.

### Similar / related work

- [**Tie Handling Is Part of the Evaluation Protocol**](2026-09-25-arxiv-tie-handling-recsys-evaluation.md) (in this bank) — another reminder that offline recsys conclusions can hinge on protocol choices.
- [**Prediction-Powered LLM Ranking with Adaptively Collected Human Feedback**](2026-11-11-arxiv-pp-rank-prediction-powered-llm-ranking-adaptive-feedback.md) (in this bank) — model-assisted rather than bound-based inference for ranking comparisons.
- Partial identification literature (Manski) — the general framework of reporting sharp bounds instead of point estimates under missing data.

### Jargon buster

- **Partial identification** — reporting the full range of values consistent with the data rather than one point estimate, when the data can't pin the answer down.
- **Transportation problem** — an LP that assigns supply (users) to demand (item counts) at optimal cost; total unimodularity guarantees integer solutions.
- **Laplace mechanism** — adding Laplace-distributed noise to counts so any one person's data barely changes the release (differential privacy).
- **NDCG@10** — a ranking metric rewarding relevant items placed higher in the top 10.
