---
title: "Complexity classes: P, NP, IP, PSPACE"
kind: concept
days: [6]
origin: notes
by: [claude]
links:
  - to: certificate
    type: needs
    proposed: true
    by: claude
---

## In one sentence
Classes of yes/no problems, sorted by the resources needed: P is solvable in polynomial time (time that grows as a fixed power of the input size), NP has yes answers with a short checkable certificate, IP has yes answers a randomised checker accepts after questioning a prover, PSPACE is solvable with polynomial memory.

## Twist
IP = PSPACE: letting the checker ask random questions takes it from NP all the way to PSPACE.

## Why it matters for safety


## Open question


## Self-test
Which of the four classes needs no prover at all?

## Sources
- [Day 6 slides, Leonardo Costa Lesage: Debate and Scalable Oversight](https://iliad-intensive.org/safety/debate/)
- [Shamir, IP = PSPACE (1992)](https://doi.org/10.1145/146585.146609)
