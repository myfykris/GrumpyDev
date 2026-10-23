# Project audit

Use for `Grump this project`. It applies the core skill to the existing system,
with the Boundaries labels as the main lens. Work read-only.

1. Areas. Split the repository into areas from its own structure: processes and
   entry points, layers, each subsystem, shared libraries, and code that crosses
   a language or generator boundary (SQL, schemas, configs). Treat the git
   history as one more area.
2. Map. For each area, list the units as they are: what each owns, who calls
   it, and what it depends on. A few lines per area.
3. Findings. Apply the Boundaries labels. Look hardest for:
   - the same rule or fact implemented in several places, and helpers that
     exist but get bypassed. Count every copy and cite each;
   - facts kept by hand on both sides of a language, service or generator
     boundary;
   - test or debug hooks on production paths;
   - global state used as hidden arguments;
   - locks, flags or queues that serve several purposes.
4. Cost. Classify the fix commits in recent history (the last 6 months, at most
   50 commits) by root cause, and link each to a finding. Say so when a finding
   has no bug evidence.
5. Intended design. Only for areas with HIGH or MEDIUM findings: units,
   responsibilities, interfaces and call direction, in a few lines.
6. Verify. Re-check every headline claim against the code and label it
   verified (traced through the code or confirmed by a safe probe), static
   (read but not traced end to end) or inferred.
7. Doctrine. Known debt from `.grump` gets one line under "Known debt seen",
   not a finding, unless it has grown. Accepted decisions are not findings.

Severity: HIGH causes a wrong result now or blocks a planned change; MEDIUM
raises the cost or risk of change; LOW is cleanliness only. List LOW items in
one line, not in the tables.

## Output

<verdict> - <one-sentence summary>
Verdicts: SOUND, NEEDS WORK, AT RISK.

Bugs (live or latent defects found along the way):
| ID | Bug | Where | Evidence | Fix |

Findings:
| ID | Issue | Where (every copy) | Cost evidence | Migration |

- The ID cell holds the ID and severity, and for findings the label:
  `GD-002 HIGH` or `GD-007 MEDIUM DUPLICATED`. Do not give them separate
  columns.
- Migration: small steps, each keeping behavior unchanged.
- Keep: well-designed boundaries to preserve, one line each.
- Known debt seen: one line.
- Order of work: fix the bugs; add ratchet checks (a lint rule or test that
  fails on a new copy or bypass); delete dead code; introduce the missing owners
  and interfaces; then move one family at a time.
- Ledger: every bug and finding is an issue in `.grumpydev/reviews/project.md`.
  Use counts in closing conditions where they exist ("copies: 4 -> 1").
