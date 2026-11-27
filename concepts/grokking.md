---
title: "Grokking: memorise first, generalise much later"
kind: case
days: [14]
origin: notes
by: [MT, claude]
links:
  - to: hidden-progress
    type: eg
    note: "Grokking is the classic case of progress that the training loss does not show."
    proposed: true
    by: claude
  - to: sparse-parity
    type: related
    note: "Both are small tasks where generalisation arrives suddenly after a long wait."
    proposed: true
    by: claude
  - to: saddle-to-saddle
    type: related
    note: "Both show a long flat stretch followed by a sudden change; whether the mechanism is the same is open."
    proposed: true
    by: claude
---
## In one sentence
On some small tasks a network first memorises the training set (training loss near zero, test loss high) and only much later, with the training loss unchanged, switches to a rule that generalises. In MT's words: the model starts by memorising and picks up a complex rule; during training it forms simpler rules that generalise better, and chooses them over the earlier ones.

## Twist
The switch can come long after the training loss stopped moving, so the loss curve alone does not say that training is over.

## Why it matters for safety
A capability can appear suddenly and late; evaluations taken early can miss it.

## Open question


## Quiz
In grokking, which loss moves late: the training loss or the test loss? (Answer: the test loss.)

## Notes


## Sources
- [Day 14 slides: mysteries of deep learning](materials/november/day-14-mysteries-of-deep-learning/mysteries-of-deep-learning-slides.pdf)
- [Power et al., Grokking: generalization beyond overfitting on small algorithmic datasets (2022)](https://arxiv.org/abs/2201.02177)
