---
id: nixtla-intermittent-demand-zero-forecast-trap
title: "The Forecast Says Zero. The Warehouse Says Otherwise."
source: "Nixtla Blog"
url: "https://www.nixtla.io/blog/intermittent-demand-zero-forecast-trap"
published: "2026-09"
added: "2026-09-25"
category: forecasting-timeseries
tags: [intermittent-demand, forecasting, croston, evaluation-metrics, inventory]
novelty: 3
sourced_via: "web search"
---

# The Forecast Says Zero. The Warehouse Says Otherwise.

**Source:** [Nixtla Blog](https://www.nixtla.io/blog/intermittent-demand-zero-forecast-trap) · Published 2026-09 · Added 2026-09-25
**Category:** Forecasting & Time Series · **Tags:** `intermittent-demand`, `forecasting`, `croston`, `evaluation-metrics`, `inventory`

## TL;DR

For sparse, intermittent demand series (mostly zeros with occasional spikes), a naive model that always predicts zero can score deceptively well on standard error metrics like MAE — while being operationally useless, since it never signals the rare demand spikes that actually drive stockouts and reorder decisions. Nixtla lays out why this happens and three fixes: occurrence/size-split methods (Croston's, TSB), evaluation metrics that reflect the real decision, and forward-looking exogenous signals.

## 1. Business context

Retail and industrial demand for many SKUs is intermittent by nature — a series like `0, 0, 0, 18, 0, 0, 0, 0, 12, 0, 0, 0` — and forecasting it well matters directly for inventory decisions: understock the item and miss the rare-but-real demand spike, overstock it and tie up capital or, for perishables, eat spoilage. The trap is that "accuracy" as conventionally measured doesn't align with "useful for the decision": a model that always predicts zero racks up a low mean absolute error simply because most periods genuinely are zero, so teams optimizing for standard accuracy metrics can end up shipping a forecaster that is statistically excellent and operationally worthless.

## 2. Technical details

The core mechanism: aggregate error metrics like MAE and WAPE penalize large misses heavily but say nothing special about *missing an event entirely* versus getting its timing or magnitude a bit wrong — since the vast majority of periods in an intermittent series are correctly zero, a naive always-zero model accumulates almost no error most of the time, and standard aggregate metrics reward that even though the model provides zero decision-useful signal for exactly the periods that matter. Nixtla's proposed fixes operate at three different levels: first, use forecasting methods purpose-built for intermittent demand — Croston's method and its refinement TSB (Teunter-Syntetos-Babai) — which explicitly separate the forecasting problem into two sub-questions (will demand occur in this period, and if so, how large will it be) rather than trying to fit one continuous-valued model to a fundamentally bursty process. Second, evaluate with metrics that actually reflect the decision the forecast supports — non-zero accuracy, demand-occurrence precision/recall, bias, service levels, and stockout frequency — instead of a single aggregate error number that a trivial zero-forecast can win. Third, feed the model forward-looking exogenous signals (planned promotions, known maintenance windows, upstream order schedules) that give it actual information to justify predicting a non-zero spike, rather than expecting it to infer bursts purely from noisy historical patterns.

## 3. Impact — potential & realized

The piece is presented as a diagnostic and prescriptive framework rather than a single case study with reported production numbers: it names the trap, explains the statistical mechanism that produces it, and gives three concrete, actionable fixes a forecasting team can apply directly. The broader value is preventive — a team that internalizes "check whether your model is just predicting zero and getting rewarded for it" before shipping an intermittent-demand forecaster avoids a failure mode that's easy to miss in an offline metrics dashboard and expensive to discover only after stockouts start happening in production.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-explained, practically useful restatement of a classic but under-discussed forecasting pitfall

Croston's method and the zero-inflation problem in intermittent demand forecasting are decades-old, well-established statistics — nothing methodologically new here. What earns this a solid score is how clearly the piece names a specific failure mode (a metric-optimal model that's decision-useless) that is genuinely easy for a team to fall into without noticing, especially teams that default to MAE/RMSE dashboards without asking whether the metric itself matches the business decision. It's a good complement to the deep-learning-forecasting pieces already in this bank, as a reminder that model sophistication doesn't fix a badly-chosen evaluation metric.

### Similar / related work

- [**Buy One Get One Free: Promotion-Aware Demand Forecasting for Groceries**](2026-09-23-afresh-promotion-aware-demand-forecasting.md) (in this bank) — a related grocery-forecasting failure mode (a model that's fine on average but breaks during the specific events that matter), addressed there with promo-aware features rather than an occurrence/size decomposition.
- [**Running Demand Forecasting Machine Learning Models at Scale**](2026-09-19-picnic-scalable-demand-forecasting.md) (in this bank) — another grocery-adjacent forecasting system; useful contrast in how different companies handle sparse/volatile SKU-level demand.
- **Croston's method / TSB (Teunter-Syntetos-Babai)** — the classic statistical methods this piece points to for intermittent demand; foundational reading predating this write-up by decades.

### Jargon buster

- **Intermittent demand** — a demand pattern where most periods have zero demand and the rest have occasional, often irregular, non-zero spikes — common for slow-moving SKUs, spare parts, and many grocery items.
- **Croston's method / TSB** — forecasting techniques for intermittent demand that separately model whether demand occurs in a period and, conditional on occurrence, how large it is, rather than fitting one model to the raw (mostly-zero) series.
- **MAE / WAPE** — Mean Absolute Error and Weighted Absolute Percentage Error, common aggregate forecast-accuracy metrics that this piece argues can be misleadingly "won" by a trivial always-zero forecast on intermittent series.
