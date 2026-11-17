---
id: arxiv-label-free-verbosity-bias-llm-recommenders-randomized-paraphrasing
title: "Label-Free Detection of Structural Bias in LLM-Based Recommender Systems via Randomized Paraphrasing: The Case of Verbosity"
source: "University of Granada / DaSCI (arXiv cs.IR)"
url: "https://arxiv.org/abs/2611.18878"
published: "2026-11"
added: "2026-11-17"
category: personalization-recsys
tags: [llm-recommenders, verbosity-bias, structural-bias, randomization-test, label-free-audit, conditional-logit, paraphrasing, black-box-audit, e-commerce]
novelty: 4
sourced_via: "full-text fetch"
---

# Label-Free Detection of Structural Bias in LLM-Based Recommender Systems via Randomized Paraphrasing: The Case of Verbosity

**Source:** [University of Granada / DaSCI (arXiv cs.IR)](https://arxiv.org/abs/2611.18878) · Published 2026-11 · Added 2026-11-17
**Category:** Personalization & Recommender Systems · **Tags:** `llm-recommenders`, `verbosity-bias`, `structural-bias`, `randomization-test`, `label-free-audit`, `conditional-logit`, `paraphrasing`, `black-box-audit`, `e-commerce`

## TL;DR

A way to audit an LLM shopping recommender for "structural" bias without any relevance labels: rewrite each retrieved product description with a randomly assigned paraphrasing model, shuffle the order, and check whether the recommender picks every paraphraser equally often — which a paraphrase-invariant recommender must do, by design. Applied to 20,000 queries and nine LLM recommenders, description length had a positive effect on selection in all nine after controlling for measured relevance, raising the odds of selection by up to 38% per standard deviation of length; relevance stayed the primary driver.

## 1. Business context

LLMs increasingly act as the recommender in e-commerce and conversational shopping: given a query and *k* retrieved candidates described in text, pick one product. That choice should depend on relevance, but may also respond to surface properties such as how long a description is. Operators routinely swap the model, edit the prompt or ingest new catalog content, and each change can silently shift what gets recommended. Standard offline evaluation would need relevance judgments for every query–product pair, which are expensive, rarely available for live catalogs and quickly stale. Where third-party sellers write descriptions, an undetected length preference also distorts competition between sellers and rewards writing for the recommender rather than for customers; the authors also point to emerging regulation requiring transparency and risk assessment of recommenders on large platforms.

## 2. Technical details

- **Design-based guarantee (Proposition 1).** Each retrieved product is rewritten by a paraphraser chosen by a uniformly random permutation, and the candidates are shown in random order. If the recommender is invariant to paraphrasing (and the paraphrasers preserve meaning), every paraphraser is selected with probability 1/*k* — no relevance labels needed. The converse doesn't hold: biases that cancel across paraphrasers can still give a uniform distribution, so uniformity is necessary but not sufficient for absence of bias.
- **Four-step pipeline.** (1) χ² test of uniform paraphraser selection; (2) a conditional-logit model over each query's candidates, decomposing selection into *solo* and *unique* R² contributions of length (φ_LEN) and semantic/relevance proxies; (3) direction and size of each coefficient; (4) a conditional analysis of conflicting signals — comparing the original description against a paraphrase when length and relevance point the same or opposite ways.
- **Controls.** Three proxies for semantic shift and relevance: cosine similarity between original and paraphrase (BAAI/bge-small-en-v1.5), query–description embedding similarity (same model), and a cross-encoder relevance score (cross-encoder/ms-marco-MiniLM-L6-v2).
- **Setup.** 20,000 sampled queries over 50,000 products from the Amazon ML Challenge 2023 catalog; top-*k*=5 retrieved with bge-small embeddings. Paraphrasers: DeepSeek-R1 7B (Qwen), GPT-OSS 20B, Gemma-3 12B, Falcon-3 7B, plus an identity "paraphraser" (original text). Nine recommenders at temperature 0: DeepSeek-R1 7B (Qwen) and 8B (Llama), Falcon-3 10B and 7B, GPT-OSS 120B and 20B, Gemma-3 12B and 27B, Llama-3.1 8B.
- **Audit cost.** *N* queries need exactly *N* recommender calls and at most *N(k−1)* paraphraser calls; paraphrases are reused across recommenders, so auditing a new model or prompt costs only *N* recommender calls.

## 3. Impact — potential & realized

**Measured:**
- Seven of nine recommenders depart significantly from uniform paraphraser selection (p<0.05); the two exceptions are the GPT-OSS models. Largest deviations (DeepSeek-R1 7B and Falcon-3 7B) reach ±1.3 percentage points. The pattern does not support a self-preference explanation (e.g. both DeepSeek-R1 recommenders avoid the DeepSeek-R1 paraphraser).
- Length has a positive *unique* contribution in all nine models after controlling for relevance and similarity proxies: unique R² from 0.28% (GPT-OSS 120B) to 2.25% (DeepSeek-R1 7B Qwen); solo (standardized) length coefficients from +0.167 to +0.351, and coefficients controlling for all other features from +0.117 (GPT-OSS 120B, ≈12% higher odds of selection per SD of length) to +0.322 (DeepSeek-R1 7B Qwen, ≈38%). Controlling for relevance attenuates the length coefficient most for the GPT-OSS models (30.2% and 24.2%) and least for the DeepSeek-R1 distillations (8.2% and 9.9%).
- Relevance (cross-encoder) is the strongest feature (solo R² 5.99–8.72%). When length and relevance conflict, the more relevant description still wins, but the preference gap is on average less than half that seen when both signals agree; GPT-OSS models are the least length-sensitive, the DeepSeek-R1 distillations the most.
- Power guidance: ~110 (most sensitive model) to ~900 (least sensitive) queries for 80% power on the length effect; 8,000–10,000 queries to detect global non-uniformity for the most biased models and ~19,000 for Gemma-3 27B (indicative, treating estimates as true).

**Potential:** a routine, black-box regression test for deployed shopping assistants whenever the model, prompt or catalog changes; new features (sentiment, brand mentions, formatting) can be added as extractors and re-analysed on the same paraphrased data at no extra inference cost. Code is public.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Randomization inference applied to the LLM itself

The clever bit is moving the randomization from users to *inputs*: by randomly assigning who rewrites what, the authors get a design-based null that needs no relevance labels — the same logic as an A/A test. That makes this a data-science contribution as much as a recsys one, and it's directly reusable for any LLM-as-ranker or LLM-as-judge pipeline. Caveats worth keeping in mind: the "relevance controls" are small proxy models, so the unique length effect is "beyond the measured relevance signals", not beyond true relevance (the authors say so), and effect sizes are modest in R² terms even if consistent.

### Similar / related work

- [**Statistical Detection of Positional Bias in LLM-Based Recommender Systems**](2026-11-04-arxiv-statistical-detection-positional-bias-llm-recommender.md) (in this bank) — the positional-bias counterpart; this paper extends the statistical-audit approach to verbosity.
- [**Trustworthy Method Comparison with AI Judges**](2026-10-07-arxiv-trustworthy-method-comparison-ai-judges.md) (in this bank) — design and estimation under order and batch effects for LLM evaluators.
- [**Lost in the Middle: How Language Models Use Long Contexts**](https://arxiv.org/abs/2307.03172) (Liu et al.) — the primacy/recency findings that motivate randomizing prompt position.

### Jargon buster

- **Structural bias** — a model's preference driven by how inputs are presented (order, length, wording) rather than what they mean.
- **Verbosity bias** — preferring longer or more elaborate text independent of its relevance.
- **Conditional logit** — a choice model that compares only the options shown in the same query, estimating how each feature shifts the odds of being chosen.
- **Unique R²** — the drop in explained variation when one feature is removed from the full model; what that feature explains that the others don't.
