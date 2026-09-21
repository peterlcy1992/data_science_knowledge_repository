---
id: baidu-gese-headline-generation-recommendation
title: "Generate to Explore, Select to Exploit: Aligning LLM-based Headline Generation with Personalized Recommendation"
source: "arXiv (Baidu Inc.)"
url: "https://arxiv.org/abs/2609.15094"
published: "2026-09"
added: "2026-09-21"
category: llm-genai
tags: [headline-generation, reinforcement-learning, gspo, personalization, mode-collapse, industrial-recsys]
novelty: 4
sourced_via: "web search"
---

# Generate to Explore, Select to Exploit: Aligning LLM-based Headline Generation with Personalized Recommendation

**Source:** [arXiv (Baidu Inc.)](https://arxiv.org/abs/2609.15094) · Published 2026-09 · Added 2026-09-21
**Category:** LLMs & Generative AI · **Tags:** `headline-generation`, `reinforcement-learning`, `gspo`, `personalization`, `mode-collapse`, `industrial-recsys`

## TL;DR

Baidu researchers show that naively fine-tuning an LLM to write the single "best" headline for a recommended item collapses onto generic, average-taste phrasing that underserves niche interests. Their fix, GESE, splits the job in two: an RL-trained LLM generates a diverse *set* of candidate headlines (explore), and a lightweight real-time selector picks the best one per user from that set (exploit) — deployed on a platform with 100M+ daily active users, lifting CTR by 2.57% and dwell time by 0.87%.

## 1. Business context

In industrial recommendation feeds, the headline or caption shown alongside a recommended item is itself a lever on engagement — the same item can be pitched differently to different users depending on what's likely to catch their attention. LLMs are a natural fit for generating those headlines, but training one to output a single optimal headline per item runs into **mode collapse**: the model converges toward generic phrasing that scores well *on average* across users, while systematically underserving users with more specific or long-tail interests who would have responded better to a differently angled headline. The business cost is a ceiling on how personalized presentation-layer content can get — a single static best guess per item, rather than headlines tailored to the specific user seeing them.

## 2. Technical details

GESE (Generate to Explore, Select to Exploit) decouples the problem into two stages operating at the presentation layer, on top of whatever ranking model already selected the item to show:

1. **Generative exploration.** The LLM is treated as a probabilistic explorer rather than a single-answer generator. It's trained with **Group Sequence Policy Optimization (GSPO)** and a hierarchical reward mechanism to produce a *set* of candidate headlines for an item that collectively maximizes semantic coverage of the different ways users might be interested in it — rather than converging on one generic phrasing.
2. **Selective exploitation.** A separate, lightweight, real-time selector then picks the single best headline from that candidate set for the specific user and context, using contextual signals at serving time. Because the heavy generative step can run offline/ahead of time per item, the online path only needs a cheap selection model, keeping serving latency low.

The framing explicitly borrows the explore/exploit vocabulary from bandit-style decision-making: generation's job is to keep options diverse enough to cover the space of user intents (explore), and selection's job is to pick the highest-value option for a given user without needing to regenerate anything online (exploit).

## 3. Impact — potential & realized

**Realized:** deployed on an industrial recommendation feed with 100+ million daily active users, GESE delivered a **2.57% lift in click-through rate** and a **0.87% improvement in dwell time** versus baselines, and the paper reports it outperforming prior state-of-the-art headline-generation approaches on the same deployment.

**Potential:** the generate-then-select decoupling is a general pattern, not specific to headlines — any presentation-layer personalization task where a single "best" LLM output would flatten diversity (thumbnails, notification copy, summary blurbs) could apply the same explore/exploit split: generate a diverse candidate pool offline with RL-trained diversity objectives, then run a cheap, fast selector online.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a genuinely useful reframing of a common LLM-personalization failure mode

Mode collapse in LLM generation isn't new, and neither is generate-then-rerank as a general pattern. What's novel here is applying that structure specifically to fix personalization diversity at the presentation layer, with a concrete RL recipe (GSPO plus a hierarchical, coverage-oriented reward) purpose-built to keep the generation stage diverse rather than accurate-on-average — and validating it with a real production A/B result rather than only offline diversity metrics. It's a clean, transferable idea that other teams doing LLM-generated user-facing copy will likely want to copy.

### Similar / related work

- General explore/exploit and bandit literature — the conceptual foundation GESE borrows its framing from; left unlinked as a broad body of work rather than one paper.
- LLM-as-judge and consensus-sampling approaches to content evaluation, such as [**Evaluating Netflix Show Synopses with LLM-as-a-Judge**](2026-09-14-netflix-llm-judge-show-synopses.md) (in this bank) — a related but distinct problem (evaluating generated text quality) rather than generating diverse candidates for personalized selection.
- Generative retrieval / semantic-ID recommendation work, e.g. [**Autoregressive Ranking: Bridging the Gap Between Dual and Cross Encoders**](2026-09-20-deepmind-autoregressive-ranking-arr.md) (in this bank) — a different point in the recommendation pipeline (ranking rather than presentation) but part of the same broader shift toward LLM-native recommendation systems.

### Jargon buster

- **Mode collapse** — when a generative model, trained to optimize an average-case objective, converges toward a narrow set of generic outputs instead of preserving the diversity needed to serve different users or contexts well.
- **Group Sequence Policy Optimization (GSPO)** — a reinforcement-learning method for training sequence generators (like LLMs) using reward signals computed over groups of generated sequences, used here to steer the model toward diverse, high-coverage candidate sets rather than a single best answer.
- **Explore/exploit** — a framing from decision theory: "explore" means gathering a range of options to learn what might work, "exploit" means committing to the option expected to perform best given what's already known; GESE splits generation (explore) from selection (exploit) into two separate stages.
- **Dwell time** — how long a user engages with a piece of content after clicking through, used alongside CTR as a proxy for whether the content actually satisfied their interest rather than just attracting an idle click.
