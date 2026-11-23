---
title: "QK and OV circuits: where an attention head looks and what it copies"
kind: concept
days: [1]
by: [MT, claude]
links:
  - to: attention
    type: needs
    proposed: true
  - to: residual-stream
    type: needs
    proposed: true
    note: "Heads read from and write to the residual stream. QK decides where to look, OV decides what gets copied."
  - to: mechanistic-interpretability
    type: eg
    proposed: true
---

## In one sentence
The two parts of an attention head: the QK circuit (query and key) decides which earlier positions to attend to, and the OV circuit (output and value) decides what is copied from them.

## Twist

## Why it matters for safety

## Open question

## Self-test

## Notes

## Sources
- [Elhage et al., A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)
