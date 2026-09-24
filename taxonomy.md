# Categories

Every article is filed under exactly one primary `category` (its slug is used in
`index.json`) and may carry any number of free-form `tags`. Keep the category
set small and stable; prefer adding tags over inventing new categories.

## Scope & balance

This is a **data-science** knowledge bank. The categories below split into two
families that should stay **balanced** (~50/50) in what gets discovered and, especially,
in what is chosen for the daily deep dive:

- **Core DS** — `experimentation-causal`, `statistical-modeling`,
  `product-analytics`, `forecasting-timeseries`. Statistics, inference,
  measurement, and decision-making: the heart of the discipline.
- **AI / ML-systems** — `llm-genai`, `personalization-recsys`, `search-ranking`,
  `ml-infra-serving`, `cv-multimodal`, `data-engineering`, `research-foundational`.
  In scope and important, but favour pieces that tie back to DS practice
  (measurement, inference, evaluation, decisions) over pure model/infra engineering.

| Slug | Name | Family | Covers |
|------|------|--------|--------|
| `experimentation-causal` | Experimentation & Causal Inference | Core DS | A/B testing, switchback/interleaving, variance reduction (CUPED), uplift modelling, causal inference (DiD, synthetic control, IV), metrics/decision design |
| `statistical-modeling` | Statistical Modeling | Core DS | Regression/GLMs, Bayesian & hierarchical models, survival analysis, sampling & inference, mixed-effects, model diagnostics |
| `product-analytics` | Product Analytics & Metrics | Core DS | Metric frameworks (north-star, guardrails), funnel/retention/cohort analysis, segmentation, decision science, dashboards & analytics practice |
| `forecasting-timeseries` | Forecasting & Time Series | Core DS | Demand forecasting, anomaly detection, temporal/hierarchical-Bayesian models |
| `personalization-recsys` | Personalization & Recommender Systems | AI/ML | Ranking, retrieval, candidate generation, cold-start, artwork/asset personalization, two-tower and sequence models |
| `llm-genai` | LLMs & Generative AI | AI/ML | Foundation models, fine-tuning, RAG, agents, prompt/context engineering, generative recommendation |
| `search-ranking` | Search & Ranking | AI/ML | Query understanding, semantic/embedding retrieval, generative retrieval, learning-to-rank |
| `ml-infra-serving` | ML Infrastructure & Serving | AI/ML | Model serving, inference engines, GPU scheduling, feature stores, training platforms, MLOps |
| `cv-multimodal` | Computer Vision & Multimodal | AI/ML | Image/video/audio understanding, multimodal embeddings, media ML |
| `data-engineering` | Data Engineering | AI/ML | Pipelines, streaming, lakehouse, feature freshness, knowledge graphs, data quality |
| `research-foundational` | Research & Foundational | AI/ML | Methods-first papers and results not tied to one product surface |

## Novelty scale (used by Claude's Take)

- **5 — Field-shifting.** Introduces a genuinely new paradigm or result others will copy.
- **4 — Strong.** A notable advance or a clever production-first take on a hot idea.
- **3 — Solid.** Good engineering; incremental over known techniques, well executed.
- **2 — Incremental.** Useful write-up, little that is new.
- **1 — Recap.** Mostly a survey or restatement of established practice.
