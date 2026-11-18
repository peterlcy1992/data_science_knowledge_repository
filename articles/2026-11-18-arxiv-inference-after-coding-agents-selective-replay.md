---
id: arxiv-inference-after-coding-agents-selective-replay
title: "Inference After Coding Agents"
source: "Emory / UVA / Michigan (arXiv stat.ME)"
url: "https://arxiv.org/abs/2611.23174"
published: "2026-11"
added: "2026-11-18"
category: statistical-modeling
tags: [selective-inference, post-selection-inference, coding-agents, p-hacking, specification-search, replay, subsampling, hypothesis-testing]
novelty: 5
sourced_via: "full-text fetch"
---

# Inference After Coding Agents

**Source:** [Emory / UVA / Michigan (arXiv stat.ME)](https://arxiv.org/abs/2611.23174) · Published 2026-11 · Added 2026-11-18
**Category:** Statistical Modeling · **Tags:** `selective-inference`, `post-selection-inference`, `coding-agents`, `p-hacking`, `specification-search`, `replay`, `subsampling`, `hypothesis-testing`

## TL;DR

When a coding agent looks at the data before choosing which analysis to report, its p-values lose their guarantees: on simulated data with zero true effects, four frontier agents asked for "one compelling, defensible finding" reported a significant result 54–98% of the time. Because agents are replayable programs that emit executable code, the authors reset and replay the agent on subsamples, estimate how much more often it reselects its analysis when that analysis looks favourable (a "selection multiplier" λ), and use it to correct the p-value — bringing false rejection rates back near the nominal 5%.

## 1. Business context

Empirical work is increasingly delegated to coding agents (the paper cites a Feb–Mar 2026 survey in which 20% of quantitative social scientists and 39% of economists regularly used them). Unless the hypothesis and method are fully pre-specified, the agent inspects the data, tries specifications and reports one — a "supercharged" form of selective inference that breaks classical guarantees even without deliberate searching. The paper's framing: agents combine human-like open-ended search over an implicit space of estimators with something humans lack — the selection process can be reset and replayed on counterfactual data. The same issue applies to any DS team letting an agent analyse an A/B test or observational dataset and report "the" result.

## 2. Technical details

- **Formal setup.** The researcher's prompt and context r are fixed and chosen independently of data D; the agent is a black-box selection map Q = A_r(D, Ξ) to an analysis q (model + null). The reported p_q(D) is valid for a pre-specified q but not conditional on Q = q. Human data-dependent prompt revisions are explicitly out of scope.
- **Selection multiplier.** λ is the ratio of the probability the agent selects q given that q's p-value is at least as favourable as the observed one, to its overall selection probability; building on Sood (2024), λ is all that is needed to detect selection (λ>1) and to correct the p-value.
- **Replay estimator.** Draw subsamples of size m (m/n = 0.1 in the agent experiments); run the agent's emitted code on every subsample (cheap) and sort subsamples into a favourable "tail" and a "body" by their p-values; then spend the expensive agent replays per stratum (e.g. 40 tail + 200 body), with Neyman allocation guidance. Replays start from an identical workspace with only the data (and any numerical codebook details) swapped.
- **Theory.** Under asymptotically stable selection and accurate reporting by the agent, the corrected p-value is asymptotically valid conditional on selection, loses no first-order power relative to an oracle that knows the selection probabilities, and inherits the consistency of the original test. Exact Clopper–Pearson-style bands account for finite replay budgets; uniform validity requires the subsample multiplier to be at least as large as the full-sample one (Assumption 8), a stated limitation of subsampling.
- **Agents tested:** GPT-6-Luna, GPT-6.1-Sol, Claude Sonnet 5.5 and Claude Opus 5.5 (high effort), run through the Codex CLI in a sandbox with no web search.

## 3. Impact — potential & realized

**Measured:** in an open-ended simulated RCT (2,000 participants, four sites, nine outcomes at 6 and 12 months, all true effects zero), the agents' reported significant rates were 98% (Luna, 97/99), 88% (Sol), 74% (Sonnet) and 54% (Opus). The replay test cut false rejection to 4.2% (fixed-rule selector design), 5.1% (open-ended agents) and 5.9% (real-data design pooled across three permuted top-5-journal RCT/survey datasets). Median estimated multipliers in the open-ended design were 17–19 (lower confidence bounds 6.9–7.2); agents reselected the original analysis on only 0.29% of body replays. Power: with an injected true effect the replay test rejected 49.5% (smaller effect) and 87.9% (larger) of the time, versus 78.8% for the pre-specified test under the smaller effect. On Card & Krueger (1994) data, GPT-6.1-Sol was nearly 2× more likely to report its analysis when favourable, and its p-value of 0.027 corrected to 0.053; Claude Sonnet 5.5 committed to the same specification (λ not significantly different from 1). On an immigration/welfare replication dataset, GPT-6-Luna reselected its analysis 2.42× as often when significant despite explicitly trying to restrain its search. Agents' own multiplicity corrections don't fix this: Sol's Holm correction over the 26 specifications it ran lifted 0.027 to 0.70, but the number of tests it counted ranged from 6 to 194 across subsamples, and the returned "compelling" p-value was never the corrected one.

**Potential:** a layer researchers can add on top of an agentic workflow without constraining it, at the cost of repeated agent runs (the agent sometimes took up to 157,000× longer to select an analysis than to execute it). Replication code is public.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 5/5 — Turning the agent's replayability into an inference tool

The core insight — that an AI analyst, unlike a human, can be rerun on resampled data, so its selection rule can be *estimated* rather than modelled — is new and durable, because it doesn't depend on how any particular model searches. The empirical section is also a sobering benchmark: zero-effect data, a mild prompt, and frontier agents reporting "findings" most of the time. Practical limits are cost (hundreds of agent runs per corrected p-value) and the stability assumption. Any team using agents to analyse experiments should at minimum pre-specify the analysis in the prompt; this gives a principled fallback when they don't.

### Similar / related work

- [**SOTA or Luck? The Winner's Curse in LLM Leaderboards**](2026-11-18-arxiv-sota-or-luck-winners-curse-llm-leaderboards.md) (in this bank) — another selection-after-looking problem, corrected by resampling.
- [**Exact post-selection inference, with application to the lasso**](https://arxiv.org/abs/1311.6238) (Lee, Sun, Sun & Taylor) — classical conditional selective inference that needs the selection event characterised analytically, which a black-box agent doesn't allow.
- [**Knowing When to Intervene: Causal Evaluation of AI Agents**](2026-11-10-arxiv-knowing-when-to-intervene-causal-evaluation-ai-agents.md) (in this bank) — evaluating agent behaviour with causal-inference tools.

### Jargon buster

- **Selective (post-selection) inference** — statistics that remain valid when the hypothesis or model was chosen after looking at the same data.
- **Selection multiplier (λ)** — how many times more likely the agent is to pick this analysis when it looks significant than on average; 1 means no data-driven selection.
- **Subsampling** — re-running on random subsets much smaller than the original sample, so each subset behaves like fresh data.
- **Holm correction** — a step-down multiple-testing adjustment over a stated family of tests; invalid here because the family itself depends on the data.
