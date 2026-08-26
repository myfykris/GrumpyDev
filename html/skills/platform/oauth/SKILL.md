---
name: oauth
description: Review OAuth 2.0 and OpenID Connect integration plans for flow selection, redirect, PKCE, state, nonce, token, scope, storage, rotation, revocation, and account-linking risks. Use when a plan adds or changes delegated authorization, social login, SSO, OAuth clients, or token-based vendor access.
---

# OAuth and OIDC plan review

Apply this guidance alongside the core GrumpyDev review. Treat provider behavior
and current security guidance as time-sensitive; verify primary documentation
when the plan depends on vendor-specific claims.

## Inspect evidence

- Identify the exact authorization server, client type, grant/flow, redirect
  URIs, scopes, token types, SDK, callback handling, and storage locations.
- Distinguish OAuth authorization from OIDC authentication and identify the
  authoritative local account-linking key.
- Trace initiation, callback, token exchange, refresh, revocation, logout,
  expiry, failure, and reconnect paths.

## Establish the operating model

Establish the project target: Providers, protocol versions and profiles, client
types, grants, redirect origins, token formats, scopes, session relationship,
key rotation, and tenant model. The changed boundary must define: OAuth and OIDC
roles, flows, redirects, PKCE, state and nonce, token validation, rotation,
scopes, consent, logout, discovery, key rollover, and threats.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for OAuth and OIDC roles, flows, redirects, PKCE, state
and nonce, token validation, rotation. Prove scopes, consent, logout, discovery,
key rollover, threats through rotation, overload, partial rollout, drain, forced
stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for ID tokens used as general API credentials, missing state,
nonce, or PKCE validation, broad redirect matching, tokens exposed to browser
storage or logs, refresh-token reuse, issuer and audience confusion, and account
linking based on an unstable identifier.

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

## Verify the claims

- Verify these behaviors through the effective OAuth and OIDC configuration and
  runtime topology: OAuth and OIDC roles, flows, redirects, PKCE, state and
  nonce, token validation, rotation. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: scopes, consent, logout, discovery,
  key rollover, threats. Exercise startup, readiness, normal load, overload,
  dependency loss, rotation, graceful drain, forced stop, failover, and recovery
  where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- Which OAuth or OpenID Connect actors, client type, flow, scopes, redirect
  rules, and provider behavior apply?
- How are state, nonce, PKCE, tokens, revocation, rotation, and account linking
  protected?

## Calibrate findings

- Treat account takeover, redirect abuse, token disclosure, or ambiguous account
  linking as critical.
- Downgrade when the selected flow matches the client and provider and protocol
  controls are enforced and tested.

## Add to the verdict

State the selected protocol flow, trust and account-linking boundary,
CSRF/replay controls, token lifecycle, scope rationale, and the current provider
documents or tests needed to support vendor-specific behavior.
