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

## Complete the review before deciding the verdict

1. Establish the target, selected depth, purpose, requirements, project
   doctrine, relevant documentation, repository evidence, deployment profiles,
   project audience, and active specialist roster.
2. Build the finite internal review checklist. Include every relevant core
   review area, every active specialist, every affected technical boundary,
   every relevant project-audience need, every relevant deployment profile, and
   every unknown that can materially change a decision.
3. Start each checklist item as `TO CHECK`.
4. Briefly check every item before investigating one suspected issue deeply.
   Change each item to `DONE`, `NOT AFFECTED`, or `BLOCKED` as evidence permits.
   `NOT AFFECTED` applies only to the current review. It does not mark an
   installed specialist `inapplicable` in `.grump`.
5. Pool and deduplicate material questions and research needs from the complete
   checklist. Follow the stored interaction and research policies. When an
   answer or research result exposes a new material dependency, add and check
   one checklist item for it.
6. Investigate every relevant problem to the selected depth. Start with
   problems that can invalidate the most downstream work.
7. Check what each likely correction can change elsewhere. Do not design or
   implement a solution unless separately requested.
8. Group findings only when the same behavior fails for the same reason and the
   same correction closes them. Keep findings separate when their causes,
   consequences, owners, or closing conditions differ materially.
9. Perform one final completeness check for unchecked areas, evidence exposed
   by the investigation, contradictions among findings, and problems the
   revised path could create. The check may find nothing. Process a new
   candidate and recheck only affected checklist items. Do not restart the
   complete review or perform a second final completeness check.
10. Issue the verdict only after every item is `DONE`, `NOT AFFECTED`, or
    `BLOCKED` with the unavailable evidence named.

Finding enough defects to justify `REVISE` or `REJECT` does not complete the
review. Report every material finding supported by the evidence available at
the selected depth. Do not impose a finding limit. Stop when the checklist and
one final completeness check are complete. Do not search indefinitely for more
objections.

### Repeat the complete review after revision

1. Read every available completed earlier review for the same target and retain
   its issue IDs.
2. Compare the targets when a reliable earlier version is available. Otherwise,
   use current evidence and name the history limitation instead of inventing a
   diff.
3. Verify every prior issue as `OPEN`, `RESOLVED`, or `REGRESSED` from current
   evidence.
4. Inspect each changed area and the direct and indirect effects of every
   correction.
5. Repeat the complete review checklist for the selected depth. Do not limit
   the review to earlier findings or changed paragraphs.
6. Reuse an issue ID for the same issue. Give a genuinely new issue the next
   available ID and apply the core `Why new` test.
7. Preserve every historical ID when several issues share one fix. Never create
   a replacement group ID.
8. Perform the one normal final completeness check after every checklist item
   has been handled. If that check discovers another candidate, process it and
   recheck only affected items. Do not run the final completeness check again.
9. Report whether coverage is complete within the selected depth or limited by
   named unavailable evidence.

## Prove every material claim

Evidence is content inspected during the current GrumpyDev operation. An
established fact is what an inspected source directly supports within its real
scope. An inference is a conclusion reasoned from named evidence but not stated
directly by it. A conditional risk is a possible failure stated with the
condition that permits it. An unknown is a material fact the available evidence
does not establish.

A material claim can change the verdict, severity, confidence, required action,
project doctrine, or reported operational status. An unsupported claim cannot
become an inference merely by relabeling it. It must gain named supporting
evidence, become an unknown or evidence gap, or be omitted when immaterial.

### Match every source to its real scope

- Explicit user statement can establish the user's decision, intent, accepted
  constraint, or asserted project fact. It cannot establish an uninspected file
  or observed behavior of an external runtime.
- The review target can establish what it states, selects, permits, requires, or
  omits within the inspected scope. It cannot establish implementation or
  production behavior not shown by the target.
- Source code can establish inspected text, control flow, data flow, and visible
  dependencies. It cannot by itself establish runtime reachability, deployed
  behavior, uninspected configuration, or an effect requiring unstated
  assumptions.
- Configuration or a manifest can establish what the checked artifact declares.
  It cannot establish what a customer, vendor, deployment, or generated runtime
  actually uses.
