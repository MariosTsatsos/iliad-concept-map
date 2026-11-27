---
title: "Deep learning as program synthesis"
kind: concept
days: [14]
origin: notes
by: [MT, claude]
links:
  - to: solomonoff-induction
    type: related
    note: "Universal induction is the ideal, uncomputable version of program synthesis."
    proposed: true
    by: claude
  - to: kolmogorov-complexity
    type: related
    note: "The ideal search prefers the program with the lowest Kolmogorov complexity."
    proposed: true
    by: claude
  - to: soft-inductive-bias
    type: related
    note: "Both are offered on Day 14 as candidate explanations of why deep learning generalises."
    proposed: true
    by: claude
  - to: compression-and-intelligence
    type: related
    note: "A short program that produces the data is a compression of it."
    proposed: true
    by: claude
---
## In one sentence
One candidate answer to the mysteries of Day 14: deep learning works because training performs a tractable form of program synthesis, a search for a short program that produces the data. Solomonoff's universal induction is the ideal version: among all programs that reproduce the observations, prefer the shortest one, which is Occam's razor made exact. The ideal is uncomputable; the hope is that gradient descent finds a cheap approximation.

## Twist
The ideal search is uncomputable, yet networks of finite size trained by gradient descent seem to find simple programs anyway. Why is open.

## Why it matters for safety
If training finds programs, a trained network contains algorithms that can in principle be read out, which is the bet of mechanistic interpretability.

## Open question
What makes the search tractable: the data, the architecture or the optimiser?

## Quiz
Among all programs that reproduce the observations, which one does universal induction choose? (Answer in Notes.)

## Notes
Answer: the shortest, the one with the lowest Kolmogorov complexity.

From MT's notes: object permanence, learnt early in life, is an example of the same move: it builds a model of the world that separates outside from inside. By the Church-Turing thesis, the rules that produced the observations can be written as a program, and reverse-engineered by program synthesis.

## Sources
- [Day 14 slides: mysteries of deep learning](materials/november/day-14-mysteries-of-deep-learning/mysteries-of-deep-learning-slides.pdf)
- [Day 14 notes: context for the day](materials/november/day-14-mysteries-of-deep-learning/mysteries-of-dl-contextualisation.pdf)
