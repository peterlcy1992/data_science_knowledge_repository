---
id: afresh-promotion-aware-demand-forecasting
title: "Buy One Get One Free: Promotion-Aware Demand Forecasting for Groceries"
source: "Afresh Engineering Blog"
url: "https://medium.com/afresh-engineering/buy-one-get-one-free-promotion-aware-demand-forecasting-for-groceries-857838c6871f"
published: "2024-07"
added: "2026-09-23"
category: forecasting-timeseries
tags: [demand-forecasting, quantile-regression, grocery, promotions, deep-learning]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Buy One Get One Free: Promotion-Aware Demand Forecasting for Groceries

**Source:** [Afresh Engineering Blog](https://medium.com/afresh-engineering/buy-one-get-one-free-promotion-aware-demand-forecasting-for-groceries-857838c6871f) · Published 2024-07 · Added 2026-09-23
**Category:** Forecasting & Time Series · **Tags:** `demand-forecasting`, `quantile-regression`, `grocery`, `promotions`, `deep-learning`

## TL;DR

Afresh found its baseline grocery demand forecaster's quantile loss got 2-3x worse during promotions, with calibration dropping to roughly 50% at a promotion's start, because promoted-item demand looks nothing like the historical pattern the model learned. Feeding promo-specific features (price, promo type, display size) into a deep quantile-forecasting model closes most of that gap.

## 1. Business context

Grocery retailers order inventory ahead of demand, and promotions (BOGO offers, temporary price cuts, end-cap displays) are exactly the moments where getting the order quantity wrong is most costly: understock a promoted item and lose sales during the highest-traffic period for that SKU, overstock it and eat spoilage costs on perishables. With inflation pushing shoppers to be more price-sensitive, promotions were driving a growing and increasingly unpredictable share of volume — and a forecaster trained mostly on non-promotional history had no signal for how demand would actually behave once a promotion started.

## 2. Technical details

Afresh's baseline forecaster, tuned for typical (non-promotional) demand, was promotion-unaware: it had no explicit input describing whether an item was on promotion, what kind of promotion, or how prominently it was displayed. When Afresh measured this baseline specifically during promotional periods, quantile loss was 2-3x worse than during normal periods, and calibration (how well the predicted quantiles matched actual outcomes) fell to about 50% right at the start of a promotion — meaning the model's uncertainty estimates, not just its point forecasts, became unreliable exactly when accurate uncertainty mattered most for avoiding stockouts or spoilage.

The fix was architectural: build promotion awareness directly into the deep learning demand model by adding promo features — price, promo type (e.g., BOGO vs. straight discount), and display size — as inputs, rather than treating promotional periods as noise to average over. This lets the same neural forecasting architecture learn how each type of promotion shifts the demand curve instead of applying one global pattern to both promotional and non-promotional periods.

## 3. Impact — potential & realized

The promotion-aware model substantially closes the accuracy and calibration gap that opened up during promotions in the baseline, directly reducing the risk of promoted items running out of stock or dropping to low fullness early in a promotion — the two failure modes that most directly cost a grocer sales (stockouts) or margin (spoilage from overstock). The broader potential is a reusable pattern: any demand-forecasting system facing structural regime shifts (promotions, holidays, weather events) can benefit from explicitly modeling the regime rather than relying on a single global model to implicitly average over it.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-executed instance of a known forecasting principle

Feeding regime/event features into a demand model isn't new in forecasting generally, but grocery promotions are a genuinely hard version of the problem (short duration, sparse historical examples per promo type, high cost of being wrong on perishables), and Afresh's explicit quantification of the failure mode — 2-3x quantile loss, ~50% calibration at promo start — is a useful, concrete illustration of why "the model looks fine on average" can hide a specific, costly failure window. Useful reference for any team about to discover their forecaster quietly falls apart during the exact events that matter most to the business.

### Similar / related work

- [**Improving ETAs with Multi-Task Models, Deep Learning, and Probabilistic Forecasting**](2026-08-30-doordash-eta-multitask-probabilistic.md) (in this bank) — same family of deep probabilistic/quantile forecasting under real-world operational constraints, applied to delivery time instead of grocery demand.
- [**Scalable Demand Forecasting**](2026-09-19-picnic-scalable-demand-forecasting.md) (in this bank) — another grocery-adjacent demand forecasting system, useful point of comparison for how different grocery-tech companies handle the same forecasting-at-scale problem.
- [**Forecasting@Meta: Balancing Art and Science**](2026-08-31-meta-forecasting-art-and-science.md) (in this bank) — a broader industry perspective on where forecasting models break down around irregular, event-driven demand shifts, the same class of problem promotions represent.

### Jargon buster

- **Quantile loss (pinball loss)** — the loss function used to train a model to predict a specific quantile (e.g., the 90th percentile of demand) rather than just the mean, letting a business tune for "how much buffer stock do I want" rather than a single point estimate.
- **Calibration** — whether a model's predicted quantiles match reality in practice — e.g., if a model's "90th percentile" forecast is well-calibrated, true demand should exceed it only about 10% of the time.
- **BOGO** — "buy one, get one" (free or at a discount), a common grocery promotion type that sharply and temporarily changes an item's demand curve.
