# Review history and persistence

Load this reference when an earlier review exists for the same target, when a
plan addendum already exists, or when the exact `Plan addenda` preference or a
current explicit instruction authorizes persistence.

## Preserve issue continuity

Read the latest completed review for the current target. Scan older issue IDs
and status records to find unresolved issues and avoid reusing an ID; open older
finding details only when needed for identity, evidence, closing conditions, or
a suspected regression. Absence from a later entry does not resolve an issue.
Use one ID namespace only for the same repository-relative artifact or an
explicitly identified successor, not merely similar titles or project membership.

Treat an earlier finding as identity and history, not current proof. Reinspect
current evidence, reuse its `GD-###` ID for the same underlying failure and
closing condition, and classify it as `OPEN`, `RESOLVED`, or `REGRESSED`.
Assign the next unused `GD-###` ID to a genuinely new finding. Never recycle a
resolved ID. When known history is unavailable, use evaluation-scoped
`TMP-###` IDs and state the continuity limit; do not give temporary IDs
lifecycle status.

For each new finding in a repeated review, use one plain `Why new` value and a
supporting sentence:

- `caused by revision`;
- `new evidence`;
- `broader requested scope`;
- `missed earlier`; or
- `unknown`.

Preserve earlier IDs when several findings now share one correction. Do not
replace them with a new group ID. A substantive correction can close a plan
finding when the revised plan resolves its condition coherently. Claims about
existing implementation need current implementation evidence; a promise or
bare statement that something is fixed is not proof.

## Persist an authorized plan review

Always return the complete review in chat. Append it to the local plan only
when `Plan addenda: allowed` is an exact valid `.grump` preference or the user
explicitly authorizes that write now. `chat only`, missing, invalid, or
conflicting values authorize no plan edit. This permission never authorizes a
remote write or a change outside the addendum.

Append only after the review and verdict are complete:

1. For Markdown, find or create a final `## GrumpyDev addendum`. For HTML, use
   one `#grumpydev-addendum` inside `body`, as the final child of `main` when
   possible. For plain text, use an unambiguous final heading. Never append
   after `</html>` or create a duplicate HTML ID.
2. Add a new entry labeled with an ISO 8601 UTC evaluation time. Preserve all
   earlier entries.
3. Persist the verdict, summary, confidence, findings, review scope, warnings,
   and material review answers used. Include evidence gaps, strengths, revised
   path, resolutions, `Why new`, and revision closure only when the chat review
   includes them. Do not persist the later execution-rules question.
4. Keep every evidence locator, established-fact scope, inference, condition,
   consequence, required action, and confidence limitation aligned with chat.
   Compact wording may deduplicate text but may not erase a material
   distinction.
5. Preserve the plan's encoding, line endings, and valid structure. Reread and
   validate the result before claiming persistence.

If the plan is remote, read-only, binary, or unsafe to edit, return the review
in chat and explain why it was not persisted. Do not invent a companion file.
If another local persistence target might be useful, ask before creating it.

On a later review, allocate IDs above the highest verified canonical ID. Report
active findings and meaningful status changes; keep unchanged resolved history
compact rather than repeating descriptions. Distinguish historical resolution
from current revalidation, and never count resolved issues as active findings.
Disclose unavailable history or failed persistence; never claim continuity or
current verification that was not established.
