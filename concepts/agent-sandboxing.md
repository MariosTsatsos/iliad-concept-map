---
title: "Sandboxing: testing an agent inside a world model"
kind: concept
days: [19]
origin: notes
by: [claude]
aliases: ["AI in a vat", "sandbox"]
links:
  - to: world-models
    type: eg
    note: "One of the three uses of world models named on Day 19."
    proposed: true
    by: claude
  - to: evals
    type: related
    note: "A sandbox test is an evaluation run inside a model of the world."
    proposed: true
    by: claude
  - to: interface-vs-mechanism
    type: related
    note: "The agent sees only the interface, so a sandbox only has to match the interface."
    proposed: true
    by: claude
---
## In one sentence
Test an AI system in a model of the world before deploying it. An agent sees the world only through its actions and observations, so a sandbox that reproduces that interface closely enough cannot be told apart from the real thing by the agent.

## Twist
How good must the model be, and can it be built efficiently? Rosas, Boyd and Baltieri (AI in a vat, 2025) study the limits.

## Why it matters for safety
Pre-deployment tests of agents depend on it, and so does the worry that an agent could tell a test from deployment.

## Open question


## Quiz


## Notes


## Sources
- [Day 19 slides, set 1](materials/november/day-19-world-models/world-models-set-1.pdf)
- [Day 19 slides, sets 2 and 3](materials/november/day-19-world-models/world-models-set-2-and-3.pdf)
