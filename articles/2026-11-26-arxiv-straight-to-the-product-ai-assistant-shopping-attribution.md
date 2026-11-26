---
id: arxiv-straight-to-the-product-ai-assistant-shopping-attribution
title: "Straight to the Product: What Online Retailers Miss When Shoppers Ask AI First"
source: "Scrunch AI (arXiv cs.IR)"
url: "https://arxiv.org/abs/2611.20378"
published: "2026-11"
added: "2026-11-26"
category: product-analytics
tags: [marketing-attribution, ai-shopping-assistants, referral-traffic, consumer-panel, llm-as-judge, product-follow-through, customer-journey, observational-study]
novelty: 4
sourced_via: "full-text fetch"
discovered_via: "arXiv listing (backlog stub)"
---

# Straight to the Product: What Online Retailers Miss When Shoppers Ask AI First

**Source:** [Scrunch AI (arXiv cs.IR)](https://arxiv.org/abs/2611.20378) · Published 2026-11 · Added 2026-11-26
**Category:** Product Analytics & Metrics · **Tags:** `marketing-attribution`, `ai-shopping-assistants`, `referral-traffic`, `consumer-panel`, `llm-as-judge`, `product-follow-through`, `customer-journey`, `observational-study`

## TL;DR

The authors link the same people's AI-assistant conversations to their later browsing at twenty large online retailers. Shoppers go to the product the assistant named: within a day, visits to the named product rise from 0.02 to 2.07 per 100 answers. But 89% of visits after a recommending answer carry no sign of the assistant's link, and 54% follow a web search, so the store logs ordinary search traffic. They propose **product follow-through** as a behavioral metric for shopping assistants that needs no referral data or provider logs.

## 1. Business context

Retailers measure AI assistants mostly through referral reports: sessions that arrive with a ChatGPT-style referrer. The paper's question is what those reports miss. A shopper may ask an assistant, get a product name, type it into a search engine and land on the product page. The store records a search visit. The conversation leaves no trace (the authors compare this gap to branded search ads, citing Blake et al. 2015).

Prior work saw one side of this. Shopping-assistant evaluations mostly stop at the answer (simulated users, simulated stores, expert rubrics). Generative engine optimization studies how products get named in answers. Referral studies see only sessions that carry a referral. The authors' own earlier panel work linked assistant recommendations to later *brand* searches and visits. This paper goes down to the product and follows the same people across sites, with or without a referral.

## 2. Technical details

- **Data.** An opt-in consumer panel in two English-speaking markets records visited web pages and, for the same people, conversations with ChatGPT, Gemini, Claude, Perplexity and Grok.
  - Main period: July–October 2026. Replication: February–June 2026, with the core analysis plan committed before its data were pulled.
  - Panel size and per-cell sample sizes are not reported (commercially sensitive). All intervals are 95%, from a bootstrap that resamples people (Wilson intervals for label validation).
- **Unit of analysis.** For each person and each of twenty retailers, the first answer that names the store.
  - The main group keeps answers where the assistant, not the person, first named the store, for people with no visit to that store in the past week.
- **LLM judges.** Two classification tasks on one underlying model, each picking among written options.
  - *Answer-type judge*: names a specific product, suggests the store for the need, or only mentions it. The first two count as "recommending".
  - *Product-match judge*: reads answer excerpts plus visited pages (title and URL). Size, color and pack variants count as a match; a same-kind product does not.
- **Three comparisons, each for a different alternative explanation.**
  - Earlier-week baseline: the same person's visits to the store 14, 21 and 28 days earlier (habits at the store).
  - Swapped answer: someone else's answer naming the same store, same month, request type, country and category; the judge is blind to whose answer it is (store's popular products).
  - Matched moments: same person and store, same three-hour time slot, weekday/weekend, recent activity and past-week visit status, no answer within a day (general online busyness, after Lewis et al. 2011). Around these moments store visits dip 0.8 points.
- **Label validation.**
  - Two other frontier models, where they agree, confirm 96% of post-answer matches and 64% of baseline matches, and agree with the answer-type judge on 83%.
  - A blind reader audited 160 match items: 93% [86, 97] of 90 post-answer matches confirmed, 54% [39, 68] of 39 baseline matches.
  - Adjusting for precision leaves the named-product rise at 1.9 points vs 2.0 unadjusted.
  - On 102 balanced answers the reader agreed with the answer-type judge 75% [65, 82]. Its errors run one way (29% of "recommending" called mentions), which would shrink the recommending rises, not inflate them.
- **Route classification.** A visit "comes through the link" if it carries an AI referrer or AI marker in its address. It "follows a web search" if it has a search referral, a search ad, or a search in the prior 30 minutes. Remaining visits are typed/direct, or from another site or a reopened tab.
- **Product follow-through (the proposed metric).** The share of answers naming a specific product followed within 24 hours by a visit to that product's page at the named store. It is counted over every such answer and compared with the earlier-week baseline. It needs only answer text and later page views.

## 3. Impact — potential & realized

