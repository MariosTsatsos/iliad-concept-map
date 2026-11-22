---
title: "Backdoor in a model"
kind: problem
days: [8, 10]
origin: notes
by: [claude]
---

## In one sentence
A model that behaves normally except on inputs carrying a hidden trigger, where it does what the attacker wants.

## Twist
In the signature construction, finding a triggering input by querying the model is as hard as forging a digital signature.

## Why it matters for safety
Testing a model on inputs cannot rule out a backdoor.

## Open question


## Self-test
Who can produce a triggering input in the signature construction?

## Sources
- Day 8 slides, George Robinson: Heuristic arguments and verification
- Goldwasser, Kim, Vaikuntanathan, Zamir, Planting undetectable backdoors in ML models (2022)
