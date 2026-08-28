# Specialist survey routing

Load this file when initial setup, a newly installed specialist, or explicit
re-survey requires specialist survey contributions.

## Select before download

Use installed complete packages only. Applicability was evaluated before
download from manifest metadata and local evidence. Do not fetch another
specialist merely because an installed survey mentions a companion.

If survey evidence shows that an installed specialist is actually
inapplicable, mark it `inapplicable` with concise project evidence and tell the
user. Do not manufacture questions to justify its installation. Do not create
status entries for uninstalled catalog specialists merely to record that they
do not apply.

## Load survey companions selectively

Read an applicable installed specialist's `SURVEY.md` during initial setup,
after that specialist is newly installed and unsurveyed, or during explicit
re-survey or doctrine refresh. Do not read it during an ordinary plan review.

Treat candidate questions as guidance, not a questionnaire. Pool all candidates
before numbering. Remove evidence-resolved candidates and deduplicate by the
decision or unknown being resolved. A specialist can contribute zero questions.

## Record status

Record each installed specialist as:

- `current` when its durable context and evidence are usable;
- `incomplete` when missing material context can limit future reviews;
- `not surveyed` when its contribution has not been evaluated; or
- `inapplicable` only when project evidence or a user answer establishes the
  explicit exception.

Identify concise evidence and any material missing context. Use `UNK-###` only
when the unresolved fact could change a future plan or verdict. Do not store
survey transcripts, package file inventories, uninstalled catalog entries, or
generic skill instructions in `.grump`.
