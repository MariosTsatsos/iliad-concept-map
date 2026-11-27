---
title: "Prediction is harder than generation"
kind: concept
days: [18, 19]
origin: notes
by: [claude]
aliases: ["unifilar", "unifilarity", "non-unifilar"]
links:
  - to: belief-state
    type: needs
    proposed: true
    by: claude
  - to: belief-state-geometry
    type: related
    note: "The Mess3 fractal is the set of beliefs its predictor must track."
    proposed: true
    by: claude
---
## In one sentence
A generator knows which hidden state it is in, so the same symbol may lead to different next states (it can be non-unifilar). A predictor sees only the symbols and must update its belief in one fixed way per symbol (it is unifilar). The predictor of a small non-unifilar generator can need infinitely many belief states.

## Twist
Simulating a process can be much cheaper than predicting it: three hidden states for the generator of Mess3, a fractal of beliefs for its predictor.

## Why it matters for safety
A model that generates plausible data is not thereby a model that predicts well, and the reverse.

## Open question


## Quiz


## Notes


## Sources
- [Day 18 exercises, part 3](materials/november/day-18-computational-mechanics/compmechexercisespt3.pdf)
- [Day 18 solutions, part 3](materials/november/day-18-computational-mechanics/compmechsolutionspt3.pdf)
- [Day 19 slides, sets 2 and 3](materials/november/day-19-world-models/world-models-set-2-and-3.pdf)