**Measured.**
- *Product match.* On days with a product-page visit at the named store, 44% show a product from the shopper's own answer vs 1.5% for a matched answer given to someone else. Replication: 42% vs 1.2%.
- *Follow-through.* 2.07 vs 0.02 per 100 answers, +2.0 points [1.7, 2.4]; earlier period +2.2 [1.9, 2.6].
  - The ratio to baseline grows with specificity: store visits ×2.8, product-name searches about ×24, named-product visits about ×100.
  - A store suggestion adds 2.7 points [2.0, 3.5] more store visits than a bare mention, which adds under one visit per 100 answers.
  - Only 8% of matched products were named by the shopper earlier; without them the rise is 1.9 [1.5, 2.2].
  - Against matched moments, paired answer by answer, the rise is 3.1 points [2.5, 3.6] larger (a more active subset). Robust to counting each person once (2.3), dropping the top 5% of users (2.4), dropping the largest retailer (2.2) and splitting the period (2.1, 2.0).
  - By assistant: +2.2 [1.8, 2.7] after ChatGPT answers, +1.0 [0.5, 1.6] after Gemini.
  - Answers quoting a price near the store name go with a larger rise (+0.93 [0.19, 1.63]). Naming one vs several products, or linking to the store, makes no detectable difference.
- *Attribution gap.* Of 100 visits after a recommending answer, 11 come through the link (2 in usual visits), and 54 follow a web search (55% usually). Search visits double, from 56 to 110 per 1,000 answers. Counting only extra visits, 81% still show no link.
  - Shoppers with no visit in the past week used the link 27% of the time vs 12% for recent visitors (+14.7 [11.9, 17.6]).
  - A search in the 30 minutes before the first visit names the answer's product 28% of the time (1% in earlier weeks). Half of first visits come within 19 minutes.
  - Total searching shows no detectable drop (+3% [−6, 11]).
- *At the store.* The named product is the visit's first page 34% of the time, other products 18%.
  - Visits open on a product page 39.3% vs 36.7%.
  - Two or more products are viewed in 31.4% vs 26.2% of visits (+5.2 [3.0, 7.4]; earlier +4.3).
  - Use of the store's recommendations is about as usual (14.5% vs 13.4%).
- **Stated limitations.** The study is observational. The causal reading rests on one assumption: without the answer, visits would follow the earlier weeks and the matched moments. At-store and route results are descriptive. There are no purchase data. The main group was chosen after first results; its store-visit rise (+5.1) is smaller than over all store-naming answers (+10.5). The scope is two markets, twenty retailers, February–October 2026.

**Potential.**
- Retailers: report assistant referrals next to search and direct product-page arrivals, and track product-name queries in search-console data. Link-only reporting captures about one in nine visits after a recommending answer.
- Assistant and agent builders: follow-through can be computed per assistant without provider logs.
- Open questions the authors name: purchase outcomes, a randomized test of which product the assistant names, and measuring follow-through on agent purchases.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A measurement result every e-commerce attribution team should know about

The core finding is a dark-funnel result: AI assistants influence product choice, and the evidence lands in the "organic search" bucket. Practitioners have suspected this. Few have had cross-site, same-person data to show it at product level. The design is careful for an observational panel. Three comparisons each rule out a named alternative, there is a pre-committed replication period, and the LLM-judge labels are validated with a blind human audit and an error-direction argument. The follow-through metric is simple. That is a strength: it is the kind of number a retailer or assistant team can actually adopt.

Caveats. The authors are from Scrunch AI, which sells AI-visibility tooling, so the "you are under-counting AI" conclusion is commercially convenient for them. The design does not look slanted, though. Panel size is withheld, which makes external power checks impossible. The main group was picked after first results, as they disclose. And page views are not purchases. For attribution teams, my practical read is that "AI referral share" in web analytics is a strong lower bound. Incrementality would need a holdout or the randomized naming test the authors propose. Branded-search ad lift studies (Blake et al.) are the right mental model.

### Similar / related work

- [**From Prompt to Purchase: How AI Brand Recommendations Move Consumers on the Open Web**](https://arxiv.org/abs/2606.10907) — the same authors' earlier panel study linking assistant brand recommendations to later searches and site visits; this paper goes down to the product level.
- **Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment** — Blake, Nosko & Tadelis (Econometrica 2015); eBay's field experiments showing that branded search ads largely capture visits that would arrive anyway. The analogy the authors use for where a decision is made vs where it is recorded.
- [**E-GEO: A Testbed for Generative Engine Optimization in E-Commerce**](https://arxiv.org/abs/2511.20867) — studies how products get named in LLM answers; this paper measures what happens after they are named.
- [**UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents**](2026-10-23-arxiv-userarena-user-simulation-shopping-agents.md) (in this bank) — evaluates shopping agents with simulated users. Follow-through is a behavioral, real-user counterpart.

### Jargon buster

- **Referral traffic** — visits whose referrer or URL marker shows they came from a specific site, such as an AI assistant. Analytics tools attribute the visit to that source.
- **Product follow-through** — the share of answers naming a specific product that are followed within 24 hours by a visit to that product's page at the named store.
- **Earlier-week baseline** — the same person's visits to the store 14, 21 and 28 days before, averaged. It is a self-comparison that controls for habits.
- **Matched moments** — placebo time points for the same person and store, at a similar time and activity level, with no assistant answer. They test whether busy people simply browse more.
- **LLM judge** — a language model used as a classifier to label data, here answer type and product match. Its labels are checked against other models and a blind human reader.
- **Dark funnel** — influence on a purchase journey that happens in channels the seller's analytics cannot observe.
