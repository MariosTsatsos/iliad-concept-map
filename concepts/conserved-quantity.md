---
title: "Symmetry gives a conserved quantity"
kind: concept
days: [16]
origin: notes
by: [claude]
aliases: ["Noether", "conservation law", "balanced"]
links:
  - to: gradient-flow
    type: needs
    proposed: true
    by: claude
  - to: degeneracy
    type: related
    note: "The symmetry that gives a conserved quantity also gives a flat direction of the loss, a zero of the Hessian."
    proposed: true
    by: claude
---
## In one sentence
If the network's function does not change under some transformation of the weights, gradient flow keeps a matching quantity fixed. Example: f(α θ1, θ2/α) = f(θ1, θ2) (scale one layer up and the next down) conserves ‖θ1‖² − ‖θ2‖². Where training ends depends on where it started.

## Twist
This is Noether's theorem of physics in a new place: a symmetry of the loss gives a conserved charge. Finite steps, mini-batches and momentum break the conservation slightly.

## Why it matters for safety
Conserved quantities fix part of the final weights from the initialisation alone, one reason why the starting point matters.

## Open question


## Quiz
For f(x) = w2 w1 x, what does gradient flow conserve? (Answer: w2² − w1².)

## Notes


## Sources
- [Day 16 slides: introduction to training dynamics](materials/november/day-16-training-dynamics/intro-training-dynamics.pdf)
- [Day 16 exercise sheet](materials/november/day-16-training-dynamics/exercise-sheet.pdf)
- [Kunin et al., Neural mechanics: symmetry and broken conservation laws (ICLR 2021)](https://arxiv.org/abs/2012.04728)
