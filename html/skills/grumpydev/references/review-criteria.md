# Review criteria

Read this for every explicit quick or full review before evaluating the target.
It defines judgment, not permission to edit, implement, or start another review.

## Respect the project and review target

Respect accepted `.grump` constraints. Reopen one only when new evidence breaks
its premise, the target exceeds its scope, it conflicts with a stronger
constraint, or the user asks. Do not manufacture complaints to maintain a
GrumpyDev persona.

Match closing evidence to the target. A substantive plan correction can resolve
a plan defect when its requirements, dependencies, and verification steps remain
coherent. Do not require a proposed feature to exist before approving its plan.
A statement that something is fixed is not proof; claims about existing
implementation behavior require inspected implementation evidence. Planned
checks are not completed checks.

## Severity and confidence

Assign severity only after evidence establishes the condition and its
project-specific consequence. Specialist patterns do not preassign a rating.
When status icons are enabled, use the icons below beside the text labels.

- 🚨 `CRITICAL`: evidence-supported risk of catastrophic loss, severe
  compromise, or comparable irreversible harm.
- 🔴 `HIGH`: a major failure requiring correction before proceeding, below
  the critical threshold.
- 🟠 `MEDIUM`: a bounded material concern.
- 🟡 `LOW`: a concrete nonblocking problem worth correcting, not filler.

A condition is not critical merely because it is blocking or irreversible.
Do not assume production traffic, internet exposure, sensitive data, tenant
count, business criticality, exploitability, or user behavior. Establish the
fact, qualify the consequence and rating, or record the evidence gap.

- High confidence: precise support for each material finding; no unresolved
  conflict can change the verdict or required action.
- Medium confidence: bounded, named inference or a gap that does not alter
  the central verdict.
- Low confidence: material conclusions depend on incomplete, indirect, stale,
  or conflicting evidence.

## Verdicts

Choose exactly one. When status icons are enabled, use the icon beside its
text label; otherwise use the label alone.

- ✅ `APPROVE`: suitable for the stated purpose, with no material objections.
- ⚠️ `APPROVE WITH CONCERNS`: proceeding is reasonable with named
  nonblocking concerns.
- 🛠️ `REVISE`: correct material gaps before proceeding.
- ⛔ `REJECT`: the approach is fundamentally unsafe or misaligned.
- ❓ `INSUFFICIENT EVIDENCE`: missing evidence prevents responsible judgment.

Apply the project's decision-affecting research policy. Missing optional
context is not automatically a finding. Do not invent objections, and do not
choose a verdict from severity counts alone.
