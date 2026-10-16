
## Constraints

- CON-001: Ledgerly is the accounting system of record; it cannot be replaced or bypassed. Source: docs/decisions.md; confirmed.
- CON-002: The v1 webhook path and payload cannot change before 2027 (Partner). Source: docs/decisions.md; confirmed.

## Accepted decisions

- DEC-001: The worker runs as a single replica. Ledgerly allows 5 requests/second per token, shared across all endpoints, and we have one token; one sequential worker stays under it. Accepted: pushes wait while the worker is down. Source: docs/decisions.md; confirmed.
- DEC-002: An invoice may take up to 1 hour to reach Ledgerly. Source: docs/decisions.md (Finance); confirmed.
- DEC-003: No metrics stack; JSON logs in Loki and Loki-based alerts are the only observability. Source: docs/decisions.md (platform team); confirmed.
