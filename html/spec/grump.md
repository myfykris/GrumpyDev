# `.grump` project doctrine specification

`.grump` is an agent-generated, human-owned Markdown file at the repository
root. The agent creates it from repository evidence, survey answers, and
explicit user corrections. It records the stable facts and decisions an
adversarial engineering reviewer must respect. It is not application runtime
configuration, a transcript, a backlog, or a place to hide unresolved
assumptions.

## Ownership rules

- Humans own the file and may edit it directly.
- Agents treat recognized review-policy values in this human-owned file as
  standing policy only for the narrowly scoped local actions those values
  describe.
- Agents may propose or apply edits only within the user's granted authority.
- Preserve manual wording and unknown sections during re-survey.
- Do not silently turn an inference into a constraint.
- Prefer repository evidence; identify the source of important claims.
- Keep the file compact enough to read for every planning review.

## Stable identifiers

Use stable identifiers for statements that plans or reviews may reference:

- `CON-###` - non-negotiable constraint
- `ACC-###` - accepted tradeoff or known risk
- `DEC-###` - durable engineering decision
- `UNK-###` - unresolved question that may change a plan
- `DEP-###` - deployment, execution, build, or consumer profile
- `INF-###` - shared infrastructure component used by multiple profiles

Never renumber an existing identifier merely for neatness. Retire obsolete
statements or profiles explicitly so old review references remain
understandable. Preserve a profile or component identifier through correction
and rename.

## Recommended structure

```markdown
# Project doctrine

## Purpose and success conditions

## System boundaries

## Project documentation
- `path/or/location`: scope, authority or status when known, and what it
  establishes

## Review output policy
- Plan addenda: allowed | chat only | unresolved
- Source: Q### or explicit user statement

## Review interaction policy
- Review questions: interactive | non-interactive | unresolved
- Source: Q### or explicit user statement

## Doctrine maintenance policy
- Confirmed doctrine updates: allowed | propose only | unresolved
- Source: Q### or explicit user statement

## Plan readiness policy
- Decision-affecting research: resolve first | gated discovery | unresolved
- Source: Q### or explicit user statement

## Research execution policy
- Research execution: automatic | ask first | report only | unresolved
- Source: Q### or explicit user statement

## Specialist survey status
- `<skill-name>`: applied | current | incomplete
  - Last surveyed: ISO 8601 UTC time when useful
  - Evidence: paths or explicit user statements
  - Missing material context: none | concise description

## Deployment and execution profiles
- [DEP-001] Concise profile name
  - Operational state: current | planned | retiring
  - Support commitment: required | supported | best effort | unsupported
  - Confidence: confirmed | inferred | unresolved
  - Deployment ownership: project | customer | vendor | shared
  - Workload and path: ...
  - Runtime and process model: ...
  - Operating target and material resource limits: ...
  - Network, identity, trust, encoding, and security boundaries: ...
  - State, delivery, recovery, and responsible owner: ...
  - Shared infrastructure: INF-### | none
  - Material environment differences: ...
  - Evidence and scope: ...

## Shared infrastructure
- [INF-001] Concise component name
  - Type and responsibility: ...
  - Operational state: current | planned | retiring
  - Support commitment: required | supported | best effort | unsupported
  - Confidence: confirmed | inferred | unresolved
  - Deployment ownership: project | customer | vendor | shared
  - Material contract, limits, recovery, and failure domain: ...
  - Used by: DEP-###, DEP-###
  - Evidence and scope: ...

## Technology and runtime

## Non-negotiable constraints
- [CON-001] ...

## Accepted tradeoffs
- [ACC-001] ...

## Durable decisions
- [DEC-001] ...

## Data and integration invariants

## Delivery, operations, and rollback

## Test and evidence expectations

## Unknowns
- [UNK-001] ...

## Survey evidence
- `path/to/file`: what it established
```

Omit empty sections only when their absence cannot be mistaken for an incomplete
survey. Use `None identified` when that distinction matters.

## Evidence quality

