---
id: arxiv-probability-feasible-historical-transport-distributional-did
title: "Probability-Feasible Historical Transport: Sharp Bounds and Falsification Tests for Distributional Pre-Trend Designs"
source: "University at Albany, SUNY (arXiv econ.EM)"
url: "https://arxiv.org/abs/2611.29632"
published: "2026-11"
added: "2026-11-27"
category: experimentation-causal
tags: [difference-in-differences, distributional-effects, partial-identification, pre-trends, sharp-bounds, breakdown-analysis, stacked-events, moment-inequalities, linear-programming, LaLonde-NSW, eitc, minimum-wage]
novelty: 3
sourced_via: "full-text fetch"
---

# Probability-Feasible Historical Transport: Sharp Bounds and Falsification Tests for Distributional Pre-Trend Designs

**Source:** [University at Albany, SUNY (arXiv econ.EM)](https://arxiv.org/abs/2611.29632) · Published 2026-11 · Added 2026-11-27
**Category:** Experimentation & Causal Inference · **Tags:** `difference-in-differences`, `distributional-effects`, `partial-identification`, `pre-trends`, `sharp-bounds`, `breakdown-analysis`, `stacked-events`, `moment-inequalities`, `linear-programming`, `LaLonde-NSW`, `eitc`, `minimum-wage`

## TL;DR

Instead of parallel trends, one recent DiD approach assumes the post-policy treated–control gap is a *mixture* of past gaps. That gives bounds, not a point estimate. Hounyo extends this "historical transport" idea from means to whole outcome distributions. The key point: a mixture of past distribution gaps can put negative probability on some outcomes, and pooling several policy events can hide this. The paper gives sharp linear-programming bounds, breakdown radii and falsification tests. In the NSW experiment the tests reject transport; for the 1993 EITC expansion they pass through 1995, with a 4.7 to 7.0 point employment gain for single mothers relative to childless women.

## 1. Business context

**The setup, for someone who knows ordinary DiD.** Classic DiD assumes the treated–control gap in the *mean* outcome would have stayed constant without the policy. Distributional DiD asks the same question about the whole distribution. Examples: the share of workers paid below $9.25, the share with any earnings, a quantile. The object to recover is the untreated outcome distribution of the treated group after the policy. Everything else is observed.

Call the gap between the two groups' untreated distributions at date t the "selection bias" ν_t. It is a difference of two distributions, so it is a *signed* measure with total mass zero. Distributional parallel trends says ν after the policy equals ν on one base date. Ban et al. (2026), working with average effects, proposed something weaker: the post-policy gap is some weighted average (weights ≥ 0, summing to 1) of the pre-policy gaps. The bias may drift, but only within the range history spans. The counterfactual is then the comparison group's current distribution plus that mixture of past gaps. Different weights give different counterfactuals, so the result is a bound.

**What goes wrong with distributions.** The paper names three failure modes, none visible one statistic at a time:
- **Negative probability.** Comparison distribution + mixture of past gaps is a signed measure. It can assign negative mass to some outcome bins. Such a "counterfactual" describes no population.
- **Incompatible endpoints.** Bounding each wage cutoff separately, with weights re-optimized per cutoff, gives endpoints that no single counterfactual distribution produces together. This matters for e.g. the Cengiz et al. (2019) bunching estimator, which nets missing jobs below a new minimum wage against excess jobs just above it.
- **Pooling hides infeasibility.** When several policy events are stacked, the averaged counterfactual can be a valid distribution even though no event's counterfactual is.

The paper calls the requirement that the counterfactual be a real distribution "coherence".

## 2. Technical details

- **Model.** Two groups, dates −T₀,…,0,1, treatment from t = 1. Assumption 1: overlap, no interference, consistency and no anticipation. Assumption 2 (historical transport): ν₁ = Σ_s λ_s ν_s for some λ in the simplex over a chosen set S of historical dates. The same λ applies to every outcome event. Outcomes can be real, categorical or mixed (earnings with a mass at zero). Data can be panels or repeated cross-sections.
- **Economic content.** In a model with latent environments (e.g. recession vs. expansion) whose shares are common to both groups, Assumption 2 holds when today's environment shares lie in the convex hull of past shares. A testable implication: the comparison group's current distribution must itself be a mixture of its own past distributions. The author argues transport "deserves a hearing" when groups differ by stable characteristics, not by a transitory state that triggered treatment.
- **Comparison to other assumptions.** Changes-in-changes (Athey & Imbens 2006) allows extrapolation beyond history through a monotone transformation; historical transport forbids extrapolation but allows reordering of individuals. Bounded-trend approaches (Manski & Pepper; Rambachan & Roth) restrict one scalar and permit extrapolation up to a chosen multiple.
- **Sharp set (Theorem 1).** The identified set is the historical hull intersected with the set of probability distributions. The model is consistent with the data iff the coherent weight set is nonempty. On a K-cell grid, any linear contrast's bound is a linear program in |S| weights with K nonnegativity constraints. The theorem concerns marginals only: it identifies quantile treatment effects, not the distribution of individual effects.
- **Distance to feasibility (Theorem 2).** The total-variation distance from a signed measure to the nearest distribution equals its negative mass. The "minimum repair" d_S is the smallest such mass over the hull.
- **Checking each date alone is not a test.** Two invalid vertices can mix into a valid distribution, e.g. (−0.1, 1.1) and (1.1, −0.1) are valid for weights in [1/12, 11/12].
- **When coherence tightens a bound (Proposition 1).** Only if every mixture that attains the unrestricted bound is infeasible. A three-cell example shows it can flip a sign: the signed hull reports −0.10, the coherent lower bound is ≈ 0.088.
- **Infeasibility certificate (Theorem 3).** If no feasible mixture exists, a single nonnegative outcome score has negative expectation under every historical mixture. On a grid its margin equals the grid repair.
- **Stacking (Theorem 4).** Eventwise coherence implies stacked coherence, but not the reverse. Checking whether they agree takes E·K linear programs (events × cells). The paper also gives event-specific weights, and a family bounding how far event weights may differ (‖λ_e − λ̄‖₁ ≤ δ). Covariate cells work the same way as events.
- **Projection is not a fix (Proposition 2).** Projecting each invalid vertex onto the simplex and then mixing can give a hull disjoint from the coherent one.
- **Grids (Propositions 3–5).** Refining a grid weakly tightens bounds. Coarsening can never narrow a bound but can hide infeasibility completely. A grid-free confidence region uses one LP over all intervals: |S| + n variables and 5n − 1 sparse inequalities for n support points. With 22,339 distinct NSW/CPS earnings values, each LP took about seven seconds.
- **Breakdown (Proposition 7).** A total-variation ball of radius τ around the hull relaxes the model. The sign breakdown radius for an effect on an outcome share is one LP with both terms at the same λ, with a confidence interval. Wasserstein balls also stay linear on a grid. Exclusion restrictions (e.g. a ~$9 minimum wage should not change employment at $18) add linear equalities.
- **Inference (Section 6).** Vertex reduction (Lemma 1): the error of any mixture never exceeds the largest error at a historical date, so no optimal weight needs to be estimated. This gives confidence sets, a coherence test, and, with an experiment, a benchmark test of transport with a lower confidence bound on its error (Theorem 6, Proposition 8). DKW radii give finite-sample validity under independent individual histories; bootstrap and studentized versions are sharper and asymptotic. Clustered data are covered on a fixed grid with bands calibrated over clusters. Cells of estimated distributions with no known sampling distribution (the minimum-wage data) are not covered.
- **Plug-in incoherence is not evidence.** With continuous outcomes the empirical coherent set is almost surely empty. On a fixed grid with a single-point population coherent set, the plug-in set is empty about half the time.
- **Simulations.** Six cells calibrated to earnings data, (N₁, N₀) from (200, 2,000) to (5,000, 20,000), 1,000 replications.
  - Transport holds: all tests reject below 1%; coverage ≥ 99.9%; coherence gives a 19% shorter region only at the largest size.
  - Benchmark test (bootstrap): power 0.85 at CDF distance 0.07 with 1,000 treated; 0.62 at 0.12 with 200.
  - Boundary design: the naive "reject if plug-in set empty" rule rejects half the time under the null. The studentized test rejects < 1% and has power 0.69 against a repair of 0.02 with 1,000 treated; the unstudentized test has none.
  - Pooling: with event-specific true weights, the stacked bound excludes the true average effect in 29% of designs; the common-weight eventwise model is empty or excludes it in 72%.

## 3. Impact — potential & realized

**Measured — NSW experimental benchmark.** 185 participants, 260 experimental controls, CPS-1 (15,992) and PSID-1 (2,490) comparison men. History: 1974 and 1975; outcome: 1978; seven-cell grid fixed in advance. The experimental control distribution is the truth, used only for testing.
- Transport fails. CDF distance to the nearest transported distribution: 0.32 (CPS), 0.35 (PSID). 95% lower bounds: 0.20 and 0.23. About a third of the probability mass would need to move.
- Implied employment effect 0.38 to 0.49, against an experimental 0.111 [0.026, 0.195]. Single-base-year distributional DiD (0.38, 0.48) and changes-in-changes (0.41, 0.51) also overstate it by three times or more.
- Without the experiment, the studentized coherence test rejects for PSID (p = 0.013) but not CPS (p = 0.84).
- Cause: eligibility selected on recent joblessness (the Ashenfelter dip). Pre-program nonemployment gaps were 0.59 and 0.49 vs. a post-program gap of 0.22 (CPS).
- Placebo: with half the experimental controls as the comparison group, the benchmark test rejects in 1 of 200 splits and the coherence test in none.
- Breakdown (CPS): feasible from τ = 0.009; the sign is lost at τ = 0.38 [0.26, 0.51], vs. a revealed departure of 0.34. In Wasserstein terms, the sign is lost at an average earnings shift of $1,053, below the $2,630 departure the experiment reveals.

**Measured — 1993 EITC expansion.** March CPS extract, unmarried women 20–54 without a high-school diploma, tax years 1991–1996 (13,746 women). Mothers vs. childless women; history 1991–92; design fixed in writing before estimation.
- Diagnostics pass: coherence p = 1.00; placebo benchmark at 1993 p = 0.96.
- Employment bounds: 1994 [−0.010, 0.014]; 1995 [0.047, 0.070]; 1996 [0.115, 0.139]. The 95% outer region excludes zero in 1996 but not 1995.
- In 1996 the childless women's distribution leaves its own historical range (p = 0.01), so the protocol flags that year.
- Dropping the 27 states with welfare waivers approved by 1995 leaves every diagnostic passing; the 1996 bound becomes [0.084, 0.118], narrowed by coherence. Dropping all 36 states with approvals through 1996 widens the bounds; the 1995 bound then includes zero.
- Common weights link contrasts: in 1995, any counterfactual with an employment gain above 6.2 points implies a fall in the phase-out-range share.

**Measured — 2014 state minimum wages (descriptive only).** Cengiz et al. 118-bin state–quarter data, five 2014 increases, stacked with equal weights.
- All four historical vertices put negative mass on some bin. Coherence halves the bound on the change in the share employed below $9.25: [−0.614, −0.228] to [−0.517, −0.324] percentage points.
- But no state's counterfactual is a distribution, under common or state-specific weights. The stacked set is nonempty only because negative bins offset across states.
- The audit fails: comparison-state nonemployment lies 0.41 points below its historical minimum; dropping an anticipation-exposed quarter empties the coherent set; population weights move the bound to [−0.01, 0.08].

**Limitations the author states.** Coherence is a check, not a validation. Pre-treatment data cannot reveal which post-policy bias will occur. Adding historical dates widens the set, and choosing S is an identifying decision. Survey weights and designs with a handful of treated clusters are outside the theory. Generalized-moment-selection critical values lack established uniform validity; a crude cluster version over-rejected (6.7% at 5%). The EITC result has no experimental benchmark.

**Potential.** A concrete protocol: pick settings where selection reflects stable group differences; prespecify dates, grid and outcomes; end history before announcement; run the studentized coherence test and the event-level check; check the comparison group stays in its historical range; report the grid-free region and breakdown radius. The author suggests a validation on randomized phase-ins such as PROGRESA.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A careful distributional closure of an existing bounds idea, with one result practitioners should remember: stacking can hide impossible counterfactuals

The core model belongs to Ban et al.; the paper says so and calls itself its "distributional closure". Intersecting a signed hull with the simplex and solving LPs is standard partial-identification machinery. What lifts it above a routine extension is the audit work. The stacked-events result is simple but practically sharp, and the minimum-wage application shows it really happens. The NSW exercise is, per the author, the first experimental evaluation of a distributional pre-trend method, and its honest negative result is useful. Prespecifying the EITC design in writing is also good practice.

For data scientists running geo or market-level rollouts: if you build a distributional counterfactual (e.g. order-value or latency histograms) from pre-period gaps, check that it has no negative bins. Check it per market before pooling, and remember that a coarse binning can hide the problem. That transfer to tech settings is my extrapolation; the paper's applications are all labor economics. The tooling is heavy (LPs, studentized bootstrap), and with a few hundred treated units the author concedes coherence is mainly a diagnostic.

### Similar / related work

- [**From pre-trends to bounds: Robust difference-in-differences**](https://arxiv.org/abs/2211.06710) — Ban, Kédagni, Chen & Denteh. The scalar historical-range model for average effects that this paper extends to distributions.
- [**Parallel Trends as a Spectrum**](2026-10-28-arxiv-parallel-trends-as-a-spectrum-l-moments-did.md) (in this bank) — a different distributional DiD route: point identification by imposing parallel trends on selected L-moments rather than bounding with historical mixtures.
- [**When Covariates Mask Pre-Trends**](2026-11-06-arxiv-when-covariates-mask-pre-trends-honest-did.md) (in this bank) — another way pre-period information can mislead a pre-trend-based bound, here in honest-DiD sets with badly timed covariates.
- [**Positive Weights Do Not Certify TWFE Inference: A Design Diagnostic under Treatment-Effect Heterogeneity**](2026-11-16-arxiv-positive-weights-do-not-certify-twfe-inference.md) (in this bank) — a pooling diagnostic for staggered TWFE, also applied to minimum-wage data; parallels the stacking warning here at the estimation rather than identification level.

### Jargon buster

- **Distributional DiD** — DiD aimed at the whole counterfactual outcome distribution (shares, quantiles) rather than only its mean.
- **Selection bias ν_t** — the difference between the treated and comparison groups' untreated outcome distributions at date t; a signed measure summing to zero.
- **Historical transport** — the assumption that the post-policy bias is a weighted average of past biases, with one set of weights for every outcome event.
- **Coherence** — the requirement that a transported counterfactual is a real probability distribution, with no negative mass in any bin.
- **Minimum repair** — the least negative mass over all historical mixtures; the total-variation distance from the hull to the set of distributions.
- **Sign breakdown radius** — how far (in total variation) the model must be relaxed before the effect's sign is no longer determined.
- **Stacked vs. eventwise transport** — imposing the assumption only on the pooled average of events vs. on each event separately; the first is weaker.
- **Studentized coherence test** — a test of whether some weight makes every cell's mass nonnegative up to sampling error, scaled by each cell's standard error so rare cells get narrow bands.
