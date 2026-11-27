---
title: "Susceptibility: how one average responds to a nudge"
kind: concept
days: [17]
origin: notes
by: [claude]
links:
  - to: bayesian-influence-function
    type: related
    note: "The BIF is the susceptibility with ψ = −L_i."
    proposed: true
    by: claude
  - to: learning-coefficient
    type: related
    note: "Refined learning coefficients are other members of the same family (notes, section 3)."
    proposed: true
    by: claude
---
## In one sentence
For a tempered posterior p ∝ exp(−t L) × prior and two observables φ and ψ, tilt the posterior along ψ, p_h ∝ exp(−t(L − h ψ)) × prior, and see how the average of φ responds: χ(φ | ψ) = ∂E[φ]/∂h at h = 0 = t Cov(φ, ψ). With ψ = −L_i the tilt adds weight to example i, and the response is the Bayesian influence function.

## Twist
The same formula as magnetic susceptibility in physics: the response to a field equals a fluctuation.

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
