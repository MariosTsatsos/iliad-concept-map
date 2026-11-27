---
title: "Gradient flow"
kind: concept
days: [16]
origin: notes
by: [claude]
links:
  - to: training-dynamics
    type: related
    note: "The idealised training process that Day 16 solves."
    proposed: true
    by: claude
  - to: three-temperatures
    type: related
    note: "Gradient flow is the zero-temperature limit of SGD: no step size, no noise."
    proposed: true
    by: claude
---
## In one sentence
Gradient descent with an infinitely small step: the weights move continuously downhill, dθ/dt = −∇L(θ). It turns training into a differential equation that can be solved or analysed with the tools of physics.

## Twist
Shrinking the step to zero removes the noise and the step size; what remains is the geometry of the loss surface. Finite steps and mini-batches are then studied as corrections.

## Why it matters for safety


## Open question


## Quiz
Write gradient flow for one weight with L(w) = ½ w². (Answer: dw/dt = −w, so w(t) = w(0) e^(−t).)

## Notes


## Sources
- [Day 16 slides: introduction to training dynamics](materials/november/day-16-training-dynamics/intro-training-dynamics.pdf)
- [Kunin et al., Neural mechanics: symmetry and broken conservation laws (ICLR 2021)](https://arxiv.org/abs/2012.04728)
