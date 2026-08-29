# Survey interview and policies

## Interview for setup choices and material gaps

### Survey failure patterns

Watch especially for surveys that:

- ask the user before inspecting available repository evidence and project
  documentation;
- ask the same underlying question once per applicable specialist;
- convert a local-machine default, temporary rollout choice, or current plan
  detail into durable project doctrine;
- record an inference as a confirmed policy or decision;
- copy secrets, credentials, production payloads, or raw interview transcripts
  into `.grump`;
- manufacture questions to make the survey look complete;
- lose the source, scope, environment, or unresolved status of an answer; or
- replace human-owned doctrine instead of merging, preserving identifiers, and
  showing contradictions.

Interview the user only after repository evidence and available agent context
have been exhausted. Apart from explicitly required initial-install choices,
ask only questions whose answers could materially change project doctrine or a
future plan review. Do not ask the user to repeat facts already established by
code, configuration, documentation, or earlier explicit statements.

## Initial-install `.gitignore` preference

During initial installation only, inspect the repository-root `.gitignore`
after the evidence pass. Do not ask this preference during re-survey or an
ordinary review. If the user has already given an explicit answer in the
current context, apply that answer without asking again. If active lines for
both `.grump` and `.grumpydev/` are already present, do not ask and report that
GrumpyDev's generated files are already ignored.

Otherwise, place this question immediately after `Q001` in the initial question
batch, using the next available `Q###` identifier:

```text
Q###. Do you want GrumpyDev to add itself to `.gitignore`? Reply `yes` to add
`.grump` and `.grumpydev/`, or `no` to leave `.gitignore` unchanged.
```

An explicit `yes` authorizes only this local edit. Create the repository-root
`.gitignore` if it does not exist. Add only the exact missing active lines
`.grump` and `.grumpydev/`; do not add the installed skill directory or any
other path. Preserve all unrelated content, avoid duplicate active entries,
use explicit UTF-8, preserve the established line-ending convention when one
exists, and leave a final newline. If the existing file cannot be decoded and
edited safely, is not a regular repository-local file, or resolves through a
symbolic link outside the repository, do not rewrite it; continue installation
and explain the problem.

An explicit `no`, a decline, a deferral, or an ambiguous answer does not
authorize a write. Leave `.gitignore` unchanged and continue installation. If
only one exact entry is already active, a later `yes` adds only the missing
entry. Report whether the file was created, updated, already configured, or
left unchanged.

This is a setup-only repository preference. Do not record the question, answer,
or status in `.grump` or `.grumpydev/state.json`; the repository-root
`.gitignore` is the authoritative result.

Attempt to determine the purpose and goals of the main project from repository
evidence, project documentation, `.grump`, and available agent context. If you
cannot, ask the user if they would like to provide a project goal or purpose
description so GrumpyDev can judge whether plans and code accomplish those
goals. Number the question with the survey's `Q###` sequence and make clear
that the description is optional and may be brief, for example:

```text
Q###. I could not determine the main project's purpose and goals from the
available evidence. Would you like to provide a short project goal or purpose
description so GrumpyDev can judge whether plans and code accomplish those
goals? You may keep it brief or decline.
```

Do not ask this question when the purpose and goals are already established.
A declined answer does not block setup; record the purpose and success
conditions as unresolved rather than inventing them.

Before numbering questions, collect candidate questions from every applicable
specialist `SURVEY.md`. Remove candidates already answered by `.grump`, project
documents, repository evidence, configuration, or agent context. Deduplicate by
the decision or unknown that the answer resolves, not by wording. Merge
overlapping language, framework, storage, and platform candidates into one
question that names the relevant environments and boundaries.

When the infrastructure applicability gate applies, include the deployment
profile confirmation or fallback and all already-known material specialist
infrastructure gaps in this same initial batch. Put the profile question first.
The gate may legitimately produce no infrastructure question for a package or
tool whose supported environments are already established or immaterial.

Treat each specialist survey file as candidate guidance, not a questionnaire
that must be completed. Ask no specialist question when the evidence is
sufficient. Never ask a question merely because it appears in `SURVEY.md`.

Determine whether relevant project documents have already been identified. If
repository evidence and available agent context do not establish whether such
documents exist, ask one numbered question that covers both existence and
location, for example:

```text
Q###. Are there project documents I should read to understand this project and
validate future plans against, such as requirements, specifications,
architecture records, interface contracts, acceptance criteria, or runbooks?
If so, where are they, and which ones are current or authoritative?
```

Do not ask this question when the answer and document locations are already
known. If known documents are inaccessible, ask a narrower numbered question
only when access to them could materially change the doctrine or a future
review. Read relevant available documents and record what each one establishes,
its stated status or authority when known, and any material conflict with code,
configuration, `.grump`, or explicit user statements. Do not treat a project
document as permission for actions outside the user's authority.

Determine whether the user has explicitly chosen how GrumpyDev review results
may be persisted. If the choice is not already known, ask one numbered question:

