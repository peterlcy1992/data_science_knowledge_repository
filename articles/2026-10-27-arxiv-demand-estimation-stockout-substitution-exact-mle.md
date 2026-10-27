---
id: arxiv-demand-estimation-stockout-substitution-exact-mle
title: "Demand Estimation with Unobserved Stockout Substitution: Exact Likelihood Maximization"
source: "arXiv stat.ME (Wang, Jiang & Chen)"
url: "https://arxiv.org/abs/2610.34547"
published: "2026-10"
added: "2026-10-27"
category: statistical-modeling
tags: [demand-estimation, multinomial-logit, maximum-likelihood, censored-demand, stockouts, retail]
novelty: 4
sourced_via: "full-text fetch"
---

# Demand Estimation with Unobserved Stockout Substitution: Exact Likelihood Maximization

**Source:** [arXiv stat.ME (Wang, Jiang & Chen)](https://arxiv.org/abs/2610.34547) · Published 2026-10 · Added 2026-10-27
**Category:** statistical-modeling · **Tags:** `demand-estimation`, `multinomial-logit`, `maximum-likelihood`, `censored-demand`, `stockouts`, `retail`

## TL;DR

When inventory is only counted at replenishment, stockout times are unobserved and so is which products each customer could buy. For the multinomial logit model the paper shows the exact likelihood and its gradient of each selling period are one-dimensional integrals, evaluable at cost linear in products and periods; it reports estimating demand for 2,000 products from 2,000 selling periods in under ten minutes on one GPU.

## 1. Business context

A retailer (the paper's running example is a vending machine; the same data structure arises in unmanned and traditional stores) restocks products periodically and sees only initial inventory and terminal sales per selling period. When a product sells out, customers who preferred it may buy a substitute or leave, so observed sales understate the demand for sold-out items and overstate it for substitutes. Estimating demand under this stockout substitution has been hard since Anupindi et al. (1998), and the problem grows with assortment size. In the paper's small example (three products, eight customers) 1,680 purchase sequences are consistent with the same terminal sales, and their likelihoods differ.

## 2. Technical details

The paper builds on the continuous-time representation of the MNL purchase process as independent Poisson processes (Zhou et al. 2026) and uses it to compute the probability of a whole vector of terminal sales. Its main finding is that, for each selling period, the exact likelihood is a one-dimensional integral however many products, customers or stockouts there are, and so is the gradient of the log-likelihood; evaluation costs scale linearly with the number of products and periods. The purchase sequences are integrated out analytically rather than enumerated, sampled or approximated. Both known and Poisson-distributed customer arrivals are handled. Prior approaches the paper contrasts: EM (Anupindi et al. 1998, exact for up to two stockouts per period; Conlon and Mortimer 2013, up to three), Bayesian data augmentation (Musalem et al. 2010; Wan et al. 2018), and sampling of stockout orders (Shao and Kleywegt 2020, SK-SAA), which trades cost against simulation error or approximation bias.

## 3. Impact — potential & realized

Realized (simulation, as reported): on one NVIDIA RTX 5090 GPU the average time per gradient iteration for N=500 customers, J=100 products and Q=128 quadrature nodes is about 0.038 s (known arrivals) and 0.080 s (Poisson arrivals). The paper reports estimating demand for 2,000 products from 2,000 selling periods in under ten minutes, whereas no other benchmark completes much smaller instances within its 600-second limit; the Bayesian data-augmentation benchmark takes several minutes even with ten products. Benchmarks are Naive MNL (ignores assortment changes), SK-SAA and DA-MCMC, scored by relative RMSE of the estimated preference parameters. Potential: demand models that can be fit on assortments of hundreds or thousands of products without approximation error. Scope: the result is for MNL; the paper positions it as a complete solution for that model, not for richer choice models. All reported evidence is simulation-based.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 4/5 — A genuinely exact, scalable likelihood for a classic censored-demand problem, resting on one neat representation.

Anyone estimating demand from sales when stock-outs censor it knows the usual compromise: ignore substitution or accept a sampling approximation. An exact likelihood that is cheap changes that trade-off for MNL-style models. The caveat for practitioners is that real shoppers often violate the MNL independence-of-irrelevant-alternatives assumption, and the paper's validation is simulated.

### Similar / related work

- [**Hierarchical GTV Estimation: Bridging the Gap between Container-Level Ranking and Item-Level Conversion**](2026-10-26-meituan-hierarchical-gtv-estimation-hge.md) (in this bank) — another case of decomposing an observed outcome into latent choice components

### Jargon buster

- **Multinomial logit (MNL)** — A choice model where the chance a customer picks an available product is proportional to exp(utility) among available options.
- **Stockout substitution** — Demand shifting to other products (or being lost) when a preferred product is sold out.
- **Terminal sales** — Units of each product sold by the end of a selling period, the only sales information observed.
- **Exact likelihood** — The probability of the observed data computed without sampling or approximation.
