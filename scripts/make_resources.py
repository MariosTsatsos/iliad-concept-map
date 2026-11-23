"""Builds resources.yml for the concept map from the links found in the lecture files.
Not part of the normal build: it needs the lecture files, which are not stored in this repository.
Usage: python scripts/make_resources.py resources.yml   (set UP below to the folder that holds the files)
Every entry keeps the file and page it was found on. Titles are the linked text on the slide, or the citation printed there."""
import os, re, subprocess, sys, collections, yaml, logging
import pypdf, docx
logging.getLogger("pypdf").setLevel(logging.ERROR)
UP = "/mnt/user-data/uploads/Iliad Intensive"
def anchors(fname):
    """[(page, url, linked text, slide title)] for every link annotation, in document order"""
    p = os.path.join(UP, fname); out = []
    r = pypdf.PdfReader(p)
    txt = subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, text=True).stdout.split("\f")
    for i, pg in enumerate(r.pages, 1):
        annots = pg.get("/Annots") or []
        if not annots: continue
        H = float(pg.mediabox.height)
        title = next((l.strip() for l in (txt[i-1] if i-1 < len(txt) else "").split("\n") if l.strip()), "")
        for a in annots:
            try:
                a = a.get_object(); act = a.get("/A")
                if not (act and act.get("/URI")): continue
                x0, y0, x1, y1 = [float(v) for v in a["/Rect"]]
                c = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-r", "72", "-x", str(int(min(x0, x1)) - 1), "-y", str(int(H - max(y0, y1)) - 1),
                                    "-W", str(int(abs(x1 - x0)) + 2), "-H", str(int(abs(y1 - y0)) + 2), p, "-"], capture_output=True, text=True).stdout
                out.append((i, str(act["/URI"]).strip(), " ".join(c.split()), title))
            except Exception: pass
    return out
def uniq(rows):
    seen = collections.OrderedDict()
    for pg, url, anc, title in rows:
        k = re.sub(r"^https?://(www\.)?", "", url).rstrip("/")
        if k not in seen: seen[k] = (pg, url, anc, title)
        elif len(anc) > len(seen[k][2]) and not seen[k][2].strip(" ,.;:"): seen[k] = (seen[k][0], url, anc, title)
    return list(seen.values())
def clean(t):
    t = re.sub(r"\s+—\s+(LessWrong|AI Alignment Forum)$", "", t.strip())
    return t.strip(" ,;").rstrip(".")
RES = collections.defaultdict(list)
def add(day, kind, title, url, src):
    url = url.strip().rstrip(".,;")
    key = re.sub(r"^https?://(www\.)?", "", url).rstrip("/")
    if any(re.sub(r"^https?://(www\.)?", "", e["url"]).rstrip("/") == key for e in RES[day]): return
    assert kind in ("exercise", "tool", "reading"), kind
    assert title and len(title) >= 4, (day, title, url)
    RES[day].append({"kind": kind, "title": title, "url": url, "from": src})
def pick(rows, sub):
    hits = [r for r in rows if sub in r[1]]
    assert hits, "no link containing " + sub
    return hits[0]

# ---------- Day 1
f = "Day  1 - iliad_ml_engineering-day1.pdf"; rows = uniq(anchors(f))
names = {"02_optimizers": "Implement optimizers (Colab notebook)", "04_mlp": "Build an MLP (Colab notebook)", "05_attention": "Implement attention (Colab notebook)"}
for pg, url, anc, t in rows:
    for k, v in names.items():
        if "colab" in url and k in url: add(1, "exercise", v, url, f"Day 1 slides, page {pg}")
    if "1607.06450" in url: add(1, "reading", "LayerNorm paper (arXiv:1607.06450)", url, f"Day 1 slides, page {pg}")

