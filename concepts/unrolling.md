---
title: "Unrolling: differentiate through the training run"
kind: concept
days: [17]
origin: notes
by: [claude]
links:
  - to: training-dynamics
    type: related
    note: "Both study the path of training; unrolling asks how the data along the path moves the result."
    proposed: true
    by: claude
  - to: influence-functions
    type: related
    note: "In the right limit unrolling gives back the classical influence function."
    proposed: true
    by: claude
---
## In one sentence
Treat training as a chain of optimiser steps, w_(t+1) = h_t(w_t; β), and backpropagate through all of it to get ∂φ(w_T)/∂β_i. Unlike influence functions, this accounts for the optimiser, the learning rate, the batch order and the length of training.

## Twist
An example in the first mini-batch has a very different effect from the same example near the end: influence depends on training time. Unrolling also supplies its own damping, with no tuning.

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
- [Day 17 slides: data attribution](materials/november/day-17-data-attribution/data-attribution-slides-24-nov.pdf)
