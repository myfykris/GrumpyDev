# Vercel survey contribution

## Applicability

Apply this contribution when an application builds or runs on Vercel. Skip it when
Vercel does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, infrastructure, build
and deployment workflows, project documentation, representative code, tests, and existing .grump
doctrine for Vercel. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Vercel projects and teams, framework and build command, output
  mode, function runtimes and regions, Fluid compute behavior, concurrency and limits, cache and
  revalidation ownership, environment variables, previews, domains, protection, observability,
  and rollout.
- Review doctrine: A function instance may serve concurrent requests and reuse global state,
  but it is not a durable singleton. Region, runtime, cache, and production build behavior must
  match data location and framework assumptions.
- Deployment-profile facts: project and team, framework and build output, function
  runtimes and regions, Fluid compute and limits, route configuration, cache policy, environment
  scopes, domains, preview protection, observability, and rollback controls.

## Ask only when materially unresolved

- Which Vercel projects, framework, runtimes, regions, Fluid settings, limits, build output,
  and data locations apply?
- How are concurrency, global reuse, connections, caches, environments, previews, domains,
  rollout, and rollback handled?

## Record in .grump

Record confirmed Vercel answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Vercel doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Vercel when the framework, build output, function runtime, region placement,
environment-variable scope, domain routing, cache behavior, preview policy, or rollout
strategy materially changes. Also re-survey when evidence conflicts with saved doctrine
or the user requests a context refresh.
