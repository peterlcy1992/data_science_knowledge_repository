---
id: arxiv-instagram-feed-baseline-incremental-debiasing
title: "Baseline and Incremental: User, Item, and Request Debiasing in Instagram Feed Ranking"
source: "arXiv cs.IR (Chen et al., Meta)"
url: "https://arxiv.org/abs/2610.27423"
published: "2026-10"
added: "2026-10-21"
category: search-ranking
tags: [feed-ranking, debiasing, value-model, ablation, position-popularity-bias]
novelty: 4
sourced_via: "web search"
---

# Baseline and Incremental: User, Item, and Request Debiasing in Instagram Feed Ranking

**Source:** [arXiv cs.IR (Chen et al., Meta)](https://arxiv.org/abs/2610.27423) · Published 2026-10 · Added 2026-10-21
**Category:** search-ranking · **Tags:** `feed-ranking`, `debiasing`, `value-model`, `ablation`, `position-popularity-bias`

## TL;DR

Meta argues a feed ranker's value model should keep the raw engagement prediction and add the incremental (de-baselined) part as a separately weighted term, unifying viewer-habit, item-popularity and request-context debiasing in one parameterized operator; a four-arm production ablation in Instagram Feed favours using both terms.

## 1. Business context

Feed rankers score candidates with a weighted sum of engagement predictions. Each prediction mixes a baseline (what this viewer, item or request would produce anyway) with the incremental lift attributable to showing the candidate. Most prior debiasing work subtracts the baseline entirely; the authors argue that discards useful signal.

## 2. Technical details

Three debiasing families (viewer habit, item popularity, request context) are expressed as instances of one parameterized operator, with a design procedure that selects a point in it. The value model keeps the raw prediction and adds the incremental term as its own weighted term. Media-type bias is handled separately through a debiased training label chosen by the same procedure. Evaluation is a controlled production ablation with four arms: neither term, each term alone, and both. The authors also suggest the offline diagnostic should be used to screen signals rather than rank them. The abstract does not give the formulas, weights or datasets.

## 3. Impact — potential & realized

Reported: at production weights the two-term arm beat both single-term arms on point estimates in 11 of 13 judged (term, metric) pairs; of 26 direct contrasts measured on impressions, 17 significantly favoured the two-term arm and 1 significantly favoured the opposing arm. The terms have run in Instagram Feed production for most of a year, and Meta reports adopting the operator on other surfaces and in both ranking stages, with launches driving sessions and daily active users. Effect sizes, confidence levels and specific metrics are not in the abstract.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Reframes ranker debiasing as baseline + incremental terms, backed by a year-long production ablation.

The idea that a baseline is signal, not just bias, is simple and testable, and the paper's strongest feature is that it reports the ablation honestly, including one significant contrast against its own favoured arm and the 11-of-13 (not 13-of-13) count. Caveats: abstract-level read, a 26-author industrial paper with no effect sizes shown, and multiple contrasts across metrics, so the 17/26 headline needs multiplicity context. Novelty 4/5 because it reframes debiasing from removal to decomposition and backs it with a year of production use.

### Similar / related work

- [**Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent**](2026-10-20-arxiv-selling-in-the-wild-sales-agent-field-rct.md) — another production-scale, controlled-arm evaluation (in this bank)
- [**Don't Rewrite the SID Map: Topology Preservation for Generative Retrieval**](2026-10-20-arxiv-sid-topology-preservation-generative-retrieval-tmall.md) — industrial ranking/retrieval change judged in online tests (in this bank)

### Jargon buster

- **Debiasing** — Removing the part of an engagement prediction explained by who the viewer is, how popular the item is, or the request context rather than by the candidate itself.
- **Value model** — The weighted combination of predicted engagement events that a feed ranker uses to order candidates.
- **Ablation** — Switching components on and off in controlled arms to see what each contributes.
