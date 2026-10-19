# Plan: event-driven invoice pipeline

Author: Sam Rivera (contractor). Status: draft.

## Problem

The worker polls `invoices` every 5 seconds and pushes one invoice at a time.
A failed push is marked `failed` and never retried, and a crash mid-batch leaves
claimed rows in `sending` forever. On-call has re-queued rows by hand several
times this quarter.

## Design

Replace polling with an event pipeline so pushes are retried, scale out, and
can be replayed.

1. **Kafka.** Run a 3-broker Kafka cluster in our Kubernetes cluster with the
   Strimzi operator. Topics: `invoices.created` (6 partitions, keyed by
   `partner_invoice_id`), `invoices.retry.1m`, `invoices.retry.10m`,
   `invoices.retry.1h` and `invoices.dlq`. Retention 7 days.
2. **Schema registry.** Deploy Confluent Schema Registry and define an Avro
   schema `InvoiceCreated` (external_id, amount, currency, created_at). All
   producers and consumers use the registry.
3. **Transactional outbox.** The webhook handler inserts the invoice and an
   `outbox` row in one transaction (migration 002 adds `outbox(id bigserial,
   payload jsonb, created_at timestamptz)`).
4. **Outbox relay.** A new `outbox-relay` Deployment (1 replica) runs a loop:
   in one transaction, select up to 500 `outbox` rows ordered by id, delete
   them, and commit; then publish each payload to `invoices.created`. Sleep
   1 second when the outbox is empty.
5. **Ledgerly pusher.** A new `ledgerly-pusher` Deployment (3 replicas, one
   consumer group) consumes `invoices.created`, posts to Ledgerly with the same
   `idempotency-key: inv-<partner_invoice_id>` as today, and updates
   `invoices.status`. On a 5xx or timeout it publishes to the next retry topic;
   after `invoices.retry.1h` it publishes to `invoices.dlq`.
6. **Redis dedupe.** Before each Ledgerly call the pusher checks a Redis set
   (`SETNX ledgerly:sent:<external_id>`, TTL 7 days) and skips the call if the
   key exists. Run Redis with Sentinel (3 nodes) for failover.
7. **Observability.** Deploy the Kafka exporter and Redis exporter, add Grafana
   dashboards for consumer lag and retry-topic depth, and page through
   PagerDuty when consumer lag exceeds 1,000 messages for 5 minutes or the DLQ
   receives any message.
8. **Remove the worker.** Delete `src/worker.ts` and `deploy/worker.yaml` once
   the pipeline is live.

## Rollout

1. Deploy Kafka, the registry, Redis and the exporters.
2. Run migration 002 and release the server with the outbox write.
3. Start `outbox-relay` and `ledgerly-pusher` with the pusher's Ledgerly calls
   switched off; check that lag stays near zero for a day.
4. Scale the old worker to 0, then switch the pusher's Ledgerly calls on.
5. Publish every `pending`, `failed` and `sending` invoice to
   `invoices.created` with a one-off script.

## Testing

- Integration test with Testcontainers (Kafka, Redis, PostgreSQL) for the
  happy path and one retry.
- Load test at 50,000 invoices per hour.

## Estimate

Three weeks for the contractor, then a handover session.
