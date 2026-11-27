---
title: "Data attribution"
kind: concept
days: [17]
origin: notes
by: [claude]
aliases: ["training data attribution", "TDA"]
links:
  - to: data-filtering
    type: related
    note: "Attribution says which data to filter out, or to upweight."
    proposed: true
    by: claude
---
## In one sentence
Asking which training examples caused a behaviour of the trained model. Give each example i a weight β_i in the training loss, choose a scalar observable φ (the loss on a test point, a logit), and ask how φ changes when β_i changes. Influence functions, Bayesian influence functions and unrolling are three ways to estimate that derivative.

## Twist
Mechanistic interpretability is causal analysis of the forward pass (which circuits caused this output?); data attribution is causal analysis of the training run (which data caused this model?).

## Why it matters for safety
Find the data behind an unwanted behaviour and filter it out; find the data behind a desired one and upweight it.

## Open question


## Quiz
What does β_i = 0 mean? (Answer: example i is removed from training.)

## Notes


## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
- [Day 17 slides: data attribution](materials/november/day-17-data-attribution/data-attribution-slides-24-nov.pdf)
