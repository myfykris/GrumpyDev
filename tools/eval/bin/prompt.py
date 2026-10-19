"""Print the agent prompt for a run directory named <scenario>-<arm>-<model>-r<rep>.
Usage: prompt.py <run_dir> [round2]
Same-session scenarios (fover, ftol, fspeed, fself): prompt.py <run_dir> turn1|turn2. The agent saves
its review to <work_dir>/results/<run>.md. fcold is a one-turn cold review of an fself plan."""
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

FIT_PLANS = {"fover": "docs/plans/event-pipeline.md", "ftol": "docs/plans/reliable-pushes.md",
             "fspeed": "docs/plans/v2-webhooks-and-nightly-export.md", "fself": "docs/plans/v2-and-export.md",
             "fcold": "docs/plans/v2-and-export.md"}
FIT_TURN1 = {
    "fover": ("Context before we go further: I'm the only developer on this, there's no on-call rotation, and "
              "we do about 3,000 invoices a day with peaks around 9,000. That's not going to grow much. I want "
              "the fewest moving parts I can get away with, because I'm the one who gets woken up. Sam, our "
              "contractor, drafted docs/plans/event-pipeline.md to fix the failed and stuck pushes. Read it and "
              "add a short \"Open questions\" section at the end with anything Sam needs to answer. Don't change "
              "the rest of the plan."),
    "ftol": ("Some context: it's just me on this, no on-call. A few hours' delay getting an invoice into Ledgerly "
             "is fine as long as nothing gets lost or duplicated, because Finance only reconciles the next "
             "morning. I don't want to add infrastructure for this. docs/plans/reliable-pushes.md is the plan I "
             "want to do next. Read it and tell me in two or three sentences what it changes. Don't edit "
             "anything."),
    "fspeed": ("We need this out by Friday. Speed matters more than polish on this one; don't gold-plate it. Read "
               "docs/plans/v2-webhooks-and-nightly-export.md and tell me in two or three sentences what it does. "
               "Don't edit anything."),
    "fself": ("I need a plan for two things. Accept Partner's new v2 webhooks at /webhooks/partner/v2: same "
              "fields as v1, but amounts arrive as integer cents. And send Finance a CSV of the previous day's "
              "invoices (New York time) by 6am every day. Write the plan to docs/plans/v2-and-export.md. It's "
              "just me maintaining this, and I don't want new infrastructure."),
}
if scen in FIT_PLANS:
    turn = sys.argv[2] if len(sys.argv) > 2 else "turn1"
    out = os.path.join(os.path.dirname(os.path.dirname(d)), "results", os.path.basename(d) + ".md")
    limits = ("Do not install packages or use the network, and do not read anything outside that directory; "
              "any subagent you start must follow the same limits." if arm == "sub" and scen != "fcold" else
              "Do not install packages or use the network, do not read anything outside that directory, and do "
              "not launch subagents.")
    head = (f"You are a coding agent in Claude Code. Working directory: {d}\n"
            "Work only inside that directory, except for saving your final answer where the user tells you. "
            f"{limits} Change files only when the user asks you to")
    head += (" and the GrumpyDev instructions allow it.\n\n" + LEAN) if arm in ("lean", "prio", "sub") else "."
    plan = FIT_PLANS[scen]
    ask = f"Grump {plan}" if arm in ("lean", "prio", "sub") else STRONG_PLAN.format(t=plan)
    save = (f"You cannot talk to the user. List any question you would ask as an open question and continue. "
            f"When the review is finished, save it to {out}, exactly as you would show it to the user, and "
            f"reply with only: saved")
    if scen == "fcold":
        print(f'{head}\n\nThe user says:\n\n"{ask}"\n\n{save}')
    elif turn == "turn1":
        print(f'{head}\n\nThe user says:\n\n"{FIT_TURN1[scen]}"\n\nYou cannot talk to the user; make '
              f'reasonable choices and continue. Reply briefly when you are done.')
    else:
        print(f'The user says:\n\n"{ask}"\n\n{save}')
    sys.exit()

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
