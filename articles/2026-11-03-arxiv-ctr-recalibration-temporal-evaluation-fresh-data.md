---
id: arxiv-ctr-recalibration-temporal-evaluation-fresh-data
title: "How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of Post-hoc Calibration"
source: "arXiv cs.LG (Rui Liu, independent researcher)"
url: "https://arxiv.org/abs/2610.33168"
published: "2026-10"
added: "2026-11-03"
category: personalization-recsys
tags: [ctr-prediction, calibration, temporal-evaluation, platt-scaling, isotonic-regression, ads]
novelty: 3
sourced_via: "full-text fetch"
---

# How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of Post-hoc Calibration

**Source:** [arXiv cs.LG (Rui Liu, independent researcher)](https://arxiv.org/abs/2610.33168) · Published 2026-10 · Added 2026-11-03
**Category:** personalization-recsys · **Tags:** `ctr-prediction`, `calibration`, `temporal-evaluation`, `platt-scaling`, `isotonic-regression`, `ads`

## TL;DR

Offline CTR evaluation defaults to random splits, but deployed models score future traffic and bidding/pacing consume the probabilities. On Avazu (40.4M impressions) the paper shows random splits make logistic regression look better calibrated (ECE 55-62% of the temporal value), that recalibrating on a 6-hour slice of recent data increases ECE in about a third of applications, and that a 12-hour slice largely removes the harm. In a simulated auction, recalibration moved profit only about -0.21% to +0.26%.

## 1. Business context

A CTR model in an ad system outputs a number that other components treat as a probability: expected-value bidding multiplies it by a value per click, and pacing controllers compare predicted with realized click rates. A model that ranks well but over- or under-predicts misprices traffic despite a healthy AUC. Yet offline evaluation in the CTR literature is built mostly around random splits with AUC and log loss as headline metrics, and post-hoc recalibration (fit a Platt or isotonic correction on the freshest labeled data) is often run unconditionally on every refresh cycle. The paper asks whether that default is safe and how much fresh data it should use.

## 2. Technical details

Data: Avazu CTR, 40,428,967 impressions over ten consecutive days (21-30 October 2014), overall CTR 16.98%. Models: logistic regression (LR), DeepFM and DCN-v2, three seeds per arm, under two rolling temporal origins (one day apart) and a random-split arm. Metrics: AUC, log loss, and expected calibration error (ECE, 15 equal-width bins). For each temporal test day the authors fit Platt scaling and isotonic regression under a leak-free rule on the slice immediately preceding the period (6 hours in the main protocol; a sweep over 1, 3, 6, 12 and 24 hours), and report paired block-bootstrap intervals on the ECE change. They also test a size-matched control (subsampling the 12-hour slice to the 1-hour slice's impression count, about 5% of the volume), a pre-serving 'slice-ECE' gate fitted on origin 1 and applied frozen to origin 2, and a simulated auction to translate calibration changes into profit.

## 3. Impact — potential & realized

Realized (per the paper, one public dataset): random-split AUC exceeded temporal AUC by +0.0135 (LR) and +0.0139 (DeepFM) at origin 1's nearest test day, and the random arm reported LR's ECE at 55-62% of the temporal value in every seed (the deep models' ratio was seed-unstable). ECE was not monotone in temporal distance for any model, contradicting the expectation that it grows with drift. Recalibration with a 6-hour slice removed up to 61% of ECE in badly miscalibrated cells (e.g. DCN-v2 isotonic 0.0098 to 0.0038) but increased ECE in 14-17 of 48 applications across seeds. On fixed evaluation sets, a 12-hour slice cut harm from 13-17 to 3-5 of 36 applications, and 24 hours raised it again; the size-matched 12-hour subsample recovered 88% of the full slice's gain while being 20-25x faster to fit, so impression count alone does not explain it. The slice-ECE gate showed no benefit out-of-origin, and in the simulated auction profit moved only about -0.21% to +0.26%. The author recommends measuring calibration temporally over multiple origins and seeds, and says that the finding that a wide span beat the freshest few hours needs confirmation on other logs. Limits: a single dataset from 2014 and only ten days.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A modest, honest measurement study that echoes the data-science lesson that evaluation design changes the answer.

A modest, honest measurement study that echoes the data-science lesson that evaluation design changes the answer. The practical takeaways (evaluate calibration temporally, do not recalibrate unconditionally, prefer a wider fitting window) are plausible but rest on one old public log, so the author's own caveat that other logs must confirm is the right reading. Valuable mainly as a protocol checklist for ad/recsys teams, not as a new method.

### Similar / related work

- [**Tie Handling Is Part of the Evaluation Protocol: An Order-Invariance Audit for Tie-Heavy Recommender Scores**](2026-09-25-arxiv-tie-handling-recsys-evaluation.md) (in this bank) — another case where the evaluation protocol, not the model, drives the reported number
- Pan et al., cited by the paper — found Platt scaling and isotonic regression worsening calibration on a date-split Avazu; not in this bank
- Ovadia et al., cited by the paper — calibration degrades with dataset shift and post-hoc recalibration on in-distribution data does not preserve it

### Jargon buster

- **Calibration** — Agreement between predicted probabilities and empirical frequencies: of impressions scored 0.2, about 20% should click.
- **ECE (expected calibration error)** — Binned average gap between predicted probability and observed rate.
- **Platt scaling / isotonic regression** — Two post-hoc corrections: a logistic fit on model scores, and a monotone piecewise-constant map.
- **Temporal split** — Training on the past and testing on the future, mimicking deployment, as opposed to a random split.