# ---------- Day 2: links placed on the slides
f = "Day 2 - alignment-nov3.pdf"; rows = uniq(anchors(f))
over = {"intelligence.org/files/CEV.pdf": "Yudkowsky, CEV (2004)", "2511.18397": "MacDiarmid et al., Natural emergent misalignment from reward hacking (2025)",
        "FDJnZt8Ks2djouQTZ": "Hubinger, How do we become confident in the safety of a machine learning system? (2021)",
        "2026/reward-seeker": "Training a misaligned reward seeker (Anthropic alignment blog, 2026)", "lesswrong.com/w/corrigibility": "Corrigibility (LessWrong wiki)",
        "2401.05566": "Sleeper agents (arXiv:2401.05566)", "research/reward-tampering": "Sycophancy to subterfuge (Anthropic)", "research/alignment-faking": "Alignment faking (Anthropic)",
        "q25-2026-timelines-update": "AI 2027: August 2026 update", "security-incident-july-2026": "Hugging Face disclosure (July 2026)"}
for pg, url, anc, t in rows:
    title = next((v for k, v in over.items() if k in url), clean(anc))
    add(2, "reading", title, url, f"Day 2 slides, page {pg}")

# ---------- Day 3
pg, url, anc, t = pick(uniq(anchors("Day 3 - Iliad_Intensive_RL_Exercises.pdf")), "arena.education")
add(3, "exercise", "ARENA: Intro to RL (chapter 2)", url, f"Day 3 exercise sheet, page {pg}")
pg, url, anc, t = pick(uniq(anchors("Day 3 - notes_preferences-rewards.pdf")), "2212.10420")
add(3, "reading", "Settling the reward hypothesis (arXiv:2212.10420)", url, f"Day 3 notes, page {pg}")

# ---------- Day 4: the reading agenda
f = "Day 4 - Agent Foundations day_ November 5th Iliad intensive.pdf"; rows = uniq(anchors(f))
skip4 = ("drive.google.com", "lri.fr", "dl1.cuni.cz", "archive.org")
over = {"goodreads.com": "Surreal Numbers (book, Goodreads page)", "pPWiLGsWCtN92vLwu": "Orientation (LessWrong sequence post)", "S8kAJamj66gekjBwC": "Knowing (LessWrong sequence post)",
        "bRcsFM6jm272ELyx8": "The Territory (LessWrong sequence post)"}
left4 = []
for pg, url, anc, t in rows:
    if any(s in url for s in skip4): left4.append((pg, anc, url)); continue
    title = next((v for k, v in over.items() if k in url), clean(anc)).strip('"“”')
    add(4, "exercise" if title.lower().startswith("exercise") else "reading", title, url, f"Day 4 reading agenda, page {pg}")

# ---------- Day 5
f = "Day 5 -Alignment in practice November (3).pdf"; rows = uniq(anchors(f))
over = {"pretraining-data-filtering": "Anthropic, Pretraining data filtering (2025)", "selective-gradient-masking": "Anthropic, Selective gradient masking, SGTM (2025)",
        "2026/psm": "Anthropic, The persona selection model (2026)", "anthropic.com/constitution": "Anthropic, the Claude constitution",
        "model-spec.openai.com": "OpenAI, Model Spec (18 Aug 2026)", "teaching-claude-why": "Anthropic, Teaching Claude Why (2026)",
        "threat-intelligence-report": "Anthropic, threat intelligence report (September 2026)", "2501.18837": "Constitutional Classifiers (arXiv:2501.18837)",
        "time.com": "TIME100 AI 2025: Pliny the Liberator", "medium.com": "Decoding the Elder Plinius repository (Medium)",
        "responsible-scaling-policy": "Anthropic, Responsible Scaling Policy", "preparedness-framework": "OpenAI, Preparedness Framework (update)", "pacing.tech": "pacing.tech: pacing the frontier"}
for pg, url, anc, t in rows:
    title = next((v for k, v in over.items() if k in url), None); assert title, url
    add(5, "reading", title, url, f"Day 5 slides, page {pg}")

