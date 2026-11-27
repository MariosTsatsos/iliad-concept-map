---
title: "JEPA and LeWorldModel: predicting in a learned code"
kind: case
days: [19]
origin: notes
by: [claude]
aliases: ["JEPA", "LeWorldModel", "SIGReg", "V-JEPA"]
links:
  - to: world-models
    type: eg
    proposed: true
    by: claude
  - to: epsilon-transducer
    type: related
    note: "Collapse, which SIGReg prevents, is what the first criterion for causal states rules out."
    proposed: true
    by: claude
---
## In one sentence
A joint-embedding predictive architecture (JEPA) trains an encoder and a predictor together to predict the code of the next frame, not its pixels. LeWorldModel (Maes, Le Lidec, Scieur, LeCun and Balestriero, 2026) does this from pixels, with actions; its loss is the error of the predicted code plus a term, SIGReg, that pushes the codes towards a standard Gaussian.

## Twist
Without the extra term the cheapest solution maps every frame to the same code: it predicts perfectly and means nothing (collapse).

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 19 slides: reading material](materials/november/day-19-world-models/readingmaterialslides.pdf)
- [Day 19 slides, set 1](materials/november/day-19-world-models/world-models-set-1.pdf)
