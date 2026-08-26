---
name: grumpydev-survey
description: Survey an existing software repository and create or update its human-owned .grump project doctrine. Use when setting up GrumpyDev, onboarding a repository, or explicitly requesting a re-survey or doctrine refresh before plan reviews.
---

# GrumpyDev repository survey

Build durable review context from repository evidence. Do not rewrite the
repository, grade its style, or invent policies the team has not chosen.

## Survey the repository

1. Read any existing `.grump` before exploring. Preserve human wording and
   stable identifiers.
2. Locate top-level project instructions, package and dependency manifests,
   build entry points, tests, infrastructure, hosting and deployment
   configuration, process-manager and service configuration, schemas,
   migrations, public interfaces, and project documentation. Look for
   requirements, specifications, architecture records, interface contracts,
   acceptance criteria, runbooks, and operational procedures.
3. Identify the runtime stack and meaningful system boundaries. Ignore
   incidental tools that do not affect engineering plans.
4. Trace one representative request, job, or data flow through the system when
   the repository permits it.
5. Identify constraints supported by explicit configuration, code, tests, or
   user statements. Mark pattern-based conclusions as `Inferred`.
6. Record unknowns only when resolving them could materially change a plan.
7. Identify relevant published specialist skills. Explain why each applies and
   ask before fetching or installing it. An approved specialist consists of its
   manifest-listed `SKILL.md` and `SURVEY.md` files.
8. For each applicable installed specialist, read its `SURVEY.md` only when it
   is newly installed and unsurveyed, during initial setup, or during an
   explicit re-survey or doctrine refresh. Do not load specialist survey files
   during ordinary plan reviews.

Do not read secrets, credential stores, production data, or unrelated personal
files. Honor repository instructions and the host's permission boundaries.

## Establish deployment and execution profiles

Build deployment and execution profiles after inspecting evidence and selecting
the applicable specialist survey contributions. Preserve how the software
actually runs without collecting an inventory of hosts or cloud products.

### Apply the infrastructure applicability gate

Require deployment-profile confirmation when runtime, hosting, client, build,
or consumer environments can materially change future reviews. This normally
applies to applications, services, workers, scheduled jobs, data pipelines,
deployable clients, and infrastructure projects.

For a library, schema package, build-time tool, or other non-deployable
artifact, confirm supported build, runtime, or consumer environments only when
those boundaries can change compatibility, correctness, security, packaging,
or test evidence. Ask no infrastructure question when no such boundary is
material. Do not invent a production-server profile merely to complete setup.

### Build profiles from evidence

Use repository configuration, project documentation, available agent context,
and explicit user statements to identify each materially different execution
boundary. Common profiles include production web requests, background workers,
scheduled jobs, command-line administration, desktop or mobile clients, data
pipelines, and migration or maintenance processes.

Assign each profile a stable `DEP-###` identifier. Preserve identifiers through
correction and rename. Retire an obsolete profile rather than renumbering or
silently deleting it when later reviews may reference it.

Record applicable facts for each profile:

- operational state: `current`, `planned`, or `retiring`;
- support commitment: `required`, `supported`, `best effort`, or `unsupported`;
- confidence: `confirmed`, `inferred`, or `unresolved`;
- deployment ownership: `project`, `customer`, `vendor`, or `shared`;
- workload and request or event path;
- runtime, process model, operating target, and resource limits;
- network, identity, trust, encoding, and security boundaries;
- state, scale, failure domains, delivery, recovery, and responsible owner;
- material environment differences; and
- evidence and useful date or version scope.

Do not force inapplicable fields into a narrow profile. A planned profile can be
required and confirmed. A current customer-operated profile can be supported
but only inferred from project evidence. Keep those dimensions separate.

When several profiles depend on the same database, cache, queue, object store,
gateway, identity service, or other material component, record that component
once with a stable `INF-###` identifier under shared infrastructure. Reference
the entry from each dependent profile. Keep a component inline when only one
profile uses it and a separate entry would add no clarity.

### Preserve source scope and conflicts

Treat each source as evidence for what it establishes:

