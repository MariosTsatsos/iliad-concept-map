---
title: "Free energy of learning"
kind: concept
days: [13]
origin: notes
weight: 3
by: [claude]
links:
  - to: boltzmann-distribution
    type: needs
    proposed: true
    by: claude
  - to: entropy
    type: needs
    proposed: true
    by: claude
  - to: pac-bayes
    type: related
    note: "The PAC-Bayes bound is written in terms of the free energy."
    proposed: true
    by: claude
---

## In one sentence
F = (average loss under a distribution over weights) + T x (KL divergence of that distribution from the prior). The prior is the distribution over weights assumed before seeing data, and the KL divergence measures how far the two distributions are apart. F is a trade-off between fitting the data and staying close to the prior.

## Twist
The distribution that minimises F is the Boltzmann distribution with the loss as energy.

## Why it matters for safety
One quantity ties together Bayesian learning, training by gradient descent on random batches, and bounds on generalisation.

## Open question


## Quiz
What does a larger T favour: fit or closeness to the prior?

## Sources
- Day 13 notes, Artemy Kolchinsky: Physics of Deep Learning
