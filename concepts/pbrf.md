---
title: "Proximal Bregman response: what influence functions really answer"
kind: concept
days: [17]
origin: notes
by: [claude]
aliases: ["PBRF", "proximal Bregman response function"]
links:
  - to: damping
    type: needs
    proposed: true
    by: claude
  - to: gauss-newton
    type: needs
    proposed: true
    by: claude
  - to: leave-one-out
    type: related
    note: "Practical influence functions approximate the PBRF, not leave-one-out."
    proposed: true
    by: claude
---
## In one sentence
Bae et al. (2022) show that the influence function used in practice, −∇φᵀ(G + λI)⁻¹∇L_i, is the exact first-order answer to a different question: retrain from w*, penalise any change of the network's outputs on the training set and any move of the weights, and reweight example i. The answer to that question is the proximal Bregman response function (PBRF).

## Twist
In their words: if influence functions are the answer, the question is the PBRF, not leave-one-out retraining.

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
- [Bae et al., If influence functions are the answer, then what is the question? (2022)](https://arxiv.org/abs/2209.05364)
