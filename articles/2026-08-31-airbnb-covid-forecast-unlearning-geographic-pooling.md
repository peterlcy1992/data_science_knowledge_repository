---
id: airbnb-covid-forecast-unlearning-geographic-pooling
title: "How We Knew COVID Was Over (and What Our Models Had to Unlearn)"
source: "Airbnb Tech Blog"
url: "https://medium.com/airbnb-engineering/how-we-knew-covid-was-over-and-what-our-models-had-to-unlearn-c606b9bdb0ab"
published: "2026-08"
added: "2026-08-31"
category: forecasting-timeseries
tags: [hierarchical-bayesian, time-series, demand-forecasting, pandemic, pooling]
novelty: 3
sourced_via: "web search"
---

# How We Knew COVID Was Over (and What Our Models Had to Unlearn)

**Source:** [Airbnb Tech Blog](https://medium.com/airbnb-engineering/how-we-knew-covid-was-over-and-what-our-models-had-to-unlearn-c606b9bdb0ab) · Published 2026-08 · Added 2026-08-31
**Category:** Forecasting & Time Series · **Tags:** `hierarchical-bayesian`, `time-series`, `demand-forecasting`, `pandemic`

## TL;DR

A follow-up from Airbnb's Finance Data Science & Strategy team on the sequel
problem to surviving COVID as a forecaster: knowing when the shock was over
and un-doing the very model changes that got them through it. The fix
re-specifies what markets "borrow strength" from — geographic adjacency and
shared real-time recovery dynamics, instead of a fixed pre-pandemic hierarchy.

## 1. Business context

Airbnb forecasts demand, bookings, and cancellations across thousands of
destination markets, many of which are too thin on history to forecast alone.
Before 2020, the team's hierarchical model handled this by having low-data
markets **borrow strength** from markets with long, stable histories, on the
assumption that a destination behaves like other comparable destinations.
COVID broke that assumption rather than just perturbing the model's
parameters: the shock was larger than anything previously seen, and recovery
was wildly uneven — some markets snapped back quickly, others stayed flat for
quarters, and markets that used to move together came apart. This is
described as the team's **second** post on the COVID era, following an
earlier piece on what the initial shock did to their models; this one covers
the harder problem of recognizing recovery and reversing the emergency
adaptations.

## 2. Technical details

- **The pre-2020 setup.** A hierarchical structure pooled thin markets toward
  stable, data-rich "anchor" markets, under the assumption of comparable
  destination behavior.
- **Why pooling broke.** Once COVID hit, the same pooling that used to
  stabilize forecasts began **contaminating** them: markets no longer moved
  together, so borrowing strength from formerly-similar markets imported the
  wrong signal.
- **The respecification.** Rather than pooling along a fixed pre-defined
  hierarchy, the model was changed to pool along **geographic adjacency and
  shared real-time recovery dynamics** — a market now borrows strength from
  places actually behaving like it *today*, not places it historically
  resembled before the crisis.
- **The "unlearning" problem.** The harder half of the post is about
  detecting when it's safe to relax the emergency adaptations made during the
  shock and let the model return toward pre-pandemic-style pooling, rather
  than staying stuck in crisis-mode assumptions indefinitely.

## 3. Impact — potential & realized

- **Realized:** A production respecification of Airbnb's hierarchical
  demand-forecasting approach that changed the pooling structure from a fixed
  hierarchy to adjacency- and dynamics-based borrowing, used to call market
  recovery from COVID.
- **Potential:** A general pattern for hierarchical/Bayesian forecasting
  systems facing any large, geographically uneven shock (not just COVID) —
  detect when a shock has decoupled entities that used to be pooled together,
  and re-pool based on current observed dynamics rather than historical
  resemblance.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — solid applied Bayesian engineering on a genuinely hard, recurring problem

The idea of dynamic rather than fixed pooling in hierarchical models isn't new
in the Bayesian time-series literature, but the framing — the harder problem
is not surviving the shock but knowing when to *stop* treating your data as
shocked — is a useful, underreported production lesson. It's a strong,
well-told applied case rather than a new method, hence a 3.

### Similar / related work

- [**Forecasting the Evolving Composition of Guest Origin Markets in Platform
  Bookings**](https://arxiv.org/abs/2602.18358) (arXiv 2602.18358) — a related Airbnb-data paper on Bayesian
  compositional time series for booking markets.
- [**Forecasting@Meta: Balancing Art and Science**](2026-08-31-meta-forecasting-art-and-science.md) (in this bank) — another
  large-platform forecasting team's account of blending statistical models
  with judgment-driven adjustment.
- Airbnb's earlier post, "What COVID did to our forecasting models (and what
  we built to handle the next shock)" — the first installment this article
  follows up on.

### Jargon buster

- **Hierarchical pooling** — letting data-sparse groups (here, thin markets)
  borrow statistical strength from related, data-rich groups, instead of
  being modeled in complete isolation.
- **Anchor market** — a market with enough history to reliably estimate on
  its own, used as a stable reference point for thinner markets nearby in the
  hierarchy.
- **Borrowing strength** — a Bayesian/hierarchical-modeling term for using
  information from related groups to improve estimates for a group with
  little data of its own.
- **Shock decoupling** — when an external event causes previously correlated
  series (here, destination markets) to stop moving together, invalidating
  assumptions the model relied on.
