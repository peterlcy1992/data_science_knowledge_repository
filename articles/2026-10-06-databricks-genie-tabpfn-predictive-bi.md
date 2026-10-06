---
id: databricks-genie-tabpfn-predictive-bi
title: "From "What Happened?" to "What Will Happen?": Genie + TabPFN for conversational predictive BI"
source: "Databricks (Yoshimatsu, Poveda Panter, Safaric, Singer et al.)"
url: "https://www.databricks.com/blog/what-happened-what-will-happen"
published: "2026-05"
added: "2026-10-06"
category: ml-infra-serving
tags: [tabpfn, genie, agent-bricks, predictive-analytics, mlflow-evaluation]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# From "What Happened?" to "What Will Happen?": Genie + TabPFN for conversational predictive BI

**Source:** [Databricks (Yoshimatsu, Poveda Panter, Safaric, Singer et al.)](https://www.databricks.com/blog/what-happened-what-will-happen) · Published 2026-05 · Added 2026-10-06
**Category:** ml-infra-serving · **Tags:** `tabpfn`, `genie`, `agent-bricks`, `predictive-analytics`, `mlflow-evaluation`

## TL;DR

A multi-agent app where Genie turns a business question into SQL that extracts a labeled dataset and TabPFN, a tabular foundation model, predicts in a single forward pass with no training, exposing predictive analytics through chat.

## 1. Business context

Predictive analytics typically needs a data scientist to find tables, build training data, choose models and interpret results, a bottleneck for business users who can already ask descriptive questions in natural language.

## 2. Technical details

A supervisor agent, deployed as a Databricks App on Agent Bricks, interprets intent, asks Genie (acting as a dynamic feature-engineering layer) to extract labeled data from the Lakehouse, passes it to TabPFN for inference, and returns recommendations. Unity Catalog lineage governs the pipeline. An evaluation harness built on MLflow GenAI evaluation runs against live agents and logs to MLflow tracking, to see which question classes yield reliable predictions.

## 3. Impact — potential & realized

The post gives no performance metrics. It lists limits: predictions depend entirely on Genie building meaningful labeled datasets, trust requires an evaluation framework, agents may hallucinate or omit information across turns, and questions must be outcome-prediction problems within the schema. A solution accelerator is on GitHub.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Pairing a no-training tabular foundation model with a text-to-SQL agent is a neat way to make prediction cheap, but the post offers no accuracy evidence, and the real risk (confident predictions from poorly constructed training sets, with no causal framing) is DS territory.

Pairing a no-training tabular foundation model with a text-to-SQL agent is a neat way to make prediction cheap, but the post offers no accuracy evidence, and the real risk (confident predictions from poorly constructed training sets, with no causal framing) is DS territory. Worth watching as a pattern.

### Similar / related work

- [**Databricks Adaptive Instructed Retriever**](2026-09-29-databricks-adaptive-instructed-retriever.md) (in this bank) — another Databricks agent-pipeline post
- **TabPFN** — tabular foundation model used here (no specific URL linked)

### Jargon buster

- **TabPFN** — A pretrained transformer for tabular data that predicts in one forward pass without per-dataset training.
- **Genie** — Databricks natural-language-to-SQL interface over Lakehouse data.
- **Unity Catalog lineage** — Databricks governance layer tracking where data and models come from.
