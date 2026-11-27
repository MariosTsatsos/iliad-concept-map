---
title: "World model"
kind: concept
days: [19]
origin: notes
by: [claude]
aliases: ["world model"]
links:
  - to: interface-vs-mechanism
    type: needs
    proposed: true
    by: claude
  - to: agent
    type: related
    note: "A world model is what lets an agent try out actions before taking them."
    proposed: true
    by: claude
---
## In one sentence
Working definition of Day 19: a representation of the relevant regularities of an environment that an agent can use off-line to predict, explain, imagine, plan or control. In interface language: a model W run in place of the environment U, which responds to actions as U does, I_W ≈ I_U.

## Twist
Not every predictor is a world model. Three tests: does it encode more than surface associations; can it be queried under hypothetical actions or perturbations; can it support reasoning over several steps? A next-frame predictor, a lookup table or a next-token predictor may be useful without passing them.

## Why it matters for safety
World models are used to train agents, to test agents in sandboxes before deployment, and to ask what a network represents about its world.

## Open question


## Quiz
Name the three diagnostics of Day 19. (Answer: latent organisation, queries under hypothetical actions, multi-step reasoning.)

## Notes


## Sources
- [Day 19 slides, set 1](materials/november/day-19-world-models/world-models-set-1.pdf)
- [Day 19 slides: reading material](materials/november/day-19-world-models/readingmaterialslides.pdf)
- [Day 19 slides, sets 2 and 3](materials/november/day-19-world-models/world-models-set-2-and-3.pdf)
