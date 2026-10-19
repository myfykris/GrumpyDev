"""Build benchmark run directories.

Usage:
  mkruns.py <work_dir> <scenario> <arm> <model> <rep>
  mkruns.py <work_dir> xs2 <arm> <model> <rep> --ledger-from <run_dir>
  mkruns.py <work_dir> <scenario> prio|sub <model> <rep> --skill <skill_dir>

Each run is <work_dir>/runs/<scenario>-<arm>-<model>-r<rep>, a git repo holding the
scenario's project. Arms:
  plain   no GrumpyDev (the strong prompt)
  lean    v2 skill from html/skills/grumpydev plus the scenario's v2 .grump
  prio    like lean, with the skill directory given by --skill
  sub     like prio; the agent may start subagents (same-session scenarios)
  v1      the earlier GrumpyDev (core skills and 20 specialists from commit e275a2c) plus its .grump
  block   impl only: CLAUDE.md with the constraints block
  none    impl only: no doctrine anywhere
Prints the run directory."""
import os, shutil, subprocess, sys, json

EVAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(EVAL))
FIX, SCEN, DOC = (os.path.join(EVAL, x) for x in ("fixtures", "scenarios", "doctrine"))
S1PLAN = "docs/plans/v2-webhooks-and-nightly-export.md"
V1_SPECIALISTS = ["postgresql", "schema-evolution", "sql", "distributed-systems", "background-jobs",
                  "data-pipelines", "kubernetes", "observability", "javascript", "typescript", "express",
                  "nodejs", "concurrent-systems", "application-security", "oauth",
                  "event-driven-architecture", "containers", "performance-capacity",
                  "dependency-supply-chain", "secrets-configuration"]
LEAN_DOCTRINE = {"s1": "research.grump", "s1r2": "research.grump", "s2": "research.grump", "s3": "research.grump", "s5": "research.grump",
                 "xs1": "research.grump", "xs2": "research.grump", "research": "research.grump",
                 "pin": "pin.grump", "upgrade": "pin.grump", "bplan": "boundaries.grump",
                 "baudit": "boundaries.grump", "touch": "touch.grump", "touchseed": "touch.grump",
                 "fover": "research.grump", "ftol": "research.grump", "fspeed": "research.grump",
                 "fself": "research.grump"}

def git(cwd, *args, date="2026-10-14T16:00:00Z"):
    env = dict(os.environ, GIT_AUTHOR_NAME="Sam Rivera", GIT_AUTHOR_EMAIL="sam@example.com",
               GIT_COMMITTER_NAME="Sam Rivera", GIT_COMMITTER_EMAIL="sam@example.com",
               GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
    return subprocess.run(["git", *args], cwd=cwd, env=env, check=True, capture_output=True, text=True).stdout

def copy_into(src, dst, skip=()):
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d != ".git"]
        rel = os.path.relpath(root, src)
        for f in files:
            r = os.path.normpath(os.path.join(rel, f))
            if r in skip:
                continue
            os.makedirs(os.path.join(dst, rel), exist_ok=True)
            shutil.copy2(os.path.join(root, f), os.path.join(dst, r))

def put(dst, rel, src_file):
    os.makedirs(os.path.dirname(os.path.join(dst, rel)), exist_ok=True)
    shutil.copy2(src_file, os.path.join(dst, rel))

def init_commit(d, msg="Initial import"):
    git(d, "init", "-q", "-b", "main")
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", msg)

def invoicer(work):
    """Build the invoicer fixture (with history) once per work dir."""
    cache = os.path.join(work, "cache", "invoicer")
    if not os.path.exists(os.path.join(cache, "fixture")):
        os.makedirs(cache, exist_ok=True)
        subprocess.run([sys.executable, "-I", os.path.join(FIX, "invoicer-build.py"), cache], check=True,
                       capture_output=True)
    return cache