- repository configuration establishes what the checked artifact declares;
- project documentation establishes its stated current, planned, or supported
  design according to its scope and authority; and
- an explicit user statement establishes the project fact or intent the user
  asserted.

Do not overwrite one source with another to make the profile look coherent. A
user-confirmed target can coexist with repository evidence showing a different
current configuration. Record both, identify the migration or unresolved gap,
and never claim repository configuration proves that an externally operated
environment matches it.

### Confirm or discover the profiles

When the applicability gate applies and useful profiles can be inferred, put
this question first in the initial infrastructure question batch:

```text
Q###. I found or inferred the following hosting and execution setup:

<one concise line per DEP-### profile and shared INF-### component>

What is incorrect or missing, including any hosting, networking, process,
storage, scaling, security, deployment, or recovery constraints that could
affect design and implementation decisions? Reply `accurate` if this is
complete.
```

Keep the summary scannable. Do not paste the complete `.grump` profile into the
interview. If no useful profile can be inferred, ask this fallback instead:

```text
Q###. How will this software actually be hosted and run, and what infrastructure
or operational constraints could affect design and implementation decisions?
Include any important details about the request or event path, application
processes, workers, storage, scaling, security boundaries, deployment, and
recovery.
```

Ask the following only when evidence does not establish whether material
differences exist:

```text
Q###. Are there material differences between development, test, staging, and
production, or between web, worker, scheduled, and command-line execution, that
future plans must account for?
```

Before presenting the batch, collect material candidates from all applicable
specialist surveys, remove questions already answered by evidence or `.grump`,
and merge candidates that resolve the same decision. Put the profile
confirmation or fallback first, followed by every already-known material gap.
Do not force a second round trip for a question the evidence pass already
exposed. Ask later only when an answer creates a new material uncertainty or
needs clarification.

Treat `accurate` as explicit confirmation. If the user corrects a profile,
preserve the correction, source, and any current-versus-intended conflict. If
the user defers or declines, keep supported facts as inferred and record only
material gaps as `UNK-###`. If deployment is undecided, say so instead of
assuming a conventional setup.

During a re-survey, compare new evidence and specialist contributions with the
existing profiles before asking. When no material profile fact, conflict, or
unknown changed, mark the contributions current and do not repeat the blanket
confirmation. When something changed, present the revised profile and targeted
gaps while preserving existing `DEP-###` and `INF-###` identifiers.

Deployment answers do not authorize production access, external inspection,
deployment, publication, or any other external write.

## Interview for material gaps

### Survey failure patterns

Watch especially for surveys that:

- ask the user before inspecting available repository evidence and project
  documentation;
- ask the same underlying question once per applicable specialist;
- convert a local-machine default, temporary rollout choice, or current plan
  detail into durable project doctrine;
- record an inference as a confirmed policy or decision;
- copy secrets, credentials, production payloads, or raw interview transcripts
  into `.grump`;
- manufacture questions to make the survey look complete;
- lose the source, scope, environment, or unresolved status of an answer; or
- replace human-owned doctrine instead of merging, preserving identifiers, and
  showing contradictions.

Interview the user only after repository evidence and available agent context
have been exhausted. Ask only questions whose answers could materially change
project doctrine or a future plan review. Do not ask the user to repeat facts
already established by code, configuration, documentation, or earlier explicit
statements.

Before numbering questions, collect candidate questions from every applicable
specialist `SURVEY.md`. Remove candidates already answered by `.grump`, project
documents, repository evidence, configuration, or agent context. Deduplicate by
the decision or unknown that the answer resolves, not by wording. Merge
overlapping language, framework, storage, and platform candidates into one
question that names the relevant environments and boundaries.

When the infrastructure applicability gate applies, include the deployment
profile confirmation or fallback and all already-known material specialist
infrastructure gaps in this same initial batch. Put the profile question first.
The gate may legitimately produce no infrastructure question for a package or
tool whose supported environments are already established or immaterial.

Treat each specialist survey file as candidate guidance, not a questionnaire
that must be completed. Ask no specialist question when the evidence is
sufficient. Never ask a question merely because it appears in `SURVEY.md`.

