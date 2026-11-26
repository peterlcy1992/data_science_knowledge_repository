---
id: arxiv-covnovbench-time-series-foundation-models-covariate-novelty
title: "CovNovBench: A Benchmark for Evaluating Time Series Foundation Models under Covariate Novelty"
source: "University of Washington / Amazon Science (arXiv cs.LG, stat.ME)"
url: "https://arxiv.org/abs/2611.33732"
published: "2026-11"
added: "2026-11-26"
category: forecasting-timeseries
tags: [time-series-foundation-models, covariate-novelty, interventional-forecasting, benchmark, zero-shot-forecasting, chronos-2, tabpfn-ts, out-of-support-extrapolation, directional-accuracy, rmsse]
novelty: 3
sourced_via: "full-text fetch"
---

# CovNovBench: A Benchmark for Evaluating Time Series Foundation Models under Covariate Novelty

**Source:** [University of Washington / Amazon Science (arXiv cs.LG, stat.ME)](https://arxiv.org/abs/2611.33732) · Published 2026-11 · Added 2026-11-26
**Category:** Forecasting & Time Series · **Tags:** `time-series-foundation-models`, `covariate-novelty`, `interventional-forecasting`, `benchmark`, `zero-shot-forecasting`, `chronos-2`, `tabpfn-ts`, `out-of-support-extrapolation`, `directional-accuracy`, `rmsse`

## TL;DR

Covariate-aware time-series foundation models (TSFMs) are being used to ask "what if we set this price or this treatment?". Often the planned value lies outside anything the series has seen. CovNovBench labels that case per series ("covariate novelty") and builds 88,476 evaluation series from four simulated and real sources. Six frozen TSFMs were run zero-shot. Point error rose over the in-distribution baseline in 52 of 54 matched comparisons. Directional accuracy often sat near the coin-flip level of 0.5. No model or model family was consistently best.

## 1. Business context

Recent TSFMs (Chronos-2, TimesFM-2.5, Moirai-1.1, and tabular models such as TabPFN-TS) accept covariates supplied over the forecast horizon. When those covariates are planned actions, the model becomes a zero-shot "what-if" tool. Examples are a new pricing policy or a new patient treatment schedule. The authors call such inputs *treatment covariates*. They call the task *interventional forecasting*.

There are two gaps. First, these models target the observational conditional. They treat the future treatment path as passively observed, so their forecasts "need not represent the interventional conditional". Second, the plans people care about often leave the history. A 40% discount after only discounts under 20%. A product's first-ever discount. Replacing a discount with buy-one-get-one. The paper calls this setting "practically common" and says it is "not systematically represented in existing benchmarks". CancerTreatment and fev-bench do not label evaluation series by covariate novelty.

The paper is a workshop benchmark (Foundation Models for Temporal Systems). It evaluates frozen models as observational baselines, not as causal forecasters.

## 2. Technical details

- **Definition.** For each treatment covariate, compare its future value set with its historical value set *within the same series*. A numerical covariate's set is its [min, max] range. A categorical covariate's set is its active (nonzero) values. The path is In-Distribution (ID) if every future set is contained in the historical one. Otherwise it is novel. Novelty is not judged against other series or pretraining data.
- **Three novelty scenarios.**
  - *Out-of-Support (OOS):* a numerical range goes below the historical min or above the max.
  - *Policy-Onset:* an active policy appears after an inactive history.
  - *Policy-Switch:* an unseen active policy follows an active history.
- **Datasets (T/H = history/horizon length):**
  - *CancerTreatment* (synthetic): adapted Geng et al. PK/PD tumor-growth simulator, log tumor volume target, radio/chemo policy plus doses. It supports all four scenarios. 12,548 series, T/H 50/10. In-range doses are [1,2] for radio and [3,5] for chemo. Treatment assignment depends on recent tumor diameter, which creates controlled time-varying confounding.
  - *CausalRivers* (real): RiversEastGermany, 666 gauges and 651 directed edges, 2019–2023. The target is downstream discharge, with lagged upstream discharge as the treatment. Pair, chain and confluence subgraphs, 6-hour means. 38,992 series, T/H 100/20. A normalized deviation score d sets the bands: ID if d < 0.1, moderate OOS if 0.1 ≤ d < 1, extreme OOS if d ≥ 1. The topology gives a physical direction but "not an identified intervention effect".
  - *MIMIC3-Real* (real): diastolic blood pressure from vasopressor/ventilation indicators, via MIMIC-Extract. 7,936 series, T/H 30/10. Its treatment associations are "suggestive, not causally identified" because of confounding by indication.
  - *MIMIC3-Synth* (semi-synthetic): real vitals plus three simulated binary treatments and a simulated outcome, following the Causal Transformer setup. 29,000 series, T/H 50/10.
- **Matched design.** Scenario-subset registries are fixed before generation or filtering. Where possible, ID and novel subsets share the same historical treatment settings. Policy-Onset has no ID counterpart. The primary evidence is same-model, same-dataset comparison against ID.
- **Metrics.** RMSSE scales error by the historical one-step change, so 1 is the reference. DA is the share of horizon steps where the predicted direction of change matches the real one. CDA computes DA only at treatment-transition steps (policy changes or reversals in numerical direction). The random-direction reference for DA and CDA is 0.5. The median quantile is the point forecast.
- **Models.** Three tabular-family models: TabPFN-TS, TabICL-v2, and ApolloPFN (a closed Amazon checkpoint). Three non-tabular: Chronos-2, TimesFM-2.5 (200M), Moirai-1.1-R-large. All are frozen and zero-shot, with no fine-tuning or retrieval. Each runs once with a fixed seed.
- **Compute.** 78 model–dataset–scenario runs on one AWS p4d.24xlarge (8× A100) took 3.78 hours of forward passes. TabICL-v2 accounted for 9,331 s. Chronos-2 took 302 s.

## 3. Impact — potential & realized

**Measured (point error):**
- All benchmark-wide weighted RMSSE averages exceed 1.
- RMSSE was higher than ID in 52 of 54 matched comparisons. The two exceptions were TimesFM-2.5 and Moirai-1.1 on MIMIC3-Synth Policy-Switch.
- CancerTreatment Policy-Onset is the hardest cell. RMSSE is 23.05 (ApolloPFN) to 30.83 (Chronos-2), against about 0.53–1.06 at ID. That is roughly 24–57× the ID value.
- On CausalRivers, RMSSE rises from moderate to extreme OOS for every model. Chronos-2 goes from 1.06 (ID) to 1.90 (moderate) to 5.41 (extreme). TimesFM-2.5 reaches 9.44 and Moirai-1.1 9.56 at extreme OOS.
- Ratios are smaller on MIMIC3-Real. For example, TabPFN-TS goes from 0.53 (ID) to 0.65 (Switch) to 0.82 (Onset).

**Measured (direction):**
- Many DA and CDA means are near 0.5. Moirai-1.1's averages stay between 0.44 and 0.51 in every scenario.
- On CancerTreatment Policy-Onset, CDA is well below chance for most models: 0.209 for TimesFM-2.5, 0.217 for Chronos-2 and 0.233 for TabICL-v2. Only ApolloPFN is above 0.5, at 0.571.
- Directional changes under novelty are "non-uniform". On the Policy-Switch average, TimesFM-2.5 has the best CDA (0.712), while TabICL-v2 has the best DA (0.677).

**Measured (who wins):**
- Chronos-2 has the best mean in all nine CausalRivers cells (numerical treatment, trending target).
- Tabular models have the best mean in 16 of 18 MIMIC cells (binary treatments, stable target).
- On CancerTreatment, tabular models have the lowest RMSSE in all four scenarios, but directional winners vary.
- The authors call these "descriptive associations because dataset characteristics vary jointly".

**Limits stated:** one fixed benchmark realization with no repeated-run uncertainty. No pretraining-contamination audit. No code, data or model is released, because of company policy. MIMIC data need credentialed access. ApolloPFN is closed.

**Potential:** the benchmark is a testbed for TSFMs that "forecast more reliably under covariate novelty". The authors suggest two directions. One is retrieval-augmented few-shot forecasting over series where the novel treatment was observed. The other is conditioning on text descriptions of each treatment and its expected effect.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sharp, useful labeling idea; a thin, unreleased benchmark

The core contribution is a simple, operational per-series label: does the planned future treatment leave this series' own history? It is split into Out-of-Support, Policy-Switch and Policy-Onset. That framing is a clean fit for how planners actually use these models, and nobody had standardized it. The matched ID-vs-novel design is the right primary comparison. The authors are careful to treat model outputs as observational forecasts, not causal estimates.

Against that: there is no new method, and the evaluation is one seed per model with no uncertainty. Two of the four sources (CausalRivers and MIMIC3-Real) have no identified causal effect. The datasets are clinical and hydrological rather than commercial. Nothing is released, which matters a lot for a benchmark paper. For tech DS teams (my mapping): if you feed planned prices, promotions or capacity into Chronos-2 or TabPFN-TS, add this check to your own backtests. Tag each forecast by whether its future covariates leave the series' history, and report error and direction accuracy separately for those slices. The Policy-Onset result (first-ever treatment, direction worse than a coin flip for most models) is a good reason not to trust zero-shot what-ifs for launches without a causal model or comparable treated series.

### Similar / related work

- [**Benchmarking Time Series Foundation Models for Load Forecasting Under Covariate Uncertainty**](2026-10-12-arxiv-tsfm-load-forecasting-covariate-uncertainty.md) (in this bank) — a load-forecasting benchmark that varies whether future covariates are missing, known or noisily forecast. It asks a different covariate-robustness question: noisy inputs rather than novel ones. It also finds Chronos-2 strong when covariates are good.
- [**fev-bench: A Realistic Benchmark for Time Series Forecasting**](https://arxiv.org/abs/2509.26468) — Shchur et al. A general benchmark that includes covariate-aware tasks but does not label series by covariate novelty.
- [**Causal Forecasting for Pricing**](https://arxiv.org/abs/2312.15282) — Schultz et al. An earlier study of demand forecasting under changed pricing policies, and part of the interventional-forecasting motivation here.
- [**Does Predictive Performance Translate to Causal Performance? Evaluating tabular foundation models as nuisance learners for causal effect estimation**](2026-11-11-arxiv-tabular-foundation-models-nuisance-learners-causal-estimation.md) (in this bank) — a related warning that strong predictive foundation models do not automatically give good causal answers, in a tabular rather than time-series setting.

### Jargon buster

- **Covariate-aware TSFM** — a pretrained forecasting model that also takes extra input series (prices, doses, weather), including their values over the forecast horizon, with no task-specific training.
- **Treatment covariate** — an input that encodes an action or exposure expected to causally affect the target, such as a discount or a drug dose.
- **Interventional forecasting** — predicting the target when the future input path is *set* by a decision (the do-operator), not merely observed.
- **Covariate novelty** — the planned future values of a treatment covariate fall outside that same series' historical range or set of active policies.
- **RMSSE** — root mean squared scaled error. Forecast error divided by the typical one-step change in the history, so values above 1 are worse than that baseline scale.
- **Directional accuracy (DA / CDA)** — the share of steps where the forecast gets the up/down direction right. CDA counts only the steps where the treatment changes. 0.5 is the random-guess level.
