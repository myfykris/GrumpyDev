"""Unblind judge scores and summarize per arm and model.

Usage: aggregate.py <work_dir> <packet_name> [<packet_name> ...]

Reads <work>/maps/<name>-map.json (from packet.py), <work>/judge/<name>-scores.json (the
format in tools/eval/judge.md), and run usage from <work>/agents.tsv
(run, agentId, tokens, tool_uses, duration_ms) plus any <work>/*-usage.tsv in the same
column order without the agentId. The packet name starts with the scenario (for example
"baudit-sonnet" is scenario baudit). Key items are read from the scenario's answer key:
every "- ID" item that is not a penalty (X...). Stops with an error when a score or an
item is missing instead of counting it as zero."""
import glob, json, os, re, statistics as st, sys

EVAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYS = {"s1": "s1", "s2": "s2", "s3": "s3", "s5": "s5", "s1r2": "s1r2", "xs2": "s1r2", "pin": "pin",
        "upgrade": "upgrade", "research": "research", "bplan": "boundaries-plan",
        "baudit": "boundaries-audit", "touch": "touch", "touchseed": "touchseed"}
EXTRA = ("CAL", "T", "TC", "SPLIT", "R", "V", "H", "K")
META = ("valid_material", "valid_minor", "invalid", "snr")

def items(scen):
    text = open(os.path.join(EVAL, "keys", KEYS[scen] + ".md"), encoding="utf-8").read()
    ids = re.findall(r"^- \**([A-Z]{1,3}[0-9]*)\b", text, re.M)
    return [i for i in ids if not i.startswith("X") and i != "PB"]  # PB is a bonus item

def usage(work):
    u = {}
    for line in open(os.path.join(work, "agents.tsv")):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 5 and p[1] != "ERROR":
            u[p[0]] = (int(p[2]), int(p[3]), int(p[4]))
    for f in glob.glob(os.path.join(work, "*-usage.tsv")):
        for line in open(f):
            p = line.rstrip("\n").split("\t")
            if len(p) == 4 and p[1].isdigit():
                u[p[0]] = (int(p[1]), int(p[2]), int(p[3]))
    return u

def fail(msg):
    sys.exit(f"aggregate: {msg}")

work = sys.argv[1]
use = usage(work)
for name in sys.argv[2:]:
    scen = name.split("-")[0]
    if scen not in KEYS:
        fail(f"unknown scenario for packet {name}")
    keys = items(scen) if scen != "touchseed" else ["C1"]  # C2 and C3 are error counts
    mp = json.load(open(os.path.join(work, "maps", f"{name}-map.json")))
    sc = json.load(open(os.path.join(work, "judge", f"{name}-scores.json")))
    rows = []
    for label, run in mp.items():
        if label not in sc:
            fail(f"{name}: no scores for {label} ({run})")
        r = sc[label]
        missing = [k for k in keys + list(META) if k not in r]
        if missing:
            fail(f"{name}: {label} ({run}) lacks {missing}")
        total = sum(float(r[k]) for k in keys)
        extra = {k: r[k] for k in EXTRA if k in r and k not in keys}
        pens = {k: r[k] for k in r if re.fullmatch(r"X[A-Z]*[0-9]+", k) or (scen == "touchseed" and k in ("C2", "C3"))}
        arm = "-".join(run.split("-")[1:2]); model = run.split("-")[2]
        rows.append((arm, model, run, total, extra, pens, r["invalid"], r["snr"], use.get(run)))
    print(f"\n{name}: key items {' '.join(keys) or '(none)'}")
    for arm, model, run, total, extra, pens, inv, snr, u in sorted(rows):
        us = f"tokens={u[0]} tools={u[1]} min={u[2] / 60000:.1f}" if u else "usage=?"
        print(f"  {run:28s} key={total:<5g} {extra} {pens} invalid={inv} snr={snr} {us}")
    groups = {}
    for arm, model, run, total, extra, pens, inv, snr, u in rows:
        groups.setdefault((arm, model), []).append((total, inv, snr, u))
    for (arm, model), g in sorted(groups.items()):
        toks = [x[3][0] for x in g if x[3]]
        print(f"  = {arm}/{model}: n={len(g)} key={st.mean(x[0] for x in g):.2f} "
              f"invalid={st.mean(x[1] for x in g):.2f} snr={st.mean(x[2] for x in g):.2f} "
              f"tokens={st.mean(toks):.0f}" if toks else
              f"  = {arm}/{model}: n={len(g)} key={st.mean(x[0] for x in g):.2f} usage=?")
