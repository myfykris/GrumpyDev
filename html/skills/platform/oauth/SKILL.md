---
name: gd-oauth
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review token-based authentication and authorization engineering work for issuance, transport, audience, scope, validation, storage, rotation, revocation, replay, and identity-linking risks."
---

# OAuth, OIDC, and token authentication GrumpyDev review

## Quick checks

- Identify every token or credential type, who issues it, who presents it, who
  accepts it, its subject, audience, permissions, transport, storage,
  validation, lifetime, rotation, revocation, and compromise path.

- When OAuth or OIDC applies, identify the authorization server, client type,
  flow, redirects, scopes, PKCE, state, nonce, SDK, callback handling, and the
  authoritative local account-linking key. Do not force OAuth flow concepts
  onto API keys, personal access tokens, or service tokens.

Watch especially for bearer credentials in URLs, logs, source, browser storage,
or crash reports; missing audience, issuer, type, scope, signature, algorithm,
expiry, replay, or tenant validation; API keys treated as user identity; ID
tokens used as general API credentials; broad redirects; refresh-token reuse;
opaque-token introspection cached past revocation; and account linking based on
mutable or unverified claims.

- Inspect account takeover, privilege escalation, cross-tenant acceptance,
  redirect abuse, reusable token disclosure, or ambiguous account linking.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material OAuth, OIDC, and token authentication effect or
uncertainty.

## Verdict context

State each token class and purpose, issuer and audience, validation and replay
controls, storage and transport boundary, lifecycle and compromise response,
and, when applicable, OAuth flow and account-linking behavior. Identify the
current provider documents or tests needed to support vendor-specific claims.
