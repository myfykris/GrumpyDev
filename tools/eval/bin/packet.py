"""Build a blinded judge packet from <dir>/results/<run>.md.
Usage: packet.py <dir> <name> <run1,run2,...>
Writes <dir>/judge/<name>-packet.md and <dir>/maps/<name>-map.json (keep maps away from judges)."""
import json, os, random, re, sys
D, name, runs = sys.argv[1], sys.argv[2], sys.argv[3].split(",")
random.seed(sum(map(ord, name)))
random.shuffle(runs)
parts, mapping = [], {}
for i, r in enumerate(runs, 1):
    t = open(os.path.join(D, "results", r + ".md"), encoding="utf-8").read()
    t = "\n".join(l for l in t.splitlines()
                  if "GRUMPYDEV_CONTEXT" not in l and not re.match(r"\s*Ledger:", l))
    t = re.sub(r"/\S*/runs/[a-zA-Z]+-[a-zA-Z]+-[a-z]+/?", "", t)
    t = re.sub(r"/Users/\S+", "<path>", t)
    t = re.sub(r"\.claude/skills/\S*", "<instructions>", t)
    t = re.sub(r"\b(?:GD|TMP)-(\d{3})\b", r"ID-\1", t)
    t = re.sub(r"(?i)\.grumpydev/\S*", "<tracking file>", t)
    t = re.sub(r"`?\.grump`?", "the project notes", t)
    t = re.sub(r"GrumpyDev|Grump(?:ed|ing)?\b", "the reviewer", t)
    label = f"R{i}"
    mapping[label] = r
    parts.append(f"\n\n==================== REVIEW {label} ====================\n\n{t.strip()}\n")
for d in ("judge", "maps"):
    os.makedirs(os.path.join(D, d), exist_ok=True)
open(os.path.join(D, "judge", f"{name}-packet.md"), "w", encoding="utf-8").write("".join(parts))
json.dump(mapping, open(os.path.join(D, "maps", f"{name}-map.json"), "w"), indent=1)
print(name, len(runs), "reviews,", sum(len(p) for p in parts), "chars")
