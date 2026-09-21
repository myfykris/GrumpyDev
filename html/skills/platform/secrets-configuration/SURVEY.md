# Secrets and configuration survey contribution

## Applies when

Apply this contribution when the project uses runtime configuration, credentials, keys,
certificates, secrets, or feature controls.

## Inspect

- Read configuration schemas, defaults, sources, precedence, secret stores,
  identities, rotation, reload behavior, audit logs, and local-development
  paths.

## Ask when unresolved

- Who owns each configuration value or secret, where is it sourced, and how is
  it validated before use?

- How do rotation, revocation, version skew, startup failure, and accidental
  exposure behave?

- Which runtime or deployment differences materially change future reviews:
  Secret and configuration sources, injection path, process scope, identity,
  rotation, reload, environment differences, redaction, fallback behavior, and
  owner?

## Record

Map durable Secrets and configuration requirements and constraints to the
matching doctrine sections, runtime facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
