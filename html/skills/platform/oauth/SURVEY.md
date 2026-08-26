# OAuth and OIDC survey contribution

## Applicability

Apply this contribution when a plan adds or changes delegated authorization,
social login, SSO, OAuth clients, or token-based vendor access. Skip it when
OAuth and OIDC does not constrain a supported build, runtime, client, data,
deployment, or operating boundary.

## Inspect before asking

For OAuth and OIDC, inspect version declarations, effective configuration
sources, rendered artifacts, infrastructure and identity policy, build and
deployment workflows, service objectives, operational runbooks, and project
documentation. Read existing `.grump` doctrine and project documentation before
treating a durable fact as unresolved.

## Durable project facts

- Target and operating model: Providers, protocol versions and profiles, client
  types, grants, redirect origins, token formats, scopes, session relationship,
  key rotation, and tenant model.
- Review doctrine for: OAuth and OIDC roles, flows, redirects, PKCE, state and
  nonce, token validation, rotation, scopes, consent, logout, discovery, key
  rollover, and threats.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: Authorization server and resource-server
  boundaries, browser or native client type, redirect origins, proxy and TLS
  termination, token storage, issuer reachability, and key rotation.

## Ask only when materially unresolved

- Which OAuth or OpenID Connect actors, client type, flow, scopes, redirect
  rules, and provider behavior apply?
- How are state, nonce, PKCE, tokens, revocation, rotation, and account linking
  protected?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: Authorization server and resource-server
  boundaries, browser or native client type, redirect origins, proxy and TLS
  termination, token storage, issuer reachability, and key rotation? Ask only
  when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record OAuth and OIDC answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed OAuth and OIDC deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, and plan-only topology out of durable OAuth
and OIDC doctrine. Do not duplicate facts owned by another applicable
contribution.

## Re-survey triggers

Re-survey OAuth and OIDC when product or protocol version, topology,
environment, identity, trust boundary, resource model, configuration authority,
deployment process, or recovery objectives materially change, when evidence
conflicts with saved doctrine, or when the user requests a context refresh.
