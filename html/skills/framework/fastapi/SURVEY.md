# FastAPI survey contribution

## Applies when

Apply this contribution when the project uses or materially depends on FastAPI.

## Inspect

- Read application and router construction, dependencies, Pydantic models and
  settings, middleware, lifespan handlers, server configuration, and tests.

## Ask when unresolved

- Which Python, FastAPI, Starlette, and Pydantic versions and server-worker
  model apply?

- How do validation, dependency lifetimes, sync work, async cancellation,
  errors, and schema compatibility behave?

- Which runtime or deployment differences are material for future reviews:
  Python, ASGI server, worker class and count, sync-thread pool, proxy,
  lifespan, sessions, background execution, limits, drain, and deployment?

## Record

Map durable FastAPI version and behavior requirements to `Requirements` or
`Constraints`, lifecycle and deployment facts to `Runtime and deployment`, and
material gaps to `Unknowns`.
