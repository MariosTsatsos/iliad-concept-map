---
title: "Training dynamics"
kind: concept
days: [16]
origin: notes
by: [claude]
aliases: ["learning dynamics"]
links:
  - to: three-temperatures
    type: related
    proposed: true
    by: claude
  - to: three-mysteries
    type: related
    note: "Optimisation, the third question of Day 14, is what training dynamics studies."
    proposed: true
    by: claude
---
## In one sentence
The study of how a network's weights move during training, and of how that path decides what the trained model is. The claim of Day 16: much of a model's structure (hierarchy, shortcuts, simplicity) can be explained by the training process, and the goal is to engineer that process to get the properties we want.

## Twist
The same data and architecture can give different models, depending on the initialisation and on timing.

## Why it matters for safety
Shape training so that it selects an aligned model, not a harmful one (Day 16 slides).

## Open question


## Quiz
Which three questions does Day 16 ask about a staircase-shaped loss curve? (Answer: why plateaus, why in this order, why at these times.)

## Notes


## Sources
- [Day 16 slides: introduction to training dynamics](materials/november/day-16-training-dynamics/intro-training-dynamics.pdf)
- [Day 16 slides: learning dynamics lectures](materials/november/day-16-training-dynamics/christian-lectures.pdf)
- [Day 16 exercise sheet](materials/november/day-16-training-dynamics/exercise-sheet.pdf)
- [Day 16 reading list](materials/november/day-16-training-dynamics/reading-list.pdf)
- [Day 16 exercise notebook (Colab)](https://colab.research.google.com/drive/1LijVg6IvVw1KG9BkN9PJsfbW3vFo-laC?usp=sharing)
