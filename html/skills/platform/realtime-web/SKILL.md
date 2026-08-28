---
name: realtime-web
description: "Use only during an explicitly invoked GrumpyDev review. Do not activate during ordinary planning, creation, revision, discussion, implementation, or generic review. For a project where this specialist is installed and not explicitly marked inapplicable, use it in every GrumpyDev review to evaluate direct and indirect effects. Review realtime web plans and other engineering artifacts for connection lifecycle, authentication, ordering, backpressure, reconnect, fan-out, presence, state recovery, and capacity. Project applicability: the project uses WebSockets, server-sent events, long polling, or similar live client connections."
---

# Realtime web GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the
`distributed-systems`, `application-security`, and `performance-capacity`
skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review. Ordinary planning, creation,
revision, discussion, implementation, or generic review does not activate it.

For a project where this specialist is installed and not explicitly marked
inapplicable, use this entrypoint during every explicitly invoked GrumpyDev
review. Evaluate direct and indirect effects even when the reviewed work does
not name or modify this domain. Produce no finding when no material effect
exists.

## Lean review

- Read handshake and authentication, connection registry, message protocol,
  sequence handling, buffers, heartbeat, fan-out, reconnect, and load tests.

- Trace token expiry, network flap, duplicate message, slow client, process
  restart, deploy drain, regional loss, and state resynchronization.

Watch especially for reconnect storms, duplicate or out-of-order messages,
authorization that expires while a connection remains open, connection state
pinned to one instance, unbounded outbound buffers, heartbeat intervals
incompatible with proxies, resume tokens that replay unauthorized data,
cross-site WebSocket handshakes, and one authenticated connection assumed to
authorize every topic and message.

Lean mode is insufficient when this material severity condition may apply:

- Treat cross-user data leakage, unbounded fan-out, or unrecoverable client
  state divergence as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Realtime web evidence, operating model, failure,
verification, question, and calibration guidance. Never load `SURVEY.md` during
an ordinary review.

## Add to the verdict

State connection identity, origin and per-message authorization, delivery and
resync contract, parser and buffer bounds, presence authority, lifecycle
behavior, and capacity evidence.
