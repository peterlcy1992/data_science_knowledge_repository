---
id: arxiv-next-best-action-causal-constrained-offline-rl
title: "Next Best Action: Causal Constrained Offline RL for Business Action Targeting"
source: "arXiv cs.LG (Ramachandiran, Li, Mancilla-Caceres, Ye & Liu; RecSys 2026 OARS workshop)"
url: "https://arxiv.org/abs/2610.26817"
published: "2026-10"
added: "2026-10-20"
category: personalization-recsys
tags: [offline-rl, cmdp, causal-correction, coupon-targeting, off-policy-evaluation]
novelty: 3
sourced_via: "web search"
---

# Next Best Action: Causal Constrained Offline RL for Business Action Targeting

**Source:** [arXiv cs.LG (Ramachandiran, Li, Mancilla-Caceres, Ye & Liu; RecSys 2026 OARS workshop)](https://arxiv.org/abs/2610.26817) · Published 2026-10 · Added 2026-10-20
**Category:** personalization-recsys · **Tags:** `offline-rl`, `cmdp`, `causal-correction`, `coupon-targeting`, `off-policy-evaluation`

## TL;DR

Frames next-best-action targeting as a constrained MDP solved as a linear program with off-policy causal correction of customer dynamics, giving shadow prices for business constraints; offline evaluation on rideshare coupons estimates +19% LTV over the behavior policy and +8% over a myopic baseline.

## 1. Business context

Choosing discounts and lifecycle messages must maximise long-term value under budgets and fairness/welfare constraints while being causally grounded, which the authors say existing methods do not do jointly.

## 2. Technical details

Customer states are RFM stages; dynamics are estimated from a temporal holdout with off-policy causal correction embedded in the CMDP's LP formulation. The LP's shadow prices quantify trade-offs of constraints. Demonstrated action space is binary (coupon or not); evaluation is model-based off-policy evaluation.

## 3. Impact — potential & realized

Reported: +19% estimated LTV over the behavior policy, +8% over a myopic baseline, under the observed coupon budget. These are model-based estimates, not live results; single rideshare case.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — Putting causal correction inside the LP and surfacing shadow prices is a tidy combination for decision science, but the validation is purely offline with a binary action, so its value rests on the quality of the estimated dynamics.

Putting causal correction inside the LP and surfacing shadow prices is a tidy combination for decision science, but the validation is purely offline with a binary action, so its value rests on the quality of the estimated dynamics.

### Similar / related work

- [**Conformal Policy Selection**](2026-10-19-arxiv-conformal-policy-selection-fdr-deployment.md) (in this bank) — a per-unit safety gate for targeting policies
- [**Prediction-Powered Data Fusion for Treatment Effect Estimation**](2026-10-09-arxiv-prediction-powered-data-fusion-treatment-effects.md) (in this bank) — causal estimation feeding decision policies

### Jargon buster

- **CMDP** — A Markov decision process with constraints on expected costs, such as a coupon budget.
- **Shadow price** — How much the objective would improve if a constraint were relaxed by one unit; read off the LP dual.
- **Model-based OPE** — Estimating a policy's value by simulating it in a learned model of the environment.
