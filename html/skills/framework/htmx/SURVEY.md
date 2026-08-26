# htmx survey contribution

## Applicability

Apply this contribution when a plan adds or changes htmx interactions. Skip it when htmx does
not constrain a supported build, runtime, client, data, deployment, or operating boundary.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, build and deployment
workflows, project documentation, representative code, tests, and existing .grump doctrine for
htmx. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: htmx version, server and template stack, extensions, request and
  response conventions, fragment detection, history policy, cache variation, CSRF transport,
  CSP, and accessibility behavior.
- Review doctrine: The URL and server-rendered HTML remain authoritative. Any URL placed in
  history must return a complete navigable page outside an htmx request.
- Conditional deployment boundary: server framework, template engine, htmx and
  extension versions, proxy cache variation, CSP and CSRF settings, origin behavior, static
  asset source, and direct-navigation routing.

## Ask only when materially unresolved

- Which htmx version, extensions, server templates, fragment convention, swap targets, and
  cache behavior apply?
- How are request races, direct navigation, history storage, CSRF, injected HTML, focus, and
  errors handled?

## Record in .grump

Record confirmed htmx answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable htmx doctrine. Do not duplicate
facts owned by another applicable contribution.

## Re-survey triggers

Re-survey htmx when its version, target platform, rendering or execution model, trust boundary,
deployment adapter, persistent state, update process, or recovery policy materially changes,
when evidence conflicts with saved doctrine, or when the user requests a context refresh.
