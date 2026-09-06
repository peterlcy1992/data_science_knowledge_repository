---
id: zillow-serving-ml-models-at-scale
title: "Serving Machine Learning Models Efficiently at Scale at Zillow"
source: "Zillow Tech Hub"
url: "https://www.zillow.com/tech/serving-machine-learning-models-efficiently-at-scale-at-zillow/"
published: "2022-11"
added: "2026-09-06"
category: ml-infra-serving
tags: [model-serving, knative, kserve, kubernetes, request-batching, inference-infrastructure]
novelty: 2
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Serving Machine Learning Models Efficiently at Scale at Zillow

**Source:** [Zillow Tech Hub](https://www.zillow.com/tech/serving-machine-learning-models-efficiently-at-scale-at-zillow/) · Published 2022-11 · Added 2026-09-06
**Category:** ML Infrastructure & Serving · **Tags:** `model-serving`, `knative`, `kserve`, `kubernetes`, `request-batching`, `inference-infrastructure`

## TL;DR

Zillow built a centralized ML model-serving platform on top of Knative and KServe, giving ML practitioners a simple, standardized way to deploy models as production-grade online services while the platform team owns the performant, shared infrastructure underneath — reporting 20–40% improvements in p50 and long-tail serving latency compared to the vendor solutions it replaced.

## 1. Business context

As Zillow's AI teams grew, each team tended to build its own bespoke path to production for serving ML models, duplicating infrastructure work and producing inconsistent performance and operational practices across teams. Zillow needed a single, centralized serving platform that both gave ML practitioners a friendly, self-service interface for deploying models and gave the platform team one place to invest in serving performance, rather than every team separately reinventing (and separately debugging) their own model-serving stack.

## 2. Technical details

The platform is built on Knative, a Kubernetes-based platform for serverless workloads, which Zillow found solved most — but not all — of the pain points around ML-serving efficiency (autoscaling, revision management, request routing). To close the remaining gaps specific to ML workloads, Zillow layered KServe on top: a purpose-built model-serving framework that provides a custom model server with strong abstractions over Knative, plus ML-specific serving features such as request batching (grouping multiple inference requests into a single batched forward pass for better hardware utilization) and separated "transformer" components for pre- and post-processing logic distinct from the core model-inference step.

Architecturally, the platform is organized around a flow/DAG (directed acyclic graph) paradigm that mirrors the natural step-by-step structure of an ML pipeline — feature transformation, inference, post-processing — echoing the design philosophy of pipeline-orchestration frameworks like Kubeflow, MLflow, and Airflow, but applied specifically to the serving path rather than training or batch orchestration.

## 3. Impact — potential & realized

**Realized:** Zillow reports 20–40% improvements in p50 (median) and long-tail (high-percentile) serving latencies compared to the vendor-based solutions the platform replaced, attributed to the combination of Knative's serverless autoscaling with KServe's ML-specific optimizations like request batching.

**Potential:** The core lesson — that a general serverless platform (Knative) solves most but not all ML-serving needs, and the remaining gap is exactly what a specialized layer like KServe fills — is a useful decision framework for any infrastructure team evaluating whether to build ML serving on general-purpose serverless primitives or invest in ML-specific serving tooling on top of them.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 2/5 — A solid infrastructure write-up using established open-source tooling

Knative and KServe are both established open-source projects, not new inventions from Zillow; the value here is the concrete adoption story and the reported latency numbers from combining them, which is useful evidence for teams evaluating the same stack rather than a novel infrastructure contribution.

### Similar / related work

- [**How Databricks Feature Store Serves Features with Sub-Second Freshness**](2026-08-30-databricks-feature-store-subsecond-freshness.md) (in this bank) — a complementary piece of the serving stack (the feature side rather than the model-serving side) tackling a similar low-latency production-infrastructure problem.
- [**In-House LLM Serving at Netflix (vLLM + Triton)**](2026-08-30-netflix-in-house-llm-serving.md) (in this bank) — a more recent, LLM-specific take on the same underlying problem (standardized, efficient model serving), useful for contrasting classical-ML serving infra against LLM-serving infra.
- **Streamlining Machine Learning Model Serving with KServe** — [Medium](https://medium.com/@dingfanz/streamlining-machine-learning-model-serving-with-kserve-05cfd4daf3cb) — a broader technical walkthrough of the KServe framework itself, useful background for the architecture described in this article.

### Jargon buster

- **Knative** — an open-source Kubernetes-based platform for building and running serverless applications, providing autoscaling (including scale-to-zero) and request routing without requiring teams to manage that infrastructure themselves.
- **KServe** — an open-source model-serving framework built on Kubernetes/Knative that adds ML-specific capabilities (standardized inference protocols, request batching, pre/post-processing "transformers") on top of general serverless infrastructure.
- **p50 / long-tail latency** — p50 is the median response time (half of requests are faster, half slower); "long-tail" latency refers to high percentiles (e.g., p95, p99) capturing the slowest requests, which matter disproportionately for user-facing system reliability.
