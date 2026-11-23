---
title: "Optimal policy and policy iteration"
kind: concept
days: [3]
module: D.1.2
by: [claude]
links:
  - to: bellman-equation
    type: needs
    proposed: true
---

## In one sentence
An optimal policy is one whose value is at least as high as that of any other policy in every state. In problems with finitely many states and actions and with discounting, one always exists, and the optimal Bellman equation is the tool for finding it.

## Twist

## Why it matters for safety

## Open question

## Self-test

## Notes
Policy iteration: start from any policy, then alternate two steps, working out the value of the current policy and improving the policy using that value, until the policy stops changing.

## Sources
- [Day 3 RL slides and exercises, Fernando Rosas](https://iliad-intensive.org/agency/reinforcement-learning/)