Determine whether relevant project documents have already been identified. If
repository evidence and available agent context do not establish whether such
documents exist, ask one numbered question that covers both existence and
location, for example:

```text
Q###. Are there project documents I should read to understand this project and
validate future plans against, such as requirements, specifications,
architecture records, interface contracts, acceptance criteria, or runbooks?
If so, where are they, and which ones are current or authoritative?
```

Do not ask this question when the answer and document locations are already
known. If known documents are inaccessible, ask a narrower numbered question
only when access to them could materially change the doctrine or a future
review. Read relevant available documents and record what each one establishes,
its stated status or authority when known, and any material conflict with code,
configuration, `.grump`, or explicit user statements. Do not treat a project
document as permission for actions outside the user's authority.

Determine whether the user has explicitly chosen how GrumpyDev review results
may be persisted. If the choice is not already known, ask one numbered question:

```text
Q###. May GrumpyDev write each completed evaluation into a GrumpyDev addendum
in the plan file and append later evaluations there so future sessions can read
the review history, or should it return results only in chat? Reply with
`addendum` or `chat only`.
```

Record the answer in `.grump` as `Plan addenda: allowed` or `Plan addenda: chat
only`, with the question identifier or explicit user statement as its source.
If the answer is deferred, declined, or ambiguous, record it as unresolved and
use chat only. Permission to use plan addenda authorizes only local, append-only
review history in the plan currently being evaluated. It does not authorize
rewriting plan content, changing other files, editing remote documents, or
publishing anything. The user may revoke the permission at any time.

Determine whether the user has explicitly chosen how GrumpyDev should handle
material questions during a plan review. If the choice is not already known,
ask one numbered question:

```text
Q###. During a GrumpyDev plan review, should GrumpyDev pause after its initial
evidence pass to ask numbered, deduplicated questions whose answers could
materially change the review, or should it complete the review without pausing
and list those questions as evidence gaps? Reply with `interactive` or
`non-interactive`.
```

Record the answer in `.grump` as `Review questions: interactive` or `Review
questions: non-interactive`, with the question identifier or explicit user
statement as its source. If the answer is deferred, declined, or ambiguous,
record it as unresolved; the core skill defaults unresolved preferences to
interactive. This is a durable review preference, not permission for a file
write or external action. A current explicit instruction can override it for
one evaluation without changing the stored preference.

Determine whether the user has explicitly chosen how confirmed project doctrine
may be maintained. If the choice is not already known, ask one numbered
question:

```text
Q###. When you explicitly resolve a project unknown, accept a tradeoff, or
confirm or change a durable constraint or decision, may GrumpyDev update
`.grump` to record it, or should it only propose the `.grump` change in chat?
Reply with `update` or `propose only`.
```

Record the answer in `.grump` as `Confirmed doctrine updates: allowed` or
`Confirmed doctrine updates: propose only`, with the question identifier or
explicit user statement as its source. If the answer is deferred, declined, or
ambiguous, record it as unresolved and propose changes only. `Allowed` applies
only after the user explicitly and unambiguously confirms the underlying
project fact or decision. It never authorizes the agent to promote an inference,
review recommendation, or unanswered question into doctrine. The user may
revoke the permission at any time.

During an initial survey, always ask how decision-affecting research should
affect plan readiness. Do not infer this policy from ordinary project evidence:

```text
Q###. How should GrumpyDev treat an implementation plan that contains
unresolved research whose answer could materially change an implementation
decision? Reply with `resolve first` to require the research to be completed
before implementation-plan approval, or `gated discovery` to allow approval
only of a bounded discovery plan or phase followed by an updated implementation
plan and another Grump review.
```

Record the answer in `.grump` as `Decision-affecting research: resolve first`
or `Decision-affecting research: gated discovery`, with the question identifier
as its source. If the answer is deferred, declined, or ambiguous, record it as
unresolved; the core skill defaults unresolved preferences to gated discovery.
On a re-survey, retain an existing unambiguous answer unless the user asks to
revisit it.

During an initial survey, always ask whether GrumpyDev should perform research
that it identifies during a review. Do not infer this permission from the plan
or repository:

