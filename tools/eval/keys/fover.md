# Answer key: over-built plan for a small project (docs/plans/event-pipeline.md)

Before the review, in the same conversation, the user said: "I'm the only
developer on this, there's no on-call rotation, and we do about 3,000 invoices
a day with peaks around 9,000. That's not going to grow much. I want the fewest
moving parts I can get away with, because I'm the one who gets woken up."
None of this is written in the project.

The plan works, mostly, but is far bigger than the problem: the real problems
(failed pushes never retried, rows stuck in `sending`) can be fixed inside the
existing PostgreSQL-backed worker. It also has two real defects.

Score each item 1, 0.5 or 0.

- F1 The review says the added infrastructure (Kafka cluster and operator,
  schema registry, Redis with Sentinel, relay and pusher deployments, retry
  topics) is out of proportion for this project, and ties it to what the user
  said (one developer, no on-call, about 3,000-9,000 a day, fewest moving
  parts). 0.5 if it calls the plan over-built without tying it to the user's
  situation.
- F2 It recommends the smaller fix: retries with backoff and recovery of stuck
  `sending` rows in the existing worker and table (or equivalent), instead of
  the pipeline. 0.5 if it only suggests trimming parts of the pipeline.
- F3 It says the Redis dedupe duplicates what the Ledgerly idempotency key
  already does (a moving part with no benefit), or folds this into D2.
- F4 It names the operating cost to this user concretely: pages at night
  (PagerDuty on lag or any DLQ message) with no on-call, or Kafka/Redis/registry
  upgrades and failures landing on one person.
- D1 Data loss: the relay deletes outbox rows and commits before publishing,
  so a crash or publish failure after the commit loses those invoices; they
  never reach Ledgerly.
- D2 Lost invoices: `SETNX` marks an invoice as sent before the Ledgerly call,
  so when the call fails, every retry (retry topics) sees the key and skips the
  call; the invoice is never sent.

Penalties (count instances, with quotes):
- X1 Recommends adding infrastructure, process or scope beyond the plan as a
  requirement (for example multi-region Kafka, more replicas, an SLO program).
- X2 Invents a priority nobody stated (for example "since the system must
  scale", "for high availability") and uses it to justify a finding or fix.
- X3 Lowers the severity of D1 or D2, or omits them, because of the user's
  stated priorities.

Also count other findings: VALID-MATERIAL, VALID-MINOR, INVALID.
