# Auth.js survey contribution

## Applicability

Apply this contribution when the project uses or materially depends on Auth.js.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

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

Re-survey Auth.js when its version, provider set, session strategy, adapter, cookie
policy, callback contract, host trust configuration, or deployment runtime materially
changes. Also re-survey when evidence conflicts with saved doctrine or the user
requests a context refresh.
