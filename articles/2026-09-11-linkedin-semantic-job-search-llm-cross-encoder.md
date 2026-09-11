---
id: linkedin-job-search-llms
title: "Building the Next Generation of Job Search at LinkedIn"
source: "LinkedIn Engineering Blog"
url: "https://www.linkedin.com/blog/engineering/ai/building-the-next-generation-of-job-search-at-linkedin"
published: "2026"
added: "2026-09-11"
category: search-ranking
tags: [semantic-search, llm, embeddings, cross-encoder, distillation, job-search, linkedin]
novelty: 4
discovered_via: "Snacks Weekly on Data Science podcast"
sourced_via: "web search"
---

# Building the Next Generation of Job Search at LinkedIn

**Source:** [LinkedIn Engineering Blog](https://www.linkedin.com/blog/engineering/ai/building-the-next-generation-of-job-search-at-linkedin) · Published 2026 · Added 2026-09-11
**Category:** Search & Ranking · **Tags:** `semantic-search`, `llm`, `embeddings`, `cross-encoder`, `distillation`, `job-search`, `linkedin`

## TL;DR

LinkedIn replaced keyword-based job search with an LLM-powered semantic pipeline — a tool-calling query engine, GPU-based exhaustive (not approximate) nearest-neighbor retrieval, and a distilled cross-encoder small language model for ranking — letting members search in plain language like "I want to use marketing skills to cure cancer" and delivering a reported +1.2% DAU lift alongside double-digit NDCG@10 gains.

## 1. Business context

Traditional keyword-based job search forced members to guess the right terms and rigid filters, and couldn't understand what a member actually wanted if they described it in their own words rather than job-title jargon. LinkedIn's bet was that LLMs could turn job search into genuine intent understanding — resolving something like "entry-level jobs in the gaming industry" or a connection-based constraint into the right structured query — surfacing roles a member might not have known to search for by name, serving all of this at the scale of LinkedIn's 1.2 billion members.

## 2. Technical details

The system has three stages. A **query engine** uses tool-calling with fine-tuned LLMs to classify intent, extract structured constraints, and pull external context (profile data, network graph) — a query like "jobs in New York Metro Area where I have a connection" gets resolved into geo IDs and company IDs fetched from LinkedIn's graph service for strict filtering, with personalized suggestions generated via retrieval-augmented generation patterns. For **retrieval**, LinkedIn deliberately chose exhaustive GPU-based nearest-neighbor search over approximate nearest neighbor (ANN) indexes, on the reasoning that "O(n) approaches can beat out O(log n) when the constant factors are sufficiently different" — flat vector layouts with fused GPU kernels handled the complex filters and high index turnover (job postings live only weeks) more simply and with better latency than a maintained ANN graph. For **ranking**, a distilled, decoder-only small language model acts as a cross-encoder — taking query and job text together and outputting a relevance score across dozens of behavioral features — trained via supervised distillation from a larger teacher model.

Training data combines real click logs with LLM-generated synthetic data: explicit product policies define a 5-point relevance grading scale, human evaluators initially grade query-job pairs, and an LLM is then fine-tuned on those human annotations to automate grading at "millions or tens of millions of grades per day" — letting the team safeguard relevance while iterating quickly on other parts of the pipeline. The retrieval model itself is fine-tuned with reinforcement learning: a teacher model provides a real-time reward signal, optimized against a composite loss combining contrastive accuracy, ListNet ranking loss, KL divergence, and score regularization, trained with Fully Sharded Data Parallel and BF16 precision. Serving-side, the query engine uses separate caching for personalized vs. non-personalized queries, KV-caching in LLM serving, minimized response schemas (replacing verbose XML/JSON), and model distillation to keep latency down — collapsing what had been a nine-stage pipeline down "by an order of magnitude."

## 3. Impact — potential & realized

**Realized:** LinkedIn reports over a +1.2% Daily Active User lift, a +7.73% improvement in NDCG@10 for Job Search, and over 10% NDCG@10 improvement for People Search in online deployment.

**Potential:** the "exhaustive GPU search beats ANN when constant factors favor it" finding is a transferable lesson for any team assuming approximate indexes are always the right call at scale, and the LLM-graded synthetic data pipeline (bootstrapped from human grades, then scaled by a fine-tuned grading model) is a reusable pattern for safely scaling relevance evaluation without a linearly growing human-labeling team.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A genuinely counter-intuitive infrastructure choice, not just "add an LLM"

Semantic, intent-aware job search is well-trodden ground by 2026, but the decision to serve retrieval via exhaustive GPU search instead of an ANN index — explicitly justified by constant-factor reasoning rather than following the default "always use ANN at scale" playbook — is a genuinely useful, somewhat contrarian engineering result worth a 4. The rest of the pipeline (tool-calling query understanding, distilled cross-encoder ranking, LLM-bootstrapped grading) is very well executed but follows patterns now common across large-scale semantic search systems industry-wide.

### Similar / related work

- [**Semantic Search At LinkedIn**](https://arxiv.org/abs/2602.07309) — the companion research paper (Borisyuk, Vasudevan, Wu et al.) covering the same system in more technical depth; read this alongside the blog post for the full methodology.
- [**Scaling Up Efficient Small Language Models Serving and Deployment for Semantic Job Search**](https://arxiv.org/pdf/2510.22101) — a related LinkedIn paper focused specifically on the SLM serving/deployment efficiency side of this same job-search system.
- [**Etsy — Deep Learning for Search Ranking**](2026-09-06-etsy-deep-learning-search-ranking.md) (in this bank) — a different company's move from classical (GBDT) to deep-learning ranking, useful contrast on how differently two marketplaces approached modernizing search ranking.

### Jargon buster

- **Cross-encoder** — a ranking model that takes the query and a candidate item together as one combined input (rather than encoding them separately), letting it directly model interactions between the two at the cost of being slower to run on every candidate.
- **Exhaustive (brute-force) nearest-neighbor search** — comparing a query against every item in the index rather than using a shortcut data structure — normally considered too slow at scale, but here made fast enough via GPU parallelism.
- **Knowledge distillation** — training a smaller "student" model to mimic a larger, more expensive "teacher" model's outputs, to get most of the teacher's quality at a fraction of the serving cost.
- **ListNet loss** — a learning-to-rank loss function that optimizes a model to produce a good overall ranking of a list of items, rather than just scoring each item independently.
