---
id: linkedin-feed-llm-retrieval-gr-ranking
title: "Engineering the Next Generation of LinkedIn's Feed"
source: "LinkedIn Engineering Blog"
url: "https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed"
published: "2026-03"
added: "2026-09-03"
category: search-ranking
tags: [generative-recommender, dual-encoder-retrieval, feed-ranking, llm-embeddings, sequential-modeling]
novelty: 4
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Engineering the Next Generation of LinkedIn's Feed

**Source:** [LinkedIn Engineering Blog](https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed) · Published 2026-03 · Added 2026-09-03
**Category:** Search & Ranking · **Tags:** `generative-recommender`, `dual-encoder-retrieval`, `feed-ranking`, `llm-embeddings`, `sequential-modeling`

## TL;DR

LinkedIn rebuilt its Feed around two unifying pillars — an LLM-powered dual-encoder retrieval layer that replaces several separate candidate sources, and a Generative Recommender (GR) ranking transformer that models a member's sequence of 1,000+ historical interactions with causal attention instead of scoring candidates one at a time — with fixes like percentile-bucketed engagement tokens delivering a 30x correlation improvement and +15% recall@10.

## 1. Business context

LinkedIn's Feed serves over 1.3 billion professionals and has to balance three competing pulls: a member's immediate network, the accounts they follow, and broader content from LinkedIn's wider "Economic Graph." The prior architecture relied on multiple separate candidate-retrieval sources (trending, collaborative filtering, embedding-based) that had grown independently, and pointwise ranking that scored each candidate in isolation rather than reasoning over a member's actual sequence of engagement over time. LinkedIn set out to unify retrieval and move ranking to a sequential, generative-recommender paradigm.

## 2. Technical details

- **Unified LLM-based retrieval:** fine-tuned LLM embeddings replace the separate trending, collaborative-filtering, and embedding-based retrieval sources with a single dual-encoder system, which also improves cold-start via profile-only inference for members with little engagement history.
- **Engagement-signal tokenization:** raw engagement metrics had near-zero correlation with embedding similarity (-0.004); converting them to percentile buckets wrapped in special tokens produced a 30x correlation improvement and a +15% recall@10 gain — a significant fix given the metric was essentially uninformative beforehand.
- **Hard-negative mining:** adding 2 hard negatives per member during training improved recall@10 by a further +3.6%.
- **Positives-only training:** restructuring training to use positives-only examples cut memory usage by 37% and sped up training by 2.6x.
- **Generative Recommender (GR) ranking model:** a causal-attention transformer over each member's interaction sequence, paired with a late-fusion Mixture-of-Experts (MMoE) head for multi-objective ranking, replacing pointwise scoring.
- **Custom Flash-Attention variant ("GRMIS"):** a specialized attention kernel delivering 2x speedup versus standard PyTorch scaled-dot-product attention.
- **Serving infrastructure:** a custom C++ data loader, custom CUDA kernels for multi-label AUC computation, disaggregated CPU-feature/GPU-inference serving, and shared-context batching, targeting sub-50ms retrieval and sub-second end-to-end ranking.

## 3. Impact — potential & realized

- **Realized:** 30x correlation improvement from engagement-signal tokenization; +15% recall@10 from that same fix; +3.6% recall@10 from hard-negative mining; 37% memory reduction and 2.6x faster training from positives-only training; 2x attention speedup from the custom GRMIS kernel; sub-50ms retrieval and sub-second end-to-end ranking latency targets met in production.
- **Potential:** a template for unifying fragmented multi-source retrieval into a single LLM-embedding-based system, and for migrating large-scale feed ranking from pointwise scoring to sequence-aware generative recommenders — directly relevant to any feed/recsys team still running several independent candidate sources.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a comprehensive, well-quantified generative-recommender migration at real scale

This is one of the more thoroughly instrumented accounts of moving a large-scale industrial feed from pointwise ranking to a sequence-aware generative recommender, and the specific fixes are unusually concrete and diagnostic — the -0.004-to-30x correlation jump from percentile-bucketing engagement signals is a genuinely instructive lesson about how raw metrics can silently fail to inform embedding similarity. It's a 4 rather than a 5 because the core paradigm (causal-attention sequential ranking, unified dual-encoder retrieval) follows the same generative-recommender direction other companies (Netflix, Meta, Shopify) are independently converging on around the same period; LinkedIn's contribution is a rigorous, well-executed production instance of that direction rather than a new one.

### Similar / related work

- [**The Generative Recommender Behind Shopify's Commerce Engine**](2026-09-03-shopify-generative-recommender-hstu.md) (in this bank) — a parallel move to sequence-based generative recommendation (HSTU architecture) at another large-scale commerce platform, with a similar emphasis on negative-sampling as a scaling lever.
- [**Towards Generalizable and Efficient Large-Scale Generative Recommenders**](https://arxiv.org/abs/2605.23312) — Netflix's research on the same generative-recommender paradigm this Feed rearchitecture is an industrial instance of.
- [**How Generative Recommenders Are Redefining RecSys at Scale**](2026-08-26-nvidia-generative-recommenders-recsys-scale.md) (in this bank) — an infrastructure-focused survey of the same broader shift from pointwise to generative, sequence-based recommendation this article implements.

### Jargon buster

- **Dual-encoder retrieval** — a retrieval architecture that embeds queries (here, a member) and candidates (content/connections) into the same vector space separately, then finds matches via nearest-neighbor search — fast enough to run over huge candidate pools.
- **Generative Recommender (GR)** — a ranking approach that models a user's interaction history as a sequence and predicts the next relevant item with causal (autoregressive-style) attention, rather than scoring each candidate independently.
- **Hard negative** — a training example that is similar to a positive example but is actually irrelevant/negative, used to sharpen a model's decision boundary more than random negatives would.
- **Mixture-of-Experts (MoE) head** — a model output layer composed of multiple specialized sub-networks ("experts") whose outputs are combined, often used to balance several ranking objectives at once.
