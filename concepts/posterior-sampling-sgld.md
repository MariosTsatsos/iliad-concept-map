---
title: "Posterior sampling with SGLD"
kind: concept
days: [17]
origin: notes
by: [claude]
aliases: ["SGLD", "Langevin", "posterior"]
links:
  - to: boltzmann-distribution
    type: needs
    note: "The weighted posterior is a Boltzmann (Gibbs) distribution with the loss as energy."
    proposed: true
    by: claude
  - to: bayes-vs-sgd
    type: related
    note: "SGLD is SGD with the noise chosen on purpose."
    proposed: true
    by: claude
---
## In one sentence
Stochastic gradient Langevin dynamics (SGLD) adds calibrated Gaussian noise to SGD updates. Repeated, the weights wander through the low-loss region and visit it in proportion to the posterior, so averages over the samples estimate posterior averages and covariances, which is what the Bayesian influence function needs.

## Twist
The same noisy step as SGD; what differs is that the noise is set so that the walk samples the posterior.

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
- [Day 17 slides: data attribution](materials/november/day-17-data-attribution/data-attribution-slides-24-nov.pdf)
