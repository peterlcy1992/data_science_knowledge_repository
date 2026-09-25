---
id: instacart-quasi-experiment-rdd
title: "Optimizing at the Edge: Using Regression Discontinuity Designs to Power Decision-Making"
source: "Instacart Tech Blog"
url: "https://tech.instacart.com/optimizing-at-the-edge-using-regression-discontinuity-designs-to-power-decision-making-51e296615046"
published: "2023-11"
added: "2026-09-25"
category: experimentation-causal
tags: [regression-discontinuity, quasi-experimentation, causal-inference, payments, econometrics]
novelty: 4
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Optimizing at the Edge: Using Regression Discontinuity Designs to Power Decision-Making

**Source:** [Instacart Tech Blog](https://tech.instacart.com/optimizing-at-the-edge-using-regression-discontinuity-designs-to-power-decision-making-51e296615046) · Published 2023-11 · Added 2026-09-25
**Category:** Experimentation & Causal Inference · **Tags:** `regression-discontinuity`, `quasi-experimentation`, `causal-inference`, `payments`, `econometrics`

## TL;DR

Instacart's economics team used a regression discontinuity design (RDD) — exploiting a hard $5-multiple threshold in how card-authorization buffers get rounded — to estimate the causal effect of buffer size on card declines and order volume without running an A/B test first. The RDD-derived estimate was later validated by a live experiment that reduced authorization-buffer rounding and measurably cut declines, generating a "win-win" increase in order volume for both customers and Instacart.

## 1. Business context

When a customer places an order, Instacart puts a temporary authorization hold on their card for slightly more than the order total — a buffer that covers potential weight-based substitutions or added items at checkout. Instacart's policy rounded that buffer up to the nearest $5 multiple, which meant two orders of nearly identical size could receive noticeably different buffer amounts depending on which side of a $5 threshold they landed on. Larger buffers reduce the risk of needing a second authorization later, but they also raise the chance a card gets declined outright (insufficient available balance) — directly costing Instacart completed orders and customers a smooth checkout. Before running a full experiment, the economics team wanted a rigorous causal read on how much buffer size was actually driving declines, using data they already had.

## 2. Technical details

The $5-multiple rounding rule creates a naturally occurring discontinuity: orders whose pre-rounding total sits just below a $5 multiple get a small buffer bump, while orders just above it jump to the next $5 increment, producing a discrete jump in buffer amount for customers who are otherwise essentially identical on every other dimension (order size, item mix, customer history). Regression discontinuity design formalizes the idea that comparing outcomes for units just below vs. just above such a threshold approximates a randomized comparison — the key identifying assumption being that everything else about a customer is "locally smooth" across the cutoff, so the discontinuous jump in buffer size can be attributed to the buffer amount itself rather than to some confound correlated with order size. Instacart fit a local regression on either side of the $5-multiple cutoffs to estimate the local average treatment effect of a higher buffer on downstream business metrics — primarily decline rate and completed order volume.

## 3. Impact — potential & realized

The RDD analysis pointed to a clear conclusion: the incremental protection from rounding buffers up to the next $5 was not worth the additional declines it caused. Instacart followed up with a live experiment that significantly reduced the amount of upward rounding in the initial authorization buffer, and the experiment's results validated the RDD's causal estimate — the change reduced card declines and generated a measurable increase in order volume, a rare case where reducing friction on the payments side pays off for both the customer experience and the business's top line simultaneously.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A clean, real production example of a quasi-experimental method that's easy to describe but rarely this well-instrumented

Regression discontinuity is textbook econometrics, but production write-ups that (a) identify a genuine, unintentional discontinuity buried in an operational policy, (b) use it to get a causal estimate before spending experiment budget, and (c) then validate that estimate against a real subsequent A/B test are uncommon — most companies either only run A/B tests or only wave at "natural experiments" without closing the loop on validation. The rounding-threshold setup here is also a nice illustration that discontinuities worth exploiting are often hiding in mundane business rules (rounding, tiering, eligibility cutoffs) rather than requiring a contrived natural experiment.

### Similar / related work

- [**The Science of Price Experiments in the Amazon Store**](2026-09-08-amazon-price-experimentation.md) (in this bank) — another payments/pricing-adjacent causal-inference production system, though Amazon's is built around randomized experiments rather than a quasi-experimental design.
- [**Harnessing the Power of Geo-Experimentation: How Mercado Libre Measures the Effectiveness of Its Third-Party Media Strategies Using GeoLift**](2026-09-13-mercadolibre-geo-experimentation-geolift.md) (in this bank) — a different quasi-experimental toolkit (geo-based synthetic control) used for the same underlying reason: getting causal answers where a clean randomized test is hard or slow to run.
- **General regression discontinuity design literature** (Imbens & Lemieux, and the broader econometrics canon) — the standard theoretical treatment of the local-linear/local-regression estimators and the smoothness/manipulation-of-the-running-variable assumptions this write-up relies on.

### Jargon buster

- **Regression discontinuity design (RDD)** — a quasi-experimental method that estimates a causal effect by comparing outcomes for units just on either side of a threshold that determines treatment, exploiting the fact that units very close to the cutoff are otherwise comparable.
- **Local average treatment effect (LATE)** — the causal effect estimated by an RDD (or similar quasi-experimental design), which applies specifically to units near the threshold, not necessarily to the whole population.
- **Running variable** — the continuous variable (here, pre-rounding order/buffer total) whose value determines which side of the threshold — and therefore which treatment — a unit receives.
