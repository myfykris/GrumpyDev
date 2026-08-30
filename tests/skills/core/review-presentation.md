# Review presentation behavior

Expected behavior:

- Missing or unresolved presentation policy defaults to preferred finding
  tables and enabled status icons.
- A current explicit user instruction overrides `.grump` for one evaluation.
- Honor an unambiguous equivalent instruction elsewhere in `.grump` without
  requiring exact field names.
- `Finding tables: disabled` uses headed prose without weakening the finding.
- `Status icons: disabled` keeps verdict, warning, severity, and issue ID text
  while omitting icons.
- Before assigning IDs, inspect available completed reviews for the same target.
- Share an ID namespace only for the same repository-relative artifact or an
  explicitly identified revision, rename, or successor.
- Never infer target continuity from similar titles, content, or project
  membership.
- Reuse a target-scoped `GD-###` identifier for the same underlying issue even
  when its title or severity changes.
- Allocate new IDs above the highest one previously used for that target and
  never recycle a resolved ID or reassign an ID to another issue.
- When known prior reviews are unavailable, identify the continuity limit and
  use labeled evaluation-scoped `TMP-###` IDs without lifecycle status instead
  of starting a potentially colliding `GD-001` sequence.
- On repeated reviews, classify issues as `NEW`, `OPEN`, `RESOLVED`, or
  `REGRESSED` and pair status icons with text when icons are enabled.
- Require current evidence before marking an issue `RESOLVED`; omission,
  renaming, or inaccessible evidence is not resolution.
- After the verdict and any required warning, print one `Summary:` sentence
  with active finding counts and the main reason for the verdict.
- When finding tables are preferred and at least two active issues are concise,
  use
  `ID | Severity | Issue | Why it matters | Required action` columns.
- Sort issues by severity and then by dependency or execution order when useful.
- Keep table cells concise and expand complex findings below the table under
  the same issue ID.
- When there are no active issues, state that plainly instead of rendering an
  empty table.
- Use headed prose for one active issue or when code, multiline evidence, or a
  narrow output surface would make a table harder to read.
- Pair every icon with a text verdict, warning, severity, or issue ID. Never use
  icon shape or color as the only status signal.
- Use the defined verdict and severity icon mappings instead of choosing
  different decorative icons in each review.
- Preserve `evidence -> failure condition -> impact -> required action` in
  either table or prose form.
- Do not invent low-severity issues to fill a table.
- Put target, depth, materially used references, and coverage limits in a final
  `Review scope` footer instead of before the summary or findings.
