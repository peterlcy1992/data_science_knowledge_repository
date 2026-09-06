---
id: linkedin-jude-llm-job-recommendations
title: "JUDE: LLM-Based Representation Learning for LinkedIn Job Recommendations"
source: "LinkedIn Engineering Blog"
url: "https://www.linkedin.com/blog/engineering/ai/jude-llm-based-representation-learning-for-linkedin-job-recommendations"
published: "2025-05"
added: "2026-09-06"
category: personalization-recsys
tags: [llm-embeddings, two-tower, lora, job-recommendations, multi-task-learning, contrastive-learning, deepspeed]
novelty: 4
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# JUDE: LLM-Based Representation Learning for LinkedIn Job Recommendations

**Source:** [LinkedIn Engineering Blog](https://www.linkedin.com/blog/engineering/ai/jude-llm-based-representation-learning-for-linkedin-job-recommendations) · Published 2025-05 · Added 2026-09-06
**Category:** Personalization & Recommender Systems · **Tags:** `llm-embeddings`, `two-tower`, `lora`, `job-recommendations`, `multi-task-learning`, `contrastive-learning`, `deepspeed`

## TL;DR

LinkedIn replaced hand-tuned smaller ML models and brittle taxonomies with JUDE, a two-tower architecture built on LoRA-fine-tuned LLM embeddings of jobs and members, and shipped what the team calls the largest single-model metric improvement its talent-recommendations org had seen in half a year: +2.07% qualified applications and +1.91% total applications, with a 5.13% drop in the dismiss-to-apply ratio.

## 1. Business context

LinkedIn's job-recommendation system serves over a billion members against tens of millions of active job postings, and previously leaned on standardized features and smaller, imprecise ML models layered on top of hard-to-maintain manual taxonomies (skills, titles, seniority levels) to represent both jobs and candidates. Taxonomies are inherently lossy and expensive to keep current as job titles and skill vocabularies evolve; the team wanted representations that captured the actual semantic content of a job description or a member's profile and resume, at real-time responsiveness for a billion-member, tens-of-millions-of-postings scale.

## 2. Technical details

JUDE uses a two-tower architecture where both towers are derived from a shared base LLM via parameter-efficient fine-tuning — LoRA (Low-Rank Adaptation) applied specifically to the Query-Key-Value matrices inside the Transformer's attention blocks, rather than fine-tuning the full model. Each tower uses specialized prompt templates depending on the input type (job description, member profile, or resume), letting the same base LLM produce meaningfully different embeddings for different entity types. On top of the LLM embeddings sit deliberately lightweight layers designed for minimal additional feature interaction, so that the heavy semantic lifting stays with the fine-tuned LLM rather than a downstream MLP.

The team explored both encoder-decoder and decoder-only base architectures, and tested mean-pooling versus last-token pooling to collapse token-level representations into a single embedding vector. Training combined three loss functions: binary cross-entropy for a direct classification signal, contrastive InfoNCE loss to shape the embedding space for retrieval, and a VP-matrix loss specifically to improve robustness to outliers. Supervision mixed two label types — "relevance" labels (human-annotated or LLM-evaluated for semantic fit) and "engagement" labels (actual job applications), so the model is trained to align with both semantic quality and real business outcomes rather than either alone.

At training-infrastructure scale, the team used Flash Attention 2, custom CUDA kernels, bfloat16 mixed precision, gradient accumulation, and gradient checkpointing for memory efficiency, on a multi-node, multi-GPU H100 cluster with DeepSpeed's optimizer-state partitioning (ZeRO-style sharding) for distributed training. In serving, an intelligent change-detection mechanism (only recomputing embeddings when the underlying job or profile has meaningfully changed) reduced inference volume by roughly 6x, keeping nearline inference latency under 300ms at the p95 percentile.

## 3. Impact — potential & realized

**Realized:** In production A/B testing, JUDE delivered +2.07% qualified applications, +1.91% total job applications, and a 5.13% reduction in the dismiss-to-apply ratio (fewer jobs get dismissed relative to how many get applied to, indicating better relevance). LinkedIn's own framing: this was the largest metric improvement from a single model change that the team supporting talent initiatives had observed in that half-year period.

**Potential:** The 6x inference-volume reduction via change detection is a broadly reusable pattern for any large-scale embedding-serving system where the underlying entities (profiles, listings, documents) change far less often than they're queried — recomputing on change rather than on a fixed schedule or every request can be a large, mostly-free cost win.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A strong, well-engineered production LLM-embedding system

LLM-based two-tower retrieval is now a fairly common pattern (see LinkedIn's own Follows recommendations work below), so the core idea isn't new. What elevates this is the training-loss design (three losses combined for both semantic quality and business alignment) and the serving-side change-detection optimization, both of which are the kind of detail that separates "we fine-tuned an LLM for embeddings" from a system that actually survives production traffic and cost constraints at LinkedIn's scale.

### Similar / related work

- [**Rebuilding LinkedIn's Follows Recommendations with LLM-Based Semantic Retrieval and Ranking**](2026-09-05-linkedin-follows-llm-semantic-retrieval-ranking.md) (in this bank) — the same company applying a very similar LLM-embedding-plus-bi-encoder recipe to a different recommendation surface (follows vs. jobs), useful for comparing architectural choices side by side.
- [**Matching LinkedIn Members with the Right Premium Products**](2026-09-02-linkedin-premium-product-two-tower-bandits.md) (in this bank) — an earlier, non-LLM two-tower approach at LinkedIn, useful context for how far the embedding backbone has evolved.
- **Towards Deep and Representation Learning for Talent Search at LinkedIn** — [arXiv 1809.06473](https://arxiv.org/abs/1809.06473) — LinkedIn's earlier (pre-LLM) representation-learning work for talent search, the conceptual predecessor to JUDE.

### Jargon buster

- **LoRA (Low-Rank Adaptation)** — a parameter-efficient fine-tuning technique that freezes most of a pretrained model's weights and injects small trainable low-rank matrices into specific layers (here, the attention block's Query/Key/Value projections), drastically cutting the number of trainable parameters and the compute needed to fine-tune.
- **InfoNCE loss** — a contrastive loss function that trains embeddings so that matching pairs (e.g., a member and a job they applied to) are pulled close together in embedding space while non-matching pairs are pushed apart, commonly used to train retrieval systems.
- **ZeRO / optimizer-state partitioning (DeepSpeed)** — a distributed-training technique that shards optimizer state, gradients, and/or model parameters across multiple GPUs instead of replicating them fully on each one, enabling training of much larger models within fixed GPU memory.
