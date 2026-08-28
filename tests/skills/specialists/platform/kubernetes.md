# kubernetes behavioral fixture

## Material-gap case

Review a plan in this domain whose available evidence does not answer:

- Which Kubernetes version, workload controller, runtime class, identity, and
  network policy apply to the deployment?
- How do disruption, readiness, resource pressure, autoscaling, rollout, and
  rollback interact?

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

- Domain boundary: cluster, provider,
  versions, nodes, namespaces, controllers, ingress, identity, network policy,
  storage, resources, scaling, rollout, drain, and failure-domain coverage.

Expected behavior:

- Use the existing domain candidates to fill the applicable `DEP-###` profile
  without repeating the core profile confirmation.
- Reference a shared `INF-###` component when several profiles use the same
  material infrastructure.
- Ask zero domain questions when current evidence already establishes the
  profile facts.

## Focused-reference routing cases

### `references/health-lifecycle-and-rollouts.md`

Positive trigger: the plan changes probes, startup, readiness, liveness, termination, pre-stop behavior, disruption budgets, Deployment or StatefulSet rollout strategy, draining, mixed versions, migration order, rollback, or controller replacement.

Expected behavior:

- Standard or deep mode loads `references/health-lifecycle-and-rollouts.md`.
- The review applies the focused checks in `references/health-lifecycle-and-rollouts.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/health-lifecycle-and-rollouts.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/resources-placement-and-scaling.md`

Positive trigger: the plan changes requests, limits, CPU or memory behavior, scheduling, affinity, topology spread, taints, priorities, quotas, autoscaling, cluster scaling, capacity, or overload behavior.

Expected behavior:

- Standard or deep mode loads `references/resources-placement-and-scaling.md`.
- The review applies the focused checks in `references/resources-placement-and-scaling.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/resources-placement-and-scaling.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/networking-identity-and-secrets.md`

Positive trigger: the plan changes Services, Ingress, Gateway API, DNS, network policy, service accounts, RBAC, workload identity, pod security, secrets, certificate rotation, external exposure, or operator access.

Expected behavior:

- Standard or deep mode loads `references/networking-identity-and-secrets.md`.
- The review applies the focused checks in `references/networking-identity-and-secrets.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/networking-identity-and-secrets.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.

### `references/stateful-work-and-recovery.md`

Positive trigger: the plan changes persistent volumes, storage classes, StatefulSets, operators, databases, backup, restore, snapshots, fencing, failover, attachment, regional recovery, or stateful migration.

Expected behavior:

- Standard or deep mode loads `references/stateful-work-and-recovery.md`.
- The review applies the focused checks in `references/stateful-work-and-recovery.md`.

Negative trigger: Review the same specialist with no affected boundary named in the positive trigger.

Expected behavior:

- Standard or deep mode does not load `references/stateful-work-and-recovery.md`.
- Missing evidence follows the material-question or uncertainty policy instead of loading every focused reference.
