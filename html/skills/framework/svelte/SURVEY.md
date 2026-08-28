# Svelte and SvelteKit survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Svelte and
SvelteKit.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, build and deployment
workflows, project documentation, representative code, tests, and existing .grump doctrine for
Svelte and SvelteKit. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Svelte and SvelteKit versions, reactivity mode, adapter and host,
  route rendering and prerender policy, load and action conventions, session and authorization
  boundary, environment sources, service worker, and browser targets.
- Review doctrine: The plan must distinguish universal load code from server-only code and
  browser code. Form actions and server routes need per-operation authorization even when page
  loading is protected.
- Conditional deployment boundary: Svelte and SvelteKit versions, adapter and host
  runtime, route rendering, prerender entries, proxy and cookie settings, environment sources,
  service worker, asset paths, and production command.

## Ask only when materially unresolved

- Which Svelte, SvelteKit, reactivity mode, adapter, host, route rendering, and service-worker
  choices apply?
- Where do load data, actions, sessions, authorization, environment values, invalidation, and
  errors live?

## Record in .grump

Record confirmed Svelte and SvelteKit answers as project technology, architecture, security,
deployment, verification, and operational doctrine. Preserve source, scope, confidence, and
environment differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Svelte and SvelteKit doctrine.
Do not duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Svelte or SvelteKit when either version, rendering mode, deployment adapter,
routing or load contract, state model, server hook, authentication boundary, or form
action strategy materially changes. Also re-survey when evidence conflicts with saved
doctrine or the user requests a context refresh.
