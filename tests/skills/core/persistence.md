# Review persistence behavior

## Plan addendum

Expected behavior:

- Always return the completed review in chat.
- Append only a completed review when the trusted `.grump` policy allows it.
- Preserve earlier addendum entries and the plan's encoding and line endings.
- Keep an HTML addendum inside `main` or `body`, never after `html`.
- Perform no alternative or remote write without explicit permission.

## Confirmed doctrine

Expected behavior:

- Treat the human-owned `.grump` policy as standing policy for its narrowly
  defined local writes.
- Treat its source field as provenance, not authentication.
- Never turn agent inference or an unanswered review question into doctrine.
