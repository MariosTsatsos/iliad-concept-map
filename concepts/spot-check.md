---
title: "Random spot checks"
kind: concept
days: [11]
origin: chat
by: [MariosTsatsos, claude]
links:
  - to: commitment
    type: needs
    proposed: true
    by: claude
  - to: interactive-proof
    type: tool
    note: "The verifier's randomness does the work in both."
    proposed: true
    by: claude
---

## In one sentence
The verifier checks a random sample of the prover's claims; if a fraction of the claims were false, the chance that every sampled one passes falls exponentially with the sample size.

## Twist
If 1% of claims are false, 4605 random checks all pass with probability 0.99^4605, about 8e-21. The slides use about 92,000 checks for 99.99% confidence that at least 99.99% of outputs are as claimed.

## Why it matters for safety


## Open question


## Self-test
Why must the prover commit before the verifier picks the sample?

## Sources
- Day 11 slides, David Zeidler: A toy model of zero-knowledge inference verification, protocol step 3
- Discussion between Marios and Claude during the course
