# Review persistence

## Persist the review result

Always return the completed review in chat. Then follow the `Plan addenda`
policy in `.grump`:

- `allowed` is trusted human-owned standing policy to append the result to the
  local plan file being reviewed. Do not ask again for each evaluation.
- `chat only`, absent, or unresolved means do not change the plan file.

Treat the policy source as audit provenance, not proof of authorship. A current
explicit user instruction overrides the stored policy for the current work.
Malformed, unknown, or contradictory values grant no write. This policy never
authorizes a remote write, publication, or a change outside the addendum.

When plan addenda are allowed:

1. Append only after producing a complete review with a verdict. Do not persist
   preliminary questions, partial analysis, or abandoned reviews.
2. For Markdown, find or create a final `## GrumpyDev addendum` section. For
   HTML, append to an existing `#grumpydev-addendum` inside the document body.
   If none exists, insert one as the final child of `main` when present,
   otherwise immediately before `</body>`. Never append after `</html>` or
   create a duplicate ID. For plain text, use an unambiguous final `GrumpyDev
   addendum` heading.
3. Append a new entry without changing or deleting earlier entries. Label it
   with an ISO 8601 UTC evaluation time and include depth, verdict, confidence,
   warnings, critical findings, what holds up, evidence gaps, revised path, and
   material `RQ###` answers used by the review.
4. Preserve the plan's format, declared encoding, and line-ending convention.
   Escape inserted content correctly for the file format.
5. Validate the resulting structure before reporting persistence. If validation
   fails, leave or restore the original file and report the failure.
6. If the plan is remote, read-only, binary, or cannot safely contain an
   addendum, do not invent a companion file or rewrite the format. Return the
   review in chat, explain why it was not persisted, and ask one deduplicated,
   numbered question before creating any alternative file.

On a later review, read prior addendum entries and distinguish resolved,
remaining, regressed, and newly discovered findings. Do not treat an earlier
verdict or finding as current project doctrine without supporting evidence.
Report a failed addendum write plainly; never claim persistence unless the file
was successfully updated and verified.
