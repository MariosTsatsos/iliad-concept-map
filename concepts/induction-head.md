---
title: "Induction head"
kind: concept
days: [10]
origin: chat
by: [MariosTsatsos, claude]
links:
  - to: k-q-composition
    type: needs
    proposed: true
    by: claude
  - to: mechanistic-interpretability
    type: eg
    proposed: true
    by: claude
  - to: in-context-learning
    type: eg
    note: "One mechanism behind it."
    proposed: true
    by: claude
---

## In one sentence
An attention head that, on seeing a token A again, looks back to the token that followed the earlier A and predicts it: [A][B] ... [A] -> [B].

## Twist
It needs two heads in different layers working together.

## Why it matters for safety
A worked example of an algorithm found inside a trained network, and a mechanism for in-context learning.

## Open question


## Self-test
Which earlier head does it rely on, and what does that head do?

## Notes
Answer to the self-test: a previous-token head, which writes into each position what the token before it was.

## Sources
- Day 10 slides: Mech Interp
- Olsson et al., In-context Learning and Induction Heads (2022)
