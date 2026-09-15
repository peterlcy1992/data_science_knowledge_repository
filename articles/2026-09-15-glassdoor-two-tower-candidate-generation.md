---
id: glassdoor-two-tower-candidate-generation
title: "Improving Embedding-Based Candidate Generation for Recommender Systems with a Two-Tower Model"
source: "Glassdoor Engineering Blog"
url: "https://medium.com/glassdoor-engineering/improving-embedding-based-candidate-generation-for-recommender-systems-with-a-two-tower-model-c222123beb7f"
published: "2026-03"
added: "2026-09-15"
category: personalization-recsys
tags: [two-tower, candidate-generation, embeddings, feed-ranking, community]
novelty: 2
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Improving Embedding-Based Candidate Generation for Recommender Systems with a Two-Tower Model

**Source:** [Glassdoor Engineering Blog](https://medium.com/glassdoor-engineering/improving-embedding-based-candidate-generation-for-recommender-systems-with-a-two-tower-model-c222123beb7f) · Published 2026-03 · Added 2026-09-15
**Category:** Personalization & Recommender Systems · **Tags:** `two-tower`, `candidate-generation`, `embeddings`, `feed-ranking`

## TL;DR

Glassdoor's community feed recommender replaced pretrained, off-the-shelf sentence embeddings in its candidate-generation stage with a Two-Tower Neural Network trained directly on real user-post interaction data — moving retrieval quality from "embeddings that happen to be semantically reasonable" to "embeddings optimized for the actual prediction task." The change delivered 40–60% relative offline retrieval-quality gains and a statistically significant lift in community engagement in production.

## 1. Business context

Glassdoor's feed recommender is a multi-stage system, and candidate generation — retrieving an initial pool of plausibly relevant posts from a very large pool spanning many different feeds — sets a ceiling on how good downstream ranking can ever be, since ranking can only reorder what candidate generation surfaces. The prior approach used pretrained, out-of-the-box sentence-embedding models that were never fine-tuned on Glassdoor's actual user-post interaction data — a common shortcut that gets a system running quickly but leaves real signal on the table, because "semantically similar" text isn't the same thing as "content this specific user actually engages with." That gap is exactly what a task-specific, interaction-trained retrieval model is positioned to close.

## 2. Technical details

Glassdoor moved to a Two-Tower Neural Network Model as the core of candidate generation: one tower encodes the user, one tower encodes the post, and both towers are trained jointly on the actual user-post interaction prediction task rather than on a generic language-modeling or sentence-similarity objective. This is the key architectural shift from the prior approach — instead of embeddings that are merely semantically coherent (from a general-purpose pretrained model), the new embeddings are directly optimized so that user and post vectors that should be close in the feed-recommendation sense are actually close in embedding space. The trained two-tower retriever sits as the candidate-generation stage within Glassdoor's broader four-stage ML recommender system, feeding into the downstream ranking stages that were left unchanged.

## 3. Impact — potential & realized

**Realized:** Offline, the switch to the interaction-trained two-tower model produced 40–60% relative improvements across standard retrieval-quality metrics (Precision@K, Recall@K, F1@K, and HitRate@K) compared to the prior pretrained-embedding baseline. Online, the change drove a statistically significant lift in community engagement, measured internally as eCRAUs (Engaged Community Registered Active Users — users who took any engagement action), and produced a secondary benefit of feed diversification: users saw more impressions from a wider variety of less-common feeds rather than the feed being dominated by only the biggest, most popular ones. These results were strong enough that the model was adopted into production as part of Glassdoor's four-stage recommender system.

**Potential:** This is a template any team running a candidate-generation stage on off-the-shelf embeddings can copy directly: training user/item towers on real interaction data, even with a fairly standard architecture, tends to substantially outperform pretrained general-purpose embeddings for a recommendation-specific retrieval task. The diversity side-effect is also a useful reminder that better-targeted retrieval doesn't automatically mean narrower retrieval — it can surface a wider, more genuinely personalized slice of the catalog rather than reinforcing popularity bias.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — Textbook two-tower retrieval, executed well

Two-tower candidate generation trained on interaction data is one of the most standard patterns in modern recommender systems — this isn't introducing anything new to the field. The value of the write-up is entirely in the "before vs. after" contrast: it's a clean, well-quantified case study of the gap between using pretrained embeddings as a shortcut versus actually training retrieval embeddings on the task, useful mainly for teams still running the pretrained-embedding version of this system.

### Similar / related work

- [**Pinterest — Evolving Pinterest's Embedding Retrieval Platform**](2026-09-15-pinterest-evolving-embedding-retrieval-platform.md) (in this bank) — a more advanced take on the same two-tower retrieval foundation, extending it with multi-embedding candidates and quantization rather than the initial pretrained-to-trained transition Glassdoor describes here.
- [**Expedia — Candidate Generation Using a Two Tower Approach With Expedia Group Traveler Data**](https://medium.com/expedia-group-tech/candidate-generation-using-a-two-tower-approach-with-expedia-group-traveler-data-ca6a0dcab83e) — another company's applied two-tower candidate-generation write-up, useful as a direct architectural comparison outside social/community feeds.
- **Two-tower retrieval literature generally (e.g. YouTube's sampled-softmax two-tower recommender)** — the foundational body of work this architecture descends from; Glassdoor's contribution here is a production case study, not a variant on the underlying method.

### Jargon buster

- **Candidate generation** — The first stage of a multi-stage recommender system, responsible for retrieving a manageable pool of plausibly relevant items from a much larger catalog before more expensive ranking models score and order them.
- **Two-tower model** — A retrieval architecture with two separate networks — one for the user/query, one for the item — each producing an embedding, with relevance scored by similarity between the two vectors, allowing item embeddings to be precomputed and searched efficiently at serving time.
- **Precision@K / Recall@K / HitRate@K** — Standard retrieval-quality metrics measuring, among the top K retrieved candidates, how many are relevant (precision), what fraction of all relevant items were found (recall), and whether at least one relevant item appears at all (hit rate).
- **Popularity bias** — The tendency of a recommender system to over-recommend already-popular items, at the expense of diverse or less mainstream ones a user might also genuinely be interested in.
