---
title: "Belief state geometry in transformers"
kind: case
days: [18]
origin: notes
by: [claude]
aliases: ["Mess3", "fractal"]
links:
  - to: belief-state
    type: needs
    proposed: true
    by: claude
  - to: residual-stream
    type: related
    note: "The belief states are found as a linear image in the residual stream."
    proposed: true
    by: claude
  - to: linear-representation
    type: related
    note: "Another case of information laid out linearly in activations."
    proposed: true
    by: claude
---
## In one sentence
Shai et al. (2024) trained transformers on sequences from small HMMs and found the belief states, the memory of the optimal predictor, laid out linearly in the residual stream, including the fractal shape that the beliefs of the Mess3 process form.

## Twist
The model was trained only to predict the next token, yet it represents the geometry of beliefs about the whole hidden process.

## Why it matters for safety
A case where theory said in advance what a network must represent, and it was found there.

## Open question


## Quiz


## Notes


## Sources
- [Day 18 slides, part 1](materials/november/day-18-computational-mechanics/compmechslidespt1.pdf)
- [Day 18 reading guide, part 4](materials/november/day-18-computational-mechanics/compmechreadingguidept4.pdf)
- [Shai et al., Transformers represent belief state geometry in their residual stream (NeurIPS 2024)](https://arxiv.org/abs/2405.15943)
