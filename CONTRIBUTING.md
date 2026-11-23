# Contributing

Every change takes about two minutes in the browser. You need a GitHub account, nothing else. When you save, GitHub makes a copy of the repository for you and opens a pull request. A check runs on it; if it goes red, the log names the file and says what is wrong.

## 1. Write a stub (most useful)

Hollow nodes have no one-sentence statement yet.

1. On the map, click a hollow node, then **Write it**.
2. Under `## In one sentence`, write one sentence in your own words.
3. Add a `## Twist` or `## Quiz` question if you have one.
4. Add your GitHub name to `by:`, for example `by: [MT, claude, your-name]`.
5. **Commit changes** → **Propose changes** → **Create pull request**.

## 2. Add a concept

1. On the map, click **Add a concept**. GitHub opens a new file with the blank card.
2. Rename `new-concept.md` to the concept, lowercase words joined by hyphens: `potential-based-shaping.md`. That name is the card's id.
3. Fill in the header and as many sections as you like. Only `title` is required.
4. Link it to at least one existing card. Use the file name without `.md`.
5. Commit and propose, as above.

## 3. Confirm or reject a proposed link

Dashed lines are suggestions nobody has checked.

- **Agree:** open the card that declares the link and delete its `proposed: true` line.
- **Disagree:** delete the whole link, and say why in the pull request.
- **Better type:** change `type:`. For example `related` instead of `needs`.

## The card format

```markdown
---
title: Potential-based shaping
kind: concept          # concept | problem | case
days: [3]
origin: participant    # participant | extension | notes | claude
by: [your-github-name]
links:
  - needs: reward
  - related: transitivity
  - to: specification-gaming      # long form, when you want a note
    type: related
    note: "Non-potential shaping can be gamed."
---

## In one sentence
## Twist
## Why it matters for safety
## Open question
## Quiz
## Notes
## Sources
```

Link types: `needs`, `eg` (example of), `related` (related to), `challenges`. A link goes on one card only; the map draws it both ways.

All attributes and their allowed values are listed in [README.md](README.md).

## House rules

- Your own words. Do not paste slides or lecture notes; link the module page under `## Sources`.
- One concept per card. If a card is doing two jobs, split it.
- A wrong card is better than no card. Fix each other's cards freely.
- Disagree with a card? Edit it and explain in the pull request, or open an issue.

## No GitHub account?

Use the **Suggest a concept** issue form, and the card will be added with your name on it.
