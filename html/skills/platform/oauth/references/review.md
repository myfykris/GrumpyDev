# OAuth, OIDC, and token authentication standard review

## Inspect additional evidence

- Trace creation or issuance, delivery, presentation, validation, refresh or
  replacement, revocation, expiry, failure, compromise, and recovery for every
  token class. Trace OAuth initiation, callback, exchange, consent, and logout
  paths when they apply.

## Establish the operating model

For each token class, establish its purpose, issuer or creator, subject,
presenter, accepting audience, tenant boundary, permissions, format, transport,
storage, validation authority, lifetime, rotation, revocation, replay control,
and compromise owner. Never assume that all token classes share one trust
model.

For OAuth and OIDC, also establish providers, protocol profiles, client types,
flows, redirects, PKCE, state, nonce, discovery, consent, logout, refresh-token
behavior, session linkage, and account-linking authority. For non-OAuth tokens,
apply only the lifecycle and trust concepts that actually fit their design.

## Challenge the reviewed work

### Recurring traps

- Treat any bearer token as usable by whoever possesses it. Require TLS, keep it
  out of URLs and logs, limit audience and permissions, prefer short lifetimes,
  and define a concrete response to disclosure.
- Require authorization code flow and PKCE where appropriate. Reject implicit
  trust in browser-supplied identity or unsigned token contents.
- Bind each authorization response to the initiating user agent and operation.
  Validate exact redirect URIs, state, issuer, audience, nonce when applicable,
  signature, expiry, and authorized algorithms.
- Treat access and refresh tokens as credentials. Minimize scopes; define
  encrypted storage, log redaction, rotation, revocation, concurrency, and
  compromise response.
- Prevent account takeover through ambiguous email matching, mutable subject
  identifiers, provider mixing, or unverified claims.
- Handle denied consent, expired codes, reused callbacks, refresh-token
  rotation, revoked grants, clock skew, provider outage, and partial
  persistence.
- Separate client secrets from public clients and verify backend-for-frontend or
  browser token exposure assumptions against the actual architecture.
- For JWTs, allowlist algorithms and validate signature, issuer, audience,
  token type, time claims, and application-required claims together. Prevent
  one token kind from being accepted in another token kind's validation path,
  and bind selected keys to the expected issuer and algorithm.
- For opaque tokens, define introspection or lookup behavior, cache lifetime,
  outage behavior, revocation delay, and the local authorization decision.
- For API keys, personal access tokens, and service tokens, require attributable
  ownership, narrow permissions, non-source storage, rotation without a flag
  day, revocation, inventory, and detection of unused or leaked credentials.
- For proof-of-possession tokens, verify key and request binding, replay cache or
  nonce behavior, clock handling, and lost-key recovery instead of assuming the
  token format alone prevents replay.

## Verify the claims

- Test every accepting service with valid tokens and with wrong issuer,
  audience, tenant, type, algorithm, signature, scope, expiry, and replay state.
- Exercise key rollover, token rotation, concurrent refresh, revocation,
  introspection or issuer outage, clock skew, leaked-credential response, and
  old and new validators coexisting during deployment.
- For OAuth and OIDC, test exact redirect matching, state, PKCE, nonce, denied
  consent, reused callbacks, provider errors, logout, and account linking using
  the effective provider and client configuration.
- Inspect logs, URLs, telemetry, client storage, caches, crash reports, and
  generated artifacts for credential disclosure.

## Ask when evidence is missing

- Which token classes exist, what is each one for, who issues and accepts it,
  and what subject, audience, tenant, permission, transport, and lifetime apply?
- How does each token class handle validation, storage, logging, replay,
  rotation, revocation, key rollover, and compromise? When OAuth or OIDC is
  involved, which actors, flow, redirects, PKCE, state, nonce, and
  account-linking rules apply?

## Calibrate findings

- Downgrade when each token has one clear purpose and audience, validation and
  lifecycle controls are enforced at every accepting boundary, compromise and
  rotation are rehearsed, and applicable OAuth or provider behavior is tested.
