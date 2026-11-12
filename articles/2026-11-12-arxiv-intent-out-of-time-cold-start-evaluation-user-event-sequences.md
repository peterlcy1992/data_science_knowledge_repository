---
id: arxiv-intent-out-of-time-cold-start-evaluation-user-event-sequences
title: "INTENT: Out-of-Sample, Out-of-Time, and Cold-Start Evaluation on User Event Sequences"
source: "arXiv cs.LG (KTH AI Society, Unbox AI, MIT; ICAIF '26 banking FM workshop)"
url: "https://arxiv.org/abs/2611.13069"
published: "2026-11"
added: "2026-11-12"
category: personalization-recsys
tags: [evaluation, temporal-split, cold-start, benchmark, next-item-prediction, banking-foundation-models, leakage]
novelty: 3
sourced_via: "full-text fetch"
---

# INTENT: Out-of-Sample, Out-of-Time, and Cold-Start Evaluation on User Event Sequences

**Source:** [arXiv cs.LG (KTH AI Society, Unbox AI, MIT; ICAIF '26 banking FM workshop)](https://arxiv.org/abs/2611.13069) · Published 2026-11 · Added 2026-11-12
**Category:** personalization-recsys · **Tags:** `evaluation`, `temporal-split`, `cold-start`, `benchmark`, `next-item-prediction`, `banking-foundation-models`, `leakage`

## TL;DR

A public benchmark that scores next-item models in seven cells defined by whether the user, the period and the target item were seen in training. On five audited datasets the cell decides the winner: SASRec leads on seen items after the cutoff but scores zero on new items, where 'repeat the last item' leads on four of five — and that parameter-free baseline shows most of the post-cutoff score drop on three datasets is changed behaviour, not the model.

## 1. Business context

Banks and payment networks now train 'large behavioural models' on ordered customer events (transactions, app sessions, authorizations), often one backbone for fraud, credit and personalization. Deployed, such a model predicts forward in time, often for customers and merchants absent from training — yet each bank evaluates on private data with its own metrics, so models can't be compared.

Public sequential-recommendation data is the obvious proxy, but its standard protocol leaks: the paper cites that 77% of recent sequential-recommendation papers hold out each user's final interactions, so training contains events that occur after some test events. INTENT aims to provide a re-runnable test of exactly the conditions a deployed model meets.

## 2. Technical details

**Grid.** Three binary axes — user (10% of users held out of training), time (a per-dataset cutoff date), item (target seen in training or not) — give seven test cells (the known-user/past cell has only seen items). Models rank the full item vocabulary (no sampled negatives); the primary metric is NDCG@10 averaged over users, with users as the unit of evidence and a 1,000-user floor per cell (giving a ~95% CI half-width of 0.012–0.019 for per-user SD 0.2–0.3). The gap between seen- and new-item scores is the 'memorization gap'.

**Data audit.** 101 public releases grouped into 59 families; five criteria (stable entities, calendar timestamps, ≥25,000 users with 3+ events, action mapping, access). Ordering was the binding constraint: 19 families lack a calendar time that orders events, including the largest public bank dataset, whose anonymization adds date noise. Five datasets survive: Amazon Reviews 2023 Home & Kitchen, KuaiRand-27K, MicroLens-1M, H&M, REES46.

**Splitting.** No single date works across datasets, so a rule fixed before any model is evaluated targets 80% of rows in training (75–85% admissible), on month boundaries (day boundaries for short sources), taking the midpoint of admissible candidates; the same rule sets a validation cutoff. Horizons still differ (2 days on KuaiRand to 377 on Amazon), so every result reports cutoff, history length, seen shares and horizon. Summed over datasets every cell holds at least 111,769 users.

**Reference models.** Popularity (user histogram 0.7 + smoothed global), repeat-last, SASRec (2 blocks, 64 dims, context 50), and SASRec-F, which builds item vectors from metadata-token embeddings with ID-embedding dropout so it can score new items.

## 3. Impact — potential & realized

**Realized (reference results).** For known users choosing seen items after the cutoff, SASRec leads on every dataset (e.g., 3.4 vs 1.7 for popularity on H&M). On new items SASRec scores zero; repeat-last leads on every dataset except MicroLens, where only SASRec-F scores above zero. New users after the cutoff cost SASRec under 4% relative to known users (no significant difference), whereas crossing the cutoff costs it 25–68% on seen items. Repeat-last, which cannot overfit, itself loses 21–64% across the cutoff on Amazon, H&M and REES46, so the authors attribute most of the time cost to changed behaviour; a model's loss beyond repeat-last's is its own (SASRec keeps 73% on Amazon vs 36% for repeat-last, but 59% vs 71% on H&M). SASRec-F retains 112% of its seen-item score on MicroLens but 10% on H&M and 4% on REES46.

**Potential.** Pipeline, cutoff rule and per-cell user counts are public, and the authors suggest a bank can apply the same protocol to its own ledger.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A careful, honest evaluation protocol rather than a new model; most useful as a template for out-of-time and cold-start evaluation of any sequence model.

The real contribution is methodological hygiene a data scientist can steal tomorrow: pre-register the split rule, report per-cell user counts and intervals, use users as the unit of evidence, and always include a parameter-free control (repeat-last) to separate *drift in the world* from *model decay*. That last point is the most transferable — it's the evaluation analogue of a difference-in-differences control. Limits: only four small reference models, horizons differ by two orders of magnitude, and the banking motivation is served by e-commerce/video proxies, so it says little directly about transaction models.

### Similar / related work

- [**How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of Post-hoc Calibration**](2026-11-03-arxiv-ctr-recalibration-temporal-evaluation-fresh-data.md) — in this bank: the same insistence on time-respecting evaluation, for calibration
- [**The Hidden Look-Ahead: Point-in-Time Leakage in Electricity Market Data**](2026-10-29-arxiv-point-in-time-leakage-electricity-forecast-archives.md) — in this bank: look-ahead leakage in forecasting archives, the time-series cousin of leave-last-out leakage
- **On Sampled Metrics for Item Recommendation (Krichene & Rendle, KDD 2020)** — Krichene & Rendle's result that sampled negatives can reverse model order, which INTENT avoids by ranking the full catalogue
- [**Self-Attentive Sequential Recommendation (SASRec)**](https://arxiv.org/abs/1808.09781) — the transformer baseline used throughout

### Jargon buster

- **Leave-last-out split** — Holding out each user's final interactions for test — which lets training include events later in calendar time than some test events.
- **Global time split** — Every event before one cutoff date trains, every event after tests, so no model sees the future.
- **Memorization gap** — The difference between a model's score on items it saw in training and on new items.
- **NDCG@10** — A ranking metric that rewards placing the true next item near the top of the first ten results.