Prefer claims supported by repository paths, checked configuration, or explicit
user statements. Mark conclusions based on pattern inference as `Inferred` and
state what would falsify them. Do not include secrets, credentials, private
customer data, or copied production payloads.

Record relevant project documents with enough detail for a later reviewer to
find and apply them. Note whether a document is authoritative, advisory, draft,
historical, or of unknown status when that distinction is known and material.
Do not silently resolve a contradiction between documentation and repository
behavior; preserve it as evidence or an unknown until it is settled.

## Deployment and execution profiles

Record a profile for each materially different boundary that builds, runs,
consumes, migrates, or operates the software. Examples include production web
requests, background workers, scheduled jobs, administrative command-line
processes, desktop or mobile clients, data pipelines, and maintenance or
migration processes. For a library, schema package, or build-time tool, use a
supported build, runtime, or consumer profile only when that boundary can
change compatibility, correctness, security, packaging, or test evidence. Do
not invent hosting for a non-deployable artifact.

Keep these dimensions separate:

- `Operational state` says whether the profile is current, planned, or being
  retired.
- `Support commitment` says whether the project requires, supports, tolerates
  on a best-effort basis, or does not support that profile.
- `Confidence` says whether the recorded fact is confirmed, inferred, or
  unresolved.
- `Deployment ownership` says whether the project, customer, vendor, or a
  shared arrangement controls the deployed boundary.

A planned profile can be required and confirmed. A current customer-operated
profile can be supported but inferred because the repository cannot prove the
customer's actual configuration. Do not collapse these distinctions into one
status field.

Record the smallest set of durable facts that could change a review. Include a
representative request or event path, runtime and process model, material
resource limits, network and trust boundaries, data and delivery behavior,
recovery, deployment ownership, environment differences, and scoped evidence
when they apply. Exclude host inventories, credentials, secrets, raw production
data, and temporary rollout details that do not establish lasting doctrine.

When several profiles use the same material database, cache, queue, object
store, gateway, identity service, or other component, record it once as an
`INF-###` shared-infrastructure entry and reference it from each `DEP-###`
profile. Keep a component inline when only one profile uses it and extraction
would add no clarity. A shared entry does not replace profile-specific facts
such as connection limits, identity, traffic shape, or failure consequences.

Repository configuration establishes what the checked artifact declares,
project documentation establishes what it states within its authority and
scope, and an explicit user statement establishes the asserted project fact or
intent. Preserve material conflicts at those scopes. A confirmed planned target
can coexist with a different current configuration. Never claim checked-in
configuration proves a customer-operated or vendor-operated environment.

When deployment information remains unknown, use `UNK-###` only if the answer
could materially change architecture, sequencing, compatibility, security,
recovery, operating cost, or a verdict. Apply the plan-readiness policy to
decision-affecting infrastructure research just as to any other research.
Distinguish research from a project decision that only an accountable owner can
make.

## Review output policy

Record whether the user granted standing permission for GrumpyDev to append
completed evaluations to the local plan files it reviews. `Allowed` authorizes
only the GrumpyDev addendum behavior defined by the core skill. `Chat only` and
`Unresolved` do not authorize a plan-file change. Record the numbered survey
answer or explicit user statement that established the policy. This preference
does not grant permission to modify plan content outside the addendum, create
alternative files, edit remote documents, or publish anything.

The source records audit provenance; it is not authentication. A missing source
on a human-authored policy is a maintenance problem, not proof that the policy
is unauthorized. Malformed, unknown, or contradictory policy values grant no
write. A current explicit user instruction overrides the stored policy for the
current work without silently rewriting it.

## Review interaction policy

Record whether plan reviews should pause after their initial evidence pass to
ask material questions. `Interactive` permits plan-scoped realtime Q&A.
`Non-interactive` completes the review without pausing and reports unanswered
material questions as evidence gaps. `Unresolved` defaults to interactive. A
current explicit instruction may override the preference for one evaluation.

Installation-survey questions use a continuous `Q###` sequence and establish
durable repository policy. Live plan-review questions use `RQ###`, restart at
`RQ001` for each evaluation, and remain scoped to that plan and evaluation.
They are not `.grump` doctrine merely because the user answered them.

