---
title: "Next-token prediction is enough"
kind: concept
days: [18]
origin: notes
by: [claude]
links:
  - to: sufficient-statistic
    type: needs
    proposed: true
    by: claude
  - to: solomonoff-induction
    type: related
    note: "Solomonoff's predictor also predicts one symbol at a time, and thereby the whole future."
    proposed: true
    by: claude
---
## In one sentence
If a network predicts the next token exactly, its internal state (for a recurrent network, the pair of its last hidden state and the last token) is a sufficient statistic for the entire future, not just the next step. The reason: the probability of any continuation is a product of next-token probabilities.

## Twist
Training to predict one step ahead forces a memory good for all steps ahead.

## Why it matters for safety
One reason why next-token predictors can come to hold a model of the process that produced their data.

## Open question


## Quiz


## Notes


## Sources
- [Day 18 slides, part 2](materials/november/day-18-computational-mechanics/compmechslidespt2.pdf)
- [Day 18 exercises, part 2](materials/november/day-18-computational-mechanics/compmechexercisespt2.pdf)
