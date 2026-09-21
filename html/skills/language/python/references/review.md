# Python full-review guidance

## Operating conditions

Establish the project target: Interpreter implementations and versions,
packaging and lock tooling, OS and architecture, worker model, async framework,
native dependencies, locale and encoding, and deployment form. The changed
boundary must define: Interpreter behavior, typing limits, packaging, import and
environment rules, async, threads and processes, GIL implications, object
lifetime, serialization, native extensions, signals, and deployment.

## Failure patterns

- Distinguish static type promises from runtime validation at untrusted
  boundaries. Flag broad `Any`, unchecked casts, and catch-all exceptions that
  erase invariants.

## Verification to run or specify in the plan

- Install the built package in a clean environment using the supported
  interpreters and native dependencies. Exercise imports and package resources
  without relying on the source checkout or development path.
- Cancel affected async tasks and interrupt worker processes during I/O and
  shutdown. Check exceptions reach their owner and files, connections, child
  processes, and pending work are cleaned up according to the runtime in use.

- Exercise malicious serialized objects, YAML tags, archive entries, symlink
  swaps, command options, expensive regular expressions, deep input, and parser
  limits where those boundaries exist.
