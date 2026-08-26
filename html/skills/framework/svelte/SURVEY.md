# Svelte and SvelteKit survey contribution

## Applicability

Apply this contribution when a plan creates or changes svelte applications. Skip it when Svelte
and SvelteKit does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

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

Re-survey Svelte and SvelteKit when its version, target platform, rendering or execution model,
trust boundary, deployment adapter, persistent state, update process, or recovery policy
materially changes, when evidence conflicts with saved doctrine, or when the user requests a
context refresh.
