---
name: grumpydev-survey
description: Use only during GrumpyDev installation or setup, or for an explicitly requested re-survey or doctrine refresh. Do not activate during ordinary planning, plan creation, revision, review, or implementation. Survey an existing software repository and create or update its human-owned .grump project doctrine. Applies during initial GrumpyDev setup, repository onboarding through that setup, or an explicit re-survey or doctrine refresh.
---

# GrumpyDev repository survey

Build durable review context from repository evidence. Do not rewrite the
project into a generic template or manufacture constraints to make the survey
look complete.

## Invocation boundary

Run this survey only as part of active GrumpyDev installation or setup, or when
the user explicitly requests a re-survey or doctrine refresh. Do not run it
because a plan is being created, revised, reviewed, or implemented, because
`.grump` exists, or because a previous survey or review occurred. Completing a
survey does not establish a standing survey or review mode.

Use plain ASCII punctuation. Read and write maintained text explicitly as UTF-8
while preserving the repository's established line-ending convention.

## Inspect before interviewing

1. Read existing `.grump` without treating it as automatically current.
2. Locate repository instructions, dependency manifests, build and deployment
   configuration, schemas, tests, and relevant project documentation.
3. Infer purpose, boundaries, technologies, supported targets, execution paths,
   and material constraints only as far as the evidence supports.
4. Distinguish confirmed, inferred, contradictory, stale, and unresolved facts.
5. Do not read secrets, credential stores, production data, or unrelated
   personal files. Do not inspect external environments to complete the survey.

The installer selected specialists before download and installed each approved
specialist as a complete local package. Those installed packages are the
specialist roster. Do not fetch another specialist during survey. If
applicability remains wrong or incomplete, record the installed specialist as
`inapplicable`, `incomplete`, or `not surveyed` as supported by evidence, then
report what an explicit later installation update would need to change.

## Start the initial question sequence

For every initial survey, read
[doctrine-format.md](references/doctrine-format.md). After the evidence pass,
ask its format question as `Q001`, the first question actually presented.

During re-survey, preserve an existing unambiguous format choice unless the user
asks to change it. Load the format reference only when the policy is missing,
contradictory, or being reconsidered.

## Load local references

All references below belong to the installed complete survey package. Never
fetch a reference during survey.

- For initial survey and any policy or interview gap, read
  [interview-and-policies.md](references/interview-and-policies.md).
- When runtime, hosting, build, client, migration, worker, or consumer
  boundaries can materially change future reviews, read
  [deployment-profiles.md](references/deployment-profiles.md). Do not load it
  for a non-deployable artifact whose environments are immaterial.
- When initial setup, a newly installed specialist, or explicit re-survey
  requires specialist contributions, read
  [specialist-surveys.md](references/specialist-surveys.md) and only the
  applicable installed `SURVEY.md` files.
- Before writing or merging `.grump`, read
  [merge-and-finish.md](references/merge-and-finish.md).

Specialist review references are not survey inputs. Ordinary reviews never load
this skill or specialist survey companions.

## Interview only for material gaps

Pool core and specialist candidates before numbering. Remove questions already
answered by `.grump`, project documentation, repository evidence, available
agent context, or an explicit user statement. Deduplicate by the decision or
unknown being resolved, not by wording.

After `Q001`, assign `Q002` onward only to questions actually asked. Present the
smallest useful batch and ask the user to answer by identifier. Never impose a
minimum question count. Accept an unnumbered answer only when its mapping is
unambiguous. Number later clarifications without renumbering earlier questions.

Track answered, deferred, declined, and unresolved questions. Keep explicit
answers separate from inference. Survey `Q###` identifiers are durable setup
provenance. Plan-review `RQ###` answers remain scoped to their evaluation unless
the user separately confirms project-wide scope and doctrine-writing policy
permits the update.

Attempt to determine project purpose and goals before asking. When unavailable,
offer one optional brief purpose question. Ask about relevant project documents
only when their existence or location is unknown. Ask the defined persistence,
interaction, doctrine-maintenance, plan-readiness, and research-execution policy
questions only when the interview reference requires them.

## Draft or merge doctrine

Follow the canonical `.grump` specification and the selected compact or detailed
format. Record project-specific doctrine, not generic GrumpyDev instructions or
a survey transcript.

Preserve manual wording and stable `CON-###`, `ACC-###`, `DEC-###`, `UNK-###`,
`DEP-###`, and `INF-###` identifiers. Do not silently replace a human decision,
promote an inference, erase a source conflict, or renumber an item for neatness.

Write `.grump` only when setup, re-survey, doctrine refresh, or a current
explicit instruction authorizes it. The survey does not authorize other project
changes, external writes, deployment, or publication.

## Finish

Verify that the selected format preserved every decision-affecting fact,
policy, constraint, tradeoff, profile, unknown, and evidence reference. Summarize
evidence, important inferences, unanswered decisions, specialist status,
profile applicability, and re-survey triggers. Do not claim completion when a
missing system boundary makes the doctrine materially misleading.
