---
id: linkedin-follows-llm-semantic-retrieval-ranking
title: "Rebuilding LinkedIn's Follows Recommendations with LLM-Based Semantic Retrieval and Ranking"
source: "LinkedIn Engineering Blog"
url: "https://www.linkedin.com/blog/engineering/ai/rebuilding-linkedins-follows-recommendations-with-llm-based-semantic-retrieval-and-ranking"
published: "2026-08"
added: "2026-09-05"
category: personalization-recsys
tags: [llm-embeddings, bi-encoder, cold-start, lora, faiss, semantic-retrieval, contrastive-learning]
novelty: 4
sourced_via: "full-text fetch"
---

# Rebuilding LinkedIn's Follows Recommendations with LLM-Based Semantic Retrieval and Ranking

**Source:** [LinkedIn Engineering Blog](https://www.linkedin.com/blog/engineering/ai/rebuilding-linkedins-follows-recommendations-with-llm-based-semantic-retrieval-and-ranking) · Published 2026-08 · Added 2026-09-05
**Category:** Personalization & Recommender Systems · **Tags:** `llm-embeddings`, `bi-encoder`, `cold-start`, `lora`, `faiss`, `semantic-retrieval`, `contrastive-learning`

## TL;DR

LinkedIn rebuilt creator recommendations for the MyNetwork tab and Home Feed around a single LLM-based bi-encoder that turns member and creator profiles into a shared embedding space via "narrative prompting," replacing a popularity-skewed system that especially failed new members with no activity history.

## 1. Business context

The prior recommendation system for "who to follow" overlooked strong but unpopular matches and leaned on activity signals that simply don't exist for new members. That's a meaningful cold-start problem for LinkedIn: the members who most need good creator recommendations to seed an engaging feed are exactly the ones the old, popularity-biased system served worst. The goal of the rebuild was to match members to creators on genuine relevance — the substance of a profile — rather than on how many other people already followed a given creator.

## 2. Technical details

Instead of embedding raw profile fields directly, the system first converts semi-structured profile attributes (bios, headlines, skills, experience) into natural-language prompts — an approach the team calls **Narrative Prompting**, chosen over templated field-concatenation because it "naturally handles missing fields, preserve[s] nuanced semantics, align[s] with LLM pretraining."

- **Encoder.** A mid-size, instruction-tuned encoder is fine-tuned specifically on the follow-prediction task using supervised contrastive learning in a bi-encoder architecture (members and creators encoded into the same space, compared by similarity).
- **Efficient fine-tuning.** Training uses LoRA (Low-Rank Adaptation) to keep the fine-tuning parameter-efficient, mixed-precision (16-bit/32-bit) training, and gradient checkpointing to manage memory at LinkedIn's scale.
- **Offline retrieval pipeline.** Ray drives distributed GPU inference across hundreds of millions of profiles; the resulting creator embeddings are indexed with FAISS for exact k-nearest-neighbor retrieval.
- **Online retrieval pipeline.** The encoder is deployed to Proxima, LinkedIn's model-serving infrastructure, to compute a member's embedding in real time during onboarding, which is then matched against a hosted vector search service.
- **Dual-purpose embeddings for ranking.** The same embeddings feed both candidate retrieval and downstream ranking as features. To make the high-dimensional (4,096-d) embeddings practical as ranking features, the team applies "task-aware supervised projection" — two lightweight feedforward layers that compress embeddings down to 64–128 dimensions while preserving follow-prediction alignment.

The team calls out two concrete next steps: enriching the narrative prompts with recent engagement signals (not just static profile fields), and adopting more expressive matching such as ColBERT-style fine-grained token-level comparison instead of single-vector similarity.

## 3. Impact — potential & realized

**Realized:** production A/B tests showed statistically significant lifts in follow rate across member segments, with the largest gains for new members, who the post says now receive relevant matches "from their first session" instead of sparse, popularity-based suggestions. No specific percentage lift is disclosed.

**Potential:** placing members and creators in one shared, LLM-derived embedding space is a template that generalizes past "who to follow" to any two-sided cold-start matching problem (job-to-candidate, product-to-buyer) where one side of the match has thin behavioral history but rich profile text to draw on instead.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A clean, well-motivated production application of LLM bi-encoders to cold-start matching

Using an LLM encoder plus contrastive learning for retrieval isn't new in the abstract, but "narrative prompting" as a specific, deliberate answer to the missing-field problem in semi-structured profile data is a nice, transferable engineering choice, and the task-aware projection trick (reusing one 4,096-d embedding for both ANN retrieval and a compact ranking feature) is the kind of practical efficiency detail that's easy to overlook and worth copying. It doesn't reach field-shifting territory because the overall retrieval-then-rank architecture is standard, but the specific choices here are genuinely well-reasoned.

### Similar / related work

- [**Matching LinkedIn Members with the Right Premium Products**](../articles/2026-09-02-linkedin-premium-product-two-tower-bandits.md) (in this bank) — another LinkedIn personalization system built on two-tower-style matching, useful contrast between bandit-driven product matching and this post's pure embedding retrieval.
- [**Engineering the Next Generation of LinkedIn's Feed**](../articles/2026-09-03-linkedin-feed-llm-retrieval-gr-ranking.md) (in this bank) — LinkedIn's other recent LLM-embedding-based retrieval system, this time for feed ranking rather than follow recommendations; the two posts share the dual-encoder-retrieval-plus-ranking pattern.
- [**Home Embeddings for Similar Home Recommendations**](../articles/2026-09-04-zillow-home-embeddings-similar-homes.md) (in this bank) — a different domain solving the same structural problem: using embeddings to handle cold-start similarity matching when behavioral signal is thin.

### Jargon buster

- **Bi-encoder** — an architecture with two separate encoders (here, one effectively shared/aligned encoder for both members and creators) that map each side of a match into the same vector space, so similarity can be computed with a fast dot product rather than a slower cross-attention model.
- **LoRA (Low-Rank Adaptation)** — a parameter-efficient fine-tuning technique that trains small low-rank update matrices instead of all of a model's weights, cutting the compute and memory needed to adapt a large pretrained encoder to a new task.
