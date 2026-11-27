---
title: "Localised posterior: keep the cloud near the trained weights"
kind: concept
days: [17]
origin: notes
by: [claude]
aliases: ["gamma", "localised BIF"]
links:
  - to: bayesian-influence-function
    type: needs
    proposed: true
    by: claude
  - to: damping
    type: related
    note: "γ in the Bayesian influence function plays the role of λ in the damped influence function."
    proposed: true
    by: claude
---
## In one sentence
The full posterior is too hard to sample and is not about the checkpoint we care about, so it is localised: add a penalty (γ/2)‖w − w*‖² that keeps the samples near the trained weights w*. In the Bayesian influence function γ plays the role that the damping λ plays in the classical one.

## Twist
The answer depends on the knobs: γ, the SGLD step size, the chain length and the number of chains (Day 17 slides).

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
- [Day 17 slides: data attribution](materials/november/day-17-data-attribution/data-attribution-slides-24-nov.pdf)
- [Kreer et al., Bayesian influence functions for Hessian-free data attribution (2026)](https://arxiv.org/abs/2509.26544)