# ---------- Day 6 (links printed as text)
t = subprocess.run(["pdftotext", "-f", "38", "-l", "38", os.path.join(UP, "Day 6 - recursive_debate_fellowship_talk.pdf"), "-"], capture_output=True, text=True).stdout
u1 = re.search(r"https://www\.lesswrong\.com/posts/\w+/synthetic-scalable-oversight", t).group(0); u2 = re.search(r"https://www\.lesswrong\.com/posts/\w+/local-factor-graph-debate", t).group(0)
add(6, "reading", "Heckett, Gour, Ahuja, Rowney, Shah, Synthetic Scalable Oversight (LessWrong, July 2026)", u1, "Day 6 slides on recursive debate, page 38")
add(6, "reading", "Heckett, Local Factor Graph Debate (LessWrong, September 2026)", u2, "Day 6 slides on recursive debate, page 38")
t = subprocess.run(["pdftotext", "-f", "2", "-l", "2", os.path.join(UP, "Day 6 - safety_case_slides.pdf"), "-"], capture_output=True, text=True).stdout
assert "arXiv:2505.03989" in t and "An alignment safety case sketch based on debate" in " ".join(t.split())
add(6, "reading", "Buhl, Pfau, Hilton and Irving, An alignment safety case sketch based on debate (2025)", "https://arxiv.org/abs/2505.03989", "Day 6 slides on the safety case, page 2")

# ---------- Day 7
pg, url, anc, t = pick(uniq(anchors("Day 7 - reinforcement-learning-nosol.pdf")), "arena.education")
add(7, "exercise", "ARENA: Intro to RL (chapter 2)", url, f"Day 7 reinforcement learning exercises, page {pg}")
for pg, url, anc, t in uniq(anchors("Day 7 - ML Foundations Iliad Intensive Julian Schulz.pdf")):
    if "colab" in url:
        a = clean(anc); a = a if a.lower().startswith("exercise") else "Exercise: " + a
        add(7, "exercise", a + " (Colab notebook)", url, f"Day 7 ML foundations slides, page {pg}")
    elif "playground.tensorflow.org" in url: add(7, "tool", "TensorFlow Playground (Exercise 4: hyperparameter tuning)", url, f"Day 7 ML foundations slides, page {pg}")
rows = uniq(anchors("Day 7  - aixi-nosol.pdf"))
for sub, title in [("hutter1.net/publ/uaibook2.pdf", None), ("hutter1.net/ai/uaibook.htm", None), ("1510.04931", None), ("10.1214/aoms", None)]:
    pg, url, anc, t = pick(rows, sub)
    extra = {"hutter1.net/publ/uaibook2.pdf": " (book, PDF on the author's site)", "hutter1.net/ai/uaibook.htm": " (book page)", "1510.04931": " (arXiv:1510.04931)", "10.1214/aoms": " (paper)"}[sub]
    add(7, "reading", clean(anc) + extra, url, f"Day 7 AIXI exercises, page {pg}")
pg, url, anc, t = pick(uniq(anchors("Day 7 - solomonoff-induction-nosol.pdf")), "lesswrong.com/posts")
slug = url.rstrip("/").split("/")[-1]
add(7, "reading", "LessWrong post linked in the exercises: " + slug.replace("-", " "), url, f"Day 7 Solomonoff induction exercises, page {pg}")
rows = uniq(anchors("Day 7 - 2.1-intro-to-rl.pdf"))
pg, url, anc, t = pick(rows, "springer.com"); add(7, "reading", "Paper linked on the Q-learning slide (convergence conditions)", url, f"Day 7 intro to RL slides, page {pg}")
pg, url, anc, t = pick(rows, "tor-lattimore.com"); add(7, "reading", "Book linked on the exploration slide (tor-lattimore.com)", url, f"Day 7 intro to RL slides, page {pg}")

