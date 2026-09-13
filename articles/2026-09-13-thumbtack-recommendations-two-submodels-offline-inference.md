---
id: thumbtack-recommendations-two-submodels-offline-inference
title: "How We Personalized Recommendations for Professionals on Thumbtack"
source: "Thumbtack Engineering"
url: "https://medium.com/thumbtack-engineering/how-we-personalized-recommendations-for-professionals-on-thumbtack-40131b57c3a9"
published: "2024-06"
added: "2026-09-13"
category: personalization-recsys
tags: [recommendations, boosted-trees, offline-inference, marketplace, personalization, thumbtack]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# How We Personalized Recommendations for Professionals on Thumbtack

**Source:** [Thumbtack Engineering](https://medium.com/thumbtack-engineering/how-we-personalized-recommendations-for-professionals-on-thumbtack-40131b57c3a9) · Published 2024-06 · Added 2026-09-13
**Category:** Personalization & Recommender Systems · **Tags:** `recommendations`, `boosted-trees`, `offline-inference`, `marketplace`, `personalization`, `thumbtack`

## TL;DR

Thumbtack personalizes which growth "recommendations" (like targeting or budget changes) it surfaces to service professionals by multiplying two simple sub-models — a boosted-tree classifier predicting the probability a pro enables a recommendation, and a fixed-effects model estimating the expected lead volume if they do — and deliberately serves the result via weekly offline batch inference rather than real-time serving, since the underlying behavior doesn't need sub-second freshness.

## 1. Business context

Thumbtack's marketplace connects consumers with service professionals ("pros"), and part of helping pros grow their business is surfacing actionable "recommendations" — for example, suggesting a pro adjust their targeting or budget. Not every recommendation is equally valuable to every pro, so the problem is deciding *which* recommendation(s) to show a given pro to maximize the expected value of that interaction, rather than showing every possible recommendation to everyone regardless of relevance.

## 2. Technical details

The system combines two sub-models multiplicatively to produce an expected-value score per recommendation:

- **Enablement classifier** — a boosted-tree binary classifier predicting the probability a given pro will enable a given recommendation, with the recommendation type itself included as a model feature (so one model serves all recommendation types) and the label being a simple binary enable/not-enable outcome. The team explicitly evaluated boosted trees against logistic regression, bagged trees, and neural networks, and chose boosted trees for the best overall balance of ranking performance, ease of training, and ease of inference — not because it had the single highest raw accuracy of the options tried.
- **Value Given Enablement (VGE) model** — estimates the expected lead volume a pro would receive from a given recommendation type *conditional on enabling it*, using **Fixed Effects Modeling (FEM)** to control for pro-level and other confounding factors when estimating that conditional value.
- **Combined score** — expected value = P(enable) × VGE, giving a single ranking signal across heterogeneous recommendation types that accounts for both how likely a pro is to act and how valuable that action would be if they did.
- **Serving architecture** — because lead-volume and enablement behavior patterns don't require sub-second freshness, the team deliberately chose **offline batch inference with a weekly refresh cadence** instead of building real-time serving infrastructure, trading maximum freshness for substantially lower operational complexity.

## 3. Impact — potential & realized

**Realized:** the combined scoring approach lets Thumbtack rank a heterogeneous set of recommendation types on a single comparable expected-value scale, and the offline weekly-batch serving choice kept the system's operational footprint modest relative to what real-time serving would require. No specific quantitative lift (e.g., percentage increase in enablement rate or lead volume attributable to personalization) was available in the source material reviewed for this entry.

**Potential:** the general pattern — multiply a "will they act" model by a "how valuable if they do" model, and choose serving cadence based on how fast the underlying behavior actually changes rather than defaulting to real-time — is a broadly reusable, low-complexity recipe for any marketplace or platform deciding which of several possible nudges/recommendations to surface to a user.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Sound, unglamorous engineering judgment rather than a new method

Multiplying a propensity model by a conditional-value model is a well-established pattern in marketing and growth analytics (similar in spirit to expected-value scoring used in ad targeting and CRM), and boosted trees over logistic regression/neural nets for tabular ranking is a common, defensible choice rather than a novel finding. What's genuinely worth noting is the explicit, stated reasoning for both the model choice (evaluated multiple alternatives, picked the best *practical* balance rather than the best raw metric) and the serving-cadence choice (offline weekly batch, justified by the actual freshness needs of the signal) — a useful demonstration of engineering judgment that resists overbuilding, even if it isn't methodologically new.

### Similar / related work

- [**Real-Time Spatial Temporal Forecasting @ Lyft**](2026-09-13-lyft-realtime-spatial-temporal-forecasting.md) (in this bank) — the same "choose the simpler, cheaper approach that actually fits the problem's real-world constraints" philosophy, applied to forecasting model choice instead of recommendation ranking.
- [**Swiggy's In-House Predicted Lifetime Value Model for Customer Acquisition**](2026-09-04-swiggy-predicted-lifetime-value-multitask-mlp.md) (in this bank) — another marketplace using a purpose-built, moderately simple model (a multi-task MLP) for a value-prediction problem rather than the most complex architecture available.
- [**AI in CVS Front Store E-commerce: Building a Complementary Product Bundle Recommender**](2026-09-07-cvs-complementary-product-bundles-gnn-gpt4.md) (in this bank) — a contrasting example from the same broad recsys space that does reach for heavier machinery (GNNs, GPT-4), useful as a comparison point on when added model complexity is and isn't chosen.

### Jargon buster

- **Boosted trees (gradient-boosted decision trees)** — an ensemble machine-learning method that builds many small decision trees sequentially, each correcting errors from the previous ones, widely used for tabular-data prediction and ranking tasks.
- **Fixed Effects Modeling (FEM)** — a statistical technique that controls for unobserved, entity-specific factors (like a pro's baseline business size) when estimating the effect of something else, reducing the risk of confounded estimates.
- **Offline batch inference** — computing model predictions for all relevant entities on a schedule (e.g., weekly) and storing the results, as opposed to computing a prediction live at the moment it's needed (real-time/online inference).
- **Propensity × value scoring** — a general pattern of multiplying "how likely is this outcome" by "how valuable is this outcome" to get a single comparable expected-value number across different possible actions.
