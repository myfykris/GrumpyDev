# Infrastructure question batching behavior

Repository evidence exposes a PHP-FPM web profile behind Nginx and a queue
worker. The PHP, Nginx, background-job, and storage surveys propose overlapping
questions about versions, process ownership, proxy trust, and the database.

Expected behavior:

- Pool every applicable specialist candidate before numbering questions.
- Put the profile confirmation first and include all already-known material
  gaps in the initial batch.
- Merge overlapping candidates by the decision they resolve rather than asking
  one runtime or ownership question per specialist.
- Ask a later question only when an answer creates a new material uncertainty
  or needs clarification.
- Impose no required minimum number of questions.