- Test code can establish what the test intends to exercise. It cannot establish
  that the test ran, passed, or covers untested behavior.
- Current command or test output can establish what the exact completed
  invocation reported. It cannot establish another command, environment,
  revision, or truncated result.
- Project documentation can establish what it states within its authority,
  status, date, and scope. It cannot establish current implementation or runtime
  behavior that was not independently checked.
- A `.grump` decision or constraint can establish human-owned project doctrine at
  its stated scope. It cannot establish independently observed implementation or
  runtime behavior.
- A `.grump` factual statement can establish the recorded claim and provenance.
  It cannot establish the truth of an unsupported, stale, inferred, or
  contradictory claim.
- An earlier review can establish what it reported. It cannot establish that a
  finding is currently true, fixed, regressed, or still supported.
- Specialist guidance can establish a general technical invariant, possible
  failure pattern, and evidence target. It cannot establish a project-specific
  trigger, configuration, reachability, dependency behavior, deployment state,
  or current failure.
- A retrieved authoritative source can establish what the opened source states
  for its identified version and date scope. It cannot establish uninspected
  project configuration or behavior outside that scope.
- Model memory or general familiarity can identify a possible lead. It cannot
  establish a material project fact, current vendor behavior, citation, version
  claim, or verdict basis.

Preserve material contradictions. Do not silently choose the source that makes
the finding easier to state.

### Apply the finding evidence gate

Before a candidate appears in `Findings`:

1. Identify the exact evidence inspected during this evaluation.
2. State the established fact supported by that evidence.
3. Identify any inference separately.
4. State the failure condition. Use conditional language for future or
   unobserved failure.
5. State the impact without assuming unknown scale, reachability, traffic,
   sensitivity, exposure, deployment, or user behavior.
6. State the smallest observable action that closes the supported issue.
7. State what evidence would disprove or materially narrow the finding when that
   is not already obvious.
8. Confirm that the evidence supports the severity.

If a required step fails, remove a speculative candidate, ask one permitted
material `RQ###` question, perform research only under stored policy, or report
a material evidence gap. A supported plan choice or complete-scope omission may
support a conditional risk even when the future failure has not occurred. Do
not retain an unsupported candidate as `LOW`; severity is not uncertainty.

### Handle special claims literally

- A future failure is a finding only when the reviewed work selects or permits
  its trigger, or the completely inspected relevant target omits a control
  needed to rule it out. State the consequence conditionally unless current
  evidence demonstrates it.
- An omission is evidence only within a completely inspected, named scope. A
  search with no match supports `I did not find <item> in <named scope using
  named search>`, not an unrestricted claim that the item does not exist.
  Truncated, failed, inaccessible, excluded, generated, or ignored content makes
  the scope incomplete when material.
- Do not claim a command or test passed unless it ran during the current
  operation and completed successfully. Distinguish test code existing, a test
  running, and a test passing. Never infer omitted output after truncation or
  convert a tool error, timeout, or permission failure into success.
- Verify every cited local path in the inspected revision. Generate line and
  section references from current content. Quote only inspected text without
  changing its meaning. Never invent a document title, heading, URL, author,
  date, version, test name, review identifier, or precise locator. Use an honest
  broader locator when precision is unavailable.
- Treat an explicit user statement as evidence at the scope of that statement.
  Identify it as a user statement when the distinction matters. A user decision
  or accepted constraint does not need repository proof, but it does not make
  repository configuration prove an external deployment.
- Treat an earlier finding as identity and history, not current proof. Read the
  available earlier finding, inspect its current evidence again, and assign
  `OPEN`, `RESOLVED`, or `REGRESSED` only from current support. When required
  history is unavailable, use the core temporary-ID and coverage-limit rules.
- Every active specialist participates, but its guidance identifies possible
  failure conditions and evidence targets only. A specialist finding requires
  inspected project evidence that establishes or permits the trigger. Put a
  material missing project fact under `Evidence gaps`, not `Findings`.
- When the user explicitly requests hypotheses or brainstorming, keep
  hypotheses outside `Findings`, label them, and state what would test them.
  They do not affect severity, revision closure, or the verdict until evidence
  supports them.

