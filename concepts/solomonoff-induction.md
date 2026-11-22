---
title: "Solomonoff induction"
kind: concept
days: [7, 14]
origin: chat
weight: 3
by: [MariosTsatsos, claude]
links:
  - to: bayesian-mixture
    type: eg
    note: "A Bayesian mixture over all computable hypotheses."
    proposed: true
    by: claude
  - to: kolmogorov-complexity
    type: needs
    proposed: true
    by: claude
---

## In one sentence
A Bayesian mixture over every computable hypothesis, where a hypothesis written as a program of length L starts with weight 2^(-L).

## Twist
It predicts almost as well as the best computable predictor, and it cannot be computed.

## Why it matters for safety
It is the reference point for what an ideal learner would do, against which real learners are compared.

## Open question
Day 14 asks whether deep learning solves approximation and generalisation in a similar way.

## Self-test
Why does a shorter program get more prior weight?

## Notes
Marios: "Solomonoff rocks."

## Sources
- [Day 7 notes and exercises, David Quarel: Solomonoff Induction and AIXI](https://iliad-intensive.org/agency/solomonoff-induction/)
- [Day 14 slide deck by Zach Furman: Mysteries of Deep Learning](https://iliad-intensive.org/learning/mysteries-of-deep-learning/)
