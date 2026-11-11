---
id: arxiv-pp-rank-prediction-powered-llm-ranking-adaptive-feedback
title: "Prediction-Powered LLM Ranking with Adaptively Collected Human Feedback"
source: "arXiv stat.ME (Sargent, Sun, Zhang, Liu; UNC Chapel Hill, Purdue, Michigan)"
url: "https://arxiv.org/abs/2611.13186"
published: "2026-11"
added: "2026-11-11"
category: llm-genai
tags: [LLM-evaluation, prediction-powered-inference, LLM-as-judge, Bradley-Terry, adaptive-sampling, rank-confidence-sets]
novelty: 4
sourced_via: "full-text fetch"
---

# Prediction-Powered LLM Ranking with Adaptively Collected Human Feedback

**Source:** [arXiv stat.ME (Sargent, Sun, Zhang, Liu; UNC Chapel Hill, Purdue, Michigan)](https://arxiv.org/abs/2611.13186) · Published 2026-11 · Added 2026-11-11
**Category:** llm-genai · **Tags:** `LLM-evaluation`, `prediction-powered-inference`, `LLM-as-judge`, `Bradley-Terry`, `adaptive-sampling`, `rank-confidence-sets`

## TL;DR

Leaderboards like Arena collect scarce human preferences adaptively, which breaks the i.i.d. assumptions of prediction-powered inference. PP-Rank combines adaptively collected human votes, unlabeled prompts and LLM-judge predictions with inverse-propensity weighting and a variance-minimising judge weight, giving valid Bradley–Terry score and rank confidence sets that are never asymptotically worse than human-only estimates.

## 1. Business context

Rankings of LLMs from human pairwise preferences drive which models organisations deploy and invest in, but human feedback is slow and expensive, so platforms collect it adaptively — concentrating comparisons on close or new models. Even so, uncertainty stays large: the paper cites an October 2026 snapshot of Arena's math leaderboard in which the top model's rank set spanned 1 to 29 and the top five models' rank sets contained 27 possible ranks on average.

Cheap auxiliary data exists — many unrated responses and LLM judges — but judges can be systematically misaligned with humans (bias), and adaptive pair selection violates the i.i.d. assumptions of standard prediction-powered methods; ignoring unequal comparison probabilities can, under a misspecified preference model, converge to a ranking different from the intended population ranking.

## 2. Technical details

Setup: K models; each round the platform sees a prompt, picks a pair via an adaptive policy and gets human feedback; there is also a large unlabeled prompt pool scored by an LLM judge. PP-Rank is an inverse-propensity-weighted, prediction-powered estimating equation for a Z-functional target such as the Bradley–Terry score vector. A tuning vector λ (one weight per model pair) scales the judge's contribution; the authors characterise the variance-minimising λ* (minimising the asymptotic covariance trace within the class) and a consistent data-driven estimate.

Theory: asymptotic normality under mild conditions on the adaptive policy via a martingale CLT with a joint martingale analysis of adaptive feedback and auxiliary data; simultaneous ranking inference; asymptotic variance never larger than the labeled-only estimator. They derive a rule for reducing exploration that prioritises lower-cost comparisons while matching a conservative variance bound, and show that with a perfect judge validity holds even as random sampling vanishes, whereas with an imperfect judge continued random sampling is necessary for any regular √T-rate estimator.

Experiments: semi-synthetic on UltraFeedback-Extended (~64,000 prompts, responses from 10 LLMs, scores from 10 judges averaged into an ensemble judge); human preferences are simulated with the Skywork-Reward-V2-8B reward model, with ties at ~27.5% to roughly match Arena. Policy: burn-in until the win graph is strongly connected, then ε-greedy (ε = 0.1) over the current top five. T = 10,000 battles, N = 30,000 judge-only prompts, 1,000 trials.

## 3. Impact — potential & realized

Realized (semi-synthetic and synthetic only): only the IPW-based estimators keep near-nominal coverage as sampling becomes more adaptive, and PP-Rank's intervals are narrower than the labeled-only IPW baseline; rank sets keep nominal 90% coverage and are narrower. Correctly certifying the top-1 set: 38% (uniform, labeled-only), 52% (targeted adaptive, labeled-only), 74% (PP-Rank, same policy). With prices from four Chatbot Arena Pareto-frontier models ($40, $3, $0.16, $0.07 per million tokens), the low-cost exploration rule cut evaluation cost by 52.6% with a perfect synthetic judge and 40.7% at the next judge-quality level, falling to near 0% with uninformative judges, while MSE, CI-width and rank-set-width ratios stayed ~0.95–1.00 of the baseline.

Potential: a drop-in inferential layer for any internal model leaderboard or vendor bake-off that mixes human ratings with LLM-judge scores and uses bandit-style allocation.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Solid statistics for a real evaluation problem; the headline gains are on simulated human preferences, not real Arena votes.

This is prediction-powered inference grown up for how evaluation is actually run — adaptively, with judges. The practical lessons travel beyond LLM leaderboards: log your sampling propensities, keep a floor of random exploration unless you trust your judge completely, and report rank confidence sets rather than point ranks. Weaknesses: the 'humans' are a reward model, and the gains depend heavily on judge quality (cost savings collapse from ~53% to ~0% as the judge degrades).

### Similar / related work

- [**Covariance-Calibrated Prediction-Powered Inference**](2026-10-16-arxiv-covariance-calibrated-prediction-powered-inference.md) — in this bank: another refinement of how much to trust model predictions inside PPI
- [**Trustworthy Method Comparison with AI Judges: Estimation and Design under Order, Batch, and Aggregation Effects**](2026-10-07-arxiv-trustworthy-method-comparison-ai-judges.md) — in this bank: design and estimation for comparisons scored by AI judges
- [**Prediction-Powered Inference**](https://arxiv.org/abs/2301.09633) — the original PPI framework (Angelopoulos et al.) this extends to adaptive sampling

### Jargon buster

- **Prediction-powered inference (PPI)** — Uses model predictions on lots of unlabeled data plus a small labeled set to debias and tighten estimates, keeping valid confidence intervals.
- **Bradley–Terry model** — A model where each competitor has a score and the probability i beats j depends on the score difference.
- **Rank confidence set** — A set of ranks that contains a model's true rank with the stated probability.
- **Inverse-propensity weighting (IPW)** — Reweights observations by the inverse of their probability of being sampled, undoing the bias from adaptive selection.
