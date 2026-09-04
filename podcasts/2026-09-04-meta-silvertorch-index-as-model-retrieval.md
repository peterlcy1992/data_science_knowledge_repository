# Meta — One Model Replaces the Whole Retrieval Stack

A deep dive into SilverTorch, the system Meta built to collapse recommendation
retrieval — normally split across separate CPU services for approximate
nearest-neighbor search, feature filtering, and scoring — into a single
GPU-native PyTorch model under a new "Index as Model" paradigm. We cover the
business problem (network overhead and duplicated infrastructure from
stitching together microservices as retrieval architectures grew more
complex), the technical approach (a model-based GPU Bloom filter for
candidate filtering fused with an Int8-quantized approximate-nearest-neighbor
kernel, plus unified scoring layers that replace what used to be separate
services), and the reported production payoff: a 23.7x throughput
improvement and 13.35x cost-efficiency gain over the prior CPU-based
approach, now running across hundreds of retrieval models serving billions
of daily active users. Source article: "SilverTorch: Index as Model — A New
Retrieval Paradigm for Recommendation Systems" — Engineering at Meta,
https://engineering.fb.com/2026/05/26/ml-applications/silvertorch-index-as-model-new-retrieval-paradigm-recommendation-systems/
(published 2026-05).
