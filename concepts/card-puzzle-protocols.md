---
title: "Card puzzle 2: three protocols and a zero-leak one"
kind: case
days: [11]
origin: participant
by: [MT, claude]
links:
  - to: zero-knowledge-proof
    type: eg
    proposed: true
    by: claude
  - to: entropy
    type: needs
    note: "The leak is measured in bits."
    proposed: true
    by: claude
---

## In one sentence
Protocols for proving that two drawn cards have the same colour: each early version left N of the 650 possible same-colour pairs as candidates, a leak of log2(650/N) bits, and the final protocol leaks nothing: sort the deck into two colour groups with the pair face down in one, shuffle, reveal.

## Twist
The leak can be counted exactly, in bits.

## Why it matters for safety


## Open question


## Self-test
Why are there 650 same-colour pairs in a 52-card deck?

## Notes
Answer to the self-test: 2 colours x (26 choose 2) = 2 x 325.

## Sources
- Day 11 slides, David Zeidler: A toy model of zero-knowledge inference verification, warm-up puzzle 2
- [Zeidler, Zero-Knowledge Training Pause (LessWrong, 2026)](https://www.lesswrong.com/posts/CuzBTs3RfekGiBaAj/zero-knowledge-training-pause)
