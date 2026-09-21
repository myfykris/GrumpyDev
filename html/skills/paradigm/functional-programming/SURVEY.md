# Functional programming survey contribution

## Applies when

Apply this contribution when the project architecture or correctness materially depends
on functional programming concepts or language features.

## Inspect

- Read data types, effect wrappers, pure core boundaries, state transitions,
  error channels, recursion, evaluation strategy, and tests.

## Ask when unresolved

- What conventions separate pure functions from effects, mutable state,
  failure, cancellation, and resource ownership in this project?

- Which evaluation, recursion, allocation, or parallelism assumptions affect
  correctness or scale?

## Record

Map accepted Functional programming architecture choices to `Accepted
decisions`, binding boundaries to `Requirements` or `Constraints`, and material
gaps to `Unknowns`.
