---
title: "Prefix code versus PRF: looks random but is not"
kind: concept
days: [10]
origin: participant
by: [MariosTsatsos, claude]
links:
  - to: prf
    type: needs
    proposed: true
    by: claude
  - to: prf-sampling-scheme
    type: needs
    proposed: true
    by: claude
---

## In one sentence
Marios's comparison of two ways to turn a message into token choices: a prefix code maps message bits to tokens directly, while a PRF produces bits that look random to anyone without the key yet are fully determined by it.

## Twist


## Why it matters for safety


## Open question


## Self-test
Who can tell PRF output from random bits?

## Sources
- Discussion between Marios and Claude during the course
- [Day 10 slides, Julian Schulz: Steganography and Backdoors](https://iliad-intensive.org/safety/steganography/)
