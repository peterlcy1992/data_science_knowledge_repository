---
id: mit-who-counts-as-exposed-occupational-ai-exposure-index
title: "Who Counts as Exposed? Measurement Choices in an Open, Re-estimable Index of Occupational AI Exposure"
source: "MIT Work Analytics Lab (arXiv cs.IR)"
url: "https://arxiv.org/abs/2611.18168"
published: "2026-11"
added: "2026-11-16"
category: llm-genai
tags: [ai-exposure, measurement-validity, llm-as-annotator, llm-ensembles, rag, calibration, onet, labor-markets, sensitivity-analysis]
novelty: 4
sourced_via: "full-text fetch"
---

# Who Counts as Exposed? Measurement Choices in an Open, Re-estimable Index of Occupational AI Exposure

**Source:** [MIT Work Analytics Lab (arXiv cs.IR)](https://arxiv.org/abs/2611.18168) · Published 2026-11 · Added 2026-11-16
**Category:** llm-genai · **Tags:** `ai-exposure`, `measurement-validity`, `llm-as-annotator`, `llm-ensembles`, `rag`, `calibration`, `onet`, `labor-markets`, `sensitivity-analysis`

## TL;DR

An open, re-estimable task-level AI-exposure index built from seven open-weight reasoning models rating all 18,796 O*NET occupation–task pairs, run in a 2×2 design (with/without retrieved context × with/without calibration to observed Claude usage). The headline is about measurement, not AI: most of the gap from the dominant 2023 benchmark (Eloundou et al.) is how much credit to give exposure that depends on **software integrations not yet built** — "a choice that no data can settle" — and that choice flips whether the index counts more or fewer exposed workers.

## 1. Business context

Exposure indices feed economic analysis, workforce planning and policy, and the 2023 Eloundou et al. labels — zero-shot prompts to a single proprietary model, without retrieved evidence or inspectable reasoning — are still used in 2026 employment analyses, partly because re-running the measurement was never part of the design. Existing measures are either *theoretical capability* (could AI halve task time?) or *observed usage* (what tasks appear on a platform such as Claude or Bing Copilot), and each misleads differently. The authors treat an exposure score as a measurement claim whose validity must be argued, and ask how much "who is exposed" depends on choices inside the measure.

## 2. Technical details

- **Construct.** Present-day task applicability: whether a contemporary AI system could cut task completion time by at least half at equivalent quality. Four classes: E0 none, E1 direct (general-purpose AI), E2 needs additional software/organizational integration, E3 needs visual capability; mapped to β = 0 / δ / 1 with δ = ½ for E2/E3, as in the benchmark.
- **Raters.** Seven open-weight reasoning models (14–32B) from six developers: DeepSeek-R1-Distill-Qwen-32B, Gemma 4 26B-A4B, Ministral 3 14B, Qwen3 30B-A3B, GPT-OSS-20B, Nemotron-3-Nano-Omni 30B-A3B and OpenReasoning-Nemotron 32B, all on a common 2026 rubric written for an agentic system.
- **Context arm.** Time-stamped retrieved news/research passages for the task, six O*NET work-context descriptors, and a protocol that decomposes the task into 2–5 subtasks and labels the time bottleneck.
- **Calibration arm.** Simplex-constrained ensemble weights fitted to observed Claude usage (penetration). Weights: Qwen3 0.511, OpenReasoning-Nemotron 0.164, Gemma 4 0.160, Ministral 0.084, DeepSeek-R1-Distill 0.081; GPT-OSS-20B and Nemotron-3-Nano-Omni get zero — "mostly a Qwen3 index".
- **Aggregation & evaluation.** Task scores aggregated to occupations with survey-based task time shares; a common held-out fold of 3,391 tasks (257 with positive usage). Validation against observed usage, Anthropic's occupation-level measure, and an independent physical-task classification (to address the worry that the measure was shaped to look like Claude usage). All outputs are stored, so every headline number is recomputed under alternatives without new inference; a scheduled incremental pipeline supports vintage-to-vintage comparison.

## 3. Impact — potential & realized

**Measured:**
- On direct exposure (E1), six of seven grounded models exceed the benchmark's 13.5%; the benchmark assigns E2/E3 to 41.4% of tasks versus 12–24% for the grounded models — the measure is "much more reluctant… to count a hypothetical future integration as present exposure."
- Ranking: every ensemble arm beats the benchmark in AUC for ranking used-vs-unused tasks by +0.025 to +0.055 (significant for all arms but one, p=0.055), with part of the all-task advantage due to finer score resolution. Context mainly shifts the **level** of exposure rather than improving ranking.
- Headcount (BLS employment, occupations above 0.5): calibrated index 30.1M workers (23.0%) vs 36.2M (27.7%) for the benchmark; calibrated no-context arm 49.9M (38.2%); uncalibrated, context lowers the count from 69.0M (52.8%) to 39.0M (29.9%). When only direct exposure counts (δ=0), the index counts *more* exposed workers than the benchmark.
- Distribution: across 923 occupations mean exposure falls 0.345 → 0.297 (A1) → 0.245 (A2) while staying strongly related to the benchmark (Spearman 0.911). The top-/bottom-wage-quintile exposure ratio rises from 2.8 to 4.9; bottom-quintile workers above 0.5 fall from 4.7% to 0.5%. Calibration (anchoring to one platform's users) does more of this relocation toward higher-wage work than context, so the uncalibrated arm is also released.

**Potential:** a template for LLM-as-measurement-instrument work in any analytics team: multi-model raters, inspectable evidence, explicit normative parameters with reported sensitivity, and stored outputs for re-estimation. The authors recommend that indices used as policy inputs state such choices, report numbers under alternatives, and be re-estimated as systems change.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — The best "LLM labels are measurements" case study in a while

What earns the 4 is not the index but the discipline: a 2×2 design that isolates what context and calibration each change, a single normative knob (δ) shown to drive the headline, and an external validation that doesn't depend on the calibration source. Data scientists who use LLMs to label support tickets, intents or product taxonomy should steal the pattern wholesale — especially "calibration to one platform's behaviour quietly relocates the construct." Caveat: the evaluation leans on Claude usage as ground truth for ranking, which the paper itself calls a lower bound for applicability.

### Similar / related work

- [**GPTs are GPTs: Labor market impact potential of LLMs**](https://arxiv.org/abs/2303.10130) (Eloundou et al.) — the E0–E3 benchmark this index re-estimates.
- [**Partial pooling beats synthetic respondents as estimators, not as covariates**](2026-11-13-arxiv-partial-pooling-vs-synthetic-respondents-small-area.md) (in this bank) — another careful test of where LLM-generated measurements help and where they mislead.
- Measurement-validity literature (Jacobs & Wallach 2021) — the framing the authors adopt for treating scores as constructs.

### Jargon buster

- **O*NET** — the US Department of Labor's database linking occupations to the tasks workers perform.
- **E2/E3 (integration-dependent exposure)** — tasks AI could speed up only with software, integrations or visual capability not available out of the box.
- **Simplex-constrained calibration** — fitting non-negative ensemble weights that sum to one, so each rater's influence is readable.
- **AUC (here)** — the probability a randomly chosen used task gets a higher exposure score than a randomly chosen unused one.
