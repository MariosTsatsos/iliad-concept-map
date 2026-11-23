---
title: "von Neumann-Morgenstern theorem"
kind: concept
days: [3, 4]
module: D.1.1
by: [MT, claude]
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
If an agent's preferences between lotteries (random choices among a finite set of options, with fixed probabilities) satisfy four axioms (completeness, transitivity, continuity, independence), then each option can be given a number, its utility, such that the agent prefers one lottery to another exactly when its expected utility is higher.

## Twist
The utility is not unique: adding a constant or multiplying by a positive number gives another utility that represents the same preferences (u′ = a + b × u with b > 0).

## Why it matters for safety

## Open question

## Self-test

## Notes
Day 4 reading: this kind of utility is called cardinal, which means that ratios of differences between the numbers carry meaning too, not only their order.

## Sources
- [Day 3 notes and slides, Fernando Rosas](https://iliad-intensive.org/agency/preferences-to-rewards/)
- [Narahari, Game Theory lecture notes, ch. 7: von Neumann-Morgenstern utilities](https://gtl.csa.iisc.ac.in/gametheory/ln/web-ncp7-utility.pdf)
