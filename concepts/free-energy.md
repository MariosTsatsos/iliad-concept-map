---
title: "Free energy of learning"
kind: concept
days: [13]
origin: notes
weight: 3
by: [claude]
links:
  - needs: boltzmann-distribution
  - needs: entropy
  - to: pac-bayes
    type: tool
    note: "The PAC-Bayes bound is written in terms of the free energy."
---

## In one sentence
F = (average loss under a distribution over weights) + T x (KL divergence of that distribution from the prior): a trade between fitting the data and staying close to the prior.

## Twist
The distribution that minimises F is the Boltzmann distribution with the loss as energy.

## Why it matters for safety
One quantity ties together Bayesian learning, SGD and generalisation bounds.

## Open question


## Self-test
What does a larger T favour: fit or closeness to the prior?

## Sources
- Day 13 notes, Artemy Kolchinsky: Physics of Deep Learning
