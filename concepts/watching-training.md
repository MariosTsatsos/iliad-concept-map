---
title: "Watching training"
kind: concept
days: [8]
origin: extension
by: [MT, claude]
links:
  - to: backdoor
    type: safety
    proposed: true
    by: claude
  - to: zk-compute-verification
    type: tool
    note: "Both verify the process that produced a model, not the model."
    proposed: true
    by: claude
---

## In one sentence
Give the defender the training data, the code, the random seed and every checkpoint, so that the network is known to be what gradient descent found and not something handed over.

## Twist
Any step left unwatched is a place to slip in a backdoor, and each check should cost about as much as the training step it checks.

## Why it matters for safety
It changes the question from 'is this network safe?' to 'was this network produced by the agreed process?'.

## Open question


## Self-test


## Sources
- Day 8 slides, George Robinson: Heuristic arguments and verification, session 2
