# Go full-review guidance

## Operating conditions

Establish the project target: Go and toolchain targets, module mode, OS and
architecture matrix, CGO policy, build tags, race testing, proxy or
private-module setup, and deployment form. The changed boundary must define: Go
version semantics, module and toolchain rules, interfaces, nil behavior, error
contracts, goroutine lifetime, contexts, channels, memory model, races, CGO,
build tags, and cross-compilation.

## Failure patterns

- Require every goroutine to have an owner, stop condition, and observable
  failure path.
- Check context cancellation and deadlines across all blocking calls; reject
  storing request contexts in long-lived state.
- Find channel close races, blocked sends, nil channels, unsynchronized maps,
  and error loss. For modules using pre-1.22 Go language semantics, check range
  loop-variable capture. For Go 1.22 or later, inspect the exact loop form and
  any other captured or shared mutation instead of reporting the retired
  range-variable rule.
- Keep interfaces at consumer boundaries and reject speculative abstractions
  that hide concrete lifecycle behavior.
- Use `html/template` for HTML and keep attacker input out of template source.
  Treat URL, JavaScript, CSS, SQL, path, header, and command contexts with their
  own controls rather than assuming one escaping rule applies.
- Bound HTTP bodies and responses, parsing, collection growth, archives,
  decompression, image work, and goroutine fan-out. Close response bodies and
  preserve cancellation and timeouts through every outbound call.
- Constrain path joins and archive extraction against absolute paths, traversal,
  symlinks, and special files. With `exec.Command`, validate option-like values
  and the target program's argument semantics even when no shell is involved.
- Require race tests, leak checks, failure-path tests, and compatibility
  evidence for build tags and supported Go versions.

## Verification to run or specify in the plan

- Run changed concurrent paths with the race detector where supported; cancel
  contexts or let deadlines expire while sends, reads, or dependency calls are
  blocked. Verify goroutines stop, response bodies close, and errors reach
  their owner.
- Build the supported module, build-tag, OS, architecture, and CGO
  combinations. Run the relevant target artifacts and check native
  dependencies instead of treating successful cross-compilation as runtime
  evidence.

- Exercise hostile templates, URLs, command options, archive entries, symlinks,
  oversized responses, parser limits, cancellation, and partial reads where
  those boundaries exist.
