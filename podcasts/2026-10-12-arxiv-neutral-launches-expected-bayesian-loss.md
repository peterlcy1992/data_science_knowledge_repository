# Neutral Launches — Measuring the Downside Risk

A deep dive into a new stat.AP paper on a question every experimentation team faces: when a launch is meant to be neutral, such as an infrastructure upgrade or migration, how do you know it did no harm? Checking whether confidence intervals overlap is too permissive when data are scarce and too strict when data are abundant. The authors propose Expected Bayesian Loss, a continuous risk score computed from ordinary frequentist estimates that captures both how likely a metric is to degrade and how bad the degradation would be, and that penalises noisy, high-variance experiments. We walk through the idea, how it works as a tunable guardrail, and the open questions about calibrating the loss scale.

Source article: "Neutral Is Not Free: Evaluating Downside Risk in Neutral Launches" — arXiv stat.AP (Alcain, Kang, Garrard, Veits, Nassif, Zaidi), https://arxiv.org/abs/2610.10223 (published 2026-10).
