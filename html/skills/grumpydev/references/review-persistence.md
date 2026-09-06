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
   with an ISO 8601 UTC evaluation time. Always persist verdict, warnings when
   present, summary, confidence, findings, review scope, and material `RQ###`
   answers used by the review. Persist the following only under the same
   conditions used for chat output:
   - `What holds up` when evidence supports a material, non-obvious strength
     worth preserving;
   - `Evidence gaps` when a material evidence or coverage gap exists;
   - `Revised path` when a correction or decision is needed;
   - `Resolved since the previous review` when current evidence verifies at
     least one earlier finding as resolved;
   - `Why new` for a `NEW` finding in a repeated review with a normal `GD-###`
     ID; and
   - `Revision closure` for an implementation plan with active findings.
   Never persist the post-review execution-rules question as part of the review
   result. Do not write empty headings, placeholder values, or inapplicable
   conditional sections.
4. Preserve the plan's format, declared encoding, and line-ending convention.
   Escape inserted content correctly for the file format.
5. Validate the resulting structure before reporting persistence. If validation
   fails, leave or restore the original file and report the failure.
6. If the plan is remote, read-only, binary, or cannot safely contain an
   addendum, do not invent a companion file or rewrite the format. Return the
   review in chat, explain why it was not persisted, and ask one deduplicated,
   numbered question before creating any alternative file.

The chat result and persisted entry must describe the same findings,
resolutions, evidence limitations, strengths, and revision requirements.
Persistence must not invent a section that chat correctly omitted.

Every persisted finding must retain the same evidence locator, established-fact
scope, inference, conditional language, impact, required action, and confidence
limitation shown in chat. A compact addendum may deduplicate repeated locator
text only when each material claim still maps unambiguously to its evidence. Do
not shorten persistence by deleting an evidence or uncertainty distinction.

On a later review, read prior addendum entries before assigning issue IDs. Match
the same underlying issue even when its title or severity changed. Reuse its
`GD-###` ID, allocate new IDs above the highest one previously used for that
plan, and never recycle resolved IDs. Classify findings as `NEW`, `OPEN`,
`RESOLVED`, or `REGRESSED`. Require current evidence before claiming resolution.
Persist the current verification evidence for every resolution. An earlier
finding, a revised plan sentence, or a claimed implementation action does not by
itself prove that implementation is fixed.
If known prior history is unavailable, persist only clearly labeled `TMP-###`
IDs and the continuity limitation. Never record a temporary ID as canonical or
give it lifecycle status.

For each repeated-review `NEW` finding with a normal ID, persist its `Why new`
label and supporting sentence. Persist `UNKNOWN` with the missing comparison
evidence. Do not persist status or `Why new` for a temporary ID. Preserve the
first recorded `Why new` label without repeating or replacing it when the issue
later becomes `OPEN`, `RESOLVED`, or `REGRESSED`. If later evidence disproves
the label, append a correction with the earlier label, correct label, evidence,
and reason. Never edit the earlier entry.

When several historical IDs share one cause, required correction, and closing
condition, persist every ID and status under the shared fix. Never replace them
with a new group ID.

Persist the core coverage statement and any named limitation. Persist revision
closure with active implementation-plan findings, including the observable
closing condition and affected plan concerns. Revision closure does not
authorize a plan edit, implementation, or another review.

Do not treat an earlier verdict or finding as current project doctrine without
supporting evidence. Report a failed addendum write plainly; never claim
persistence unless the file was successfully updated and verified.
