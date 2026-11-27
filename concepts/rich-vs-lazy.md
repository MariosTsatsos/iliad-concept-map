---
title: "Rich and lazy training"
kind: concept
days: [16]
origin: notes
by: [claude]
aliases: ["NTK", "neural tangent kernel", "lazy training", "feature learning"]
links:
  - to: training-dynamics
    type: related
    proposed: true
    by: claude
  - to: deep-linear-network
    type: related
    note: "The deep linear network from a small initialisation is the textbook rich case."
    proposed: true
    by: claude
  - to: linear-representation
    type: related
    note: "Rich training is where learned feature directions come from; lazy training learns almost none."
    proposed: true
    by: claude
---
## In one sentence
With large initial weights a network barely changes its features during training: it behaves like a fixed kernel machine (its neural tangent kernel, NTK, stays put). With small initial weights the kernel moves and the network learns new features. The first regime is called lazy, the second rich.

## Twist
Same architecture, same data: only the scale of the starting weights decides whether features are learned at all.

## Why it matters for safety
Interpretability looks for learned features; in the lazy regime there are few to find.

## Open question


## Quiz
Which regime learns features: small or large initialisation? (Answer: small, the rich regime.)

## Notes


## Sources
- [Day 16 slides: introduction to training dynamics](materials/november/day-16-training-dynamics/intro-training-dynamics.pdf)
- [Chizat, Oyallon, Bach, On lazy training in differentiable programming (NeurIPS 2019)](https://arxiv.org/abs/1812.07956)
