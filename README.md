# Iliad concept map

An interactive map of the ideas from the [Iliad Intensive](https://iliad-intensive.org/) (London, November 2026): the course material, the questions and analogies participants came up with, and the projects they proposed at the end.

[![Preview of the concept map: about 200 cards as nodes, coloured by course cluster](docs/preview.png)](https://mtsatsos.com/iliad-concept-map/)

**Open the map:** https://mtsatsos.com/iliad-concept-map/

Each idea is one **card**, a small text file in `concepts/`. Cards are joined by **links**. The map draws every card as a node and every link as a line.

## Reading the map

| You see | It means |
|---|---|
| Colour | Course cluster: A alignment, B learning, C interpretability, D agency, E safety guarantees |
| Size | Number of cards the card is linked to |
| Ring | A participant's own idea |
| Hollow node | Stub: nobody has written its one sentence yet |
| Dashed line | Proposed link, not yet confirmed |
| Dotted line (open card only) | Close but not linked: a hint for a new link |
| Small square (Projects on) | A project a participant proposed on the last day |

Click a node to read its card: a refresher in one sentence, a twist, why it matters for safety, a quiz, and links to the slides and papers. Some cards have an interactive plot (**Try it**). Pick a day to see its slides, exercises and reading.

## Finding new connections

**Arrange by** (top left of the map) moves the cards and lets them glide to new places:

- **Links**: linked cards sit close.
- **Words**: cards whose texts share uncommon words sit close, across days.
- **Sources**: cards from the same day, or citing the same papers and files, sit close.

Cards that end up side by side without a link are candidates for one. The open card shows its three closest unlinked cards as dotted lines, with the words or sources they share, and the home panel lists the closest unlinked pairs from different days. These are hints computed from the text, not claims.

**Relax** shakes the map and lets it settle; drag a node and its neighbours follow.

## Course material

`materials/` holds the slides, notes, exercise sheets and solutions of the Intensive, published with Iliad's permission. `materials/README.md` lists them by day, and the map links to them from each day and from the cards. Books and papers by other authors are linked, not copied.

## Add or edit a card

You need a GitHub account and a browser.

1. Click **Add a concept** on the map. GitHub opens a new file with the blank card.
2. Name the file in lowercase words joined by hyphens, for example `loss-plateau.md`. The name without `.md` is the card's id.
3. Fill in the header and write the sentence under `## In one sentence`, in your own words.
4. Link it to at least one existing card.
5. Commit, then **Create pull request**. A check runs; once merged, the live map rebuilds in a few minutes.

To edit a card, open it on the map and click **Edit this card on GitHub**.

```yaml
---
title: "The loss plateau as latent heat"
kind: concept            # concept, problem or case
days: [14]               # course days, without quotes
origin: participant      # participant, extension, notes or claude
by: [your-github-name]
links:
  - needs: hidden-progress
  - to: double-descent
    type: related
    note: "Why the two are similar."
    proposed: true       # dashed until someone confirms it
---
```

Optional attributes: `module` (overrides the colour), `aliases` (found by search), `load_bearing: true`, `plot` (a page in `site/plots/`). Sections: `In one sentence`, `Twist`, `Why it matters for safety`, `Open question`, `Quiz`, `Notes`, `Sources`.

| Type | Shown as | Read "A, type, B" as |
|---|---|---|
| `needs` | builds on | A builds on B: read B first |
| `eg` | example of | A is an example of B |
| `related` | similar to | A and B share an idea, method or concern; the note says which |
| `challenges` | problem for | A is a problem for B; the note says why |

To confirm a dashed link, delete its `proposed: true` line. Participants' projects live in `projects.yml` (title and area only). Days, clusters and link types live in `course.yml`; links per day in `resources.yml`.

## Run it locally

```sh
pip install -r requirements.txt
python scripts/build.py --check   # checks every card
python scripts/build.py           # writes site/dist/index.html
```

`scripts/build.py` checks the cards, builds the graph with networkx and computes the three layouts and the nearness of cards. `site/template.html` is the page (Cytoscape.js). On every push to `main`, the workflow in `.github/workflows/` builds the page and `scripts/publish.sh` puts it, with `materials/`, on the `gh-pages` branch that GitHub Pages serves.

## Authors

- Marios Tsatsos ([@MariosTsatsos](https://github.com/MariosTsatsos)): the ideas marked "Participant's own idea" and the direction of the map. In `by:` lines he is `MT`.
- Claude (Anthropic): the code, the wording of every card that lists `claude` in `by:`, and the first draft of the links, all marked as proposed. Edit them freely.

## Licence

Course material is by the Iliad team and the lecturers; see [iliad-intensive.org](https://iliad-intensive.org/). Cards are CC BY 4.0, by the people named in each card's `by:` field. Code is MIT (see `LICENSE`).
