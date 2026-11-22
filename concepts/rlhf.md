---
title: "RLHF"
kind: concept
days: [5]
by: [marios, claude]
links:
  - eg: post-training
  - to: representability
    type: needs
    proposed: true
    note: "Raters compare two outputs and a reward model is fitted to the comparisons (Bradley–Terry). That assumes the preferences can be summarised by one number per output."
  - to: transitivity
    type: vs
    proposed: true
    note: "Human raters are not always transitive. A preference cycle A > B > C > A cannot be fitted by any reward model."
---

## In one sentence
Reinforcement learning from human feedback: train a reward model on human comparisons of outputs, then optimise the model against it.

## Twist

## Why it matters for safety

## Open question

## Self-test

## Notes

## Sources
- [Day 5 slides, Margot Stakenborg](https://iliad-intensive.org/alignment/alignment-in-practice/)
