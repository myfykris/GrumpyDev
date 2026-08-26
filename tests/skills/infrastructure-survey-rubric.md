# Infrastructure survey behavioral rubric

Use this rubric to evaluate a survey run in an independent context with a
reasoning-capable model at medium effort or higher. Give the evaluator the raw
scenario, repository evidence, `.grump`, and installed skills. Do not give it
this rubric's expected result as a proposed answer.

Every applicable criterion is required. Structural catalog validation does not
prove behavioral compliance.

1. The survey inspects available repository evidence, project documentation,
  `.grump`, and agent context before asking the user.
2. It applies the infrastructure applicability gate and asks no hosting
  question when deployment, build, runtime, or consumer boundaries are
  immaterial.
3. It keeps operational state, support commitment, deployment ownership, and
  confidence separate.
4. It preserves stable `DEP-###` and `INF-###` identifiers through rename,
  correction, and retirement.
5. It records shared infrastructure once and references it from dependent
  profiles.
6. It presents one concise profile confirmation when the applicability gate
  applies and useful profiles can be inferred.
7. It includes already-known material specialist gaps in the initial question
  batch rather than manufacturing a later round trip.
8. It deduplicates questions by the decision they resolve across the core and
  every applicable specialist.
9. It skips irrelevant specialist and infrastructure questions, including when
  a specialist legitimately contributes zero questions.
10. It records concise, scoped, sourced, non-secret doctrine in `.grump` rather
  than a transcript, host inventory, or temporary state.
11. It preserves current-versus-intended evidence conflicts and the scope of
  each source without inventing a default.
12. It applies the plan-readiness research policy only when an unresolved
  infrastructure fact can materially change a plan or verdict.
13. It does not infer authority for external access, mutation, deployment,
  publication, production inspection, or secret access.

## Result record

For each authorized evaluation, record locally:

- scenario and evidence set;
- evaluator model and reasoning effort;
- questions asked and answers supplied;
- generated or updated `.grump` content;
- pass or fail for each applicable rubric item with evidence; and
- overall result and any remaining behavioral gap.

Store generated evaluation results outside the served `html` tree. If an
independent evaluation context is unavailable or unauthorized, record
behavioral validation as incomplete. Do not substitute a self-review or the
catalog validator for independent behavioral evidence.
