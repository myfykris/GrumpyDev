# Infrastructure applicability behavior

Exercise the survey with two repositories. One is a deployable service whose
runtime affects correctness. The other is a documentation-only package with no
material build, runtime, hosting, or consumer boundary.

Expected behavior:

- Require a deployment or execution profile for the service.
- Ask no infrastructure question for the documentation-only package.
- Do not invent a production server, process manager, database, or cloud
  environment merely to complete the second survey.
- If a library has a material supported-runtime or consumer matrix, represent
  that boundary without pretending the library itself is hosted.
