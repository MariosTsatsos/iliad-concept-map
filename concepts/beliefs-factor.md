---
title: "In an agent-environment loop, beliefs factor"
kind: concept
days: [19]
origin: notes
by: [claude]
aliases: ["factored beliefs", "monoliths to modules"]
links:
  - to: belief-state
    type: related
    proposed: true
    by: claude
  - to: agent
    type: related
    note: "A formal handle on what separates an agent from its environment."
    proposed: true
    by: claude
---
## In one sentence
Put an agent T and an environment U in a loop: together they form one hidden Markov model. Given the past pairs of observations and actions, if an observer's belief about the joint hidden state starts as a product of a belief about the agent and a belief about the environment, it stays a product. The dimensions then add instead of multiplying: (|R| − 1) + (|S||X| − 1) instead of |R||S||X| − 1.

## Twist
The loop does not mix agent and environment in the observer's beliefs, which gives one way to say where the agent ends and the world begins.

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 19 slides, sets 2 and 3](materials/november/day-19-world-models/world-models-set-2-and-3.pdf)
- [Ehrlich, Baltieri, Rosas, Boyd (2026)](https://arxiv.org/abs/2611.02047)
- [Boyd et al., From monoliths to modules (2025)](https://arxiv.org/abs/2512.02193)
