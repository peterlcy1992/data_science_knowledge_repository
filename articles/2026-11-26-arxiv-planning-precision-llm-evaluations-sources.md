---
id: arxiv-planning-precision-llm-evaluations-sources
title: "How Many Sources, Not Just How Many Problems: Planning the Precision of LLM Evaluations from Earlier Results"
source: "Florida State University (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.33622"
published: "2026-11"
added: "2026-11-26"
category: llm-genai
tags: [llm-evaluation, design-effect, intraclass-correlation, cluster-sampling, finite-population-correction, benchmark-design, confidence-intervals, swe-bench]
novelty: 3
sourced_via: "full-text fetch"
---

# How Many Sources, Not Just How Many Problems: Planning the Precision of LLM Evaluations from Earlier Results

**Source:** [Florida State University (arXiv stat.ME)](https://arxiv.org/abs/2611.33622) · Published 2026-11 · Added 2026-11-26
**Category:** LLMs & Generative AI · **Tags:** `llm-evaluation`, `design-effect`, `intraclass-correlation`, `cluster-sampling`, `finite-population-correction`, `benchmark-design`, `confidence-intervals`, `swe-bench`

## TL;DR

When benchmark problems share sources (templates, repositories), a fixed eval budget must choose how many sources as well as how many problems. Guang Qiu tests whether the classical design effect, with an intraclass correlation ρ estimated on disjoint pilot or earlier-submission data, predicts the SD inflation of concentrated subsets *before* running them. For pass@1 it does, to within a few percent (median over splits), but only if the finite-population terms of the actual sampling plan are included. Dropping them gives 13–35% errors. Widening iid intervals by the pilot √deff restores near-nominal pass@1 coverage, but not pass@16. The author makes no methodological novelty claim; the contribution is a held-out test plus a recipe.

## 1. Business context

LLM benchmarks increasingly group problems. GSM-Symbolic instantiates each grade-school template many times. SWE-bench draws all tasks from 12 Python repositories. Teams that evaluate many checkpoints or agent variants, such as automated research pipelines, often score each candidate on a small subset. How that subset is drawn decides which differences between systems can be trusted.

The fact that clustering matters is known. Miller (2024) recommends clustered standard errors and gives a cluster-adjusted power formula. Survey sampling has the design effect 1 + (m−1)ρ (Kish, 1965). What was missing, the paper says, is evidence of how accurate these *advance* predictions are on real LLM results, and which details of the sampling plan they need. Miller's planning example is analytic and not checked against observed spread.

There is also a gap in post-hoc fixes. Cluster-robust SEs and the cluster bootstrap are biased downward with few clusters. With one source per stratum, no within-sample method can estimate between-source variance at all. The paper's approach borrows that variance from outside the evaluated set.

## 2. Technical details

- **Score and tiers.** Each problem gets n attempts; the score is the mean of the unbiased per-problem pass@k estimator (Chen et al., 2021). Tiers hold the problem budget fixed and vary only the number of sources: R sources × V problems per source.
- **Naive prediction (eq. 1).** SD(R×V)/SD(baseline) ≈ √deff = √(1 + (V−1)ρ).
- **Design prediction (eq. 2).** A stratified two-stage variance with finite-population corrections (FPC) on both stages: between-source variance σ²_b scaled by (1 − t/T), attempt noise σ²_a, and within-source variance σ²_w scaled by (1 − V/N_j). The predicted ratio is the square root of tier variance over baseline variance. Computed for pass@1 only.
- **Held-out protocol.** The pilot estimates ρ and the variance components; held-out data are used only to measure SD over repeated draws.
  - **GSM-Symbolic:** 250 templates (main, P1, P2) from 100 GSM8K questions, first 20 variants each. 64 attempts per problem with Qwen2.5-Math-1.5B-Instruct on vLLM (temperature 0.6, top-p 0.95), graded by math-verify; each evaluation subsamples n = 16. Budget 100 problems, 40/30/30 by level. Pilot 15 original questions, held-out 85; 1,000 draws, 20 splits.
  - **SWE-bench Verified:** per-task resolved lists of public submissions, retrieved November 2026. 129 submissions kept (resolve rate 0.1–0.9). 500 tasks, 12 repositories, one attempt, so pass@1 only. Budget 40 tasks. Pilot 10 random submissions, held-out 119; split is submission-disjoint on the same 500 tasks. 300 draws, 100 splits.
  - **MATH-500:** no source labels; the 35 subject × level cells act as groups. A negative control.
- **GSM-Symbolic result.** Pass@1 SD grows from 2.65 pp (100×1) to 3.88, 6.62 and **9.24 pp (10×10)**. Templates explain about three quarters of per-variant variance (0.74–0.84 by level). Pilot ρ = 0.74.
  - Naive rule underpredicts by 13–21%. Cause: the 100×1 baseline draws 40 of 85 main and 30 of 40 P2 templates without replacement, which shrinks the baseline SD.
  - Design prediction: 1.50 / 2.45 / 3.49 vs measured 1.51 / 2.45 / 3.52.
  - Single splits err by −13% to +16% (median absolute error 5%).
- **SWE-bench result.** Repositories are much less homogeneous: median between-repo variance share 0.034. SD still rises from 7.1 pp (random 40) to 9.0 pp (2×20).
  - Design prediction within 3% of the median measured ratio at 8×5, 4×10 and 2×20.
  - At 1×40 only django, sympy and sphinx are eligible. Naive predicts 1.57, design 1.24, measured 1.16.
  - The ratio below one at 8×5 (0.96) is a finite-population effect: drawing 8 of 10 eligible repos is close to stratifying by repository.
  - ρ varies across submissions (5–95%: 0.007–0.073). Each submission's own ρ correlates 0.82 with its measured ratio at 2×20. So the prediction is a planning number for a *typical* submission.
  - After removing task difficulty (terciles), median ρ falls to 0.012, so much of the repository effect runs through difficulty.
- **FPC ablation (Table 6).** Without FPC, the GSM design prediction collapses exactly to the naive rule. On SWE-bench, dropping FPC overpredicts by 25–35%, because tiers draw 8 of 10, 4 of 9 and 2 of 7 eligible repositories.
- **Two validation pitfalls.**
  - *Split by source, not by difficulty version.* A level-wise split leaked 28–37 of ~35 pilot questions into the held-out pool. Pass@1 was unchanged, but the pass@16 correction looked better than a clean split supports.
  - *A good fit is not a diagnosis.* On MATH-500, treating cells as sources predicts 3.14 vs 2.87 measured and fixes coverage (0.58 → 0.95). But fixing the cell mix (design B) removes the problem entirely (iid coverage 0.99). The formula is an accounting identity and fits whenever some grouping explains variance.
- **Recipe (Section 7).** Label sources at the level that still varies under your design; stratify composition variables first. Get per-problem outcomes from earlier results or a pilot of ≥15 sources, split by source. Predict each allocation with eq. 2 including FPC. After evaluation, report the iid interval widened by √(1 + (V−1)ρ̂) for pass@1; flag pass@k, k > 1, as uncalibrated.
- Code: github.com/Guang627/deff-eval.

## 3. Impact — potential & realized

**Measured.**
- **Coverage of 95% intervals.** On GSM-Symbolic the iid interval width stays near 13.5 pp while true spread triples; pass@1 coverage falls from 0.99 to 0.54 on held-out draws. Widening by the pilot √deff gives 0.93–0.98 on GSM pass@1 and 0.94–0.95 on SWE-bench, including 1×40.
- **Cluster bootstrap on the evaluated set falls short.** Template bootstrap: 0.97, 0.93, 0.85 at 50×2, 20×5, 10×10. Repository bootstrap: 0.91, 0.82, 0.53 and 0.00 from 8×5 to 1×40.
- **pass@16.** Pilot ρ is small and noisy (0.00–0.61). The naive rule underpredicts by 6–22%, and widened coverage is only 0.85 (20×5) and 0.76 (10×10). A 24-question pilot raises this to 0.88 and 0.82.
- **Pilot size.** On GSM, median error stays within ±6% from 6 pilot questions up, but the 5–95% range narrows from [−38%, +20%] (6 questions) to about −12% to +16% (15–24). On SWE-bench, 3 earlier submissions already give a median error of −1%; 20 give the narrowest range [−5%, +10%].
- **Worked example.** For a 4 pp SD target on 100 GSM-Symbolic problems, eq. 2 predicts 2.6 / 3.9 / 6.4 / 9.1 pp; 50×2 is the most concentrated design that qualifies, confirmed by held-out SDs. With ρ = 0.74, going from 5 to 10 problems per template lowers SD by only about 2%.
- **Cost of concentration on SWE-bench.** 2×20 has 1.25× the SD of 40 random tasks, worth about 26 random tasks. Drawing repositories uniformly also biases the plain mean by −3 to −4 pp; post-stratifying on difficulty removes most of it and lowers SD to about 5.5 pp.

**Limitations the author states.** ρ is a property of a model–benchmark pair; neither benchmark shows transfer of ρ across models. SWE-bench submissions are not independent systems. The design prediction covers pass@1 only. Robustness analyses reuse the same answers. The GSM pilot (2,560 calls) costs more than one evaluation (1,600 calls), so it only pays when reused across many evaluations or when earlier results already exist.

**Potential.** For pipelines that evaluate many candidates on small subsets, every earlier run is a free pilot. The paper's GSM numbers imply that 10-point gaps between candidates scored on 10 templates can be noise.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Textbook survey sampling, but the first careful held-out check of it on LLM evals

The author is explicit that nothing methodological is new. The value is the validation discipline: disjoint pilots, repeated splits, an FPC ablation and a negative control. The FPC finding is the one I would remember. Benchmarks have tens of sources, not thousands, so the "detail" that every survey course skips is a 13–35% error here. The MATH-500 control is also a useful warning for anyone tempted to read a good deff fit as proof of clustering.

For DS teams this is the familiar cluster-randomized-trial planning problem, moved to model evaluation. Anyone running eval sweeps on subsampled benchmarks, or reporting leaderboard deltas from a few hundred grouped items, should copy the recipe. The main open gap is pass@k for k > 1, which the paper flags honestly rather than papering over. I would also like to see ρ transfer across model families tested directly, since that is the realistic use case for a new model.

### Similar / related work

- [**Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads**](2026-10-06-arxiv-agentic-rag-evaluation-budget-allocation.md) (in this bank) — uses generalizability theory to split an eval budget across questions, trajectories and reads; a variance-components sibling of this source-vs-problem allocation question.
- [**Unlocking 66% Faster Experiments with Covariate Adjustment: Power Analysis for Clustered Data, Ratio Metrics, and OLS Regression**](2026-10-12-instacart-covariate-adjustment-power-analysis-clustered-data.md) (in this bank) — power analysis with clustered data in production A/B testing; the same design-effect logic in an experimentation setting.
- [**Adding error bars to evals: A statistical approach to language model evaluations**](https://arxiv.org/abs/2411.00640) — Miller (2024); recommends clustered SEs and a cluster-adjusted power formula, whose advance predictions this paper checks empirically.
- [**Quantifying variance in evaluation benchmarks**](https://arxiv.org/abs/2406.10229) — Madaan et al. (2024); measures seed and benchmark variance across models.

### Jargon buster

- **Design effect (deff)** — how much a sampling plan inflates variance relative to simple random sampling of the same size; for clusters of m, 1 + (m−1)ρ.
- **Intraclass correlation (ρ)** — the share of outcome variance that lies between sources; high ρ means problems from one source behave alike.
- **Finite-population correction (FPC)** — the (1 − n/N) factor that shrinks variance when you sample a large share of a small pool without replacement.
- **Two-stage sampling** — first draw sources, then draw problems within each chosen source.
- **pass@k** — probability that at least one of k sampled attempts solves the problem, estimated without bias from n ≥ k attempts.
- **Cluster bootstrap** — resample whole sources from the evaluated set to estimate uncertainty; breaks down when there are only a few sources.
- **Negative control** — a case where the effect should be absent, used to check that a method is not just fitting anything.
