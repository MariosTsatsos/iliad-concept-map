---
title: "Bayesian influence function (BIF)"
kind: concept
days: [17]
origin: notes
by: [MT, claude]
aliases: ["BIF", "Bayesian influence"]
plot:
  - title: "How one example's weight moves the minimum, with the posterior cloud"
    file: beta-landscape.html
links:
  - to: posterior-sampling-sgld
    type: needs
    note: "The covariance is estimated from posterior samples."
    proposed: true
    by: claude
  - to: influence-functions
    type: related
    note: "Under the Laplace approximation its leading term is the classical influence function."
    proposed: true
    by: claude
---
## In one sentence
Instead of one trained weight vector, take the posterior over weights, p_β(w) ∝ exp(−Σ β_i L_i(w)) × prior, and ask how the average of φ changes when β_i changes. The answer is a covariance: BIF = −Cov(L_i, φ) under the posterior. No Hessian is inverted; the posterior is sampled instead.

## Twist
It still works where H has zeros. Its leading term is the classical (damped) influence function; the extra terms carry the geometry the classical one cannot see.

## Why it matters for safety
Attribution for the degenerate models that are actually trained.

## Open question


## Quiz
Across the posterior, example i's loss is high exactly where φ is high. Is the BIF positive or negative? (Answer: negative. Upweighting i moves the posterior away from where L_i is high, which lowers the average of φ.)

## Notes
MT's words (Notion, Day 17): the Bayesian influence of example i is how much that average changes when β_i is increased. The identity is a fluctuation-response relation of statistical physics (notes, Remark 3.3). Caveat on the plot: true as long as observable = loss.

## Sources
- [Day 17 notes: data attribution](materials/november/day-17-data-attribution/data-attribution-notes-24-nov.pdf)
- [Day 17 slides: data attribution](materials/november/day-17-data-attribution/data-attribution-slides-24-nov.pdf)
- [Kreer et al., Bayesian influence functions for Hessian-free data attribution (2026)](https://arxiv.org/abs/2509.26544)
