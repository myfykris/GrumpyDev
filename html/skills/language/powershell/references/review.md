# PowerShell full-review guidance

## Operating conditions

Establish the project target: PowerShell editions and versions, operating
systems, remoting transport, required modules, execution policy, native tools,
host process, encoding, and automation environment. The changed boundary must
define: Edition and version differences, object pipelines, streams, errors,
remoting, serialization, modules, scopes, providers, quoting, native-process
boundaries, encoding, and execution policy.

## Failure patterns

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

## Verification to run or specify in the plan

- Run scripts under the supported PowerShell editions, operating systems, and
  automation host. Trigger a non-terminating cmdlet error, a terminating
  exception, and a failing native command; verify the intended exit status and
  cleanup.
- Round-trip paths and non-ASCII data through native arguments, remoting, JSON
  or CSV, and files where used. Check that object properties survive
  serialization and formatting output is not mistaken for data.
- For mutations, use disposable targets to check exact path selection, repeat
  execution, interruption, and dry-run behavior when offered. Verify
  transcripts and error streams do not expose secrets.
