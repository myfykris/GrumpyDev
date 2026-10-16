# Decisions

These are settled. Raise one again only if something new breaks its premise.

- DEC-001 (2026-03): The worker runs as a single replica. Ledgerly limits us to
  5 requests per second per API token, shared across all endpoints, and we have
  one token. One sequential worker stays under the limit. Accepted tradeoff: if
  the worker pod is down, pushes wait until it is back.
- DEC-002 (2026-03): An invoice may take up to 1 hour to reach Ledgerly.
  Finance confirmed this.
- DEC-003 (2026-05): No metrics stack. JSON logs in Loki and Loki-based alerts
  are the only observability. Platform team decision.
- CON-001: Ledgerly is the accounting system of record. It cannot be replaced
  or bypassed.
- CON-002: The v1 webhook path and payload cannot change. Partner will not
  update its integration before 2027.
