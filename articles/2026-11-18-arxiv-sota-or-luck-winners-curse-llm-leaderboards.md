---
id: arxiv-sota-or-luck-winners-curse-llm-leaderboards
title: "SOTA or Luck? The Winner's Curse in LLM Leaderboards"
source: "WashU Olin / ASU W. P. Carey (arXiv cs.LG / stat.ME)"
url: "https://arxiv.org/abs/2611.22227"
published: "2026-11"
added: "2026-11-18"
category: statistical-modeling
tags: [winners-curse, selection-bias, bootstrap, m-out-of-n-bootstrap, rank-uncertainty, llm-evaluation, leaderboards, swe-bench]
novelty: 4
sourced_via: "full-text fetch"
---

# SOTA or Luck? The Winner's Curse in LLM Leaderboards

**Source:** [WashU Olin / ASU W. P. Carey (arXiv cs.LG / stat.ME)](https://arxiv.org/abs/2611.22227) · Published 2026-11 · Added 2026-11-18
**Category:** Statistical Modeling · **Tags:** `winners-curse`, `selection-bias`, `bootstrap`, `m-out-of-n-bootstrap`, `rank-uncertainty`, `llm-evaluation`, `leaderboards`, `swe-bench`

## TL;DR

Leaderboard scores are sample averages over a finite task set, so sorting them rewards luck as well as ability: the top score is overstated (the winner's curse) and, more generally, scores near the top are inflated and those near the bottom deflated ("rank-induced bias"). An m-out-of-N bootstrap over tasks estimates and removes that bias at every rank position and also yields rank probabilities, rank intervals and tiers, packaged as RULER. On SWE-bench Verified the two tied leaders' 79.2% is estimated to be inflated by 0.9 points, and 13 of 173 models share the leading tier.

## 1. Business context

Organisations use benchmark rankings to choose and buy models, researchers to claim SOTA, and funders to assess progress — usually from point rankings, without accounting for the noise behind fractional-point differences. With many competing models and narrowing gaps at the top, these are exactly the conditions under which the winner's curse is worst. The authors note that in 2025 the top SWE-bench Verified score rose 13 times with a median increase of 0.8 points, and 7 of the 13 increases were smaller than their estimated inflation. Because the bias comes from sampling noise, it persists on private, uncontaminated benchmarks too.

## 2. Technical details

- **Score adjustment.** Resample m of the N tasks (m = ⌊N^0.9⌋ in the Tau2 examples; B = 5,000 resamples there), re-rank models, measure how much the model at each rank position exceeds its original score, and rescale that excess to the full-sample noise level. The adjustment belongs to a *rank position*, not a particular model.
- **Rank Probability Matrix (RPM).** From the same resamples, how often each model occupies each rank. **Rank intervals** contain at least 1−α of a model's bootstrap rank mass (α = 0.20 by default). **Tiers** group consecutive models whose rank intervals share a common intersection.
- **Assumptions.** Fixed model pool; i.i.d. bounded tasks (binary pass/fail as the main case); arbitrary within-task correlation among models. Theory assumes exact population tiers separated by positive gaps — described as a deliberate idealisation of closely performing models.
- **Theory.** An all-position bias expansion shows rank-induced bias is Θ(N^−1/2); the bootstrap adjustment reduces it to expected residual o(N^−1/2). The RPM converges to a block-diagonal matrix of within-tier Gaussian rank probabilities, and the tiering rule recovers the population tiers with probability tending to one. Rank-mass intervals summarise the distribution rather than provide simultaneous confidence coverage.

## 3. Impact — potential & realized

**Measured:** across 14 benchmarks from 5 families (SWE-bench, Tau2-Bench, LiveBench, AlpacaEval 2, WildBench), rank-1 adjustments range from about 0.09 to 3.86 points, exceed 1 point in 7 benchmarks, and the leading tier contains multiple models in 12 of 14. On SWE-bench Verified (173 models, 500 tasks) the tied leaders get adjusted scores of 78.3%, only 30.5% and 29.0% probability of remaining leader (the rank-3 model 26.4%), and 80% rank intervals spanning ranks 1–6. In Tau2, Airline and Retail each place 5 of 7 models in the leading tier. Validation: in a split-sample study (half the tasks rank, the other half rescore; 200 splits per benchmark), adjustment reduces rank-1 score error from 2.38 to 0.73 points; a simulation calibrated to SWE-bench Verified reduces mean winner bias from 1.41 to 0.21 points. Sensitivity analyses on non-i.i.d. resampling schemes are reported as broadly robust for SWE-bench, with Telecom sensitive to issue-subcategory clustering.

**Potential:** the authors advocate publishing RULER alongside raw rankings and using it in benchmark design (how many tasks are needed to resolve an ordering).

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Old statistics, overdue application

The winner's curse and m-out-of-n bootstrap are well known; extending the correction to every leaderboard position while allowing cross-model correlation within a task, and pairing it with rank probabilities and tiers, is a useful and practical package. The SWE-bench numbers make the point concrete: typical "new SOTA" margins are within the noise. The same logic applies directly to internal model bake-offs and to picking the "winning" variant from many A/B arms — any DS selecting the max of noisy estimates should shrink or bootstrap before quoting it.

### Similar / related work

- [**Inference After Coding Agents**](2026-11-18-arxiv-inference-after-coding-agents-selective-replay.md) (in this bank) — selection after looking at the data, corrected via replay on subsamples.
- [**Shrink Responsibly: Empirical Bayes in Economics**](2026-11-18-arxiv-shrink-responsibly-empirical-bayes-economics.md) (in this bank) — empirical Bayes shrinkage, the alternative selection correction the paper contrasts with.
- [**Trustworthy Method Comparison with AI Judges: Estimation and Design under Order, Batch, and Aggregation Effects**](2026-10-07-arxiv-trustworthy-method-comparison-ai-judges.md) (in this bank) — statistical design for comparing LLM systems.

### Jargon buster

- **Winner's curse** — the selected best of several noisy estimates is, on average, an overestimate of its true value.
- **m-out-of-N bootstrap** — resampling fewer items (m < N) than the original sample, which fixes cases where the ordinary bootstrap fails, such as statistics involving a max or a ranking.
- **Rank Probability Matrix** — a table of how often each model lands at each rank across resamples.
- **Tier** — a group of models whose plausible ranks overlap, i.e. whose order the benchmark can't resolve.
