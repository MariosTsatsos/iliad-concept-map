---
title: "Learning coefficient (LLC)"
kind: concept
days: [15]
origin: notes
by: [claude]
aliases: ["LLC", "RLCT", "real log canonical threshold", "local learning coefficient", "lambda"]
plot:
  - title: "Four shapes of a loss surface, and their λ"
    file: hessian-shapes.html
links:
  - to: degeneracy
    type: needs
    note: "λ measures how degenerate a minimum is."
    proposed: true
    by: claude
  - to: occam-factor
    type: related
    note: "λ takes the place of d/2 in the penalty of the Bayesian information criterion (BIC) when the model is degenerate."
    proposed: true
    by: claude
  - to: hessian
    type: related
    note: "H sees only second-order bends; λ sees the whole shape of the minimum."
    proposed: true
    by: claude
---
## In one sentence
The learning coefficient λ measures how much room there is around a minimum: how fast the volume of nearly-as-good weights shrinks as you ask for lower loss. For a regular minimum in d dimensions (the Hessian positive definite) λ = d/2; degenerate minima have smaller λ. In the free energy it replaces d/2 as the price of complexity: F_n ≈ n L_n + λ log n.

## Twist
Two minima with the same Hessian rank can have different λ: the losses w1² and w1² + w2⁴ both have Hessian rank 1, but λ is ½ and ¾.

## Why it matters for safety
λ can be estimated around a trained checkpoint, and λ measured around SGD solutions tracks how compressible a model is and how well it generalises.

## Open question
How well do sampling estimates of λ track the true value in large models?

## Quiz
If the Hessian at a minimum is positive definite, what is λ? (Answer: d/2, half the number of parameters.)

## Notes
In algebraic geometry λ is the real log canonical threshold (RLCT). The local learning coefficient (LLC) is λ at one minimum. The Day 15 notes define it through the volume of near-optimal parameters (section 2.1).

## Sources
- [Day 15 notes: Oxford SLT course, lectures 1 to 5](materials/november/day-15-singular-learning-theory/oxford-slt-course-lecture-1-5.pdf)
- [Day 15 optional exercise: estimating the LLC](materials/november/day-15-singular-learning-theory/exercise-optional-llc-estimation.pdf)
- [Day 15 slides: Bayesian learning compared to SGD dynamics](materials/november/day-15-singular-learning-theory/slides-bayesian-learning-vs-sgd-dynamics.pdf)
- [Lau et al., The local learning coefficient: a singularity-aware complexity measure (2023)](https://arxiv.org/abs/2308.12108)
