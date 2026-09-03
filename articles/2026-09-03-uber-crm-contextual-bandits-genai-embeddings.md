---
id: uber-crm-contextual-bandits-genai-embeddings
title: "Enhancing Personalized CRM Communication with Contextual Bandit Strategies"
source: "Uber Engineering Blog"
url: "https://www.uber.com/blog/enhancing-personalized-crm/"
published: "2025-03"
added: "2026-09-03"
category: personalization-recsys
tags: [contextual-bandits, crm-personalization, llm-embeddings, exploration-exploitation]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Enhancing Personalized CRM Communication with Contextual Bandit Strategies

**Source:** [Uber Engineering Blog](https://www.uber.com/blog/enhancing-personalized-crm/) · Published 2025-03 · Added 2026-09-03
**Category:** Personalization & Recommender Systems · **Tags:** `contextual-bandits`, `crm-personalization`, `llm-embeddings`, `exploration-exploitation`

## TL;DR

Uber's Creative Optimization Platform uses contextual bandits — LinUCB and an XGBoost-plus-SquareCB combination — fed by GPT-derived embeddings of message subject lines and pre-headers, to dynamically pick which CRM message variant to send each user, replacing slow multi-week A/B tests with a system that can converge across 100+ variants while reducing exposure to under-performing content.

## 1. Business context

Traditional A/B testing of CRM message variants (subject lines, pre-headers) only supports comparing 2-3 variants at a time and takes 4-6 weeks to reach a conclusion — too slow and too narrow for a marketing organization that wants to iterate quickly and test much larger variant sets. Uber's Creative Optimization Platform team built a contextual-bandit system to replace that workflow, aiming to converge on good-performing content faster while limiting how many users get exposed to weak variants along the way.

## 2. Technical details

- **Two bandit approaches:** LinUCB, which assumes a linear reward relationship and updates at the campaign level in a stateless way; and an XGBoost model with SquareCB post-processing, which models nonlinear reward relationships and drives exploration via inverse-gap-weighted action probabilities.
- **Content embeddings:** subject-line and pre-header text (including emojis) is embedded via OpenAI's `text-embedding-ada-002` (1,536 dimensions), then reduced to 128 dimensions via PCA to form the content feature vector each bandit consumes.
- **User preference embeddings:** a DNN encoder trained on historical variant content features plus user feedback produces a "creative preference" embedding per user, designed to be reusable across both CRM email/push and in-app surfaces.
- **Pipeline:** marketing creates message templates → a scheduler ingests the eligible user population → the model predicts open probability per variant using user context plus content embeddings → SquareCB selects the variant to send → resulting engagement feeds back into retraining.

## 3. Impact — potential & realized

- **Realized:** the article describes qualitative benefits — faster convergence toward well-performing variants and reduced exposure to under-performing content compared to sequential A/B testing — but does not disclose specific quantified engagement-lift or ROI numbers; that is a notable gap in an otherwise detailed technical write-up.
- **Potential:** supporting 100+ simultaneous variants (versus 2-3 in classical A/B testing) and reusing the same user preference embeddings across CRM and in-app surfaces are the two most transferable ideas — a pattern applicable to any high-volume messaging or notification system currently bottlenecked by sequential A/B testing.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — solid production bandit engineering, undercut by missing headline metrics

Using LLM-derived content embeddings as bandit context, and building a reusable cross-surface user-preference embedding on top of it, is sensible, well-explained production engineering for a genuinely common marketing-optimization problem. It lands at a 3 rather than higher both because contextual bandits for content selection are a well-established technique (Uber's contribution is the specific embedding pipeline, not the bandit method itself) and because the write-up's impact section is unusually thin on results — no lift numbers are reported, which makes it harder to judge how much better this actually performs than the sequential A/B testing it replaced.

### Similar / related work

- [**Bandits for Marketing Optimization at Instacart**](2026-08-16-instacart-bandits-marketing-optimization.md) (in this bank) — another production contextual-bandit system for marketing decisions, useful as a direct comparison point for bandit design choices in a similar domain.
- [**How Discovery Bank Delivers Hyper-Personalized Banking at Scale**](2026-09-03-databricks-discovery-bank-hyperpersonalization.md) (in this bank) — a different personalization-decisioning architecture (a next-best-action engine over unified behavioral data) solving an adjacent problem in a different industry.

### Jargon buster

- **Contextual bandit** — an online decision-making algorithm that chooses among several options (here, message variants) based on context, balancing exploring less-tried options against exploiting known-good ones.
- **LinUCB** — a contextual-bandit algorithm that assumes a linear relationship between context features and expected reward, and picks actions using an upper-confidence-bound rule.
- **SquareCB** — a contextual-bandit algorithm that converts a regression model's predictions into exploration probabilities via inverse-gap weighting, allowing nonlinear reward models like XGBoost to be used within a bandit framework.
- **PCA (Principal Component Analysis)** — a dimensionality-reduction technique used here to shrink 1,536-dimensional text embeddings down to a more manageable 128 dimensions while preserving most of their informative structure.
