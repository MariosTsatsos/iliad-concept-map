---
title: "Double descent and the bias-variance trade-off"
kind: concept
days: [13, 14]
origin: participant
by: [MT, claude]
aliases: ["bias-variance", "memorisation", "interpolation", "benign overfitting"]
links:
  - to: double-descent
    type: related
    proposed: true
    by: claude
  - to: zhang-random-labels
    type: related
    note: "Fitting random labels is memorisation; double descent shows memorisation and generalisation can coexist."
    proposed: true
    by: claude
  - to: implicit-bias
    type: needs
    note: "The second descent depends on which of the many perfect fits training picks."
    proposed: true
    by: claude
  - to: double-descent-as-resonance
    type: related
    note: "The participant's resonance analogy is about the same peak at d = n."
    proposed: true
    by: claude
---
## In one sentence
The classical bias-variance trade-off splits test error into bias² + variance + noise: small models are too stiff (bias), large ones chase the noise (variance), so error is U-shaped. Double descent follows the U up to the point where the model can just fit every training example (d = n), where the variance peaks, and then descends again: with more parameters than examples, training picks the smoothest of the many perfect fits, so the variance falls.

## Twist
Memorising every training point, even the noisy ones, need not ruin generalisation; what matters is which of the perfect fits training picks.

## Why it matters for safety
A perfect fit to the training data says nothing about behaviour off it; the choice among perfect fits does.

## Open question
MT's question: is there a hidden connection between memorisation, interpolation and generalisation in a network, and the bias-variance trade-off? This card is a first answer.

## Quiz


## Notes


## Sources
- [Day 13 notes: physics of deep learning](materials/november/day-13-physics-for-deep-learning/physicsofdeeplearning-notes.pdf)
- [Belkin, Hsu, Ma, Mandal, Reconciling modern machine-learning practice and the classical bias-variance trade-off (PNAS 2019)](https://arxiv.org/abs/1812.11118)
