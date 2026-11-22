---
title: "PAC-Bayes bound"
kind: concept
days: [13]
origin: notes
by: [claude]
links:
  - to: free-energy
    type: needs
    proposed: true
    by: claude
  - to: generalisation-gap
    type: safety
    proposed: true
    by: claude
---

## In one sentence
A guarantee that the test loss of a distribution over weights is at most its training loss plus a term that grows with its KL divergence from the prior (a measure of how far it is from the distribution over weights assumed before seeing data) and shrinks with the number of examples.

## Twist
For the Ising perceptron the notes show the bound is valid but loose.

## Why it matters for safety


## Open question


## Self-test


## Notes
PAC stands for 'probably approximately correct': the guarantee holds with high probability and up to a small error.

## Sources
- Day 13 notes, Artemy Kolchinsky: Physics of Deep Learning, Sec. III A, Eq. (31)
