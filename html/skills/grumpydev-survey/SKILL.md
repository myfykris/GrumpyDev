---
name: grumpydev-survey
description: Use only during an explicit GrumpyDev installation or approved specialist setup, or when the user explicitly requests a GrumpyDev re-survey or doctrine refresh. Never start or continue a survey automatically. Inspect the project and create or update its human-owned .grump doctrine.
---

# GrumpyDev project survey

Create durable review context from evidence and explicit project-wide answers.
Do not make the project fit a generic template or invent facts to complete the
file.

## Run only when requested

Run this survey only during an active installation, explicitly approved
specialist setup (including additions during an update), or a requested
re-survey or doctrine refresh. Do not run it during
ordinary planning, review, revision, or implementation. Completion creates no
standing survey or review mode.

Use plain ASCII punctuation in maintained text. Read and write text explicitly
as UTF-8, preserve the repository's established line endings, and never inspect
secrets, production data, credential stores, or unrelated personal files.

## Inspect before asking

For approved specialist additions, inspect and ask only about their unresolved
durable context; preserve existing doctrine and preferences. Do not restart the
initial interview.

Read an existing `.grump` without assuming it is current. Inspect relevant
repository instructions, dependency manifests, build and deployment
configuration, schemas, tests, source, and project documentation before asking
questions. Attempt to establish the project's purpose, goals, requirements,
constraints, accepted decisions, technologies, runtime paths, and deployment
boundaries from those sources.

State the source behind every material factual doctrine claim. An inspected
source establishes only what it shows within its actual scope. Label inference,
contradiction, staleness, and unknowns. Never turn a filename, convention,
model memory, or missing answer into a fact. Use `UNK-###` only for an unresolved
fact that could materially change future reviews.

The confirmed installed `gd-` specialist directories define the available
specialist roster. The directory and frontmatter names must match, and the
description must contain the explicit-only GrumpyDev activation boundary. Do
not treat unrelated skills or malformed `gd-` collisions as specialists. Do not
fetch skills during survey. Read
[specialist-surveys.md](references/specialist-surveys.md), then load the
`SURVEY.md` for every installed specialist that project evidence does not make
clearly inapplicable. Pool their question candidates with the core candidates.
Specialist review references are not survey inputs.

## Ask numbered, deduplicated questions

Before interpreting any preference or fallback, read the installed
[review-preferences.md](../grumpydev/references/review-preferences.md).

For an initial survey, read
[doctrine-format.md](references/doctrine-format.md) and ask its doctrine-format
question as `Q001`. It asks whether future doctrine should use the most compact
semantically complete form or retain more explanation. Record only an explicit
project-wide answer. If the user declines to choose, use compact as the fallback
without storing a fabricated answer.

Read [survey-workflow.md](references/survey-workflow.md) for missing project-wide
preferences, the initial setup's `.gitignore` question and its scope warning,
question pooling, merge rules, and finish checks. Skip exact valid prior
answers; do not infer consent.

Ask project-fact questions only when inspected evidence leaves a material fact
unresolved. This can include an optional short statement of project purpose,
the existence or location of relevant project documents, hard constraints,
accepted decisions, runtime or hosting differences, and specialist-specific
versions or configurations. Preference answers are never inferred from silence
or repository evidence.

Pool all candidates before numbering them. Remove questions already answered
by reliable evidence, `.grump`, available context, or an explicit user
statement. Deduplicate by the decision or unknown resolved, not just wording.
Ask the smallest useful batch, number questions continuously as `Q001`, `Q002`,
and so on, and let the user answer by number. Never impose a minimum question
count. Preserve answered, deferred, declined, and unresolved states without
turning any of them into another answer.

When runtime, environment, worker, client, migration, hosting, or deployment
differences can change engineering judgment, read
[deployment-profiles.md](references/deployment-profiles.md). Do not load it for
a project where those differences are immaterial.

## Write bounded project doctrine

Before creating or changing `.grump`, use
[doctrine-format.md](references/doctrine-format.md) and
[survey-workflow.md](references/survey-workflow.md). These installed references
define the canonical format. Store project facts and decisions, not generic
GrumpyDev instructions or a survey transcript.

Preserve human wording, unknown sections, and existing stable identifiers. Make
bounded edits only to recognized sections and managed preference fields. Never
silently promote an inference, resolve a contradiction, replace a human
decision, normalize unknown content, or renumber items for neatness. If the
requested change cannot preserve surrounding human content safely, leave the
file unchanged and show the proposed edit in chat.

The survey may write only project-local `.grump` content authorized by the
active setup, re-survey, or doctrine-refresh request. An affirmative
`.gitignore` answer authorizes adding exactly `.grump` and `.grumpydev/` to the
repository-root `.gitignore` while preserving all other content. No survey
answer authorizes source changes, production inspection, deployment,
publication, remote writes, or another external action.

After writing, reread the exact file, verify its UTF-8 decoding, structure,
recorded answers, evidence locators, and preservation of surrounding content.
Report what was created, changed, proposed but not written, and left unresolved.
Do not claim a write succeeded merely because it was attempted.
