---
title: "Leverage: when one example moves the fit"
kind: concept
days: [17]
origin: notes
by: [claude]
links:
  - to: influence-functions
    type: needs
    proposed: true
    by: claude
  - to: leave-one-out
    type: related
    note: "Leverage says when the influence function and leave-one-out disagree."
    proposed: true
    by: claude
---
## In one sentence
In linear regression the leverage of example j is h_j = x_jᵀ A⁻¹ x_j, with A = Σ x_i x_iᵀ: how unusual x_j is compared with the rest of the data. Removing j changes the weights by exactly −A⁻¹ x_j r_j / (1 − h_j), where r_j is its residual; the influence function keeps only −A⁻¹ x_j r_j.

## Twist
The influence function is the first term of a series in h_j: fine for typical points (h_j near 0), badly wrong for outliers (h_j near 1), which is where attribution matters most.

## Why it matters for safety


## Open question


## Quiz
If h_j = 0.5, by what factor does the influence function underestimate the leave-one-out change? (Answer: 2.)

## Notes


## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
