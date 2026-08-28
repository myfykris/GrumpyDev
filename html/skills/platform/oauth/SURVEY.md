# OAuth OIDC and token authentication survey contribution

## Applicability

Apply this contribution when the project uses OAuth, OpenID Connect, delegated
authorization, social login, SSO, bearer tokens, JWTs, opaque access tokens, API
keys, personal access tokens, service tokens, signed tokens, or
proof-of-possession tokens. Do not apply it to cookie-only sessions unless they
are backed by or exchanged for one of these token types.

Skip it only when project evidence or an explicit user answer establishes that this
domain does not constrain a supported build, runtime, client, data, deployment, or
operating boundary.

This is project-level applicability, not a current-plan trigger. Once the package is
installed and not explicitly marked inapplicable, its `SKILL.md` participates in every
explicitly invoked GrumpyDev review.

## Inspect before asking

Inspect authentication and authorization middleware, token issuers and
consumers, API client configuration, secret sources, key sets, discovery or
introspection configuration, logs and redaction rules, deployment workflows,
incident runbooks, project documentation, and existing `.grump` doctrine before
treating a durable fact as unresolved.

## Durable project facts

- Token classes and purposes; issuer or creator, presenter, accepting service,
  subject, audience, tenant, permission or scope model, format, and lifetime.
- Transport, storage, logging and redaction, validation, clock-skew, replay,
  rotation, revocation, bootstrap, recovery, and compromise-response policy.
- For OAuth and OIDC: providers, protocol profiles, client types, grants,
  redirect origins, PKCE, state, nonce, consent, logout, discovery, refresh
  tokens, account linking, and session relationship.
- For JWTs and other signed tokens: allowed algorithms, issuer, audience, type,
  key source and binding, claim rules, and key rollover.
- For opaque tokens, API keys, personal access tokens, and service tokens:
  lookup or introspection authority, caching, scoping, ownership, rotation, and
  revocation behavior.
- For proof-of-possession tokens: key binding, request binding, nonce or replay
  policy, and key-loss recovery.
- Sources of truth and owners for relevant configuration, contracts, builds,
  deployment, upgrades, incidents, rollback, and recovery.
- Environment differences that materially change these facts.
- Deployment-profile facts: token issuers and accepting services, client or
  workload type, transport and TLS termination, credential storage, validation
  or introspection reachability, key authority, rotation, and revocation. When
  OAuth or OIDC applies, include authorization-server and resource-server
  boundaries and redirect origins.

## Ask only when materially unresolved

- Which token classes exist, what is each one for, who issues and accepts it,
  and what subject, audience, tenant, scope, format, transport, and lifetime
  apply?
- How does each token class handle validation, storage, logging, replay,
  rotation, revocation, key rollover, and compromise? When OAuth or OIDC is
  involved, which actors, client type, flow, redirects, PKCE, state, nonce, and
  account-linking rules apply?
- For the affected profiles, which of these facts materially differ across
  current, planned, and retiring operation, what support commitments apply, and
  what evidence establishes each fact: token issuers and accepting services,
  client or workload type, transport and TLS termination, credential storage,
  validation or introspection reachability, key authority, rotation and
  revocation, plus OAuth redirects when applicable? Ask only
  when evidence and the core profile confirmation do not resolve them.

## Record in .grump

Record token authentication and authorization answers in project technology, runtime, security,
deployment, verification, and operational doctrine. Preserve source and scope.
Record a material unknown as unresolved doctrine instead of guessing.

Record confirmed token-authentication deployment facts on the affected `DEP-###`
profile. Use a referenced `INF-###` entry for a material component shared by
several profiles. Preserve separate state, support, ownership, confidence,
source, and scope fields.

## Do not ask or record

Keep current host or process identifiers, transient resource readings, one
rollout value, private endpoints, actual credentials or token values, and
plan-only topology out of durable token-authentication doctrine. Do not
duplicate facts owned by another applicable contribution.

## Re-survey triggers

Re-survey when a token type, issuer, accepting audience, identity or tenant
model, scope policy, validation rule, key authority, storage or transport
boundary, OAuth flow, rotation or revocation process, or compromise response
materially changes. Also re-survey when evidence conflicts with saved doctrine
or the user requests a context refresh.
