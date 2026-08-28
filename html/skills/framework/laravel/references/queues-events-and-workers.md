# Laravel queues, events, and workers

Read this reference when the reviewed work directly or indirectly changes queued jobs,
events, listeners, notifications,
Horizon, scheduler behavior, retry, uniqueness, ordering, idempotency, worker
termination, Octane, or another resident process.

## Queues, events, and long-running processes

- Treat every queued job as repeatable unless the selected queue proves a
  stronger guarantee. Define idempotency at the side effect, not just a unique
  dispatch check.
- Check dispatch-before-commit, after-commit configuration, model identifier
  serialization, relation loading, deleted records, tenant context, encrypted
  payloads, code-version overlap, retry delay, timeout, and worker termination.
- Separate events that announce a committed fact from commands that request an
  effect. Retrying a listener can duplicate email, billing, file, or external
  API effects even if the database update is transactional.
- Define scheduler overlap, single-server locks, clock and timezone behavior,
  missed runs, manual replay, and long-running command failure.
- For Octane or other resident runtimes, require reset of request-scoped state,
  locale, tenant, authentication, static caches, singletons, database sessions,
  and third-party client state. Confirm package compatibility with the runtime.
