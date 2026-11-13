---
id: arxiv-instrumental-variables-treatment-clusters
title: "Instrumental variables with treatment clusters"
source: "arXiv econ.EM (Nibbering, Oosterveen & Silva — Monash, ISEG Lisbon, UAB)"
url: "https://arxiv.org/abs/2611.13313"
published: "2026-11"
added: "2026-11-13"
category: experimentation-causal
tags: [instrumental-variables, LATE, multiple-treatments, monotonicity, regression-discontinuity, testable-implications, treatment-aggregation]
novelty: 3
sourced_via: "full-text fetch"
---

# Instrumental variables with treatment clusters

**Source:** [arXiv econ.EM (Nibbering, Oosterveen & Silva)](https://arxiv.org/abs/2611.13313) · Published 2026-11 · Added 2026-11-13
**Category:** experimentation-causal · **Tags:** `instrumental-variables`, `LATE`, `multiple-treatments`, `monotonicity`, `regression-discontinuity`, `testable-implications`, `treatment-aggregation`

## TL;DR

Researchers often collapse many unordered treatments (e.g. 22 fields of study) into a few clusters (STEM vs non-STEM) and run IV as if each cluster were a binary treatment. The paper shows what that estimand is: a weighted average of pairwise LATEs across clusters — but only under assumptions stated at the *unclustered* level, which cluster-level IV assumptions don't imply. With unclustered data, those assumptions have testable necessary conditions; in a Portuguese university-admissions application they pass for STEM/non-STEM but are rejected for an eight-cluster ISCED grouping.

## 1. Business context

Aggregating treatments is common for practical reasons: small categories can't be disclosed for privacy, many pairwise effects are estimated imprecisely, and policy may be set at the cluster level. Product analogues are everywhere — "any premium plan" vs "free", "any recommendation surface" vs none — where users actually choose among finer options. If an instrument (an offer, an encouragement, a cutoff) shifts choices *within* a cluster as well as across clusters, a cluster-level IV can mix in effects that have nothing to do with the cluster contrast, or with negative weights.

## 2. Technical details

**Setting.** Unordered treatment D ∈ {1..J} and instrument Z ∈ {1..J} on the same support; standard independence and exclusion. Cluster-level IV estimand β = ΔE[Y | Z̃₁] / ΔE[D̃₁ | Z̃₁], with relevance imposed only at the cluster level.

**Decomposition (Lemma 1).** β is not necessarily a positively weighted average of cross-cluster effects. Response types who switch the "wrong way" across clusters enter with negative weight; types who switch *within* cluster 1 or within cluster 2 contribute extra terms B₁ and B₂. Cluster-level monotonicity (as used in prior STEM IV work) removes the negative terms but not B₁, B₂; a cluster-level exclusion restriction would force those within-cluster effects to be zero.

**Assumptions at the unclustered level.**
- *Monotonicity (A3):* an offer in cluster S_a can't make a specific S_a treatment less likely than an offer in S_b would — this rules out, e.g., a student choosing Physics under a Physics offer but Engineering under a non-STEM offer.
- *Irrelevance (A4):* rules out switching between two different treatments both outside S_a — less restrictive than the irrelevance assumptions needed for unclustered pairwise LATEs (Bhuller & Sigstad 2024).
- *Control group (A5)* for more than two clusters.
Under these, β (and its TSLS generalization to any number of clusters and matching instruments, and a fuzzy-RDD version) identifies a weighted average of LATEs over all cross-cluster treatment pairs and instrument values.

**Testable necessary conditions (Prop. 1).** With unclustered treatment data, sign restrictions on φ = E[1{Y∈A}·D_l | Z=j] − E[1{Y∈A}·D_l | Z=k] (≥ 0, ≤ 0 or = 0 depending on where l, j, k sit) can be tested as conditional moment inequalities (intersection-bounds framework; Stata `clrtest`), with Holm corrections across samples. The authors warn that sequentially testing to find a grouping that passes creates a pre-testing problem.

## 3. Impact — potential & realized

**Realized (application).** Portuguese centralized public university admissions (deferred-acceptance, up to six ranked courses), four cohorts; course cutoffs give a fuzzy RDD; outcome is second-year ECTS credits; 22 two-digit ISCED fields as unclustered treatments.
- STEM vs non-STEM: offers raise cluster enrollment by 88 pp (STEM) and 82 pp (non-STEM). STEM enrollment *lowers* second-year ECTS by 3.15 credits (~88 hours of intended workload) for students preferring STEM; non-STEM enrollment raises ECTS by 1.33 credits for students preferring non-STEM. No significant violations of the necessary conditions after Holm correction.
- Eight ISCED clusters: take-up effects mostly 0.80–0.90; four effects significant at 5% after Holm (twelve before), with average absolute values of 4.13 and 3.44 ECTS respectively. The necessary conditions are **rejected** for the Health and Personal-services fields, so a causal interpretation of the eight-cluster estimates is rejected.

**Potential.** A checklist for any aggregated-treatment IV: state assumptions at the fine level, and test them when fine-grained choice data exist.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A clean identification result with a practical test; most valuable as a warning about how you define the treatment.

The STEM/ISCED contrast is the memorable part: the same data, grouped two ways, passes the test once and fails it once. For experimentation teams the analogue is encouragement designs where the "treatment" is a bundle — the instrument may move people between options inside the bundle, and the cluster-level Wald ratio silently absorbs those moves. If you have the fine-grained choice logs, the paper gives you a falsification test for free.

### Similar / related work

- [**A Practical Guide to Instrumental Variables Methods with Heterogeneous Treatment Effects**](https://arxiv.org/abs/2605.15115) — background on LATE interpretation under heterogeneity
- [**Do Modern Difference-in-Differences Estimators Change Published Findings in Business Research?**](2026-11-11-arxiv-modern-did-estimators-business-research-replication.md) — in this bank: another case where hidden negative weights change what an estimand means
- [**Aggregating treatment effects across multiple outcomes**](2026-11-12-arxiv-aggregating-treatment-effects-multiple-outcomes.md) — in this bank: aggregation on the outcome side rather than the treatment side

### Jargon buster

- **LATE** — Local average treatment effect: the effect for "compliers" whose treatment choice the instrument changes.
- **Monotonicity** — The instrument pushes everyone's choice in the same direction (no "defiers").
- **Fuzzy RDD** — Regression discontinuity where crossing a cutoff changes the probability of treatment, used as an instrument.
- **Response type** — A person's full list of treatment choices under each possible instrument value.
- **ECTS** — European study-credit unit; 60 ECTS ≈ one academic year (1,500–1,800 hours of workload).
