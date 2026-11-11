---
id: meta-feature-invariant-scaling-laws-ab-experimentation-recsys
title: "Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems"
source: "arXiv cs.IR (Meta: Zhiliang Chen, Sammy Nammari, Jiahao Su, Xiaoqiang Luo)"
url: "https://arxiv.org/abs/2611.13539"
published: "2026-11"
added: "2026-11-11"
category: personalization-recsys
tags: [scaling-laws, offline-experimentation, bayesian-decision-rule, small-scale-proxies, HSTU, Wukong]
novelty: 4
sourced_via: "full-text fetch"
---

# Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems

**Source:** [arXiv cs.IR (Meta: Zhiliang Chen, Sammy Nammari, Jiahao Su, Xiaoqiang Luo)](https://arxiv.org/abs/2611.13539) · Published 2026-11 · Added 2026-11-11
**Category:** personalization-recsys · **Tags:** `scaling-laws`, `offline-experimentation`, `bayesian-decision-rule`, `small-scale-proxies`, `HSTU`, `Wukong`

## TL;DR

Small-scale trial runs of a recommender-model change often point the wrong way. The authors show that a model with a feature change still follows a power-law scaling curve of the same functional form (with different coefficients), so a handful of small runs can be extrapolated, with intervals, to a posterior probability that the change wins at full scale. Validated on Wukong, HSTU and an LLM-based recommender across 40+ changes.

## 1. Business context

Recommender teams improve models through what the paper calls A/B experimentation on model changes: add an architecture, optimizer or data-feature change to the baseline, retrain at full scale on full data, and compare. That full retrain is costly and must be repeated for every candidate change, which the authors say can number in the hundreds in an industrial setting; sometimes the full-size model will not even fit on the GPUs available for experimentation.

The common workaround is a single small-scale run (small model, data subset), but the paper argues this is often misleading. Its motivating case: adding movie genre information to an LLM-based recommender's training prompt lowers HR@10 at small training scale but significantly improves it at full scale on MovieLens-20M, so the small run would have rejected a useful change. The authors add that you cannot pick a 'safe' small scale in advance, because different categories of changes give different signals across small scales.

## 2. Technical details

Key empirical claim — feature-invariant scaling: validation loss follows a power law Loss = a·N^b·D^c (N model size, D training data size) for both baseline and changed models, with the same functional form but different fitted coefficients; in the motivating case both fits have R² > 0.99. The authors say they believe this is the first demonstration that a modified recommender keeps the scaling form.

Method: run a sweep of small co-scaled experiments (they use scale s = N·D, varying layers, width and embedding-table size fairly uniformly), fit the log-linear scaling regression, and compute the closed-form predictive distribution of full-scale log-loss; the paper notes Bayesian (flat prior) and frequentist prediction intervals coincide here. The decision quantity is Pr(L_feature(S) < (1−δ)·L_baseline | data). Their rule: call a change beneficial if the probability of beating the baseline by δ = 1% exceeds 90% (0.05% margin for Wukong and the LLM model, whose effects are sub-1%). For non-power-law forms they describe an MCMC variant (appendix).

Cost: with data and model co-scaled, a half-scale run costs about a quarter of a full run, so a sweep at s ∈ {0.1,…,0.5} costs about 55% of one full-scale run. Models: Wukong, HSTU, and GR2 (an LLM-based recommender) fine-tuned from Qwen3-Instruct and Llama-3.1-Instruct checkpoints (data scale only for the LLMs).

## 3. Impact — potential & realized

Realized (as reported, offline): across more than 40 architectural, optimization and data changes, posterior probability of improvement rises toward 100% for changes that truly help and toward zero for regressions as more small-scale points are added, and out-of-sample full-scale prediction error shrinks with more points. Changes flagged as beneficial improved HSTU-Large on MovieLens-20M from HR@10 0.3567 to as high as 0.3603 (+1.01%), HR@50 0.6139→0.6186, HR@200 0.8073→0.8112. They also note occasional failures of the power-law fit (e.g. Qwen-0.5B after adding genre information).

Potential: a cheap, uncertainty-aware screen for which model changes deserve a full retrain and, downstream, an online A/B test. The paper cites prior work that a 0.1% loss reduction can mean more than 0.5% topline lift at billion-user scale, which is the economic case for not wrongly rejecting small wins. Note the 'A/B experiment' here is offline model comparison on validation loss, not a randomized online test.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A genuinely useful bridge between scaling-law curve fitting and experiment decision rules; the evidence is offline and on public benchmarks.

The DS-relevant move is reframing 'is this model change good?' as a predictive-inference problem with an explicit decision threshold and a posterior probability, rather than eyeballing one small run. It is the offline-model analogue of surrogate-based early readouts in online experimentation. Caveats: the intervals are conditional on the power-law form holding (they show it sometimes doesn't), validation loss is still a proxy for the online metric, and the 55%-of-a-full-run cost means this is a screen for promising changes, not a free lunch. Expect large ranking teams with established scaling sweeps to adopt it quickly.

### Similar / related work

- [**From User Sequences to Scaling Laws: A Multi-Stage Architecture for Meta's Ads Ranking**](2026-08-31-meta-llatte-ads-ranking-scaling-laws.md) — in this bank: Meta's ads-ranking scaling-law work, the descriptive side this paper turns into a decision tool
- [**The surrogate index: combining short-term proxies to estimate long-term treatment effects**](https://arxiv.org/abs/1603.09326) — cited by the authors; the online-experimentation analogue of predicting a long-run effect from cheap early signals
- [**Actions Speak Louder than Words (HSTU)**](https://arxiv.org/abs/2402.17152) — the generative recommender used as one of the three test families

### Jargon buster

- **Scaling law** — An empirical formula (here a power law) that predicts loss from model size and data size.
- **Feature-invariant scaling** — The paper's term for a model change preserving the scaling law's functional form while shifting its coefficients.
- **HR@10** — Hit rate at 10: the share of test cases where the held-out item appears in the top-10 recommendations.
- **Posterior probability of improvement** — The probability, given the small-scale results, that the changed model beats the baseline by the chosen margin at full scale.
