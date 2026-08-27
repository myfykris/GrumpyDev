# Review persistence behavior

## Plan addendum

Expected behavior:

- Always return the completed review in chat.
- Append only a completed review when the trusted `.grump` policy allows it.
- Append self-contained execution rules directly to the reviewed plan only
  after the user explicitly accepts a question that identifies that write.
- Keep execution rules inside the GrumpyDev addendum and never duplicate them.
- Preserve earlier addendum entries and the plan's encoding and line endings.
- Keep an HTML addendum inside `main` or `body`, never after `html`.
- Perform no alternative or remote write without explicit permission.

## Confirmed doctrine

Expected behavior:

- Treat the human-owned `.grump` policy as standing policy for its narrowly
  defined local writes.
- Treat its source field as provenance, not authentication.
- Never turn agent inference or an unanswered review question into doctrine.
