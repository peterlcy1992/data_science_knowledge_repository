---
id: stripe-ml-flywheel-card-testing
title: "The ML Flywheel: How We Continually Improve Our Models to Reduce Card Testing"
source: "Stripe Engineering"
url: "https://stripe.com/blog/the-ml-flywheel-how-we-continually-improve-our-models-to-reduce-card-testing"
published: "2024-12"
added: "2026-09-06"
category: data-engineering
tags: [fraud-detection, card-testing, continual-retraining, foundation-models, real-time-scoring, mlops]
novelty: 3
sourced_via: "full-text fetch"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# The ML Flywheel: How We Continually Improve Our Models to Reduce Card Testing

**Source:** [Stripe Engineering](https://stripe.com/blog/the-ml-flywheel-how-we-continually-improve-our-models-to-reduce-card-testing) · Published 2024-12 · Added 2026-09-06
**Category:** Data Engineering · **Tags:** `fraud-detection`, `card-testing`, `continual-retraining`, `foundation-models`, `real-time-scoring`, `mlops`

## TL;DR

Stripe describes a three-tier, continually-retrained ML system (Radar) that estimates platform-wide card-testing prevalence, localizes where attacks are occurring, and scores individual transactions in real time — with a rapid labeling-to-redeployment loop that lets the models adapt as fast as attackers change tactics. Stripe reports an 80% reduction in successful card-testing attacks over two years, even as total payment volume grew past $1 trillion annually.

## 1. Business context

Card testing is a fraud technique where attackers validate stolen or guessed card numbers using small or zero-dollar transactions before using the confirmed-valid cards for large fraudulent purchases or reselling them on illegal markets. It comes in two flavors: verification attacks (testing cards already known to be stolen) and enumeration attacks (systematically guessing card numbers within a range to find ones that work). Because card testing evolves quickly — attackers shift targets and tactics as soon as one channel gets blocked — a static fraud model decays fast; Stripe's problem was building a defense that could be retrained and redeployed roughly as quickly as the attacks themselves change, without either missing new attack patterns or over-blocking legitimate transaction spikes that merely look similar to an attack.

## 2. Technical details

The system is organized into three tiers operating at different granularities:

- **Layer 1 (Macro)** — models estimate overall card-testing prevalence across the entire platform, informing daily, platform-wide risk-posture adjustments.
- **Layer 2 (Meso)** — models identify *where* attacks are concentrated (specific businesses, specific card issuers, or specific transaction surfaces), which is what lets the system distinguish a genuine attack from an unrelated legitimate traffic spike that merely resembles one at the aggregate level.
- **Layer 3 (Micro)** — individual transaction-level classifiers score each transaction's fraud probability using a wide range of signals in real time.

These three layers jointly drive a dynamically-updated blocking threshold, letting Stripe tighten enforcement precisely where an attack is actually happening while minimizing disruption to legitimate transactions elsewhere on the platform.

The "flywheel" is the rapid retraining loop that keeps all three layers current: (1) labeling combines attack intelligence, automated pattern discovery, and expert human review to generate training labels for new attack variants; (2) feature engineering runs through Shepherd, a feature platform Stripe built with Airbnb, designed to let the team add new features with minimal code changes; (3) testing uses Flyte for workflow orchestration, offline evaluation, and blue-green deployment of new model versions; (4) redeployment can push updated models to production immediately during active incident response, rather than waiting for a routine release cycle. Stripe also layers foundation models into the pipeline to catch subtler cross-transaction patterns that its more traditional per-transaction classifiers miss, looking for signal across billions of global transactions.

## 3. Impact — potential & realized

**Realized:** Stripe reports an 80% reduction in successful card-testing attacks over a two-year period, achieved while total payment volume processed grew past $1 trillion annually — meaning the reduction happened despite (not merely alongside) a large increase in the raw transaction surface attackers could target. The system is described as maintaining low false-positive rates while blocking attacks in real time.

**Potential:** The three-tier macro/meso/micro decomposition is a generalizable fraud-system design pattern beyond card testing specifically — any adversarial, adaptive-attacker domain (account takeover, promo abuse, content spam) benefits from separating "is something happening at all," "where specifically," and "is this individual instance bad," because each tier can be retrained on a different cadence appropriate to how fast that layer's signal actually shifts.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Solid, mature MLOps applied to an adversarial domain

Multi-tier fraud detection and rapid-retraining "flywheels" are well-established patterns in the fraud/trust-and-safety space; nothing architecturally here is a first. The value is in the concrete operational detail — a shared feature platform built jointly with another company (Shepherd, with Airbnb), Flyte-based blue-green deployment, and the explicit incident-response fast path for immediate redeployment — which together describe a genuinely mature MLOps practice for an adversarial, fast-moving fraud domain.

### Similar / related work

- [**Using Grab's Trust Counter Service to Detect Fraud Successfully**](2026-09-05-grab-trust-counter-fraud-detection.md) (in this bank) — a different real-time fraud architecture (self-service rule counters over ScyllaDB) solving a related trust-and-safety problem with a lighter-weight, rules-first approach.
- [**Leveraging Graph Technology for Real-Time Fraud Detection and Prevention at Booking.com**](2026-08-30-booking-graph-fraud-detection.md) (in this bank) — another real-time fraud system, using graph-based entity relationships rather than the tiered-classifier approach here.
- [**Model Excellence Scores: A Framework for ML Quality at Scale at Uber**](2026-08-30-uber-model-excellence-scores.md) (in this bank) — a complementary "how do you keep many production ML models healthy over time" governance framework, relevant to the retraining-cadence problem this article addresses tactically.

### Jargon buster

- **Card testing** — a fraud technique where stolen or guessed card numbers are validated via small test transactions before being used for larger fraud or resold.
- **Blue-green deployment** — a release strategy that runs the new and old versions of a system side by side and switches traffic over only once the new version is validated, minimizing the risk and downtime of a bad deploy.
- **Feature platform** — shared infrastructure for defining, computing, and serving the input features ML models consume, letting teams add or change features without rebuilding each model's data pipeline from scratch.
