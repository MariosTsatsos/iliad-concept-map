---
title: "No fixed key: why one key table cannot work in every context"
kind: concept
days: [10]
origin: participant
by: [MT, claude]
links:
  - to: steganography
    type: related
    proposed: true
    by: claude
---

## In one sentence
The token probabilities change with every context, so a fixed table that maps key bits to tokens cannot match the model's distribution everywhere; this is the reason a simple key table fails.

## Twist
This is what the PRF scheme answers: the key is turned into fresh randomness for each context.

## Why it matters for safety


## Open question


## Self-test


## Sources
- [Day 10 slides, Julian Schulz: Steganography and Backdoors](https://iliad-intensive.org/safety/steganography/)
