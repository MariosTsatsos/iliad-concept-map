---
title: "Q-learning"
kind: concept
days: [3]
module: D.1.2
by: [MariosTsatsos, claude]
links:
  - to: bellman-equation
    type: needs
    proposed: true
  - to: explore-exploit
    type: needs
    proposed: true
    note: "Q-learning only learns about actions it tries, so it needs a rule for exploring."
---

## In one sentence
Knowing the best achievable value of each state does not tell the agent which action to take, unless it also knows how the environment responds to actions. Q-learning learns from experience alone the value of each action in each state (written Q), and that gives the best action directly.

## Twist

## Why it matters for safety

## Open question

## Self-test

## Notes
In some applications Q is represented by a deep neural network.

## Sources
- [Day 3 RL slides and exercises, Fernando Rosas](https://iliad-intensive.org/agency/reinforcement-learning/)
