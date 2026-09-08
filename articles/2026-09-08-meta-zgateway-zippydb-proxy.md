---
id: meta-zgateway-zippydb-proxy
title: "ZGateway: Learnings from Putting a Proxy in Front of ZippyDB"
source: "Engineering at Meta"
url: "https://engineering.fb.com/2026/09/03/core-infra/zgateway-proxy-zippydb-meta/"
published: "2026-09"
added: "2026-09-08"
category: data-engineering
tags: [database-proxy, connection-scaling, load-shedding, tenant-isolation, service-mesh, reliability]
novelty: 3
sourced_via: "web search"
---

# ZGateway: Learnings from Putting a Proxy in Front of ZippyDB

**Source:** [Engineering at Meta](https://engineering.fb.com/2026/09/03/core-infra/zgateway-proxy-zippydb-meta/) · Published 2026-09 · Added 2026-09-08
**Category:** Data Engineering · **Tags:** `database-proxy`, `connection-scaling`, `load-shedding`, `tenant-isolation`, `service-mesh`, `reliability`

## TL;DR

Meta built ZGateway, a stateless proxy tier in front of ZippyDB (its distributed key-value store), to break the unsustainable many-to-many connection mesh between over a million client hosts and the database fleet. It now carries 1B+ ops/sec and about 40% of all ZippyDB traffic at roughly 6% overhead, cutting per-host connection counts by ~97–98% and total persistent connections by ~19x, while a tested overload scenario showed the system shedding traffic from only 6 of ~1,350 tenant buckets while the rest kept 99.9%+ request success.

## 1. Business context

ZippyDB is accessed directly by client hosts across hundreds of teams at Meta — over a million of them. Direct access meant a dense many-to-many mesh of TLS connections: each database host could face tens of thousands of inbound connections, and each client held tens of thousands of outbound ones, the large majority idle but still consuming memory, CPU, and file descriptors on both ends. That architecture created cascading failure risk: a routing bug once caused every client to open a connection per shard, database hosts breached their file-descriptor limits, and the fleet fell into a reboot loop. Because client population and database fleet size both grow independently and rapidly, the direct-connection model had no natural ceiling — the fix was to decouple the two sides with a proxy tier that absorbs the connection fan-in.

## 2. Technical details

ZGateway is a **stateless proxy tier** discovered through ServiceRouter, Meta's internal hyperscale service mesh, with several purpose-built subsystems:

- **Connection management & routing.** Clients hold sticky regional connections to ZGateway instead of connecting directly to database hosts. ZGateway terminates TLS, applies per-tenant admission control, resolves shard locations, and routes to the correct replica — while deliberately leaving TLS handling to the existing Thrift/ServiceRouter layer and key-to-shard mapping to the existing shard locator, rather than reimplementing either.
- **Request batching & coalescing.** Requests from unrelated callers bound for the same backend destination are merged into single backend RPCs; identical concurrent key requests are coalesced into a single fetch, preventing hot-key stampedes. Batches flush on a linger window, a size threshold, or a request-count threshold, with idle eviction and in-flight caps as safety valves.
- **Tenant isolation & admission control.** Discriminant Load Shedding (DLS) buckets each request by tenant and priority; buckets drain round-robin so one misbehaving tenant's excess load gets shed without affecting others. CPU concurrency is governed by an AIMD (additive-increase/multiplicative-decrease) feedback loop, with an analogous mechanism protecting memory.
- **Load balancing.** A control-plane balancer normalizes per-host CPU utilization against the tier average and adjusts ServiceRouter routing weights accordingly; Meta is moving toward classifying tier states (steady drift, task churn, hot outliers, regional skew) and matching balancing strategy to the detected state.
- **Cross-region resilience.** Global routing tables spanning regions, "mega-regions" grouping geographically close regions, and explicit backup-ring declarations together give ZGateway controlled failover paths during regional issues.
- **Caching.** Hot reads are served from in-process caches with live invalidation via change-data-capture streams; per-key fill locks collapse thundering herds into a single backend fetch while preserving bounded-staleness correctness guarantees.

## 3. Impact — potential & realized

**Realized — scale:** ZGateway handles more than 1 billion operations per second and carries roughly 40% of all ZippyDB traffic today, with Meta projecting it will exceed 60%, at approximately 6% average computational overhead.

**Realized — connection reduction:** model-based estimates put per-host connection-count reduction at roughly 97–98%, and total persistent connections across the system drop by roughly 19x, since each backend connection now multiplexes many clients. Critically, database-host fan-in becomes independent of client population growth — it's now bounded by region count and shard density, both of which operators control directly, rather than by however many client hosts happen to exist.

**Realized — admission control under load:** in a controlled overload test exceeding 90% CPU across roughly 1,350 active tenant buckets, only 6 buckets actually had traffic shed; the remaining ~1,344 executed 99.9% of requests with zero rejections, and overall goodput stayed near 97–98% while the admission-control machinery itself consumed about 8% of CPU.

**Potential:** Meta names three future directions — agent-operated heuristics to replace hand-tuned control loops, co-locating gateway components next to ZServer hosts for latency-critical workloads while preserving the fleet decoupling that motivated ZGateway in the first place, and splitting ZGateway's own responsibilities across separate fault domains with independent lifecycles.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Not ML, but a rigorously quantified infra pattern worth knowing

This is core infrastructure engineering rather than applied ML or data science, kept in this bank as a lower-priority but genuinely useful lead: the proxy-in-front-of-a-distributed-database pattern itself is well established (similar to connection-pooling proxies like PgBouncer, or Meta's own prior work like Tao and Mcrouter for other data stores). What earns this a 3 rather than lower is the specificity and honesty of the numbers — a real production overload test with a named tenant-bucket count and named goodput figures, not just an architecture diagram. Any team running an ML feature store or serving layer behind a distributed database at real scale will recognize the exact failure mode (connection-count growth outpacing database fleet growth) that motivated this.

### Similar / related work

- [**Meta — SilverTorch: Index as Model, a New Retrieval Paradigm**](2026-09-04-meta-silvertorch-index-as-model-retrieval.md) (in this bank) — a different Meta infra rethink from the same broader period, collapsing a multi-service retrieval stack into one GPU-native model rather than adding a proxy layer in front of existing services.
- [**Databricks — How Databricks Feature Store Serves Features with Sub-Second Freshness**](2026-08-30-databricks-feature-store-subsecond-freshness.md) (in this bank) — a complementary problem (serving ML features at low latency and scale) that runs into similar connection- and load-management challenges as ZGateway addresses for ZippyDB.
- [**Coinbase — How Coinbase Builds Sequence Features for Machine Learning**](2026-09-07-coinbase-sequence-features-ml.md) (in this bank) — another data-infrastructure piece on scaling a streaming/serving data layer, useful as a contrast in how different companies handle fan-out and freshness trade-offs.

### Jargon buster

- **Stateless proxy** — a proxy layer that holds no client-specific session state itself, so any proxy instance can handle any request, making the tier easy to scale horizontally and fail over.
- **AIMD (additive-increase/multiplicative-decrease)** — a feedback-control algorithm (the same family used by TCP congestion control) that increases a resource limit gradually but cuts it sharply on signs of overload.
- **Thundering herd** — a failure pattern where many concurrent requests for the same uncached data all miss the cache simultaneously and hit the backend at once; "fill locks" prevent this by letting only one request fetch while others wait for its result.
- **Fan-in / fan-out** — the number of connections converging on (fan-in) or spreading out from (fan-out) a single node in a distributed system; ZGateway's core goal is reducing fan-in on database hosts.
