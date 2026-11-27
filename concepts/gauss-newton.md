---
title: "Gauss-Newton matrix"
kind: concept
days: [17]
origin: notes
by: [claude]
aliases: ["GNH", "Gauss-Newton Hessian"]
links:
  - to: hessian
    type: needs
    note: "A stand-in for H."
    proposed: true
    by: claude
---
## In one sentence
A stand-in for the Hessian that never bends down: G = Σ_i J_iᵀ H_y,i J_i, where J_i is how the network's output at example i moves with the weights, and H_y,i is the bend of the loss with respect to that output. It drops the second derivatives of the network itself.

## Twist
G equals H when the network fits every training example exactly; away from that, H can have negative bends and G cannot.

## Why it matters for safety


## Open question


## Quiz


## Notes


## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
