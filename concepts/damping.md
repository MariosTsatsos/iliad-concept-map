---
title: "Damping: adding λI to the Hessian"
kind: concept
days: [17]
origin: notes
by: [claude]
links:
  - to: influence-functions
    type: needs
    proposed: true
    by: claude
  - to: degeneracy
    type: related
    note: "Damping is the standard patch for degenerate directions."
    proposed: true
    by: claude
---
## In one sentence
When H has zero or tiny eigenvalues it cannot be inverted, so practice uses (H + λI)⁻¹ with a small λ > 0. This is the same as adding a penalty (λ/2)‖w − w*‖² for moving away from the trained weights.

## Twist
Damping changes the question: it predicts retraining that is held near w*, not plain retraining. Bae et al. call the difference the proximity gap.

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
- [Bae et al., If influence functions are the answer, then what is the question? (2022)](https://arxiv.org/abs/2209.05364)
