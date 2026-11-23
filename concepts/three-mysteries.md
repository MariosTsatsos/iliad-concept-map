---
title: "Three questions of learning: approximation, generalisation, optimisation"
kind: concept
days: [14]
origin: notes
weight: 3
by: [claude]
links:
  - to: solomonoff-induction
    type: needs
    note: "The Day 14 recap uses it as the ideal answer to two of the three."
    proposed: true
    by: claude
  - to: curse-of-dimensionality
    type: needs
    note: "The classical warning behind the approximation question."
    proposed: true
    by: claude
---

## In one sentence
Three questions any learning machine must answer: does a good hypothesis exist in its class (approximation), will a hypothesis that fits the data also work on new data (generalisation), and can a good one be found in reasonable time (optimisation).

## Twist
Classical theory predicted failure on all three for large networks, and all three work in practice.

## Why it matters for safety
The Day 14 slides say that state-of-the-art safety methods are often based 'more on vibes than rigorous understanding'; understanding these three questions is the proposed remedy.

## Open question


## Self-test
Solomonoff induction answers two of the three. Which one does it leave unsolved?

## Notes
Answer to the self-test: optimisation.

## Sources
- [Day 14 slide deck by Zach Furman: Mysteries of Deep Learning](https://iliad-intensive.org/learning/mysteries-of-deep-learning/)
- [Day 14 slides, Miguel Donaire Arcas-Sariot: Historical introduction to the science of deep learning](https://iliad-intensive.org/learning/mysteries-of-deep-learning/)
