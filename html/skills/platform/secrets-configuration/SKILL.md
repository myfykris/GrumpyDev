---
name: secrets-configuration
description: Review secrets and configuration plans for ownership, validation, least exposure, rotation, versioning, environment parity, failure behavior, and auditability. Use when a plan changes runtime configuration, credentials, keys, certificates, or feature controls.
---

# Secrets and configuration plan review

Apply this guidance alongside the core GrumpyDev review, the
`application-security` skill, and the applicable installed deployment-platform
specialist.

## Inspect evidence

- Read configuration schemas, defaults, sources, precedence, secret stores,
  identities, rotation, reload behavior, audit logs, and local-development
  paths.
- Trace a value from authoring through storage, delivery, parsing, logging, use,
  rotation, revocation, and process shutdown.

## Establish the operating model

Establish the project target: Configuration systems, secret stores, environment
hierarchy, identity and access, rotation cadence, reload behavior, audit
requirements, and ownership. The changed boundary must define: Source and
precedence, validation, secret lifecycle, rotation, reload, redaction, least
privilege, environment drift, emergency access, and failure modes.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Source and precedence, validation, secret lifecycle,
rotation, reload. Prove redaction, least privilege, environment drift, emergency
access, failure modes through rotation, overload, partial rollout, drain, forced
stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for secrets committed or logged, environment variables
inherited by child processes, reloads applying half a configuration, development
defaults accepted in production, rotation without old-and-new overlap,
configuration sources disagreeing, redaction that runs after serialization,
and credentials copied into browser bundles, source maps, model prompts, URLs,
or generated build artifacts.

- Specify type, encoding, units, allowed values, and required presence; fail
  startup clearly on invalid critical configuration.
- Keep secrets out of source, images, environment dumps, command lines,
  telemetry, crash reports, URLs, model context, client-visible payloads,
  browser storage, source maps, and generated artifacts.
- Grant workload identity access to only the values and versions it needs, with
  an auditable owner for each secret.
- Prefer short-lived workload or user identity over long-lived shared values.
  Bind credentials to the expected audience, environment, workload, and action,
  and prevent forwarding one service's token to an unrelated downstream API.
- Define rotation overlap, cache invalidation, certificate renewal,
  revoked-value behavior, and recovery when the secret service is unavailable.
- Treat feature flags as temporary production code with ownership, safe
  defaults, targeting tests, expiry, and removal plans.
- Make unavailable, malformed, stale, or partially reloaded security
  configuration fail closed. Validate the complete configuration before making
  it active, and keep the last known safe version only when that behavior is
  deliberate and observable.

## Verify the claims

- Verify these behaviors through the effective Secrets and configuration
  configuration and runtime topology: Source and precedence, validation, secret
  lifecycle, rotation, reload. Use effective rendered configuration and
  deployable artifacts in a representative identity, topology, capacity, and
  policy boundary.
- Exercise failure and edge behavior for: redaction, least privilege,
  environment drift, emergency access, failure modes. Exercise startup,
  readiness, normal load, overload, dependency loss, rotation, graceful drain,
  forced stop, failover, and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.
- Scan source history, build context, images, packages, client bundles, source
  maps, logs, traces, crash reports, prompts, and backups for accidental
  exposure, then rehearse revocation and replacement from detection to recovery.

## Ask when evidence is missing

- Who owns each configuration value or secret, where is it sourced, and how is
  it validated before use?
- How do rotation, revocation, version skew, startup failure, and accidental
  exposure behave?

## Calibrate findings

- Treat secret disclosure, silent unsafe defaults, or a rotation path that
  causes broad outage as critical.
- Downgrade when values are non-sensitive and bounded or secret access,
  rotation, validation, and failure tests are complete.

## Add to the verdict

State configuration schema and precedence, secret exposure and audience
boundary, identity model, rotation and revocation behavior, fail-closed mode,
and audit evidence.
