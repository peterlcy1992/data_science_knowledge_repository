---
id: shopify-sid-llm-generative-search-recommendation
title: "Generative Search and Recommendation at Shopify"
source: "arXiv cs.IR (Shopify: Kangaspunta, Hajji, Fofadiya et al.)"
url: "https://arxiv.org/abs/2611.08804"
published: "2026-11"
added: "2026-11-12"
category: personalization-recsys
tags: [semantic-ids, generative-retrieval, multi-token-prediction, incremental-pool-recall, LLM-judge, distillation, online-ab-test]
novelty: 4
sourced_via: "full-text fetch"
---

# Generative Search and Recommendation at Shopify

**Source:** [arXiv cs.IR (Shopify: Kangaspunta, Hajji, Fofadiya et al.)](https://arxiv.org/abs/2611.08804) · Published 2026-11 · Added 2026-11-12
**Category:** personalization-recsys · **Tags:** `semantic-ids`, `generative-retrieval`, `multi-token-prediction`, `incremental-pool-recall`, `LLM-judge`, `distillation`, `online-ab-test`

## TL;DR

Shopify's SID-LLM casts both product search and recommendation as generating short semantic IDs (three RQ-KMeans codewords per product) from an LLM jointly pre-trained on catalog and behavioural data. On its own it gets close to Shopify's whole multi-model search stack; added to the stacks it lifts judged search relevance and, in a home-feed A/B test, attributed orders by 7.95%. The paper is unusually careful about how it measures what a retriever adds.

## 1. Business context

Shopify serves search through the Catalog API, merchant storefronts and the Shop app, and recommendations on the Shop app home feed and ads, over a multi-merchant catalog of billions of products with eligibility that depends on context such as the buyer's market. Both need to retrieve relevant candidates under latency budgets of tens of milliseconds.

The prior state is the usual industrial split: two-tower retrievers and lexical/dense search, each compressing the buyer or query into a fixed vector before scoring candidates, plus a separate HSTU-style generative recommender over item IDs. The bet is that one LLM generating content-derived product IDs can give search and recommendation a shared representation and training objective, while a catalog index keeps generation restricted to eligible products.

## 2. Technical details

**Tokenization.** Each product's 768-dim in-house search embedding is quantized by RQ-KMeans into three codewords (a semantic ID, SID); codebooks are fit on the top 25M products by GMV, which gave higher downstream relevance than random sampling. A 32768-8192-8192 tokenizer scored higher than 8192-8192-8192, but the latter was chosen for p95-latency headroom. SIDs are shared: 78.9% of predicted SIDs cover more than one product.

**Backbones and decoding.** Ablations over LFM2-2.6B and Qwen3-1.7B/4B/14B-Base: the Qwen3 models improved average quality at higher latency, and LFM2-2.6B (lowest p95 latency) is deployed. New SID tokens get an embedding-alignment stage (only new embeddings trained) before full continued pre-training on a catalog/search/recommendation data mix; general-domain replay hurt the 2.6B model and was roughly neutral for 14B. Autoregressive (AR) decoding needs one backbone pass per codeword; multi-token prediction (MTP) predicts all three codeword distributions in one prefill, roughly halving median server-side latency but scoring below AR. Re-scoring MTP's 250 candidates with a lightweight ranker distilled from a Qwen3.5-9B relevance judge more than recovers the gap, so search serves MTP + ranker; recommendation serves AR with a parameter-free *joint-probability* SID-to-product decode (log p(SID|user) + log of within-cluster popularity share), which raised Recall@50 by 15.8% over one product per SID.

**Post-training.** Search quality is improved with judge-scored supervision (soft-target CE, CE+DPO, and on-policy feedback); the abstract says reinforcement learning further improves judged search relevance. Routed multi-teacher distillation from task experts into a unified student improved Recall@50 by 1.76% and discovery Recall@50 by 10.03% over joint SFT without a statistically detected loss in search quality — but the unified student remains experimental; production uses task-specific models.

**Measurement.** Search is scored with OneDCG@10, a DCG whose gain combines an LLM judge's 0–3 relevance grade (query + buyer profile) with a static quality score, normalized by a constant rather than each query's ideal DCG so scores are comparable across queries. Because judge, query set, index and inference code changed during the project, each table names a fixed 'evaluation protocol' and absolute scores are compared only within a table. Recommendation retrieval is judged by *incremental pool recall*: drop one generator from the union of all generators' top-200 candidates and measure how much recall of next-week orders falls.

## 3. Impact — potential & realized

**Realized (as reported).** Search-stack ablation (protocol E6): removing SID-LLM lowers OneDCG@10 by 6.5% (7.7% on personalized search); SID-LLM alone, with its own ranker, is 12.8% below the full stack (5.9% on personalized). Successive versions were A/B tested in search on purchases, high-quality clicks and clicks by head/torso/tail query segment, and the results 'supported deploying' it (no lift numbers given for search). In the recommendation candidate pool (70,747 users with a purchase in the held-out week), SID-LLM has Recall@50 of 24.61% vs 17.28% for recent-engagement and 17.21% for HSTU, and incremental pool recall of 2.65 points — 61% more than the next-best generator (1.64). A home-feed A/B test raised attributed orders by 7.95%, converting users by 8.60% and conversion rate by 9.85% on the impacted surface, all significant after Dunnett correction.

**Potential.** The authors expect product search to move 'more and more towards a single model' and plan in-session personalization, related-product recommendation, test-time chain-of-thought and multimodal inputs.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A strong production report on semantic-ID generative retrieval, made more useful to data scientists by how it measures a retriever's marginal contribution.

Semantic-ID generative retrieval is no longer new (Spotify, WeChat, Tmall and others are already in this bank), so the novelty is in the production engineering and, above all, the measurement. Two practices are worth copying regardless of model choice: *incremental pool recall* (a leave-one-generator-out ablation that measures what a retriever uniquely adds to the candidate pool, rather than its standalone recall), and naming a fixed evaluation protocol per table because the LLM judge, query set and index drifted over the project. The OneDCG constant normalizer is a deliberate trade: it makes scores comparable across queries but bakes the static popularity/brand score into 'relevance', so it partly rewards popularity. Caveats: search online lifts aren't quantified, the unified search+recs model is still experimental, and the home-feed result is on the 'impacted surface' only.

### Similar / related work

- [**Deploying Semantic ID-based Generative Retrieval for Large-Scale Podcast Discovery at Spotify**](2026-08-30-spotify-semantic-id-generative-retrieval-podcasts.md) — in this bank: cited by the authors; the closest production SID-retrieval precedent
- [**The Generative Recommender Behind Shopify's Commerce Engine**](2026-09-03-shopify-generative-recommender-hstu.md) — in this bank: Shopify's earlier HSTU-style generative recommender, which SID-LLM outperforms on incremental pool recall
- [**WeGR: Unified Generative Retrieval for Industrial Search Systems in WeChat**](2026-10-15-arxiv-wegr-generative-retrieval-wechat-search.md) — in this bank: another industrial unified generative-retrieval system for search
- [**Recommender Systems with Generative Retrieval (TIGER)**](https://arxiv.org/abs/2305.05065) — the semantic-ID generative retrieval paper this line of work builds on

### Jargon buster

- **Semantic ID (SID)** — A short sequence of discrete tokens derived by quantizing a product's content embedding, so similar products share prefixes.
- **RQ-KMeans** — Residual quantization with k-means: each level clusters what the previous levels failed to explain.
- **Multi-token prediction (MTP)** — Predicting all codewords of an ID in one forward pass instead of one at a time — faster, but ignores dependence between codewords.
- **Incremental pool recall** — How much the union of all retrievers' candidates loses in recall of real purchases when one retriever is removed.
- **Dunnett correction** — A multiple-comparison adjustment for comparing several treatment arms against one shared control.
