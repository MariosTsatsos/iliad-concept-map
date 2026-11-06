---
title: "von Neumann–Morgenstern theorem"
kind: concept
days: [3, 4]
module: D.1.1
by: [marios]
links:
  - needs: completeness
  - needs: transitivity
  - needs: continuity
  - needs: independence
  - to: ordinal-utility
    type: needs
    proposed: true
    note: "Understand the ordering-only version first. vNM adds lotteries and two more axioms, and gets a utility unique up to a + b·u."
  - to: representability
    type: eg
    proposed: true
---

## In one sentence
If completeness, transitivity, continuity and independence hold for lotteries over a finite set X, there is a u: X → ℝ with μ ≥ ν exactly when Σ μ(x)u(x) ≥ Σ ν(x)u(x).

## Twist
u is unique only up to positive affine transformations: u′ = a + b·u with b > 0.

## Why it matters for safety

## Open question

## Self-test

## Notes
Day 4 reading: cardinal utility means ratios of differences matter too (interval scale).

## Sources
- [Day 3 notes and slides, Fernando Rosas](https://iliad-intensive.org/agency/preferences-to-rewards/)
- [Narahari, Game Theory lecture notes, ch. 7: von Neumann–Morgenstern utilities](https://gtl.csa.iisc.ac.in/gametheory/ln/web-ncp7-utility.pdf)
