---
id: arxiv-transport-safe-llm-agent-evaluation-judge-error
title: "Transport-Safe Evaluation of LLM Agents: Trajectory-Dependent Judge Error and Anytime-Valid Auditing"
source: "Efrei Research Lab, Université Paris-Panthéon-Assas / CEDRIC, Cnam (arXiv cs.AI)"
url: "https://arxiv.org/abs/2611.30742"
published: "2026-11"
added: "2026-11-24"
category: llm-genai
tags: [llm-as-a-judge, agent-evaluation, measurement-error, aipw, randomized-auditing, partial-identification, confidence-sequences, rank-inference]
novelty: 3
sourced_via: "full-text fetch"
---

# Transport-Safe Evaluation of LLM Agents: Trajectory-Dependent Judge Error and Anytime-Valid Auditing

**Source:** [Efrei Research Lab, Université Paris-Panthéon-Assas / CEDRIC, Cnam (arXiv cs.AI)](https://arxiv.org/abs/2611.30742) · Published 2026-11 · Added 2026-11-24
**Category:** LLMs & Generative AI · **Tags:** `llm-as-a-judge`, `agent-evaluation`, `measurement-error`, `aipw`, `randomized-auditing`, `partial-identification`, `confidence-sequences`, `rank-inference`

## TL;DR

Agent leaderboards often correct an LLM judge's verdicts using one sensitivity/specificity pair measured on a calibration set. If the judge's errors depend on the trajectory, and agents produce different trajectories, that correction is biased. The paper derives the exact bias. Instead it recommends a randomized human audit with AIPW, an anytime-valid confidence sequence, and rank *sets*. On a semi-synthetic four-agent benchmark, the scalar correction had maximum bias 0.245 and never recovered the true ranking (0/250). Audited AIPW kept maximum bias below 0.003.

## 1. Business context

Expert labels for agent trajectories are expensive, so teams grade agents with a second LLM. They estimate its sensitivity and specificity once on a hand-labelled sample and correct every agent's judged success rate with those two numbers. The authors point out that "a judge, however, reads trajectories, not agent names". Its errors can change with trajectory length, task family, number of tool calls or failure type. Error rates averaged over calibration trajectories therefore need not hold for another agent, even with a blind judge.

As a warning sign, they cite a *prior analysis* of AgentRewardBench public outputs that they did not rerun. Judge sensitivity fell from 0.840/0.884/0.876 in the shortest-trajectory tercile to 0.182/0.364/0.477 in the longest, for three judges (AER, GPT-4o, GPT-4o-mini). Leave-one-agent-out scalar calibration gave reported biases from +0.097 to −0.186. The authors say these figures "are not new evidence and do not show that length alone causes the drop".

The question is when a judge-based leaderboard can be trusted, and what to report when it cannot. The authors call their contribution "integrative": AIPW, latent classes, confidence sequences and rank inference are not new, and the paper connects them around an agent-specific target.

## 2. Technical details

- **Transport bias (Theorem 1).** Assume the judge is blind given (trajectory covariates X, true success Y). The transported Rogan–Gladen correction then converges to θ_a + B_a, where B_a = [θ_a(s*_a − s₀) + (1 − θ_a)(t₀ − t*_a)] / J₀. Here s*_a and t*_a are the judge's sensitivity and specificity averaged over *agent a's* trajectories, and s₀, t₀, J₀ are the calibration values. The gap s*_a − s₀ equals a covariance between the agent's trajectory-shift weights and judge accuracy. So the bias "couples trajectory shift with judge accuracy, not just a low average accuracy". Two agents' order reverses exactly when B_b − B_a > θ_a − θ_b.
- **More judge calls are not a generic fix.** A majority vote over an odd number ≥ 3 of i.i.d. calls pushes each trajectory-level accuracy further from 1/2, "so the bias can grow or shrink".
- **One-judge identification (Theorem 2, Proposition 1).** θ_a is point-identified only if calibration observes both classes wherever the target agent puts mass and the judge is informative there (J(x) ≠ 0). Otherwise θ_a lies in a support-failure set [ν_a, ν_a + ρ_a], where ρ_a is the target mass without support.
- **Three judges (Theorem 3).** Three conditionally independent judges identify θ(x) from second and third moments. Two are "generically insufficient". The prior source analysis reports within-(Y, length) judge dependence ψ = 0.41–0.70, so the paper defines a *dependence-envelope set* I_Γ. The bound Γ must come from outside the judge data, e.g. external human calibration, held-out perturbations or a preregistered range. Without it, report only the independence point and a sensitivity curve.
- **Randomized human auditing (recommended default).** Audit episodes with known probabilities φ(V) ≥ φ_min, where V = (X, judge verdict), and use cross-fitted AIPW. The estimator is exactly design-unbiased for the finite-population mean "even when the imputation model is wrong", and semiparametrically efficient for the given design. The authors call this "less novel but stronger by design".
- **Allocation.** A bounded Neyman-type rule φ*(v) = min{1, max{φ_min, λ*σ(v)}}, learned from a randomized pilot wave and applied in a second wave.
- **Anytime-valid monitoring (Theorem 4).** A hedged e-process over a fixed λ-grid gives a confidence sequence. Its coverage is finite-sample and holds under adaptive auditing, repeated looks and arbitrary stopping. This requires a *stable target*: one frozen agent on independently drawn tasks. It does not hold for clustered tasks, small benchmarks sampled without replacement, agent updates or mixed agents. Use level α/K for K agents.
- **Rank sets.** Rank sets come from pairwise tests with familywise directional control. An identification-robust version certifies only orderings that hold for every compatible ability vector. Comparisons should be clustered at the task-generating unit, e.g. the software repository.
- **Algorithm 1.** It chains these steps into a protocol. The output is "simultaneous ability intervals and rank sets, not point scores alone".
- **Disclosure.** The paper states that Claude drafted or edited all sections, including the proofs, and that ChatGPT assisted an earlier version. The authors say they checked every source, statement and number and that no data or results were AI-generated.

## 3. Impact — potential & realized

**Measured (all newly executed results are simulations or the semi-synthetic benchmark; public-data figures are carried over from prior analyses, not rerun):**
- *Four-agent semi-synthetic benchmark, 250 replications.* Scalar plug-in with oracle calibration: MAE 0.168, maximum bias 0.245, mean pointwise coverage 0.016 (nominal 0.95), exact full ranking 0/250. Conditional oracle, uniform-audit AIPW and design-aware AIPW: MAE 0.018 / 0.023 / 0.021, coverage 0.939 / 0.939 / 0.950. Maximum bias was below 0.003 for both audited estimators.
- *48-cell rich-covariate stress test* (length × task family × tool-call intensity). The target mass with enough calibration support was only 0.209, 0.421, 0.643 and 0.805 at 600, 1,200, 2,400 and 4,800 labels. A cellwise plug-in had MAE 0.188 → 0.077 over that range. AIPW with a 12% uniform randomized audit stayed at 0.018–0.020.
- *Support-failure example.* Set [0.445, 0.645] contains the truth 0.525. Naive extrapolation from short trajectories gives 0.431, outside the set.
- *Three judges with a shared factor.* The independence point 0.502 misses the truth 0.525. The half-envelope set is [0.457, 0.547]. As conditional dependence grew to 0.231, label-free MAE rose from 0.0085 to 0.0343, while AIPW with a 10% audit stayed at 0.0062–0.0096.
- *Allocation.* The two-wave rule's variance ratio to the oracle fell from 1.076 (20,000 episodes) to 1.038 (10⁵) and 1.018 (5 × 10⁵). Uniform auditing stayed at 1.077.
- *Peeking.* In 200 streams monitored after every episode up to t = 3,000, repeated Wald intervals jointly covered 0.535, against 0.995 for the confidence sequence. The confidence sequence was wider at the final look.
- *Ranks.* With interval-centre displacement 0.025 over 1,000 simulations, identification-robust rank sets had simultaneous coverage 1.000. Midpoint rankings had 0.037 coverage and 0/1,000 exact recovery. With 40 repositories × 10 tasks and eight truly tied systems, treating tasks as independent gave a false-split rate of 0.188. Repository-cluster Holm cut it to 0.035 and restored coverage to 0.965.

**Potential:** A recipe for agent leaderboards and internal agent A/B comparisons: audit a random ~10–12% of episodes with known probabilities and report intervals and rank sets. The authors list as limitations that the main results are semi-synthetic, that live-judge validation is still needed, and that a preregistered test of the trajectory-length effect has not been run, "so no causal effect of length is claimed".

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — A clear, well-argued synthesis that names a real flaw in judge-corrected agent leaderboards

Theorem 1 is simple, but it is useful. It turns a vague worry ("judge accuracy varies") into a bias formula and an exact ranking-reversal condition that practitioners can reason about. Everything after that is established machinery (two-phase AIPW, Neyman allocation, e-process confidence sequences, rank inference), and the paper says so openly. The value is the protocol and the honesty about scope: the paper is explicit about what was rerun, what was preregistered and what remains assumption.

The weak spot is evidence. There is no live-judge experiment, and the motivating AgentRewardBench numbers are carried over from prior work. Still, the practical message for anyone running agent evals is robust: one global judge confusion matrix is not safe to reuse across agents, and a small randomized human audit is the design-based fix. The clustering result (0.188 false splits when SWE-bench-style tasks are treated as independent) is a quietly important point for leaderboard builders.

### Similar / related work

- [**Prediction-Powered LLM Ranking with Adaptively Collected Human Feedback**](2026-11-11-arxiv-pp-rank-prediction-powered-llm-ranking-adaptive-feedback.md) (in this bank) — also combines scarce human labels with LLM-judge predictions under known sampling probabilities and outputs rank confidence sets, for Arena-style preference data.
- [**Efficient inference for noisy LLM-as-a-judge evaluation**](https://arxiv.org/abs/2601.05420) — Chen et al.; the EIF/PPI uniform-audit route used as this paper's baseline.
- [**How to correctly report LLM-as-a-judge evaluations**](https://arxiv.org/abs/2511.21140) — Lee et al.; the scalar sensitivity/specificity plug-in correction whose transport bias this paper derives.
- [**Trustworthy Method Comparison with AI Judges: Estimation and Design under Order, Batch, and Aggregation Effects**](2026-10-07-arxiv-trustworthy-method-comparison-ai-judges.md) (in this bank) — another statistical treatment of when judge-based comparisons go wrong, focused on order and batch effects.

### Jargon buster

- **Transport bias** — error from carrying a quantity (here the judge's error rates) measured on one population over to another where it does not hold.
- **Rogan–Gladen correction** — the classic formula that converts an imperfect test's positive rate into a true prevalence using its sensitivity and specificity.
- **AIPW (augmented inverse-probability weighting)** — combine a model's prediction for every episode with a reweighted correction from the randomly audited ones; it stays unbiased even if the model is wrong.
- **Confidence sequence / e-process** — an interval that stays valid however often you look and whenever you stop, unlike a fixed-time Wald interval.
- **Partial identification** — when the data cannot pin down a single value, you report the set of values consistent with the data instead of a point.
