---
id: datadog-how-we-built-datadog-experiments
title: "How we built Datadog Experiments"
source: "Datadog Engineering Blog"
url: "https://www.datadoghq.com/blog/how-we-built-datadog-experiments/"
published: "2026-09"
added: "2026-11-27"
category: experimentation-causal
tags: [experimentation-platform, cuped, variance-reduction, percentile-metrics, segments, global-lift, coverage, warehouse-native, eppo, reproducibility]
novelty: 3
sourced_via: "full-text fetch"
---

# How we built Datadog Experiments

**Source:** [Datadog Engineering Blog](https://www.datadoghq.com/blog/how-we-built-datadog-experiments/) · Published 2026-09 · Added 2026-11-27
**Category:** Experimentation & Causal Inference · **Tags:** `experimentation-platform`, `cuped`, `variance-reduction`, `percentile-metrics`, `segments`, `global-lift`, `coverage`, `warehouse-native`, `eppo`, `reproducibility`

## TL;DR

After acquiring Eppo, Datadog rebuilt its experimentation side as Datadog Experiments. The post covers four changes. CUPED was reworked from per-variant regression adjustment into "metric augmentation", which lets one set of global coefficients give unbiased adjusted results for any segment and extends to percentile metrics such as p90. Global lift is now defined as Coverage × Local lift, so it can be checked by hand and works for windowed metrics. "Copy SQL" exposes the warehouse query behind a number, and RUM and Product Analytics metrics give an early signal that updates about every 15 minutes.

## 1. Business context

Datadog usually rebuilds an acquired product rather than plugging it in as is. Eppo was an experimentation and feature-management platform. Its feature management became Datadog Feature Flags; its experimentation became Datadog Experiments. This post covers only the experimentation side.

Experiments analyzes randomized experiments (A/B tests) next to observability data. Warehouse-native metrics "often act as the primary basis for decision making", but RUM (Real User Monitoring) and Product Analytics data can also feed experiment metrics.

The stated goal of the rebuild is to move "from an experiment result to a confident decision more quickly". The post names four levers: statistical efficiency, interpretable impact, verifiability and faster feedback. Each maps to a pain point in the old Eppo product:

- CUPED could not be extended to segments without refitting a model per segment.
- Global lift and coverage were reported separately and did not combine.
- About 20 pipeline steps sat between raw tables and a reported result, so customers often sent their queries to the Eppo team to debug discrepancies.
- Results came from the warehouse on a schedule, and business metrics such as revenue or retention "can land hours later".

## 2. Technical details

**CUPED, Eppo version.** Regression adjustment with a separate subject-level model for each variant. The lift estimate was unbiased only for the population used to fit those models. Each segment would have needed its own refit, which made segment-level CUPED impractical.

**CUPED as metric augmentation.** The new model is "inspired by CUPED's original authors, who describe the method as a metric augmentation rather than a regression adjustment".
- Start from the unadjusted lift. Add adjustment terms chosen to average out to zero over many randomizations.
- Because the terms are zero in expectation, they add no bias but can reduce variance.
- A single set of coefficients gives zero-expectation adjustments for any segment. One model run, reusing the global coefficients, yields unbiased CUPED-adjusted results for any segment.
- The post says this "generally reduces variance" and keeps segment results consistent with the overall result.
- Example (waterfall figure): raw lift 16.09% is adjusted term by term to a CUPED-adjusted lift of 12.96%. The estimated run time drops by 51.97% ("about 52%").

**CUPED on percentiles.** Regression-based CUPED does not naturally extend to percentiles, because there is no obvious subject-level outcome to predict. Augmentation removes that limit: the ordinary p90 gets adjustment terms like any other metric. The post claims variance reduction on percentiles "has long been out of reach for commercial experimentation platforms". It does not give the form of the percentile adjustment terms or how their variance is estimated.

**Global lift.** Global lift estimates how the company-wide metric total would change if the treatment went to every eligible user. Applying the relative lift to the whole total assumes every user is affected and overstates the effect when only a fraction are.
- At Eppo, global lift and coverage were computed separately. Multiplying coverage by local lift did not reproduce the reported global lift.
- Eppo's global lift did not extend to windowed metrics. Users had to build a second, unwindowed metric, which might have a different local lift.
- New definition: **Global lift = Coverage × Local lift**. Local lift is the relative lift among enrolled subjects. Coverage is the share of the company-wide metric total that the experiment's eligible users account for.
- Worked example: 50% coverage × 10% local lift on revenue = 5% global lift. The product screenshot shows 13.0% relative lift, 40.3% coverage and 5.23% global lift.
- Coverage is computed separately from global lift, not inside it. That is why global lift now works for windowed metrics.

**Copy SQL.** For warehouse-native metrics, the user can copy the query behind a number and run it in their own warehouse. The query shows the pipeline's steps as named stages.
- A copied query "lands very close to the dashboard number". Small differences can arise because the pipeline is incremental and data can arrive late.
- Copy SQL reproduces results for metrics *without* CUPED adjustment only.
- Separately, diagnostic checks run before results are interpreted, flagging e.g. a traffic imbalance between variants or a metric with no data.

**Behavioral and performance metrics.** Metrics can be built from RUM and Product Analytics events (pageviews, clicks, errors) across web and mobile. APM Spans metrics are in Preview. RUM and Product Analytics metrics update in near real time, "typically about every 15 minutes", without separate streaming infrastructure. Warehouse metrics stay as they are. Within minutes of launch, users can also watch Session Replays of the first exposed users; the post notes confidence intervals are still wide at that stage.

## 3. Impact — potential & realized

**Realized (as reported).** The post gives one quantitative result: in an example experiment, CUPED variance reduction shortened the estimated run time by about 52%. There is no aggregate figure across customers or experiments, and no benchmark of percentile CUPED against unadjusted percentiles. The other changes are described as product capabilities, not measured outcomes.

**Potential.**
- Segment results that use the same global coefficients stay consistent with the topline, so slicing does not produce a segment story that contradicts the overall result through model refits.
- Percentile guardrails (e.g. p90 page load time) could guard a rollout "on less traffic than an unadjusted percentile would need". The post says a latency spike "can be caught sooner and rolled back faster".
- A multiplicative, inspectable global lift makes impact reporting auditable, including for windowed metrics.
- Copy SQL moves result debugging from the vendor's support team to the customer's own analysts, for non-CUPED metrics.
- RUM and Product Analytics metrics give an early check that a change has not broken something before warehouse metrics arrive.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A well-argued platform rebuild; percentile CUPED via augmentation is the interesting bit, but its details stay off the page

The most useful idea is reframing CUPED from per-variant regression to zero-mean augmentation. That framing is old; the post credits the original CUPED authors. What is practical is the consequence: one set of global coefficients gives valid adjustment for any segment, and percentiles become adjustable. The percentile claim is the boldest and the least documented. The post does not say how the adjustment terms for a quantile are built (an influence-function or linearization approach would be the natural route, but that is my guess) or how variance is estimated. Nor does it report how much variance reduction percentiles get in practice. "Unbiased" for segments also presumably means in expectation over randomizations, with variance gains that may shrink when global coefficients fit a segment poorly. The post says "generally reduces variance", which is honest.

The global lift fix is simple but valuable. Many platforms report a "company-wide impact" number that cannot be reconstructed. Making it a visible product of two readable factors is the kind of thing other platform teams should copy. Copy SQL is similar: good practice for warehouse-native tools, though the non-CUPED limitation matters, since adjusted numbers are usually the ones teams decide on.

This is a product post from a vendor. Treat the single 52% run-time example as an illustration, not evidence of typical gains.

### Similar / related work

- [**Ensuring Trustworthy Online A/B Testing: Addressing Five Key Questions on CUPED**](2026-10-02-arxiv-cuped-five-questions-bytedance.md) (in this bank) — ByteDance's practical treatment of CUPED estimator choice and variance estimation; useful background for judging augmentation-style CUPED claims.
- [**Under the Hood of Uber's Experimentation Platform**](2026-09-29-uber-under-the-hood-experimentation-platform-xp.md) (in this bank) — another in-house platform write-up with a CUPED-based stats engine, for comparison of platform design choices.
- [**Oda's Online Experimentation Journey: Lessons Learned and Best Practices**](2026-09-25-oda-ab-testing-culture.md) (in this bank) — a customer-side view of adopting a warehouse-native experimentation platform, the same deployment model Copy SQL targets.
- **Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data** — Deng, Xu, Kohavi & Walker (WSDM 2013). The original CUPED paper, whose authors the post credits with the augmentation framing.

### Jargon buster

- **CUPED** — Controlled-experiment Using Pre-Experiment Data: uses each subject's pre-experiment data to cut metric variance, so confidence intervals tighten and tests finish sooner.
- **Metric augmentation** — adding terms to an estimate that average to zero across randomizations; they leave it unbiased but can lower its variance.
- **Regression adjustment** — fitting a model of the outcome on covariates and using it to adjust the treatment-effect estimate; here, one model per variant.
- **Local lift** — the relative lift among subjects enrolled in the experiment.
- **Coverage** — the share of the company-wide metric total that the experiment's eligible users account for.
- **Global lift** — the estimated change in the company-wide total if the treatment went to all eligible users; here Coverage × Local lift.
- **Windowed metric** — a metric measured over a fixed window relative to each subject's exposure (e.g. revenue in the first N days).
- **RUM (Real User Monitoring)** — front-end telemetry from real users' sessions, such as page loads, clicks and errors.
