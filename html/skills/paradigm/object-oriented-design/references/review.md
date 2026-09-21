# Object-oriented design full-review guidance

## Operating conditions

Establish the project target: Domain object conventions, framework lifecycle
constraints, mutability policy, dependency injection approach, persistence
mapping, and accepted inheritance or composition rules. The changed boundary
must define: Identity, state and invariants, composition, inheritance,
substitutability, encapsulation, mutation, lifecycle, dependency direction, and
test seams.

## Failure patterns

- Reject classes that only rename records, functions, or database tables without
  owning behavior or invariants.
- Prefer composition unless substitution is real, tested, and stable across
  every subtype.
- Keep invalid state unrepresentable where practical and prevent partially
  initialized objects from escaping.
- Check whether dependency injection clarifies replaceable boundaries or merely
  adds interfaces and factories everywhere.
- Expose temporal coupling, feature envy, god objects, hidden mutation, and
  mocks that test implementation instead of behavior.

## Verification to run or specify in the plan

- Run the same caller-level contract against each subtype, including error and
  lifecycle behavior. Check that substituting an implementation does not
  strengthen preconditions or weaken guarantees.
- Exercise invalid construction, unexpected method order, and mutation through
  shared references. Verify object invariants survive without requiring
  callers to know hidden initialization or cleanup steps.
