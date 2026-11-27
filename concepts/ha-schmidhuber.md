---
title: "World models (Ha and Schmidhuber, 2018)"
kind: case
days: [19]
origin: notes
by: [claude]
aliases: ["Ha and Schmidhuber", "Dreamer"]
links:
  - to: world-models
    type: eg
    proposed: true
    by: claude
---
## In one sentence
An agent in three parts: V, a variational autoencoder that compresses each frame to a code z; M, a recurrent network that predicts the next z from z, its memory h and the action; and C, a small controller acting on (z, h), trained by an evolutionary method (CMA-ES). The controller can be trained inside M's predictions, in its dream.

## Twist
V is trained to reconstruct frames and then frozen, so nothing makes its code keep what matters for the future.

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 19 slides: reading material](materials/november/day-19-world-models/readingmaterialslides.pdf)
- [Ha and Schmidhuber, World models (2018)](https://arxiv.org/abs/1803.10122)
