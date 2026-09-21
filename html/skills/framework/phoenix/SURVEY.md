# Phoenix survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Phoenix.

## Inspect

- Read endpoint and router pipelines, plugs, contexts, Ecto schemas and
  migrations, LiveViews or channels, PubSub, supervision, releases, and tests.

## Ask when unresolved

- Which Elixir, Erlang/OTP, Phoenix, LiveView, and deployment versions apply?

- How do process ownership, supervision, socket state, PubSub, transactions,
  reconnect, and release rollout interact?

- Which runtime or deployment differences materially change future reviews:
  Elixir and OTP release, node topology, endpoint and proxy, PubSub adapter,
  clustering, sessions, Ecto pool, workers, rollout, and distributed shutdown?

## Record

Map durable Phoenix version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
