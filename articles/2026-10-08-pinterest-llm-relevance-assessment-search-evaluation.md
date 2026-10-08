---
id: pinterest-llm-relevance-assessment-search-evaluation
title: "LLM-based Relevance Assessment for Web-Scale Search Evaluation at Pinterest"
source: "arXiv / Pinterest Search (Han Wang, Alex Whitworth, Pak Ming Cheung, Zhenjie Zhang, Krishna Kamath)"
url: "https://arxiv.org/abs/2509.03764"
published: "2025-09"
added: "2026-10-08"
category: search-ranking
tags: [llm-as-judge, relevance-evaluation, minimum-detectable-effect, stratified-sampling, online-experiments, pinterest]
novelty: 3
sourced_via: "full-text fetch"
---

# LLM-based Relevance Assessment for Web-Scale Search Evaluation at Pinterest

**Source:** [arXiv / Pinterest Search (Han Wang, Alex Whitworth, Pak Ming Cheung, Zhenjie Zhang, Krishna Kamath)](https://arxiv.org/abs/2509.03764) · Published 2025-09 · Added 2026-10-08
**Category:** search-ranking · **Tags:** `llm-as-judge`, `relevance-evaluation`, `minimum-detectable-effect`, `stratified-sampling`, `online-experiments`, `pinterest`

## TL;DR

Pinterest replaces slow human relevance labelling in search A/B tests with a fine-tuned multilingual cross-encoder judge, then pairs it with stratified, Neyman-allocated query sampling to shrink the minimum detectable effect from roughly 1.3-1.5% to 0.25% or less.

## 1. Business context

Search relevance in experiments is traditionally measured by human annotators, which is expensive and slow and limits how many queries and experiences can be assessed. Small query samples mean noisy readouts and large minimum detectable effects (MDE), so teams cannot detect modest relevance changes.

## 2. Technical details

Judge model: a fine-tuned XLM-RoBERTa-large cross-encoder, chosen after comparing mBERT, T5-base, mDeBERTaV3-base and Llama-3-8B (Llama was slightly more accurate but about 6x costlier at inference). Trained on about 2.6 million human-annotated query-Pin pairs with pointwise cross-entropy over a 5-point scale (L1 highly irrelevant to L5 highly relevant). Inputs are text-only: Pin titles/descriptions, BLIP image captions, linked page text, board titles and engaged queries. Runs on one A10G, ~150k rows in ~30 minutes. Metric: sDCG@25. Sampling: paired control/treatment query samples, strata from query interest (in-house DistilBERT) x popularity, with Neyman optimal allocation. Agreement with humans (US): 73.7% exact, 91.7% within one level, Kendall tau 0.652, Spearman 0.817; query-level sDCG error mean 0.005. France/Germany are weaker (tau about 0.47).

## 3. Impact — potential & realized

Realized (authors' estimates): MDE falls from about 1.3-1.5% to at most 0.25%; stratification cut the standard deviation by 52% at n=2000 and 67% at n=5000 versus simple random sampling, so most of the gain is variance reduction rather than sample size. Cheap labels also allow bigger query sets and more experiences per experiment. Limits: weaker non-English agreement, text-only features (vision-language judges are future work), and human labels are still used when an experiment changes the relevance model itself, to avoid bias. Figures are Pinterest's own setup.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Good measurement engineering: the sampling design does more than the LLM.

The LLM judge is a fairly standard fine-tuned encoder; the DS-relevant insight is that cheap labels let you redesign the sampling (paired queries, stratification, Neyman allocation), and that is where the MDE reduction comes from. Anyone with a search A/B programme can copy this. The unaddressed risk is judge bias when the treatment changes the very model family the judge resembles, which Pinterest handles by keeping humans in that case.

### Similar / related work

- [**Pinterest metric-movement root-cause analysis**](2026-08-31-pinterest-metric-movements-root-cause-analysis.md) (in this bank) — same team's measurement-side thinking
- [**Trustworthy Method Comparison with AI Judges**](2026-10-07-arxiv-trustworthy-method-comparison-ai-judges.md) (in this bank) — statistical design for judge-based evaluation

### Jargon buster

- **MDE (minimum detectable effect)** — The smallest true change an experiment can reliably detect at its sample size and variance.
- **Neyman allocation** — Allocating samples across strata in proportion to stratum size times standard deviation, minimising estimator variance.
- **sDCG@K** — A nDCG variant that assumes unlimited top-grade documents, scoring ranked relevance up to rank K.
