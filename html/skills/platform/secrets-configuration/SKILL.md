---
name: secrets-configuration
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review secrets and configuration engineering work for ownership, validation, least exposure, rotation, versioning, environment parity, failure behavior, and auditability."
---

# Secrets and configuration GrumpyDev review

Apply this guidance alongside the core GrumpyDev review, the
`application-security` skill, and the applicable installed deployment-platform
specialist.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

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

Lean mode is insufficient when this material severity condition may apply:

- Treat secret disclosure, silent unsafe defaults, or a rotation path that
  causes broad outage as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Secrets and configuration evidence, operating model,
failure, verification, question, and calibration guidance. Never load
`SURVEY.md` during an ordinary review.

## Add to the verdict

State configuration schema and precedence, secret exposure and audience
boundary, identity model, rotation and revocation behavior, fail-closed mode,
and audit evidence.
