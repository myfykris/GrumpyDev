# Doctrine maintenance

## Maintain confirmed doctrine

When the user explicitly resolves a project unknown, accepts a tradeoff, or
confirms or changes a durable constraint or decision during a review, follow the
`Confirmed doctrine updates` policy in `.grump`:

- `allowed` is trusted human-owned standing policy to record that explicitly
  confirmed item in the local `.grump` file without asking again for the file
  write.
- `propose only`, missing, invalid, or conflicting means show the exact proposed
  `.grump` change in chat and do not write it.

Before an authorized write, read the installed
[doctrine-format.md](../../grumpydev-survey/references/doctrine-format.md)
for structure and editing rules. This does not authorize a survey.

An allowed update must preserve the user's meaning, manual wording, unknown
content, section structure, and stable identifiers. Assign the next available
applicable `CON-###`, `DEC-###`, or `UNK-###` identifier only when a stable
cross-session reference is useful. When resolving an existing unknown, preserve
its identifier and mark its resolution or link it to the new durable item
instead of silently deleting history. If a bounded edit cannot preserve the
surrounding human-owned content, leave `.grump` unchanged and show the proposed
edit in chat.

Do not write when the user's statement is ambiguous, hypothetical, or merely
acknowledges a review finding. Ask one deduplicated, numbered clarification when
the intended doctrine change is material but unclear. Never convert agent
inference or a GrumpyDev recommendation into accepted doctrine. This policy does
not authorize changes to plans outside their addenda, source code, project
documentation, issue trackers, remote files, or any external system.

For a promoted review answer, require the user's explicit `project-wide`
choice. Record its provenance as the evaluation timestamp, reviewed target path,
and `RQ###` identifier. If the policy is `propose only`, missing, invalid, or
conflicting, show the exact proposed `.grump` change in chat without writing it.

After an allowed update, reread the affected `.grump` section, verify the
recorded meaning and identifiers, and report the exact file changed. Never claim
the doctrine was updated unless the write succeeded and was verified.
