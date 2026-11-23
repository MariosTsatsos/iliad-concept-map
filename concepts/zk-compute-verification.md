---
title: "Zero-knowledge verification of AI compute"
kind: case
days: [11]
origin: notes
by: [claude]
links:
  - to: zero-knowledge-proof
    type: needs
    proposed: true
    by: claude
  - to: commitment
    type: needs
    proposed: true
    by: claude
  - to: spot-check
    type: needs
    proposed: true
    by: claude
  - to: network-tap
    type: needs
    proposed: true
    by: claude
  - to: compute-verification
    type: related
    proposed: true
    by: claude
---

## In one sentence
A proposal in which a prover commits to an approved model, logs commitments to its outputs, and proves in zero knowledge that randomly sampled outputs came from that model, while network taps record everything leaving the compute pods.

## Twist
The two parts do different jobs: the proofs cover the computation that the prover declares, and the taps bound everything else that could leave the machines.

## Why it matters for safety
One layer of a defence in depth for compute governance: the prover's covert goal is to train powerful models, the verifier's is to steal intellectual property, and the protocol is meant to block both.

## Open question


## Self-test


## Sources
- Day 11 slides, David Zeidler: A toy model of zero-knowledge inference verification
- [Peigné et al., Zero knowledge verification for frontier AI training is possible (arXiv 2606.05433)](https://arxiv.org/abs/2606.05433)
- [Zeidler, Zero-Knowledge Training Pause (LessWrong, 2026)](https://www.lesswrong.com/posts/CuzBTs3RfekGiBaAj/zero-knowledge-training-pause)
