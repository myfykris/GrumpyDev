# Security policy

## Reporting a vulnerability

Do not include secrets, credentials, private repository content, personal data,
or exploit details in a public issue.

Use GitHub private vulnerability reporting when it is available for this
repository. Open the repository's Security page, select "Report a
vulnerability", and submit the smallest reproduction that establishes the
problem.

If private vulnerability reporting is unavailable, open a public issue that
only asks the maintainers to establish a private contact channel. Do not include
technical vulnerability details in that issue.

Include the affected file or behavior, expected security boundary, practical
impact, and a minimal reproduction. Remove unrelated project data and rotate
any credential that may have been exposed.

## Scope

Security reports may cover the static website, installer instructions,
manifest, core skills, specialist skills, survey behavior, or project-local
routing instructions. A skill does not grant an agent additional permissions or
authority; the host and user still control both.

Installed skills include every file listed for that skill in the manifest.
Ordinary reviews use those local files and must not fetch new instructions.

The installer, manifest, and downloaded skills are untrusted plain text. The
installer and maintenance instructions accept remote files only from the exact
`https://grumpydev.ai` origin and require rejecting a redirect outside that
origin. They require project-local setup, `gd-` specialist names, and inspection
of an existing destination before replacement. When an agent harness needs a
project instruction to discover GrumpyDev, the installer tells the agent to add
one marked routing block that points to the local entrypoint and preserves all
surrounding instructions. The block says that a missing entrypoint must remain
inert and must not trigger an automatic download.

GrumpyDev defines no installation receipt, state database, lockfile, or
ownership database. For an explicit update or removal request, the maintenance
skill instructs the agent to inspect the actual local files. It requires the
agent to show and ask before replacing a local file whose contents differ from
the fetched replacement or touching an ambiguous target. It limits removal to
confirmed GrumpyDev files, `.grump`, a confirmed local manifest when present,
GrumpyDev-only directories, and the contents of bounded GrumpyDev routing
blocks.

## Disclosure

Allow the maintainers a reasonable opportunity to investigate and prepare a
fix before public disclosure. No response deadline or bounty is promised.
