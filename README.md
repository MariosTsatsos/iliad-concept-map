# Iliad concept map

An interactive map of the concepts from the [Iliad Intensive](https://iliad-intensive.org/) (London, November 2026), written by the participants in their own words.

Each concept is one card. Cards are joined by typed links, so the map shows *how* ideas connect, not just that they do. The links that cross days or course clusters are the interesting ones: transitivity of preferences (Day 3) turns up again in RLHF reward models (Day 5); reward shaping (Day 2) uses the same potential-function idea as transitivity.

**Live map:** https://mariostsatsos.github.io/iliad-concept-map/

## Reading the map

| You see | It means |
|---|---|
| Node colour | Course cluster: A alignment, B learning, C interpretability, D agency, E safety guarantees |
| Node shape | ● concept, ◆ safety problem, ▬ case (paper, incident, forecast) |
| Hollow node | Stub: nobody has written its one-sentence statement yet |
| Dashed line | Proposed link that nobody has confirmed yet |
| Dashed ring | Island: a card with no links |

Click a node to read its card, click a line to see why two cards are linked. Press `/` to search.

## Link types

| Type | Read `A → B` as |
|---|---|
| `needs` | A needs B: understand B first |
| `gen` | A generalises B: B is a special case of A |
| `tool` | A and B use the same maths |
| `vs` | A and B are in tension |
| `safety` | A bears on the safety problem B |
| `eg` | A is an example of B |

## Add to it

Everything happens in the browser, no install. See [CONTRIBUTING.md](CONTRIBUTING.md). The quickest useful thing: open the map, pick a hollow node, write its one sentence.

## Run it locally

```sh
pip install -r requirements.txt
python scripts/build.py          # writes site/dist/index.html
python scripts/build.py --check  # validate cards only
```

## What is in here

- `concepts/` one Markdown file per concept (`_template.md` is the blank card)
- `course.yml` days, lecturers, modules, link types
- `scripts/build.py` checks the cards, builds the graph with networkx, writes the site
- `site/template.html` the interactive page (Cytoscape.js)

No slides, PDFs or exercise sheets are stored here. Cards link to the module pages instead.

## Licence

Course material is by the Iliad team, published at [iliad-intensive.org](https://iliad-intensive.org/) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Cards are CC BY 4.0, by the people named in each card's `by:` field. Code is MIT (see `LICENSE`).
