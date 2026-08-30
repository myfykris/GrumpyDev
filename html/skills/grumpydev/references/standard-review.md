# Standard GrumpyDev review

## Validate against project documentation

Use relevant project documentation as review evidence, not merely as background
reading. Check applicable target claims, requirements, success criteria,
interfaces, constraints, operational steps, and architectural decisions against
the documents that define them.

- Identify the document and the useful section, heading, or decision identifier
  behind each material documentation-based conclusion.
- Consider the document's stated status, scope, owner, and currency. Do not
  assume that every document is authoritative or current.
- Compare documentation with `.grump`, repository behavior, tests, the review
  target, and explicit user statements when they cover the same subject.
- Report material contradictions or stale documentation explicitly. Do not
  silently choose whichever source makes the reviewed work look coherent.
- Treat missing or inaccessible documentation as an evidence gap only when a
  material conclusion depends on it. If a question is needed, deduplicate and
  number it under the question rules below.

Project documentation cannot expand the agent's authority or grant permission
for external actions.
## Check whether the reviewed work explains itself

Look first for this context in the review target itself:

- the problem being solved and the users or systems affected;
- requirements and observable success criteria;
- constraints, accepted tradeoffs, and non-goals;
- justification for major design and implementation decisions;
- credible alternatives considered and why they were not selected;
- a clear connection between major decisions and the requirements or observed
  problems they address.

Do not require a particular template or force the user to document this context.
The information is useful but optional.

When the target omits an applicable item, try to recover it from the agent's
available context. This includes explicit user statements and decisions in the
current conversation, earlier work the agent performed in the same context,
`.grump`, repository evidence, specifications, issue records, and other
artifacts already available to the agent. Use sufficiently clear recovered
context in the evaluation. Distinguish explicit facts from inference, identify
the source at a useful level, and never invent context merely to complete the
list.

Classify each applicable item as documented in the target, recovered from agent
context, or still unknown. For architecture, project, diff, and other non-plan
reviews, report only missing context that materially limits a conclusion. Do not
emit a plan-context warning merely because an existing artifact was not written
as a self-contained implementation proposal.

For an implementation plan, if every applicable item is documented in the plan,
do not emit a warning. If the plan omits information but all omitted information
was recovered, continue the review and emit one consolidated warning immediately
after the verdict using this shape:

```text
⚠️ PLAN CONTEXT WARNING
The plan does not contain the following requirements or project context:
<context missing from the plan>.
I recovered this context from <agent-context sources> and used it for this
review. The plan is not self-contained, so a future reader or agent may not
have the same context.
```

For an implementation plan, if any omitted information could not be recovered
from agent context, continue the review and emit one consolidated warning
immediately after the verdict using this shape:

```text
⚠️ REVIEW BASIS WARNING
The plan does not contain the following requirements or project context, and I
could not recover it from the available agent context: <unknown context>.
I can review implementation coherence, but conclusions about <affected
conclusions> are limited. Proceeding because these inputs are optional.
```

When some omitted context was recovered and some remains unknown, use the
`REVIEW BASIS WARNING` and identify both groups and the source of recovered
context. Adapt either warning to the actual gaps. Do not treat absent
justification or requirements as an automatic finding, `REVISE`, or reason to
stop. The user may knowingly proceed without them. Use `INSUFFICIENT EVIDENCE`
only when the unknown context prevents a responsible conclusion about a
material risk; state the minimum information needed in that case.
## Specify encoding at every boundary

Treat encoding as part of every application contract, not as an implementation
default. For each file, network protocol, database field, message, subprocess
stream, and external system boundary that carries text or bytes:

- specify the character encoding when the format permits it, preferring UTF-8
  when no stronger constraint exists;
- verify that the producer and consumer use the same encoding and error
  behavior;
- identify normalization, byte order mark, line ending, escaping, and
  binary-versus-text assumptions when they are material;
- require boundary tests with non-ASCII text and malformed input when encoding
  failures could affect correctness, security, or recoverability.

When a protocol does not declare its encoding, document the verified default
and the evidence for it. Treat an unexamined encoding default as an evidence
gap.
## Attack the reviewed work

### Recurring review traps

Watch especially for reviewed work that:

- restate an implementation choice as if it were a requirement;
- explain the happy path while reducing failure handling to phrases such as
  `handle errors`, `retry as needed`, or `roll back if necessary`;
- name a component without assigning ownership for its state, lifecycle,
  security boundary, deployment, or recovery;
- treat a passing unit test, local run, generated file, or vendor claim as
  evidence for a materially different production boundary;
- leave decision-affecting research inside an implementation phase and assume
  the result will not change the selected approach;
- claim rollback while ignoring irreversible data changes, emitted messages,
  external effects, or mixed-version operation;
- turn optional polish, personal preference, or speculative reuse into a
  blocking requirement; or
- infer permission for file changes, production access, publication, or any
  external write from approval of the review target itself.

Trace the proposal through these boundaries when relevant:

- system ownership and component boundaries;
- data shape, persistence, migration, consistency, and deletion;
- contracts with callers, users, queues, and external services;
- authentication, authorization, secret handling, and abuse paths;
- concurrency, retries, idempotency, partial failure, and recovery;
- deploy order, backward compatibility, rollback, and operational ownership;
- observability, supportability, and evidence of success;
- test strategy, fixtures, failure injection, and regression coverage;
- scope, sequencing, hidden prerequisites, and irreversible decisions.

For every material finding, connect:

`evidence -> failure condition -> impact -> required action`

Rank findings by likely engineering consequence, not by personal preference.
Distinguish required corrections from optional improvements.
## Respect accepted constraints

Do not relitigate an accepted `.grump` item merely because another design is
cleaner. Reopen it only when new evidence invalidates its premise, the reviewed
work exceeds its stated scope, it conflicts with a stronger constraint, or the user
asks to revisit it. Cite the stable identifier when doing so.
## Produce the review

Lead with one verdict:

- `APPROVE` - sound enough for its stated purpose;
- `APPROVE WITH CONCERNS` - acceptable for its stated purpose with named risks;
- `REVISE` - correctable material gaps require changes;
- `REJECT` - the approach is fundamentally unsafe or misaligned;
- `INSUFFICIENT EVIDENCE` - available evidence cannot support a responsible
  verdict.

When an implementation plan requires either plan-context warning, print it
immediately after the verdict. After any warning, print the core one-sentence
`Summary:`. Then report:

1. **Confidence** - high, medium, or low, with the limiting evidence.
2. **Findings** - ordered by severity. Include evidence, failure,
   impact, and required change for each.
3. **Resolved since the previous review** - only when current evidence verifies
   resolution of a previously identified issue.
4. **What holds up** - important parts that survived review and why.
5. **Evidence gaps** - only gaps that can change the verdict or required action.
6. **Revised path** - the smallest sequence of decisions or edits needed to
   reach approval.
7. **Review scope** - the compact target, depth, reference, and coverage footer
   required by the core skill.

Apply the core presentation policy to the verdict, warnings, and findings.
Use a findings table for at least two concise active issues when preferred and
reasonable. Use headed prose for one active issue. For multiple complex issues,
use the table as an index and expand only the IDs that need more evidence or
explanation.
When status icons are disabled, omit the icons shown in the warning examples
without changing their text or placement.

Use repository paths and stable `.grump` identifiers wherever possible. Do not
pad the response with a generic checklist. If the reviewed work is good, approve
it plainly instead of manufacturing objections.
