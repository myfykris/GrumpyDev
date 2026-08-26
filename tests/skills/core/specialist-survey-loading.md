# Specialist survey loading behavior

## Initial survey

The repository uses PHP, Laravel, PostgreSQL, and containers, and those
specialists are installed with survey companions.

Expected behavior:

- Read only the applicable installed survey companions.
- Inspect repository and documentation evidence before forming questions.
- Merge overlapping runtime, database, worker, and deployment candidates.
- Assign `Q###` identifiers only after deduplication.
- Record durable answers and useful evidence in `.grump` without storing a raw
  transcript.

## Ordinary review

The same repository later asks GrumpyDev to review an implementation plan.

Expected behavior:

- Read `.grump` and applicable specialist `SKILL.md` files.
- Do not read any specialist `SURVEY.md`.
- Ask an `RQ###` question only when current review evidence still lacks a
  material answer.

## Re-survey

An explicit re-survey finds unchanged evidence and a current recorded answer.

Expected behavior:

- Read the applicable survey contribution.
- Retain the supported answer without asking the user again.
- Ask only when evidence conflicts, a material environment changed, or the
  recorded context is incomplete.
