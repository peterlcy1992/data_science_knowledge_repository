---
id: arxiv-curiosity-aware-recommendation-information-gap
title: "When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field Evidence"
source: "arXiv econ.GN (Li & Tuzhilin; working paper)"
url: "https://arxiv.org/abs/2611.14938"
published: "2026-11"
added: "2026-11-13"
category: personalization-recsys
tags: [curiosity, beyond-accuracy, information-gap-theory, axiomatic-measure, online-ab-test, heterogeneous-effects, exploration]
novelty: 3
sourced_via: "full-text fetch"
---

# When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field Evidence

**Source:** [arXiv econ.GN (Li & Tuzhilin)](https://arxiv.org/abs/2611.14938) · Published 2026-11 · Added 2026-11-13
**Category:** personalization-recsys · **Tags:** `curiosity`, `beyond-accuracy`, `information-gap-theory`, `axiomatic-measure`, `online-ab-test`, `heterogeneous-effects`, `exploration`

## TL;DR

The authors turn Loewenstein's information-gap theory of curiosity into five axioms and derive a computable per-user, per-item curiosity score from consumption histories. They validate it against self-reported curiosity in a 283-person survey, add it to a relevance model's ranking utility, and report a month-long A/B test (516,201 users, 2021) at a large Asian video platform in which click-through rose 2.75 percentage points, completed views 1.97 points and time spent 0.71 minutes per recommendation; the company has since deployed the method.

## 1. Business context

Relevance-only recommenders tend to repeat what users already consume, producing filter bubbles, lower sales diversity and dissatisfaction. Existing "beyond-accuracy" proxies — unexpectedness, variety-seeking, Wundt-curve arousal — score an item by its distance from the user's taste, but the authors argue curiosity also depends on what the user already knows *near* the item: an item next to a partially explored area opens a perceivable gap, one in totally unfamiliar territory opens none.

## 2. Technical details

**Measure.** Curiosity C depends only on three state variables (Axiom 1): the *information gap* g (Euclidean distance between the item vector and a sequential encoding of the user's history), the *surrounding context* f (a saturating transform of a Gaussian-kernel sum of the user's consumed items near the item, in [0,1)), and the *reference gap* τ (a recency-weighted — exponentially decayed — average of gaps the user has encountered). The other axioms: no curiosity at zero context or extremely large gaps (perceivability); the curiosity-maximizing gap shrinks as context grows; it grows with the reference gap; and the reference gap adapts to recent experience. The axioms plus shape conditions determine a canonical functional form.

**Recommender.** Ranking utility V = (1 − α)·r̂ + α·w·C, with both terms standardized, r̂ from any relevance model (CF, MF, NCF, DeepFM, DIN…), w a per-user curiosity responsiveness estimated by regressing the user's past engagement on C, and α a platform policy parameter tracing the convex part of the relevance–curiosity Pareto frontier.

**Validation survey.** 300 adults (283 retained after an attention check; 4,245 film-level observations from MovieLens). Pearson correlation with self-reported curiosity: 0.636 (designed gaps) / 0.598 (computed gaps), vs 0.603 unexpectedness, 0.589 variety-seeking, 0.611 Wundt-curve arousal. With participant fixed effects, C stays significant (β = 4.29) while perceived novelty and unexpectedness become insignificant. Axiom tests: almost no curiosity at zero context; inverted-U in the gap; the peak gap rises across reference-gap terciles (1.72, 2.70, 3.73).

**Offline.** On Yelp, MovieLens and Alibaba-Youku, the curiosity-aware system is reported to significantly beat state-of-the-art baselines on accuracy, diversity and novelty metrics.

## 3. Impact — potential & realized

**Realized (online experiment).** 516,201 users split by hashing into control (production DIN) and treatment (same relevance score plus the curiosity utility, with a simplified latency-friendly computation), over one month in 2021 and 26,959,538 recommendation records; covariate balance checked (all standardized mean differences ≤ 0.051). OLS with video/user features and date-hour fixed effects: CTR +2.75 pp, video views +1.97 pp, time spent +0.71 min per recommendation (all p < 0.01). Heterogeneity: larger effects for younger users (under-30s +11.46 pp CTR vs no-age-reported users; over-60s −13.84 pp), premium users, users with deeper histories (+0.87 pp per SD) and more recent activity (+1.19 pp per SD) — patterns the authors present as consistent with the theory. An illustrative extrapolation to 500M MAU gives 308M viewing hours/month and US$101–108M/year of revenue, assuming everyone responds as in the experiment.

**Potential.** A theory-grounded, plug-in objective that works on top of an existing relevance model with little serving cost.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A neat axiomatization with a real A/B test, but the measurement edge over existing proxies is small.

The idea that curiosity needs *context* near the item, not just distance, is a genuinely useful refinement of novelty/serendipity scoring, and the heterogeneity analysis (bigger effects for deeper, more recent histories) is a nice theory-driven check. But the survey correlation gap over the best proxy is 0.636 vs 0.611 with no uncertainty interval quoted, the A/B test is from 2021, the OLS is at the recommendation level with tables reporting "robust standard errors" — randomization was by user, so user-clustered errors would be the safer choice and could widen the intervals, and the revenue extrapolation assumes uniform response. Data scientists should treat the online lift as one experiment against one baseline, not a general effect size.

### Similar / related work

- [**Statistical Detection of Positional Bias in LLM-Based Recommender Systems: Methodologies and Empirical Evidence**](2026-11-04-arxiv-statistical-detection-positional-bias-llm-recommender.md) — in this bank: another statistically careful look at what recommenders actually optimize
- [**Exploratory creative pre-ranking: Hierarchical empirical-Bayes Thompson sampling for real-time creative optimization**](2026-10-29-roblox-creative-pre-ranking-empirical-bayes-thompson-sampling.md) — in this bank: exploration framed as a bandit rather than as a curiosity objective
- **Unexpectedness in recommender systems (Adamopoulos & Tuzhilin, 2014)** — the proxy metric this paper's measure is compared against

### Jargon buster

- **Information-gap theory** — Loewenstein's (1994) account: curiosity arises when people notice a gap between what they know and what they want to know.
- **Surrounding context** — How much of what the user has already consumed lies near a candidate item.
- **Reference gap** — The size of gap a user has recently become used to; it moves the gap that feels most intriguing.
- **Linear scalarization** — Combining two objectives as a weighted sum to pick points on their trade-off frontier.
