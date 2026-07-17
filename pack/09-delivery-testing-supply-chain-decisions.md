# SW Pack - 09 Delivery Testing Supply Chain Decisions

Decision scope
Use this matrix for implementation governance, CI/CD, tests, releases, environments, artifacts, migrations, and provenance.

Test strategy
Options: unit, integration, contract, end-to-end, property-based, mutation, performance, accessibility, security, chaos/resilience.
Prefer when: tests map to risk and decision objects, not just coverage percentage.
Avoid when: expensive E2E tests replace lower-level contracts or critical behavior has no automated check.
Metrics: meaningful coverage, mutation score where useful, flake rate, contract pass rate, security test findings, performance regression.

CI/CD gates
Options: lint/typecheck, unit/integration tests, contract tests, security scans, SBOM, provenance, image/package scan, deploy approval.
Prefer when: gates catch real risks quickly and are tied to release criticality.
Avoid when: gates are slow/noisy and teams bypass them.
Metrics: build time, failure signal quality, bypass count, vulnerability count, artifact provenance present.
Sources: NIST SSDF, SLSA, SPDX/CycloneDX.

Release strategy
Options: trunk-based, short-lived branches, feature flags, canary, blue-green, phased rollout, kill switch, rollback.
Prefer when: blast radius and reversibility match product risk.
Avoid when: deploy and release are coupled for risky features.
Metrics: deployment frequency, lead time, change failure rate, rollback time, flag stale count.
Sources: DORA and Twelve-Factor App.

Environment and configuration
Options: dev/stage/prod parity, externalized config, ephemeral preview environments, test data management.
Prefer when: environment drift is a known risk and repeatability matters.
Avoid when: production-only behavior is discovered after release.
Metrics: drift findings, preview environment success, config incident count, test data freshness.
Sources: Twelve-Factor App and provider docs.

Artifacts
Options: container images, packages, binaries, SBOM, signed releases, attestations, release notes.
Prefer when: reproducibility and traceability are required.
Avoid when: artifact identity cannot be connected to source, build, dependency, and deployment.
Metrics: artifact signing status, SBOM status, provenance status, dependency freshness, license findings.
Sources: SLSA, SPDX, CycloneDX, NIST SSDF.

Database and data migrations
Options: backward-compatible migration, expand/contract, dual-write/read, shadow table, backfill, rollback, data reconciliation.
Prefer when: data loss and downtime are unacceptable.
Avoid when: destructive migrations lack backup, rehearsal, and rollback.
Metrics: migration duration, lock time, failed rows, reconciliation diff, restore success, rollback success.

 
Test Reality Guardrail (anti-accommodating tests)
Canonical text lives in SW Pack - 12 Code Quality AI Implementation Gates (Test Reality Guardrail). Apply it to every test-strategy decision; do not fork or restate the wording here - single source of truth.

Delivery health
Use DORA metrics as a useful delivery lens: deployment frequency, lead time for changes, change failure rate, and time to restore service. Do not use them as vanity metrics; connect them to user impact and system risk.

Pipeline completeness
CI/CD gate addition - deployment pipeline completeness:
- Every shipped target is compiled in CI: all client platforms/TFMs, all services, all artifacts that reach users. A target covered only by linked-source logic tests is not covered; its real build can still break.
- Schema and data migrations have an explicit step in the release pipeline (or a documented manual procedure with an owner) and run in a defined order relative to code deploy (prefer expand/contract with migrate-before-deploy).
- Rollback strategy explicitly covers schema and data, not only the code artifact swap. If migrations are backward-compatible by policy, state it; if not, name the restore procedure and its RPO/RTO.
- Optional automation must degrade safely: pipeline steps that depend on environment-specific secrets or paid tiers should be explicit no-ops with a loud notice when absent, so minimal/low-cost deployment profiles keep working.
Evidence and metrics: end-to-end release rehearsal result, CI coverage of shipped targets (count gap), migration step present and exercised, rollback drill including schema, no-op path tested.
