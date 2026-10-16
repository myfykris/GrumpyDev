# GrumpyDev benchmark

Fixtures, scenarios and answer keys used to decide what goes into the skill.

- `fixtures/`: test projects (`invoice-sync`, `php-portal`; `invoicer-build.py` builds the
  invoicer project with its git history).
- `scenarios/`: plans, diffs and tasks layered on a fixture.
- `keys/`: answer keys, one per scenario.
- `doctrine/`: the `.grump` each arm gets.
- `bin/mkruns.py`: build one run directory: `<work> <scenario> <arm> <model> <rep>`.
- `bin/prompt.py`: the exact prompt for a run directory.
- `bin/run.sh`: build and run one arm (Claude models through `claude -p`, which needs a
  valid login; other model ids through `qagent.py` against an OpenAI-compatible endpoint).
- `bin/collect.py`, `bin/packet.py`: gather reports and build blind judge packets;
  `judge.md` is the judge prompt.
- `bin/php8scan.py`: flags PHP 8-only syntax (stand-in for running on PHP 7.4).
- `RESULTS.md`: the October 2026 results.

Scenarios: s1 flawed plan, s2 good plan, s3 subtle infra traps, s5 buggy diff, s1r2
same-session re-review, xs1/xs2 cross-session re-review with the ledger, pin (PHP 7.4 diff),
upgrade (plan needing PHP 8), impl (coding with and without the constraints block),
research (deferred decisions), bplan/baudit (boundaries plan and audit), touch and
touchseed (sound plan in files with pre-existing problems, without and with a seeded
project ledger). Arms: plain (strong prompt), lean (this skill), v1 (the old skill with specialists, commit e275a2c).
