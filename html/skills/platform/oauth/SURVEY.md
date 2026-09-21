# OAuth, OIDC, and token authentication survey contribution

## Applies when

Apply this contribution when the project uses OAuth, OpenID Connect, delegated
authorization, social login, SSO, bearer tokens, JWTs, opaque access tokens, API
keys, personal access tokens, service tokens, signed tokens, or
proof-of-possession tokens. Do not apply it to cookie-only sessions unless they
are backed by or exchanged for one of these token types.

## Inspect

- Identify every token or credential type, who issues it, who presents it, who
  accepts it, its subject, audience, permissions, transport, storage,
  validation, lifetime, rotation, revocation, and compromise path.

## Ask when unresolved

- Which token classes exist, what is each one for, who issues and accepts it,
  and what subject, audience, tenant, scope, format, transport, and lifetime
  apply?

- How does each token class handle validation, storage, logging, replay,
  rotation, revocation, key rollover, and compromise? When OAuth or OIDC is
  involved, which actors, client type, flow, redirects, PKCE, state, nonce, and
  account-linking rules apply?

- Which runtime or deployment differences materially change future reviews:
  token issuers and accepting services, client or workload type, transport and
  TLS termination, credential storage, validation or introspection
  reachability, key authority, rotation and revocation, plus OAuth redirects
  when applicable?

## Record

Map durable OAuth, OIDC, and token authentication requirements and constraints
to the matching doctrine sections, runtime facts to `Runtime and deployment`,
and material gaps to `Unknowns`.
