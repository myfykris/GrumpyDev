# object-storage behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which provider and product, namespace, region, object or blob type, client API,
  and exact compatibility guarantees apply?
- Which version, generation, ETag, lease, or conditional-operation rules prevent
  overwrite races, and how do transfers, deletion, lifecycle, events,
  replication, archive retrieval and recovery behave?

Expected behavior:

- Ask only the unresolved questions that can change the verdict, severity, or
  required action.
- Apply the skill's domain-specific critical and lower-severity conditions.

## Resolved-evidence case

Review the same plan after repository evidence or explicit plan content
resolves the material decisions.

Expected behavior:

- Ask zero questions that the evidence already answers.
- Downgrade or omit findings that the supplied evidence invalidates.

## Provider-semantics cases

Review equivalent conditional-write and large-upload plans for Amazon S3,
Google Cloud Storage, Azure Blob Storage, and an S3-compatible self-hosted
service.

Expected behavior:

- Apply the shared object identity, integrity, access, lifecycle, event, cost
  and recovery checks to all four providers.
- For S3, verify conditional requests, version IDs, delete markers, multipart
  completion and conflict responses without treating ETag as a universal
  checksum.
- For Google Cloud Storage, use generation and metageneration preconditions and
  separate object consistency from IAM propagation and caching.
- For Azure Blob Storage, distinguish blob types, ETags, leases, block commits,
  SAS or Entra authorization and access tiers.
- Treat S3 compatibility as a feature-by-feature claim that must be verified.

## Evidence-resolved survey case

Run initial setup or an explicit re-survey after `.grump`, repository evidence,
and project documentation already establish every applicable durable fact for
this specialist.

Expected behavior:

- Load this specialist's `SURVEY.md` because this is a survey operation.
- Ask zero questions whose decisions are already supported by current evidence.
- Preserve concise doctrine with useful evidence references and mark the
  specialist survey contribution current.

## Material survey-gap case

Run initial setup or an explicit re-survey when inspection leaves one durable
project fact unresolved and that fact will materially change future reviews in
this domain.

Expected behavior:

- Ask only the unresolved durable question after pooling and deduplicating all
  applicable specialist contributions.
- Let the survey orchestrator assign its sequential question identifier; do not
  obtain a fixed identifier from `SURVEY.md`.
- Record the confirmed answer as project doctrine or record a deliberate
  deferral as unresolved without inventing a default.

## Ordinary-review loading case

Run an ordinary Grump review after setup has saved the project's durable domain
context in `.grump`.

Expected behavior:

- Because this specialist is installed and not explicitly marked inapplicable,
  every explicitly invoked GrumpyDev review loads its `SKILL.md`, even when the
  reviewed work does not name or modify this domain.
- The entrypoint evaluates direct and indirect effects before deciding whether
  supporting references or findings are needed.
- When no material effect exists, the specialist produces no finding.
- Lean mode loads this specialist's `SKILL.md` and saved doctrine without
  loading `references/review.md` unless an entrypoint escalation trigger
  applies.
- Standard mode loads `SKILL.md` and loads `references/review.md` only when
  the entrypoint identifies a plausible direct or indirect material effect.
- Deep mode loads every applicable local reference for the affected boundary.
- No ordinary review loads this specialist's `SURVEY.md`.
- Ask a review-scoped question only if a material decision remains unresolved
  after inspecting the plan, repository, documentation, and agent context.

## Companion-overlap case

Run setup with this specialist and a companion specialist whose survey proposes
the same underlying version, runtime, ownership, deployment, or recovery
decision using different wording.

Expected behavior:

- Pool both contributions before numbering questions.
- Ask one combined question for the shared decision rather than one question
  per file, while retaining any genuinely distinct domain choices.
- Record one coherent project fact in `.grump` and mark both contributions
  appropriately.

## Infrastructure-profile case

Run initial setup or an explicit re-survey with an applicable execution profile
and this domain boundary:

- Domain boundary: Provider or product, region, account and bucket or container
  boundary, object or blob type, version, generation, ETag or lease behavior,
  replication, access identity, signed access, endpoint, encryption, lifecycle,
  transfer protocol, archive retrieval, events, cost, and recovery.

Expected behavior:

- Include the unresolved domain facts in the same initial batch as the core
  profile confirmation.
- Record confirmed facts on the applicable `DEP-###` profile and reference a
  shared `INF-###` component when several profiles use it.
- Ask nothing from this contribution when repository evidence and the core
  profile already resolve every material fact.
