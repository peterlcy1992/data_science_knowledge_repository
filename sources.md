# Curated sources

The daily refresh sweeps these sources for new articles. Seed inspiration is
the [*Snacks Weekly on Data Science*](https://podcasts.apple.com/us/podcast/snacks-weekly-on-data-science/id1709920384)
podcast, which reviews recent applied-ML posts from big-tech engineering blogs;
the list below is expanded well beyond it.

> **Balance the two families.** This is a *data-science* bank: aim for a roughly
> even split between **Core DS** (statistical modelling, experimentation & causal
> inference, product analytics, forecasting — the **Tier 0** sources below) and
> **AI / ML-systems** (Tiers 1–3). The AI tiers are richer and easier to find, so
> deliberately spend discovery effort on Tier 0 to keep intake ~50/50. See
> `taxonomy.md` → "Scope & balance" and `refresh-playbook.md` Steps 2/5.

## Tier 0 — Core data science (experimentation, causal, analytics, statistics)

*Prioritise these to counter the AI skew — the daily deep dive targets ~50% Core DS.*

| Source | Where | Focus |
|--------|-------|-------|
| Microsoft ExP | exp-platform.com, microsoft.com/en-us/research/group/experimentation-platform-exp | A/B testing at scale, variance reduction, trustworthy experimentation |
| Netflix experimentation | netflixtechblog.com (tag: experimentation) | Interleaving, quasi-experiments, causal inference, metrics |
| Booking.com experimentation | booking.ai, medium.com/booking-com-development | Large-scale online experimentation, stats pitfalls |
| Airbnb experimentation & DS | medium.com/airbnb-engineering (data-science-and-analytics) | Experiment platform, causal inference, metrics |
| Spotify experimentation | engineering.atspotify.com (tag: experimentation) | A/B testing, Bayesian vs frequentist, holdouts |
| DoorDash experimentation | careersatdoordash.com/engineering-blog | Switchback tests, variance reduction, marketplace causal |
| Eppo blog | geteppo.com/blog | Experiment analysis, CUPED, sequential testing, warehouse-native stats |
| Statsig blog | statsig.com/blog | Experimentation methodology, guardrails, metric design |
| Amplitude / Mixpanel | amplitude.com/blog, mixpanel.com/blog | Product analytics, retention/funnels, metric frameworks |
| Andrew Gelman | statmodeling.stat.columbia.edu | Statistical modelling, Bayesian & causal inference, applied stats |
| arXiv stat.ME / stat.AP | arxiv.org/list/stat.ME/recent, stat.AP/recent | Statistical methodology & applied statistics |
| arXiv econ.EM | arxiv.org/list/econ.EM/recent | Econometrics, causal estimation, marketplace inference |
| Nixtla | nixtlaverse.nixtla.io/blog | Time-series forecasting methods & benchmarks |

> Egress note: this environment's proxy blocks direct fetching of many blog
> domains (Medium-hosted blogs such as `netflixtechblog.com`, several corporate
> `careers*` domains, etc.). The refresh therefore uses **web search** as the
> primary discovery + summarisation channel and only attempts a direct fetch
> when a domain is reachable. Entries note when they were built from
> search-surfaced content rather than a full-text fetch.

## Tier 1 — Big-tech engineering & research blogs

| Source | Where | Focus |
|--------|-------|-------|
| Netflix Tech Blog | netflixtechblog.com | Recsys, personalization, media ML, ML infra |
| Uber Engineering | uber.com/blog/engineering | ML platform, forecasting, marketplace |
| Airbnb Tech | medium.com/airbnb-engineering | Search, ranking, data platform |
| DoorDash Engineering | careersatdoordash.com/engineering-blog | LLMs, personalization, fraud, forecasting |
| Meta Engineering / AI | engineering.fb.com, ai.meta.com | Recsys, LLMs, infra |
| Google Research / DeepMind | research.google/blog, deepmind.google | Foundational research |
| LinkedIn Engineering | linkedin.com/blog/engineering | Recsys, GNNs, feed ranking |
| Pinterest Engineering | medium.com/pinterest-engineering | Retrieval, ranking, embeddings |
| Spotify R&D / Engineering | engineering.atspotify.com, research.atspotify.com | Recsys, audio ML, generative retrieval |
| Instacart Tech | tech.instacart.com | Search, catalog, forecasting |
| Etsy / eBay Engineering | etsy.com/codeascraft, innovation.ebayinc.com | Search, ranking |
| Stripe / Shopify Engineering | stripe.com/blog/engineering, shopify.engineering | Fraud, data infra |

## Tier 2 — Vendor & platform blogs (production ML patterns)

| Source | Where | Focus |
|--------|-------|-------|
| Databricks | databricks.com/blog | Lakehouse, feature stores, MLOps |
| AWS ML Blog | aws.amazon.com/blogs/machine-learning | Applied ML, serving |
| NVIDIA Developer | developer.nvidia.com/blog | Inference, GPU, vLLM/Triton |
| Hugging Face | huggingface.co/blog | Open models, fine-tuning |
| Chip Huyen / Eugene Yan | huyenchip.com, eugeneyan.com | Applied-ML essays |

## Tier 3 — Research feeds

| Source | Where | Focus |
|--------|-------|-------|
| arXiv cs.IR | arxiv.org/list/cs.IR/recent | Information retrieval / recsys |
| arXiv cs.LG | arxiv.org/list/cs.LG/recent | Machine learning |
| arXiv cs.CL | arxiv.org/list/cs.CL/recent | NLP / LLMs |
| Papers with Code (trending) | paperswithcode.com | Reproducible SOTA |
| ZenML LLMOps Database | zenml.io/llmops-database | Curated production LLM case studies |

## Aggregators used for discovery

- `eugeneyan/applied-ml` (GitHub) — papers & tech blogs by companies on
  production DS/ML.
- Company post round-ups surfaced via web search (InfoQ, ByteByteGo, daily.dev)
  when the primary domain is unreachable.

## Mining the podcast for episode sources

Each *Snacks Weekly on Data Science* episode breaks down one company blog post,
so its back catalogue (101+ episodes) is itself a source list. The episode
aggregators (Apple, Spotify, podnews, castbox) are egress-blocked, so episode
topics are recovered via web search (`"Snacks Weekly on Data Science" episode
<company>`), then the underlying company article is located and summarised
directly. Entries found this way carry
`discovered_via: "Snacks Weekly on Data Science podcast"` in `index.json`.
The 2026-08-30 batch added Airbnb (map ranking), DoorDash (ETA), Instacart
(marketing bandits), Booking.com (graph fraud), and Uber (Model Excellence
Scores) this way.

## Adding a source

Append a row to the relevant tier with a stable URL and a one-line focus. The
refresh playbook reads this file each run, so new sources are picked up
automatically on the next day.
