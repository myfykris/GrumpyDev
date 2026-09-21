# Modular monolith survey contribution

## Applies when

Apply this contribution when one deployable system contains intentionally isolated
business modules.

## Inspect

- Read module APIs, dependency rules, build layout, database ownership,
  transaction boundaries, background work, and architecture tests.

## Ask when unresolved

- Which module owns each invariant and data set, and what mechanism enforces
  dependency direction?

- How do transactions, background work, migrations, tests, and future
  extraction cross module boundaries?

## Record

Map accepted Modular monolith architecture choices to `Accepted decisions`,
binding boundaries to `Requirements` or `Constraints`, and material gaps to
`Unknowns`.
