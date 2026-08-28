# Go standard review

## Establish the operating model

Establish the project target: Go and toolchain targets, module mode, OS and
architecture matrix, CGO policy, build tags, race testing, proxy or
private-module setup, and deployment form. The changed boundary must define: Go
version semantics, module and toolchain rules, interfaces, nil behavior, error
contracts, goroutine lifetime, contexts, channels, memory model, races, CGO,
build tags, and cross-compilation.

Define ownership, errors, cancellation, and concurrency for Go version
semantics, module and toolchain rules, interfaces, nil behavior, error
contracts, goroutine lifetime, contexts. Verify version, package, native,
serialization, and artifact compatibility for channels, memory model, races,
CGO, build tags, cross-compilation across every declared target and rollback
path.

## Challenge the reviewed work

### Recurring traps

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

## Verify the claims

- Verify these behaviors through the declared Go compiler and runtime targets:
  Go version semantics, module and toolchain rules, interfaces, nil behavior,
  error contracts, goroutine lifetime, contexts. Use the real compiler or
  interpreter and supported release modes rather than a development substitute.
- Exercise failure and edge behavior for: channels, memory model, races, CGO,
  build tags, cross-compilation. Exercise boundary values, encoding,
  cancellation, resource exhaustion, concurrency, dependency failure, and
  termination where they can change behavior.
- Inspect generated code, packages, native boundaries, and final artifacts for
  target and compatibility claims.
- Exercise hostile templates, URLs, command options, archive entries, symlinks,
  oversized responses, parser limits, cancellation, and partial reads where
  those boundaries exist.

## Ask when evidence is missing

- Which Go language version in go.mod, toolchain version, target, build tags,
  and module graph apply?
- Who owns each goroutine, channel, context, timer, and shared value, including
  the exact loop form for captures?

## Calibrate findings

- Downgrade when ownership is bounded and race, leak, cancellation, and
  supported-version tests cover the exact semantics.
