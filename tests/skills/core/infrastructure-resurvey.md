# Infrastructure re-survey behavior

After the initial survey, the project changes runtime, hosting owner, network
trust boundary, worker delivery behavior, and database recovery design. A
separate deployment changes only a transient hostname.

Expected behavior:

- Recommend re-survey for each durable change that can invalidate future
  reviews.
- Reinspect evidence and merge only changed material facts into `.grump`.
- Preserve human wording and stable `DEP-###` and `INF-###` identifiers.
- Retire obsolete profiles or shared components without renumbering later ones.
- Do not trigger durable doctrine churn for the transient hostname alone.
