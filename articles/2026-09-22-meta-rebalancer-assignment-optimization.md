---
id: meta-rebalancer-assignment-optimization
title: "Open-Sourcing Rebalancer: A Generic, High-Performance Library for Solving Assignment Problems"
source: "Engineering at Meta"
url: "https://engineering.fb.com/2026/09/21/open-source/rebalancer-generic-high-performance-library-assignment-problems/"
published: "2026-09"
added: "2026-09-22"
category: ml-infra-serving
tags: [optimization, assignment-problem, mixed-integer-programming, local-search, infrastructure-scheduling, open-source]
novelty: 4
sourced_via: "web search"
---

# Open-Sourcing Rebalancer: A Generic, High-Performance Library for Solving Assignment Problems

**Source:** [Engineering at Meta](https://engineering.fb.com/2026/09/21/open-source/rebalancer-generic-high-performance-library-assignment-problems/) · Published 2026-09 · Added 2026-09-22
**Category:** ML Infrastructure & Serving · **Tags:** `optimization`, `assignment-problem`, `mixed-integer-programming`, `local-search`, `infrastructure-scheduling`, `open-source`

## TL;DR

Meta open-sourced Rebalancer, a generic library for "assign objects to bins under constraints while optimizing an objective" problems that its infrastructure teams had each been re-solving from scratch — hardware placement, service placement, task scheduling, and traffic routing. It runs roughly 40 million assignment problems a day across more than 30 distinct problem formulations, splitting work between an exact mixed-integer-program solver for small/medium problems and a millions-of-moves-per-second local-search solver for problems too large to solve exactly.

## 1. Business context

Assignment problems — deciding which objects go in which bins, subject to constraints, to optimize some objective — show up constantly in large-scale infrastructure: which racks go in which datacenter, which services run on which servers, which workloads land on which hosts, which users route to which regional datacenter. Historically, each of Meta's infrastructure teams built a bespoke solver for its own version of this problem, re-deriving the same core techniques (translating policy into constraints, choosing between exact and approximate solving, scaling to real fleet sizes) independently. That duplication is expensive in engineering time and makes it hard to improve solving techniques once and have every team benefit. The bet behind Rebalancer is that these problems share enough structure — a common "distribute objects to bins" shape — to be served by one general-purpose, reusable engine instead of N custom ones.

## 2. Technical details

Rebalancer's design centers on a three-layer abstraction:

1. **Specification layer** — modeling constructs (dimensions, partitions, scopes, utilization) let a team describe *their* assignment problem — what the objects and bins are, what constraints apply, what to optimize — without hand-writing solver code.
2. **Expression graphs** — the specification compiles into a directed-acyclic graph representing the objectives and constraints, giving Rebalancer a common intermediate representation regardless of the source problem.
3. **Dual solving strategy** — the same expression graph can be routed to either of two solvers depending on problem size:
   - An **optimal solver** that converts the graph into a mixed-integer program (MIP) and hands it to a commercial or open-source MIP solver — used when problems are small/structured enough to solve exactly.
   - A **local-search solver** that starts from a current assignment and explores neighborhoods of alternative assignments, evaluating on the order of millions of candidate moves per second — used for the NP-hard, fleet-scale problems that no commercial solver can crack in reasonable time.

This lets Rebalancer serve both ends of the spectrum — small, high-stakes problems where an exact optimum matters, and huge fleet-scale problems where a fast, good-enough local search is the only tractable option — through one shared abstraction rather than two disconnected tools.

Concrete internal consumers named in the post include Meta's Shard Manager, RAS, and Taiji systems, spanning hardware placement (racks to datacenters), service placement (servers to services), task placement (workloads to servers), and traffic routing (users to geographically distributed datacenters).

## 3. Impact — potential & realized

**Realized:** Rebalancer runs roughly **40 million assignment problems per day** across **30+ distinct problem formulations** inside Meta. For large problems (265k objects, 3.2k bins), the local-search solver hits a **P99 solve time of 12 seconds**; for the largest tier (>1M objects, 5k bins) average solve time is **171 seconds** across **3,400+ monthly runs**.

**Potential:** by open-sourcing the library, Meta is betting the same "generic assignment engine" pattern generalizes beyond its own infra — any organization solving repeated placement/scheduling problems (capacity planning, ML training job scheduling, marketplace matching) could adopt one engine instead of building bespoke solvers per use case, and benefit from solver improvements landing once rather than per-team.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — a strong production-first unification of a well-known problem class

Assignment/bin-packing problems and the MIP-vs-local-search tradeoff are textbook operations research, not new theory. What's genuinely valuable here is the systems contribution: building one abstraction (expression graphs) expressive enough to unify racks-to-datacenters, servers-to-services, workloads-to-hosts, and users-to-datacenters — four superficially different problems — under a single specification-and-solving pipeline that Meta runs 40M times a day. That kind of "collapse N bespoke solvers into 1 general engine, validated at real fleet scale" contribution is exactly the sort of production-first systems work that tends to get copied once it's public, especially by any company juggling multiple placement/scheduling problems across teams.

### Similar / related work

- General mixed-integer programming and local-search literature (OR-Tools, Gurobi, CP-SAT) — the classical toolkit Rebalancer builds a generic front-end over; left unlinked as broad prior art rather than one paper.
- [**Machine-Learning Predictive Autoscaling for Flink**](2026-09-21-grab-ml-predictive-autoscaling-flink.md) (in this bank) — a narrower, single-purpose instance of the same "predict then allocate resources" family of problems that Rebalancer aims to generalize across many use cases at once.
- [**KernelEvolve: How Meta's Ranking Engineer Agent Optimizes AI Infrastructure**](2026-09-18-meta-kernelevolve-ranking-engineer-agent-infra.md) (in this bank) — another Meta infrastructure-optimization system, but attacking a different problem (GPU kernel generation) with a different technique (LLM-driven search) rather than combinatorial assignment.

### Jargon buster

- **Assignment problem** — a class of optimization problems where the task is to match objects to slots ("bins") under constraints while optimizing some objective, e.g., matching workloads to servers or hardware to datacenters.
- **Mixed-integer program (MIP)** — an optimization formulation combining continuous and integer-valued decision variables; solved exactly by dedicated MIP solvers, but scales poorly as problem size grows.
- **Local search** — an optimization technique that starts from a valid (if imperfect) solution and repeatedly tries small changes ("moves") that improve it, trading a guarantee of optimality for the ability to handle far larger problems than exact solvers can.
- **NP-hard** — a class of problems believed to have no algorithm that solves all instances quickly (in polynomial time) as they grow large, meaning practical solutions often rely on approximation or heuristics rather than guaranteed-optimal exact solving.
