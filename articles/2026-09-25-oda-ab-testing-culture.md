---
id: oda-ab-testing-culture
title: "Oda's Online Experimentation Journey: Lessons Learned and Best Practices"
source: "Oda Product & Tech (Medium) / GrowthBook customer case study"
url: "https://medium.com/oda-product-tech/odas-online-experimentation-journey-lessons-learned-and-best-practices-7091c318beeb"
published: "2024-04"
added: "2026-09-25"
category: experimentation-causal
tags: [ab-testing, experimentation-platform, warehouse-native, cuped, bayesian, culture]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Oda's Online Experimentation Journey: Lessons Learned and Best Practices

**Source:** [Oda Product & Tech (Medium) / GrowthBook customer case study](https://medium.com/oda-product-tech/odas-online-experimentation-journey-lessons-learned-and-best-practices-7091c318beeb) · Published 2024-04 · Added 2026-09-25
**Category:** Experimentation & Causal Inference · **Tags:** `ab-testing`, `experimentation-platform`, `warehouse-native`, `cuped`, `bayesian`, `culture`

## TL;DR

Oda, Norway's largest online grocery retailer, replaced a homegrown Postgres-and-hard-coded-flags experimentation setup with a warehouse-native platform (GrowthBook, on top of Snowflake/dbt/Snowplow) in 2021, scaling to 400+ experiments run and roughly 50 active at any time. The bigger story isn't the tooling swap itself but the cultural shift it enabled: experimentation went from a "big, hard thing" owned by a specialist team to a routine part of how engineers, PMs, and growth managers ship product.

## 1. Business context

As an online grocer, Oda's product changes routinely trade off against each other — a change that lifts engagement can hurt margins, operational efficiency, or delivery reliability, so the company needed a way to evaluate changes on multiple guardrail dimensions (customer, marketplace, operational, trust) rather than optimizing a single metric blind. Its original experimentation setup was homegrown: hard-coded feature flags on top of PostgreSQL, with post-experiment analysis described internally as laborious. That friction meant experimentation stayed a "big, hard thing" reserved for major bets rather than a routine tool, which is exactly the opposite of what a company trying to build "the world's most efficient retail system" through continuous iteration needs.

## 2. Technical details

Oda adopted GrowthBook in 2021 specifically because it could sit on top of the data stack Oda already had — Snowflake as the warehouse, with metrics already built in dbt from Snowplow event data — rather than forcing a migration to a vendor's own data pipeline. That warehouse-native approach meant experiment results could still be sliced in the tools the team already used (Looker, Jupyter) and avoided duplicating event data into a third-party system. Statistically, Oda's default approach is Bayesian rather than frequentist significance testing, and the team explicitly named CUPED-style variance reduction (using pre-experiment behavior as a covariate to shrink noise) and multi-armed bandits as near-term areas they are investing in to make tests faster and more reliable, alongside guardrail metrics spanning customer, marketplace, operational, and trust dimensions with pre-set minimum-effect-worth-acting-on thresholds and planned durations.

## 3. Impact — potential & realized

Oda reports running 400+ experiments to date, with about 50 active and up to 10 receiving deeper statistical analysis at any given time — evidence the program scaled well past a handful of showcase tests. One concretely cited result: a recommendation-algorithm refinement, iterated through A/B testing, drove 16-17% usage growth; the company's loyalty program was likewise built up over months of testing before full launch. Fredrik Jørgensen, Oda's Head of Insight for Retail Platform, frames the bigger payoff as cultural: "Our culture has totally changed. Experimentation went from 'big, hard thing' to standard" — with faster feedback loops making teams more willing to try things in the first place.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A solid, well-documented case study of experimentation-program maturity rather than a new method

There's no new statistical technique here — CUPED and Bayesian testing are established practice, and warehouse-native experimentation platforms (GrowthBook, Eppo, Statsig) are now a well-trodden category. The value of this write-up is as a template for the *organizational* side of experimentation: how a mid-sized company moved from ad hoc, engineer-only testing to a program with guardrail metrics, minimum-detectable-effect discipline, and genuine cross-functional adoption, and what specifically (warehouse integration, faster iteration) drove that adoption curve rather than a tooling mandate alone.

### Similar / related work

- [**How Booking.com Increases the Power of Online Experiments with CUPED**](https://booking.ai/how-booking-com-increases-the-power-of-online-experiments-with-cuped-995d186fff1d) — the canonical production CUPED write-up; useful contrast for teams considering Oda's stated next step of adding variance reduction.
- [**The Science of Price Experiments in the Amazon Store**](2026-09-08-amazon-price-experimentation.md) (in this bank) — another company narrative built around guardrail-metric discipline in a margin-sensitive, operationally constrained domain (retail/e-commerce pricing vs. Oda's grocery logistics).
- [**Harnessing the Power of Geo-Experimentation: How Mercado Libre Measures the Effectiveness of Its Third-Party Media Strategies Using GeoLift**](2026-09-13-mercadolibre-geo-experimentation-geolift.md) (in this bank) — a different company's experimentation-maturity story, this time built around a geo-based quasi-experimental method rather than classic randomized A/B testing.

### Jargon buster

- **Warehouse-native experimentation** — running an A/B testing platform directly against a company's existing data warehouse (e.g., Snowflake) and metric definitions, instead of routing event data into a separate vendor-hosted analytics pipeline.
- **CUPED (Controlled-experiment Using Pre-Experiment Data)** — a variance-reduction technique that uses a user's pre-experiment behavior as a covariate to shrink the noise in an experiment's outcome metric, letting the same sample size detect smaller effects.
- **Guardrail metric** — a metric a team commits to *not* letting get worse during an experiment (e.g., delivery reliability, margin), even while optimizing a separate primary metric.
