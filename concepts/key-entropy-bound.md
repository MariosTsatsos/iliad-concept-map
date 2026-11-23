---
title: "The key must carry as much entropy as the message"
kind: concept
days: [10]
origin: participant
by: [MT, claude]
links:
  - to: entropy
    type: needs
    proposed: true
    by: claude
  - to: steganography
    type: related
    proposed: true
    by: claude
---

## In one sentence
For perfect secrecy the key needs at least the entropy of the message, H(M) <= H(K); the receiver also needs the rule for using the key, not the key alone.

## Twist


## Why it matters for safety


## Open question


## Quiz
Why can a 10-bit key not perfectly hide a 20-bit message?

## Sources
- [Day 10 slides, Julian Schulz: Steganography and Backdoors](https://iliad-intensive.org/safety/steganography/)