```text
Q###. May GrumpyDev write each completed evaluation into a GrumpyDev addendum
in the plan file and append later evaluations there so future sessions can read
the review history, or should it return results only in chat? Reply with
`addendum` or `chat only`.
```

Record the answer in `.grump` as `Plan addenda: allowed` or `Plan addenda: chat
only`, with the question identifier or explicit user statement as its source.
If the answer is deferred, declined, or ambiguous, record it as unresolved and
use chat only. Permission to use plan addenda authorizes only local, append-only
review history in the plan currently being evaluated. It does not authorize
rewriting plan content, changing other files, editing remote documents, or
publishing anything. The user may revoke the permission at any time.

Determine whether the user has explicitly chosen how GrumpyDev should handle
material questions during a plan review. If the choice is not already known,
ask one numbered question:

```text
Q###. During a GrumpyDev plan review, should GrumpyDev pause after its initial
evidence pass to ask numbered, deduplicated questions whose answers could
materially change the review, or should it complete the review without pausing
and list those questions as evidence gaps? Reply with `interactive` or
`non-interactive`.
```

Record the answer in `.grump` as `Review questions: interactive` or `Review
questions: non-interactive`, with the question identifier or explicit user
statement as its source. If the answer is deferred, declined, or ambiguous,
record it as unresolved; the core skill defaults unresolved preferences to
interactive. This is a durable review preference, not permission for a file
write or external action. A current explicit instruction can override it for
one evaluation without changing the stored preference.

Determine whether the user has explicitly chosen how confirmed project doctrine
may be maintained. If the choice is not already known, ask one numbered
question:

```text
Q###. When you explicitly resolve a project unknown, accept a tradeoff, or
confirm or change a durable constraint or decision, may GrumpyDev update
`.grump` to record it, or should it only propose the `.grump` change in chat?
Reply with `update` or `propose only`.
```

Record the answer in `.grump` as `Confirmed doctrine updates: allowed` or
`Confirmed doctrine updates: propose only`, with the question identifier or
explicit user statement as its source. If the answer is deferred, declined, or
ambiguous, record it as unresolved and propose changes only. `Allowed` applies
only after the user explicitly and unambiguously confirms the underlying
project fact or decision. It never authorizes the agent to promote an inference,
review recommendation, or unanswered question into doctrine. The user may
revoke the permission at any time.

During an initial survey, always ask how decision-affecting research should
affect plan readiness. Do not infer this policy from ordinary project evidence:

```text
Q###. How should GrumpyDev treat an implementation plan that contains
unresolved research whose answer could materially change an implementation
decision? Reply with `resolve first` to require the research to be completed
before implementation-plan approval, or `gated discovery` to allow approval
only of a bounded discovery plan or phase followed by an updated implementation
plan and another Grump review.
```

Record the answer in `.grump` as `Decision-affecting research: resolve first`
or `Decision-affecting research: gated discovery`, with the question identifier
as its source. If the answer is deferred, declined, or ambiguous, record it as
unresolved; the core skill defaults unresolved preferences to gated discovery.
On a re-survey, retain an existing unambiguous answer unless the user asks to
revisit it.

During an initial survey, always ask whether GrumpyDev should perform research
that it identifies during a review. Do not infer this permission from the plan
or repository:

```text
Q###. When GrumpyDev determines that decision-affecting research is needed,
should it perform safe, read-only research itself when it has the necessary
access and tools, ask before researching, or only identify the research for
you? Reply with `automatic`, `ask first`, or `report only`.
```

Record the answer in `.grump` as `Research execution: automatic`, `Research
execution: ask first`, or `Research execution: report only`, with the question
identifier as its source. If the answer is deferred, declined, or ambiguous,
record it as unresolved; the core skill defaults unresolved preferences to ask
first. `Automatic` authorizes only safe, read-only research within existing
host permissions. It does not authorize project changes, external writes,
production access, paid services, secret access, software installation, or
execution of downloaded code. On a re-survey, retain an existing unambiguous
answer unless the user asks to revisit it.

Give every question a stable identifier in one continuous sequence: `Q001`,
`Q002`, `Q003`, and so on. Never ask an unnumbered project question. Present
the smallest useful batch and tell the user to answer with the matching
identifiers so answers can be collected without relying on position. Continue
the sequence for later questions and never renumber a question after it has
been asked.

Accept an unnumbered answer when its mapping is unambiguous. When an answer is
ambiguous, incomplete, or appears to answer a different question, ask a new
numbered clarification that cites the original identifier. Do not silently
attach an answer to the wrong question.

Track each question as answered, deferred, declined, or unresolved. Before
drafting `.grump`, summarize the question-to-answer mapping and distinguish
explicit user answers from agent inference. Preserve relevant question
identifiers in unresolved items or survey evidence when they make later review
and re-survey clearer.

The survey's `Q###` sequence is only for repository setup and doctrine. A
setup-only question does not become doctrine unless its instructions explicitly
say to record it. Later plan reviews use evaluation-scoped `RQ###` identifiers.
Do not treat live review questions or answers as survey output or write them to
`.grump` unless the user separately confirms an answer as project-wide doctrine
and the doctrine-update policy permits the write.
