---
title: "Patterning: choosing data to get the model you want"
kind: concept
days: [17]
origin: notes
by: [claude]
links:
  - to: susceptibility
    type: needs
    note: "Patterning inverts the linear response."
    proposed: true
    by: claude
  - to: data-filtering
    type: related
    note: "Filtering is the crudest kind of patterning: set some data weights to zero."
    proposed: true
    by: claude
  - to: pretraining-safety
    type: related
    note: "Both shape a model through what it is trained on."
    proposed: true
    by: claude
---
## In one sentence
Attribution in reverse: instead of asking which data caused a behaviour, choose the data perturbation that produces a desired change in the model, using the same linear response (susceptibilities). The notes call it the dual of interpretability.

## Twist
If you can predict how data shapes a model, you can design data to shape it.

## Why it matters for safety
A route from understanding to control: shaping a model's internals through what it is trained on.

## Open question


## Quiz


## Notes


## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