# ---------- Day 8
f = "Day 8 - HeuristicArgumentsFinal.pdf"; rows = uniq(anchors(f))
over = {"2204.06974": "Goldwasser, Kim, Vaikuntanathan, Zamir, Planting undetectable backdoors in ML models (2022)", "2409.03077": "Christiano, Hilton, Lecomte, Xu, Backdoor defense, learnability and obfuscation (2024)",
        "2008.09317": "Jain, Lin, Sahai, Indistinguishability obfuscation from well-founded assumptions (2021)", "2406.11779": "Gross et al., Compact proofs of model performance via mechanistic interpretability (2024)",
        "vwt3wKXWaCvqZyF74": "Christiano, Mechanistic anomaly detection and ELK (2022)", "PwnadG4BFjaER3MGf": "Nanda, Interpretability will not reliably find deceptive AI (2025)",
        "a-computational-no-coincidence-principle": "A computational no-coincidence principle (ARC blog)", "competing-with-sampling": "Competing with sampling (ARC blog)",
        "MxPhi-Gowers2023": "Gowers, What makes mathematicians believe unproved mathematical statements? (2023)",
        "2605.05179": "Wu, Lecomte, Winer, R., Hilton, Christiano, Estimating the expected output of wide random MLPs more efficiently than sampling (2026)",
        "mechanistic-estimation-for-expectations": "Hilton et al., Mechanistic estimation for expectations of random products (2026)", "algzoo": "Hilton, AlgZoo (2026)"}
for pg, url, anc, t in rows:
    title = next((v for k, v in over.items() if k in url), None); assert title, url
    add(8, "reading", title, url, f"Day 8 slides, page {pg}")

# ---------- Day 9: the reading list in the schedule
d = docx.Document(os.path.join(UP, "Day 9 - november-schedule-multi-agent-systems.docx"))
paras = [p.text.strip() for p in d.paragraphs if p.text.strip()]
for para in paras:
    m = re.search(r"arXiv\s*(\d{4}\.\d{4,5})", para)
    if not m: continue
    title = re.sub(r"\s*arXiv\s*%s\.?$" % re.escape(m.group(1)), "", para).strip().rstrip(".")
    title = re.sub(r"\.\s*(NeurIPS|AAMAS)\s*20\d\d$", "", title).strip().rstrip(".")
    add(9, "reading", title, "https://arxiv.org/abs/" + m.group(1), "Day 9 schedule and reading list")

# ---------- Day 10
f = "Day 10 - Mech Interp.pdf"; rows = uniq(anchors(f))
tools = {"gemma-3-27b": "Neuronpedia: Gemma 3 27B, Gemma Scope 2 features", "gemma-2-2b/graph": "Neuronpedia: attribution graphs for Gemma 2 2B",
         "llama3.3-70b-it/nla": "Neuronpedia: natural language autoencoder (NLA) for Llama 3.3 70B", "deepseek-v4-flash/jlens": "Neuronpedia: J-lens for DeepSeek V4 Flash"}
for pg, url, anc, t in rows:
    if "x.com/" in url: continue
    if "colab" in url: add(10, "exercise", "Logit lens exercise: " + ("hard" if "hard" in anc.lower() else "normal") + " (Colab notebook)", url, f"Day 10 mechanistic interpretability slides, page {pg}")
    elif "neuronpedia" in url:
        title = next((v for k, v in tools.items() if k in url), None); assert title, url
        add(10, "tool", title, url, f"Day 10 mechanistic interpretability slides, page {pg}")
    else: add(10, "reading", clean(anc), url, f"Day 10 mechanistic interpretability slides, page {pg}")
f = "Day 10 - Steganography.pdf"; rows = uniq(anchors(f))
pg, url, anc, t = pick(rows, "colab"); add(10, "exercise", "Exercise 1: Watermarking (Colab notebook)", url, f"Day 10 steganography slides, page {pg}")
pg, url, anc, t = pick(rows, "iliad-intensive.org/safety/steganography"); add(10, "exercise", "Exercise: Backdoor via Random ReLU Measurements (course page)", url, f"Day 10 steganography slides, page {pg}")

# ---------- Day 11
pg, url, anc, t = pick(uniq(anchors("Day 11 - Iliad-Intensive-Talk (5).pdf")), "ProofsArgsAndZK")
add(11, "reading", "Thaler's book: Proofs, Arguments, and Zero-Knowledge (PDF on the author's page)", url, f"Day 11 slides, page {pg}")

