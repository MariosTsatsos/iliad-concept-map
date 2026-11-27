---
title: "ε-transducer: the minimal world model"
kind: concept
days: [19]
origin: notes
by: [claude]
aliases: ["epsilon-transducer", "transducer"]
links:
  - to: causal-states
    type: needs
    note: "The ε-transducer is causal states with actions."
    proposed: true
    by: claude
  - to: world-models
    type: eg
    note: "On Day 19 it is what a world model should track."
    proposed: true
    by: claude
---
## In one sentence
Causal states with actions: group histories of actions and observations by the distribution of future observations they predict, for every future sequence of actions. The resulting machine, the ε-transducer, is Markov given the action, and on Day 19 it is what a world model should track.

## Twist
The criteria are the same as for causal states: keep what the past says about the future, be predictable, be small. Drop the first and a constant memory is perfectly predictable: that is collapse.

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 19 slides: reading material](materials/november/day-19-world-models/readingmaterialslides.pdf)
- [Day 19 slides, sets 2 and 3](materials/november/day-19-world-models/world-models-set-2-and-3.pdf)
