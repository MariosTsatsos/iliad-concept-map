---
title: "Bayesian learning compared to SGD"
kind: concept
days: [15]
origin: notes
by: [claude]
links:
  - to: learning-coefficient
    type: related
    note: "λ measured around SGD solutions tracks compressibility and generalisation."
    proposed: true
    by: claude
  - to: three-temperatures
    type: related
    note: "Day 13 gives SGD a temperature, T = η σ²/(2B); that temperature is what makes SGD look like a tempered posterior."
    proposed: true
    by: claude
  - to: soft-inductive-bias
    type: related
    note: "Both learners show a soft bias towards simpler solutions."
    proposed: true
    by: claude
---
## In one sentence
Practice trains with SGD or Adam, not Bayes' rule, yet the two behave alike: both prefer simpler solutions, and both concentrate on low-loss weights. In Bayesian learning the preference is a theorem (the λ log n term of the free energy); in SGD it is observed. SGD with a constant step and noisy gradients behaves like a sampler of a tempered posterior.

## Twist
The two notions of simple seem to coincide: λ measured around SGD solutions predicts properties of SGD-trained models.

## Why it matters for safety
If SGD is close to Bayes, the tools of singular learning theory apply to the models that are actually trained.

## Open question
Where does SGD depart from the posterior, and does it change what is learned?

## Quiz
Why can SGD be modelled as sampling? (Answer: with a constant step and noisy gradients its stationary distribution is a Gibbs distribution, like a tempered posterior.)

## Notes


## Sources
- [Day 15 slides: Bayesian learning compared to SGD dynamics](materials/november/day-15-singular-learning-theory/slides-bayesian-learning-vs-sgd-dynamics.pdf)
