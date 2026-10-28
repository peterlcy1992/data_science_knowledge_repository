---
id: arxiv-lcm-promo-llm-uplift-promotion-allocation
title: "LCM-Promo: An LLM-Based Uplift Model for Promotion Allocation"
source: "arXiv cs.LG (Prosus / iFood)"
url: "https://arxiv.org/abs/2610.37570"
published: "2026-10"
added: "2026-10-28"
category: personalization-recsys
tags: [uplift-modeling, promotion-allocation, finetuned-llm, ab-testing, monotonic-response-curve, budget-constrained-allocation]
novelty: 3
sourced_via: "full-text fetch"
---

# LCM-Promo: An LLM-Based Uplift Model for Promotion Allocation

**Source:** [arXiv cs.LG (Prosus / iFood)](https://arxiv.org/abs/2610.37570) · Published 2026-10 · Added 2026-10-28
**Category:** personalization-recsys · **Tags:** `uplift-modeling`, `promotion-allocation`, `finetuned-llm`, `ab-testing`, `monotonic-response-curve`, `budget-constrained-allocation`

## TL;DR

Prosus and iFood finetune a 4B-parameter LLM (a "Large Commerce Model") to predict, in a single token, the minimum discount at which a user would convert; decoding that token distribution as a conversion-threshold PMF gives a promotion-response curve that is monotone by construction. In a one-month production A/B test on churn reactivation (90/10 split) it increased conversion by 1% and reduced promotion cost by 6% relative to the Segment-EMA baseline.

## 1. Business context

Promotion budgets in food delivery are spent on discounts that vary by day, delivery shift, product category and discount mechanic. iFood's prior production policy, Segment-EMA, forecasts orders per segment-promotion cell with an exponentially weighted moving average; because every new discount, segment or context needs exploration within its cell, it limits how finely users can be segmented. The bet is that a prompt-based model can take user representation, session context and discount options directly as input and so share information across what used to be separate cells.

## 2. Technical details

Promotion response is cast as single-token prediction. Each prompt holds a system prompt, session context (e.g. day and delivery shift), an LCM-generated user representation (the Large Commerce Model turns raw logs into structured behavioural summaries) and discount options mapped to alphabetic identifiers, ordered by increasing discount depth. The base model is a 4B-parameter dense model, trained with cross-entropy on the observed conversion-discount label (a no-purchase token for non-converters). At inference the next-token distribution is restricted to the valid identifiers and renormalised, then read as a PMF over a latent conversion threshold T (the minimum discount at which the user converts; T = infinity for no purchase). The cumulative sum r_k(x) = P(T <= d_k | x) is the promotion-response curve, monotone non-decreasing by construction; model-implied uplift versus no discount follows directly. In the churn-reactivation setting users may see several offers in a month but typically convert once, so the observed conversion discount is used as a proxy for the threshold. A "waterfall" label augmentation (all discounts at or above the conversion discount labelled positive, soft-target smoothed) was also tried. For production, inference runs twice daily (lunch and dinner) over user clusters (city, session, lifecycle) with mean curves estimated by bootstrap-sized random sampling, on a self-hosted vLLM deployment via the authors' open-source BESH batch endpoint, about 1 hour daily on 8 H200s. Curves feed a linear-optimisation allocator under a global budget.

## 3. Impact — potential & realized

Realized (as reported): one-month production A/B on churn-reactivation users across Brazil, randomised 90% control (Segment-EMA) / 10% treatment (LCM-Promo), same global budget constraint and same allocator so only the response model differed: conversion +1% and promotion cost -6% (relative lifts, no intervals reported in the paper). Allocation expanded from about 50 segments to over 1,000 clusters and from 10 wallet configurations to over one million promotion combinations; the system was then rolled out to all churn users. Offline, on RCT data with a fixed promotion versus an uplift random forest (causalml) trained on earlier RCT months: AUUC 0.0608 vs 0.0578 and Qini 0.0490 vs 0.0466 (LCM-Promo slightly ahead, with overlapping spreads), Uplift@30 0.1626 vs 0.1708 (forest ahead); the waterfall variant was worse. The authors treat this as validation for online testing, not evidence of offline superiority. Limits stated: one lifecycle stage, one platform. Potential: a template for compact task-specialised LLMs as response models in budget-constrained targeting.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A decision-oriented use of an LLM: the LLM is not the allocator, it is a response-curve estimator whose output is shaped (threshold PMF to cumulative curve) so that it satisfies the monotonicity a promotion optimiser needs.

A decision-oriented use of an LLM: the LLM is not the allocator, it is a response-curve estimator whose output is shaped (threshold PMF to cumulative curve) so that it satisfies the monotonicity a promotion optimiser needs. The A/B design is clean (same allocator and budget in both arms), but the headline 1% / 6% lifts come without uncertainty estimates, a 10% arm over one month, and a baseline that is itself coarse, so how much comes from the LLM versus simply finer segmentation is not separable from the reported evidence. The training label is a proxy for a latent threshold learned from observational logs, so causal validity leans on the production logs having enough discount variation; the RCT check is narrower than production, as the authors admit.

### Similar / related work

- [**Next Best Action: Causal Constrained Offline RL for Business Action Targeting**](2026-10-20-arxiv-next-best-action-causal-constrained-offline-rl.md) (in this bank) — same family of budget-constrained targeting with logged-data learning
- [**Reinforcement Learning for Controller Parameters in the Auto-Bidding System at Pinterest**](2026-10-27-pinterest-rlbp-rl-meta-controller-auto-bidding.md) (in this bank) — another production budget-allocation system with an A/B readout

### Jargon buster

- **Uplift modelling** — Estimating how much more likely a user is to convert when shown a treatment (here a promotion) than when not, rather than just predicting conversion.
- **AUUC / Qini** — Area-under-uplift-curve style metrics that score how well a model ranks users by incremental effect, measured on randomised data.
- **Monotone response curve** — A conversion probability that never falls as the discount deepens; building this in avoids nonsensical allocations.
