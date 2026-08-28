# Shell standard review

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

## Challenge the reviewed work

### Recurring traps

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

- Downgrade when inputs and targets are explicit and shell, quoting, failure,
  cleanup, and portability tests cover the script.
