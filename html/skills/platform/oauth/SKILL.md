---
name: oauth
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review token-based authentication and authorization plans and other engineering artifacts for issuance, transport, audience, scope, validation, storage, rotation, revocation, replay, and identity-linking risks. Project applicability: the project uses OAuth, OpenID Connect, SSO, bearer tokens, JWTs, opaque access tokens, API keys, personal access tokens, service tokens, signed tokens, or proof-of-possession tokens. Cookie-only sessions do not make this specialist applicable unless they are backed by or exchanged for such tokens."
---

# OAuth, OIDC, and token authentication GrumpyDev review

Treat provider behavior and current security guidance as time-sensitive; verify
primary documentation when the reviewed work directly or indirectly depends on
vendor-specific claims.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

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

Lean mode is insufficient when this material severity condition may apply:

- Treat account takeover, privilege escalation, cross-tenant acceptance,
  redirect abuse, reusable token disclosure, or ambiguous account linking as
  critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete token-authentication evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State each token class and purpose, issuer and audience, validation and replay
controls, storage and transport boundary, lifecycle and compromise response,
and, when applicable, OAuth flow and account-linking behavior. Identify the
current provider documents or tests needed to support vendor-specific claims.
