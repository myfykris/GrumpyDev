# Runtime and deployment survey

Load this reference only when materially different build, runtime, hosting,
client, worker, migration, or consumer environments can change engineering
decisions.

Inspect repository configuration, project documentation, and explicit user
statements before asking. Identify each materially different workload path,
runtime or process model, operating target, network and trust boundary, storage
dependency, deployment sequence, rollback limit, and recovery owner. Preserve
current and intended states when they differ. Repository configuration proves
only what it declares, not what a customer, vendor, or deployed environment
actually uses.

Use `DEP-###` only when two or more materially different execution or
deployment profiles need stable cross-references. Use `INF-###` only when a
shared infrastructure component is referenced from more than one place. Keep a
simple project as concise bullets under `## Runtime and deployment`.

When useful evidence exists, ask one confirmation question that summarizes the
inferred setup and asks what is wrong or missing. When no useful profile can be
inferred, ask how the software will be built, hosted, run, deployed, and
recovered, limited to facts that can change design or review judgment. Ask a
separate environment-differences question only when evidence leaves a material
difference unresolved.

Pool specialist deployment candidates first and deduplicate them by the
decision they resolve. A PHP SAPI question, web-server question, and process
lifecycle question may be one question when one answer establishes the whole
boundary. If the user defers, preserve supported facts at their actual
confidence and record only material gaps as `UNK-###`. Deployment answers never
authorize access to production or an external change.
