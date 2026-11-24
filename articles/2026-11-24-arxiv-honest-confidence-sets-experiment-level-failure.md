---
id: arxiv-honest-confidence-sets-experiment-level-failure
title: "Honest confidence sets under experiment-level failure"
source: "City University of Macau / University of Georgia (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.20079"
published: "2026-11"
added: "2026-11-24"
category: experimentation-causal
tags: [confidence-sets, huber-contamination, minimax, randomized-inference, robust-inference, prevalence-estimation, coverage, reference-calibration]
novelty: 3
sourced_via: "full-text fetch"
---

# Honest confidence sets under experiment-level failure

**Source:** [City University of Macau / University of Georgia (arXiv stat.ME)](https://arxiv.org/abs/2611.20079) · Published 2026-11 · Added 2026-11-24
**Category:** Experimentation & Causal Inference · **Tags:** `confidence-sets`, `huber-contamination`, `minimax`, `randomized-inference`, `robust-inference`, `prevalence-estimation`, `coverage`, `reference-calibration`

## TL;DR

Sometimes a whole experiment can fail, not just a few observations. This paper asks how precise an honest 95% confidence set can be when a declared 5% bound on failure probability uses up the entire noncoverage budget. At that boundary, every deterministic procedure for a Uniform endpoint or a Gaussian mean has full-range worst-case expected width. Independent randomisation restores shrinking width, at sharp rates of (2+o(1))·log N/N and (2σ+o(1))·√(log N/N). The authors also show two settings where the data supply that randomness themselves: observation order under exchangeability, and a small reserved subset of a reference sample.

## 1. Business context

The paper is theory-first, and its motivation is statistical rather than commercial. A team may have a well-understood clean model but know that, with some probability, the whole experiment can fail in a way that replaces the joint data law while the target stays the same. The question is what "95% coverage, guaranteed" can still mean then.

The authors model this as a Huber contamination neighbourhood on the sample space of the *entire experiment*, not on individual observations. They contrast this with recent work on observation-wise contamination for Gaussian means, binomial proportions, linear regression and high-dimensional means. Their applied setting is population-count inference in a fixed roster. Membership of the main roster is latent, and a separate roster of known members calibrates a binary response mechanism. This relates to prevalence correction in the style of Rogan–Gladen. Calibration can fail across shared environments with declared probability η.

## 2. Technical details

- **Model.** The observation law is P = (1−λ)·G_θ + λ·Q, where G_θ is the clean law, Q is any allowed failure law for the full observation vector, and the actual failure probability λ can be anything in [0, η]. A set is *honest* if its noncoverage is at most α uniformly over θ, λ and Q. Risk is the worst-case expected diameter. The focus is the boundary η = α.
- **Deterministic obstruction.** Take any deterministic rule with positive clean error at θ. A failure law can be the clean law conditioned on that error event, which makes the miss certain. At λ = α the error then exceeds α. So clean coverage must be perfect, and this forces full-range width (risk 1 for the endpoint in [1, 2], and D for the Gaussian mean).
- **Randomised fix (Proposition 2).** Build a base set with clean error β. With an independent seed, return the full range with probability p_β = (1−α)β / (α + (1−α)β), and the base set otherwise. This is honest under every allowed mixture. With β = 1/N (endpoint) or N^(−1/2) (Gaussian), it attains the sharp rates. The seed works because the failure law cannot control it.
- **Coverage budget (Lemma 1) and information cost (Corollary 2).** A failure law shared by many targets means a short set covers only a small fraction of the parameter range. Uniform coverage then forces average clean-state noncoverage to fall with expected width. Combined with a one-sided local KL bound of order N·h^κ, this gives a general lower rate (log N/N)^(1/κ).
- **Error-budget frontier (Theorem 3).** For the endpoint with deterministic rules: polynomial slack δ_N = N^(−γ) between allowed noncoverage and failure bound gives width (2γ+o(1))·log N/N. Exponentially small slack gives a positive limiting width min{1, 2(1−e^(−c))}. Zero slack forces full range.
- **Recovery from observation order.** Under exchangeable failure laws without ties, the original index of the largest observation is uniform and independent of the statistic. It can serve as the coin, so a *deterministic* rule attains the randomised rates, at a rounding cost of at most 1/N (endpoint) or D/N (Gaussian). Permutation-invariant deterministic rules still have full-range risk.
- **Roster rate (Theorem 4).** The randomised minimax width separates main-sample noise √n, reference noise n/√m, calibration tolerance nε and background ambiguity nδ_b. For a balanced, exactly calibrated roster with known background, the count risk is of order √n, √(n log n) and n for fixed η < α, η = α and fixed η > α respectively.
- **Deterministic roster obstruction (Theorem 5) and reference reserve (Theorem 6).** With unrestricted response probabilities and a rational background, deterministic honest rules have width approaching the full count range. If a prespecified reserve of O(log m) reference responses has probabilities bounded away from 0 and 1 in every state, a fixed linear map over GF(2) turns them into an approximately uniform seed. A deterministic rule then attains the randomised rate on that subclass. The reference sample thus does two jobs: calibration and preserving randomness.

## 3. Impact — potential & realized

**Measured (analytic bounds and simulations only; no real-data application):**
- **Finite-sample bounds.** For η = α = 0.05, finite lower and upper bounds bracket the randomised minimax risk and converge slowly to the sharp asymptotic limits over N from 10² to 10¹⁴.
- **Roster simulation at η = α.** The setting uses α = 0.05, τ = 0.1, known background 0.1 and true count 0.4n, with 50,000 response sets per state. External randomisation gives mean width 0.3225·D_n at n = m = 4,000 and 0.0955·D_n at 64,000. The deterministic reference-reserve rule gives 0.3732·D_n and 0.0999·D_n, using reserves of 126 and 168 responses.
- **Deterministic floor vs alternatives.** At the clean law G₋ with n = m = 4,000, every deterministic rule honest over the unrestricted class has expected width at least about 0.990·D_n. External randomisation reaches 0.217·D_n, and the reserve rule (honest on the smaller interior subclass) reaches 0.235·D_n.
- **Coverage.** The smallest coverage estimate across the selected designs is 0.9515. Misspecification matters: declaring η = 0.04 when the actual failure probability is 0.05 drops coverage to 0.9495.
- **Below the boundary.** For η < α at n ≥ 4,000, the bound-based selection picks plain direct inversion, so all three procedures coincide there.

**Potential:** A precise account of what experiment-level failure costs: a logarithmic factor at the boundary, and full range for any deterministic rule unless the failure class leaves some usable randomness. The authors flag open questions, including how to split the error budget when the failure bound itself is learned from auxiliary data.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Sharp, elegant minimax theory, but far from day-to-day practice

The randomised-versus-deterministic separation is clean, and the two "free randomness" results are clever: argmax index under exchangeability, and linear extraction from a reserved reference subset. They make a simple point concrete. When your failure allowance equals your error budget, any deterministic interval can be beaten by an adversarial failure, and only a coin that the failure cannot see gets you a useful width.

For working data scientists the main lesson is conceptual. If you budget a known probability that a whole study or calibration source is broken, you must leave noncoverage slack beyond it, or your "honest" interval collapses to the full range. Randomised intervals that sometimes return the full range are a hard sell in practice. The applications are stylised, with Uniform, Gaussian and a binary roster model plus simulations, and the failure bound η has to be declared from outside. A single roster does not identify it, as the authors note.

### Similar / related work

- [**Robust confidence intervals for a binomial proportion: local optimality and adaptivity**](https://arxiv.org/abs/2509.05568) — Cho, Luo & Gao; robust intervals under observation-wise contamination, the setting this paper contrasts with experiment-level failure.
- [**Adaptive robust confidence sets in high dimensions**](https://arxiv.org/abs/2610.15723) — Diakonikolas, Gao, Kane & Luo; the high-dimensional Gaussian mean version of observation-wise robust confidence sets.
- **Robust confidence limits** — Huber (1968); the original randomised minimax confidence procedures under contamination that this work builds on.
- [**Honest Inference for Synthetic Controls with Imperfect Fit: Time-Split Validity and the Choice of Anchor**](2026-10-26-arxiv-honest-inference-synthetic-controls-imperfect-fit.md) (in this bank) — another "honest" interval whose coverage holds under an explicitly declared bound on how far the model may fail.

### Jargon buster

- **Honest confidence set** — one whose coverage guarantee holds uniformly over every law in the declared model class, including the worst-case failure.
- **Huber contamination** — a model where data come from the clean law with probability 1−λ and from an arbitrary law with probability λ; here applied to the whole experiment at once.
- **Randomised confidence procedure** — uses an independent random seed besides the data; here it means sometimes returning the full parameter range on purpose.
- **Minimax expected diameter** — the smallest worst-case average interval width any honest procedure can achieve.
- **Reference reserve** — a prespecified small subset of known-member responses set aside to generate a nearly uniform random seed instead of being used for calibration.
