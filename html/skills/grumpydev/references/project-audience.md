# Review for the project audience

Apply this reference to the intended recipients of the reviewed project's
output. Do not apply it to GrumpyDev's own review prose or assume that the
developer requesting the review is the project audience.

## Establish the audience at the point of use

Identify each materially affected audience from project documentation,
`.grump`, explicit user statements, existing product behavior, research,
support evidence, analytics, or other repository evidence. Do not invent a
generic persona to fill a gap.

For each affected audience, establish only what the review needs:

- what they are trying to learn, decide, or accomplish;
- what they can reasonably know before encountering the output;
- the vocabulary, domain knowledge, permissions, devices, and constraints that
  materially shape the experience;
- where they encounter the output and what they need before and after it; and
- what a successful outcome looks like from their perspective.

Judge the output at its actual point of use. Knowledge available to the
developer, implementation agent, internal team, or author is not automatically
available to the recipient. When multiple audiences have materially different
goals or knowledge, do not flatten them into one fictional average user.

## Require copy to communicate

Audience-facing copy must communicate the intended meaning to its recipient.
Check headings, labels, instructions, descriptions, calls to action, errors,
empty states, confirmations, notifications, generated content, documentation,
and help text as applicable.

Flag copy when it:

- depends on project history, internal terminology, unstated prerequisites, or
  surrounding context the recipient does not have;
- uses vague claims, generic praise, fashionable abstractions, unsupported
  promises, or polished filler instead of saying what the thing does;
- describes internal implementation when the recipient needs an outcome,
  consequence, choice, or next action;
- hides an undecided product requirement behind plausible-sounding prose;
- repeats information without improving comprehension or action; or
- uses a tone, vocabulary, reading level, or amount of detail that conflicts
  with evidence about the intended recipient.

Do not enforce a mechanical banned-word list. A technical term is appropriate
when the audience knows it and it is the clearest term. A simple word is still
bad when the statement remains vague. Judge whether the copy does useful work.

For errors and blocked states, require enough information for the recipient to
understand what happened, what remains safe or uncertain, and what they can do
next when a next action exists. Do not expose sensitive implementation details
merely to make an error sound specific.

## Require the right structure

Evaluate the inventory and organization of audience-facing artifacts before
polishing individual sentences. This includes pages, screens, routes, sections,
navigation, task flows, forms, messages, documentation topics, and content
grouping.

Check whether:

- each artifact exists for a real audience need rather than an internal org
  chart, implementation boundary, template slot, or generated-site convention;
- every material audience task has a discoverable place and path;
- grouping, labels, hierarchy, sequence, and navigation match how recipients
  seek information and complete work;
- prerequisites appear before decisions or actions that depend on them;
- secondary detail is available without obscuring the primary task;
- redundant, misplaced, or unnecessary artifacts are removed or consolidated;
  and
- changes account for affected entry points, links, search, saved locations,
  help, support, and recovery paths when material.

A perfectly accurate and well-written page is still wrong when the project
audience does not need the page. Likewise, strong copy on existing pages does
not compensate for a missing page, task, state, or path. Require the structural
correction before treating copy polish as sufficient.

## Review the complete experience

When relevant, also evaluate:

- whether actions, consequences, defaults, progress, completion, and system
  state are apparent to the recipient;
- whether failure, cancellation, correction, and recovery paths are usable;
- whether accessibility, input method, display size, localization, and content
  expansion assumptions exclude part of the established audience;
- whether permissions or audience segmentation expose the wrong content or
  hide required content; and
- whether persuasive design, defaults, or omissions work against the
  recipient's informed interests without an explicit and defensible reason.

Do not demand formal user research for every change. Require stronger audience
evidence when a high-impact or hard-to-reverse structural decision depends on
an unverified assumption. Treat a material unknown as an evidence gap or ask a
deduplicated `RQ###` question according to the stored interaction policy.

## Write actionable findings

Connect each material audience finding as:

`evidence -> recipient mismatch -> failed task or consequence -> required change`

Name the affected audience and distinguish content defects from structural
defects. A concrete replacement phrase can clarify a copy finding, but sample
copy does not replace the requirement or repair an information-architecture
problem. Do not block work over personal taste when the content and structure
serve the established audience.
