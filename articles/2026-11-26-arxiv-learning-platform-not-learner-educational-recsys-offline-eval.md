---
id: arxiv-learning-platform-not-learner-educational-recsys-offline-eval
title: "Learning the Platform, Not the Learner: Sequencing Shortcuts in the Offline Evaluation of Educational Recommender Systems and LLM Rankers"
source: "ENSAD / Hassan II University of Casablanca (arXiv cs.IR)"
url: "https://arxiv.org/abs/2611.33240"
published: "2026-11"
added: "2026-11-26"
category: personalization-recsys
tags: [offline-evaluation, educational-recommenders, shortcut-learning, sequential-recommendation, structural-baselines, llm-rankers, negative-sampling, inverse-propensity-weighting, exposure-bias]
novelty: 4
sourced_via: "full-text fetch"
---

# Learning the Platform, Not the Learner: Sequencing Shortcuts in the Offline Evaluation of Educational Recommender Systems and LLM Rankers

**Source:** [ENSAD / Hassan II University of Casablanca (arXiv cs.IR)](https://arxiv.org/abs/2611.33240) · Published 2026-11 · Added 2026-11-26
**Category:** Personalization & Recommender Systems · **Tags:** `offline-evaluation`, `educational-recommenders`, `shortcut-learning`, `sequential-recommendation`, `structural-baselines`, `llm-rankers`, `negative-sampling`, `inverse-propensity-weighting`, `exposure-bias`

## TL;DR

In educational logs the next activity is mostly chosen by the platform, teacher or syllabus, not the learner. So a next-activity recommender can score well offline by imitating that sequencing policy. Youssef Jdidou audits eight public datasets from five platforms. Predictors that know only the learner's last activity reach 0.81–1.00 of the best accuracy of any method (median 0.95), mostly through population transitions. Small open LLM rankers look strong only with random negatives, where a word-matching baseline does as well. Weighting test steps by how unlikely the structure makes them reveals a personalisation signal on seven of eight datasets.

## 1. Business context

Learning apps, tutoring systems and MOOCs develop and compare recommenders offline. A model sees a learner's history and is rewarded when it ranks the logged next activity high. But in education that next activity is "seldom a free choice of the learner". Teachers assign problem sets, tutors draw problems until mastery, engines pick questions. The log is the output of a sequencing policy π.

The paper frames offline next-activity evaluation as measuring agreement with π, not whether recommendations help learners. This is a shortcut in the sense of Geirhos et al. Han et al. (2026) found a similar shortcut in general sequential-recommendation benchmarks. Here, the author argues, the shortcut "is the design of the platform". The datasets were also mostly collected for knowledge tracing, where sequencing did not matter.

The stakes: a team could select a model that learns the platform, and rank a pedagogically motivated policy last. The paper also targets LLM rankers, which are evaluated on small candidate sets where the choice of negatives decides the result.

## 2. Technical details

- **Three summary quantities.** S_struct = the best metric of any structural predictor. Δ(f) = M(f) − S_struct, the lift over structure. ρ = S_struct / best metric of any method, the structural share. The author notes Δ itself still measures agreement with π, not pedagogical value.
- **Structural predictors (no learner info beyond the last activity).** POP (popularity). ORDER (median relative course position). CONT (unseen activities of the last activity's container first). MC (first-order Markov transition counts with popularity back-off). MC counts as structural because all learners with the same last activity get the same ranking.
- **Ten personalised recommenders.** ItemKNN, RP3beta, EASE, iALS, SKNN, peer-based MCLD and aMCLD (the author's own earlier methods), knowledge-tracing policies ZPD and DKT, and SASRec with outcome-aware tokens and cross-entropy loss. All are tuned on validation NDCG@10.
- **Datasets (8, from 5 platforms).** ASSISTments A09, A12, A15, A17; EdNet (Santa TOEIC app, 4,387 learners, 8,472 question bundles); Junyi Academy (20,000-learner sample); Eedi (NeurIPS 2020 quizzes); ACT-MOOC (7,047 learners, 97 activities). OLI Engineering Statics was dropped, since 74% of its transitions go to the next item id.
- **Task.** Rank all activities the learner has not done; the target is the next new activity. Repeats are removed for every method.
- **Protocols.** P1 is leave-last-out, the protocol under audit. P2 is a global temporal split at the 80th percentile of step times.
- **Metrics.** HR@K and NDCG@10 over the full ranking, computed as exact expectations over random tie orders. Uncertainty uses 2,000-resample bootstrap intervals and a paired bootstrap with Holm correction.
- **Step splits.** Novel (transition never seen in training) vs. seen. On-path (same container) vs. off-path. On EdNet and Junyi, steps are also split by who started the activity.
- **LLM rankers.** Qwen2.5-Instruct 0.5B and 1.5B (bfloat16) and 3B and 7B (4-bit, llama.cpp), all on CPUs. Candidate sets have 20 items: the target plus 19 random or *structural* negatives drawn from MC's and CONT's top 20. Scoring is a PMI-style likelihood of each candidate name given the history, minus the same name with no history. A multiple-choice letter format was abandoned: the 0.5B model picked the same letter in 84% of Eedi cases (HR@1 0.045). LEX, a word-overlap baseline against the last activity's name, is the control.
- **Simulation with known needs.** 10 units × 10 activities and 3,000 learners, each with three weak units. With probability α the platform path picks the next step. need@10 scores true usefulness. Oracles: NEED (exact needs) and PI (true logging probabilities).
- **Structure-corrected accuracy.** Each test step is weighted by w = 1/max(p, 0.01), with p the MC transition probability. This gives a self-normalised IPS-style NDCG. The author stresses it "is not an estimate of online performance" and is deliberately unfavourable to MC.
- **Release.** The `beat-the-syllabus` Python package and per-case results are on GitHub and Zenodo.

## 3. Impact — potential & realized

**Measured (P1, NDCG@10):**
- Structural share ρ is 0.81–1.00 (median 0.95). MC is the best structural predictor on 7/8 datasets (CONT on A09).
- The best personalised method (always SASRec) is significantly better on A15 (+0.102), MOOC (+0.088), Junyi (+0.047), A17 (+0.015) and EdNet (+0.007). It is significantly worse on A12 (−0.020) and not different on A09 and Eedi. On Eedi, three other SASRec seeds gave significant lifts of +0.024 to +0.043, so there "the conclusion depends on the training run".
- Without MC, POP/ORDER/CONT reach a median ρ of only 0.45. "The shortcut is the paths, not the syllabus as written."
- On novel transitions, no method exceeds NDCG@10 0.162. Novel steps are 72% of A09 tests and 66% of EdNet tests.
- Off-path steps are much harder on four of six datasets, e.g. Junyi 0.748 on-path vs. 0.130 off-path. On Junyi, learner-chosen exercises score 0.264 vs. 0.649 for platform suggestions (best structural).
- ZPD ranks below popularity on all seven datasets with outcomes, and DKT on six, even though DKT predicts outcomes better (AUC 0.65–0.82 vs. 0.50–0.77).

**Measured (LLM rankers, HR@1 of 20, random level 0.05):**
- Random negatives on A09: Qwen 0.5B 0.600, LEX 0.594, CONT 0.650. The better LLM beats LEX by at most 0.056 on any dataset.
- Structural negatives: LLMs fall to 0.095–0.110 on A09 and 0.055 on EdNet. On Junyi and Eedi, MC leads the best LLM by at least 0.14 (Table 8).
- 0.5B → 7B changes HR@1 by −0.03 to +0.06, with "no systematic gain".

**Measured (P2 and simulation):**
- Under the temporal split, ρ is 0.62–1.00 (median 0.91) and absolute scores are lower.
- In the simulation, ρ rises from 0.53 at α=0 to 0.99 at α=0.75. Kendall τ between NDCG@10 and need@10 falls from 0.86 to 0.16 at α=0.9. NEED drops from 3rd to 7th of 11 by NDCG@10 at α=0.75, while SASRec (need@10 0.40) and MC (0.37) top it.
- Corrected accuracy keeps τ at 0.85 (α=0.5) and 0.75 (α=0.75) and ranks NEED 2nd. It fails too at α=0.9 (τ 0.35).
- On real data, corrected lifts are significant on 7/8 datasets (all but A09), e.g. A15 +0.245 (MCLD) and MOOC +0.202. Corrected ρ has median 0.66.

**Potential:** a six-item syllabus-aware checklist. (1) Report structural predictors. (2) Report S_struct, Δ with CIs, ρ and corrected accuracy. (3) Split by step type and initiator. (4) Use structural negatives for candidate-set evaluation. (5) Prefer temporal splits. (6) Don't read log agreement as pedagogical value; claims about learning need randomised or field data. The LLM finding is framed as "a caution rather than a verdict" for models up to 7B.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A sharp, reusable measurement frame for any platform-steered log

Each ingredient is familiar: strong-baseline reproducibility audits, sampled-metric pitfalls, IPS reweighting, Han et al.'s transition-heuristic shortcut. What's new is a small set of reportable numbers (S_struct, Δ, ρ) and a simulation that shows offline NDCG ranking the true-needs oracle near the bottom. The structural-negatives test for LLM rankers is the most portable piece. "Random negatives plus LEX" is a cheap sanity check every LLM-recsys paper should run.

The lesson goes beyond education (my mapping). Any feed, onboarding flow or "next episode" surface where the product picks the next item has the same problem: next-item accuracy partly scores your own logging policy. A team could report ρ against a Markov baseline and add the transition-weighted NDCG next to its usual offline metrics. Caveats: one author, modest tuning grids, SASRec hitting its time budget on three datasets, and LLMs capped at 7B on CPU. The corrected metric uses MC's own probabilities, so it is a diagnostic, not a fair leaderboard. It also cannot replace online or randomised evaluation, which the paper says plainly.

### Similar / related work

- [**An embarrassingly simple graph heuristic reveals shortcut-solvable benchmarks for sequential recommendation**](https://arxiv.org/abs/2605.07125) — Han et al. A training-free transition-graph heuristic matches generative recommenders on standard sequential benchmarks. This paper extends the shortcut argument to educational logs, where the shortcut is designed in.
- [**The Recall Ceiling of LLM Recommendation Reranking**](2026-09-28-arxiv-recall-ceiling-llm-reranking.md) (in this bank) — another candidate-set critique of LLM reranker evaluation: oracle candidate sets inflate NDCG. Here, random negatives make the task solvable by topic matching.
- [**Large Language Models are Zero-Shot Rankers for Recommender Systems**](https://arxiv.org/abs/2305.08845) — Hou et al. Documents the order, popularity and position biases of LLM rankers that motivate the likelihood-based scoring used here.
- [**UniER: a unified benchmark for item-level and path-level exercise recommendation**](https://arxiv.org/abs/2605.16750) — Cheng et al. Benchmarks 18 exercise-recommendation methods on nine datasets with a simulated cognitive-gain metric, a different route around raw log agreement.

### Jargon buster

- **Sequencing policy (π)** — the combined rule of syllabus, teacher, engine and learner that produced the logged next activity. Offline accuracy measures agreement with it.
- **Structural share (ρ)** — the best accuracy of learner-agnostic predictors divided by the best accuracy of any method. Close to 1 means the benchmark mostly rewards replaying the platform.
- **Lift over structure (Δ)** — a recommender's metric minus the best structural predictor's metric. It is the only part that can reflect personalisation.
- **Structural negatives** — candidate distractors drawn from items the course structure already finds plausible, so topic matching alone cannot pick the target.
- **Leave-last-out vs. global temporal split** — hold out each learner's last item vs. cut all data at one point in time. The latter avoids training on other learners' future.
- **Self-normalised inverse-propensity weighting** — reweight test cases by 1/probability under a reference policy, then divide by the total weight, so rare (unexplained) steps count more.
