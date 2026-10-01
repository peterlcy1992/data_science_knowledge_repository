# Kuaishou E-commerce — An Agent That Learns From Its Own A/B Tests

A deep dive into A/B Agent, a self-evolving LLM agent for iterating recommendation strategies. Researchers at Kuaishou E-commerce organise past strategies into a hierarchical experience tree keyed by business scenario, recommendation stage and optimisation objective, use multi-path Tree-RAG retrieval to generate new actionable strategies, and then refine parameters and knowledge from continuous A/B feedback. They built an industrial benchmark from 310 historical strategies across three scenarios and report a 4.829% GMV improvement on a short-video e-commerce platform with guardrail metrics staying positive — author-reported numbers, with limited experiment-design detail.

Source article: "A/B Agent: A Self-Evolving Agent for Strategy Iteration in Industrial A/B Testing" — arXiv (Jiang et al.), https://arxiv.org/abs/2608.04625 (published 2026-08).
