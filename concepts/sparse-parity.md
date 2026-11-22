---
title: "Sparse parity"
kind: case
days: [14]
origin: chat
by: [MariosTsatsos, claude]
links:
  - to: hardness-of-learning
    type: eg
    proposed: true
    by: claude
  - to: hidden-progress
    type: eg
    proposed: true
    by: claude
---

## In one sentence
Learn a function that is the parity of k unknown bits out of n: about k log n examples identify it, but gradient-based learners need on the order of n^k computation.

## Twist
During training the loss stays flat for a long time and then drops; the network was making progress that the loss did not show.

## Why it matters for safety


## Open question


## Self-test
For n = 50 and k = 3, how do k log2 n and n^k compare?

## Notes
Answer to the self-test: about 17 against 125,000.

## Sources
- Barak et al., Hidden Progress in Deep Learning: SGD Learns Parities Near the Computational Limit (arXiv 2207.08799)
- Discussion between Marios and Claude during the course
