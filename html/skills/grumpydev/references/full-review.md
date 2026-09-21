# Full GrumpyDev review

Load this reference only for a full review. It expands the core finite review
and evidence contract. It does not authorize changes to the reviewed work.

## Build one complete checklist

1. Establish the exact target, target type, purpose, requirements, success
   criteria, project doctrine, relevant documentation, project audience,
   deployment boundaries, and active installed specialists.
2. Build a finite checklist from every materially relevant boundary. Include
   ownership and component boundaries; data shape, persistence, migration,
   consistency, deletion, text encoding, normalization, and serialization at
   every application boundary; caller and external contracts; authentication,
   authorization, secrets, and abuse paths; concurrency, retries, idempotency,
   and partial failure; deployment order, compatibility, rollback, and
   recovery; observability and support; tests and failure injection; scope,
   sequencing, prerequisites, and irreversible decisions.
3. Give every active specialist one checklist item. Check direct effects,
   indirect effects through consumers or dependencies, and missing evidence.
   Load a specialist reference only when the entrypoint trigger is established.
4. Start every item as `TO CHECK`. Briefly inspect every item before pursuing
   one suspected issue deeply. End each as `DONE`, `NOT AFFECTED`, or `BLOCKED`.
   `NOT AFFECTED` applies only to this target and does not change project-wide
   specialist status.
5. Pool and deduplicate decision-affecting questions and research needs. Use the
   research-and-questions reference when any exist. Add a checklist item only
   when an answer or research result reveals a new material dependency.
6. Investigate supported candidates to full depth, beginning with issues that
   can invalidate the most downstream work. Check the effects of likely
   corrections without implementing them.
7. Group issues only when the same cause reaches the same consequence boundary
   and the same correction and closing condition resolve all of them.
8. Perform one final completeness and evidence pass. Check for unfinished
   items, contradictions, new evidence exposed by the investigation, and
   problems a proposed correction could cause. Process a new candidate and
   recheck only affected items. Do not restart the review or repeat the final
   pass.
9. Issue the verdict only after no item remains `TO CHECK`. Name the unavailable
   evidence behind every `BLOCKED` item.

## Keep each source within its scope

Evidence is content inspected in the current operation. Apply these limits:

| Source | It can establish | It cannot establish by itself |
| --- | --- | --- |
| Explicit user statement | The user's intent, decision, accepted constraint, or asserted project fact | Uninspected file contents or external runtime behavior |
| Review target | What the target states, selects, permits, requires, or omits within its inspected scope | Existing implementation or production behavior not shown there |
| Source code | Inspected text, visible control and data flow, and declared dependencies | Runtime reachability, deployed configuration, or uninspected callers |
| Configuration or manifest | What the checked artifact declares | What a customer, vendor, generated runtime, or deployment actually uses |
| Test source | What the test intends to exercise | That it ran, passed, or covers another behavior |
| Current command output | What that exact completed invocation reported | Another command, revision, environment, or truncated result |
| Project documentation | What it states within its authority, status, date, and scope | Current behavior that was not independently inspected |
| `.grump` | Human-owned doctrine and the recorded provenance of factual claims | Independent proof that a factual claim remains true |
| Earlier review | What was reported earlier | Current issue state or current proof |
| Specialist guidance | A general invariant, possible failure pattern, and evidence target | That this project contains the trigger |
| Opened authoritative source | What that source states for its version and date scope | Uninspected project configuration or other versions |
| Model memory | A lead worth checking | A material project fact, current vendor behavior, or citation |

Preserve contradictions instead of silently selecting the convenient source.
An omission supports a negative claim only when the complete named scope was
inspected. Otherwise say what was not found in the actual scope.

## Pass every finding through the evidence gate

Before a candidate becomes a finding, record:

1. the exact inspected locator;
2. the established fact that locator supports;
3. any inference, labeled separately;
4. the condition under which failure occurs;
5. the consequence without assuming unknown scale or exposure;
6. the smallest observable required action; and
7. the evidence that would close or materially narrow the issue when it is not
   obvious.

Confirm that the evidence supports the severity. If a step fails, inspect more
evidence, ask one permitted material question, conduct permitted research,
report an evidence gap, or remove the candidate. Uncertainty is not a reason to
retain an unsupported `LOW` finding.

State future failures conditionally unless current evidence shows the failure
already occurs. Verify every cited local path and locator in the current
revision. Never invent a quotation, heading, URL, author, date, version, test,
review ID, or result. Distinguish a command starting from completing, and a test
existing from running and passing.

## Judge the work, not its vocabulary

Watch for proposals that turn a chosen implementation into a supposed
requirement, describe only a happy path, leave ownership undefined, treat local
success as proof of another environment, hide decision-affecting research
inside implementation, claim rollback without reversible data and external
effects, assume encoding instead of specifying it at producer and consumer
boundaries, or make optional polish block delivery.

For a plan, check whether purpose, requirements, success criteria, constraints,
tradeoffs, and reasons for major decisions are present. If missing items are
fully recovered from inspected context, place one concise warning after the
verdict naming what was recovered and from where. If material context remains
unknown, name the affected conclusions and use `INSUFFICIENT EVIDENCE` only
when the gap prevents responsible judgment. These inputs are useful, not a
mandatory plan template.

## Assemble the verdict

Use the shared review criteria and presentation preferences. Every completed
review includes verdict, summary, confidence, findings, and review scope. Add
`Evidence gaps` only for material limitations, `Revised path` only when a
correction or decision is needed, and `What holds up` only for an
evidence-backed strength worth preserving.

For an implementation plan with active findings, add `Revision closure`. Give
each active issue an observable closing condition and identify plan sections,
assumptions, dependencies, sequencing, tests, migration, deployment, rollback,
or recovery concerns that must remain coherent. Require one whole-plan check
after corrections. This does not authorize editing or implementing the plan.

During the final pass, audit every material statement in the summary,
confidence basis, findings, evidence gaps, strengths, revised path, resolution
claims, and scope. Confirm each source was inspected, each locator exists, each
claim stays within source scope, inference and conditional consequences are
labeled, and severity does not depend on an unnamed assumption. Reclassify or
remove anything that fails this audit before issuing the verdict.
