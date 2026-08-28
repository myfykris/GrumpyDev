# React untrusted content and browser security

Read this reference when the reviewed work directly or indirectly handles untrusted
HTML, Markdown, URLs, styles,
iframes, widgets, direct DOM sinks, browser storage, client-side secrets, source maps,
CSP, framing, or cross-origin behavior.

## Review requirements

- Treat all client-side authorization as presentation behavior. Enforce object,
  property, and action permissions on the authoritative server and avoid
  serializing inaccessible records or secrets merely because the UI hides them.

- Keep normal text in React's escaped rendering path. Require a reviewed
  sanitizer and explicit policy for intentionally rendered HTML or Markdown;
  constrain URL schemes, iframe and navigation targets, CSS or style input, and
  direct DOM sinks used by components or third-party libraries.

- Keep credentials and sensitive personal data out of source maps, client
  environment values, error payloads, analytics, browser storage, and cached
  state unless the architecture explicitly requires and protects that exposure.

- Use browser security controls such as Content Security Policy, frame policy,
  safe cookie attributes, and trusted origin rules as defense in depth matched
  to the actual deployment and third-party script model.

## Verify the claims

- Exercise stored, reflected, and DOM-based hostile content through text, HTML,
  Markdown, URL, navigation, hydration, error, analytics, and widget boundaries.

- Inspect production bundles, source maps, storage, network calls, and rendered
  DOM for secrets, cross-user data, dangerous schemes, and executable markup.
