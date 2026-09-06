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
3. Give every material factual doctrine claim an inspected source and preserve
   that source's real scope. A material claim can change future verdicts,
   severity, confidence, required actions, project doctrine, or reported
   operational status.
4. Infer purpose, boundaries, technologies, supported targets, execution paths,
   and material constraints only as far as named evidence supports. Label an
   inference and retain its evidence. Do not convert missing evidence into an
   inference merely by relabeling it.
5. Distinguish confirmed, inferred, contradictory, stale, and unresolved facts.
   Keep unsupported material facts as `UNK-###` items or omit them when
   immaterial. Never invent a source to make doctrine look complete.
6. Do not read secrets, credential stores, production data, or unrelated
   personal files. Do not inspect external environments to complete the survey.

The installer selected specialists before download and installed each approved
specialist as a complete local package. Those installed packages are the
specialist roster. Do not fetch another specialist during survey. If
applicability remains wrong or incomplete, record the installed specialist as
`inapplicable`, `incomplete`, or `not surveyed` as supported by evidence, then
report what an explicit later installation update would need to change.

An active specialist is an installed specialist not explicitly marked
`inapplicable` in `.grump`.

## Start the initial question sequence

For every initial survey, read
[doctrine-format.md](references/doctrine-format.md). After the evidence pass,
ask its format question as `Q001`, the first question actually presented.

During re-survey, preserve an existing exact allowed format value unless the
user asks to change it. Load the format reference only when the policy is
missing, contradictory, or being reconsidered.

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

## Interview for setup choices and material gaps

Pool core and specialist candidates before numbering. Remove questions already
answered by `.grump`, project documentation, repository evidence, available
agent context, or an explicit user statement. Deduplicate by the decision or
unknown being resolved, not by wording.

After `Q001`, apply the initial-install `.gitignore` preference defined in the
interview reference. Then assign the remaining identifiers only to questions
actually asked. Present the smallest useful batch and ask the user to answer by
identifier. Never impose a minimum question count. Accept an unnumbered answer
only when its mapping is unambiguous. Number later clarifications without
renumbering earlier questions.

Track answered, deferred, declined, and unresolved questions. Keep explicit
answers separate from inference. Survey `Q###` identifiers stay stable within
the setup sequence. Preserve doctrine question identifiers as provenance, but
never record the initial-install `.gitignore` question in `.grump`. A
plan-review `RQ###` answer applies only to the current review by default. It can
affect future reviews only when the user explicitly says it should become
project doctrine and the exact `Confirmed doctrine updates` policy permits the
`.grump` update.

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

Treat explicit user decisions and constraints as authoritative doctrine at the
scope of the statement, while identifying them as user statements rather than
repository observations. Do not silently promote an existing `.grump` fact from
`inferred` or `unresolved` to `confirmed`.

Write `.grump` only when setup, re-survey, doctrine refresh, or a current
explicit instruction authorizes it. Apart from the exact repository-root
`.gitignore` edit authorized by an affirmative answer to the initial-install
preference, the survey does not authorize other project changes, external
writes, deployment, or publication.

## Finish

Before writing, audit every material factual doctrine entry. Confirm that its
source was inspected, its scope supports the claim, its `confirmed`, `inferred`,
or `unresolved` confidence is honest, contradictions remain visible, and the
selected compact or detailed form preserves the claim-to-source mapping. An
entry that fails this gate becomes an unknown or is omitted when immaterial. Do
not invent a source.

Verify that the selected format preserved purpose and success conditions;
requirements; constraints; decisions and any rationale needed to apply them;
accepted tradeoffs and debt; stored policies; project documentation and
evidence; system boundaries and invariants; technology and runtime facts;
deployment and infrastructure profiles; installed-specialist status; and
material unknowns. Summarize evidence, important inferences, unanswered
decisions, specialist status, profile applicability, and re-survey triggers.
Do not claim completion when a missing system boundary makes the doctrine
materially misleading.
