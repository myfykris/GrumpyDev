# application-security behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which actors cross each changed trust boundary, and where are object,
  property, function, tenant, and state-change permissions enforced?
- Which hostile input or output context, abuse case, exceptional failure,
  credential failure, or incident response path can change the design?

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

## Adversarial-boundary case

Review a plan that authenticates a route, accepts an uploaded archive, renders
user content, and follows a user-supplied URL, but says only to sanitize input.

Expected behavior:

- Require object, property, action, and tenant authorization rather than
  accepting route authentication as access control.
- Identify the exact output context, archive and filesystem boundary, upload
  limits, destination and redirect policy, DNS and address handling, egress,
  timeout, and response limits.
- Require fail-closed and denied-case evidence without inventing findings for a
  boundary the plan and repository do not contain.

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

- Domain boundary: Trust zones, internet
  exposure, identities, service accounts, tenant boundaries, TLS termination,
  proxy trust, egress, secret sources, logging, and security ownership.

Expected behavior:

- Include the unresolved domain facts in the same initial batch as the core
  profile confirmation.
- Record confirmed facts on the applicable `DEP-###` profile and reference a
  shared `INF-###` component when several profiles use it.
- Ask nothing from this contribution when repository evidence and the core
  profile already resolve every material fact.

## Focused-reference routing cases

### `references/identity-sessions-and-authorization.md`

Positive trigger: the plan changes authentication, object or property authorization, tenant isolation, session creation or rotation, cookies, CSRF, CORS, account recovery, revocation, role changes, or security-sensitive state transitions.

Expected behavior:

- Standard or deep mode loads `references/identity-sessions-and-authorization.md`.
- The review applies the focused checks in `references/identity-sessions-and-authorization.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/identity-sessions-and-authorization.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/injection-output-and-untrusted-input.md`

Positive trigger: untrusted data can reach HTML, attributes, URLs, CSS, JavaScript, SQL, NoSQL, operating-system commands, code, templates, dynamic identifiers, parsers, canonicalization, or other instruction-bearing sinks.

Expected behavior:

- Standard or deep mode loads `references/injection-output-and-untrusted-input.md`.
- The review applies the focused checks in `references/injection-output-and-untrusted-input.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/injection-output-and-untrusted-input.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/files-uploads-ssrf-and-deserialization.md`

Positive trigger: the plan changes file or archive handling, uploads, path resolution, symlinks, temporary files, decompression, server-side URL fetching, redirects, DNS resolution, private network access, object deserialization, or schema and allocation limits.

Expected behavior:

- Standard or deep mode loads `references/files-uploads-ssrf-and-deserialization.md`.
- The review applies the focused checks in `references/files-uploads-ssrf-and-deserialization.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/files-uploads-ssrf-and-deserialization.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/cryptography-abuse-and-incident-response.md`

Positive trigger: the plan changes encryption, hashing, signatures, tokens, key management, secret rotation, rate limits, automation abuse, fail-closed behavior, security logs, vulnerability response, patch ownership, alerts, or incident handling.

Expected behavior:

- Standard or deep mode loads `references/cryptography-abuse-and-incident-response.md`.
- The review applies the focused checks in `references/cryptography-abuse-and-incident-response.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/cryptography-abuse-and-incident-response.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.
