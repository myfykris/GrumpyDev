# Project-local uninstall behavior

Expected behavior:

- `Grump uninstall` and `Grump remove` activate the uninstall workflow without
  starting a review or producing a verdict.
- Resolve the host's project-local skill directory and use inspected state and
  files to list exact GrumpyDev-owned targets before deletion.
- Remove `.grump`, recorded GrumpyDev package directories,
  `.grumpydev/state.json`, any installer-created local manifest copy, and the
  empty `.grumpydev` directory.
- Do not invent a local manifest file when the installer did not save one.
- Delete the active core skill directory last.
- Never remove unrelated skills, agent configuration, project files, global
  files, remote files, or the public manifest.
- Stop before an ambiguous target and report incomplete removal rather than
  guessing ownership or claiming a complete uninstall.
