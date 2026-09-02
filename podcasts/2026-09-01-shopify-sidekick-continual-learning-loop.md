# Episode 2 — Shopify: An AI Agent That Trains Itself

- **Show:** [Data Science in the Wild](SHOW.md)
- **Company:** Shopify
- **Audio:** [`2026-09-01-shopify-sidekick-continual-learning-loop.m4a`](2026-09-01-shopify-sidekick-continual-learning-loop.m4a)
- **Cover:** [`2026-09-01-shopify-sidekick-continual-learning-loop.cover.png`](2026-09-01-shopify-sidekick-continual-learning-loop.cover.png)
- **Source article:** [`../articles/2026-09-01-shopify-sidekick-continual-learning-loop.md`](../articles/2026-09-01-shopify-sidekick-continual-learning-loop.md)

## Title

**Shopify — An AI Agent That Trains Itself (Sidekick's Continual Learning Loop)**

## Description

A deep dive into how Shopify rebuilt the improvement loop for **Sidekick**, its
AI agent, as a four-stage flywheel that keeps getting better without perpetually
scaling frontier-model spend. We cover the business context (quality that gets
expensive fast when you only buy it by upgrading models), and the technique: a
**human-calibrated quality rubric** (validated with Cohen's kappa), an
**LLM-as-judge** tuned with DSPy/GEPA/ACE and — crucially — validated against
real **production A/B outcomes** before it's trusted, automated prompt/tool
research, and **continual learning** via SFT plus **GRPO** fine-tuning that uses
the calibrated judge itself as the reward signal. The payoff: serving cost for a
GraphQL agent handling **2,000 requests/min** fell roughly **96%, from ~$27M to
~$1M/year**. The real lesson is the discipline of calibrating the judge *before*
using it as a reward.

Source article: "Sidekick's Continual Learning Loop" — Shopify Engineering,
<https://shopify.engineering/sidekicks-continual-learning-loop> (published
2026-08).
