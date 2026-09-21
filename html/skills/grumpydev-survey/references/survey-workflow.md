# Survey workflow

Load this reference for the initial preference interview and before creating or
merging `.grump`. For approved specialist additions, use only the relevant
project-fact and merge steps; do not restart the initial interview.

## Ask durable preferences

After `Q001`, ask each missing project-wide preference below. Say that the
answer applies to future GrumpyDev work in this project. Preserve the exact
allowed values.

1. `Plan addenda`: ask whether completed plan reviews may be appended to a
   GrumpyDev addendum or must remain `chat only`. Store `allowed` or `chat only`.
2. `Review questions`: ask whether reviews should pause for material numbered
   questions or finish without pausing and list gaps. Store `interactive` or
   `non-interactive`.
3. `Confirmed doctrine updates`: ask whether explicitly confirmed durable facts
   may update `.grump` or should be proposed only. Store `allowed` or
   `propose only`.
4. `Decision-affecting research`: ask whether research that can change an
   implementation decision must be resolved before plan approval, or may be a
   bounded discovery phase followed by another review. Store `resolve first` or
   `gated discovery`.
5. `Research execution`: ask whether safe read-only research should run
   automatically, require permission, or only be reported. Store `automatic`,
   `ask first`, or `report only`.

Do not store a preference after a decline, deferral, ambiguous answer, or
silence. Apply the documented missing-value fallback instead.

During initial setup, inspect the repository-root `.gitignore`. Unless both
exact active lines are already present or the user already answered in the
current context, ask whether GrumpyDev should add `.grump` and `.grumpydev/`.
State before the question that these two entries cover the doctrine file and
the canonical fallback installation only. When setup used a harness-native
project skill directory, its installed `gd-` skill directories are not covered
and remain subject to the repository's existing tracking rules. Do not add a
native skill-root pattern without a separate explicit request.
An explicit `yes` authorizes adding only missing exact lines while preserving
all other content. An explicit `no` or unclear answer changes nothing. Never
record this choice in `.grump`; the file itself is the result.

## Ask only material project questions

Attempt to determine purpose and goals from evidence. If that fails, offer an
optional brief purpose description so future reviews can judge whether work
serves the project. Ask whether relevant requirements, specifications,
architecture decisions, interface contracts, acceptance criteria, or runbooks
exist only when their existence or location remains unknown. Ask about
constraints, accepted decisions, deployment, and specialist facts only when an
answer can materially change future judgment.

Number every asked question in one continuous `Q###` sequence. Pool candidates
before numbering, remove answered candidates, and deduplicate by the decision
or unknown resolved. Preserve mappings for answered, deferred, declined, and
unresolved questions. Do not store raw interview history.

## Create or merge doctrine

Use [doctrine-format.md](doctrine-format.md) before writing `.grump`; omit
empty optional sections. Preserve human-authored text, unknown subsections,
stable identifiers, evidence scope, and contradictions. Store explicit user
decisions as user statements. Do not
promote inference into confirmed fact or convert a review recommendation into
doctrine.

Generate and interpret only the eight managed fields defined in the installed
[review-preferences.md](../../grumpydev/references/review-preferences.md).
Unknown human-authored preference fields are non-operative. Make bounded edits;
if surrounding content cannot be preserved, leave the file unchanged and return
the proposed edit.

Before reporting completion, audit each material factual entry against an
inspected source, reread the written file, and verify the exact preference
answers and stable identifiers. Report created, changed, unresolved, and
unwritten proposed content. Distinguish an attempted write from a verified
write.
