# Review answer promotion behavior

## Durable answer

An `RQ###` answer appears to establish a project-wide constraint that would
materially improve future reviews, but the user has not stated its scope.

Expected behavior:

- Ask one separate `RQ###` question offering `project-wide` and `this review
  only`.
- Do not promote the answer automatically.
- If project-wide is selected, apply the separate confirmed-doctrine write
  policy.
- If doctrine writes are not allowed, show the exact proposed `.grump` change
  without writing it.

## Evaluation-only answer

The answer is temporary or specific to the current implementation plan.

Expected behavior:

- Do not ask a promotion question.
- Keep the answer in the current evaluation and any authorized plan addendum.
- Do not write it to `.grump`.
