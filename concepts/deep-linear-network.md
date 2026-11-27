---
title: "Deep linear network"
kind: concept
days: [16]
origin: notes
by: [claude]
aliases: ["DLN"]
links:
  - to: gradient-flow
    type: needs
    proposed: true
    by: claude
  - to: training-dynamics
    type: eg
    note: "The main toy model of Day 16."
    proposed: true
    by: claude
---
## In one sentence
A network f(x) = W_L ⋯ W_1 x: a product of weight matrices with no nonlinearity. As a function of the input it is only a linear map, but as a function of the weights it is a product, so training it is a nonlinear problem, and one that can be solved exactly.

## Twist
Its loss has no bad local minima: every critical point is a global minimum or a saddle. Training still shows plateaus and stages, so the interesting dynamics come from saddles, not from traps.

## Why it matters for safety
A solvable toy that shows how the order and the timing of what a network learns are set by the data and the initialisation.

## Open question


## Quiz
Is a deep linear network more expressive than a single linear layer? (Answer: no, it still computes a linear map; what changes is how training gets there.)

## Notes


## Sources
- [Day 16 slides: introduction to training dynamics](materials/november/day-16-training-dynamics/intro-training-dynamics.pdf)
- [Day 16 slides: learning dynamics lectures](materials/november/day-16-training-dynamics/christian-lectures.pdf)
- [Day 16 exercise sheet](materials/november/day-16-training-dynamics/exercise-sheet.pdf)
- [Saxe, McClelland, Ganguli, A mathematical theory of semantic development in deep neural networks (PNAS 2019)](https://arxiv.org/abs/1810.10531)
- [Day 16 exercise notebook (Colab)](https://colab.research.google.com/drive/1LijVg6IvVw1KG9BkN9PJsfbW3vFo-laC?usp=sharing)
