---
title: "Does a backdoor's checker leave a trace?"
kind: problem
days: [8]
origin: participant
by: [claude]
links:
  - to: indistinguishability-obfuscation
    type: vs
    proposed: true
    by: claude
  - to: backdoor
    type: safety
    proposed: true
    by: claude
  - to: mechanistic-interpretability
    type: tool
    note: "Looking for the checker is a mechanistic interpretability task."
    proposed: true
    by: claude
---

## In one sentence
A backdoor has to check every input for the trigger, so the checking computation runs on every input, including the normal ones; the open question is whether that leaves something a defender can see.

## Twist


## Why it matters for safety


## Open question
Open. The iO result says that in the worst case reading the weights does not help. It does not say what a trained network's checker looks like.

## Self-test


## Sources
- Discussion during the course
- Day 8 slides, George Robinson: Heuristic arguments and verification
