---
title: "Subliminal learning"
kind: case
days: [16, 17]
origin: notes
by: [MT, claude]
links:
  - to: steganography
    type: related
    note: "Both: a signal hidden in ordinary-looking data. Here nobody hid it on purpose."
    proposed: true
    by: claude
  - to: data-filtering
    type: challenges
    note: "Filtering the data for the trait does not stop the transfer."
    proposed: true
    by: claude
  - to: data-attribution
    type: related
    note: "Which examples carry the trait is a data attribution question."
    proposed: true
    by: claude
---
## In one sentence
A teacher model that loves owls writes only number sequences; a student trained on those numbers comes to love owls too, but only if teacher and student start from the same base model (Cloud et al., 2025). Traits pass through data that does not mention them.

## Twist
The signal is not in what the data says but in how it nudges a student that shares the teacher's starting weights.

## Why it matters for safety
Training on another model's outputs can pass on hidden traits, including misalignment, and filtering the data does not prevent it.

## Open question
Which of the teacher's outputs carry the trait? See the card on Bayesian influence functions for subliminal learning.

## Quiz
What must teacher and student share for the trait to transfer? (Answer: the same initialisation, the same base model.)

## Notes
The paper also proves that a small gradient step on a teacher's outputs moves a student with the same initialisation towards the teacher.

## Sources
- [Day 16 slides: introduction to training dynamics](materials/november/day-16-training-dynamics/intro-training-dynamics.pdf)
- [Cloud et al., Subliminal learning (2025)](https://arxiv.org/abs/2507.14805)
