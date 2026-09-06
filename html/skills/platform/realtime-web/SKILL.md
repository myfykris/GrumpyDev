---
name: realtime-web
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review realtime web engineering work for connection lifecycle, authentication, ordering, backpressure, reconnect, fan-out, presence, state recovery, and capacity."
---

# Realtime web GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the
`distributed-systems`, `application-security`, and `performance-capacity`
skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

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