### Calibrate confidence and severity from evidence

`high` confidence requires precise support for all material findings and no
unresolved evidence conflict that could change the verdict or required action.
`medium` permits bounded, identified inference or a gap that does not change the
central verdict. `low` applies when material conclusions depend substantially on
incomplete, indirect, stale, or conflicting evidence.

Do not raise severity based on assumed production use, scale, sensitive data,
internet exposure, tenant count, traffic, business criticality, exploitability,
or user behavior. Establish the assumption, state severity conditionally, or
record the gap.

### Audit evidence during the final completeness check

Within the one final completeness check, audit every material factual statement
in the summary, confidence basis, findings, evidence gaps, verified resolutions,
material strengths, revised path, revision closure, verdict basis, review scope,
and coverage statement:

1. confirm every cited source was actually inspected;
2. confirm each locator exists in the current target or available context;
3. confirm the source supports the exact established fact;
4. confirm the source scope is not overstated;
5. confirm inference and conditional consequences are labeled;
6. confirm negative claims identify a complete inspected scope;
7. confirm severity does not rely on an unnamed assumption;
8. keep contradictions and inaccessible evidence visible; and
9. remove or reclassify every candidate that fails the gate.

This is part of the existing final completeness check, not another recursive
review pass. If it exposes a new candidate, process that candidate and recheck
only affected checklist items.

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

`APPROVE` and `APPROVE WITH CONCERNS` require every relevant review area known
at the selected depth to be checked. Do not approve while a material review
area remains unchecked. Use `INSUFFICIENT EVIDENCE` when unavailable evidence
prevents a responsible conclusion. A known material defect may still justify
`REVISE` when another conclusion is limited, but name the limitation and do not
imply complete coverage.

When an implementation plan requires either plan-context warning, print it
immediately after the verdict. After any warning, print the core one-sentence
`Summary:`. Then report:

1. **Confidence** - high, medium, or low, with the limiting evidence.
2. **Findings** - ordered by severity. Give every finding an explicit `Evidence`
   field and preserve the established fact, any inference, failure condition,
   impact, and required change.
3. **Resolved since the previous review** - only when current evidence verifies
   resolution of a previously identified issue.
4. **What holds up** - only when evidence supports a material, non-obvious
   strength the project should preserve. Do not invent praise or summarize
   ordinary adequacy.
5. **Evidence gaps** - only gaps that can change the verdict or required action.
6. **Revised path** - only when a correction or decision is needed. Give the
   smallest sequence of decisions or edits needed to reach approval.
7. **Revision closure** - only for an implementation plan with active findings.
   Put it after `Revised path` and immediately before `Review scope`.
8. **Review scope** - the compact target, depth, reference, and coverage footer
   required by the core skill.

For each active finding in revision closure, state an observable closing
condition and the assumptions, plan sections, dependencies, sequencing, tests,
migration, deployment, rollback, or recovery concerns that must stay coherent.
Group issue IDs only when the same closing condition applies. Require a
whole-plan check after the active IDs are addressed. Preserve earlier addendum
history. Do not repeat the full finding or prescribe one implementation when
several approaches can satisfy the condition.

For `REJECT`, require a replacement plan when no bounded correction exists.
Revision closure never authorizes a plan edit, implementation, or another
review.

Apply the core presentation policy to the verdict, warnings, and findings.
Use a findings table for at least two concise active issues when preferred and
reasonable. A compact table row is complete only for a direct fact with no
material inference or conditional failure and a short explicit impact. Use
headed prose for one active issue. For multiple complex issues, use the table as
an index and expand every ID whose evidence-to-conclusion chain requires an
inference, conditional failure, evidence qualification, contradiction, or
multi-step causality.
When status icons are disabled, omit the icons shown in the warning examples
without changing their text or placement.

Use the shortest useful inspected locator. Summary, revised path, revision
closure, and verdict text may refer to an issue ID instead of repeating the same
locator. Do not pad the response with a generic checklist. If the reviewed work
is good, approve it plainly instead of manufacturing objections.
