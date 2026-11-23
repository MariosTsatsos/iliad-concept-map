---
title: "Curse of dimensionality"
kind: concept
days: [14]
origin: notes
by: [claude]
---

## In one sentence
The number of possible functions explodes with input size (there are 2^(2^n) Boolean functions of n bits), so approximating a generic function needs exponentially many parameters.

## Twist
Networks solve real problems with far fewer parameters, so real targets cannot be generic: they have structure the networks use.

## Why it matters for safety


## Open question


## Quiz
How many Boolean functions of 3 bits are there?

## Notes
Answer to the quiz: 2^8 = 256.

## Sources
- [Day 14 slide deck by Zach Furman: Mysteries of Deep Learning](https://iliad-intensive.org/learning/mysteries-of-deep-learning/), 'the universal approximation razor'
- [Day 14 slides, Miguel Donaire Arcas-Sariot: Historical introduction to the science of deep learning](https://iliad-intensive.org/learning/mysteries-of-deep-learning/)
