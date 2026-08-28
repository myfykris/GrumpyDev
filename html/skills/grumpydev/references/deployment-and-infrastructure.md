# Deployment and infrastructure review

## Apply deployment and execution profiles

When `.grump` contains deployment and execution profiles, load every applicable
`DEP-###` entry and any referenced shared `INF-###` components during the
initial evidence pass. Map each planned change to the profiles that will build,
run, consume, migrate, or operate it. Do not assume that a web request, worker,
scheduled task, command-line process, desktop client, mobile client, migration,
or data pipeline has the same runtime and failure boundaries as another.

For each affected profile:

- distinguish `current`, `planned`, and `retiring` operational states;
- apply its `required`, `supported`, `best effort`, or `unsupported` support
  commitment without converting support into evidence that an environment
  exists;
- honor whether deployment ownership is `project`, `customer`, `vendor`, or
  `shared`, especially when the project cannot inspect or control the boundary;
- preserve whether facts are `confirmed`, `inferred`, or `unresolved` and cite
  the evidence scope; and
- check the workload path, runtime and process model, resource limits, network
  and trust boundaries, storage and delivery behavior, recovery, deployment
  order, mixed-version operation, and material environment differences that
  affect the plan.

Every active installed specialist already participates in the review. Use the
actual profiles and planned boundaries to determine which specialists have a
plausible direct or indirect material effect and therefore need supporting
references. A dependency used only by a build tool, a retired profile, or an
unsupported consumer can still participate without governing the verdict.
Conversely, a customer-operated or externally configured runtime can make an
installed specialist material even when its configuration is absent from the
repository. Never load specialist `SURVEY.md` files during an ordinary review.

Treat `application-security` as materially affected whenever the work directly
or indirectly affects identity, authentication, authorization, tenant or trust
boundaries, exposed endpoints, untrusted input or output, parsers, uploads,
filesystem access, server-side URL fetches, deserialization, code or command
execution, secrets, payments, or sensitive data. The absence of a security
section in the plan is not evidence that the boundary is unaffected. Treat
`dependency-supply-chain` as materially affected when dependencies, build
tools, generated code, packages, images, or artifact promotion change. Apply
the same test to installed API, browser, mobile, identity, storage, deployment,
LLM, agentic, and MCP specialists. If a materially relevant specialist is not
installed, report incomplete coverage without fetching it.

Keep conflicting evidence at its real scope. For example, repository
configuration can establish the checked-in default while a user statement
establishes a different planned target. Report the current-versus-intended gap
instead of replacing either fact. Do not claim that repository evidence proves
an environment owned by a customer or vendor matches it.

Classify missing infrastructure information by consequence:

- a plan defect when the plan should define the boundary, owner, transition,
  validation, or recovery action;
- decision-affecting research when evidence must be gathered before a material
  design choice can be made; or
- a project decision when only the user or another accountable owner can choose
  the constraint or accepted risk.

Apply the existing decision-affecting research policy when an infrastructure
unknown can materially change architecture, sequencing, compatibility,
security, recovery, cost, or the verdict. In interactive mode, ask one
deduplicated `RQ###` question only when the answer is needed and available
evidence cannot resolve it. In non-interactive mode, preserve the question and
affected conclusion under `Evidence gaps`.

When a review answer materially changes a durable profile or shared component,
offer to promote that knowledge under the doctrine-promotion rules. Cite the
affected `DEP-###` and `INF-###` identifiers in findings, evidence gaps, and the
verdict rationale. Do not silently rewrite profile state, support commitment,
confidence, deployment ownership, or source scope.
