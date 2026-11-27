---
title: "Watanabe's free energy formula"
kind: concept
days: [15]
origin: notes
by: [claude]
links:
  - to: learning-coefficient
    type: needs
    proposed: true
    by: claude
  - to: free-energy
    type: related
    note: "Day 13's free energy is the same kind of quantity seen from physics: fit plus a price for complexity."
    proposed: true
    by: claude
  - to: soft-inductive-bias
    type: related
    note: "The λ log n term is a soft preference for simpler regions, stated as a theorem."
    proposed: true
    by: claude
---
## In one sentence
With n data points, the free energy of a region U of weight space, F_n(U) = − log Z_n(U) (minus the log of the evidence that the region contributes), grows as F_n ≈ n L_n(w*) + λ log n: a term for fit, and a term for complexity set by the learning coefficient λ. The posterior concentrates on the region with the lowest free energy.

## Twist
The price of complexity counts the geometry of the minimum, not the number of parameters: a large but degenerate region can be cheaper than a small sharp one.

## Why it matters for safety
It gives a quantitative reason why Bayesian learning prefers simpler solutions, a soft inductive bias that can be stated and measured.

## Open question


## Quiz
As n grows, which term grows faster? (Answer: n L_n, linearly, against λ log n. With enough data fit wins; with little data simplicity can win.)

## Notes
Full statement (Theorem 3.2.1 of the notes): F_n(U) = n L_n(w*) + λ_U log n − (μ_U − 1) log log n + O_p(1), where μ_U is the multiplicity.

## Sources
- [Day 15 notes: Oxford SLT course, lectures 1 to 5](materials/november/day-15-singular-learning-theory/oxford-slt-course-lecture-1-5.pdf)
