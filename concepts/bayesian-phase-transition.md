---
title: "Bayesian phase transition"
kind: concept
days: [15]
origin: notes
by: [claude]
links:
  - to: free-energy-formula
    type: needs
    proposed: true
    by: claude
  - to: latent-heat-plateau
    type: related
    note: "A participant's analogy for plateaus; here the jump is in the posterior as data grows."
    proposed: true
    by: claude
  - to: saddle-to-saddle
    type: related
    note: "Day 16's plateaus and drops are jumps in time during training; these are jumps in the posterior as n grows. Whether they are the same jumps is the question of Bayes compared to SGD."
    proposed: true
    by: claude
---
## In one sentence
As the number of data points n grows, the posterior can jump from one region of weight space to another. Early on it sits where λ is small (simple, slightly worse fit); later it moves to a region with lower loss but larger λ, because n L_n grows faster than λ log n.

## Twist
Learning happens in jumps although only the amount of data changes: an internal model selection inside one network.

## Why it matters for safety
A jump in what a model computes can happen between two checkpoints: new solutions, and new capabilities, can appear suddenly.

## Open question


## Quiz
Two regions fit equally well (same loss) but have λ = 1 and λ = 2. For large n, where is the posterior? (Answer: around λ = 1.)

## Notes
Internal model selection: the posterior compares regions of one network (each like a sub-model) by their free energies and settles in the cheapest.

## Sources
- [Day 15 notes: Oxford SLT course, lectures 1 to 5](materials/november/day-15-singular-learning-theory/oxford-slt-course-lecture-1-5.pdf)
- [Day 15 exercise: a Bayesian phase transition](materials/november/day-15-singular-learning-theory/exercise-phase-transition.pdf)
