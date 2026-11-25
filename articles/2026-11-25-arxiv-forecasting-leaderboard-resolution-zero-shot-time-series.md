---
id: arxiv-forecasting-leaderboard-resolution-zero-shot-time-series
title: "What a Forecasting Leaderboard Can Establish: Resolution Reporting for Zero-Shot Time-Series Models"
source: "Academic (arXiv cs.LG)"
url: "https://arxiv.org/abs/2611.31619"
published: "2026-11"
added: "2026-11-25"
category: forecasting-timeseries
tags: [time-series-foundation-models, leaderboards, benchmark-evaluation, minimum-detectable-effect, cluster-robust-inference, wild-cluster-bootstrap, rank-stability, context-length, reproducibility]
novelty: 4
sourced_via: "full-text fetch"
---

# What a Forecasting Leaderboard Can Establish: Resolution Reporting for Zero-Shot Time-Series Models

**Source:** [Academic (arXiv cs.LG)](https://arxiv.org/abs/2611.31619) · Published 2026-11 · Added 2026-11-25
**Category:** Forecasting & Time Series · **Tags:** `time-series-foundation-models`, `leaderboards`, `benchmark-evaluation`, `minimum-detectable-effect`, `cluster-robust-inference`, `wild-cluster-bootstrap`, `rank-stability`, `context-length`, `reproducibility`

## TL;DR

Time-series foundation models are compared on a few public leaderboards, but none states how small a difference its datasets can detect. The paper calls that the board's *resolution* and releases Vernier, a tool that computes it from the per-dataset scores a board already publishes. GIFT-Eval resolves 6.8 rank places while its displayed neighbours sit 0.91 apart, so its top ten spans fewer than two resolvable steps. Below the resolution, the order depends on who else submitted and on unrecorded run settings such as history length.

## 1. Business context

A foundation model for time series is pretrained once and then asked to forecast series it has never seen. The evidence for it is its score on held-out datasets. Independent public forecasting datasets are scarce, so comparisons run through a few shared boards. Papers cite a position on GIFT-Eval, the board with the most entries, as evidence of state-of-the-art accuracy.

Every measurement has a resolution. GIFT-Eval scores 128 displayed entries on 97 configurations (one dataset at one frequency and horizon). But those 97 come from 28 datasets, and the configurations of one dataset rise and fall together. So the evidence is 28 independent draws, not 97.

Two forecasting boards already attach uncertainty: fev-bench reports paired bootstrap intervals over tasks, and TS-Arena reports intervals on ratings. An interval describes one comparison. The authors note that no forecasting board states its smallest detectable difference or tests whether its order depends on the pool of entries.

## 2. Technical details

Vernier reads one file: a score for every entry on every evaluation unit. It answers three questions.

- **How small a difference can the board detect?** Units from one source are not independent, so the *source* is the sampling unit. The standard error of a pairwise mean difference uses CR2, a cluster-robust estimator corrected for few clusters, with Satterthwaite degrees of freedom. A pair's resolution is the minimum detectable effect: the smallest true difference a 5% test detects with 80% power, (t₀.₉₇₅,ν + t₀.₈₀,ν)·SE. A board's resolution is the median over neighbouring pairs in its top ten. On GIFT-Eval ν runs 11.4–17.1, giving a multiplier of about 3.0.
- **Which entries can't be separated from the leader?** A CR2 t-test at 5%, uncorrected and Holm-corrected. Every test is repeated with a wild cluster bootstrap (one random sign per source) and its exact form, which enumerates all 2²⁸ sign patterns. Proposition 1 shows the exact test holds its level for any number of sources when the two entries are interchangeable within each source. Entries not separated from the leader form its *tier*.
- **Does the order depend on who else submitted?** A mean-rank rule scores an entry against the pool, so an unrelated submission can move it. The *bystander test* replays the board's version history. At each update it counts top-ten pairs that reversed although neither entry's result or metadata files changed.
- **Validity checks.** In 4,000 simulated boards with GIFT-Eval's layout, CR2 holds 4.4–5.8% false alarms except in the most extreme setting (6.8%). On resampled real mean-rank pairs it is 5.2%, against 6–10% for a percentile bootstrap. Under the geometric mean of scaled error, CR2 and both bootstraps over-reject (about 16%), because one dataset (most often solar) can supply over half the variance. A pre-specified search found one test that holds its level there: an exact Wilcoxon signed-rank test with datasets as units (5.6% pooled).
- **History-length experiment.** Inference only, four open models: Chronos-Bolt-base, Moirai-2.0-R-small, TimesFM-2.5-200M and Toto-Open-Base-1.0. They ran on 70 GIFT-Eval configurations (18 datasets, 14 sources), at the documented history length from GIFT-Eval's reference notebook and at 512 steps. A 12-configuration discovery set and a 58-configuration confirmation set were fixed in advance. The test is an exact sign-flip test on the 14 source totals, with Holm correction.
- **Boards covered.** GIFT-Eval, fev-bench, fev-bench-mini, Chronos Benchmark II, TIME and BOOM. Each analysis first reproduced the board's own numbers. Several other benchmarks could not be analysed because they publish no per-entry, per-unit file or an unreproducible rating.

## 3. Impact — potential & realized

**Measured (resolution):**
- *GIFT-Eval:* 6.8 rank places against a median neighbour gap of 0.91 (ratio 7.5). The top ten spans 11.0. One of nine neighbouring pairs separates before Holm correction (places 9–10, p = 0.036), and none after, under CR2, wild bootstrap or exact tests. Closing the median gap would take about 48 times as many datasets (median 1,342). The authors call this a lower estimate, since new sources look noisier.
- *Other boards:* on every board built from 15 to 39 public sources, resolution is 3.6 to 19 times the median gap. At most one of nine neighbouring pairs separates. BOOM is the exception: with each of its 2,554 series as a source its ratio is 0.63 and all nine neighbours separate. Grouped into 23 domains the ratio is 2.04 and five of nine separate. The authors' reading: "independent sources set the resolution, not units".
- By 2026-11-13 GIFT-Eval displayed 170 entries, with a resolution of 17.28 against a median gap of 0.48 (ratio 36).

**Measured (pool dependence):**
- Across four boards whose history could be replayed, pool-dependent rules reversed 43 untouched top-ten pairs in 31 of 226 updates. GIFT-Eval alone reversed 20 in 14 of 141 updates, plus 8 more in the ten weeks after the snapshot. The pool-independent geometric mean reverses none.
- In one week, three unrelated arrivals on GIFT-Eval fully reversed the order of Falcon-Agent, CastStar and limix_moe. On fev-bench, ChakraTS and TimesFM-3 swapped 2nd and 3rd when an unrelated entry arrived.
- Adding a near-copy of one displayed entry (every error ×1.000001) reorders GIFT-Eval's top ten in 42 of 128 cases.

**Measured (tiers):** all ten GIFT-Eval leaders are agentic pipelines, and nine declare no reproduction code. The leading tier has 3 entries under the displayed rule. Under the pool-independent rule it has 17 (CR2) or 16 (signed-rank), and TimesFM-3, a pretrained model released with weights, is in both. The authors conclude the evidence "does not settle the choice between an agentic pipeline and a pretrained model".

**Measured (history length):** at 512 steps, error rose by 15.3% for TimesFM-2.5 [+4.1, +32.6], 15.3% for Toto [+4.0, +27.1] and 6.2% for Moirai-2.0, all significant after Holm and again on the confirmation set. No effect is established for Chronos-Bolt (+2.7%). For TimesFM-2.5 and Toto the error rises on 64 of 70 configurations. On the discovery set, TimesFM-3 and Timestral-209M rose 31.8% and 28.9%. Thirteen of 48 discovery-set runs received less history than documented. Sampling is a second unrecorded setting: Toto with one point forecast misses the board's rows by 5.5%, while the notebook's median of 256 samples reproduces them to 0.02%.

**Potential:** a five-field disclosure checklist (history length received, aggregation rule, evaluation windows, normalisation, sampling). Plus a one-command report for any board that publishes per-dataset scores ([github.com/therealram18/vernier](https://github.com/therealram18/vernier)). The authors argue better comparisons "will come from more independent data, not from more submissions to the same datasets".

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Power analysis turned on the leaderboard itself, with hard numbers

The statistics are standard: few-cluster CR2, wild cluster bootstrap, Bloom's minimum detectable effect, Holm. What earns the 4 is the framing and the audit. "Resolution vs. displayed gap" is a single number any reader can check. The bystander test is a clean, falsifiable demonstration that mean-rank boards encode the submission pool. The history-length experiment is pre-registered, with discovery and confirmation splits. It shows a run setting moving error by more than the whole top-ten spread for two models, though the paper notes its test against that spread does not reject.

For product DS teams (my mapping, not the paper's): don't pick a forecasting foundation model by its leaderboard place. Treat entries within a tier as tied, rerun the candidates on your own series, and fix and log the context length and sample count. The same logic applies to any internal model-comparison dashboard that ranks against a pool. Caveats: this is a workshop paper by two authors with no stated affiliation, and the "48× datasets" figure assumes new datasets vary like the current ones.

### Similar / related work

- [**SOTA or Luck? The Winner's Curse in LLM Leaderboards**](2026-11-18-arxiv-sota-or-luck-winners-curse-llm-leaderboards.md) (in this bank) — same diagnosis for LLM boards, via a task-level m-out-of-N bootstrap that yields rank intervals and tiers.
- [**GIFT-Eval: A benchmark for general time series forecasting model evaluation**](https://arxiv.org/abs/2410.10393) — the main board audited here.
- [**fev-bench: A realistic benchmark for time series forecasting**](https://arxiv.org/abs/2509.26468) — already reports paired bootstrap intervals over tasks; Vernier finds 0 of 9 neighbouring pairs separate on it.
- [**Rank intervals for leaderboards: A hierarchical framework for model evaluation**](https://arxiv.org/abs/2606.08679) — Neuhof & Benjamini; cited among the rank-interval work for language-model and tabular leaderboards that has no forecasting counterpart.
- [**TimesFM-3: A Zero-Shot Foundation Model for Multivariate Forecasting**](2026-09-03-google-timesfm3-multivariate-forecasting.md) (in this bank) — Google's "ranks first on three leaderboards" claim. This paper places TimesFM-3 inside a 16–17-entry tier under the pool-independent rule.

### Jargon buster

- **Resolution / minimum detectable effect** — the smallest true difference a test would catch with 80% power at the 5% level. Displayed gaps smaller than it are not supported by the data.
- **CR2 cluster-robust SE** — a standard error that treats correlated units from the same source as one cluster, with a small-sample correction for few clusters.
- **Wild cluster bootstrap** — resampling by randomly flipping the sign of each cluster's differences; its exact form enumerates every sign pattern.
- **Pool-dependent rule** — a score, like mean rank or win rate, computed relative to the other entries, so a new submission can reorder entries nobody reran.
- **Geometric mean of scaled error** — each entry's error divided by a seasonal-naive baseline, averaged on the log scale. It uses only the entry's own scores, so it is pool-independent.
- **Holm correction** — a step-down adjustment of p-values for testing many pairs at once.
