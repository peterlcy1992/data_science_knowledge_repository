---
id: arxiv-statistical-detection-positional-bias-llm-recommender
title: "Statistical Detection of Positional Bias in LLM-Based Recommender Systems: Methodologies and Empirical Evidence"
source: "arXiv cs.IR (Peláez-González, Herrera, Herrera-Poyatos, University of Granada)"
url: "https://arxiv.org/abs/2610.37962"
published: "2026-10"
added: "2026-11-04"
category: personalization-recsys
tags: [llm-recommender, positional-bias, hypothesis-testing, rag, permutation-test, evaluation]
novelty: 4
sourced_via: "full-text fetch"
---

# Statistical Detection of Positional Bias in LLM-Based Recommender Systems: Methodologies and Empirical Evidence

**Source:** [arXiv cs.IR (Peláez-González, Herrera, Herrera-Poyatos, University of Granada)](https://arxiv.org/abs/2610.37962) · Published 2026-10 · Added 2026-11-04
**Category:** personalization-recsys · **Tags:** `llm-recommender`, `positional-bias`, `hypothesis-testing`, `rag`, `permutation-test`, `evaluation`

## TL;DR

When an LLM picks one product from a candidate list in the prompt, does the pick depend on where the item sits? The paper proposes two hypothesis tests (a chi-square test on a contingency matrix, and a permutation-based uniformity test) plus three metrics, and finds that every evaluated model rejects position independence and uniformity in a RAG product-recommendation testbed of 40,000 instances. The bias grows with candidate-set size and is not removed by lower temperature.

## 1. Business context

LLMs are increasingly used as the recommendation generator in conversational recommenders built on retrieval-augmented generation (RAG): retrieve top-k products, put them in a prompt, ask the model to recommend one. The order in which candidates appear is an arbitrary design choice, yet the paper studies whether the recommended item depends systematically on it. A position-dependent pick means exposure and sales could be shaped by prompt layout rather than relevance - a fairness and measurement problem for any team shipping such a system.

## 2. Technical details

Scope: top-1, single-turn LLM recommenders. Testbed: a real product catalog, title embeddings, cosine-distance retrieval of top-k, fixed prompt template, 2,000 template-generated user queries x 20 permutations each = 40,000 instances. Models: LLaMA 3.1 (8B, 70B), LLaMA 4 Scout, GPT-OSS (20B, 120B) and three DeepSeek R1 distills (8B, 7B, 32B). Methods: (i) POB-ICM - a contingency matrix of the position chosen vs the position of the item in the retrieval ranking, tested with chi-square independence; (ii) POB-UNBP - a sample-efficient test derived from a uniformity null model under permutation-based evaluation, designed to allow stochastic decoding with formal statistical guarantees. Metrics: permutation sensitivity (PS: probability the recommendation differs from the instance's most frequent pick across permutations, an upper bound on PB), positional bias (PB) and strong positional bias (sPB), the last counting cases where position displaces the recommendation to clearly less relevant items. Robustness sweeps vary k in {5,10,15,20} and temperature in {0.0,0.2,0.4,0.6}.

## 3. Impact — potential & realized

Realized (per the paper, one controlled testbed): both tests reject the null for all evaluated models. At k=5, PS was 15.5% for GPT-OSS 120B and 34.0% for DeepSeek R1 7B, with PB of 4.4% and 5.6% respectively (other models fall in similar ranges, e.g. PB 2.4-4.2%). PS grows monotonically with k (DeepSeek R1 7B: 34.0% at k=5 to 58.1% at k=20); sPB rises for every model; LLaMA 4 Scout's PB climbs from 2.9% to 33.8% between k=5 and k=20. The authors conclude the bias is structural and model-dependent, not an artifact of deterministic decoding or candidate-set size, and recommend routine auditing and controls such as order randomization and standardized prompting. Limits: template-generated queries, one catalog, single-turn top-1 setting; code is public.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A reusable position-bias audit for LLM recommenders

A clean statistics-flavoured audit: reorder, recount, and test against a uniformity null, with a metric (sPB) that separates harmless ties from real relevance displacement. The headline is stronger as a method than as a finding, since position sensitivity of LLMs is well known and results rest on a templated single-catalog testbed. Still, a practical recipe a DS team can run on its own LLM recommender before launch.

### Similar / related work

- [When Can You Ship on Evals Alone? Trial-Level Surrogacy for Offline Evaluation of LLM Systems](2026-11-02-arxiv-trial-level-surrogacy-ship-on-evals-alone.md) (in this bank) - another paper on whether offline LLM measurements can be trusted for decisions
- [How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of Post-hoc Calibration](2026-11-03-arxiv-ctr-recalibration-temporal-evaluation-fresh-data.md) (in this bank) - evaluation-protocol critique in a different recsys setting

### Jargon buster

- **Positional bias** — The chosen item depends on where it appears in the prompt's candidate list rather than only on its content.
- **RAG** — Retrieval-augmented generation: fetch relevant documents or items first and place them in the LLM's prompt.
- **Permutation test** — Compare an observed statistic with its distribution when labels/orders are randomly reshuffled under the null.
- **Chi-square independence test** — Tests whether two categorical variables (here chosen position and ranking position) are independent.
