---
id: arxiv-execjudges-program-judges-relevance-labeling
title: "Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling"
source: "Emory / Waterloo / Stanford (arXiv cs.IR)"
url: "https://arxiv.org/abs/2611.24849"
published: "2026-11"
added: "2026-11-19"
category: search-ranking
tags: [llm-as-judge, relevance-judgments, program-synthesis, trec, krippendorff-alpha, evaluation-cost, reproducibility, offline-evaluation]
novelty: 4
sourced_via: "full-text fetch"
---

# Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling

**Source:** [Emory / Waterloo / Stanford (arXiv cs.IR)](https://arxiv.org/abs/2611.24849) · Published 2026-11 · Added 2026-11-19
**Category:** Search & Ranking · **Tags:** `llm-as-judge`, `relevance-judgments`, `program-synthesis`, `trec`, `krippendorff-alpha`, `evaluation-cost`, `reproducibility`, `offline-evaluation`

## TL;DR

ExecJudges has a frontier LLM (Claude Opus 5.5) write a few short, inspectable Python programs per topic from the assessment guidelines, then labels whole document pools with no further model calls. Without labels it matches NIST agreement at the level of Claude Sonnet 5.5 judges on TREC DL 2019–2021. With 16 human labels per topic it beats per-topic classifiers on all seven collections. Writing the programs costs $0.17–$0.49 per topic.

## 1. Business context

LLM relevance judges now produce much of the evaluation data for search and RAG systems. Each judgment is a frontier-model call, so cost grows with pool depth and with every new run. The decision is opaque even when the judge explains itself, and documents can carry content that sways the judge. Relevance assessment applies the same topic-specific criteria to many documents. The authors (Agichtein, Clarke, Dhole, Stern) ask whether an LLM can write those criteria down once, as a readable program, instead of re-deriving them per document. The idea builds on executable-rubric work (Dhole et al., 2026).

## 2. Technical details

- **Program writer.** Claude Opus 5.5, called once per topic. It sees the topic as assessors saw it, the official grading guidelines, a grade-distribution statement, five unlabeled pool passages showing the input format, and a tool-use policy.
- **Program shape.** Each program defines `assess(query, pool)` and answers the guideline's questions per document. On TREC DL's 0–3 scale these are *on_subject, some_answer, exact_answer, dedicated*; on Robust04 and TREC-COVID's 0–2 scales they are *relevant, key*. A **fixed formula outside the generated code** maps answers to grades, so the writer decides only what counts as evidence. Allowed operations: the Python standard library plus a small toolkit (Snowball-stemmed tokenization, BM25 scores and percentiles within the topic pool, windowed phrase matching, sentence splitting, number/date/unit parsing, and "supported-terms" and "unrelated-share" helpers). Programs run in a sandbox with no network and no model calls, and get one repair attempt on failure.
- **Consensus.** k = 3 independently written programs per topic; the label is the **mean grade rounded down**. Averaging reduces single-program errors and over-grading, and more programs added little.
- **ExecJudges-L.** Adds a few human-labeled passages (4–16 per topic) to the writer prompt and asks for general rules that reproduce their grades without referring to their wording. Labels are chosen by stratified sampling by NIST grade, or by BM25 top-k as a practical alternative.
- **Protocol.** Seven TREC collections: DL 2019/2020 for development, DL 2021 as pilot, and DL 2022, DL 2023, Robust04 and TREC-COVID held out as test sets. Baselines: pointwise (UMBRELA prompt) and listwise Claude Sonnet 5.5 and Haiku 5.5 judges, per-topic classifiers (Gienapp et al., 2026), and One-shot DuoT5-3B labeling. Agreement is Krippendorff's α against NIST, and system-ranking agreement is Kendall's τ.

## 3. Impact — potential & realized

**Measured:**
- **No labels.** Agreement with NIST is within the confidence intervals of the pointwise and listwise Sonnet judges on DL 2019–2021, and within 0.054 of the listwise judge on DL 2019–2022. It is significantly below the judge on DL 2022 (in a paired test on the documents the judge labeled), and below it on DL 2023, Robust04 and TREC-COVID.
- **16 labels.** ExecJudges-L agrees with NIST more than the per-topic classifier and One-shot on **all seven collections**. It beats the classifier on 69–89% of topics in each test collection. Against the listwise Sonnet judge given the same labels it is **+0.037 to +0.130** on DL 2019–2022 and about 0.05 below on Robust04 and TREC-COVID. Label-fitted methods over-predict relevance when relevant documents are rare: only 3.5% of Robust04 evaluation documents are relevant.
- **System rankings.** Kendall's τ against the NIST-label ranking of official DL runs is **0.87–0.91** without labels and **0.93–0.94** with 16 labels.
- **Cost.** Writing the programs costs **$0.17–$0.49 per topic**, after which grading needs no API calls or GPU. The programs become cheaper than the listwise judge beyond about 200–350 documents per topic. The median program is about 70 lines, mostly topic-specific regular expressions and term lists.
- **Negative results (the paper's).** With an open-weight writer (GPT-OSS-120B), α is at most 0.486 and significantly lower; its programs grade too low. Four attempts to correct programs from labeled errors did not raise agreement on new passages.

**Potential:** deterministic, re-runnable labels for deep pools and frequent re-evaluation, plus cheap rewards for training generators. The authors list robustness to keyword stuffing as future work.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — Compiles the judge once instead of calling it per document

For a data scientist this is a measurement-instrument story. A program judge is a fixed, auditable instrument: the same labels on every run, a diffable definition of relevance per topic, and costs that don't grow with pool depth. That fixes reproducibility problems LLM judges carry into offline A/B readouts. The design choice that matters most is keeping the grading formula outside the generated code, which limits what the LLM can get wrong.

The limits are real. The method is lexical, so paraphrase-heavy relevance and adversarial keyword stuffing are open risks (the authors flag the latter). Without labels it trails the LLM judge on harder document collections. It also depends on a frontier writer. I'd use it as a cheap first-pass labeller and drift detector, with a small human-label budget per topic where the 16-label variant shines.

### Similar / related work

- [**From Relevance to Utility: Rubric Alignment in Yuanbao Search**](2026-11-18-tencent-yuanbao-rubric-aligned-search.md) (in this bank) — query-specific rubrics as the supervision target, applied in production.
- [**The Impact of Backbone Evolution on LLM-Based Relevance Assessments**](2026-10-09-arxiv-backbone-evolution-llm-relevance-assessments.md) (in this bank) — why LLM-judge labels drift across model versions, the reproducibility problem a frozen program avoids.
- [**LLM-based Relevance Assessment for Web-Scale Search Evaluation at Pinterest**](2026-10-08-pinterest-llm-relevance-assessment-search-evaluation.md) (in this bank) — the per-document LLM-judge approach this replaces with programs.
- [**UMBRELA (Upadhyay et al., 2025)**](https://arxiv.org/abs/2406.06519) — the open-source pointwise LLM-judge prompt used as the pointwise baseline.

### Jargon buster

- **Relevance judgment (qrel)** — a graded label saying how well a document answers a query, used to score retrieval systems.
- **Krippendorff's α** — an agreement statistic that corrects for chance and handles ordinal grades; 1 is perfect agreement.
- **Kendall's τ** — a rank correlation; here, how closely two label sets order the same retrieval systems.
- **Document pool** — the union of top results from many systems for a topic; the set that gets judged.
- **BM25** — a classic lexical relevance score based on term frequency and document length.
