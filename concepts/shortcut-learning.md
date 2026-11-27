---
title: "Shortcut learning"
kind: problem
days: [16]
origin: notes
by: [MT, claude]
aliases: ["gradient starvation", "spurious feature"]
links:
  - to: goal-misgeneralization
    type: related
    note: "In both, the training data cannot tell two rules apart and the model picks the wrong one."
    proposed: true
    by: claude
  - to: saddle-to-saddle
    type: needs
    note: "The order of learning decides which feature wins."
    proposed: true
    by: claude
---
## In one sentence
A network learns an easy feature that happens to predict the label in training, instead of the intended one. The classic case (Sagawa et al.): asked to tell waterbirds from landbirds, the network learns the background, water or land, because the background is learned first.

## Twist
It is a matter of timing: features learned first take the gradient away from the others (gradient starvation), so the intended feature may never be learned.

## Why it matters for safety
The model looks right on the training data and fails when the shortcut breaks, the same shape as goal misgeneralisation.

## Open question


## Quiz
In the waterbirds example, what does the network learn first? (Answer: the background.)

## Notes


## Sources
- [Day 16 slides: introduction to training dynamics](materials/november/day-16-training-dynamics/intro-training-dynamics.pdf)
- [Sagawa, Koh, Hashimoto, Liang, Distributionally robust neural networks for group shifts (ICLR 2020)](https://arxiv.org/abs/1911.08731)
- [Pezeshki et al., Gradient starvation (NeurIPS 2021)](https://arxiv.org/abs/2011.09468)
