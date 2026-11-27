---
title: "Generalised hidden Markov model (GHMM)"
kind: concept
days: [18]
origin: notes
by: [claude]
aliases: ["GHMM", "generalized HMM"]
links:
  - to: hidden-markov-model
    type: needs
    proposed: true
    by: claude
  - to: belief-state
    type: related
    note: "For a minimal-dimensional GHMM, belief states are the lowest-dimensional minimal sufficient statistics."
    proposed: true
    by: claude
---
## In one sentence
An HMM whose matrices may have negative entries, as long as every sequence still gets a valid probability. This can describe a process in fewer dimensions, and every process that has a GHMM realisation has a minimal-dimensional one.

## Twist
The hidden coordinates are no longer probabilities of anything; only the predictions are.

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 18 slides, part 3](materials/november/day-18-computational-mechanics/compmechslidespt3.pdf)
