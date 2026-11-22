---
title: "Degeneracy"
kind: concept
days: [15]
origin: chat
by: [MariosTsatsos, claude]
links:
  - to: parameter-function-map
    type: needs
    proposed: true
    by: claude
  - to: implicit-bias
    type: eg
    note: "A preference for more degenerate solutions is one candidate for such a bias."
    proposed: true
    by: claude
---

## In one sentence
A weight setting is degenerate when there are directions in weight space along which the function does not change, to first order or beyond.

## Twist
For neural networks this is the normal case, and classical statistics assumes it never happens.

## Why it matters for safety
Singular learning theory uses the amount of degeneracy to say which solutions training prefers.

## Open question


## Self-test


## Sources
- [Kai Ogden, Oxford SLT course notes, Lectures 1 to 5](https://iliad-intensive.org/learning/singular-learning-theory/), Exercises 1.2.1 and 1.2.2
- Discussion between Marios and Claude during the course
