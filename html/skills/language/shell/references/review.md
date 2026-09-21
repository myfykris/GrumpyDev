# Shell full-review guidance

## Operating conditions

Establish the project target: Shells and versions, operating systems, required
utilities, POSIX requirement, locale and encoding, privilege context, scheduler
or CI host, and supported execution environments. The changed boundary must
define: Shell dialects, expansion, quoting, globbing, pipelines, exit status,
traps, signals, subprocesses, portability, temporary files, concurrency,
encoding, and destructive boundaries.

## Failure patterns

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

## Verification to run or specify in the plan

- Run scripts with the declared shell and utility implementations, including
  the scheduler or CI environment when relevant. Check empty arguments,
  whitespace, newlines, leading hyphens, glob characters, and non-ASCII paths.
- Fail commands in pipelines, substitutions, and subshells; interrupt work
  with the signals it must handle. Verify exit status, trap behavior,
  child-process cleanup, and temporary-file removal.
- Use disposable targets to test destructive path selection, symlink handling,
  interrupted writes, and repeat execution. Confirm that failures cannot
  broaden the target or leave a partial result presented as success.
