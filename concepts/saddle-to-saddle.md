---
title: "Saddle-to-saddle dynamics: plateaus, then drops"
kind: concept
days: [16]
origin: notes
by: [claude]
aliases: ["plateau", "stagewise learning", "staircase"]
links:
  - to: deep-linear-network
    type: needs
    proposed: true
    by: claude
  - to: hidden-progress
    type: related
    note: "A plateau looks like nothing is happening; underneath, the weights are slowly leaving a saddle."
    proposed: true
    by: claude
  - to: latent-heat-plateau
    type: related
    note: "The participant's latent-heat analogy is about the same plateaus."
    proposed: true
    by: claude
---
## In one sentence
Started from small weights, training sits near a saddle point of the loss (a plateau), escapes along one direction (a sudden drop), and arrives near the next saddle. Each escape learns one more mode of the data. A mode of strength s_α is learned at about t_α = (1/(2 s_α)) ln(s_α/σ0), where σ0 is the scale of the initial weights: strongest first.

## Twist
The staircase of the loss curve is not noise: its timing follows from the strengths in the data and the size of the initialisation.

## Why it matters for safety
When a capability appears, and in which order, can be engineered through the data, for example by a curriculum.

## Open question


## Quiz
Two modes have strengths 4 and 1. Which is learned first? (Answer: strength 4.)

## Notes


## Sources
- [Day 16 slides: introduction to training dynamics](materials/november/day-16-training-dynamics/intro-training-dynamics.pdf)
- [Day 16 slides: learning dynamics lectures](materials/november/day-16-training-dynamics/christian-lectures.pdf)
- [Zhang, Saxe, Latham, Saddle-to-saddle dynamics explains a simplicity bias across architectures (ICLR 2026)](https://arxiv.org/abs/2512.20607)
- [Jacot et al., Saddle-to-saddle dynamics in deep linear networks (2022)](https://arxiv.org/abs/2106.15933)
