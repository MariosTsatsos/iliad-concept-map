---
title: "Logic gates from ReLU units"
kind: concept
days: [8]
origin: chat
by: [MariosTsatsos, claude]
---

## In one sentence
On inputs 0 and 1: NOT x = ReLU(1 - x), x AND y = ReLU(x + y - 1), x OR y = ReLU(x + y) - ReLU(x + y - 1); so every Boolean circuit can be written as a ReLU network.

## Twist
OR is the one that needs two units.

## Why it matters for safety


## Open question


## Self-test
Check AND on all four inputs.

## Sources
- Day 8 slides, George Robinson: Heuristic arguments and verification, exercise 1
- Discussion between Marios and Claude during the course
