---
name: powershell
description: Review PowerShell engineering plans for object-pipeline behavior, quoting, remoting, credentials, error semantics, platform differences, idempotency, and automation safety. Use when a plan changes PowerShell scripts, modules, deployment automation, or administrative workflows.
---

# PowerShell plan review

Apply this guidance alongside the core GrumpyDev review.

## Inspect evidence

- Read module manifests, required PowerShell editions and versions, parameter
  declarations, remoting setup, execution policy assumptions, and tests.
- Trace object and string conversion, native command invocation, credentials,
  temporary files, retries, partial changes, and cleanup.

## Establish the operating model

Establish the project target: PowerShell editions and versions, operating
systems, remoting transport, required modules, execution policy, native tools,
host process, encoding, and automation environment. The changed boundary must
define: Edition and version differences, object pipelines, streams, errors,
remoting, serialization, modules, scopes, providers, quoting, native-process
boundaries, encoding, and execution policy.

Define ownership, errors, cancellation, and concurrency for Edition and version
differences, object pipelines, streams, errors, remoting, serialization,
modules. Verify version, package, native, serialization, and artifact
compatibility for scopes, providers, quoting, native-process boundaries,
encoding, execution policy across every declared target and rollback path.

## Challenge the plan

### Recurring traps

Watch especially for formatted text mistaken for pipeline objects,
non-terminating errors treated as success, quoting and interpolation changes
across local and remote execution, scalar and array unrolling, remoting
serialization that strips behavior, and scope or preference variables inherited
implicitly.

- Distinguish non-terminating errors from exceptions and require explicit
  failure behavior instead of relying on ambient preferences.
- Check quoting and encoding at PowerShell, native-process, remote-session,
  JSON, CSV, and filesystem boundaries.
- Require idempotency, dry-run support where practical, exact targets, and
  recovery for scripts that mutate systems.
- Prevent secrets from entering command lines, transcripts, verbose output,
  history, or serialized objects.
- Test on every supported operating system and PowerShell edition because
  command, path, and encoding behavior differs.

## Verify the claims

- Verify these behaviors through the declared PowerShell compiler and runtime
  targets: Edition and version differences, object pipelines, streams, errors,
  remoting, serialization, modules. Use the real compiler or interpreter and
  supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: scopes, providers, quoting,
  native-process boundaries, encoding, execution policy. Exercise boundary
  values, encoding, cancellation, resource exhaustion, concurrency, dependency
  failure, and termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.

## Ask when evidence is missing

- Which PowerShell edition and version, operating systems, remoting mode,
  execution policy, and module versions apply?
- How do object and text pipelines, quoting, native processes, credentials,
  errors, and encoding cross boundaries?

## Calibrate findings

- Treat command injection, credential exposure, destructive wildcard targeting,
  or ignored terminating failure as critical.
- Downgrade when targets are explicit and quoting, encoding, error, remoting,
  and cross-platform tests cover the script.

## Add to the verdict

State supported hosts, error policy, mutation and rollback behavior, credential
handling, encoding assumptions, and cross-platform evidence.
