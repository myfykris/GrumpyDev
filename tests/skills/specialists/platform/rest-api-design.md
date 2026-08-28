# rest-api-design behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which clients depend on the changed resource, method, schema, status, and
  error contract?
- What idempotency, object and property authorization, business-flow abuse,
  resource limits, upstream trust, pagination, caching, and compatibility
  behavior applies?

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

## API abuse case

Review a plan that checks login at the route, binds request JSON directly to a
record, uses an IP rate limit for a high-value business flow, and trusts a
vendor response including redirects.

Expected behavior:

- Require object, property, function, tenant, and state authorization plus an
  explicit mutable-property allowlist.
- Analyze business-flow automation by actor and tenant rather than treating an
  IP limit as sufficient.
- Treat the vendor response and redirect as hostile, with schema, semantic,
  timeout, size, decompression, destination, and local-policy checks.

## Applicability boundary case

Compare a resource-oriented HTTP API that relies on methods, statuses,
conditional requests and cache semantics with a GraphQL endpoint, gRPC gateway,
RPC-style JSON endpoint and webhook that merely use HTTP as transport.

Expected behavior:

- Apply this specialist to the resource-oriented contract.
- Do not install or apply it to the other endpoints solely because they use
  HTTP. Use their specific skills unless part of their contract deliberately
  depends on REST and HTTP resource semantics.

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

- Domain boundary: Gateway and proxy path, TLS
  and identity, cache, body and timeout limits, retries, regions, version
  rollout, rate limits, and object-authorization boundary.

Expected behavior:

- Include the unresolved domain facts in the same initial batch as the core
  profile confirmation.
- Record confirmed facts on the applicable `DEP-###` profile and reference a
  shared `INF-###` component when several profiles use it.
- Ask nothing from this contribution when repository evidence and the core
  profile already resolve every material fact.

## Focused-reference routing cases

### `references/authorization-input-and-abuse.md`

Positive trigger: the plan changes authentication, object or property authorization, tenant isolation, mutable fields, validation, bulk operations, uploads, body or decompression limits, expensive filters, automation-sensitive business flows, rate limits, or abuse controls.

Expected behavior:

- Standard or deep mode loads `references/authorization-input-and-abuse.md`.
- The review applies the focused checks in `references/authorization-input-and-abuse.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/authorization-input-and-abuse.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/idempotency-pagination-and-caching.md`

Positive trigger: the plan changes retried mutations, idempotency keys, concurrent duplicate requests, asynchronous jobs, pagination, ordering under concurrent writes, conditional requests, cache keys, cache variance, or stale behavior.

Expected behavior:

- Standard or deep mode loads `references/idempotency-pagination-and-caching.md`.
- The review applies the focused checks in `references/idempotency-pagination-and-caching.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/idempotency-pagination-and-caching.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/versioning-upstreams-and-evolution.md`

Positive trigger: the plan changes public contracts, independently deployed clients, versions, deprecation, compatibility, error formats, third-party or upstream responses, redirects, exposed routes, administrative surfaces, retirement, mixed versions, or rollout sequencing.

Expected behavior:

- Standard or deep mode loads `references/versioning-upstreams-and-evolution.md`.
- The review applies the focused checks in `references/versioning-upstreams-and-evolution.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/versioning-upstreams-and-evolution.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.
