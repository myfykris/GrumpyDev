# PowerShell standard review

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

## Challenge the reviewed work

### Recurring traps

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

- Downgrade when targets are explicit and quoting, encoding, error, remoting,
  and cross-platform tests cover the script.
