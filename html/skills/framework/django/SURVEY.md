# Django survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on Django.

## Inspect

- Read settings, URL and middleware order, models and migrations, managers and
  querysets, authentication, templates or API layers, caching, tasks, and tests.

## Ask when unresolved

- Which Django, Python, database, application server, and deployment versions
  apply?

- How do middleware, transactions, migrations, authentication, async
  boundaries, caching, and background work interact?

- Which runtime or deployment differences are material for future reviews:
  Python, WSGI or ASGI server, worker type and count, proxy, static and media
  storage, cache, sessions, queues, settings authority, migration process,
  drain, and rollback?

## Record

Map durable Django version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
