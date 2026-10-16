# Security policy

## Reporting a problem

Open a GitHub issue. Say which file or behavior is affected, what it should not
be able to do, and how to reproduce it. Leave out secrets, credentials and
private code, and rotate any credential that may have been exposed.

## Scope

Reports may cover the static website, the installer (`skills/install.md`), the
skill (`skills/grumpydev/SKILL.md` and `references/audit.md`), or the blocks
GrumpyDev writes into project instruction files. A skill grants an
agent no additional permissions or authority; the host and the user still
control both.

The installer and skill files are untrusted plain text. The installer fetches
only the two skill files, only from `https://grumpydev.ai`, rejects a redirect
to another origin, and installs inside the current project only.

During a review the skill fetches nothing and writes only to
`.grumpydev/reviews/`. It never edits the reviewed work, source code or
`.grump`. `Grump accept` writes `.grump` only after the user confirms, and
`Grump sync` writes only inside the marked constraints blocks.

Setup may add marked blocks to project instruction files: a constraints block
(`BEGIN GRUMPYDEV CONSTRAINTS` ... `END GRUMPYDEV CONSTRAINTS`) in each agent
context file the user chooses, and, only for harnesses without project skill
discovery, a routing block (`BEGIN GRUMPYDEV ROUTING INSTRUCTION` ...
`END GRUMPYDEV ROUTING INSTRUCTION`). The routing block tells the agent to read
the local skill only on an explicit GrumpyDev request and never to fetch or
reinstall it automatically. Nothing outside a block is changed.

`Grump update` shows the diff for each skill file and replaces them only after
the user confirms. `Grump remove` deletes the skill directory and the marked blocks, and asks
before deleting `.grump` or `.grumpydev/`. GrumpyDev keeps no installation
receipt, state database or lockfile.

Keep passwords, API keys and production data out of `.grump` and the ledgers;
they are plain text intended for the repository.
