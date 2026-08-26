---
name: web-accessibility
description: Review web-accessibility plans for semantic structure, keyboard use, focus, names, contrast, motion, forms, live updates, and assistive-technology evidence. Use when a plan creates or changes user-facing web interfaces.
---

# Web accessibility plan review

Apply this guidance alongside the core GrumpyDev review and the relevant web
framework skill.

## Inspect evidence

- Read rendered HTML, interaction states, forms, routing, CSS, content, error
  handling, automated checks, and manual keyboard and screen-reader results.
- Trace a task using keyboard only, zoom, reduced motion, high contrast, a
  screen reader, validation errors, loading, and dynamic updates.

## Establish the operating model

Establish the project target: Accessibility target and standard, browser and
assistive-technology matrix, input methods, localization, design-system
constraints, test tooling, and exception process. The changed boundary must
define: Semantic structure, keyboard behavior, focus, names and roles, forms,
errors, contrast, motion, zoom, dynamic updates, media, and assistive testing.

Name the identity, trust, configuration, capacity, failure-domain, deployment,
and operational owners for Semantic structure, keyboard behavior, focus, names
and roles, forms, errors. Prove contrast, motion, zoom, dynamic updates, media,
assistive testing through rotation, overload, partial rollout, drain, forced
stop, rollback, and recovery.

## Challenge the plan

### Recurring traps

Watch especially for generic elements imitating native controls, keyboard focus
lost after updates, meaning conveyed only by color or position, ARIA overriding
correct native semantics, dynamic changes never announced, focus traps, and
layouts that fail under zoom or text enlargement.

- Prefer native elements and semantics; ARIA does not repair a div that behaves
  like a broken button.
- Require logical focus order, visible focus, safe focus movement, escape
  behavior, and no keyboard traps in every interactive state.
- Verify accessible names, headings, landmarks, labels, instructions, error
  association, status announcements, and route-title updates.
- Test contrast, zoom and reflow, target size, color independence, reduced
  motion, captions, and content at realistic lengths.
- Use automated checks as a floor, then require manual keyboard and
  representative assistive-technology evidence for critical flows.

## Verify the claims

- Verify these behaviors through the effective Web accessibility configuration
  and runtime topology: Semantic structure, keyboard behavior, focus, names and
  roles, forms, errors. Use effective rendered configuration and deployable
  artifacts in a representative identity, topology, capacity, and policy
  boundary.
- Exercise failure and edge behavior for: contrast, motion, zoom, dynamic
  updates, media, assistive testing. Exercise startup, readiness, normal load,
  overload, dependency loss, rotation, graceful drain, forced stop, failover,
  and recovery where applicable.
- Rehearse rolling change, interruption, rollback, and restoration while old and
  new components or long-lived work coexist.

## Ask when evidence is missing

- Which changed interactions must work by keyboard, screen reader, zoom, reduced
  motion, and high-contrast settings?
- How are focus, accessible names, errors, live updates, and semantic
  relationships verified?

## Calibrate findings

- Treat a blocker that prevents a user from completing a core task or receiving
  critical information as critical.
- Downgrade when the component is non-interactive or tested platform semantics
  already provide the required behavior.

## Add to the verdict

State semantic and keyboard behavior, focus management, name and error
contracts, visual accommodations, and manual evidence.
