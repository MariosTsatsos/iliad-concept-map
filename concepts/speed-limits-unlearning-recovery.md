---
title: "Speed limits for unlearning recovery"
kind: concept
days: [13, 20]
origin: participant
by: [MT, claude]
aliases: ["unlearning", "relearning", "relearning limit"]
links:
  - to: gradient-routing
    type: related
    note: "Gradient routing puts a capability in a known place so it can be removed; the proposal asks how fast it can come back."
    proposed: true
    by: claude
  - to: thermodynamics-of-learning
    type: related
    note: "The proposal uses the thermodynamic view of learning from Day 13."
    proposed: true
    by: claude
  - to: free-energy
    type: related
    note: "Day 13's free energy is the starting point of the thermodynamic picture."
    proposed: true
    by: claude
  - to: training-dynamics
    type: related
    note: "Recovery is a stretch of training; its speed is a question of training dynamics."
    proposed: true
    by: claude
---
## In one sentence
Proposal from proposal day 2. A lab removes a capability before releasing a model's weights; an attacker fine-tunes to restore it. Claim: the attacker needs at least N training steps, a bound in the spirit of the speed limits of stochastic thermodynamics (Day 13). A proof for a narrow case exists; proving a stronger, general theorem is the project.

## Twist
It turns the worry that unlearning is shallow into a question with a number for an answer.

## Why it matters for safety
A lower bound on recovery time would say how much protection unlearning buys for open-weight models.

## Open question
Which distance between the unlearned and the original model sets the bound, and can it be measured?

## Quiz


## Notes


## Sources
- [Working note with the proof for a narrow case](https://mtsatsos.com/relearning-limit.html)
- [Day 13 notes: physics of deep learning](materials/november/day-13-physics-for-deep-learning/physicsofdeeplearning-notes.pdf)
- [Day 20 slides: launch and proposal day 2](materials/november/day-20-project-proposal-day/launch-and-proposal-day-2-27-nov.pdf)
