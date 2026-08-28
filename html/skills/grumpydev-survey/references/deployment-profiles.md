# Survey deployment profiles

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
