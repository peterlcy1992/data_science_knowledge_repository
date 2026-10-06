---
id: arxiv-bayesian-reconciliation-overlapping-forecasts
title: "Bayesian Reconciliation of Overlapping Multi-Step Forecasts: A Post-Processing Framework for Cross-Origin Coherence"
source: "arXiv (Fajana, Ehlers, Andrade)"
url: "https://arxiv.org/abs/2610.05340"
published: "2026-10"
added: "2026-10-06"
category: forecasting-timeseries
tags: [forecast-reconciliation, state-space, bayesian, multi-step-forecasts, prediction-intervals]
novelty: 3
sourced_via: "web search"
---

# Bayesian Reconciliation of Overlapping Multi-Step Forecasts: A Post-Processing Framework for Cross-Origin Coherence

**Source:** [arXiv (Fajana, Ehlers, Andrade)](https://arxiv.org/abs/2610.05340) · Published 2026-10 · Added 2026-10-06
**Category:** forecasting-timeseries · **Tags:** `forecast-reconciliation`, `state-space`, `bayesian`, `multi-step-forecasts`, `prediction-intervals`

## TL;DR

A model-agnostic Bayesian state-space post-processor that treats forecasts for the same target date, issued from different origins, as noisy and biased measurements of one latent trajectory, reducing cross-origin incoherence.

## 1. Business context

Rolling forecasting systems, including ML and deep-learning ones, issue a new multi-step forecast every period, so the same future date gets different predictions from different forecast origins. Downstream planners see revisions that contradict each other ("cross-origin incoherence") even though the model never changed.

## 2. Technical details

The framework models overlapping forecasts as measurements of a common latent trajectory in a state-space model with horizon-specific bias and uncertainty. It needs no access to the base model's architecture, parameters or training data. Validated in controlled simulations, an S&P 500 volatility application, and an LSTM experiment showing it applies to deep-learning forecasters.

## 3. Impact — potential & realized

Per the abstract: simulations show substantial reductions in incoherence and accurate latent-trajectory recovery. In the S&P 500 volatility application, 90% prediction-interval coverage moved from 94.8% to 88.3% (closer to the 90% nominal target), though point-forecast error increased. Full paper not read.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Interesting framing (revisions as measurement noise) and honest about the trade-off: better calibrated intervals, worse point error.

Interesting framing (revisions as measurement noise) and honest about the trade-off: better calibrated intervals, worse point error. Niche but relevant to anyone whose planners complain about forecast "churn". Evidence is simulation plus one financial application.

### Similar / related work

- **Hierarchical / temporal forecast reconciliation literature** — related coherence-enforcing methods (no specific URL linked)
- **Forecast revision and vintage analysis** — general literature on how forecasts change across origins (no specific URL linked)

### Jargon buster

- **Forecast origin** — The date at which a forecast is made.
- **Cross-origin incoherence** — Different origins giving conflicting predictions for the same target date.
- **State-space model** — A model with a hidden evolving state observed through noisy measurements.
