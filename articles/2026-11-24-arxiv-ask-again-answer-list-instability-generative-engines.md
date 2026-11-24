---
id: arxiv-ask-again-answer-list-instability-generative-engines
title: "Ask Again: Answer-List Instability in Generative Engines"
source: "University of Kaiserslautern–Landau (RPTU) / German Research Center for Artificial Intelligence (DFKI) (arXiv cs.IR)"
url: "https://arxiv.org/abs/2611.30819"
published: "2026-11"
added: "2026-11-24"
category: search-ranking
tags: [generative-engine-optimization, ai-search, answer-stability, rank-biased-overlap, measurement-reliability, repeated-sampling, brand-visibility]
novelty: 3
sourced_via: "full-text fetch"
---

# Ask Again: Answer-List Instability in Generative Engines

**Source:** [University of Kaiserslautern–Landau (RPTU) / German Research Center for Artificial Intelligence (DFKI) (arXiv cs.IR)](https://arxiv.org/abs/2611.30819) · Published 2026-11 · Added 2026-11-24
**Category:** Search & Ranking · **Tags:** `generative-engine-optimization`, `ai-search`, `answer-stability`, `rank-biased-overlap`, `measurement-reliability`, `repeated-sampling`, `brand-visibility`

## TL;DR

Ask a generative engine the same question twice and the answer list can change. The authors sent 200 list-style prompts 50 times each to ChatGPT, Gemini and Perplexity, from Germany and the US, collecting 60,000 responses. Two answers to the same prompt name a different first item 32% of the time. Seven or eight runs, the budgets recommended for brand and source monitoring, find a "clear leader" but find a "close leader" only about half the time. Even 25 runs find a close leader only 60% of the time. Switching engine changes the answer more than rerunning one. The paper argues that visibility reports should give, for each engine, how often an item appears and how often it comes first, each with its own uncertainty.

## 1. Business context

In generative engine optimization (GEO), creators, brands and researchers measure whether an entity appears in an AI answer and in what order. The first product, institution or recommendation is usually more salient than those that follow. The authors note that such a measurement "is meaningful only if run-to-run variation is known." Prior audits documented that variation for cited domains and brand mentions. Some recommend repetition budgets of seven to eight runs (Schulte et al., 2026) or context-dependent dynamic budgets (Sielinski, 2026a). Those budgets concern whether a brand or source appears, not the order of items within one answer. This paper tests whether they suffice for what a user actually sees: which items an answer lists and in what order.

## 2. Technical details

- **Unit of measurement.** A *cell* is one prompt on one engine for one country, run 50 times. Every pair of responses in a cell is compared and averaged. The prompt is the unit of analysis. Stability is defined for the deployed system as a whole: retrieval, generation, routing, experimentation and collection channel.
- **Prompts.** 3,209,860 GEO-Bench and WildChat prompts were filtered down to 225 hand-reviewed candidates. 150 were kept, plus 50 researcher-authored prompts, for 200 in English or German. Five topics (facts, health, science, localized, products) hold 40 prompts each.
- **Collection.** Public web interfaces of ChatGPT, Gemini and Perplexity, without logging in, through the Bright Data platform with location set to DE or US. All responses were collected 11–14 July 2026. 1,200 cells and 60,000 responses; 59,347 (98.9%) outcomes analyzed. Clarification requests (592) and refusals (168) count as no-answer outcomes.
- **List extraction.** gpt-4.1-mini extracted the listed items in order and merged synonyms per prompt, giving 15,927 canonical items. Two annotators checked 180 runs. They found no first-item errors and errors affecting the full ordered list in 1.1% of runs.
- **Three stability measures.** Jaccard overlap (shared items, ignoring order), extrapolated rank-biased overlap (RBO, p = .7, top-weighted) and rank-one agreement (same first item or not).
- **Engine and locale penalty.** The penalty is the mean within-engine similarity minus the cross-engine similarity on the same prompt and country. Zero means two engines are "as interchangeable as two reruns of either one." The locale penalty does the same for DE vs US.
- **Leader recovery.** The *leader* of a cell is the item most often ranked first. Subsamples of n runs test how often they find it. Cells are grouped by the gap between their two most frequent first items: *clear* when ≥ 40 points, *close* when ≤ 10 points.
- **Prompt model.** A hierarchical Bayesian ordered beta regression with one random intercept per prompt. Prompt features (subjectivity, list size, geographic dependence, temporal sensitivity) were coded by four LLM judges and kept only if Fleiss' κ ≥ .67.

## 3. Impact — potential & realized

**Measured:**
- *Within-engine stability.* Mean RBO .69, Jaccard .60, rank-one agreement .68 across all engines. ChatGPT is highest (RBO .73) and Gemini (.68) and Perplexity (.67) differ little. The first item changes at least once in 74% of cells (67% ChatGPT, 81% Perplexity).
- *Items and first item vary separately.* 315 cells name the same first item in every outcome; only 65 return the same list every time. Among pairs whose lists contain the same items, 8.1% name a different first item; this happens in 136 of the 193 prompts with such pairs.
- *Run budgets.* The 90th-percentile RBO error falls from about .38 at two runs to about .06 at 40. Eight runs almost always find a clear leader, and seven in ten cells have one. For close leaders, 8 runs find the leader 51% of the time and 25 runs 60%.
- *Engine vs rerun.* The engine penalty averages .184 RBO and is positive in 94% (1,133 of 1,200) of comparisons. It is largest for pairs involving Perplexity (.198, .208). For the least determinate quarter of prompts it is .230, against .095 for the most determinate. In 14 prompts, one engine almost always puts first an item another engine never lists. For three Karnataka folk sports, ChatGPT and Gemini name Kambala first every time; Perplexity never lists it.
- *Country.* The locale penalty is small on average (.006–.039), but exceeds .10 on at least one engine for 34 prompts, about one in six.
- *What drives stability.* Prompts account for 69.0% of the variance in cell RBO; topic, engine and country together for less than 5%. Coded features explain only about a fifth of prompt differences. Objective prompts score about .2 RBO higher than subjective ones. Researcher-authored prompts are more stable than GEO-Bench and WildChat prompts.
- *Sources and queries.* These explain little. Correlations between domain overlap and answer RBO are .06–.11. Two ChatGPT outcomes with the same query and the same cited domains still reach only RBO .82. Time between runs shows no effect (correlations about ±.01), and exact repeats of an answer are rare (at most 0.062% of pairs).

**Potential:** The authors' recommendations for visibility measurement: report appearance and first-place frequency separately, each with uncertainty. Set the run budget by the gap between the two leading items; where it is small, report how often each comes first rather than name a single leader. Name the engines and report each separately. For GEO experiments, use many prompts, each measured before and after, because one prompt's change "can be ordinary run-to-run variation." Since "being cited is not the same as being listed," measure the list itself. The prompts, responses, extracted lists and analysis code are released.

**Scope (from the paper):** Results hold for anonymous requests to three web interfaces through one collection provider within one week of July 2026. Logged-in, personalized, conversational and API use were not tested, nor change over days or weeks. The study measures agreement, not correctness, and cannot say whether variation comes from retrieval, generation, routing, provider experiments or the collection channel.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A careful measurement study that turns "rank one" into its own estimand

Repeated-sampling audits of AI search already exist, and the metrics (Jaccard, RBO) are standard. The contribution is in the design and the framing. It runs 50 runs per cell within minutes across three engines and two countries. It separates "is it listed" from "is it first." And it shows the required budget depends on the gap between the top two items, which is a classic multinomial mode-estimation problem. For GEO tool vendors and brand teams, the practical message is uncomfortable. A dashboard that says "we rank #1 in ChatGPT" from a handful of runs may be reporting noise when competitors are close. Results also should not be pooled across engines. For data scientists, the finding that prompts carry about 69% of the variance matters most. It means prompt-set sampling, not run count, likely dominates the error of any aggregate visibility score. Before/after GEO tests should be designed as paired, many-prompt experiments.

Caveats: one week, anonymous web sessions, one scraping provider, and LLM-based extraction with a small validation sample. Treat the exact numbers as a snapshot. The recommendations should travel well beyond it.

### Similar / related work

- [**Don't Measure Once: Measuring Visibility in AI Search (GEO)**](https://arxiv.org/abs/2604.07585) — Schulte et al.; source of the seven-to-eight-run budgets this paper tests for first-position targets.
- [**From Stochastic to Stable: Rank Stability and Structural Sufficiency in AI Visibility Measurement**](https://arxiv.org/abs/2607.10341) — Sielinski; argues for context-dependent run budgets, which this paper agrees with.
- [**Statistical Detection of Positional Bias in LLM-Based Recommender Systems: Methodologies and Empirical Evidence**](2026-11-04-arxiv-statistical-detection-positional-bias-llm-recommender.md) (in this bank) — another statistical audit of order effects in LLM product lists.
- [**Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories, and Reads**](2026-10-06-arxiv-agentic-rag-evaluation-budget-allocation.md) (in this bank) — also finds that covering more questions beats re-running the same ones, echoing the prompt-dominates-variance result.

### Jargon buster

- **Generative engine optimization (GEO)** — the AI-search analogue of SEO: trying to make a brand, product or source appear, and appear early, in generated answers.
- **Rank-biased overlap (RBO)** — a similarity score between two ranked lists that weights agreement at the top more than further down; 1 means identical.
- **Rank-one agreement** — whether two answers name the same item first; 1 if yes, 0 if not.
- **Engine penalty** — how much less two different engines agree than two reruns of the same engine; zero means the engines are interchangeable.
- **Clear vs close leader** — a cell's most-often-first item, called clear when it leads the runner-up by at least 40 percentage points and close when by at most 10.
