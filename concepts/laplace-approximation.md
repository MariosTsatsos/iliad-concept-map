---
title: "Laplace approximation: a Gaussian around the minimum"
kind: concept
days: [15, 17]
origin: notes
by: [claude]
links:
  - to: hessian
    type: needs
    note: "The width of the Gaussian in each direction is set by H."
    proposed: true
    by: claude
  - to: occam-factor
    type: related
    note: "The Laplace approximation is where the (d/2) log n of the BIC comes from."
    proposed: true
    by: claude
  - to: influence-functions
    type: related
    note: "Under the Laplace approximation the leading term of the Bayesian influence function is the classical influence function."
    proposed: true
    by: claude
  - to: degeneracy
    type: related
    note: "It fails in degenerate directions, where H has zeros."
    proposed: true
    by: claude
---
## In one sentence
Approximate the posterior near a minimum by a Gaussian whose spread is set by the Hessian: a sharp bend gives a narrow cloud, a gentle bend a wide one. For a regular model it gives the BIC penalty (d/2) log n (Day 15); used on the Bayesian influence function it gives the classical influence function as the leading term (Day 17).

## Twist
It breaks exactly where neural networks live: where H has a zero the Gaussian has infinite width.

## Why it matters for safety
Tools built on it (the BIC, classical influence functions) inherit its blind spot for degenerate directions.

## Open question


## Quiz
What sets the width of the Gaussian along a direction? (Answer: the inverse of the bend of H along it.)

## Notes


## Sources
- [Day 15 exercise 1.9: BIC via the Laplace approximation](materials/november/day-15-singular-learning-theory/exercise-1-9-bic-via-laplace-approximation.pdf)
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
