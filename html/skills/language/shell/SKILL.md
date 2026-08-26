---
name: shell
description: Review POSIX shell and Bash engineering plans for quoting, expansion, pipelines, error propagation, portability, idempotency, filesystem safety, and automation risks. Use when a plan changes shell scripts, build steps, deployment scripts, or operational automation.
---

# Shell plan review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read the declared shell, shebangs, strict-mode settings, target operating
  systems, command dependencies, environment assumptions, and tests.
- Trace expansions, pipelines, temporary files, signals, cleanup traps,
  privilege boundaries, retries, and every destructive target.

## Establish the operating model

Establish the project target: Shells and versions, operating systems, required
utilities, POSIX requirement, locale and encoding, privilege context, scheduler
or CI host, and supported execution environments. The changed boundary must
define: Shell dialects, expansion, quoting, globbing, pipelines, exit status,
traps, signals, subprocesses, portability, temporary files, concurrency,
encoding, and destructive boundaries.

Define ownership, errors, cancellation, and concurrency for Shell dialects,
expansion, quoting, globbing, pipelines, exit status, traps. Verify version,
package, native, serialization, and artifact compatibility for signals,
subprocesses, portability, temporary files, concurrency, encoding, destructive
boundaries across every declared target and rollback path.

## Challenge the plan

### Recurring traps

Watch especially for word splitting and glob expansion, set -e providing false
confidence, pipeline failures being discarded, unsafe temporary-file patterns,
traps that do not cover every termination path, utility differences across
systems, and bytes interpreted under an assumed locale.

- Require quoting and delimiter-safe handling for paths, whitespace, newlines,
  globs, and untrusted values.
- Check pipeline and subshell error propagation instead of assuming one
  strict-mode setting makes the script safe.
- Require explicit validated targets, idempotency, atomic writes, cleanup traps,
  and recoverable behavior for mutations.
- Prevent secrets from command arguments, tracing, logs, environment dumps, and
  temporary files.
- Test with the actual shell and command implementations on every supported
  platform; Bash behavior is not automatically POSIX.

## Verify the claims

- Verify these behaviors through the declared Shell compiler and runtime
  targets: Shell dialects, expansion, quoting, globbing, pipelines, exit status,
  traps. Use the real compiler or interpreter and supported release modes rather
  than a development substitute.
- Exercise failure and edge behavior for: signals, subprocesses, portability,
  temporary files, concurrency, encoding, destructive boundaries. Exercise
  boundary values, encoding, cancellation, resource exhaustion, concurrency,
  dependency failure, and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which shell implementations, operating systems, utilities, locales, and
  privilege contexts must the script support?
- How do quoting, word splitting, globbing, pipelines, temporary files, signals,
  errors, and encoding cross boundaries?

## Calibrate findings

- Treat command injection, destructive expansion, credential leakage, or ignored
  partial failure as critical.
- Downgrade when inputs and targets are explicit and shell, quoting, failure,
  cleanup, and portability tests cover the script.

## Add to the verdict

State the shell and platform contract, quoting and encoding assumptions,
mutation safeguards, error propagation, and realistic execution evidence.
