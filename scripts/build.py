#!/usr/bin/env python3
"""Build the Iliad concept map.

Reads course.yml and every card in concepts/*.md, checks them, builds a
networkx graph, and writes site/dist/index.html and site/dist/graph.json.
The page loads Cytoscape.js and its fonts from public CDNs.

    python scripts/build.py           # check and build
    python scripts/build.py --check   # check only; exit 1 on errors (used in CI)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import sys
from pathlib import Path

import networkx as nx
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONCEPTS = ROOT / "concepts"
SITE = ROOT / "site"

SECTIONS = {
    "in one sentence": "statement",
    "twist": "twist",
    "why it matters for safety": "safety",
    "open question": "question",
    "quiz": "selftest",
    "self-test": "selftest",      # old name of the Quiz section, still accepted
    "notes": "notes",
    "sources": "sources",
}
KNOWN_KEYS = {"title", "kind", "days", "origin", "by", "links", "module", "aliases", "load_bearing"}
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)


class Problems:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")


def split_frontmatter(text: str) -> tuple[str, str] | None:
    if not text.startswith("---"):
        return None
    parts = text.split("\n---", 1)
    if len(parts) != 2:
        return None
    head = parts[0][3:]
    body = parts[1].split("\n", 1)[1] if "\n" in parts[1] else ""
    return head, body


def parse_sections(body: str, where: str, probs: Problems) -> dict[str, str]:
    out = {key: "" for key in SECTIONS.values()}
    current = None
    buf: list[str] = []

    def flush() -> None:
        if current:
            out[current] = COMMENT_RE.sub("", "\n".join(buf)).strip()

    for line in body.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            flush()
            name = m.group(1).strip().lower()
            current = SECTIONS.get(name)
            if current is None:
                probs.warn(where, f"unknown section '## {m.group(1)}' (ignored)")
            buf = []
        elif current:
            buf.append(line)
    flush()
    return out


def parse_link(raw, where: str, link_types: dict, probs: Problems) -> dict | None:
    if not isinstance(raw, dict):
        probs.error(where, f"link {raw!r} is not a mapping; write it as '- needs: other-card'")
        return None
    if "to" in raw:
        link = {
            "to": str(raw.get("to", "")).strip(),
            "type": str(raw.get("type", "")).strip(),
            "note": str(raw.get("note", "") or "").strip(),
            "proposed": bool(raw.get("proposed", False)),
            "by": raw.get("by"),
        }
    elif len(raw) == 1:
        (ltype, target), = raw.items()
        link = {"to": str(target).strip(), "type": str(ltype).strip(), "note": "", "proposed": False, "by": None}
    else:
        probs.error(where, f"link {raw!r} needs either one 'type: card' pair or 'to' and 'type'")
        return None
    if link["type"] not in link_types:
        probs.error(where, f"unknown link type '{link['type']}' (use one of: {', '.join(link_types)})")
        return None
    return link


def load(probs: Problems):
    course = yaml.safe_load((ROOT / "course.yml").read_text(encoding="utf-8"))
    link_types = course["link_types"]
    kinds = course["kinds"]
    origins = course["origins"]
    for name, spec in origins.items():
        if not isinstance(spec, dict) or not spec.get("label"):
            probs.error("course.yml", f"origin '{name}' needs a 'label'")
            origins[name] = spec = {"label": str(name), **(spec if isinstance(spec, dict) else {})}
    days = {int(k): v for k, v in course["days"].items()}

    # links from the lectures, by day (resources.yml)
    resources: dict[str, list] = {}
    res_path = ROOT / "resources.yml"
    if res_path.exists():
        raw = yaml.safe_load(res_path.read_text(encoding="utf-8")) or {}
        for day, items in raw.items():
            for n, item in enumerate(items or [], 1):
                where = f"resources.yml, day {day}, entry {n}"
                if not isinstance(item, dict) or not all(item.get(k) for k in ("kind", "title", "url")):
                    probs.error(where, "needs 'kind', 'title' and 'url'")
                    continue
                if item["kind"] not in ("exercise", "tool", "reading"):
                    probs.error(where, f"unknown kind '{item['kind']}' (use exercise, tool or reading)")
                    continue
                if not str(item["url"]).startswith(("http://", "https://")):
                    probs.error(where, "url must start with http:// or https://")
                    continue
                resources.setdefault(str(day), []).append(
                    {"kind": item["kind"], "title": str(item["title"]), "url": str(item["url"]), "from": str(item.get("from") or "")}
                )
    course["resources"] = resources

    cards: dict[str, dict] = {}
    for path in sorted(CONCEPTS.glob("*.md")):
        if path.name.startswith("_"):
            continue
        cid = path.stem
        where = f"concepts/{path.name}"
        if not ID_RE.match(cid):
            probs.error(where, "file name must be lowercase words joined by hyphens, e.g. bellman-equation.md")
            continue
        split = split_frontmatter(path.read_text(encoding="utf-8"))
        if split is None:
            probs.error(where, "missing the --- header block at the top")
            continue
        head, body = split
        try:
            fm = yaml.safe_load(head) or {}
        except yaml.YAMLError as exc:
            probs.error(where, f"header is not valid YAML: {exc}")
            continue
        if not isinstance(fm, dict):
            probs.error(where, "the header must be a list of 'name: value' lines")
            continue
        unknown = sorted(k for k in fm if k not in KNOWN_KEYS)   # review finding 11
        if unknown:
            probs.warn(where, f"unknown attribute(s) {', '.join(map(str, unknown))} (ignored). Known: {', '.join(sorted(KNOWN_KEYS))}")
        title = str(fm.get("title") or "").strip()
        if not title:
            probs.error(where, "missing 'title'")
            continue
        kind = fm.get("kind", "concept")
        if kind not in kinds:
            probs.error(where, f"kind must be one of {', '.join(kinds)}")
            kind = "concept"
        cdays = fm.get("days") or []
        if isinstance(cdays, int) and not isinstance(cdays, bool):
            cdays = [cdays]
        if not isinstance(cdays, list) or any(type(d) is not int for d in cdays):
            probs.error(where, "days must be a list of day numbers without quotes, e.g. [14] or [10, 13]")
            cdays = []
        bad_days = [d for d in cdays if d not in days]
        if bad_days:
            probs.error(where, f"days {bad_days} are not in course.yml")
        if not cdays:
            probs.warn(where, "no 'days' given")
        module = str(fm.get("module") or (days[cdays[0]].get("module", "") if cdays and cdays[0] in days else ""))
        cluster = module[:1] if module else ""
        if not cluster and cdays and cdays[0] in days:
            cluster = str(days[cdays[0]].get("cluster", ""))
        origin = str(fm.get("origin") or "notes")
        if origin not in origins:
            probs.error(where, f"origin must be one of {', '.join(origins)}")
            origin = "notes"
        by = fm.get("by") or []
        if isinstance(by, str):
            by = [by]
        links = []
        for raw in fm.get("links") or []:
            link = parse_link(raw, where, link_types, probs)
            if link:
                links.append(link)
        sections = parse_sections(body, where, probs)
        cards[cid] = {
            "id": cid,
            "title": title,
            "kind": kind,
            "days": cdays,
            "module": module,
            "cluster": cluster,
            "by": by,
            "origin": origin,
            "load_bearing": fm.get("load_bearing"),
            "aliases": fm.get("aliases") or [],
            "sections": sections,
            "status": "draft" if sections["statement"] else "stub",
            "links": links,
            "path": f"concepts/{path.name}",
        }
    return course, cards


def build_graph(course: dict, cards: dict, probs: Problems) -> nx.MultiDiGraph:
    link_types = course["link_types"]
    g = nx.MultiDiGraph()
    for cid, card in cards.items():
        g.add_node(cid, **{k: v for k, v in card.items() if k != "links"})
    seen: dict[tuple, dict] = {}
    for cid, card in cards.items():
        where = card["path"]
        for link in card["links"]:
            tgt = link["to"]
            if tgt == cid:
                probs.error(where, "a card cannot link to itself")
                continue
            if tgt not in cards:
                probs.error(where, f"links to '{tgt}', but concepts/{tgt}.md does not exist")
                continue
            directed = link_types[link["type"]]["directed"]
            key = (cid, tgt, link["type"]) if directed else (*sorted((cid, tgt)), link["type"])
            if key in seen:
                prev = seen[key]
                prev["proposed"] = prev["proposed"] and link["proposed"]
                if link["note"] and not prev["note"]:
                    prev["note"] = link["note"]
                continue
            data = {
                "type": link["type"],
                "note": link["note"],
                "proposed": link["proposed"],
                "by": link["by"] or ("claude" if link["proposed"] else (card["by"][0] if card["by"] else "")),
                "declared_in": cid,
            }
            seen[key] = data
            g.add_edge(cid, tgt, **data)
    for cid, card in cards.items():
        if card["status"] == "stub":
            probs.warn(card["path"], "stub: '## In one sentence' is empty")
    return g


def landscape(p: dict) -> dict:
    """Turn the layout so that its long side is horizontal, and widen it to suit a wide screen.
    Screens are wider than tall, so this leaves more room for labels. The result is the same on every machine."""
    import numpy as np
    ids = sorted(p)
    a = np.array([p[n] for n in ids], dtype=float)
    a -= a.mean(axis=0)
    _, _, vt = np.linalg.svd(a, full_matrices=False)
    a = a @ vt.T                                   # long axis first
    for k in (0, 1):                               # fix the mirror image: first card (by id) sits left and above
        if a[0, k] > 0:
            a[:, k] *= -1
    w, h = np.ptp(a[:, 0]), np.ptp(a[:, 1])
    if w > 0 and h > 0:
        a[:, 0] *= min(1.5, max(1.0, 1.6 * h / w))  # aim for 1.6 wide to 1 high, widen by at most half
    return {n: (float(x), float(y)) for n, (x, y) in zip(ids, a)}


def layout(g: nx.MultiDiGraph) -> dict[str, tuple[float, float]]:
    """Deterministic positions: biggest connected group in the middle,
    smaller groups to the right, isolated cards in a row underneath."""
    u = nx.Graph(g.to_undirected())
    comps = sorted(nx.connected_components(u), key=lambda c: (-len(c), sorted(c)[0]))
    pos: dict[str, tuple[float, float]] = {}
    groups = [c for c in comps if len(c) > 1]
    isolates = sorted(n for c in comps if len(c) == 1 for n in c)
    if groups:
        main = u.subgraph(groups[0])
        scale = 90 * math.sqrt(len(main))
        p = nx.kamada_kawai_layout(main, scale=scale) if len(main) > 2 else nx.circular_layout(main, scale=scale)
        p = landscape(p)
        p0 = dict(p)
        pos.update({n: (float(x), float(y)) for n, (x, y) in p.items()})
        right = max(x for x, _ in p.values()) + 190
        y_cursor = min(y for _, y in p.values())
        for comp in groups[1:]:
            sub = u.subgraph(comp)
            s = 52 * math.sqrt(len(sub))
            p = nx.kamada_kawai_layout(sub, scale=s) if len(sub) > 2 else nx.circular_layout(sub, scale=s)
            for n, (x, y) in p.items():
                pos[n] = (float(x) + right, float(y) + y_cursor + s)
            y_cursor += 2 * s + 110
        bottom = max(y for _, y in p0.values()) + 120
    else:
        bottom = 0
    for i, n in enumerate(isolates):
        pos[n] = (-((len(isolates) - 1) * 120) / 2 + i * 120, bottom)
    return pos


def stats(g: nx.MultiDiGraph) -> dict:
    u = nx.Graph(g.to_undirected())
    comps = sorted(nx.connected_components(u), key=len, reverse=True)
    mainland = comps[0] if comps and len(comps[0]) > 1 else set()
    cross = [
        (s, t, d["type"]) for s, t, d in g.edges(data=True)
        if g.nodes[s]["cluster"] and g.nodes[t]["cluster"] and g.nodes[s]["cluster"] != g.nodes[t]["cluster"]
    ]
    cross_day = [
        (s, t) for s, t in g.edges()
        if not set(g.nodes[s]["days"]) & set(g.nodes[t]["days"])
    ]
    return {
        "cards": g.number_of_nodes(),
        "links": g.number_of_edges(),
        "proposed": sum(1 for *_, d in g.edges(data=True) if d["proposed"]),
        "stubs": sum(1 for _, d in g.nodes(data=True) if d["status"] == "stub"),
        "isolated": sorted(n for n in g.nodes if u.degree(n) == 0),
        "cut_off_groups": [sorted(c) for c in comps if 1 < len(c) and c is not comps[0]],
        "mainland": len(mainland),
        "cross_cluster": len(cross),
        "cross_day": len(cross_day),
    }


def to_payload(course: dict, g: nx.MultiDiGraph, pos: dict, st: dict, template: str) -> dict:
    u = nx.Graph(g.to_undirected())
    nodes = []
    for n, d in g.nodes(data=True):
        x, y = pos.get(n, (0.0, 0.0))
        nodes.append({
            "id": n, "title": d["title"], "kind": d["kind"], "days": d["days"], "module": d["module"],
            "cluster": d["cluster"], "by": d["by"], "origin": d["origin"], "load_bearing": d["load_bearing"], "aliases": d["aliases"],
            "status": d["status"], "sections": d["sections"], "path": d["path"],
            "degree": u.degree(n), "x": round(x, 1), "y": round(y, 1),
        })
    edges = []
    for i, (s, t, d) in enumerate(g.edges(data=True)):
        edges.append({"id": f"e{i}", "source": s, "target": t, **d})
    days = {str(k): v for k, v in course["days"].items()}
    for v in days.values():
        if isinstance(v.get("date"), (dt.date,)):
            v["date"] = v["date"].isoformat()
    return {
        "meta": {
            "cohort": course.get("cohort", ""),
            "repo": course.get("repo", ""),
            "branch": course.get("branch", "main"),
            "built": dt.date.today().isoformat(),
            "clusters": course["clusters"],
            "link_types": course["link_types"],
            "kinds": course["kinds"],
            "origins": course["origins"],
            "days": days,
            "resources": course.get("resources", {}),
            "card_template": template,
        },
        "nodes": nodes,
        "edges": edges,
        "stats": st,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validate only")
    ap.add_argument("--out", default=str(SITE / "dist"), help="output folder")
    args = ap.parse_args()

    probs = Problems()
    course, cards = load(probs)
    g = build_graph(course, cards, probs)

    for w in probs.warnings:
        print(f"warning  {w}")
    for e in probs.errors:
        print(f"ERROR    {e}")
    st = stats(g)
    print(
        f"\n{st['cards']} cards, {st['links']} links ({st['proposed']} proposed), {st['stubs']} stubs, "
        f"{len(st['isolated'])} isolated, {len(st['cut_off_groups'])} cut-off groups, "
        f"{st['cross_cluster']} cross-cluster links, {st['cross_day']} cross-day links"
    )
    if probs.errors:
        print(f"\n{len(probs.errors)} error(s). Fix them and run again.")
        return 1
    if args.check:
        return 0

    template = (CONCEPTS / "_template.md").read_text(encoding="utf-8")
    payload = to_payload(course, g, layout(g), st, template)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    data = json.dumps(payload, ensure_ascii=False, indent=None, separators=(",", ":"))
    (out / "graph.json").write_text(data, encoding="utf-8")
    fragment = (SITE / "template.html").read_text(encoding="utf-8")
    fragment = fragment.replace("/*__DATA__*/null", data.replace("</", "<\\/"))
    page = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        "</head>\n<body>\n" + fragment + "\n</body>\n</html>\n"
    )
    (out / "index.html").write_text(page, encoding="utf-8")
    (out / "fragment.html").write_text(fragment, encoding="utf-8")
    print(f"wrote {out / 'index.html'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
