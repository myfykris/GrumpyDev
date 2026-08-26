# GrumpyDev skill authoring specification

A GrumpyDev specialist skill packages review judgment for one bounded domain.
Its purpose is to improve what an agent inspects and which failure modes it can
recognize. A generic best-practices list is not enough.

## Required artifacts

Store each skill in the directory for its catalog type:

```text
/skills/language/<name>/SKILL.md and SURVEY.md
/skills/framework/<name>/SKILL.md and SURVEY.md
/skills/paradigm/<name>/SKILL.md and SURVEY.md
/skills/storage/<name>/SKILL.md and SURVEY.md
/skills/platform/<name>/SKILL.md and SURVEY.md
```

Core skills remain directly under `/skills/<name>/SKILL.md` and do not have a
survey companion. Every specialist folder contains one `SKILL.md` and one
`SURVEY.md`. `SKILL.md` must begin with YAML frontmatter containing exactly
`name` and `description`:

```yaml
---
name: postgresql
description: Review PostgreSQL engineering plans for migration, locking,
  transaction, indexing, and data-integrity risks. Use when a plan creates,
  changes, queries, or operates a PostgreSQL database.
---
```

Names use lowercase letters, digits, and hyphens, remain under 64 characters,
and match their folder name. Descriptions state both what the skill does and
when it should trigger.

## `SKILL.md` body requirements

Write imperative instructions. Keep the main file focused on plan review and
include:

1. evidence to inspect before reaching a conclusion;
2. the operating model, lifecycle, ownership, compatibility, and failure
   assumptions needed to judge the plan;
3. domain-specific invariants and high-cost failure modes;
4. evidence that can verify or falsify the plan's material claims;
5. criteria for asking only questions needed to expose material hidden
   assumptions, with useful domain-specific candidate wording;
6. conditions that change severity or invalidate a finding; and
7. additions the skill makes to the standard GrumpyDev review.

Use these base headings:

```text
## Inspect evidence
## Establish the operating model
## Challenge the plan
## Verify the claims
## Ask when evidence is missing
## Calibrate findings
## Add to the verdict
```

Add domain-specific subsections when they improve navigation. Do not add empty
or generic sections merely to satisfy the shape.

Do not restate the core review contract. Do not teach elementary syntax. Prefer
concrete lifecycle boundaries, artifacts, and counterexamples. Do not append a
generic language, framework, storage, paradigm, or platform checklist after a
domain-specific block. Integrate a useful cross-cutting concern into the domain
instruction that it changes, and omit it when the core review already owns it.

Begin `Challenge the plan` with one `### Recurring traps` subsection. Name the
domain's recognizable failure patterns, misleading shortcuts, and false
assumptions in concrete terms so a reviewer can spot them quickly. Do not fill
the subsection with generic reminders that belong to the core review, and do
not repeat the detailed challenge bullets that follow it word for word.

Keep reusable rules in the core skills rather than copying the same paragraph
through the specialist catalog. A repeated template must earn its place in each
standalone skill by changing that domain's review decisions. Wrap body prose at
80 columns when practical. The single-line YAML `description` may be longer.

Do not impose a minimum or maximum question count. A specialist can contribute
zero questions when the plan and available evidence resolve its material
decisions. The core review collects, deduplicates, numbers, and decides whether
to ask candidate questions.

Keep durable repository setup questions in `SURVEY.md`. Keep only questions that
can be needed for the current plan in `SKILL.md`. A plan review may still ask
about a durable fact when `.grump`, the plan, documentation, repository, and
agent context all lack it and the answer could change the current evaluation.

When naming a specific companion skill, use its exact manifest name in
backticks. If no exact skill exists, describe the applicable installed
specialist and the decision criterion instead of inventing a skill name.

## `SURVEY.md` requirements

`SURVEY.md` is a progressively disclosed contribution to the repository survey.
It is installed beside `SKILL.md`, but it is not an independently selectable
skill and has no YAML frontmatter. The survey orchestrator reads it only during
initial setup, after a newly added specialist needs surveying, or during an
explicit re-survey or doctrine refresh. Ordinary plan reviews never load it.

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

`Inspect before asking` names the repository files, generated configuration,
documentation, and runtime evidence that can answer questions without user
interruption. `Durable project facts` identifies context stable enough to
improve later plan reviews, including material differences among development,
CI, test, staging, production, CLI, worker, region, client, and desktop targets.

Every specialist survey must identify which deployment, execution, build, or
consumer facts in its domain can materially change a review. Inspect evidence
first, then contribute only domain-specific candidates that the core profile
confirmation cannot resolve. Examples include a language process model, a
framework adapter or rendering mode, a storage topology and failover contract,
a client distribution boundary, or an infrastructure ownership constraint.
Do not repeat the core `How will this software be hosted and run?` question in
each specialist.

Record applicable infrastructure facts in one `DEP-###` profile or a referenced
`INF-###` shared component, not in parallel prose under every technology. Keep
profile-specific connection, identity, scaling, and failure consequences on
the profile even when the shared component owns its common contract. Identify
the destination and scope under `Record in .grump`.

