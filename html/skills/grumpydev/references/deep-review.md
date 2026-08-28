# Deep GrumpyDev review

Load this file only when the user requests deep review. Apply it after the
standard review guidance.

## Widen evidence deliberately

Trace every materially affected boundary far enough to test the reviewed work's failure
claims. Inspect callers, consumers, schemas, generated artifacts, deployment
configuration, migrations, recovery procedures, and failure-oriented tests
when they can change the verdict. Do not audit unrelated installed technology.

Distinguish checked evidence from a plausible but unverified path. Record which
conclusion depends on evidence that remains inaccessible.

## Challenge transitions and coexistence

Examine startup, steady state, interruption, retry, cancellation, shutdown,
deployment, rollback, restoration, and retirement. Include mixed old and new
versions, long-lived work, duplicate delivery, partial completion, stale state,
and operator intervention when relevant.

Require an owner and a bounded response for each state that can persist after a
failure. A rollback claim is incomplete when emitted messages, external side
effects, irreversible data changes, or client-visible contracts cannot roll
back with the code.

## Challenge degraded operation

Test the reviewed work against unavailable dependencies, slow dependencies, exhausted
resources, corrupt or malformed input, lost acknowledgements, partial regions,
clock and ordering differences, permission denial, and incomplete observability
when those conditions exist in the system.

Identify whether degradation is safe, visible, bounded, and recoverable. Do not
accept `retry`, `fallback`, or `manual recovery` without limits, ownership,
idempotency, and evidence.

## Require independent success evidence

Look beyond the implementation's own happy-path signal. Require evidence that
can distinguish correct behavior from silent omission, partial rollout,
duplicated work, stale reads, authorization bypass, or failed recovery.

Deep review may produce more findings because it inspects more evidence. It
must not produce findings merely to justify the selected depth.