# ---------- Day 13
rows = uniq(anchors("Day 13 - lecture1-equilibrium.pdf"))
pg, url, anc, t = pick(rows, "iliad-intensive.org/learning/qft"); add(13, "reading", "Czejdo, Dimofte, Grado-White, Renshaw-Whitman, Physics of Deep Learning (notes for earlier runs of this day)", url, f"Day 13 lecture 1 slides, page {pg}")
pg, url, anc, t = pick(rows, "2604.21691"); add(13, "reading", "Simon et al., There Will Be a Scientific Theory of Deep Learning (2026)", url, f"Day 13 lecture 1 slides, page {pg}")
pg, url, anc, t = pick(rows, "2106.10165"); add(13, "reading", "Roberts, Yaida, Hanin, The Principles of Deep Learning Theory (Cambridge, 2022)", url, f"Day 13 lecture 1 slides, page {pg}")

# ---------- Day 15: courses, videos, theses and exercises from the notes' reading list
f = "Day 15 - Oxford_SLT_Course__Lecture_1-5.pdf"; rows = uniq(anchors(f))
sel = [("lesswrong.com/s/czrXjvCLsqGepybHC", "reading", "Carroll, Distilling singular learning theory (LessWrong sequence, 2023)"),
       ("lesswrong.com/posts/3HYqTAi4kD35G3BzQ", "exercise", "Furman, Singular learning theory: Exercises (LessWrong, 2024)"),
       ("therisingsea.org/notes/MSc-Carroll.pdf", "reading", "Carroll, Phase Transitions in Neural Networks (Master's thesis, 2021)"),
       ("far.in.net/mthesis", "reading", "Farrugia-Roberts, Structural Degeneracy in Neural Networks (Master's thesis)"),
       ("iliad-intensive.org/learning/mysteries-of-deep-learning", "reading", "Furman, Mysteries of deep learning: reading guide (Iliad Intensive, 2026)"),
       ("sumiowatanabe/home/singular-learning-theory-2", "reading", "Watanabe, Singular learning theory, part 2 (2023)"),
       ("sumiowatanabe/home/singular-learning-theory", "reading", "Watanabe, Singular learning theory, part 1 (2023)")]
for sub, kind, title in sel:
    hit = [r for r in rows if r[1].rstrip("/").endswith(sub.split("/")[-1]) and sub.split("/")[0] in r[1]]; assert len(hit) == 1, (sub, hit)
    add(15, kind, title, hit[0][1], f"Day 15 SLT notes, page {hit[0][0]}")
# the two video series: check which reference each YouTube link belongs to
p = os.path.join(UP, f); r = pypdf.PdfReader(p)
for i in (58, 59, 60):
    pg = r.pages[i-1]; H = float(pg.mediabox.height)
    for a in (pg.get("/Annots") or []):
        a = a.get_object(); act = a.get("/A")
        if not (act and act.get("/URI") and "youtube.com" in str(act["/URI"])): continue
        x0, y0, x1, y1 = [float(v) for v in a["/Rect"]]
        c = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-r", "72", "-x", "0", "-y", str(int(H - max(y0, y1)) - 16), "-W", "700", "-H", "30", p, "-"], capture_output=True, text=True).stdout
        c = " ".join(c.split()); url = str(act["/URI"])
        which = "low road" if "low road" in c else ("high road" if "high road" in c else None); assert which, c
        who = "Lau and Chen" if which == "low road" else "Murfet and Carroll"
        add(15, "reading", f"{who}, Singular learning theory: The {which} (lecture series, YouTube, 2023)", url, f"Day 15 SLT notes, page {i}")
pg, url, anc, t = pick(uniq(anchors("Kai-Miguel/Bayes vs SGD.pdf")), "lesswrong.com/posts")
add(15, "reading", clean(anc) + " (LessWrong)", url, f"Slides 'Bayes vs SGD', page {pg}")

