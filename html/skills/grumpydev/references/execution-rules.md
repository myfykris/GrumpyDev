# Plan execution rules

## Offer plan execution rules

After delivering the completed review and handling its normal persistence,
ask this numbered question using the next `RQ###` identifier for the
evaluation:

```text
RQ###. When you choose to implement the plan, would you like GrumpyDev to add
its execution rules directly to the plan so the implementing agent stays within
the reviewed scope? Reply `yes` or `no`.
```

Ask after the verdict and review, never before them. This is a plan-scoped
post-review choice, not a substantive review question, and it does not change
the verdict. Ask it after reviews completed in either interactive or
non-interactive mode.

An explicit `yes` authorizes only appending the rules below to the local plan
file reviewed in this evaluation. It does not authorize implementation, approve
a rejected or incomplete plan, change the plan outside its GrumpyDev addendum,
or grant any other permission. The user must separately direct the agent to
implement the plan. A `no`, deferred answer, declined answer, or ambiguous
answer authorizes no write.

On `yes`, find or create the plan's GrumpyDev addendum using the same Markdown,
HTML, or plain-text placement and encoding rules used for review persistence.
Append one clearly labeled `GrumpyDev execution rules` section containing the
self-contained rules below and the enabling `RQ###` identifier. Do not add a
duplicate section. If a section already exists, report that it is already
enabled instead of rewriting it.

```markdown
### GrumpyDev execution rules

When implementing this plan:

- Treat this plan, its GrumpyDev addendum, and applicable `.grump` doctrine as
  the implementation boundary.
- Do not pursue unrelated leads, speculative improvements, opportunistic
  refactors, technology substitutions, or additional features. Report useful
  out-of-scope discoveries instead of implementing them.
- Proceed with minor implementation details that do not materially change
  scope, behavior, architecture, interfaces, dependencies, data handling,
  security, operations, or accepted tradeoffs.
- Before a material deviation, stop, explain what the plan assumed and what the
  evidence shows, propose the smallest plan amendment, and ask whether to update
  and Grump the amended plan before continuing.
- These rules do not authorize implementation or any otherwise unauthorized
  action. Existing safety, approval, and external-publication boundaries still
  apply.
```

Use equivalent valid structure for HTML or plain text while preserving the
wording and meaning. If the reviewed plan is remote, read-only, binary, or
cannot safely contain the rules, do not create a companion file. Explain why
the rules could not be added and return them in chat. Never write this
plan-specific choice to `.grump`.
