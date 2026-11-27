#!/usr/bin/env python3
"""Build the Iliad concept map.

Reads course.yml, resources.yml, materials/index.yml, projects.yml and every card in
concepts/*.md, checks them, builds a networkx graph, and writes site/dist/index.html,
site/dist/graph.json and site/dist/plots/. The page loads Cytoscape.js and its fonts
from public CDNs.

Besides the layout by links, the build computes two more layouts, by shared words and by
shared sources, and for every card the cards closest to it in each sense. The page uses
them for "Arrange by" and for the dotted "close but not linked" lines.

    python scripts/build.py           # check and build
    python scripts/build.py --check   # check only; exit 1 on errors (used in CI)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

import networkx as nx
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONCEPTS = ROOT / "concepts"
SITE = ROOT / "site"
PLOTS = SITE / "plots"
RES_KINDS = ("material", "exercise", "tool", "reading")

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
KNOWN_KEYS = {"title", "kind", "days", "origin", "by", "links", "module", "aliases", "load_bearing", "plot"}
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
                if item["kind"] not in RES_KINDS:
                    probs.error(where, f"unknown kind '{item['kind']}' (use {', '.join(RES_KINDS)})")
                    continue
                if not str(item["url"]).startswith(("http://", "https://")):
                    probs.error(where, "url must start with http:// or https://")
                    continue
                resources.setdefault(str(day), []).append(
                    {"kind": item["kind"], "title": str(item["title"]), "url": str(item["url"]), "from": str(item.get("from") or "")}
                )
    # uploaded course material (materials/index.yml), listed first under each day
    mat_path = ROOT / "materials" / "index.yml"
    if mat_path.exists():
        for n, item in enumerate(yaml.safe_load(mat_path.read_text(encoding="utf-8")) or [], 1):
            where = f"materials/index.yml, entry {n}"
            if not isinstance(item, dict) or not all(item.get(k) for k in ("day", "title", "path")):
                probs.error(where, "needs 'day', 'title' and 'path'")
                continue
            if not (ROOT / item["path"]).is_file():
                probs.error(where, f"file {item['path']} does not exist")
                continue
            size = f"{item['bytes'] / 1e6:.1f} MB" if item.get("bytes") else ""
            resources.setdefault(str(item["day"]), []).insert(
                sum(1 for x in resources.get(str(item["day"]), []) if x["kind"] == "material"),
                {"kind": "material", "title": str(item["title"]), "url": str(item["path"]), "from": size})
    course["resources"] = resources

    # participants' projects (projects.yml): titles and areas only
    projects = []
    proj_path = ROOT / "projects.yml"
    if proj_path.exists():
        raw = yaml.safe_load(proj_path.read_text(encoding="utf-8")) or {}
        areas = raw.get("areas") or {}
        for n, item in enumerate(raw.get("projects") or [], 1):
            where = f"projects.yml, project {n}"
            if not isinstance(item, dict) or not item.get("title") or item.get("area") not in areas:
                probs.error(where, f"needs a 'title' and an 'area' from: {', '.join(areas)}")
                continue
            projects.append({"id": f"project-{n}", "title": str(item["title"]).strip(), "area": item["area"],
                             "cluster": str(areas[item["area"]].get("cluster", "")), "links": list(item.get("links") or [])})
        course["project_note"] = str(raw.get("note") or "")
    course["projects"] = projects

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
        plots = []
        raw_plot = fm.get("plot") or []
        for pl in (raw_plot if isinstance(raw_plot, list) else [raw_plot]):
            if not isinstance(pl, dict) or not pl.get("file") or not pl.get("title"):
                probs.error(where, "plot needs 'title' and 'file' (a file in site/plots/)")
                continue
            if not (PLOTS / str(pl["file"])).is_file():
                probs.error(where, f"plot file site/plots/{pl['file']} does not exist")
                continue
            plots.append({"title": str(pl["title"]), "url": f"plots/{pl['file']}"})
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
            "plots": plots,
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
    for p in course.get("projects", []):
        bad = [t for t in p["links"] if t not in cards]
        if bad:
            probs.error("projects.yml", f"'{p['title']}' links to {', '.join(bad)}, which are not cards")
        p["links"] = [t for t in p["links"] if t in cards]
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


# ---------- nearness: shared words and shared sources ----------
STOP = set("""a about above after again against all also am an and any are as at be because been before being below
between both but by can could did do does doing down during each either else even ever every few for from further had
has have having he her here hers him his how however i if in into is it its itself just less let like may me might
more most much must my no nor not now of off often on once one only or other ought our ours out over own per quite
rather same she should since so some such than that the their theirs them then there these they this those though
three through thus to too two under until up upon us use used uses using very via was we were what when where whether
which while who whom whose why will with within without would yet you your yours itself themselves first second
new get gets got make makes made way ways thing things something anything everything see seen say says said give
gives given take takes taken lot well many card cards day days lecture lectures note notes slide slides question
questions quiz answer sentence page pages example examples also e g i e eg ie etc versus vs exercise exercises
part parts chapter section sections remark called call known called kind kinds same different another
still together large small big break least open time times set group pass number unit network networks neural show
shows find finds work works good better best right hard easy far whole often exact exactly simple simply way
change changes changed law laws""".split())
WORD_RE = re.compile(r"[a-z][a-z0-9]+(?:-[a-z0-9]+)*")
URL_RE = re.compile(r"\((?:https?://|materials/|plots/)[^)\s]+\)")


def stem(w: str) -> str:
    w = re.sub(r"(?<=[a-z]{3})iz(e|ed|es|ing|ation|ations)$", r"is\1", w)
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 3 and w.endswith("s") and not w.endswith(("ss", "us", "is")):
        return w[:-1]
    return w


def words_of(card: dict) -> Counter:
    sec = card["sections"]
    c: Counter = Counter()
    def add(text: str, weight: float) -> None:
        text = URL_RE.sub(" ", text.lower())
        for tok in WORD_RE.findall(text):
            for part in tok.split("-") + ([tok] if "-" in tok else []):
                if len(part) >= 3 and part not in STOP and not part.isdigit():
                    c[stem(part)] += weight
    add(card["title"], 3.0)
    add(" ".join(map(str, card["aliases"])), 2.0)
    for k in ("statement", "twist", "safety", "question", "selftest", "notes"):
        add(sec.get(k, ""), 1.0)
    return c


ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})")
LINK_RE = re.compile(r"\[([^\]]+)\]\(((?:https?://|materials/)[^)\s]+)\)")


def sources_of(card: dict, course: dict) -> dict[str, str]:
    """Features a card shares with others: its days, the module, and every paper, page or file it cites.
    Maps a feature key to a readable label."""
    out: dict[str, str] = {}
    for d in card["days"]:
        out[f"day:{d}"] = f"Day {d}"
        lec = (course["days"].get(d) or {}).get("lecturer")
        if lec:
            out[f"lecturer:{lec}"] = f"lectures by {lec}"
    for label, url in LINK_RE.findall(card["sections"].get("sources", "")):
        m = ARXIV_RE.search(url)
        key = f"arxiv:{m.group(1)}" if m else re.sub(r"^https?://(www\.)?", "", url).split("#")[0].rstrip("/")
        out[key] = label if len(label) <= 70 else label[:67] + "..."
    return out


def tfidf(feats: dict[str, Counter], min_df: int = 2, max_df_frac: float = 0.2) -> dict[str, dict[str, float]]:
    n = len(feats)
    df: Counter = Counter()
    for f in feats.values():
        df.update(set(f))
    vecs = {}
    for cid, f in feats.items():
        v = {t: w * math.log(n / df[t]) for t, w in f.items() if min_df <= df[t] <= max_df_frac * n}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        vecs[cid] = {t: x / norm for t, x in v.items()}
    return vecs


def nearest(vecs: dict[str, dict[str, float]], k: int, labels=None) -> dict[str, list]:
    """For each card the k most similar cards (cosine), with the three shared features that count most."""
    inv: dict[str, list] = {}
    for cid, v in vecs.items():
        for t, x in v.items():
            inv.setdefault(t, []).append((cid, x))
    out = {}
    for cid, v in vecs.items():
        acc: Counter = Counter()
        why: dict[str, Counter] = {}
        for t, x in v.items():
            for other, y in inv[t]:
                if other != cid:
                    acc[other] += x * y
                    why.setdefault(other, Counter())[t] += x * y
        best = []
        for other, sc in acc.most_common(k):
            if sc < 0.04:
                break
            terms = [t for t, _ in why[other].most_common(3)]
            if labels:
                terms = [labels.get(t, t) for t in terms]
            best.append([other, round(sc, 3), terms])
        out[cid] = best
    return out


def proximity(cards: dict, course: dict) -> dict:
    words = nearest(tfidf({cid: words_of(c) for cid, c in cards.items()}), 8)
    labels: dict[str, str] = {}
    sfeats = {}
    for cid, c in cards.items():
        f = sources_of(c, course)
        labels.update(f)
        sfeats[cid] = Counter({k: 1.0 for k in f})
    sources = nearest(tfidf(sfeats, max_df_frac=0.35), 8, labels)
    cites = {cid: Counter({k: 1.0 for k in f if not k.startswith(("day:", "lecturer:"))}) for cid, f in sfeats.items()}
    return {"words": words, "sources": sources, "cites": nearest(tfidf(cites, max_df_frac=0.35), 8, labels)}


def spread_out(a, size, rounds: int = 60):
    """Push apart nodes that overlap, a little at a time, so that no node hides another."""
    import numpy as np
    a = a.copy() + np.stack([np.cos(np.arange(len(a))), np.sin(np.arange(len(a)))], 1) * 1e-3   # split exact ties
    rad = np.array(size, dtype=float) / 2
    need = (rad[:, None] + rad[None, :]) * 1.25 + 6         # wanted distance between centres
    np.fill_diagonal(need, 0)
    for _ in range(rounds):
        d = a[:, None, :] - a[None, :, :]
        dist = np.maximum(np.sqrt((d ** 2).sum(-1)), 1e-6) + np.eye(len(a))
        push = np.clip(need - dist, 0, None) / dist / 2
        np.fill_diagonal(push, 0)
        if push.max() <= 0:
            break
        a += (d * push[:, :, None]).sum(1) * 0.5
    return a


def near_layout(near: dict[str, list], ref: dict, sizes: dict, k: int = 4) -> dict[str, tuple[float, float]]:
    """A layout in which cards that are near (by one notion) sit close. Each card is joined to its k nearest;
    edge length falls as similarity rises; Kamada-Kawai then places the cards, and the result is turned and
    scaled to match the layout by links as closely as possible, so that switching moves the cards as little as it can."""
    import numpy as np
    g = nx.Graph()
    g.add_nodes_from(near)
    for a, lst in near.items():
        for b, sc, _ in lst[:k]:
            length = 1.0 - min(0.85, sc)
            if not g.has_edge(a, b) or g[a][b]["length"] > length:
                g.add_edge(a, b, length=length)
    # Distances along the near-graph; groups that are not joined at all are kept apart at a fixed, larger distance,
    # so that every card is placed (for sources, the days form groups of their own).
    sp = dict(nx.shortest_path_length(g, weight="length"))
    far = 1.25 * max(d for row in sp.values() for d in row.values())
    ids = sorted(g)
    dist = {a: {b: sp[a].get(b, far) for b in ids} for a in ids}
    scale = 90 * math.sqrt(len(ids))
    p = nx.kamada_kawai_layout(g, dist=dist, scale=scale)
    # Procrustes: turn (or mirror) and scale onto the links layout, so that switching moves the cards as little as it can
    a = np.array([p[n] for n in ids]); b = np.array([ref[n] for n in ids])
    am, bm = a.mean(0), b.mean(0)
    u, sv, vt = np.linalg.svd((a - am).T @ (b - bm))
    r = u @ vt
    sc = math.sqrt(((b - bm) ** 2).sum() / ((a - am) ** 2).sum())   # same spread as the links layout
    a2 = spread_out((a - am) @ r * sc + bm, [sizes.get(n, 18) for n in ids])
    pos = {n: (float(x), float(y)) for n, (x, y) in zip(ids, a2)}
    return pos


def hidden_connections(g: nx.MultiDiGraph, prox: dict, top: int = 12) -> list:
    """Pairs of cards that are close in words and in sources but have no link: candidates for a new link."""
    u = nx.Graph(g.to_undirected())
    score: dict[tuple, float] = {}
    why: dict[tuple, list] = {}
    for mode, wt in (("words", 1.0), ("cites", 0.3)):
        for a, lst in prox[mode].items():
            for b, sc, terms in lst:
                key = tuple(sorted((a, b)))
                if mode == "words":
                    if len(terms) < 2:
                        continue                             # one shared word is too weak a hint
                elif key not in score:
                    continue                                 # a shared source alone is not enough: the texts must meet too
                score[key] = score.get(key, 0.0) + wt * sc / 2      # each pair is seen from both ends
                why.setdefault(key, [])
                for t in terms:
                    if t not in why[key] and len(why[key]) < 4:
                        why[key].append(t)
    out, seen = [], Counter()
    for (a, b), sc in sorted(score.items(), key=lambda kv: -kv[1]):
        if u.has_edge(a, b) or nx.has_path(u, a, b) and nx.shortest_path_length(u, a, b) <= 2:
            continue                                         # already linked, or one step apart
        if set(g.nodes[a]["days"]) & set(g.nodes[b]["days"]):
            continue                                         # same day: the interesting ones cross days
        if "stub" in (g.nodes[a]["status"], g.nodes[b]["status"]):
            continue
        if seen[a] >= 2 or seen[b] >= 2:
            continue                                         # at most two pairs per card, so the list stays varied
        seen[a] += 1; seen[b] += 1
        out.append([a, b, round(sc, 3), why.get((a, b), [])])
        if len(out) >= top:
            break
    return out


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


def to_payload(course: dict, g: nx.MultiDiGraph, pos: dict, st: dict, template: str, prox: dict, alt: dict) -> dict:
    u = nx.Graph(g.to_undirected())
    nodes = []
    for n, d in g.nodes(data=True):
        x, y = pos.get(n, (0.0, 0.0))
        nodes.append({
            "id": n, "title": d["title"], "kind": d["kind"], "days": d["days"], "module": d["module"],
            "cluster": d["cluster"], "by": d["by"], "origin": d["origin"], "load_bearing": d["load_bearing"], "aliases": d["aliases"],
            "status": d["status"], "sections": d["sections"], "path": d["path"], "plots": d["plots"],
            "degree": u.degree(n), "x": round(x, 1), "y": round(y, 1),
            "alt": {m: [round(alt[m][n][0], 1), round(alt[m][n][1], 1)] for m in alt},
            "near": {m: prox[m].get(n, [])[:6] for m in ("words", "sources")},
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
            "project_note": course.get("project_note", ""),
        },
        "projects": course.get("projects", []),
        "hidden": hidden_connections(g, prox),
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
    pos = layout(g)                                    # the layouts run in --check too, so a failure shows on the pull request
    prox = proximity(cards, course)
    u = nx.Graph(g.to_undirected())
    sizes = {n: 18 + 15 * math.sqrt(u.degree(n)) for n in u}      # node diameter on the page, as in the template
    alt = {m: near_layout(prox[m], pos, sizes) for m in ("words", "sources")}
    if args.check:
        return 0

    template = (CONCEPTS / "_template.md").read_text(encoding="utf-8")
    payload = to_payload(course, g, pos, st, template, prox, alt)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    if PLOTS.is_dir():                                 # the interactive plots that cards link to
        shutil.copytree(PLOTS, out / "plots", dirs_exist_ok=True)
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
