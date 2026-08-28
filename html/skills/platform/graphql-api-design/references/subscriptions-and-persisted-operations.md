# GraphQL subscriptions and persisted operations

Read this reference when the reviewed work directly or indirectly changes subscriptions,
long-lived authorization, token
expiry, revocation, reconnect, fan-out, event filtering, persisted operations, operation
registration, allowlists, rollout, or revocation.

## Review requirements

- Authenticate and authorize subscription connection, operation, topic, and
  each delivered event. Define token expiry, permission change, revocation,
  reconnect, message size, and per-client fan-out limits.

- Treat persisted operations as a controlled contract with ownership,
  registration, rollout, revocation, and query-cost evidence. An allowlisted
  operation still requires normal authorization and input validation.

## Verify the claims

- Connect, subscribe, reconnect, refresh and revoke through the production
  transport and authorization path. Verify authorization at connection,
  operation, topic and event delivery rather than only at initial login.

- Expire tokens, change roles, remove tenant access, reorder and duplicate
  events, slow consumers, exceed fan-out and message limits, lose a server, and
  verify reconnect does not skip or expose data outside the stated contract.

- Register, deploy, revoke and roll back persisted operations while old and new
  clients coexist. Verify allowlists, query-cost controls and normal input and
  authorization checks remain active throughout.

- Exercise deep and broad fragments, repeated aliases, list multipliers,
  malformed variables, oversized batches, expensive mutations, reconnect, and
  introspection or persisted-operation policy in the production configuration.
