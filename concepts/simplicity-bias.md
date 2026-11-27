---
title: "Simplicity bias of training"
kind: concept
days: [16]
origin: notes
by: [claude]
links:
  - to: implicit-bias
    type: eg
    note: "A concrete form of the implicit bias of training."
    proposed: true
    by: claude
  - to: soft-inductive-bias
    type: related
    proposed: true
    by: claude
  - to: saddle-to-saddle
    type: needs
    note: "Learning one mode at a time is why training stops at a simple solution."
    proposed: true
    by: claude
---
## In one sentence
Gradient training from small weights tends to end at simple solutions: small norm, low rank, sparse matrices. On Day 16 this follows from the dynamics: modes are learned one at a time, so training stops at the simplest solution that fits.

## Twist
Nobody adds a penalty for simplicity; it comes from the path that training takes.

## Why it matters for safety
If we understand which solutions training prefers, we can predict and shape which ones it reaches.

## Open question


## Quiz


## Notes


## Sources
- [Day 16 slides: introduction to training dynamics](materials/november/day-16-training-dynamics/intro-training-dynamics.pdf)
- [Zhang, Saxe, Latham, Saddle-to-saddle dynamics explains a simplicity bias across architectures (ICLR 2026)](https://arxiv.org/abs/2512.20607)
