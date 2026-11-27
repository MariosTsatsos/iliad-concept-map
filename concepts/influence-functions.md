---
title: "Influence functions"
kind: concept
days: [17]
origin: notes
by: [MT, claude]
aliases: ["IF", "influence function"]
plot:
  - title: "Four shapes of a loss surface"
    file: hessian-shapes.html
  - title: "How one example's weight moves the minimum"
    file: beta-landscape.html
links:
  - to: hessian
    type: needs
    note: "The formula inverts H."
    proposed: true
    by: claude
  - to: leave-one-out
    type: needs
    note: "A first-order approximation to leave-one-out retraining."
    proposed: true
    by: claude
  - to: data-attribution
    type: eg
    note: "One of the three methods of Day 17."
    proposed: true
    by: claude
---
## In one sentence
A first-order approximation to leave-one-out: how the trained weights w* move when example i's weight β_i changes, −H⁻¹∇L_i, and how an observable φ moves, I(z_i, φ) = −∇φᵀ H⁻¹ ∇L_i. Read it as: the pull of example i (its gradient), resisted by the stiffness of the surface (H⁻¹), seen through what you measure (∇φ).

## Twist
The classical derivation assumes a unique minimum and an invertible H. Neither holds for a neural network, which is not even trained to convergence.

## Why it matters for safety
The main tool for asking which training data produced a behaviour of a large model.

## Open question


## Quiz
In −∇φᵀ H⁻¹ ∇L_i, which factor is small when the surface is steep? (Answer: H⁻¹.)

## Notes
MT's words (Notion, Day 17): a formal way to quantify how much a particular input data influences training and an observed behaviour. The notes: classical influence functions give a first-order approximation to the change in a point estimate w* when the training data is perturbed.

## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
- [Day 17 slides: data attribution](materials/november/day-17-data-attribution/data-attribution-slides-24-nov.pdf)
- [Koh and Liang, Understanding black-box predictions via influence functions (2017)](https://arxiv.org/abs/1703.04730)
