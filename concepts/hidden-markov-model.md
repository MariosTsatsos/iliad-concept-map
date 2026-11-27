---
title: "Hidden Markov model (HMM)"
kind: concept
days: [18]
origin: notes
by: [claude]
aliases: ["HMM"]
links:
  - to: interface-vs-mechanism
    type: related
    note: "An HMM is one mechanism; the sequences it emits are its interface, and many HMMs give the same one."
    proposed: true
    by: claude
  - to: mdp
    type: related
    note: "In an MDP the agent sees the state; in an HMM the state is hidden and only the symbols are seen."
    proposed: true
    by: claude
---
## In one sentence
A process with hidden states that change by fixed probabilities and emit visible symbols. It is written as matrices T(x): the probability of emitting x and moving from one hidden state to another. You see the symbols, never the states.

## Twist
Many different HMMs produce exactly the same distribution over sequences of symbols.

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 18 slides, part 3](materials/november/day-18-computational-mechanics/compmechslidespt3.pdf)
- [Day 18 exercises, part 3](materials/november/day-18-computational-mechanics/compmechexercisespt3.pdf)
