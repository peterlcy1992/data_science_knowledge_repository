---
id: meituan-hierarchical-gtv-estimation-hge
title: "Hierarchical GTV Estimation: Bridging the Gap between Container-Level Ranking and Item-Level Conversion"
source: "Meituan (RecSys '26)"
url: "https://arxiv.org/abs/2610.32420"
published: "2026-10"
added: "2026-10-26"
category: search-ranking
tags: [gtv-estimation, sponsored-search, label-variance, proxy-labels, ads-ranking]
novelty: 3
sourced_via: "full-text fetch"
---

# Hierarchical GTV Estimation: Bridging the Gap between Container-Level Ranking and Item-Level Conversion

**Source:** [Meituan (RecSys '26)](https://arxiv.org/abs/2610.32420) · Published 2026-10 · Added 2026-10-26
**Category:** search-ranking · **Tags:** `gtv-estimation`, `sponsored-search`, `label-variance`, `proxy-labels`, `ads-ranking`

## TL;DR

Meituan ranks 'containers' (livestream rooms or stores) but transactions happen on items inside them, which makes Gross Transaction Value (GTV) labels noisy and sparse. HGE decomposes post-click GTV into purchase probability, quantity and unit price, encodes the item set, and blends item-level and container-level predictions; it reports +1.42% Revenue Per Search in a 13-day online A/B test.

## 1. Business context

In Meituan's O2O and live-streaming sponsored search, the platform ranks and bids at the container level while actual transactions occur at the item level inside each container. A single observed transaction (say a cheap service in a premium store) is a very noisy label for the container's expected value, and a ranking that over-weights click probability can lead merchants to pay for traffic whose realized GTV lags the cost. The paper names three challenges: high label variance, label sparsity (item-level conversions are rarer than container-level ones, which are rarer than clicks) and dynamic item heterogeneity.

## 2. Technical details

HGE has three parts. A Hybrid Set-Aware Encoder (HSAE; one Transformer encoder layer, hidden dimension 256, top-K = 10 items) models the dynamic item composition and container-item feature interaction. Proxy-Label Learning (PLL) decomposes post-click GTV into purchase probability, purchase quantity and expected unit price to reduce the effect of outlier transactions. Residual Correction and Ensemble Fusion (RCEF) aggregates item-level predictions where item interactions are observed and falls back on a universal container-level regression tower (DIN + DCN) elsewhere, with a per-sample learned gate for the ensemble weight.

Training uses Huber loss for the regression towers and BCE for the binary tasks, Adam (lr 9×10⁻⁴, batch 6,000), one epoch, negative sampling at 0.3. Data: 712M records, 121M users, 949K POIs from Meituan's ad logs, with a chronological out-of-time split (last 5%, 29M records, for test). Baselines: WLR, DLRM (DIN + DCN), RankMixer and CREAD.

## 3. Impact — potential & realized

Realized (as reported): offline, HGE reaches XAUC 0.8158 against 0.8105 for RankMixer and 0.8095 for CREAD (the abstract reports a +0.63% XAUC lift), PCOC (calibration ratio) 0.9858 against 0.7528–0.7921 for the baselines, and MAE 4.9915. Ablations: removing PLL drops XAUC to 0.7873 (PCOC 0.4180), removing HSAE to 0.8031, removing RCEF to 0.8146. Online, a 13-day A/B test (after an A/A validation phase) showed +1.42% Revenue Per Search with a 95% confidence interval of [+0.80%, +2.05%]; HGE is deployed on Meituan's main traffic.

Potential: the same decomposition-plus-aggregation pattern for any marketplace where the unit being ranked is a bundle or container of items.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A solid, practical applied-ML paper whose measurement angle (decomposing a noisy value label; calibration via PCOC; A/A then A/B with a CI) is the useful part.

What makes this interesting to a data scientist rather than just an ads engineer is the treatment of the label: when the target is a heavy-tailed realized value, factorising it into probability × quantity × price is a variance-reduction move, and the huge PCOC change in the PLL ablation (0.4180) shows how much calibration depends on it. The usual caveats apply: an industrial dataset not available externally and gains reported against four chosen baselines.

### Similar / related work

- [**The Science of Unified Ranking: Integrating Ads and Organic Recommendations**](2026-09-14-flipkart-unified-ranking-ads-organic.md) (in this bank) — Flipkart unified ranking — ads value estimation inside a ranker
- [**From Scoring to Spelling: Rebuilding Ads Retrieval at Instacart**](2026-09-01-instacart-ads-retrieval-rebuild.md) (in this bank) — Instacart ads retrieval rebuild — another commerce-ads ranking system

### Jargon buster

- **GTV** — Gross Transaction Value: the total value of purchases attributable to an impression or click.
- **XAUC** — A pairwise ranking metric: the share of sample pairs whose predicted order matches the order of their true values.
- **PCOC** — Predicted-over-actual ratio; 1.0 means predictions are calibrated in aggregate.
- **RPS** — Revenue Per Search, the online metric used in the A/B test.
