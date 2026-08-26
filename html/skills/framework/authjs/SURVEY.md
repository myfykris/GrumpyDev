# Auth.js survey contribution

## Applicability

Apply this contribution when a plan authenticates users with auth.js or nextauth.js. Skip it
when Auth.js does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

## Inspect before asking

Inspect package and lock files, effective configuration, generated output, build and deployment
workflows, project documentation, representative code, tests, and existing .grump doctrine for
Auth.js. Resolve facts from current evidence before asking.

## Durable project facts

- Target and operating model: Auth.js version and framework integration, providers, deployment
  origins, session strategy, adapter and schema, cookie policy, account-linking policy, callback
  ownership, and authorization boundary.
- Review doctrine: Authentication proves identity and creates a session; it does not replace
  resource authorization. The plan must separate provider tokens, Auth.js sessions, application
  permissions, and tenant membership.
- Conditional deployment boundary: framework adapter, public and internal origins,
  proxy headers, cookie domain and security, session store, provider callback URLs, secret
  sources, database connectivity, and runtime limits.

## Ask only when materially unresolved

- Which Auth.js version, framework adapter, providers, session strategy, database adapter, and
  deployment origins apply?
- How are accounts linked, provider credentials refreshed, sessions revoked, cookies scoped,
  and resources authorized?

## Record in .grump

Record confirmed Auth.js answers as project technology, architecture, security, deployment,
verification, and operational doctrine. Preserve source, scope, confidence, and environment
differences. Record a material unknown as unresolved instead of inventing a default.

Map execution-specific facts to the affected `DEP-###` profile. Reference a shared `INF-###`
component rather than copying its common contract. Keep separate ownership, support, confidence,
source, and scope fields.

## Do not ask or record

Do not record transient host identifiers, current resource readings, temporary rollout values,
credentials, private endpoints, or plan-only choices as durable Auth.js doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey Auth.js when its version, target platform, rendering or execution model, trust
boundary, deployment adapter, persistent state, update process, or recovery policy materially
changes, when evidence conflicts with saved doctrine, or when the user requests a context
refresh.
