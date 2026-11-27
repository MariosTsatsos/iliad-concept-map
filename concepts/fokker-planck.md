---
title: "Fokker-Planck: the posterior cloud as a fluid"
kind: concept
days: [17]
origin: claude
by: [claude]
aliases: ["optimal transport", "Langevin"]
links:
  - to: posterior-sampling-sgld
    type: related
    proposed: true
    by: claude
  - to: bayes-vs-sgd
    type: related
    note: "SGD modelled as noisy flow obeys the same equation."
    proposed: true
    by: claude
  - to: boltzmann-distribution
    type: related
    note: "Its steady state is the Boltzmann (Gibbs) distribution."
    proposed: true
    by: claude
---
## In one sentence
Under Langevin dynamics (SGLD, or SGD modelled as a noisy flow) the density of the weights obeys the Fokker-Planck equation, a continuity equation: probability flows downhill and spreads by noise, like dye in a fluid. Its steady state is the Gibbs distribution, that is, the posterior.

## Twist
The Day 17 notes include a long exercise that reads influence functions as optimal transport of this fluid (section 3.3).

## Why it matters for safety


## Open question


## Quiz


## Notes
Claude's analogy, from general knowledge; the optimal-transport exercise is in the notes.

## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