## Doctrine maintenance policy

Record whether the user granted standing permission to write explicitly
confirmed project facts and decisions into `.grump`. `Allowed` applies only
after an unambiguous user statement resolves an unknown, accepts a tradeoff, or
confirms or changes a durable constraint or decision. `Propose only` and
`Unresolved` require the agent to show the proposed change in chat without
writing it.

This policy never turns an inference, review recommendation, or unanswered
question into doctrine. It grants no permission to modify other files or any
external system. Preserve stable identifiers and historical meaning when an
allowed update is applied.

When a live review answer appears materially useful as durable project
doctrine, GrumpyDev may ask whether to treat it as `project-wide` or keep it as
`this review only`. Only an explicit project-wide answer confirms the scope.
The doctrine maintenance policy separately controls whether GrumpyDev writes
the item or only proposes the exact change. Record an allowed promotion's
source as the evaluation timestamp, reviewed plan path, and `RQ###` identifier.

## Plan readiness policy

Record whether unresolved research that can materially change an implementation
decision must be resolved before an implementation plan can be approved or may
be handled as a separately gated discovery plan. `Resolve first` requires the
research result and selected decision before implementation-plan approval.
`Gated discovery` permits approval only when the reviewed scope is a bounded
discovery plan with explicit research questions, evidence methods, decision
criteria, stopping conditions, and downstream decisions. It never approves the
dependent implementation. `Unresolved` defaults to gated discovery.

Research is decision-affecting when its outcome could materially change
architecture, scope, safety, data or migration design, an external contract,
sequencing, rollback, cost, or the verdict. Ordinary validation of an already
selected design is not automatically decision-affecting when the plan specifies
the response to either outcome and leaves no material design choice open.

## Research execution policy

Record whether GrumpyDev should perform needed decision-affecting research
automatically, ask first, or report it without researching. `Automatic` permits
safe, read-only research within the host's existing permissions. `Ask first`
requires a plan-scoped permission question before research. `Report only`
preserves the work as an evidence gap. `Unresolved` defaults to ask first.

This preference does not authorize a project change, external write,
production or secret access, paid service, software installation, downloaded
code execution, or state-changing experiment. Those actions retain their own
permission requirements. Research results must identify their sources, relevant
version or date scope, confidence, and the implementation decision they affect.
An answer that requires project-owner judgment cannot be replaced by research.

## Specialist survey status

Record which installed specialist survey contributions supplied the durable
context in `.grump`. `Applied` means the contribution was read for the current
survey. `Current` means an earlier answer and its evidence remain usable, so the
question was not repeated. `Incomplete` means a missing answer can materially
limit future reviews; identify that gap and use an `UNK-###` item when
appropriate.

This status is routing evidence, not a dependency version or integrity system.
Do not record hashes, checksums, secrets, raw transcripts, or transient machine
details. Ordinary Grump reviews use the resulting doctrine and do not load the
specialist `SURVEY.md` files.

## Accepted constraints in reviews

A reviewer must not repeatedly argue against an accepted tradeoff merely because
it would have chosen differently. Reopen an accepted item only when:

1. the proposed plan exceeds its stated scope;
2. new evidence invalidates its premise;
3. it conflicts with a stronger constraint; or
4. the user explicitly asks to revisit it.

When reopening an item, cite its stable identifier and the new evidence.

## Re-survey and change handling

Recommend an explicit re-survey after major architecture, deployment, data, or
integration changes. Deployment-specific triggers include adding or retiring a
workload type, changing runtime or process model, changing hosting or deployment
ownership, adding a materially different supported environment, moving a trust
or network boundary, changing a shared stateful component, revising recovery or
delivery behavior, or discovering that recorded evidence no longer describes
the current or planned target.

Merge evidence into the existing file. Preserve human notes, accepted items,
and `DEP-###` and `INF-###` references; propose changes instead of replacing the
file wholesale. Rename in place, record corrected facts with their new source,
and retire obsolete profiles or components without renumbering later entries.
Add a short `Last surveyed` date only if the team finds it useful; the
installation state already records tool check times.
