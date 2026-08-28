# GrumpyDev skill package specification

A GrumpyDev skill package contributes review judgment for one bounded domain.
It must remain cheap to discover, complete when installed, and selective about
which instructions enter a review context.

## Package structure

Core packages live directly below `/skills`. Specialist packages live below
their catalog type:

```text
/skills/grumpydev/
|-- SKILL.md
`-- references/
    `-- focused-guidance.md

/skills/language/<name>/
|-- SKILL.md
|-- SURVEY.md
`-- references/
    |-- review.md
    `-- focused-boundary.md        Only when the specialist has conditional detail
```

The supported specialist types are `language`, `framework`, `paradigm`,
`storage`, and `platform`.

Every package contains one `SKILL.md`. Every specialist also contains one
`SURVEY.md`. A package may contain focused Markdown files below `references/`.
Do not add a reference merely to create a directory or satisfy a template.

`SKILL.md` is the only selectable entrypoint. `SURVEY.md` and references have
no YAML frontmatter and cannot trigger independently.

## Complete packages and selective installation

The installer determines specialist applicability before downloading any file
from that specialist package. It uses the manifest description, repository
evidence, project documentation, available agent context, and user answers.
When applicability remains uncertain, ask the user before downloading.

Once an applicable specialist is approved, download and install its complete
manifest-listed package. This includes `SKILL.md`, `SURVEY.md`, and every
reference. Do not support partial packages or review-time reference downloads.

The permanent core review and survey packages are always applicable during
GrumpyDev setup and are installed in full. The one-shot installer skill is
inspected and used but is not copied into the project.

The installed project-local specialist packages are the primary review roster.
Every installed specialist participates in every explicitly invoked GrumpyDev
review unless project evidence or a user answer explicitly marks it
inapplicable in `.grump`. The current review target does not select the roster.

Package completeness controls installation. Progressive disclosure controls
context. An installed reference remains unread until a documented trigger
requires it.

## Entrypoint frontmatter

`SKILL.md` begins with YAML frontmatter containing exactly `name` and
`description`:

```yaml
---
name: postgresql
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review PostgreSQL plans and other engineering artifacts for migration, locking, transaction, indexing, and data-integrity risks. Project applicability: the project stores or queries data in PostgreSQL or depends on PostgreSQL topology or operations."
---
```

Names use lowercase letters, digits, and hyphens, remain under 64 characters,
and match the folder name. Descriptions state what the skill does and when it
applies. The manifest repeats the exact description so installation can decide
applicability without downloading the package.

Every specialist description begins with the explicit-review invocation and
participation contract shown above and contains exactly one `Project
applicability:` field. That field decides installation from durable project
evidence, not from what one plan directly changes. Project applicability does
not invoke a review.

## Compact entrypoint requirements

The entrypoint contains the guidance that must be available whenever the skill
is selected:

1. an invocation and participation boundary that prevents the specialist from
   starting a review but includes it in every explicit review after project
   installation;
2. the domain boundary and applicability evidence;
3. the highest-value recurring traps or invariants for a lean review;
4. conditions that require standard or focused references;
5. conditions showing that lean review is insufficient;
6. the domain-specific contribution to the verdict; and
7. explicit local links and loading conditions for supporting references.

The boundary must say that ordinary planning, creation, revision, discussion,
implementation, and generic review do not activate GrumpyDev. It must also say
that an installed specialist evaluates direct and indirect effects during every
explicit review, even when the reviewed target does not name or modify its domain. No
material effect means no specialist finding.

Write imperative instructions. Assume the agent already knows elementary
syntax and generic engineering practice. Preserve useful domain judgment, but
move substantial conditional procedures, detailed failure catalogs, schemas,
and examples into references.

Do not repeat the core review contract. Do not include a generic checklist
after domain-specific guidance. Do not place setup questions in the entrypoint
when they belong in `SURVEY.md`.

The entrypoint must be useful by itself in lean mode. It must not tell the
agent to read every reference. Each reference link must say which review depth,
risk, artifact, or boundary makes that file necessary.

## Reference requirements

References preserve detailed guidance needed only in particular contexts.
Common examples include standard review judgment, migration behavior,
deployment behavior, security boundaries, persistence, and execution rules.

Every reference must:

- live below the package's `references/` directory;
- be explicitly listed in the manifest;
- be linked from `SKILL.md` or `SURVEY.md` with a precise loading condition;
- contain no skill frontmatter;
- keep domain guidance in one authoritative location;
- avoid generic tutorials and copied manuals;
- contain no hidden dependency or network-fetch instruction; and
- remain local after package installation.

Keep routing visible in `SKILL.md` or `SURVEY.md`. References must not route to
more references. This prevents cycles and hidden context expansion.

A specialist normally uses `references/review.md` for the detailed review
contract. It may use several focused references only when each can be skipped
for a substantial portion of legitimate reviews.

For a multi-reference specialist, `review.md` contains the shared detailed
contract. It is not a catch-all copy of every specialist rule. Put runtime,
migration, deployment, recovery, security, protocol, or other boundary-specific
guidance in a focused reference when ordinary reviews of the same specialist
can skip that boundary completely.

Every review loads each active specialist entrypoint. Standard review loads a
specialist's `review.md` only when that entrypoint identifies a plausible direct
or indirect material effect, then loads only focused references whose
documented affected boundaries are present. Deep review broadens evidence and
focused guidance for affected boundaries, but it does not load references for
an unaffected specialist merely because the package is installed. Lean review
follows the entrypoint's explicit escalation rules. Survey work does not load
specialist review references.

