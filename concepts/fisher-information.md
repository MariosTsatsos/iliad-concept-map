---
title: "Fisher information: weight space as a curved space"
kind: concept
days: [17]
origin: claude
by: [claude]
aliases: ["Fisher", "information geometry", "natural gradient"]
links:
  - to: gauss-newton
    type: related
    note: "For squared loss, and for cross-entropy with softmax outputs, the Gauss-Newton matrix is the Fisher matrix."
    proposed: true
    by: claude
  - to: hessian
    type: related
    note: "H is the bend of the loss surface; Fisher is the curvature of the space of models."
    proposed: true
    by: claude
---
## In one sentence
The Fisher information matrix measures how much a model's predicted distribution changes when the weights move. It makes weight space a curved space (information geometry), in which distance is measured by change in prediction, not change in weights. For the usual losses it equals the Gauss-Newton matrix of Day 17.

## Twist
H and Fisher agree at a perfect fit and differ elsewhere: one describes the loss surface, the other the space of models it sits over.

## Why it matters for safety


## Open question


## Quiz


## Notes
Added by Claude from general knowledge, not from the course material. Martens (2020) works out the equivalence with the Gauss-Newton matrix.

## Sources
- [Martens, New insights and perspectives on the natural gradient method (JMLR 2020)](https://arxiv.org/abs/1412.1193)
