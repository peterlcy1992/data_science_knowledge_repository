---
id: nubank-scaling-predictive-intelligence
title: "Scaling Predictive Intelligence to Accelerate Nubank's AI-First Vision"
source: "Building Nubank"
url: "https://building.nubank.com/unlocking-financial-insights-how-nubank-powers-personalized-experiences-with-foundation-models/"
published: "2026-08"
added: "2026-09-04"
category: research-foundational
tags: [foundation-model, transformer, tabular-data, transaction-modeling, fintech]
novelty: 3
sourced_via: "web search"
discovered_via: "Snacks Weekly on Data Science podcast"
---

# Scaling Predictive Intelligence to Accelerate Nubank's AI-First Vision

**Source:** [Building Nubank](https://building.nubank.com/unlocking-financial-insights-how-nubank-powers-personalized-experiences-with-foundation-models/) · Published 2026-08 · Added 2026-09-04
**Category:** Research & Foundational · **Tags:** `foundation-model`, `transformer`, `tabular-data`, `transaction-modeling`, `fintech`

## TL;DR

Nubank built nuFormer, a transformer-based "predictive foundation model" that learns directly from raw transaction sequences (rather than hand-engineered features) by representing each transaction as modular tokens — amount sign, amount bucket, timing, and BPE-tokenized description — and is now deployed across credit risk, lending, income prediction, and cross-sell, with the team reporting consistent offline lifts across all four use cases as they scaled from 24M to 330M parameters.

## 1. Business context

Nubank, following its 2024 acquisition of Hyperplane (a company specializing in large financial-behavior models), set out to build foundation models for financial behavior that could serve multiple predictive product surfaces from one underlying representation, rather than each team building bespoke, hand-engineered-feature models for credit risk, lending, income estimation, and cross-sell independently. The pitch of a "predictive foundation model" here mirrors the broader foundation-model playbook from language and vision: pretrain one large model on a huge volume of raw behavioral data, then reuse or lightly adapt it across many downstream tasks — aiming to let a single platform investment pay off horizontally across many product teams instead of each team repeating feature-engineering work from scratch.

## 2. Technical details

- **Model:** nuFormer, a transformer-based sequence model trained on raw transaction data.
- **Tokenization scheme:** each transaction is represented as a set of modular tokens rather than one hand-engineered feature vector — an amount-sign token (positive/negative), a quantized amount-bucket token, temporal tokens (month, day, weekday), and a natural-language description tokenized via byte-pair encoding (BPE), similar in spirit to how text-based approaches tokenize language.
- **Data integration:** beyond standard transaction attributes, training data included Money Box (Nubank's savings product) investment activity, loan data, and Brazilian Credit Information System (SCR) data, which brings in external financial-history signal beyond what's visible within Nubank's own transaction data alone.
- **Scaling behavior:** the team observed incremental gains scaling training data from 5 million to 40 million user rows, and distinct performance lifts moving the model from 24 million to 330 million parameters — with a stated roadmap toward 1.5 billion parameters.
- **Context-length tradeoff:** longer historical transaction windows improved performance, but because attention computation scales quadratically with sequence length, longer context comes with a real training-efficiency cost the team had to balance against the accuracy gain.

## 3. Impact — potential & realized

- **Realized:** the article reports "offline lifts" across credit risk, lending, income prediction, and cross-sell recommendation use cases from applying the shared foundation-model representation, and frames this as evidence the underlying investment can be delivered horizontally across many product teams — but does not disclose specific quantified lift numbers for any of the four use cases, which is a notable gap for readers trying to judge magnitude.
- **Potential:** if a single pretrained transaction-sequence model genuinely transfers well across credit, lending, income, and cross-sell tasks, it reduces the marginal cost of building the *next* predictive product at Nubank — new use cases could fine-tune from a shared representation instead of engineering features from scratch, which is the core economic argument for foundation models in any vertical.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — a credible domain application of the foundation-model playbook, thin on hard numbers

Applying the "pretrain on raw sequences, tokenize everything, scale parameters and data" foundation-model recipe to transaction data is a sensible and increasingly common pattern in fintech (several banks and payment companies have published similar transaction-transformer work), and the BPE-tokenized-description-plus-structured-token design for transactions is a reasonable domain adaptation rather than a novel architecture. It lands at a 3 rather than higher both because the pattern itself is now well-established across the industry, and because the write-up's impact section leans on "offline lifts across four use cases" without giving readers the actual lift magnitudes — making it hard to judge how large a win this really is versus the hand-engineered-feature baselines it replaces.

### Similar / related work

- [**How Discovery Bank Delivers Hyper-Personalized Banking at Scale: Behavioral AI, Governed Data, and Real-Time Decisioning**](2026-09-03-databricks-discovery-bank-hyperpersonalization.md) (in this bank) — another bank building a shared, cross-product behavioral-AI platform, useful as a direct industry comparison for the "one investment, many downstream products" thesis.
- [**How Coinbase Builds Sequence Features for Machine Learning**](https://www.coinbase.com/blog/how-coinbase-builds-sequence-features-for-machine-learning) — a related fintech infrastructure effort for building sequence-based features (rather than a full foundation model) for ML, a useful contrast in how much modeling investment different companies put behind sequential transaction/behavior data.

### Jargon buster

- **Foundation model** — a large model pretrained on broad data (here, raw transaction sequences) intended to be reused or lightly adapted across many downstream tasks, rather than trained from scratch for each one.
- **Tokenization** — breaking raw input into discrete units ("tokens") a model can consume; nuFormer tokenizes transactions into components like amount sign, amount bucket, and time, plus BPE tokens for free-text descriptions.
- **BPE (Byte-Pair Encoding)** — a common tokenization algorithm (used by most modern language models) that builds a vocabulary of frequently occurring sub-word units, applied here to transaction description text.
- **SCR (Sistema de Informações de Crédito)** — Brazil's Credit Information System, a central bank registry of credit-related data that gives lenders visibility into a borrower's obligations across institutions, not just within one bank.
