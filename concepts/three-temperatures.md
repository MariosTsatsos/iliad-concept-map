---
title: "Three temperatures"
kind: concept
days: [13]
origin: extension
by: [MT, claude]
links:
  - to: boltzmann-distribution
    type: needs
    proposed: true
    by: claude
  - to: free-energy
    type: tool
    proposed: true
    by: claude
---

## In one sentence
'Temperature' means three different things: the physical temperature of the hardware, the training temperature that sets how much the weights are shaken (T = 1/n for exact Bayesian learning, T = eta sigma^2 / (2B) for stochastic gradient descent, SGD, where each step uses a small random batch of examples), and the sampling temperature that sets how random the output tokens are.

## Twist
The temperature of SGD is set by the optimiser and differs from 1/n in general; and real SGD noise has no single clean temperature.

## Why it matters for safety


## Open question


## Self-test
Which of the three does a user change in a chat interface?

## Notes
Symbols: n is the number of training examples, eta the step size, B the batch size, and sigma^2 measures how much the gradients of single examples differ from each other.

## Sources
- Day 13 notes, Artemy Kolchinsky: Physics of Deep Learning, Sec. IV and Eq. (42)
