# Doctrine maintenance

## Maintain confirmed doctrine

When the user explicitly resolves a project unknown, accepts a tradeoff, or
confirms or changes a durable constraint or decision during a review, follow the
`Confirmed doctrine updates` policy in `.grump`:

- `allowed` is trusted human-owned standing policy to record that explicitly
  confirmed item in the local `.grump` file without asking again for the file
  write.
- `propose only`, absent, or unresolved means show the exact proposed `.grump`
  change in chat and do not write it.

An allowed update must preserve the user's meaning, manual wording, section
structure, and stable identifiers. Assign the next available identifier to a
new constraint, tradeoff, decision, or unknown. When resolving an existing
unknown, preserve its identifier and mark its resolution or link it to the new
durable item instead of silently deleting history.

Do not write when the user's statement is ambiguous, hypothetical, or merely
acknowledges a review finding. Ask one deduplicated, numbered clarification when
the intended doctrine change is material but unclear. Never convert agent
inference or a GrumpyDev recommendation into accepted doctrine. This policy does
not authorize changes to plans outside their addenda, source code, project
documentation, issue trackers, remote files, or any external system.

For a promoted review answer, require the user's explicit `project-wide`
choice. Record its provenance as the evaluation timestamp, reviewed target path,
and `RQ###` identifier. If the policy is `propose only`, absent, or unresolved,
show the exact proposed `.grump` change in chat without writing it.

After an allowed update, reread the affected `.grump` section, verify the
recorded meaning and identifiers, and report the exact file changed. Never claim
the doctrine was updated unless the write succeeded and was verified.
