---
id: grab-ml-predictive-autoscaling-flink
title: "Machine-Learning Predictive Autoscaling for Flink"
source: "Grab Engineering Blog"
url: "https://engineering.grab.com/ml-predictive-autoscaling-for-flink"
published: "2025-10"
added: "2026-09-21"
category: ml-infra-serving
tags: [flink, autoscaling, time-series-forecasting, stream-processing, kafka, cost-optimization]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Machine-Learning Predictive Autoscaling for Flink

**Source:** [Grab Engineering Blog](https://engineering.grab.com/ml-predictive-autoscaling-for-flink) · Published 2025-10 · Added 2026-09-21
**Category:** ML Infrastructure & Serving · **Tags:** `flink`, `autoscaling`, `time-series-forecasting`, `stream-processing`, `kafka`, `cost-optimization`

## TL;DR

Grab replaced reactive, threshold-based autoscaling for its Kafka-consuming Flink jobs with an ML-driven predictive autoscaler that forecasts incoming throughput and scales TaskManager CPU *ahead* of demand spikes instead of reacting after latency or CPU thresholds are already breached — cutting cloud CPU cost by roughly 35% on rolled-out pipelines.

## 1. Business context

Grab runs many Flink stream-processing jobs consuming from Kafka, and CPU provisioning for their TaskManagers (the worker processes that execute Flink tasks) was a persistent source of waste: teams tended to over-provision to avoid falling behind during traffic spikes, since Kafka-bound Flink jobs following seasonal demand patterns (rush hours, daily cycles) don't scale gracefully under naive reactive autoscaling. Reactive scaling — triggering more resources once CPU or latency crosses a threshold — has a structural problem for this workload: by the time the threshold is breached, the job may already be falling behind on its Kafka backlog, and a scaling event itself (restarting or resizing TaskManagers) can briefly disrupt processing, amplifying instability rather than resolving it. The business cost was twofold: wasted cloud spend from over-provisioning as an insurance policy, and residual instability risk even with that insurance in place.

## 2. Technical details

Grab's predictive autoscaler replaces threshold-based reactive scaling with a two-model pipeline:

1. **Time-series forecasting model** — forecasts near-future Kafka source-topic throughput, exploiting the seasonal patterns (daily/weekly cycles) that Grab's marketplace traffic follows.
2. **Regression-based resource predictor** — maps the forecasted throughput to the TaskManager CPU required to process it without falling behind.

The system uses these two models together to **vertically scale CPU ahead of the predicted demand spike**, rather than waiting for an observed CPU or latency breach to trigger a reactive scale-up. Because the scaling decision is based on a forecast rather than a lagging signal, TaskManagers are resized before load actually arrives, avoiding both the backlog buildup of under-provisioning and the restart-induced instability that reactive threshold-crossing scaling can cause.

## 3. Impact — potential & realized

**Realized:** the predictive autoscaler has been **rolled out to the majority of applicable pipelines** at Grab and reduced cloud CPU cost by **roughly 35%** on those pipelines, while improving stability by avoiding the reactive restart spikes and scaling spirals that threshold-based autoscaling was prone to.

**Potential:** the forecast-then-provision pattern generalizes to any stream-processing workload with seasonally predictable throughput (not just Flink-on-Kafka) — anywhere reactive autoscaling's lag between threshold breach and resource availability causes either backlog buildup or wasted over-provisioning, a lightweight time-series-plus-regression forecasting pipeline can substitute for hand-tuned reactive thresholds.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a clean, pragmatic application of forecasting to infra cost, not a new technique

Predictive/proactive autoscaling driven by time-series forecasting is a known pattern in the ML-infra space, and the two-model pipeline here (forecast throughput, regress to required CPU) is deliberately simple rather than novel. The value is in the concrete, quantified production payoff — a ~35% CPU cost reduction rolled out broadly — which is a strong result for what is architecturally a fairly modest system, and a good reminder that infra cost savings don't always require sophisticated modeling to pay off.

### Similar / related work

- [**Uber's Forecasting Models to Improve Driver Availability at Airports**](2026-09-14-uber-airport-driver-availability-forecasting.md) (in this bank) — a different domain (marketplace supply) but the same underlying pattern of using time-series forecasting to act ahead of predictable demand rather than reacting to it.
- [**Real-Time Spatial Temporal Forecasting @ Lyft**](2026-09-13-lyft-realtime-spatial-temporal-forecasting.md) (in this bank) — discusses similar classical-vs-deep-learning trade-offs for production forecasting systems that this autoscaler's simple time-series-plus-regression design implicitly makes.
- General reactive-vs-predictive (proactive) autoscaling literature for cloud infrastructure — the broader body of work this system positions itself against; left unlinked as a general area rather than one paper.

### Jargon buster

- **TaskManager** — the worker process in Apache Flink that actually executes stream-processing tasks; scaling a Flink job typically means adding, removing, or resizing TaskManagers.
- **Reactive (threshold-based) autoscaling** — scaling resources up or down only after a monitored metric (like CPU utilization or processing latency) crosses a predefined threshold, meaning the response always lags the triggering event.
- **Vertical scaling** — increasing the resources (CPU, memory) allocated to an existing worker instance, as opposed to horizontal scaling, which adds more worker instances.
- **Kafka-bound job** — a stream-processing job whose throughput is driven by (and limited by) how fast it can consume from its upstream Kafka topic, making Kafka's incoming message rate the key forecasting target for this kind of autoscaler.
