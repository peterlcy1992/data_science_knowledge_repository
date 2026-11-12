---
id: arxiv-auc-brier-decision-weighted-auc-policy-youden-index
title: "One Curve, Different Weights: AUC, the Brier Score, Decision-Weighted AUC, and the Policy Youden Index"
source: "arXiv stat.ME (Yegor Baranovski)"
url: "https://arxiv.org/abs/2611.14465"
published: "2026-11"
added: "2026-11-12"
category: statistical-modeling
tags: [model-evaluation, AUC, Brier-score, Youden-index, decision-analysis, H-measure, model-selection]
novelty: 3
sourced_via: "full-text fetch"
---

# One Curve, Different Weights: AUC, the Brier Score, Decision-Weighted AUC, and the Policy Youden Index

**Source:** [arXiv stat.ME (Yegor Baranovski)](https://arxiv.org/abs/2611.14465) · Published 2026-11 · Added 2026-11-12
**Category:** statistical-modeling · **Tags:** `model-evaluation`, `AUC`, `Brier-score`, `Youden-index`, `decision-analysis`, `H-measure`, `model-selection`

## TL;DR

AUC, the Brier score and a new decision-weighted AUC are all weighted averages of one curve, the Youden index J(t)=TPR−FPR across cutoffs; they differ only in which cutoffs they weight. When the decision policy is known, the paper argues models should be compared by its numerator, the policy Youden index — the expected share of positives the policy acts on minus the share of negatives.

## 1. Business context

Risk scores are used to decide who to act on: a lender approves, a hospital treats, a bank blocks a payment. Model choice is usually made on AUC or the Brier score, which can rank models differently, and it is unclear what each rewards in terms of the decisions actually taken. Hand (2009) objected that AUC measures different models with different 'rulers'. This paper gives a single lens to see what each metric weights and proposes one aligned with a stated decision policy.

## 2. Technical details

**Core identity (cutoff lemma).** For any nondecreasing weight w with values in [0,1] (read as the probability of acting on score s), the average of J over a random cutoff with CDF w equals E[w(S₁)] − E[w(S₀)]. Every result is one choice of w; all hold for discrete scores with ties.

- **AUC** = ½ + E[J] with cutoffs weighted by the (mid-point) distribution of all scores — equal weight on acting on the top 10%, top 20%, and so on. With n distinct scores, AUC = ½ + (J₁+…+Jₙ₋₁)/n.
- **Brier score** = E[(p−r)²] + Var(Y)(1 − E[J]) with cutoffs weighted by the true probability r — equal weight on every risk threshold, plus a miscalibration penalty. For the ideal forecast, the Brier skill score is E[J].
- **AUC_π** weights each positive–negative pair by |π(s) − π(s′)|, how differently the decision maker treats them, giving AUC_π = ½ + E[J(T_π)] / (2E|π(S₁)−π(S₀)|). Theorem 4: this is, up to scale, the only pair weight fixed in advance that makes a pair-weighted AUC an average of J for every score distribution.

**Coherence.** Because AUC's weights come from each model's own scores, two models' AUCs count different decisions (Hand's critique restated). The numerator J_π judges every model by the same policy, so it is coherent; the ratio AUC_π is not, because its denominator (share of pairs split) depends on the model. When π is linear in r, AUC_π is exactly a rescaled Brier skill score.

## 3. Impact — potential & realized

**Realized (worked examples, no empirical study).** Ten applicants, two models: AUC is 0.80 for A and 0.72 for B, yet a lender funding three loans gets J₃ = 0.2 under A and 0.6 under B — AUC prefers A because A ranks well near the bottom of the list, where no decisions are made. A second example (models C and D under a 70% threshold) shows AUC_π preferring C (1.0 vs 0.86) only because C is judged on 5 pairs and D on 14, while J_π correctly prefers D (0.4 vs 0.2). The same weighting issue applies when one model's AUC is compared across demographic groups; the fix is to use one weight for both groups.

**Potential.** J_π needs only the mean of π in each class, so it is trivial to compute; when the policy is unknown it can be reported over a range of plausible policies, including as the cross-validation criterion.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A clean unifying identity with a directly usable recommendation: score models by the policy you will actually run.

Not a new paradigm — Hand's H-measure, Hernández-Orallo et al.'s threshold-choice framework and net-benefit curves cover similar ground, and the paper says so. Its value is pedagogical clarity plus a metric (J_π) you can compute from two class means. For product data scientists the direct application is capacity-constrained targeting (top-k outreach, fraud review queues, promo eligibility): if ops will only ever act on the top 3%, evaluate and select on that policy, not AUC. Caveat: it's a theory note with toy examples — no empirical study of how often AUC/J_π disagree in practice.

### Similar / related work

- [**When Predictive Fit Misleads: Selecting Marketing Mix Models Using Experimental RoAS Benchmarks**](2026-11-06-arxiv-when-predictive-fit-misleads-mmm-experimental-roas.md) — in this bank: another case of a generic fit metric selecting the wrong model for the decision
- [**How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of Post-hoc Calibration**](2026-11-03-arxiv-ctr-recalibration-temporal-evaluation-fresh-data.md) — in this bank: the calibration side the Brier score penalizes and J_π ignores
- [**Measuring classifier performance: a coherent alternative to the area under the ROC curve (Hand, 2009)**](https://doi.org/10.1007/s10994-009-5119-5) — the H-measure and the coherence critique this paper restates in Youden terms

### Jargon buster

- **Youden index J(t)** — TPR minus FPR at a cutoff: the extra share of positives a rule reaches compared with acting at random.
- **Brier skill score** — How much a probabilistic forecast's squared error improves on always predicting the base rate.
- **Policy Youden index J_π** — Expected share of positives a fixed (possibly randomized) acting policy reaches minus the share of negatives it reaches.
- **Coherent metric** — One that judges every model with the same weights on decisions, so differences reflect the models, not the ruler.
