# Instacart — The Death of the Static Shopping Page

A deep dive into how Instacart rebuilt its Shopping Hub — the discovery page
shoppers see right after picking a retailer — around a four-phase generative
pipeline instead of a static, manually curated content library. We cover the
business problem (personalization that couldn't scale, and a page built by
siloed teams that never felt cohesive), the technical approach (an LLM agent
that designs page themes top-down, retrieval-augmented keyword generation
grounded in the real catalog, layered LLM-judge and embedding-based quality
filters, and a cheap distilled classifier that cuts evaluation cost by an
estimated 99%), and what the early results show — and don't yet show — about
putting a generative model in charge of page structure itself. Source
article: "Our Early Journey to Transform Instacart's Discovery
Recommendations with LLMs" — Instacart Tech,
https://tech.instacart.com/our-early-journey-to-transform-instacarts-discovery-recommendations-with-llms-cf4591a8602b
(published 2026-02).
