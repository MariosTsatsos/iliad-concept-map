---
title: "Steganography by PRF sampling"
kind: concept
days: [10]
origin: chat
by: [MariosTsatsos, claude]
links:
  - to: prf
    type: needs
    proposed: true
    by: claude
  - to: steganography
    type: safety
    proposed: true
    by: claude
  - to: no-fixed-key
    type: needs
    note: "The problem this scheme answers."
    proposed: true
    by: claude
---

## In one sentence
Sender and receiver share a key; the sender uses the PRF output as the randomness for sampling tokens so that the text depends on the message, and the receiver recomputes the same PRF values and checks which message fits the text.

## Twist
To a watcher without the key the text is distributed like ordinary samples from the model.

## Why it matters for safety


## Open question
Marios found this the hardest part of Day 10. The sender and receiver steps should be written out here with a small numeric example.

## Self-test


## Sources
- [Day 10 slides, Julian Schulz: Steganography and Backdoors](https://iliad-intensive.org/safety/steganography/)
- Discussion between Marios and Claude during the course
