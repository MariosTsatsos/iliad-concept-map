---
title: "Hessian: how the loss surface bends"
kind: concept
days: [15, 16, 17]
origin: extension
by: [MT, claude]
aliases: ["H", "second derivative", "curvature"]
plot:
  - title: "Four shapes of a loss surface"
    file: hessian-shapes.html
links:
  - to: degeneracy
    type: related
    note: "The zeros of H are the degenerate directions."
    proposed: true
    by: claude
  - to: saddle-to-saddle
    type: related
    note: "A saddle is a point where H has a negative bend."
    proposed: true
    by: claude
---
## In one sentence
The Hessian H is the matrix of second derivatives of the loss with respect to the weights. It says how the surface bends at a point in every direction: its eigenvalues are the bends along its main directions, positive for up, zero for flat, negative for down.

## Twist
For neural networks H at a minimum has many zero eigenvalues (degeneracy), so formulas that need H⁻¹ (influence functions, the Laplace approximation, the BIC) cannot be used as they stand.

## Why it matters for safety
Data attribution, model comparison and the analysis of training all run through H; where it fails tells you which tools to trust.

## Open question


## Quiz
Give two minima with the same Hessian rank but different learning coefficients. (Answer: w1² and w1² + w2⁴; both have rank 1, with λ = ½ and ¾. This is question 7 of the SLT quiz.)

## Notes
MT's picture: a bowl with a minimum; change w and see how the shape, the incline and the bend, changes. The incline is the gradient, the bend is H.

## Sources
- [Day 15 exercise: Hessian degeneracy in a teacher-student model](materials/november/day-15-singular-learning-theory/exercise-hessian-degeneracy-teacher-student.pdf)
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
- [Day 16 slides: learning dynamics lectures](materials/november/day-16-training-dynamics/christian-lectures.pdf)