```text
Q###. When GrumpyDev determines that decision-affecting research is needed,
should it perform safe, read-only research itself when it has the necessary
access and tools, ask before researching, or only identify the research for
you? Reply with `automatic`, `ask first`, or `report only`.
```

Record the answer in `.grump` as `Research execution: automatic`, `Research
execution: ask first`, or `Research execution: report only`, with the question
identifier as its source. If the answer is deferred, declined, or ambiguous,
record it as unresolved; the core skill defaults unresolved preferences to ask
first. `Automatic` authorizes only safe, read-only research within existing
host permissions. It does not authorize project changes, external writes,
production access, paid services, secret access, software installation, or
execution of downloaded code. On a re-survey, retain an existing unambiguous
answer unless the user asks to revisit it.

Give every question a stable identifier in one continuous sequence: `Q001`,
`Q002`, `Q003`, and so on. Never ask an unnumbered project question. Present
the smallest useful batch and tell the user to answer with the matching
identifiers so answers can be collected without relying on position. Continue
the sequence for later questions and never renumber a question after it has
been asked.

Accept an unnumbered answer when its mapping is unambiguous. When an answer is
ambiguous, incomplete, or appears to answer a different question, ask a new
numbered clarification that cites the original identifier. Do not silently
attach an answer to the wrong question.

Track each question as answered, deferred, declined, or unresolved. Before
drafting `.grump`, summarize the question-to-answer mapping and distinguish
explicit user answers from agent inference. Preserve relevant question
identifiers in unresolved items or survey evidence when they make later review
and re-survey clearer.

The survey's `Q###` sequence is only for repository setup and doctrine. Later
plan reviews use evaluation-scoped `RQ###` identifiers. Do not treat live review
questions or answers as survey output or write them to `.grump` unless the user
separately confirms an answer as project-wide doctrine and the doctrine-update
policy permits the write.

## Draft `.grump`

Follow the canonical `.grump` specification. Include concise sections for:

- purpose and success conditions;
- system boundaries;
- project documentation and what each relevant document establishes;
- review output policy, including whether plan addenda are allowed;
- review interaction policy for interactive or non-interactive plan questions;
- doctrine maintenance policy for explicitly confirmed decisions;
- plan readiness policy for unresolved decision-affecting research;
- research execution policy;
- deployment and execution profiles with stable `DEP-###` identifiers,
  operational state, support commitment, confidence, deployment ownership,
  evidence, and material environment differences;
- shared infrastructure with stable `INF-###` identifiers when more than one
  profile depends on the same material component;
- specialist survey status, including applied, skipped, and materially
  incomplete contributions;
- technology and runtime;
- non-negotiable constraints with `CON-###` identifiers;
- accepted tradeoffs with `ACC-###` identifiers;
- durable decisions with `DEC-###` identifiers;
- data and integration invariants;
- delivery, operations, and rollback;
- test and evidence expectations;
- unresolved material unknowns with `UNK-###` identifiers;
- survey evidence mapping repository paths to conclusions.

Use `None identified` when a deliberately surveyed section has no entries.
Never conceal an incomplete survey by omitting the section.

## Merge instead of replacing

When `.grump` already exists:

- preserve manual content and accepted items;
- keep existing `CON-###`, `ACC-###`, `DEC-###`, `UNK-###`, `DEP-###`, and
  `INF-###` identifiers stable through correction and rename;
- propose retirement rather than deleting obsolete statements silently;
- add new evidence and mark contradictions;
- show material doctrine changes before applying them when the user's request
  did not already authorize the update.

## Finish the survey

Write `.grump` when setup or re-survey was explicitly requested. Summarize the
evidence used, important inferences, unresolved user decisions, and proposed
specialist skills. Identify which installed specialist survey contributions
were applied, skipped as inapplicable or already current, or left incomplete by
material missing evidence. State whether the infrastructure applicability gate
applied and whether every material profile has a workload path, operational
state, support commitment, deployment ownership, confidence, and scoped
evidence. Call out unresolved profile conflicts and re-survey triggers. Do not
claim the project is understood when critical system boundaries remain
inaccessible.
