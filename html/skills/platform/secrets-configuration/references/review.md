# Secrets and configuration full-review guidance

## Operating conditions

Establish the project target: Configuration systems, secret stores, environment
hierarchy, identity and access, rotation cadence, reload behavior, audit
requirements, and ownership. The changed boundary must define: Source and
precedence, validation, secret lifecycle, rotation, reload, redaction, least
privilege, environment drift, emergency access, and failure modes.

## Failure patterns

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

## Verification to run or specify in the plan

- Render and inspect effective configuration for every supported environment,
  including precedence, types, encoding, required values and workload access.
- Exercise startup and reload with missing, malformed, stale, revoked,
  partially updated and unavailable values, proving fail-closed or deliberate
  last-known-safe behavior and useful diagnostics.
- Rotate and revoke credentials with old and new processes active, then test
  cache invalidation, emergency access, dependent-service failure and recovery.
- Scan source history, build context, images, packages, client bundles, source
  maps, logs, traces, crash reports, prompts, and backups for accidental
  exposure, then rehearse revocation and replacement from detection to recovery.