Specialist contributions must preserve these independent dimensions when they
are material:

- current, planned, or retiring operational state;
- required, supported, best effort, or unsupported support commitment;
- project, customer, vendor, or shared deployment ownership; and
- confirmed, inferred, or unresolved confidence with scoped evidence.

Do not record secrets, host inventories, copied production data, or transient
machine state as infrastructure doctrine. Name re-survey triggers that can make
the specialist contribution stale, such as a runtime, process model, hosting
owner, supported target, topology, trust boundary, delivery, or recovery
change. A specialist may contribute zero infrastructure questions when the
core profile and evidence already establish every material domain fact.

Candidate questions have no identifiers. The survey orchestrator pools all
applicable candidates, removes questions already answered by evidence or
`.grump`, deduplicates overlaps across skills, and assigns continuous `Q###`
identifiers only to the questions it actually asks. Do not require every
candidate to be asked and do not impose a question count.

`Record in .grump` identifies where to preserve an answer, its scope, and the
evidence that supports it. Use an `UNK-###` item only when the unresolved answer
could materially change future reviews. Do not store a raw survey transcript.

Keep each survey file a domain contribution. Do not repeat the survey
orchestrator's generic numbering, deduplication, transcript, or secret-handling
procedure in every specialist. Use the required sections for domain-specific
evidence, durable facts, candidate questions, recording destinations,
exclusions, and refresh triggers.

Never ask for or record secrets, credentials, private keys, tokens, copied
production payloads, unrelated personal data, or transient machine trivia.
Keep temporary and plan-specific decisions in the current evaluation rather
than project doctrine.

## Safety and provenance

- Do not include secrets, credentials, telemetry, tracking, or obfuscated text.
- Do not instruct the agent to execute downloaded code.
- Do not claim additional permissions or bypass host approval rules.
- Do not fetch network resources unless the user's task requires current vendor
  documentation and the host permits it.
- Identify the publisher in every manifest entry using the same `publisher`
  field and format for every skill type.
- Material vendor-specific claims should be maintainable against primary
  documentation and dated when time sensitivity matters.

## Catalog metadata

Each schema version 1 `/manifest.json` core entry includes:

- `name`
- `type`: one of the schema version 1 values below
- canonical HTTPS `url`
- `aliases`
- `publisher`: the identity responsible for publishing the exact file

Each specialist entry also includes canonical HTTPS `survey_url` for the
sibling `SURVEY.md`. The one `publisher` value applies to both files. Do not add
per-file versions, hashes, digests, checksums, or integrity fields.

Manifest schema version 1 allows these `type` values:

- `core`: required review doctrine and project survey behavior;
- `language`: language semantics, runtime, toolchain, and package hazards;
- `framework`: framework lifecycle, conventions, and deployment hazards;
- `paradigm`: architectural and programming-model failure modes;
- `storage`: database, cache, search, file, and analytical storage semantics;
- `platform`: cross-cutting protocols, operations, security, and infrastructure;

Choose the narrowest truthful type. Do not create copies of the same guidance
under several types. Framework skills build on language skills, but published
skills do not declare transitive dependencies or independent versions. Any
unreleased build keeps `grumpydev_version` at `1`. After the first actual
release, any published skill change increments the overall integer
`grumpydev_version`.

## Review checklist

- Frontmatter parses and contains only the required keys.
- Name and folder follow the naming rules.
- Description is an effective trigger, not a slogan.
- Review instructions are substantive, imperative, and domain-specific without
  becoming an elementary tutorial.
- Sections contain one cohesive domain-specific instruction set, not an
  original block followed by generic expansion boilerplate.
- Specialist body prose is wrapped for direct review, apart from unavoidable
  long tokens and the frontmatter description.
- The operating model, failure paths, recovery, and verification evidence are
  sufficient to change an actual plan review.
- `Recurring traps` calls out concrete domain patterns rather than generic
  caution or a renamed topic list.
- The survey companion inspects evidence before asking and records only durable
  project context.
- The survey companion contributes domain-specific deployment or execution
  candidates, records them once in `DEP-###` or `INF-###`, and can legitimately
  contribute zero questions when evidence is sufficient.
- Operational state, support commitment, deployment ownership, and confidence
  remain distinct when they affect the domain.
- Ordinary reviews never load the survey companion.
- Findings require evidence and distinguish fact from inference.
- Advice accounts for failure recovery, not only the happy path.
- No hidden dependencies, executable payloads, or expanded authority.
- Representative plans have been reviewed with and without the skill to confirm
  it materially changes the analysis.
- Development-only catalog validation and behavioral fixtures live outside the
  served site under `/tools` and `/tests`.

## Publication

Submit source and representative examples for review. Publishers validate the
skill structure, inspect safety and provenance, test its review behavior, then
publish the file and update its manifest entry. Do not publish a changed skill
under an old overall version.
