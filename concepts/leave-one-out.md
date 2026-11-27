---
title: "Leave-one-out: the counterfactual behind attribution"
kind: concept
days: [17]
origin: notes
by: [claude]
aliases: ["LOO", "counterfactual"]
links:
  - to: data-attribution
    type: needs
    proposed: true
    by: claude
---
## In one sentence
Example i caused a behaviour if removing it from the training set and retraining weakens that behaviour. This counterfactual is what most attribution methods try to approximate, because retraining once per example is far too expensive.

## Twist
Counterfactuals dilute credit: if two examples each suffice for a behaviour, removing either one changes nothing, so neither counts as a cause (the notes' example of butter and yeast).

## Why it matters for safety


## Open question


## Quiz
Why approximate leave-one-out instead of computing it? (Answer: it needs one full retraining per training example.)

## Notes


## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
- [Day 17 slides: data attribution](materials/november/day-17-data-attribution/data-attribution-slides-24-nov.pdf)
