---
id: meta-forecasting-art-and-science
title: "Forecasting@Meta: Balancing Art and Science"
source: "Analytics at Meta (Medium)"
url: "https://medium.com/@AnalyticsAtMeta/forecasting-meta-balancing-art-and-science-92526e1ae36c"
published: "2024-05"
added: "2026-08-31"
category: forecasting-timeseries
tags: [forecasting, backtesting, product-impact, judgment, statistics]
novelty: 2
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Forecasting@Meta: Balancing Art and Science

**Source:** [Analytics at Meta (Medium)](https://medium.com/@AnalyticsAtMeta/forecasting-meta-balancing-art-and-science-92526e1ae36c) · Published 2024-05 · Added 2026-08-31
**Category:** Forecasting & Time Series · **Tags:** `forecasting`, `backtesting`, `product-impact`, `judgment`

## TL;DR

Meta's Analytics team lays out how they combine statistical forecasting
models with human judgment in production: validating forecasts through
backtesting, and deciding when and how to manually incorporate known product
impact (e.g. from an experiment holdout) on top of what the model predicts.

## 1. Business context

Large organizations run forecasts that feed real planning and resourcing
decisions, and a purely model-driven number can miss context a forecaster
knows but the model doesn't — an upcoming feature launch, a known seasonal
quirk, a one-off event. Relying purely on human judgment, on the other hand,
reintroduces bias and inconsistency. Meta frames its forecasting practice as
deliberately balancing these two failure modes rather than picking one side.

## 2. Technical details

- **Validation via backtesting.** Forecasts are checked by **backtesting**
  against historical data as a sanity check on whether the modeling approach
  behaves sensibly before being trusted going forward.
- **Incorporating product impact.** When Meta has an experiment holdout with
  reasonably high confidence in a feature's causal impact, that estimated
  impact is **incorporated directly into the forecast**, in addition to
  whatever the base model predicts.
- **Avoiding double-counting.** This incorporation step requires explicitly
  assessing confidence in the impact measurement itself; to avoid
  double-counting, the team either **subtracts the prior known product
  impact from historical training data** before fitting, or **measures rough
  incrementality** in a way designed to minimize disruption to the model's
  fidelity.
- **The art/science framing.** The post frames the tension as: modern
  algorithms can find complex patterns and cut through human bias, but
  forecasting also benefits from domain knowledge and expertise that isn't
  easily encoded into a model — the practice sits at the intersection of
  relying on the model and relying on expert judgment, rather than choosing
  one exclusively.

## 3. Impact — potential & realized

- **Realized:** A described, in-production process at Meta for validating
  forecasts (backtesting) and folding known product impact into forecasts
  without double-counting.
- **Potential:** A reusable playbook for any forecasting team facing the same
  tension between trusting a statistical model and incorporating known,
  judgment-based information (like a measured feature launch effect) that the
  model can't see on its own.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — a clear, useful practitioner write-up of established practice

There's no new method here — backtesting and manually adjusting a forecast
for known upcoming effects are standard forecasting practice going back
decades. The value is in the clear articulation of *how* to avoid
double-counting when blending a measured experiment effect into a
statistical forecast, which is a genuinely easy mistake to make in practice,
but that's a useful recap rather than a novel technique.

### Similar / related work

- **How We Knew COVID Was Over (and What Our Models Had to Unlearn)** at
  Airbnb (in this bank) — another large-platform forecasting team's account
  of when to trust versus override a statistical model during unusual
  conditions.
- **Forecasting the Evolving Composition of Guest Origin Markets in Platform
  Bookings** (arXiv 2602.18358) — a more technical, methods-first companion
  on hierarchical/compositional forecasting for a similar class of problem.
- Standard time-series forecasting practice (e.g. Meta's own Prophet library
  documentation) — this post is a practitioner-process complement to that
  more technical tooling.

### Jargon buster

- **Backtesting** — evaluating a forecasting approach by simulating it
  against historical data and checking how well it would have predicted
  known outcomes.
- **Experiment holdout** — a control group deliberately excluded from a
  feature rollout so its impact can be measured by comparison.
- **Incrementality** — the portion of an observed outcome that is genuinely
  caused by an intervention, as opposed to something that would have
  happened anyway.
- **Double-counting** — accidentally including the same effect twice in an
  estimate, here by having both the model and a manual adjustment separately
  account for the same known impact.
