# Elixir survey contribution

## Applies when

Apply this contribution when the project contains, builds, deploys, operates, or
interoperates with Elixir or Erlang code, OTP applications, or runtime behavior.

## Inspect

- Establish the exact Elixir, Erlang/OTP, release-target, and dependency
  versions.

## Ask when unresolved

- Which Elixir, Erlang/OTP, release target, and dependency versions define
  runtime behavior?

- Which process owns state and work, and how do supervision, messages,
  timeouts, overload, and upgrades behave?

- Which runtime or deployment differences materially change future reviews:
  Erlang/OTP and Elixir versions, release packaging, node topology, schedulers,
  clustering, distribution, process supervision, and rolling upgrade model?

## Record

Map durable Elixir version and compatibility requirements to `Requirements` or
`Constraints`, runtime facts to `Runtime and deployment`, and material gaps to
`Unknowns`.
