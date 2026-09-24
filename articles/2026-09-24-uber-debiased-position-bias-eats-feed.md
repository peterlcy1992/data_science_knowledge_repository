---
id: uber-debiased-position-bias-eats-feed
title: "Improving Uber Eats Home Feed Recommendations via Debiased Relevance Predictions"
source: "Uber Engineering"
url: "https://www.uber.com/blog/improving-uber-eats-home-feed-recommendations/"
published: "2023-12"
added: "2026-09-24"
category: personalization-recsys
tags: [position-bias, examination-model, two-tower, click-model, debiasing]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Improving Uber Eats Home Feed Recommendations via Debiased Relevance Predictions

**Source:** [Uber Engineering](https://www.uber.com/blog/improving-uber-eats-home-feed-recommendations/) · Published 2023-12 · Added 2026-09-24
**Category:** Personalization & Recommender Systems · **Tags:** `position-bias`, `examination-model`, `two-tower`, `click-model`, `debiasing`

## TL;DR

Uber Eats' home-feed conversion model was learning "biased CVR" — orders correlated with a store's rank position, not its true relevance — because users order disproportionately from whatever appears first. A dual-tower model that separates true relevance from a dedicated position-bias/examination tower recovered position-independent relevance estimates and drove a statistically significant increase in orders per user.

## 1. Business context

Uber Eats ranks restaurants and stores on the home feed using a conversion-rate (CVR) model trained on historical click/order data — but that data is itself shaped by where items were previously shown. Users click and order disproportionately from higher-ranked positions regardless of whether those stores are actually the best match, so a naively-trained CVR model partly just learns to predict "was this in a good slot" rather than "is this genuinely relevant," creating a self-reinforcing feedback loop where already-high-ranked stores keep getting boosted. The team first had to prove this bias existed before they could justify the cost of fixing it, then needed a fix that didn't require throwing away the existing ranking infrastructure.

## 2. Technical details

**Measuring the bias**: the team ran a **selective randomization** experiment — randomly permuting store order for a slice of production traffic — and showed that empirical CVR correlated with vertical position even when the underlying relevance of the stores shown was held constant. That's the direct evidence that position, not just relevance, was driving orders.

**Fixing it**: the solution follows the classic **examination model** from information retrieval, factoring observed (biased) conversion into two independent components: `Biased CVR = True CVR × P(Examination)`, where examination probability captures whether a user actually looked at an item in a given position. The model architecture is a **dual-tower design**:
- a **CVR tower** that predicts true, position-independent conversion probability, and
- a **position-bias tower** that estimates examination probability, fed exclusively position-related features so it can't leak relevance signal.

L1 regularization and dropout on the bias tower specifically discourage that tower from absorbing relevance information it shouldn't have access to, keeping the separation between "was it seen" and "was it good" clean.

## 3. Impact — potential & realized

Reported results: offline analysis confirmed the debiased True CVR predictions showed no residual correlation with vertical position (the bias was successfully isolated into the dedicated tower); in production, the team reports a statistically significant increase in orders per user and a shift toward more home-feed orders relative to search — i.e., the improved feed became good enough that users relied on it more and searched less. The model was rolled out to production. The realized win is a ranking signal that reflects genuine relevance rather than a self-reinforcing popularity loop; the broader potential is that any ranked-feed product with the same click-position confound (most recommendation and search surfaces) can apply the same dual-tower examination-model pattern without redesigning the rest of the ranking stack.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A textbook fix, applied and validated cleanly

The examination model and position-debiasing via a side "bias tower" are established techniques in learning-to-rank and search-ranking research, going back over a decade in the information-retrieval literature. What makes this a solid rather than groundbreaking entry is the production validation: a randomized-traffic experiment to first *prove* the bias existed (rather than assuming it), and a clean before/after production rollout with a measurable business outcome. This is a good reference implementation for teams who know they should be debiasing their ranking model but haven't seen a concrete architecture and measurement plan for doing so.

### Similar / related work

- Classic click-model / examination-model literature (Joachims et al. on interpreting clickthrough data as implicit, position-biased feedback) — the foundational IR research this dual-tower design operationalizes; left unlinked as general body-of-work rather than a single citable source.
- Inverse propensity scoring (IPS) approaches to unbiased learning-to-rank — the other common family of techniques for the same problem, reweighting training examples by estimated examination probability rather than modeling it as a separate network tower.

### Jargon buster

- **Position bias** — the tendency for users to interact with items shown in higher/earlier positions regardless of true relevance, which contaminates naively-trained ranking models trained on that interaction data.
- **Examination model** — a framework from search/recommendation research that splits observed user interaction into "did the user see this" (examination) times "did they like it, given they saw it" (true relevance), letting each be modeled separately.
- **Selective randomization** — running a controlled experiment where item order is randomized for a slice of traffic, breaking the correlation between position and prior relevance so the effect of position alone can be isolated and measured.
