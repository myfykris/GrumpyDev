# Cloudflare developer platform survey contribution

## Applicability

Apply this contribution when applications run on Cloudflare Workers or related
developer-platform services. Skip it when Cloudflare developer platform does not
constrain a supported build, runtime, client, data, deployment, or operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, infrastructure, build
and deployment workflows, project documentation, representative code, tests, and existing .grump
doctrine for Cloudflare developer platform. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Cloudflare products, compatibility date and flags, plans and
  limits, routes and domains, bindings, storage consistency requirements, Durable Object
  migrations and placement, D1 topology, queue delivery, cache policy, secrets, and deployment
  environments.
- Review doctrine: A Worker isolate and its global memory are reusable but not durable or
  guaranteed to handle the next request. State consistency must follow the selected storage
  product, not a generic edge assumption.
- Deployment-profile facts: compatibility date and flags, Workers plan and limits,
  routes and domains, regions, bindings, storage products, migrations, queue settings, secrets,
  cache rules, observability, and rollout controls.

## Ask only when materially unresolved

- Which Cloudflare products, compatibility settings, account limits, routes, bindings, regions,
  and stores apply?
- What consistency, isolate lifecycle, retry, cache, migration, security, observability, and
  rollback behavior is required?

## Record in .grump

Record confirmed Cloudflare developer platform answers as project technology, architecture,
security, deployment, verification, and operational doctrine. Preserve source, scope,
confidence, and environment differences. Record a material unknown as unresolved instead of
inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Cloudflare developer platform
doctrine. Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey the Cloudflare developer platform when the products in use, Workers
compatibility date or flags, bindings, routes, regions, storage services, deployment
strategy, or account trust boundaries materially change. Also re-survey when evidence
conflicts with saved doctrine or the user requests a context refresh.
