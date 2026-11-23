---
title: "Same-colour card proof: showing two cards match without revealing them"
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
A Day 11 warm-up exercise on zero-knowledge proofs: the prover draws two cards from a deck and has to convince the verifier that they have the same colour, without showing them. A protocol can be scored by what it gives away. There are 650 possible same-colour pairs; if what the verifier sees narrows them down to N candidates, the protocol has leaked log2(650/N) bits.

## Twist
What a protocol gives away can be counted exactly, in bits.

## Why it matters for safety


## Open question


## Self-test
Why are there 650 same-colour pairs in a 52-card deck?

## Notes
Answer to the self-test: 2 colours x (26 choose 2) = 2 x 325.

A candidate protocol that narrows nothing down: sort the rest of the deck into its two colours, add the pair face down to the group of its colour, shuffle, then reveal. The steps still have to be written out one by one.

## Sources
- Day 11 slides, David Zeidler: A toy model of zero-knowledge inference verification, warm-up puzzle 2
- [Zeidler, Zero-Knowledge Training Pause (LessWrong, 2026)](https://www.lesswrong.com/posts/CuzBTs3RfekGiBaAj/zero-knowledge-training-pause)
