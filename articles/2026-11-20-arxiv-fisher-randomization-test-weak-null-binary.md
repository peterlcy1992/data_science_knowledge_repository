---
id: arxiv-fisher-randomization-test-weak-null-binary
title: "On the Validity of Fisher Randomization Tests under the Weak Null"
source: "Sudijono, Dobriban & Tchetgen Tchetgen (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.24821"
published: "2026-11"
added: "2026-11-20"
category: experimentation-causal
tags: [randomization-inference, fisher-randomization-test, weak-null, binary-outcomes, fishers-exact-test, mcnemar, matched-pairs, bernoulli-design]
novelty: 3
sourced_via: "full-text fetch"
---

# On the Validity of Fisher Randomization Tests under the Weak Null

**Source:** [Sudijono, Dobriban & Tchetgen Tchetgen (arXiv stat.ME)](https://arxiv.org/abs/2611.24821) · Published 2026-11 · Added 2026-11-20
**Category:** Experimentation & Causal Inference · **Tags:** `randomization-inference`, `fisher-randomization-test`, `weak-null`, `binary-outcomes`, `fishers-exact-test`, `mcnemar`, `matched-pairs`, `bernoulli-design`

## TL;DR

The Fisher randomization test (FRT) is normally justified only under the sharp null that no unit responds to treatment. For binary outcomes, this note proves it is exactly finite-sample valid for Neyman's weak null (zero average effect) in three designs. They are balanced completely randomized experiments with difference-in-means, matched pairs with difference-in-means, and balanced Bernoulli designs with the centered Horvitz–Thompson statistic. So Fisher's exact test and McNemar's test are weak-null valid in those designs. In any design, twice the one-sided FRT p-value is valid.

## 1. Business context

Analysts run permutation tests and Fisher's exact test on conversion-style binary outcomes all the time, but the textbook justification (no individual effects) is stronger than the question they usually ask (is the average effect zero?). Asymptotic weak-null validity was known for studentized statistics. Finite-sample-valid alternatives (Chiba / Rigdon–Hudgens, concentration-inequality tests) are computationally heavy or conservative. The paper shows the plain FRT already has the guarantee in common binary designs.

## 2. Technical details

- **Results.** One- and two-sided FRTs are valid for H≤0N and H0N respectively, for all even n, in a balanced completely randomized experiment (CRE) with difference-in-means. The same holds for matched pairs with a fair coin per pair, and for a balanced Bernoulli design with the centered Horvitz–Thompson statistic. A corollary covers Fisher's exact test (CRE) and McNemar's test (pairs).
- **Unbalanced designs.** Twice the one-sided FRT p-value is valid under the weak null.
- **Proof idea.** Symmetric designs make the imputed reference distribution symmetric around zero, and the proof then works through the principal-strata counts (n11, n10, n01, n00) of a binary table.
- **Limit.** Example A.1 shows the FRT can be anticonservative for non-binary outcomes. Extending to bounded outcomes is left open.

## 3. Impact — potential & realized

**Measured:**
- Simulations (α = 0.05, n up to 300, 200,000 reassignments per setting) cover rare outcomes (τ = 0.05, p0 ∈ {0, 2.5, 5%}), common outcomes (p0 = 30%, τ ∈ {0.1, 0.2, 0.3}) and a no-harm monotone suite. FRTs generally beat concentration-inequality tests and are similar to the Chiba–Rigdon–Hudgens test, except for a clear advantage with rare outcomes in the CRE.
- With matched pairs, the paired FRT is much more powerful than the alternatives for rare outcomes. Wilson's method is competitive elsewhere.

**Potential:** A licence to use simple permutation tests and Fisher's exact test as finite-sample tests of 'no average effect' on binary conversion metrics, provided the design is balanced (or with the 2× rule if not). This is useful for small or rare-event experiments where asymptotics are shaky.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A clean, practically reassuring theorem for binary A/B tests

The theorem is narrow but lands squarely on what practitioners already do. Many teams run 50/50 tests on binary metrics and quote Fisher's exact or a permutation p-value. Now that p-value means what they thought it meant (no average effect), not only 'no effect for anyone'.

Caveats: binary outcomes only, the specific statistics named, balanced or symmetric designs for the direct result, and anticonservatism shown for non-binary outcomes. So don't generalize to revenue.

### Similar / related work

- [**Randomization Tests in Switchback Experiments**](2026-10-05-arxiv-randomization-tests-switchback.md) (in this bank) — randomization inference in a different design, where sharp-null vs weak-null also matters.
- [**Randomization Tests for Weak Null Hypotheses in Randomized Experiments**](https://arxiv.org/abs/1809.07419) — Wu & Ding; asymptotic weak-null validity via studentized statistics, the prior state of the art this note sharpens to finite samples for binary outcomes.
- [**Stratified Randomization Incorporating Historical Control Data**](2026-11-17-arxiv-stratified-randomization-historical-control-data.md) (in this bank) — design-based inference for randomized trials with small samples.

### Jargon buster

- **Sharp (Fisher) null** — no unit's outcome changes under treatment.
- **Weak (Neyman) null** — the average treatment effect over the sample is zero; individuals may still respond in opposite directions.
- **Fisher randomization test** — re-randomize treatment labels many times assuming the null, and see how extreme the observed statistic is.
- **Centered Horvitz–Thompson** — an inverse-probability-weighted difference estimator, centred so that its randomization distribution behaves under Bernoulli assignment.
