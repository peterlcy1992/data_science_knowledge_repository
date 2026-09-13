---
id: mercadolibre-geo-experimentation-geolift
title: "Harnessing the Power of Geo-Experimentation: How Mercado Libre Measures the Effectiveness of Its Third-Party Media Strategies Using GeoLift"
source: "Tecnología de Mercado Libre"
url: "https://medium.com/mercadolibre-tech/harnessing-the-power-of-geo-experimentation-how-mercado-libre-measures-the-effectiveness-of-its-f68b38857c4b"
published: "2023-06"
added: "2026-09-13"
category: experimentation-causal
tags: [geo-experimentation, causal-inference, geolift, synthetic-control, media-measurement, mercadolibre]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Harnessing the Power of Geo-Experimentation: How Mercado Libre Measures the Effectiveness of Its Third-Party Media Strategies Using GeoLift

**Source:** [Tecnología de Mercado Libre](https://medium.com/mercadolibre-tech/harnessing-the-power-of-geo-experimentation-how-mercado-libre-measures-the-effectiveness-of-its-f68b38857c4b) · Published 2023-06 · Added 2026-09-13
**Category:** Experimentation & Causal Inference · **Tags:** `geo-experimentation`, `causal-inference`, `geolift`, `synthetic-control`, `media-measurement`, `mercadolibre`

## TL;DR

Mercado Libre measures the true incremental effect of its third-party media spend (like app-install campaigns) using Meta's open-source GeoLift methodology — holding out entire states from advertising and comparing them against a synthetic control built from untreated regions — since individual-user A/B testing can't cleanly measure market-level, channel-wide media decisions.

## 1. Business context

Mercado Libre spends heavily on third-party media, such as app-install advertising campaigns, across its marketplace and fintech businesses, and needed a reliable way to measure the *incremental* impact of that spend — how much of the outcome (installs, transactions) is actually caused by the advertising, versus what would have happened anyway. Standard individual-user A/B testing doesn't work well here: media and channel-level decisions (like whether to advertise in a given market at all, or how to allocate budget across channels) operate at a level where user-level randomization either isn't feasible or introduces contamination between treatment and control users who see the same ads or live in the same market.

## 2. Technical details

Mercado Libre built its geo-experimentation practice around **GeoLift**, Meta's open-source, synthetic-control-based geo-experimental framework. In a described Mexico campaign example, the team:

- Selected a **treatment group of 12 states**, which were excluded from app-install advertising entirely for a **21-day holdout window** — the geographic unit itself is the randomized/held-out entity, not individual users.
- Constructed a **synthetic control** from the untreated regions, weighting them so their combined pre-period trends closely match the treatment group's pre-period trends, which is the core idea behind synthetic-control methods: build an artificial "what would have happened without treatment" comparison series when no single untreated group is naturally comparable on its own.
- Compared the treatment group's actual outcomes during the holdout window against the synthetic control's projected outcomes to estimate the true incremental lift attributable to the advertising that was paused.

## 3. Impact — potential & realized

**Realized:** by the time of writing, Mercado Libre had incorporated GeoLift as an in-house measurement practice and had run roughly 20 geo-lift experiments, using the results to measure real incremental media contribution and to inform investment-response-curve modeling and channel-optimization decisions. No specific percentage-lift figure for the described Mexico example was available in the source material reviewed for this entry.

**Potential:** geo-experimentation via synthetic control is broadly applicable to any company facing the "can't cleanly randomize at the user level" problem for market-level or channel-level decisions — not just media spend, but any policy, pricing, or product change that must be rolled out at a geographic or market granularity rather than a per-user one.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Established methodology, useful production adoption story

GeoLift and synthetic-control methods are well-established in the causal-inference and marketing-measurement literature; Mercado Libre isn't introducing a new method here, but is a useful, concrete case study of a large e-commerce/fintech platform operationalizing geo-experimentation as a repeatable in-house practice (roughly 20 experiments run) rather than a one-off analysis. The lack of published lift numbers limits how much can be independently verified from this specific write-up, but the operational maturity signal (institutionalizing it into their measurement stack) is itself the notable part.

### Similar / related work

- [**The Science of Price Experiments in the Amazon Store**](2026-09-08-amazon-price-experimentation.md) (in this bank) — another large e-commerce platform's systematic approach to a hard-to-randomize causal question (pricing), complementary to Mercado Libre's market-level media-measurement problem.
- [**Ladder of Evidence in Understanding Effectiveness of New Products**](2026-09-01-meta-ladder-of-evidence.md) (in this bank) — Meta's own framework for choosing the right causal-evidence method when a clean randomized experiment isn't available, directly relevant background for why geo-experimentation exists as a category.
- [**Using Marketplace Marginal Values to Address Interference Bias**](2026-09-11-lyft-interference-bias-mmv.md) (in this bank) — a different technique (marginal-value-based correction) for a related root problem: standard user-level A/B testing breaking down due to interference/contamination in a shared marketplace.

### Jargon buster

- **Geo-experimentation** — running an experiment where the unit of randomization is a geographic region (like a state or city) rather than an individual user, used when treatment can't be cleanly isolated at the user level.
- **Synthetic control** — a causal-inference technique that constructs an artificial comparison group by weighting a combination of untreated units so their historical trend matches the treated unit's pre-treatment trend, used to estimate what would have happened without the treatment.
- **GeoLift** — an open-source geo-experimentation methodology and toolkit (originally released by Meta) built specifically for measuring the incremental impact of marketing/media spend using geographic holdouts and synthetic control.
- **Incrementality** — the portion of an outcome (like app installs) that is actually caused by an intervention (like an ad campaign), as opposed to outcomes that would have happened regardless.
