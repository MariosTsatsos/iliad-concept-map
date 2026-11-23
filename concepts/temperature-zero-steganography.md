---
title: "Temperature 0 leaves no room for steganography"
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
    type: safety
    proposed: true
    by: claude
  - to: three-temperatures
    type: needs
    proposed: true
    by: claude
---

## In one sentence
At sampling temperature 0 the model always emits the most likely token (word or piece of a word), so the output has zero entropy and the choice of tokens cannot carry a hidden message.

## Twist


## Why it matters for safety


## Open question
Is forcing low-entropy output a practical defence, and what does it cost in quality?

## Self-test
How many hidden bits can a deterministic output carry?

## Sources
