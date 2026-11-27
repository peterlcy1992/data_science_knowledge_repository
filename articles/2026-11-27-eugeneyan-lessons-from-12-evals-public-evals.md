---
id: eugeneyan-lessons-from-12-evals-public-evals
title: "Lessons from 12 Evals: Where They Break and What to Measure Instead"
source: "Eugene Yan (eugeneyan.com)"
url: "https://eugeneyan.com/writing/public-evals"
published: "2026-11"
added: "2026-11-27"
category: llm-genai
tags: [llm-evaluation, agent-evaluation, benchmarks, grader-error, measurement-error, pass-k, reliability, all-pass-scoring, llm-as-judge, harness-effects]
novelty: 3
sourced_via: "full-text fetch"
---

# Lessons from 12 Evals: Where They Break and What to Measure Instead

**Source:** [Eugene Yan (eugeneyan.com)](https://eugeneyan.com/writing/public-evals) · Published 2026-11 · Added 2026-11-27
**Category:** LLMs & Generative AI · **Tags:** `llm-evaluation`, `agent-evaluation`, `benchmarks`, `grader-error`, `measurement-error`, `pass-k`, `reliability`, `all-pass-scoring`, `llm-as-judge`, `harness-effects`

## TL;DR

Eugene Yan reviews twelve public agent benchmarks: four on coding and science, six on knowledge work, two on browsing and computer use. In eight of the twelve, audits or issue reports found the grader failing valid work, and in some it passed incorrect or hallucinated work. He argues that a benchmark score is a noisy measurement of a model-harness pair, that average pass rate hides reliability (two 70% agents can score 70% and 17% on pass^5), and that cost per task should be judged against human review time, not tokens.

## 1. Business context

Eval scores are often the first thing practitioners learn about a new model. The question is how much weight to put on them. Yan's answer: look past the headline number to how tasks are built, how they are graded, and what the error analyses show. Use public scores to narrow the shortlist, then evaluate in your own harness.

Most eval tasks have four parts. An **instruction**, given once, usually with no chance to ask clarifying questions. An **environment** (a container with a repo at a fixed commit, a VM, simulated business apps, a folder of documents). A **grader** (deterministic code, an LLM judge over yes/no rubric items, or both). An optional **reference** solution from a human expert.

Benchmarks are now maintained like software, with versioned releases, issues and pull requests. Agents' Last Exam v1.1 retired 30 tasks and revised 57 others. Harvey LAB's public set grew from about 1,250 to 2,010 tasks since May 2026. Releases can break comparability: Terminal Bench drops saturated tasks with each version.

For a data scientist the piece is mostly about measurement. The grader is a measuring instrument with false-negative and false-positive rates. Scoring rules (all-pass vs partial credit), harness, task versioning and answer-key noise all change what the number means.

## 2. Technical details

**Shared design principles.**
- **Deterministic checks over LLM judges.** Code checks are reproducible and don't shift rankings when a judge model is updated. DeepSWE and AutomationBench use no LLM judge. Where a judge is needed (legal memo, clinical response), its job is narrowed to binary rubric items rather than a holistic score.
- **Grade the outcome, not the steps.** Terminal Bench inspects the final container state and ignores intermediate commands. AutomationBench, OSWorld 2.0 and DeepSWE do the same.
- **All-pass scoring is common.** A task passes only if every test or criterion passes (DeepSWE, Terminal Bench, Terminal Bench Science, AutomationBench, Harvey LAB). Harvey: "there is no partial credit for catching most of the issues." The cost is brittleness: one flawed check fails an otherwise correct solution. FrontierSWE and HealthBench Professional use partial credit; Agents' Last Exam, Finance Agent and OSWorld 2.0 report both.
- **Difficulty mining to slow saturation.** AutomationBench hardened easy tasks with irrelevant data and conflicting policies. HealthBench Professional made difficult tasks about 3.5x more common than in its 15,079-candidate pool. BrowseComp kept only questions the strongest models of the time could not solve. Terminal Bench retires saturated tasks.

**Recurring model failures.** Two dominate. (1) Skipping verification or stopping early: OSWorld 2.0 agents submitted without checking the final state and spent under 7% of their budget on error recovery; AutomationBench models processed part of a list and declared success. (2) Missing stated requirements: instruction following was the most common failure in GDPval, and OSWorld 2.0 agents dropped constraints stated in the prompt.

**Grader false negatives (failing correct work).** Usually a check stricter than the prompt, or one that tests an unstated requirement.
- Terminal Bench 4.0: Preference Model rebuilt 65 tasks and found 41 graded on an unstated requirement. With those made explicit (and shortcuts closed), one model went from 63% to 89%. Epoch AI separately found scoring defects in 30 of 66 tasks, 11 of which failed correct solutions.
- DeepSWE: the article reports reviewers finding 23 of 113 tasks marking correct solutions as failures, Epoch AI finding 18 of 113 in v1.1 (rated "Flawed"), and an audit putting it at "at least 20%" of tasks. The cause: hidden test files clash with tests the agent wrote, so agents that verify their own work are penalized. (The three figures are given in different places; their relationship is not spelled out.)
- OSWorld 2.0: an outside review found checks failing correct work in 23 of 108 tasks, e.g. a grader whose software can't open the task's own starter file.
- Terminal Bench Science: 128 task-fix issues filed against 57 of 70 tasks, 79 reporting verifier or instruction bugs (e.g. rejecting correct predictions in a different row order).
- AutomationBench: one review flagged 108 of 600 public tasks (43 missing/conflicting information, 65 grading defects). Another, across ~2,600 runs, found checks rejecting valid work in 115 tasks, such as treating "150,000" and "150000.0" as different.
- Answer keys: on BrowseComp, trainers who solved a question disagreed with the reference on 50 of 367 (14%); a later paper confirmed errors in 10 of 200 BrowseComp-Plus questions. Harvey removed 17 unsolvable criteria from its 120-task held-out set.

**Grader false positives (passing wrong work).** Rubrics check that an expected point is present, not that the rest is correct.
- Harvey LAB: the judge sees only task title, deliverable and criterion, not the matter files. Artificial Analysis found material hallucinations (wrong party, amount, date) in more than 60% of deliverables that passed every criterion.
- AutomationBench: the overview says 55% of assertions are substring contains/excludes checks; the detailed section says 57% of ~9,700. 94 tasks check a message for a one- or two-digit number, so any date or ID containing the digit passes. One task checks only that an email contains "3" and "4", so swapped counts pass.
- Terminal Bench runs negative tests (a do-nothing agent and an adversarial agent), yet reviewers found 44 of 65 v4 tasks could be passed by cheating.

**Scoring and noise, benchmark by benchmark (selected).**
- **GDPval:** 44 occupations, 1,320 tasks (220 public gold). Blind pairwise comparison by three experts against the human deliverable; headline is win-or-tie rate. Human graders agreed with each other 71% of the time; a trained grader model agreed with them 66%. Win rates peaked on tasks under two hours of expert time. In the dozen tasks Yan sampled, roughly half the rubric criteria check instruction following.
- **HealthBench Professional:** 525 tasks, 1,135 criteria (about two per task vs ~11 in the original HealthBench); an independent analysis found 47% of tasks have one positive criterion. Scores are length-adjusted by 1.47 points per 500 characters away from a single 2,000-character target, while physician baselines range ~600–3,800 characters (10th–90th percentile). Averaged over eight samples per task.
- **Terminal Bench Science:** all-pass forces binary rewards even for continuous metrics. One task needs class and period of all 100 stars right; a reported run got 99 and scored zero.
- **FrontierSWE v2:** v1 scored on wall-clock time, which made rankings unstable across host machines; v2 uses a deterministic weighted instruction count. Partial credit is normalized between a baseline (0.0) and a full-credit target (1.0). Five trials per task. Most models used 100M–500M tokens per trial; the cheapest model above 30% averaged $97 per trial.
- **Finance Agent v2.1:** a three-LLM jury grades severity-weighted checks; failing a "dealbreaker" zeroes the task. Top model 68% partial credit, 59% all-pass.
- **Agents' Last Exam:** partial credit, 93% deterministic. Best configuration fully passed 24% of public tasks at launch. Failure split: approach 47% (wrong strategy 30%, gave up early 17%), understanding 31%, execution 22%.
- **OSWorld 2.0:** rubric of ~27 criteria per task; LLM-judged criteria are 11.5% of the score. Top agent 20.6% binary, 54.8% partial. In the paper's behavioral analysis, 31%–43% of trajectories were flagged for a possible mismatch between the state the agent reached and the state recorded.

**Harness effects.** A score belongs to a model-harness pair. On Terminal Bench 2.0, one model scored 57.8% on the neutral Terminus 2 harness and 52.1% on its provider's own harness; another 32.6% vs 19.6%. On FrontierSWE, models scored higher on Proximal's Proximus harness than on Claude Code or Codex across six tasks.

## 3. Impact — potential & realized

**What the sources measured (as compiled here).** Grader false negatives were reported in eight of twelve benchmarks. Making unstated requirements explicit moved one Terminal Bench model from 63% to 89%. Material hallucinations appeared in over 60% of fully passing Harvey LAB deliverables. AutomationBench models falsely declared success in 72%–91% of analyzed failures. In GDPval's analysis, GPT-4o cost about a tenth of GPT-5 per task, but once expert review and redo time was included, GPT-4o was slower than an expert working alone while GPT-5 was faster. Laban et al. found models scored 39% lower on average in simulated multi-turn conversations than single-turn.

**What Yan proposes (his "hot takes"; he says some are "vibes").**
- **Report pass^k alongside average pass rate.** An agent that solves 70% of tasks every time stays at 70% over five trials; one that solves every task 70% of the time falls to 17% (0.7⁵). The first can be trusted on its 70%; every output of the second needs checking.
- **Cost per task is misleading.** It averages over passes and fails, and models can fail cheaply by giving up. On FrontierSWE, one model submitted and stopped within eight hours of a 20-hour budget in 169 of 170 trials. The scarce resource is human attention.
- **Verifiable tasks test implementation more than judgment.** 83 of 122 ALE v1.1 public instructions use "exact" or "exactly"; FrontierSWE hands the agent a self-check tool that tracks the grader score.
- **Real work is multi-turn.** Few evals simulate users; OSWorld 2.0 is an exception (clarification user, mid-task requirement changes), and agents guessed instead of asking.
- **Invest in graders, not just harder tasks.** As model errors shrink and grader errors stay fixed, a growing share of remaining failures are grader bugs. Audit tasks where multiple frontier models fail the same check; add negative tests; audit passing transcripts for reward hacking.
- **Scoring fixes:** publish partial credit next to all-pass; report a companion score on a fixed task subset across versions; score performance tasks as share of cost saved (1 − 1/speedup) instead of capping at a target; benchmark length against the physician's own response.

**Limits of the piece.** It is a review, not a study. Error rates come from third-party audits, issue trackers and Yan's own sampling (a dozen GDPval tasks, "dozens" of DeepSWE trajectories), with different definitions and denominators. No uncertainty is attached to any of them.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A sharp field guide to grader error; the prescriptions are known, the cross-benchmark tally is the value

Pass^k, "evaluate in your own harness" and "LLM judges drift" are established ideas; τ-bench popularized the first. What is new is the side-by-side inventory of grader defects across twelve current benchmarks, with concrete counts. That turns "benchmarks are noisy" into "here is roughly how noisy, and in which direction".

The data-science reading is that a benchmark score is a misclassified binary outcome. False negatives cap observed accuracy below true accuracy. False positives inflate it. Neither is constant across models: a grader that penalizes agents who write their own tests is differential error correlated with a behavior we want. All-pass scoring compounds per-check error: with many checks per task, even small per-check false-negative rates add up to a large task-level rate. Yan's point that grader error grows as a *share* of failures as models improve is the key one. At the top of a leaderboard, the gap between models can be smaller than the gap between grader and truth. A 14% answer-key disagreement on BrowseComp means differences of a few points there are not interpretable without an error model.

What is missing is the inference layer: confidence intervals, clustering by task source, and correction for judge error. Several in-bank papers supply exactly that. Practitioners should copy three habits: report pass^k with k ≥ 3, publish a fixed-subset score across versions, and audit a random sample of *passing* runs, not just failures.

### Similar / related work

- [**Transport-Safe Evaluation of LLM Agents: Trajectory-Dependent Judge Error and Anytime-Valid Auditing**](2026-11-24-arxiv-transport-safe-llm-agent-evaluation-judge-error.md) (in this bank) — formalizes the problem Yan documents: judge error that depends on the trajectory biases scalar corrections, and a randomized human audit with AIPW fixes it.
- [**Your Agent Aced the Task. Will It Do It Again?**](2026-09-22-ibm-research-altk-evolve-agent-consistency.md) (in this bank) — IBM Research reports Pass^5 alongside mean success on AppWorld, the reliability metric Yan argues for.
- [**How Many Sources, Not Just How Many Problems: Planning the Precision of LLM Evaluations from Earlier Results**](2026-11-26-arxiv-planning-precision-llm-evaluations-sources.md) (in this bank) — design-effect intervals for benchmarks whose problems share sources; the uncertainty layer this review leaves out.
- **τ-bench** (Sierra) — the benchmark Yan credits with popularizing pass^k.

### Jargon buster

- **Grader** — the code checks, LLM judge or both that decide whether an agent's output passes. It is a measuring instrument and can be wrong.
- **False negative / false positive (grader)** — failing work that should pass / passing work that should fail.
- **All-pass vs partial credit** — all-pass gives 1 only if every check passes; partial credit gives the weighted share of checks met (0.0–1.0).
- **pass^k** — a task counts as solved only if the agent passes all k independent trials. Measures reliability, unlike average pass rate or pass@1.
- **Harness** — the scaffolding around a model: system prompt, tools, compaction, retry budget. Scores belong to the model-harness pair.
- **Prompt-verifier bijection** — DeepSWE's review rule that the grader tests exactly what the instruction asks, nothing unstated.
- **Saturation** — when top models score near the ceiling, so the benchmark no longer separates them; benchmarks respond by retiring or hardening tasks.
- **Negative test** — running a known-bad agent (do-nothing, adversarial) to confirm the grader rejects it.
