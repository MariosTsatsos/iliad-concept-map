---
title: "Bellman equation"
kind: concept
days: [3]
module: D.1.2
by: [MariosTsatsos, claude]
links:
  - to: value-function
    type: needs
    proposed: true
  - to: mdp
    type: needs
    proposed: true
---

## In one sentence
The value of a state equals the expected reward of the next step plus the discounted value of the state that comes after it. The equation holds for a fixed policy and depends on how the environment moves between states, on the reward and on the discount factor γ (gamma, a number between 0 and 1 that says how much later rewards count).

## Twist

## Why it matters for safety

## Open question

## Self-test

## Notes
Working out the value of every state for a given policy is called policy evaluation.

## Sources
- [Day 3 RL slides and exercises, Fernando Rosas](https://iliad-intensive.org/agency/reinforcement-learning/)
