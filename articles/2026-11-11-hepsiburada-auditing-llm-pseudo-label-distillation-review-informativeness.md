---
id: hepsiburada-auditing-llm-pseudo-label-distillation-review-informativeness
title: "Auditing LLM Pseudo-Label Distillation for Review Informativeness at E-Commerce Scale"
source: "arXiv cs.IR (Hepsiburada Analytics: Er, Kulunk, Eseoglu, Sahin)"
url: "https://arxiv.org/abs/2611.13797"
published: "2026-11"
added: "2026-11-11"
category: llm-genai
tags: [distillation, weak-supervision, LLM-labels, temporal-evaluation, evaluation-design, review-ranking]
novelty: 3
sourced_via: "full-text fetch"
---

# Auditing LLM Pseudo-Label Distillation for Review Informativeness at E-Commerce Scale

**Source:** [arXiv cs.IR (Hepsiburada Analytics: Er, Kulunk, Eseoglu, Sahin)](https://arxiv.org/abs/2611.13797) · Published 2026-11 · Added 2026-11-11
**Category:** llm-genai · **Tags:** `distillation`, `weak-supervision`, `LLM-labels`, `temporal-evaluation`, `evaluation-design`, `review-ranking`

## TL;DR

Hepsiburada distils Gemini 3.1 Flash-Lite labels of review informativeness into compact Turkish encoders on 5.34M reviews. The careful part is evaluation: a category prefix slightly improves fidelity to the teacher on a strict new-SKU test but reduces agreement with both Gemini and a blind human annotator on a 16K chronological audit — so teacher fidelity alone does not establish editorial alignment. The student pipeline runs 50.2× faster than the teacher.

## 1. Business context

Marketplaces want to surface reviews with product-specific evidence (fit, durability, compatibility) over delivery-only comments — a narrower construct than general 'helpfulness'. LLMs can label millions of reviews to train cheap students, but a student agreeing with its teacher and agreeing with an editorial reference are different questions, and the paper's contribution is an evaluation of what survives entity and time shift.

## 2. Technical details

Data: 5,344,302 reviews (June 2025–June 2026); cutoff May 7, 2026 fixed before training; SKU-disjoint train (3,844,147), validation (486,000) and IID test (479,724); strict out-of-time set of 159,570 reviews from SKUs first seen after the cutoff. Teacher: frozen Vertex AI gemini-3.1-flash-lite, temperature and thinking budget 0, three ordinal classes, structured output with reason and signals; only hard scores train students.

Students: BERTurk with text only or H3-category prefix + text, cross-entropy vs CORN ordinal loss, three seeds; plus XLM-R, COSMOS Turkish BERT and Turkish ModernBERT (21 runs). Audit: one native-Turkish company annotator labeled 40,000 reviews blind to Gemini labels (no second annotator); a 16,000-review chronological OOT subset is the held-out audit. Paired SKU-bootstrap (1,000 draws) intervals for contrasts.

## 3. Impact — potential & realized

Realized: on the strict new-SKU test, the category prefix raises BERTurk QWK by .0023 (CE) and .0016 (CORN); ModernBERT CORN/C is highest at QWK .9223. On the 16K audit the prefix lowers annotator QWK by −.0011 for CE (95% CI [−.0039, .0012]) and −.0040 for CORN ([−.0068, −.0014]), and also lowers teacher fidelity there; the authors stress these are different populations, so this does not show a same-population trade-off. Gemini agrees exactly with the annotator on 93.79% of the audit subset (90.34% over all 40K); 3,855 of 3,864 disagreements are adjacent classes. Under a combined market/language shift (~30K Amazon reviews, teacher labels only), XLM-R leads (QWK .7614). Teacher-relative NDCG@10 is .9846 for the student vs .7858 for the production composite, but the authors caution this shows teacher-relative ordering, not independent ranking quality. Throughput: 2,218 reviews/s on one L4 vs 44.19/s for the teacher pipeline (50.2×, not hardware-normalised, not an online A/B result).

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Modest modelling, exemplary evaluation hygiene: a useful template for anyone shipping LLM-distilled classifiers.

The most valuable thing here is the discipline of naming the evaluation population and the reference target for every number — the kind of thing that stops a small 'improvement' from being a measurement artefact. Data scientists building LLM-labelled training sets should copy the frozen-teacher protocol, the SKU-disjoint and out-of-time splits, and the blind human audit. Limits are acknowledged: one annotator, input mismatch between teacher and students, and no online test.

### Similar / related work

- [**From Generation to Scoring: Scaling LLM-Based Semantic Labeling at LinkedIn**](2026-11-04-linkedin-from-generation-to-scoring-llm-semantic-labeling.md) — in this bank: LinkedIn's use of LLM labels to train scoring models
- [**Evaluating Netflix Show Synopses with LLM-as-a-Judge**](2026-09-14-netflix-llm-judge-show-synopses.md) — in this bank: another check of LLM judgments against human editorial standards
- [**Distilling the Knowledge in a Neural Network**](https://arxiv.org/abs/1503.02531) — the classic distillation reference the paper cites

### Jargon buster

- **Hard-label distillation** — Training a small model on a big model's final predicted class labels rather than its probabilities.
- **QWK** — Quadratic weighted kappa: agreement between two ordinal labelers that penalises far-off disagreements more.
- **CORN** — Conditional ordinal regression: predicts P(y>0), then P(y>1 | y>0), respecting class order.
- **Out-of-time (OOT) test** — Evaluation on data from after the training cutoff, here also restricted to never-seen products.
