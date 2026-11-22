---
title: "Indistinguishability obfuscation (iO)"
kind: concept
days: [8]
origin: notes
by: [claude]
links:
  - safety: backdoor
---

## In one sentence
A compiler that scrambles a circuit without changing what it computes, such that for two same-size circuits computing the same function nobody can tell which one was scrambled.

## Twist
With it, a trigger can be made impossible to flag even for a defender who reads the weights.

## Why it matters for safety


## Open question
Scrambled circuits are huge and unnatural, and training would not produce them. Does that make the result irrelevant to real models?

## Self-test


## Sources
- Day 8 slides, George Robinson: Heuristic arguments and verification
- Jain, Lin, Sahai, Indistinguishability obfuscation from well-founded assumptions (2021)
- Christiano, Hilton, Lecomte, Xu, Backdoor defense, learnability and obfuscation (2024)
