---
title: "AI safety via debate"
kind: concept
days: [6]
origin: chat
by: [MariosTsatsos, claude]
links:
  - to: scalable-oversight
    type: safety
    proposed: true
    by: claude
  - to: complexity-classes
    type: needs
    proposed: true
    by: claude
  - to: interactive-proof
    type: eg
    note: "Two provers that oppose each other."
    proposed: true
    by: claude
---

## In one sentence
Two AI systems argue for opposite answers and a judge with limited time picks a winner; the hope is that telling the truth is the winning strategy.

## Twist
With optimal debaters, a polynomial-time judge can decide every problem in PSPACE, far beyond what the judge could check alone.

## Why it matters for safety
A proposal for scalable oversight: the judge only has to check one small step that the debaters disagree on.

## Open question
The theorem assumes optimal debaters. What is left of it for trained models that are not optimal?

## Self-test
Why does the judge need to check only one step of a long argument?

## Sources
- [Day 6 slides, Leonardo Costa Lesage: Debate and Scalable Oversight](https://iliad-intensive.org/safety/debate/)
- [Irving, Christiano, Amodei, AI safety via debate (2018)](https://arxiv.org/pdf/1805.00899)
