---
id: arxiv-gaffke-confidence-interval-discrete-bounded-mean
title: "Exact, narrow and fast: Use the Gaffke confidence interval for the mean of a discrete bounded variable"
source: "Louis Abraham (arXiv stat.CO)"
url: "https://arxiv.org/abs/2611.29512"
published: "2026-11"
added: "2026-11-27"
category: statistical-modeling
tags: [confidence-intervals, exact-inference, bounded-means, gaffke-interval, clopper-pearson, dirichlet, saddlepoint, small-samples, ratings]
novelty: 3
sourced_via: "full-text fetch"
---

# Exact, narrow and fast: Use the Gaffke confidence interval for the mean of a discrete bounded variable

**Source:** [Louis Abraham (arXiv stat.CO)](https://arxiv.org/abs/2611.29512) · Published 2026-11 · Added 2026-11-27
**Category:** Statistical Modeling · **Tags:** `confidence-intervals`, `exact-inference`, `bounded-means`, `gaffke-interval`, `clopper-pearson`, `dirichlet`, `saddlepoint`, `small-samples`, `ratings`

## TL;DR

Ratings, scores and similar data take a few known values. For small samples or means near the ends of the range, the usual intervals cover the mean much less often than claimed. The Gaffke interval generalizes Clopper–Pearson to any finite set of values and, since a 2026 proof of Gaffke's conjecture, has guaranteed coverage for every n and every distribution. This note gives a fast algorithm for its endpoints (under a millisecond for any n), shows it is the shortest valid published interval for n ≤ 30 (17–20% shorter than the betting interval), and ships tested Python and R packages named `gaffke`.

## 1. Business context

A sample of n trials, each taking one of k known values, has an unknown mean μ. Examples: ratings on a 1–5 scale, test scores, counts of items in classes of known size.

- **Normal-based intervals fail at the edges.** Wald and Student rest on the normal approximation. It fails for small n or when μ is close to an end of the range.
- **Distribution-free intervals are wide.** Hoeffding, empirical Bernstein, Anderson and betting intervals keep the level, but pay in width.
- **Gaffke's interval was stuck on two fronts.** Gaffke (2005) proposed the test and conjectured it was valid. Learned-Miller and Thomas (2019) studied the resulting interval for bounded data and proved validity for Bernoulli and half-Bernoulli data. Vlassis and Thomas (2026) proved the conjecture in general. Ming et al. (2026) showed its width is asymptotically that of the normal interval. But the endpoints are quantiles of a weighted sum of Dirichlet variables, with no closed form.

The note's bet: with a fast, accurate solver and packaged code, there is no remaining reason not to use it.

## 2. Technical details

- **The interval.** Counts X ~ Mult(n, p) over values v₁…v_k; μ = vᵀp. The level-(1−α) interval is L = Q_{α/2}(vᵀP₋), U = Q_{1−α/2}(vᵀP₊), with P₋ ~ Dir(X + e_{i_min}) and P₊ ~ Dir(X + e_{i_max}). In words: a Dirichlet with the observed counts as parameters, plus one extra unit on the smallest value (lower bound) or the largest value (upper bound).
- **Where it comes from.** Gaffke's test adds a zero to the sample, averages the n+1 values with Dir(1,…,1) weights, and rejects when that random average is rarely at most 1. Applying it to rescaled data and merging weights within each category gives the Dirichlet form above.
- **Clopper–Pearson as a special case.** For values (0, 1), the two Dirichlet sums become Beta(x, n−x+1) and Beta(x+1, n−x), which are exactly the Clopper–Pearson bounds.
- **"Exact" means what it means for Clopper–Pearson.** Coverage ≥ 1−α for every p and every n, not just asymptotically. In the experiments some one-sided coverages equal 1−α/2, so the author says the bound cannot be improved in general.
- **Reductions.** Drop categories with zero parameter, merge equal values, rescale to [0, 1]. One distinct value is trivial; two reduce to a Beta quantile. The numerical method is for k′ ≥ 3.
- **Tail probability as a Fourier integral.** Writing the Dirichlet via independent Gammas, P(Y ≤ y) = P(S ≤ 0) with S = Σ(wᵢ − y)Γᵢ, whose MGF is a product of simple factors. A Gil-Pelaez inversion integral is taken on a vertical line through the saddle point. The integrand's size at t = 0 equals the tail size, so quadrature error small relative to the integral is small relative to the tail.
- **Quadrature on geometric panels.** All singularities lie on the imaginary axis. The integral is cut where r(T) = e⁻⁴⁰ and split into panels whose lengths double, each with a 12-point Gauss–Legendre rule. On a panel [x, 2x] the imaginary axis maps to Re u = −3, so the convergence rate is the same on every panel wherever the singularities are. Panels are split further where the phase θ turns fast.
- **Quantile by Newton in log-distance.** Near the end of the tail, tail ≈ C·dᵃ, so the log-tail is nearly linear in u = log d. Newton runs on u, bracketed with bisection fallback, starting from a moment-matched Beta quantile (exact for two values). The upper endpoint solves P(Y > y) = α/2 directly, so 1 − α/2 is never formed.
- **Cost.** O(k log k + E(I + N)k) per endpoint. n enters only through the Dirichlet parameters, so cost does not grow with n. N = 60 nodes (five panels) for n ≥ 10⁶ in tests. Over random problems with k ≤ 20, n from 5 to 10⁹ and α ∈ {0.05, 10⁻⁶}: median N 60–192, max 456. E averages 2.6 evaluations per endpoint (max 7). There is no proven bound on N.
- **Monte Carlo is not an option for extreme levels.** A tail of 5×10⁻⁷ with relative error 10⁻¹⁰ would need about 2×10²⁶ samples.

## 3. Impact — potential & realized

**Measured — coverage and width (Table 1).** Values v = (0, ½, 1), α = 0.05. Minimum coverage over a lattice of 3,321 points of the simplex (boundary included), computed by enumerating all outcomes; mean expected width over the lattice.

| Interval | Min cov. n=5 | n=10 | n=30 | Width n=5 | n=10 | n=30 |
|---|---|---|---|---|---|---|
| Gaffke | 0.976 | 0.963 | 0.954 | 0.648 | 0.472 | 0.268 |
| Betting† | 0.991 | 0.982 | 0.946 | 0.797 | 0.592 | 0.323 |
| Anderson | 0.991 | 0.992 | 0.991 | 0.802 | 0.648 | 0.426 |
| Hoeffding | 0.991 | 0.992 | 0.991 | 0.878 | 0.728 | 0.470 |
| Empirical Bernstein | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.847 |
| Student t | 0.061 | 0.118 | 0.314 | 0.619 | 0.451 | 0.251 |
| Wald | 0.061 | 0.118 | 0.314 | 0.454 | 0.378 | 0.237 |
| Profile likelihood | 0.446 | 0.477 | 0.493 | 0.474 | 0.377 | 0.236 |
| Bayes (Jeffreys) | 0.000 | 0.000 | 0.000 | 0.490 | 0.377 | 0.234 |

†Betting depends on trial order; averaged over 8 random orders on a grid of step 10⁻³. Its 0.946 at n = 30 comes from those approximations.

- Among intervals that keep the level, Gaffke's is the shortest: 17–20% shorter than Waudby-Smith and Ramdas's betting interval, 19–37% shorter than Anderson's.
- The intervals below the line are 5–30% shorter still, but their minimum coverage falls far below 95%. Wald and Student bottom out at 0.061 at n = 5; the Jeffreys-prior Bayesian interval at 0.000.
- Results are the same for values (0, 0.1, 1) and for five values, per the author.
- Gaffke is not the shortest valid interval for every outcome: Ming et al. construct one that is strictly shorter in some cases. No published interval is shorter in this comparison.

**Measured — accuracy.** References: an exact B-spline formula in rational arithmetic (integer parameters), 40-digit inversion integrals, Beta law for two values, Monte Carlo, invariance and monotonicity checks, edge cases (n ≤ 1, n = 10¹², α = 10⁻¹⁵), and enumerated coverage for three values and n ≤ 13. Across all tests, including 40,000 random problems with up to 20 values and n up to 3×10⁶:
- endpoints within 10⁻¹² of the range of the values;
- tail probabilities with relative error below 10⁻¹⁰, down to α = 10⁻¹²;
- each one-sided coverage at least 1 − α/2.

**Measured — speed.** 0.15–0.3 ms per interval for k ≥ 3 and about 0.02 ms for two values, "almost all of it Python overhead".

**Software.** `pip install gaffke`, `install.packages("gaffke")`, and a browser page via a JavaScript port. Both packages expose `gaffke_ci(counts, values, alpha)` plus the CDF, density and quantile of wᵀP. The R port agrees with Python to 10⁻¹⁰ of the range; the JS port to 10⁻¹⁵. MIT licensed.

**Limitations the author states.** No proof of an error bound (the panel argument gives the convergence rate; tests measure the error). No proven bound on N. The interval is not the shortest valid one for every outcome. Scope: the values must be known and finite in number.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Turns a newly proven interval into a sub-millisecond default; solid numerics, not new statistics

The statistics belong to others: Gaffke's test, Learned-Miller and Thomas's interval, Vlassis and Thomas's validity proof, Ming et al.'s efficiency result. This note's contribution is engineering. Saddle-point inversion and Gauss–Legendre quadrature are textbook. Geometric panels chosen so the convergence rate is independent of where the singularities sit is a tidy observation. The testing is unusually thorough for a short note. The width comparison is useful and honest (it flags the betting approximations). It is narrow in scope, though: one three-value support, n ≤ 30, a single α, and summaries as worst-case coverage and lattice-mean width. Practitioners would want to see width at realistic sample sizes and on skewed supports like a 1–10 NPS scale. The asymptotic result says the gap to Wald should vanish there.

The practical case is still strong. The interval is a strict generalization of Clopper–Pearson, which most teams already trust for proportions. It now has a pip/CRAN install and runs fast enough for per-segment dashboards.

My extrapolation, not tested in the paper: A/B tests on rating or bounded metrics (CSAT, 1–5 star ratings, quiz scores, NPS buckets) often have small segments or means stuck near a ceiling. That is where Table 1 shows Wald and Student failing badly. Per-arm Gaffke intervals would be a safe way to report each arm's mean in small segments. But the paper gives an interval for *one* mean, not for a difference of two. Combining two per-arm intervals conservatively (e.g. Bonferroni-style) would be valid but wide. A proper two-sample version is not addressed here. At typical online-experiment sample sizes the CLT-based z-test will usually be fine anyway.

### Similar / related work

- [**Gaffke's confidence interval for the mean of bounded data is inadmissible but asymptotically efficient**](https://arxiv.org/abs/2607.18661) — Ming, Ramdas, Shen, Wang & Waudby-Smith (2026). Shows √n × width matches the normal interval, and that a strictly shorter valid interval exists in some cases.
- [**An exact distribution-free test for means of nonnegative random variables**](https://arxiv.org/abs/2607.08415) — Vlassis & Thomas (2026). The proof of Gaffke's conjecture that makes the interval's coverage guaranteed.
- [**A new confidence interval for the mean of a bounded random variable**](https://arxiv.org/abs/1905.06208) — Learned-Miller & Thomas (2019). Introduced the interval for bounded data and proved validity in the Bernoulli and half-Bernoulli cases.
- [**Why is it OK to run a z-test on a non-normal distribution for A/B tests?**](2026-09-30-statsig-z-test-non-normal-ab-tests.md) (in this bank) — a Statsig explainer defending CLT-based z-tests at typical online sample sizes. This paper's Table 1 shows where that defence breaks: small n and means near the edge of a bounded range.

### Jargon buster

- **Coverage** — the probability that an interval contains the true value; a 95% interval should do so at least 95% of the time.
- **Exact (Clopper–Pearson sense)** — coverage is guaranteed at the nominal level for every sample size and distribution, not only as n grows.
- **Clopper–Pearson interval** — the classic exact interval for a binomial proportion, built from Beta quantiles; the Gaffke interval reduces to it for 0/1 data.
- **Dirichlet distribution** — a distribution over probability vectors (non-negative, summing to one); here it describes the random weights whose weighted sum gives each endpoint.
- **Saddle point** — the point on the real axis where the log-MGF's derivative is zero; integrating through it keeps the integrand well behaved and the tail error relatively small.
- **Gauss–Legendre quadrature** — a numerical integration rule that evaluates the function at specially chosen nodes; very accurate for smooth functions.
- **Betting interval** — Waudby-Smith & Ramdas's distribution-free interval built from the wealth of a hypothetical bettor; valid but, here, 17–20% wider than Gaffke's.
- **Inadmissible** — some other valid interval is never wider and is strictly shorter in some cases.
