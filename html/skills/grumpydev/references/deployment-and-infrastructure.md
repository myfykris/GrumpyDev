# Deployment and infrastructure review

Load this reference only when runtime, environment, migration, capacity,
deployment, rollback, or recovery can materially change a review conclusion.

## Establish the affected execution boundaries

Identify each materially different path that will build, run, consume, migrate,
or operate the reviewed work. This can include web requests, workers, scheduled
jobs, command-line processes, desktop or mobile clients, data pipelines,
migrations, and customer- or vendor-operated environments.

Use applicable facts in `.grump`, including `DEP-###` or `INF-###` entries when
they exist, without requiring those identifiers for a simple project. For each
affected path, establish only the facts that can change judgment:

- runtime, process, operating-system, architecture, and version boundaries;
- workload, traffic, data size, concurrency, resource, and capacity limits;
- network, identity, trust, secret, filesystem, storage, and delivery behavior;
- artifact construction, configuration authority, and deployment ownership;
- rollout order, old and new version overlap, migration, drain, and restart;
- rollback limits, restoration source, recovery objectives, and recovery owner;
  and
- material differences among development, test, build, staging, production,
  customer, vendor, regional, or offline environments.

Do not assume two paths share behavior merely because they use the same source
code. Do not assume repository configuration proves what an external or
deployed environment actually runs. Preserve conflicting current and intended
facts at their real evidence scope.

## Follow material effects through specialists

Every active installed specialist entrypoint already participates in the
review. Use the established execution boundaries to decide which specialist
references have a direct or indirect trigger. A build-only dependency,
customer-operated runtime, external identity system, data store, proxy, queue,
or deployment platform can be material even when the reviewed files do not
configure it directly.

If project evidence exposes a material technology or boundary whose specialist
is not installed, report the coverage gap without downloading anything during
the review. Never load specialist `SURVEY.md` files as review guidance.

## Classify missing deployment information

Treat a missing fact as:

- a plan defect when the plan should define the boundary, owner, transition,
  validation, or recovery action;
- decision-affecting research when evidence must be gathered before a material
  design choice can be made; or
- a project decision when an accountable person must choose a constraint or
  accept a tradeoff.

Apply the stored research and review-question policies. In interactive mode,
ask one deduplicated `RQ###` question only when the answer can change a finding,
severity, required action, or verdict. In non-interactive mode, preserve the
question and affected conclusion under `Evidence gaps`.

When a review answer appears to establish durable project-wide runtime or
infrastructure knowledge, offer doctrine promotion under the normal promotion
rules. Do not silently rewrite `.grump`, access production, or treat review or
research permission as authority to deploy or change infrastructure.
