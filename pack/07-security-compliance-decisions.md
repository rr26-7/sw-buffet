# SW Pack - 07 Security Compliance Decisions

Decision scope
Use this matrix for secure design, verification controls, privacy/compliance boundaries, payment scope, dependencies, and release trust.

Authentication and authorization
Options: session auth, OAuth/OIDC, service accounts, API keys, RBAC, ABAC, relationship-based access, tenant isolation.
Prefer when: the model maps to user, service, tenant, and data sensitivity requirements.
Avoid when: authentication is selected without authorization tests or tenant isolation model.
Metrics: authz test coverage, privilege escalation findings, session/token incidents, tenant isolation tests.
Sources: OWASP ASVS and relevant provider docs.

Input validation and output encoding
Options: schema validation, allowlists, contextual escaping, canonicalization, file/content validation.
Prefer when: every trust boundary has explicit validation and encoding rules.
Avoid when: validation is UI-only or ad hoc string checks replace parser/schema support.
Metrics: validation test coverage, injection findings, rejected malicious payloads, error leakage.
Sources: OWASP ASVS and NIST SSDF.

Secrets and credentials
Options: managed secret store, short-lived credentials, rotation, least privilege, no secrets in repo/logs.
Prefer when: rotation, audit, scoping, and emergency revoke are defined.
Avoid when: secrets live in source, local files, shared chat, or unscoped environment variables.
Metrics: secret scan failures, rotation age, credential scope, audit log completeness.
Sources: NIST SSDF and provider docs.

Supply chain
Options: lockfiles, dependency scanning, SBOM, provenance, signed artifacts, SLSA target, review of licenses and transitive deps.
Prefer when: artifact identity and dependency risk need traceability.
Avoid when: builds are non-reproducible, dependencies are unpinned, or SBOM/provenance is absent for regulated work.
Metrics: critical vulns, dependency freshness, SBOM present, provenance present, SLSA level target, license findings.
Sources: NIST SSDF, SLSA, SPDX, CycloneDX.

Threat modeling
Options: misuse cases, trust-boundary diagram, STRIDE-like review, attack trees, abuse cases.
Prefer when: the decision crosses auth, data, money, safety, tenancy, or external integrations.
Avoid when: threat model is only a checklist after implementation.
Metrics: threats identified/mitigated, residual risks accepted, security tests mapped to threats.
Sources: OWASP ASVS and NIST SSDF.

Payment/card data
Options: hosted checkout/fields, payment provider tokens, direct card processing, wallet payments, invoicing.
Prefer when: PCI scope is minimized and provider docs are followed.
Avoid when: raw card data touches systems without PCI program and explicit scope evidence.
Metrics: PCI scope, payment failure rate, idempotency coverage, reconciliation errors, chargeback/fraud signals.
Sources: PCI SSC and payment provider docs such as Stripe.

Compliance posture
Options: GDPR, CCPA, PCI DSS, sector-specific controls, internal policy.
Prefer when: applicability is documented with data map and evidence owners.
Avoid when: compliance is guessed from product category alone.
Metrics: evidence completeness, data subject request handling, retention compliance, audit findings.
Sources: official legal/regulatory and standards documentation.
