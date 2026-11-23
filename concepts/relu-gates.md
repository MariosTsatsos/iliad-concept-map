---
title: "Logic gates from ReLU units"
kind: concept
days: [8]
origin: extension
by: [MT, claude]
---

## In one sentence
ReLU(z) is z when z is positive and 0 otherwise. On inputs 0 and 1: NOT x = ReLU(1 - x), x AND y = ReLU(x + y - 1), x OR y = ReLU(x + y) - ReLU(x + y - 1); so every circuit of logic gates can be written as a network of ReLU units.

## Twist
In this form OR uses two units (the Day 8 exercise asks which gate needs two, and why). With a constant added after the unit, one is enough: x OR y = 1 - ReLU(1 - x - y).

## Why it matters for safety


## Open question


## Quiz
Check AND on all four inputs.

## Sources
- Day 8 slides, George Robinson: Heuristic arguments and verification, exercise 1
