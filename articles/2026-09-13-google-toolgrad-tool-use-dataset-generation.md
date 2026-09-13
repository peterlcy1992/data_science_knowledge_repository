---
id: google-toolgrad-tool-use-dataset-generation
title: "ToolGrad: Efficient Tool-Use Dataset Generation with Textual \"Gradients\""
source: "Google Research"
url: "https://research.google/blog/toolgrad-efficient-tool-use-dataset-generation-with-textual-gradients/"
published: "2026-09"
added: "2026-09-13"
category: llm-genai
tags: [tool-use, function-calling, synthetic-data, agents, textgrad, dataset-generation]
novelty: 4
sourced_via: "full-text fetch"
---

# ToolGrad: Efficient Tool-Use Dataset Generation with Textual "Gradients"

**Source:** [Google Research](https://research.google/blog/toolgrad-efficient-tool-use-dataset-generation-with-textual-gradients/) · Published 2026-09 · Added 2026-09-13
**Category:** LLMs & Generative AI · **Tags:** `tool-use`, `function-calling`, `synthetic-data`, `agents`, `textgrad`, `dataset-generation`

## TL;DR

Google Research flips the usual recipe for generating LLM tool-use training data — instead of writing a user query first and then struggling to annotate a matching multi-step tool-call chain, ToolGrad builds a valid API-call workflow first (guided by an iterative propose-execute-select-update loop that treats an LLM critic's feedback as "textual gradients") and only then synthesizes the user query to match, hitting a 99.8% annotation pass rate and producing a fine-tuned 12B model that scores competitively with Gemini 2.5 Pro and Claude 4.5 Opus on the Berkeley Function Calling Leaderboard.

## 1. Business context

Training an LLM to reliably call external tools/APIs (function calling) requires training data pairing a realistic user request with a correct sequence of API calls that satisfies it. The standard "query-first" recipe — generate a plausible user query, then search for a tool-call chain that answers it — frequently fails: a randomly generated query may not actually be answerable by the available APIs, or the search for a matching call chain (often depth-first search over thousands of APIs) may not converge, wasting generation cost and yielding noisy or invalid training examples. As tool catalogs (ToolBench alone has 16,000+ real APIs) and expected task complexity both grow, the annotation-failure rate of query-first generation becomes a real bottleneck on how much clean tool-use training data can be produced.

## 2. Technical details

ToolGrad inverts the pipeline into an "answer-first" framework: build a valid, executable tool-call workflow *before* writing the query it will answer, since an explicit, already-verified tool-use solution is far less ambiguous to work backward from than a natural-language query is to work forward from. The workflow itself is constructed iteratively through a four-module loop:

- **API Proposer** — narrows a sampled pool of candidate APIs down to promising ones that could plausibly extend the workflow being built.
- **API Executors** — actually run the candidate API calls in parallel and produce execution reports (what each call would return).
- **API Selector** — reviews those execution reports and picks the best-performing API call to add next, producing directional feedback on what worked and what didn't.
- **LLM Updater** — revises the synthetic user query and the AI's response so they stay consistent with the growing set of API calls chosen so far.

This loop is explicitly framed as an adaptation of **TextGrad**'s "textual gradients" idea: rather than optimizing a static prompt with numeric gradients, ToolGrad treats the API Selector's plain-language feedback as the "gradient" signal that steers construction of the next step of the workflow — an iterative propose→execute→select→update cycle rather than a one-shot search. Using this pipeline, Google built the **ToolGrad-500** dataset by sampling from ToolBench's catalog of 16,000+ real APIs, and used it to fine-tune a 12B model, **ToolGrad-12B**.

## 3. Impact — potential & realized

**Realized:** ToolGrad's generation pipeline achieves a 99.8% pass rate (i.e., nearly all generated workflows are valid and executable), versus the failure-prone query-first, depth-first-search baseline. On the Berkeley Function Calling Leaderboard, ToolGrad-12B scores 83.1 — ahead of GPT-5's 74.4, essentially matching Claude 4.5 Opus (82.8), and just behind Gemini 2.5 Pro (83.2) — despite being fine-tuned from a much smaller base model than those frontier models. Notably, ToolGrad-12B also outperforms Gemini 2.5 Flash-Lite, the very model used as the "teacher" generating its training data.

**Potential:** an answer-first, gradient-guided data-generation recipe generalizes beyond function calling to any synthetic-data setting where verifying a candidate solution is easier than generating a matching prompt for it — e.g., code generation, structured-output tasks, or other agentic workflows where "does this actually execute correctly" is a cheap, hard check.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A clean inversion of a known bottleneck, with a strong result to back it

Answer-first (or "solution-first") data generation isn't a wholly unprecedented idea in synthetic-data literature, but applying it specifically to tool-use annotation — where the "solution" is a verifiable, executable API-call chain rather than an unverifiable free-text answer — is a well-targeted fit, and adapting TextGrad's textual-gradient framing to guide the iterative workflow construction (rather than just a fixed search) is a genuinely useful mechanism, not just a rebrand. The headline result — a 12B model produced from data generated by a smaller "teacher" model outperforming that teacher, while landing within a point of Gemini 2.5 Pro and Claude 4.5 Opus on a public leaderboard — is a strong practical validation that data quality/structure can matter more than teacher-model size for this task.

### Similar / related work

- [**TextGrad: Automatic "Differentiation" via Text**](https://arxiv.org/abs/2406.07496) — the original framework ToolGrad explicitly adapts, which backpropagates LLM-generated natural-language feedback through a computation graph as a general optimization technique; ToolGrad specializes this specifically to constructing tool-call workflows.
- [**Designing Lifecycle Policies for AgentCore Memory**](2026-09-09-aws-agentcore-memory-lifecycle-policies.md) (in this bank) — a different piece of the production-agent-tooling puzzle (managing what an agent remembers across tool calls) that pairs naturally with better tool-use training data as agents get more capable at multi-step tasks.
- **ToolBench (API benchmark/dataset)** — the underlying 16,000+ real-API catalog ToolGrad samples from to build training workflows; well-established as a tool-use benchmark, used here as raw material rather than as the contribution itself.

### Jargon buster

- **Function calling / tool use** — an LLM's ability to invoke external APIs or tools (e.g., a weather API, a database query) as part of answering a request, rather than only generating free text.
- **Textual gradient** — a natural-language critique or feedback signal used to iteratively steer an LLM-driven process, analogous to how a numeric gradient steers standard neural-network training, but expressed as plain-language directional feedback instead of a number.
- **Answer-first (vs. query-first) generation** — building the correct solution to a problem before writing the problem statement that leads to it, which sidesteps the difficulty of guessing whether a randomly generated question is even answerable.
- **Berkeley Function Calling Leaderboard** — a public benchmark that scores how accurately different LLMs can select and correctly invoke tools/functions across a range of tasks, commonly used to compare function-calling capability across models.
