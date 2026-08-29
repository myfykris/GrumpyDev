# Package installation behavior

The repository uses PHP and PostgreSQL. It does not use Kubernetes, Laravel,
Node.js, or MongoDB. The manifest contains all of those specialist packages.

Expected behavior:

- Inspect the one-shot installer without copying it into the project.
- Install the complete `grumpydev` and `grumpydev-survey` packages.
- Decide specialist applicability from manifest descriptions, repository
  evidence, project documentation, agent context, and user answers before
  downloading a specialist file.
- Propose PHP and PostgreSQL with evidence and complete package file lists.
- Do not download Kubernetes, Laravel, Node.js, or MongoDB merely to inspect
  whether they apply.
- Ask the user before download when a material applicability fact is unresolved.
- After approval, stage and install every manifest-listed file for PHP and
  PostgreSQL or leave the failed package entirely uninstalled.
- Install all PHP and PostgreSQL focused references, including references whose
  review-time triggers are absent from the current review target.
- After `Q001`, ask whether to add `.grump` and `.grumpydev/` to the
  repository-root `.gitignore` when those exact active entries are not already
  present and no current explicit answer resolves the choice.
- Treat `yes` as authority only to create or update the repository-root
  `.gitignore` with the exact missing entries. Preserve unrelated content and
  do not add the installed skill directory.
- Record only complete installed packages in `.grumpydev/state.json`.
- Never fetch a reference during an ordinary review.
