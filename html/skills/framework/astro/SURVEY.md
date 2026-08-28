# Astro survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Astro.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, build and deployment
workflows, project documentation, representative code, tests, and existing .grump doctrine for
Astro. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Astro version, output mode, adapter and host, route rendering
  choices, client frameworks, content sources, environment model, cache policy, and browser
  targets.
- Review doctrine: The plan must distinguish build-time code, request-time server code,
  isolated client code, and public serialized props. It must name which routes require a server
  and which remain deployable as static files.
- Conditional deployment boundary: Astro output mode, adapter, host runtime, route
  prerendering, server and client islands, cache ownership, environment sources, asset handling,
  and production command.

## Ask only when materially unresolved

- Which Astro version, output mode, adapter, host, routes, and client integrations apply?
- Which data is fixed at build time, rendered per request, deferred in a server island, or
  hydrated in a client island?

## Record in .grump

Record confirmed Astro answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Astro doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Astro when its version, rendering mode, deployment adapter, island hydration
strategy, content or data source, cache boundary, or supported host materially changes.
Also re-survey when evidence conflicts with saved doctrine or the user requests a
context refresh.
