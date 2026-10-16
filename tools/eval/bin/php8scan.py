"""Flag PHP 8-only syntax and APIs in PHP files (a static stand-in for running on 7.4).
Usage: php8scan.py <dir> [<dir>...]   Prints one line per hit and a total."""
import os, re, sys
RULES = [
    ("match expression", r"\bmatch\s*\("),
    ("nullsafe operator", r"\?->"),
    ("enum", r"^\s*enum\s+\w+"),
    ("readonly", r"\breadonly\s+(class|public|protected|private|function|\??\w)"),
    ("constructor promotion", r"function\s+__construct\s*\([^)]*\b(public|protected|private)\s+"),
    ("union type", r"[(,]\s*\??[A-Za-z_\\]+\|[A-Za-z_\\]+\s+\$"),
    ("union return type", r"\)\s*:\s*\??[A-Za-z_\\]+\|[A-Za-z_\\|]+"),
    ("mixed type", r"[(,:]\s*\??mixed\b"),
    ("static return type", r"\)\s*:\s*static\b"),
    ("never type", r"\)\s*:\s*never\b"),
    ("attribute", r"^\s*#\["),
    ("str_contains/starts/ends", r"\bstr_(contains|starts_with|ends_with)\s*\("),
    ("array_is_list", r"\barray_is_list\s*\("),
    ("throw expression", r"(\?\?|=>|\?:)\s*throw\b"),
    ("named argument", r"\b\w+\s*\(\s*[a-z_][a-zA-Z0-9_]*\s*:\s*[^:]"),
    ("new in initializer", r"function\s*\w*\s*\([^)]*=\s*new\s"),
    ("first-class callable", r"\w\(\.\.\.\)"),
]
hits = 0
for root_arg in sys.argv[1:]:
    for root, dirs, files in os.walk(root_arg):
        dirs[:] = [d for d in dirs if d not in (".git", "vendor", ".claude", ".grumpydev")]
        for f in files:
            if not f.endswith(".php"):
                continue
            p = os.path.join(root, f)
            for n, line in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
                code = line.split("//")[0]
                for name, rx in RULES:
                    if re.search(rx, code):
                        if name == "named argument" and re.search(r"\b(case|default|function|fn|static|self|parent)\b|::|\?\s*$|\bnew\b.*\?", code):
                            continue
                        hits += 1
                        print(f"{os.path.relpath(p, root_arg)}:{n}: {name}: {line.strip()[:100]}")
print(f"TOTAL {hits}")
