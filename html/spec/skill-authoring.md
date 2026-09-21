# GrumpyDev specialist skill authoring

Version 1

A specialist skill adds domain judgment to an explicitly requested GrumpyDev
review. It is not a tutorial, independent reviewer, executable plugin, or
replacement for the core evidence rules.

## Complete skill shape

Each published specialist directory contains:

```text
skills/<type>/<subject-slug>/
  SKILL.md
  SURVEY.md
  references/
    <focused-guidance>.md
```

Its manifest and frontmatter name is `gd-<subject-slug>`. Installation places
the complete skill in an immediate directory with that namespaced name. The
clean published path and the namespaced installed identity are deliberately
different.

Every file is plain Markdown encoded as UTF-8 with LF line endings and a final
newline. A skill may have one broad `references/review.md`, several focused
references, or both. Add a reference only when a clear trigger lets the agent
avoid loading it for unrelated reviews.

Installation copies every manifest-listed file for an approved skill. Runtime
progressive disclosure controls which local references a review reads. A
reference must never require a later download.

## `SKILL.md`

Use YAML frontmatter with exactly the canonical `gd-` skill name and a concise,
discriminating description. Every specialist description must contain this
exact activation boundary:

```text
Use only during an explicitly requested GrumpyDev review when this installed specialist is applicable. Never start or continue a review automatically.
```

Follow it with the domain and the material engineering boundaries the skill
reviews. The safeguard is intentionally repeated in every specialist because
an agent harness may discover that entrypoint before the core skill.

The body should usually be 100 to 250 words and contain only judgment needed
whenever the specialist participates:

- what a direct or indirect effect means in this domain;
- the smallest useful quick-review inspection path;
- domain-specific assumptions and failure patterns that commonly mislead a
  reviewer;
- exact evidence triggers for each local reference; and
- any domain-specific fact that must be named in the verdict.

Do not repeat the core invocation policy, active-specialist definition,
evidence contract, checklist procedure, severity rules, output format, or
generic direct-versus-indirect boilerplate in the body. Do not use vague routes
such as `read this for more detail`. State the boundary that triggers the file.

Guidance identifies possible failures and evidence targets. It is never proof
that the current project contains the trigger. Phrase version-dependent or
configuration-dependent behavior conditionally and tell the reviewer what to
inspect.

## `SURVEY.md`

The survey companion contributes project facts that materially change later
domain judgment. It does not run during an ordinary review. Keep it focused on:

- repository or documentation evidence to inspect before asking;
- versions, runtime modes, ownership, deployment, compatibility, or other
  durable facts that change the specialist's conclusions;
- question candidates only for facts evidence cannot establish; and
- concise mapping into the canonical `.grump` sections.

Do not repeat global survey invocation, numbering, deduplication, safe-write,
deployment-profile, or doctrine-format rules. Do not ask tutorial questions or
record transient environment details, secrets, raw dumps, or a survey
transcript. Most surveys should be 100 to 250 words.

## References

References contain the scar tissue: domain invariants, recurring failure modes,
misleading assumptions, evidence targets, operational traps, and observable
closing conditions. They should challenge technically valid approaches that
remain unsafe or inappropriate in common project contexts.

Remove generic advice a capable agent can reconstruct and any core GrumpyDev
process. Avoid unstable universal claims. When behavior varies by version,
provider, runtime, feature flag, or deployment mode, name that condition and
require evidence from the applicable project or authoritative source.

Keep separate focused references when their triggers are materially different.
Merge files only when nearly every review would load both or a route cannot be
stated precisely. File names must describe the boundary they cover.

## Applicability metadata

The global manifest decides which specialists setup may propose before any
specialist files are downloaded. Each specialist record needs at least one
complete `install_when` condition based on durable project evidence. Add
`do_not_install_when` only for a real exclusion. Do not use one current plan as
the project-level applicability test.

The manifest also owns the human-facing description, ordered display subjects,
skill path, complete ordered file list, and popularity order within its type.
Do not duplicate invocation boilerplate in the catalog description. Every file
record uses only a skill-relative path and one role: `entrypoint`, `survey`, or
`reference`.

## Author review checklist

Before contributing a specialist, confirm:

1. the frontmatter activation boundary is exact, the namespaced name matches
   the manifest, and the clean catalog path matches its type and subject slug;
2. the entrypoint adds domain judgment rather than shared process;
3. every reference route names an observable trigger and resolves locally;
4. the survey asks only material unresolved domain questions;
5. claims distinguish stable invariants from version or configuration details;
6. each failure pattern points to evidence and an observable consequence;
7. the manifest lists every skill file and no unrelated file; and
8. all text uses plain ASCII punctuation unless a project rule expressly
   permits a narrow exception.

The structural validator checks shape, links, manifest coverage, encoding, and
site rendering. It does not certify the technical truth or usefulness of the
guidance. Authors remain responsible for that judgment.
