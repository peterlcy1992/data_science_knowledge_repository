---
id: instacart-ads-retrieval-rebuild
title: "From Scoring to Spelling: Rebuilding Ads Retrieval at Instacart"
source: "Instacart Tech"
url: "https://tech.instacart.com/from-scoring-to-spelling-rebuilding-ads-retrieval-at-instacart-cf36b4e8d1bb"
published: "2026-06"
added: "2026-09-01"
category: search-ranking
tags: [ads-retrieval, generative-retrieval, sequence-modeling, session-modeling, beam-search]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# From Scoring to Spelling: Rebuilding Ads Retrieval at Instacart

**Source:** [Instacart Tech](https://tech.instacart.com/from-scoring-to-spelling-rebuilding-ads-retrieval-at-instacart-cf36b4e8d1bb) · Published 2026-06 · Added 2026-09-01
**Category:** Search & Ranking · **Tags:** `ads-retrieval`, `generative-retrieval`, `sequence-modeling`

> **A note on sourcing:** `tech.instacart.com` was unreachable in this
> environment (blocked at the egress proxy), so this entry is built entirely
> from search-engine-surfaced summaries rather than the primary text.
> Several details below are flagged as unconfirmed rather than stated as
> settled fact — this entry would be worth revisiting with a direct fetch
> before treating its architecture claims as final.

## TL;DR

Instacart rebuilds ads retrieval around a generative model that "spells out"
product identifiers token-by-token, rather than scoring a pre-enumerated
candidate list — the successor to its 2024 BERT-like Contextual
Recommendations sequence model — aiming to surface ad products a
fixed-candidate scoring system couldn't structurally reach. Instacart
reports a click-through-rate lift in online A/B testing, though the exact
figure could not be independently confirmed beyond a single search-surfaced
summary.

## 1. Business context

Instacart surfaces sponsored products on the retailer home page, in search
results, and near the cart, via a retrieval model that selects from a large
ads catalog. In 2024, Instacart built **Contextual Recommendations (CR)**, a
BERT-like sequence model treating grocery shopping like language modeling —
product IDs as tokens, a user's real-time session (views, item-page visits,
cart adds) as the input sequence — replacing older co-occurrence,
similarity, and popularity heuristics for both ads and organic retrieval.
This 2026 rebuild moves from a model that *scores* a fixed, pre-enumerated
candidate list to one that *generates* product identifiers directly, aiming
to expand what the system can discover beyond whatever was enumerated in
advance.

## 2. Technical details

> Confidence on this section is lower than most entries in this bank — see
> the sourcing note above.

- The new retrieval model reportedly generates product representations
  token-by-token instead of scoring an enumerated list, using **beam
  search** to explore candidate sequences, mapped against a
  retailer-partitioned index to retrieve available, relevant ad products.
- Whether items are represented via **Semantic IDs** — discrete codes from
  residual quantization of product embeddings, as used elsewhere in
  generative retrieval — is plausible given the "spelling" framing, but this
  detail could not be confirmed as specific to Instacart's implementation
  rather than general background on the technique category. It's noted here
  as unconfirmed, not asserted as fact.
- The predecessor CR system is reported elsewhere (a third-party case-study
  summary, not this article) to have delivered a 30% lift in cart additions
  and a 10-40% Recall@K improvement over randomized-sequence baselines, and
  to have let Instacart retire several legacy retrieval systems — background
  context on the system this one replaces, not this article's own number.

## 3. Impact — potential & realized

- **Realized (single-source, unverified):** a reported **+5% click-through
  rate** improvement in online A/B testing against the incumbent
  scoring-based model. This figure came from search-engine synthesis of the
  article rather than a second independent citation, so it's included with
  that caveat rather than treated as confirmed.
- **Potential:** if the generative "spelling" approach genuinely escapes the
  discovery ceiling of a pre-enumerated candidate list, it's a pattern
  applicable to any ads or organic retrieval system currently bottlenecked
  by a fixed candidate set.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a real shift, but the least-verified entry in this batch

The scoring-to-generation reframing is meaningful and consistent with where
the rest of the industry (Spotify, Netflix, LinkedIn) is heading. But the
specific architectural claims here are the least verified of anything in
this batch — the score reflects that uncertainty as much as the underlying
content. This entry would be worth revisiting once the primary source is
directly reachable.

### Similar / related work

- [**Deploying Semantic ID-based Generative Retrieval for Large-Scale
  Podcast Discovery at Spotify**](2026-08-30-spotify-semantic-id-generative-retrieval-podcasts.md) (in this bank) — the generative-retrieval
  pattern this entry's "spelling" framing likely resembles.
- [**GenRec: Towards LLM-Native Recommendation at Netflix**](2026-08-30-netflix-genrec-llm-native-recommendation.md) (in this
  bank) — another production system moving retrieval/ranking toward
  LLM-native generation.
- [**An Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking
  (Feed SR)**](2026-09-01-linkedin-feed-sr-sequential-recommender.md) (in this bank) — a useful contrast: a case where a
  similarly-motivated generative/LLM-based ranker was tried and explicitly
  rejected in favor of a more constrained sequential transformer.

### Jargon buster

- **Beam search** — a search strategy that keeps the top-k partial sequences
  at each generation step, instead of only the single best, to explore
  multiple candidate outputs.
- **Candidate retrieval** — the stage that narrows a huge catalog down to a
  shortlist before ranking, as distinct from ranking that shortlist.
- **Contextual Recommendations (CR)** — Instacart's 2024 BERT-like
  session-sequence retrieval and recommendation model, the predecessor to
  the system described here.
