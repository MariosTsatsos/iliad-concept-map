---
title: "Zero-knowledge proof"
kind: concept
days: [11]
origin: notes
weight: 3
by: [claude]
links:
  - to: interactive-proof
    type: eg
    proposed: true
    by: claude
---

## In one sentence
A way for a prover to convince a verifier that a statement is true while revealing nothing beyond the fact that it is true.

## Twist
Three properties: complete (an honest prover always convinces), sound (a cheating prover almost never does), zero-knowledge (the verifier learns nothing else).

## Why it matters for safety
A lab could prove what it ran on its chips without showing weights or data.

## Open question


## Quiz
Which of the three properties protects the prover, and which protect the verifier?

## Sources
- Day 11 slides, David Zeidler: A toy model of zero-knowledge inference verification
- [Zeidler, Zero-Knowledge Training Pause (LessWrong, 2026)](https://www.lesswrong.com/posts/CuzBTs3RfekGiBaAj/zero-knowledge-training-pause)