# ---------- Day 16
add(16, "exercise", "Learning dynamics: exercise notebook (Colab)", "https://colab.research.google.com/drive/1LijVg6IvVw1KG9BkN9PJsfbW3vFo-laC?usp=sharing", "shared with participants on the day")
rows = uniq(anchors("Day 16 - reading_list.pdf"))
rl = [("1810.10531", "Saxe, McClelland, Ganguli, A mathematical theory of semantic development in deep neural networks (PNAS 2019)"),
      ("2012.04728", "Kunin, Sagastuy-Brena, Ganguli, Yamins, Tanaka, Neural mechanics: symmetry and broken conservation laws in deep learning dynamics (ICLR 2021)"),
      ("2411.09004", "Menon, The geometry of the deep linear network (2024)"),
      ("proceedings.iclr.cc", "Zhang, Saxe, Latham, Saddle-to-saddle dynamics explains a simplicity bias across neural network architectures (ICLR 2026)"),
      ("proceedings.neurips.cc", "Kunin, Marchetti, Chen, Karkada, Simon, DeWeese, Ganguli, Miolane, Alternating gradient flows: a theory of feature learning in two-layer neural networks (NeurIPS 2025)"),
      ("2011.09468", "Pezeshki, Kaba, Bengio, Courville, Precup, Lajoie, Gradient starvation: a learning proclivity in neural networks (NeurIPS 2021)")]
for sub, title in rl:
    pg, url, anc, t = pick(rows, sub); add(16, "reading", title, url, f"Day 16 reading list, page {pg}")
rows = uniq(anchors("Day 16 - intro_training_dynamics.pdf"))
for sub, title in [("1911.08731", "Sagawa, Koh, Hashimoto, Liang, Distributionally robust neural networks for group shifts (ICLR 2020)"),
                   ("2502.17424", "Betley et al., Emergent misalignment: narrow finetuning can produce broadly misaligned LLMs (2025)"),
                   ("2507.14805", "Cloud et al., Subliminal learning: language models transmit behavioral traits via hidden signals in data (2025)"),
                   ("2604.21691", "Simon, Kunin, et al., There will be a scientific theory of deep learning (2026)")]:
    pg, url, anc, t = pick(rows, sub); add(16, "reading", title, url, f"Day 16 intro slides, page {pg}")

# ---------- titles that the automatic step cut short
FIX = {(4, "new-paper-logical-induction"): 'New paper: "Logical induction" (MIRI)',
       (4, "2208.07006"): "Cooperative and uncooperative institution designs: Surprises and problems in open-source game theory",
       (7, "hutter1.net/ai/uaibook.htm"): "Universal Artificial Intelligence: Sequential Decisions Based on Algorithmic Probability (book page)",
       (7, "HSDumToH57nSRdLST"): "A technical introduction to Solomonoff induction without K-complexity (LessWrong)"}
for (day, sub), title in FIX.items():
    hit = [e for e in RES[day] if sub in e["url"]]; assert len(hit) == 1, (day, sub, len(hit))
    hit[0]["title"] = title
w = [e for e in RES[15] if "sumiowatanabe" in e["url"]]; assert len(w) == 2
i1, i2 = RES[15].index(w[0]), RES[15].index(w[1]); RES[15][i1], RES[15][i2] = RES[15][i2], RES[15][i1]
print("solomonoff slug:", [e["url"].split("/")[-1] for e in RES[7] if "HSDumToH57nSRdLST" in e["url"]])

# ---------- write
order = {"exercise": 0, "tool": 1, "reading": 2}
out = {d: sorted(v, key=lambda e: order[e["kind"]]) for d, v in sorted(RES.items())}
head = """# Links found in the lecture files, by course day. Shown on the map when a day is selected.
# kind: exercise (notebooks, exercise pages), tool (things to try in the browser), reading (papers, posts, books, videos).
# 'from' says where the link was found. Titles are the linked text on the slide, or the citation printed there.
# What is listed: every exercise and tool link; reading that a lecturer put on a slide, a reading list or an agenda.
# What is not listed: entries that appear only in a bibliography at the end of a deck, private share links, and links to scanned books.
"""
dst = sys.argv[1]
open(dst, "w").write(head + yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=1000))
print("written", dst, "|", {d: collections.Counter(e["kind"] for e in v) for d, v in out.items()})
print("total:", sum(len(v) for v in out.values()), "| left out of Day 4:", [(p_, a_[:40]) for p_, a_, u_ in left4])