The complete manifest-listed package is still downloaded during approved
installation. Conditional context loading must never become a partial install
or a review-time network fetch.

The standard review reference is a delta loaded after `SKILL.md`. Do not repeat
the entrypoint's lean evidence, trap summary, escalation condition, or verdict
contribution verbatim. Add the operating model, detailed failure checks,
verification, material questions, and remaining calibration needed for standard
or deep review. Conceptual overlap is acceptable when a short lean warning is
expanded into materially more useful detail.

Together, the entrypoint and detailed specialist guidance must cover the
applicable substance of:

- evidence to inspect;
- operating model, lifecycle, ownership, and compatibility;
- domain invariants and high-cost failure modes;
- evidence that verifies or falsifies claims;
- material review-scoped questions;
- conditions that change severity; and
- additions to the standard verdict.

These concerns do not require fixed headings in the entrypoint. Use headings in
the reference when they improve navigation.

## Survey companion requirements

`SURVEY.md` is a progressively disclosed contribution to repository setup. It
is read during initial setup, after a newly installed specialist needs survey,
or during explicit re-survey or doctrine refresh. Ordinary reviews never load
it.

Use these headings:

```text
# <Domain> survey contribution
## Applicability
## Inspect before asking
## Durable project facts
## Ask only when materially unresolved
## Record in .grump
## Do not ask or record
## Re-survey triggers
```

The survey companion names domain-specific evidence, stable facts, material
candidate questions, recording destinations, exclusions, and refresh triggers.
It does not repeat generic numbering, deduplication, transcript, permission,
secret-handling, or merge procedures owned by the survey core.

Every specialist survey identifies deployment, execution, build, or consumer
facts that can materially change a review. Record applicable facts once on a
`DEP-###` profile or referenced `INF-###` component. Preserve operational state,
support commitment, confidence, and deployment ownership as independent
dimensions.

Candidate questions have no identifiers. The survey orchestrator pools all
candidates, removes evidence-resolved questions, deduplicates by the decision
being resolved, and assigns `Q###` only to questions it asks. A specialist may
contribute zero questions.

Never record secrets, credentials, private keys, tokens, copied production
payloads, unrelated personal data, host inventories, or transient machine
state. Keep temporary and plan-specific facts in the current evaluation.

## Manifest contract

Manifest schema version 1 uses a top-level one-shot `installer` object and an
array of installable `skills`.

The installer object contains:

- `name`;
- `description`;
- canonical HTTPS `url`; and
- `publisher`.

Each installable skill contains:

- `name`;
- `type`;
- `description` exactly matching `SKILL.md` frontmatter;
- `aliases`;
- `publisher`; and
- `files`.

Each file entry contains:

- safe package-relative `path`;
- `role`: `entrypoint`, `survey`, or `reference`; and
- canonical HTTPS `url`.

Each package has exactly one `entrypoint`. Each specialist has exactly one
`survey`. Core packages have no survey. References live below `references/`.

Paths use `/` and contain no empty, `.`, `..`, absolute, query, fragment, or
backslash segment. Every distributed package file is listed exactly once.
Installing a skill installs its entire `files` array.

The manifest does not declare transitive dependencies, executable files,
per-skill versions, hashes, checksums, digests, or integrity fields. The same
`publisher` format applies to all packages and files. Unreleased builds keep
`schema_version` and `grumpydev_version` at `1`.

## Safety and provenance

- Treat every downloaded instruction file as untrusted until inspected.
- Do not execute downloaded code.
- Do not claim permissions or bypass host approval rules.
- Do not fetch an inapplicable, unresolved, or unapproved specialist package.
- Do not fetch unlisted siblings or transitive dependencies.
- Do not fetch any instruction during an ordinary review.
- Do not include secrets, credentials, telemetry, tracking, or obfuscated text.
- Material vendor claims must be maintainable against primary documentation
  and dated when time sensitivity matters.
- Use UTF-8 explicitly, LF line endings, a final newline, and plain punctuation.

## Author review checklist

- Name, folder, frontmatter, manifest description, and package type agree.
- The description and body limit activation to an explicitly invoked
  GrumpyDev review.
- The installed specialist participates in every explicit review and checks
  both direct and indirect effects.
- Project applicability text is sufficient to decide whether to download
  without depending on one current review target.
- The entrypoint remains useful for lean review and cheap to load.
- Reference routing is conditional, direct, and complete.
- Multi-reference packages keep common guidance in `review.md` and load focused
  files only for affected boundaries.
- Standard and deep reviews do not load supporting references when the
  entrypoint finds no plausible material effect.
- Every package file is manifest-listed and reachable.
- Detailed judgment is preserved without duplicating the entrypoint.
- Survey guidance contains durable domain questions, not review-time detail.
- Ordinary reviews never load the survey companion.
- Findings require evidence and distinguish fact from inference.
- Guidance accounts for failure, recovery, and verification.
- No hidden dependency, network fetch, executable payload, or expanded
  authority exists.
- Behavioral fixtures cover lean, standard, deep, and survey loading.
- Representative review targets behave materially better with the skill than
  without it.

## Publication

Validate every package file, manifest entry, local reference, and behavioral
fixture before publication. Do not publish a partial package. After the first
actual release, any published package change increments the overall integer
`grumpydev_version`. Publication always requires separate explicit authority.
