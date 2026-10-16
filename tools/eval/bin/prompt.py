"""Print the agent prompt for a run directory named <scenario>-<arm>-<model>-r<rep>.
Usage: prompt.py <run_dir> [round2]"""
import os, sys

d = os.path.abspath(sys.argv[1])
scen, arm = os.path.basename(d).split("-")[:2]
round2 = len(sys.argv) > 2 and sys.argv[2] == "round2"
EVAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PLANS = {"s1": "docs/plans/v2-webhooks-and-nightly-export.md", "s1r2": "docs/plans/v2-webhooks-and-nightly-export.md", "xs1": "docs/plans/v2-webhooks-and-nightly-export.md",
         "xs2": "docs/plans/v2-webhooks-and-nightly-export.md", "s2": "docs/plans/reliable-pushes.md",
         "s3": "docs/plans/scale-out.md", "research": "docs/plans/multi-currency.md",
         "upgrade": "docs/plans/ledger-sync.md", "bplan": "docs/plans/credit-notes.md",
         "touch": "docs/plans/issued-at.md", "touchseed": "docs/plans/issued-at.md"}
DIFFS = ("s5", "pin")
STRONG_PLAN = ("Critically review {t} before we implement it. Act like a skeptical senior engineer: find the "
               "real problems, not nitpicks, and check the plan against the actual code and deploy config. "
               "Give me a verdict.")
STRONG_DIFF = ("Critically review the uncommitted changes in this repository before we merge them. Act like a "
               "skeptical senior engineer: find the real problems, not nitpicks, and check the changes against "
               "the actual code and deploy config. Give me a verdict.")
STRONG_AUDIT = ("Critically review this codebase's design. Act like a skeptical senior engineer: find the real "
                "problems with abstractions and boundaries (code in the wrong place, rules duplicated, units "
                "reaching into each other's internals), not nitpicks, and check your claims against the actual "
                "code, git history and deploy config. Give me a ranked report.")
LEAN = ("This project has GrumpyDev installed: .claude/skills/grumpydev/SKILL.md, with project doctrine in "
        ".grump. Claude Code has not loaded it as a skill in this session, so when the user asks for "
        "GrumpyDev, read that file first and follow it, including any reference file it tells you to read.")
V1 = ("This project has GrumpyDev installed: its skills are in .claude/skills/ and its project doctrine is in "
      ".grump. Claude Code has not loaded them as skills in this session, so when the user asks for GrumpyDev, "
      "start by reading .claude/skills/grumpydev/SKILL.md and follow it, including every file it tells you to "
      "read. If GrumpyDev would pause for a question, write the question out as the user would see it, then "
      "answer it as the user with: \"No. Proceed without research and list these as open questions.\" Then "
      "continue.")
END_REVIEW = ("You cannot talk to the user. List any question you would ask as an open question and continue. "
              "Return only the review, exactly as the user would see it.")

if round2:
    t = PLANS[scen]
    ask = f"I revised the plan in {t}. Grump it again." if arm == "lean" else \
          f"I revised the plan in {t}. Review it again the same way."
    print(f'The user says:\n\n"{ask}"\n\n{END_REVIEW}')
    sys.exit()

head = (f"You are a coding agent in Claude Code. Working directory: {d}\n"
        "Work only inside that directory. Do not install packages or use the network, do not read anything "
        "outside that directory, and do not launch subagents.")
if scen == "impl":
    task = open(os.path.join(EVAL, "scenarios", "impl", "task.md"), encoding="utf-8").read().strip()
    print(f"{head} You may create and edit files inside the working directory to do the task; do not commit.\n\n"
          f'The user says:\n\n"{task}"\n\nYou cannot talk to the user; make reasonable choices and continue.')
    sys.exit()
if arm in ("lean", "v1"):
    head += " Do not modify files except what the GrumpyDev instructions explicitly permit.\n\n"
    head += LEAN if arm == "lean" else V1
    ask = "Grump this diff" if scen in DIFFS else "Grump this project" if scen == "baudit" else f"Grump {PLANS[scen]}"
else:
    head += " Do not modify, create, or delete files."
    ask = STRONG_DIFF if scen in DIFFS else STRONG_AUDIT if scen == "baudit" else STRONG_PLAN.format(t=PLANS[scen])
print(f'{head}\n\nThe user says:\n\n"{ask}"\n\n{END_REVIEW}')
