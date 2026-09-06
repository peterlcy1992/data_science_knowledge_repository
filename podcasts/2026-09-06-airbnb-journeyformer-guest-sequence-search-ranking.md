# Airbnb — A Transformer That Reads Your Whole Travel History

A deep dive into JourneyFormer, the transformer Airbnb built to replace
hundreds of hand-crafted "what this guest likes" statistics with a model
that reads a guest's raw event history directly. We cover the business
problem (aggregate features that scale poorly and throw away order,
recency, and co-occurrence information a raw sequence preserves, against
histories that are long, exploratory, and have very sparse booking labels),
the technical approach (splitting history into a 7-year non-view sequence
and a 21-day view sequence, a 4-layer transformer that surprisingly performs
better *without* feed-forward sublayers, hierarchical multi-level location
embeddings, and throughput tricks that cut training time roughly 4x), and
the realized impact: a 1.48% offline ranking-quality gain and, in a 3-week
production test, measurable lifts in bookers, booked nights, and views
across both search ranking and email ranking — including a 5% jump in
email views. Source article: "JourneyFormer: Encoding Airbnb Guest Journey
with Sequence Modeling" — Airbnb Tech Blog / arXiv (KDD 2026),
https://arxiv.org/abs/2606.19108 (published 2026-06).
