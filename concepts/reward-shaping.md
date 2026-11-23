---
title: "Reward shaping"
kind: concept
days: [2, 3]
module: D.1.1
by: [MT, claude]
links:
  - to: transitivity
    type: related
    proposed: true
    note: "Both rest on a potential. Transitive preferences come from a potential V (no cycles). Potential-based shaping adds γΦ(s′) − Φ(s), which telescopes away over a trajectory, so the optimal policy does not change (Ng, Harada and Russell 1999)."
  - to: specification-gaming
    type: related
    proposed: true
    note: "Shaping that is not potential-based can be gamed: Randløv and Alstrøm's bicycle agent rode in circles to collect shaping reward. Potential-based shaping was designed to rule that out."
---

## In one sentence
Adding extra reward to guide learning; done carelessly it changes which behaviour is optimal.

## Twist

## Why it matters for safety

## Open question

## Self-test

## Notes

## Sources
- [DeepMind, Specification gaming: the flip side of AI ingenuity](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/)
- [Day 3 notes and slides, Fernando Rosas](https://iliad-intensive.org/agency/preferences-to-rewards/)
