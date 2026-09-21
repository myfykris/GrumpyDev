---
name: gd-secrets-configuration
description: "Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically. Review secrets and configuration engineering work for ownership, validation, least exposure, rotation, versioning, environment parity, failure behavior, and auditability."
---

# Secrets and configuration GrumpyDev review

## Quick checks

- Read configuration schemas, defaults, sources, precedence, secret stores,
  identities, rotation, reload behavior, audit logs, and local-development
  paths.

- Trace a value from authoring through storage, delivery, parsing, logging, use,
  rotation, revocation, and process shutdown.

Watch especially for secrets committed or logged, environment variables
inherited by child processes, reloads applying half a configuration, development
defaults accepted in production, rotation without old-and-new overlap,
configuration sources disagreeing, redaction that runs after serialization, and
credentials copied into browser bundles, source maps, model prompts, URLs, or
generated build artifacts.

- Assess secret disclosure, silent unsafe defaults, or a rotation path that
  causes broad outage under the core severity rules.

## References

In a full review, read [review.md](references/review.md) after a quick check
establishes a material effect or uncertainty covered by the Secrets and
configuration specialist.

## Verdict context

State configuration schema and precedence, secret exposure and audience
boundary, identity model, rotation and revocation behavior, fail-closed mode,
and audit evidence.
