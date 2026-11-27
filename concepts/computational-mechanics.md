---
title: "Computational mechanics"
kind: concept
days: [18]
origin: notes
by: [claude]
aliases: ["comp mech"]
links:
  - to: sufficient-statistic
    type: needs
    proposed: true
    by: claude
  - to: compression-and-intelligence
    type: related
    note: "Causal states are the most compressed memory of the past that still predicts as well as possible."
    proposed: true
    by: claude
---
## In one sentence
The theory of what a predictor must remember about the past. Group past sequences by the future they predict: the groups are the causal states, the smallest memory that loses nothing about the future. Day 18 used it to ask what a transformer trained on next-token prediction must represent.

## Twist
Exact next-token prediction already forces a memory that is sufficient for the entire future.

## Why it matters for safety
It says in advance what structure should be inside a trained model (belief states), which can then be looked for: a theory-first route to interpretability.

## Open question


## Quiz


## Notes


## Sources
- [Day 18 slides, part 1](materials/november/day-18-computational-mechanics/compmechslidespt1.pdf)
- [Day 18 slides, part 2](materials/november/day-18-computational-mechanics/compmechslidespt2.pdf)
- [Day 18 slides, part 3](materials/november/day-18-computational-mechanics/compmechslidespt3.pdf)
- [Day 18 reading guide, part 4](materials/november/day-18-computational-mechanics/compmechreadingguidept4.pdf)
