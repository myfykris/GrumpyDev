# Initial-install gitignore preference

Expected behavior:

- Inspect the repository-root `.gitignore` after repository evidence and before
  presenting the initial question batch.
- Keep the doctrine-format question first as `Q001`.
- When one or both exact active entries are missing and no current explicit
  answer resolves the choice, ask one numbered question immediately after
  `Q001`: `Do you want GrumpyDev to add itself to .gitignore?`
- An explicit `yes` creates the repository-root `.gitignore` when absent or adds
  only the missing exact entries when it exists.
- Preserve unrelated content, established line endings, UTF-8 encoding, and a
  final newline. Do not duplicate active entries.
- Do not add the installed skill directory or any path other than `.grump` and
  `.grumpydev/`.
- If both exact active entries already exist, do not ask and report that the
  generated files are already ignored.
- If only one exact active entry exists, ask when needed and add only the other
  entry after an explicit `yes`.
- A current explicit `yes` or `no` resolves the choice without another
  question.
- A `no`, decline, deferral, ambiguous answer, unsafe-to-edit encoding, or
  unsafe file target leaves `.gitignore` unchanged and does not block the rest
  of installation.
- Never ask this preference during re-survey or an ordinary review.
- Do not store the question, answer, or status in `.grump` or
  `.grumpydev/state.json`; `.gitignore` itself is authoritative.
- Report whether `.gitignore` was created, updated, already configured, or left
  unchanged.
