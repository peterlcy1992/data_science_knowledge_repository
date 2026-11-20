---
id: amazon-window-lever-observation-windows-customer-forecasting
title: "The Window Lever: Longer Observation Windows Outweigh the Observed Effects of Data, Capacity, and Architecture in Customer Behavior Forecasting"
source: "Amazon (arXiv cs.LG)"
url: "https://arxiv.org/abs/2611.26521"
published: "2026-11"
added: "2026-11-20"
category: forecasting-timeseries
tags: [customer-behavior-forecasting, observation-window, history-length, matched-cohorts, pre-registration, sequence-models, ridge-probe, saturation-curve, calendar-confound]
novelty: 4
sourced_via: "full-text fetch"
---

# The Window Lever: Longer Observation Windows Outweigh the Observed Effects of Data, Capacity, and Architecture in Customer Behavior Forecasting

**Source:** [Amazon (arXiv cs.LG)](https://arxiv.org/abs/2611.26521) · Published 2026-11 · Added 2026-11-20
**Category:** Forecasting & Time Series · **Tags:** `customer-behavior-forecasting`, `observation-window`, `history-length`, `matched-cohorts`, `pre-registration`, `sequence-models`, `ridge-probe`, `saturation-curve`, `calendar-confound`

## TL;DR

Sowrirajan and Wang (Amazon) forecast each customer's 364-day forward activity from their event history. Going from an 8- to a 16-week observation window adds +0.070 to +0.107 log-space R² in all eight model families. The observed effects of 10× more customers, wider or deeper models, and newer sequence architectures are about an order of magnitude smaller (≤0.007). The authors call the window result a robust positive association: their design can't separate window length from calendar coverage.

## 1. Business context

Teams forecasting customer activity, such as lifetime value, churn or next-year engagement, usually spend effort on more data, bigger models and newer architectures. The history window is often fixed or treated as a capacity knob. Interventions ship sequentially on moving populations, so it is hard to tell which lever mattered. The paper runs a controlled, one-factor-at-a-time comparison on an internal Amazon export. It fixes the export, the test anchor weeks, the target (364-day forward activity, log(1+y), scored by log-space R²) and the evaluation. It then sweeps model family, population tier (nominal 1M/5M/10M), capacity, training objective and observation-window length. Four predictions were internally registered before the evaluations that decided them.

## 2. Technical details

- **Families.** Eight model families: transformer, GRU, LSTM, time-biased attention (a ContiFormer stand-in), a decay-gated recurrent model (Neural Hawkes stand-in), LightGBM boosted trees, a 6-feature ridge and a single-feature linear model. In the main runs the two continuous-time stand-ins had an inert clock (inter-event interval identically zero).
- **Window effect.** 8→16 weeks adds +0.070 to +0.107 log-space R² at the 1M tier in every family. The gain is similar across tiers: +0.0731 at 1M vs +0.0737 at 10M (3-seed, Huber).
- **Matched cohorts.** A longer window changes who is eligible to be scored. Re-scoring the same customer-weeks at every window gives Δ(M16−M8) = +0.096 matched vs +0.075 on the full set (Huber, seed 42), so the raw comparison understates the gain in every family covered. On internal data, longer windows also admit up to 10% more, and colder, training customers, which matching does not fix.
- **Other levers.** 1M→10M tier moves sequence models by ≤0.006. Doubling width or depth moves the metric by ≤0.005 at 8 weeks. Five sequence architectures at 16 weeks land within ~0.005 (0.5525 to 0.5474). The three-seed detection floor is 0.0059, so the authors call these axes 'bounded but unresolved', not nulls.
- **Time representation.** MS-RoPE is rotary encoding with frequencies constrained to hour/day/week/year bands. It gains +0.021 over their integer-position RoPE (3 seeds). Stacked with the best loss it reaches 0.6060±0.0006, about 96% of the additive gain.
- **Saturation by activity.** The pooled curve plateaus around 22–24 weeks. The top activity decile reaches half its gain at about 3.9 weeks. The bottom half shows no detectable bend within 16 weeks. Past 24 weeks the per-decile gains are small (+0.012 to +0.021), so 'allocate history by activity' holds only within roughly the first six months.
- **Confound.** All test anchors fall in one ~8-week band (2025-02-24, 03-24, 04-21), so a longer window also reaches back into the holiday period. An anchor-varying control was voided by its own pre-registered criterion. A ridge probe on training-period anchors keeps about 72% of its gain on holiday-free anchors. Of the four registered predictions, the only fully blind one failed: an activity-mixture model predicted +0.014 from 24→32 weeks, and the probe returned −0.0004.

## 3. Impact — potential & realized

**Measured:**
- 8→16-week window: +0.070 to +0.107 log-space R² across eight families, vs ≤0.007 for scale, capacity and architecture.
- Matched-cohort window gain of +0.096 (vs +0.075 raw). The same pattern holds at 10M (+0.094 vs +0.075).
- The direction replicates on five public datasets: Taobao (9 days), Online Retail II, dunnhumby Complete Journey, CDNOW and H&M, with ridge and the transformer on all five.
- MS-RoPE: +0.021, nearly additive with the objective gain.

**Potential:** An ordering of levers for anyone building customer-level forecasts on event logs: lengthen the window first, score window comparisons on matched cohorts, and size history per activity level. It is also a template for reporting ML comparisons honestly, with registered falsifiers, detection floors and 'bounded but unresolved' rather than 'no effect'.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — An unusually careful lever comparison whose headline is actionable on Monday

The result itself (history length beats scale) will be familiar to anyone who has built RFM or BTYD-style features. The contribution is the method. The authors use matched cohorts to remove the selection bias that a longer window introduces. They pre-register falsifiers and report the one that failed. They give a detection floor and refuse to call sub-floor effects nulls. And they admit that calendar coverage and window length are confounded rather than burying it. That is the standard applied DS comparisons should meet.

Limits: one internal export, one target, three test anchors in an eight-week band, many single-seed numbers, and continuous-time baselines whose clocks were inert in the main runs. The practical advice ('start by lengthening the window') is well supported. The causal magnitude of a calendar-independent history effect is not, and the paper says so.

### Similar / related work

- [**t0: A Time-Series Foundation Model for Forecasting with Context**](2026-10-13-arxiv-t0-time-series-foundation-model-context.md) (in this bank) — another look at how much context a forecaster should see, from the foundation-model side.
- [**The Hidden Look-Ahead: Point-in-Time Leakage in Electricity Market Data**](2026-10-29-arxiv-point-in-time-leakage-electricity-forecast-archives.md) (in this bank) — a companion warning that evaluation design (what data the model 'sees') can dominate model choice.
- **Fader, Hardie & Lee (2005), 'Counting Your Customers the Easy Way'** — the BTYD/Pareto-NBD tradition of customer-activity forecasting that the paper cites as its task lineage.

### Jargon buster

- **Observation window** — the weeks of a customer's history the model sees before the week it forecasts from.
- **Matched cohort** — scoring every window setting on exactly the same customer-weeks, so a longer window can't change who is evaluated.
- **Log-space R²** — R² computed on log(1+y), which stops a few very heavy customers from dominating the score.
- **Detection floor** — the smallest difference the experiment can reliably distinguish from seed noise; effects below it are 'unresolved', not zero.
- **RoPE** — rotary positional encoding; MS-RoPE pins its frequencies to physical time scales such as days, weeks and years.
