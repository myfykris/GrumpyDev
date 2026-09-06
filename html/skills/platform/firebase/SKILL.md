---
name: firebase
description: "Use only when the user explicitly asks for a GrumpyDev review. Never start a review automatically. If installed and not marked inapplicable, use this skill in every GrumpyDev review. Review Firebase engineering work for Security Rules, identity, client trust, Firestore consistency, offline writes, Cloud Functions, Storage, indexes, quotas, and deployment."
---

# Firebase GrumpyDev review

Apply this guidance alongside the core GrumpyDev review and the `application-security`,
`distributed-systems` and `schema-evolution` skills.

## Invocation and participation boundary

This specialist cannot start a GrumpyDev review.

Use this skill in every explicitly requested GrumpyDev review when it is
installed and `.grump` does not explicitly mark it `inapplicable`.

Check direct and indirect effects even when the reviewed target does not name
or modify this technology. Produce no finding when there is no material effect.

## Lean review

- Read Firebase products, SDK and rules versions, project aliases, emulator configuration,
  indexes, functions, and deployment files.

- Trace user identity, custom claims, App Check, Security Rules, Admin SDK use, service
  accounts, and tenant boundaries.

Watch especially for open development rules reaching production, broad
overlapping rules granting access, Admin SDK endpoints without equivalent
authorization, custom claims remaining stale, offline writes resolving
last-write-wins, and triggers repeating non-idempotent effects.

Lean mode is insufficient when this material severity condition may apply:

- Treat open rules, tenant-crossing access, exposed service accounts, or privileged Admin
  endpoints without authorization as critical.

## Load local references

When this entrypoint identifies a plausible direct or indirect material effect
during a standard or deep review, or whenever lean evidence or escalation
conditions leave a material uncertainty, read
[review.md](references/review.md). It
contains the complete Firebase evidence, operating model, failure, verification,
question, and calibration guidance. Never load `SURVEY.md` during an ordinary
review.

## Add to the verdict

State products, project separation, rule and identity boundaries, data and query model, offline
policy, trigger safety, and deployment evidence.