def build_project(work, scen, d):
    if scen in ("s1", "xs1", "s1r2", "fspeed"):
        copy_into(os.path.join(FIX, "invoice-sync"), d); init_commit(d)
    elif scen in ("fover", "fself"):
        copy_into(os.path.join(FIX, "invoice-sync"), d, skip=(S1PLAN,)); init_commit(d)
        if scen == "fover":
            put(d, "docs/plans/event-pipeline.md", os.path.join(SCEN, "fit", "event-pipeline.md"))
            git(d, "add", "-A"); git(d, "commit", "-q", "-m", "Plan draft: event pipeline")
    elif scen in ("s2", "s3", "s5", "research", "xs2", "ftol"):
        copy_into(os.path.join(FIX, "invoice-sync"), d, skip=(S1PLAN,) if scen != "xs2" else ())
        if scen in ("s2", "s5", "ftol"):
            copy_into(os.path.join(SCEN, "s2"), d)
        elif scen == "s3":
            copy_into(os.path.join(SCEN, "s3"), d)
        elif scen == "research":
            put(d, "docs/plans/multi-currency.md", os.path.join(SCEN, "research", "multi-currency.md"))
        init_commit(d)
        if scen == "s5":
            copy_into(os.path.join(SCEN, "s5-impl"), d)  # uncommitted diff
        if scen == "xs2":
            put(d, S1PLAN, os.path.join(SCEN, "s1r2", "v2-webhooks-and-nightly-export.md"))
            git(d, "add", "-A"); git(d, "commit", "-q", "-m", "Plan revision 2", date="2026-10-15T09:00:00Z")
    elif scen in ("pin", "upgrade", "impl"):
        copy_into(os.path.join(FIX, "php-portal", "base"), d); init_commit(d)
        if scen == "pin":
            copy_into(os.path.join(FIX, "php-portal", "diff"), d)  # uncommitted diff
        elif scen == "upgrade":
            put(d, "docs/plans/ledger-sync.md", os.path.join(SCEN, "upgrade", "ledger-sync.md"))
            git(d, "add", "-A"); git(d, "commit", "-q", "-m", "Plan: live payment status")
    elif scen in ("bplan", "baudit", "touch", "touchseed"):
        cache = invoicer(work)
        src = os.path.join(cache, "fixture-plan" if scen == "bplan" else "fixture")
        shutil.copytree(src, d, symlinks=True, dirs_exist_ok=True)
        if scen in ("touch", "touchseed"):
            put(d, "docs/plans/issued-at.md", os.path.join(SCEN, "touch", "issued-at.md"))
            git(d, "add", "-A"); git(d, "commit", "-q", "-m", "Plan: store Partner's invoice issue date")
        if scen == "touchseed":
            put(d, ".grumpydev/reviews/project.md", os.path.join(SCEN, "touch", "project-ledger.md"))
    else:
        sys.exit(f"unknown scenario {scen}")

def v1_overlay(d):
    man = json.loads(git(REPO, "show", "e275a2c:html/manifest.json"))
    want = {"grumpydev", "grumpydev-survey", "grumpydev-update-remove"} | {"gd-" + n for n in V1_SPECIALISTS}
    found = set()
    for s in man["skills"]:
        if s["name"] not in want:
            continue
        found.add(s["name"])
        for f in s["files"]:
            content = git(REPO, "show", f"e275a2c:html/{s['path']}/{f['path']}")
            out = os.path.join(d, ".claude", "skills", s["name"], f["path"])
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "w", encoding="utf-8").write(content)
    missing = want - found
    if missing:
        sys.exit(f"v1 overlay missing {sorted(missing)}")
    shutil.copy2(os.path.join(DOC, "v1-invoice-sync.grump"), os.path.join(d, ".grump"))

def lean_overlay(d, scen, src=os.path.join(REPO, "html", "skills", "grumpydev")):
    shutil.copytree(src, os.path.join(d, ".claude", "skills", "grumpydev"))
    shutil.copy2(os.path.join(DOC, LEAN_DOCTRINE[scen]), os.path.join(d, ".grump"))

def main():
    a = sys.argv[1:]
    work, scen, arm, model, rep = a[:5]
    name = f"{scen}-{arm}-{model}-r{rep}"
    d = os.path.join(work, "runs", name)
    if os.path.exists(d):
        sys.exit(f"exists: {d}")
    os.makedirs(d)
    build_project(work, scen, d)
    if scen == "xs2" and arm == "lean":
        src = a[a.index("--ledger-from") + 1]
        shutil.copytree(os.path.join(src, ".grumpydev"), os.path.join(d, ".grumpydev"))
    if arm == "lean":
        lean_overlay(d, scen)
    elif arm in ("prio", "sub"):
        lean_overlay(d, scen, os.path.abspath(a[a.index("--skill") + 1]))
    elif arm == "v1":
        v1_overlay(d)
    elif arm == "block":
        put(d, "CLAUDE.md", os.path.join(SCEN, "impl", "claude-md-block.md"))
        git(d, "add", "CLAUDE.md"); git(d, "commit", "-q", "-m", "Agent context: constraints")
    elif arm not in ("plain", "none"):
        sys.exit(f"unknown arm {arm}")
    if not os.path.isdir(os.path.join(d, ".git")):
        sys.exit(f"no .git in {d}")
    with open(os.path.join(d, ".git", "info", "exclude"), "a") as f:
        f.write(".claude/\n.grump\n.grumpydev/\n")
    print(d)

if __name__ == "__main__":
    main()
