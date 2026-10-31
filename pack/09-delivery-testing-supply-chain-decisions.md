# sw-buffet page 09: Delivery Testing Supply Chain Decisions

Decision scope
Use this matrix for implementation governance, CI/CD, tests, releases, environments, artifacts, migrations, and provenance.

Test strategy
Options: unit, integration, contract, end-to-end, property-based, fuzzing, differential (back-to-back), mutation, performance, accessibility, security, chaos/resilience.
Prefer when: tests map to risk and decision objects, not just coverage percentage.
Avoid when: expensive E2E tests replace lower-level contracts or critical behavior has no automated check.
Metrics: meaningful coverage, mutation score where useful, flake rate, contract pass rate, security test findings, performance regression.
Proportionality: the blocks below are options, not a mandatory checklist; select them by risk and record the choice in the decision object.

Test oracle selection
Options: expected values taken from the requirement, property or invariant oracle (round-trip, idempotence, ordering, conservation, model-based state machine), differential oracle (a reference or previous implementation, a simpler slow version, another library), crash or sanitizer oracle (fuzzing), metamorphic relation (a known change of input gives a known change of output).
Prefer when: every risk-bearing test names where its expected value comes from, and that source is independent of the code under test (Test Reality Guardrail, page 12).
Avoid when: expected values are produced by running the implementation and pasting its output, or by re-implementing the same algorithm inside the test.
Metrics: share of risk-bearing behaviors with a named independent oracle, mutation score on those modules.

Property-based testing
Options: generator-based property tests (for example Hypothesis, fast-check, jqwik, FsCheck or CsCheck, proptest), stateful or model-based tests, shrinking with a recorded seed or failure database.
Prefer when: logic has invariants over a large input space - parsers and serializers (round-trip), money and unit arithmetic, sorting, merging and deduplication, state machines, permission rules, idempotency and retry logic.
Avoid when: the only expressible property is "does not throw", or the generators cannot reach the boundary values the risk depends on.
Metrics: properties per risk-bearing module, defects found, shrunk counterexamples kept as regression tests, seed recorded so CI failures reproduce.

Fuzzing
Options: coverage-guided fuzzing (for example libFuzzer, AFL++, cargo-fuzz, Atheris, Jazzer, Go native fuzzing, SharpFuzz), schema-driven API fuzzing from OpenAPI or GraphQL schemas, continuous fuzzing (OSS-Fuzz, ClusterFuzzLite), sanitizers (ASan, UBSan, MSan, TSan) for native, unsafe, and FFI code.
Prefer when: code parses or deserializes attacker-controlled input (files, uploads, network protocols, query or template languages), sits on a trust boundary, or contains native, unsafe, or FFI code.
Avoid when: the target has no input surface beyond a fixed set of options; fuzz jobs run without a time box or spend cap (gate 17).
Metrics: fuzz targets per trust-boundary parser, corpus size and coverage, short time-boxed run on each change and a longer scheduled run, crash-free hours, every crash minimized and kept as a regression test, sanitizer findings.
Sources: OSS-Fuzz and the official documentation of the chosen fuzzer; OWASP ASVS (input validation).

Mutation testing
Options: a mutation tool for the language (for example Stryker, PIT, mutmut, cosmic-ray, cargo-mutants), mutation scoped to the changed lines, a scheduled full run on risk-bearing modules.
Prefer when: tests guard security, money, data integrity, or documented invariants, and whenever an AI agent wrote or modified the tests - the mutation score is the automated form of the seeded-defect check in the Test Reality Guardrail.
Avoid when: full-repository mutation runs on every change (cost grows with suite time times mutant count; scope to the diff and risk-bearing modules); a score of 100 percent is treated as the target - equivalent mutants exist, so survivors are triaged with a reason, never silently suppressed.
Metrics: mutation score on risk-bearing modules, surviving mutants triaged, run time.

Rewrite, port, and migration equivalence
Use when code is rewritten, ported to another language (for example C or C++ to Rust), or a component is replaced (library swap, algorithm optimization, framework migration).
Options: differential testing of old and new implementation on shared inputs, one fuzz corpus run against both, recorded traffic or golden files replayed against both, shadow comparison during a staged rollout.
Prefer when: the old implementation is the best available specification; keep it buildable and runnable in CI until the new one reaches equivalence on the agreed corpus.
Avoid when: divergences are closed by silently copying the old output. Every intended difference (bug fix, security fix, dropped behavior) is a decision object; every defect the old implementation shows is a finding, not a requirement to preserve.
Metrics: corpus size and coverage, divergence count (open, accepted as intended, fixed), shadow mismatch rate, inherited-defect findings.

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
Canonical text lives in the Test Reality Guardrail of page 12 (Code Quality AI Implementation Gates). Apply it to every test-strategy decision; do not fork or restate the wording here - single source of truth.

Delivery health
Use DORA metrics as a useful delivery lens: deployment frequency, lead time for changes, change failure rate, and time to restore service. Do not use them as vanity metrics; connect them to user impact and system risk.

Pipeline completeness
CI/CD gate addition - deployment pipeline completeness:
- Every shipped target is compiled in CI: all client platforms/TFMs, all services, all artifacts that reach users. A target covered only by linked-source logic tests is not covered; its real build can still break.
- Schema and data migrations have an explicit step in the release pipeline (or a documented manual procedure with an owner) and run in a defined order relative to code deploy (prefer expand/contract with migrate-before-deploy).
- Rollback strategy explicitly covers schema and data, not only the code artifact swap. If migrations are backward-compatible by policy, state it; if not, name the restore procedure and its RPO/RTO.
- Optional automation must degrade safely: pipeline steps that depend on environment-specific secrets or paid tiers should be explicit no-ops with a loud notice when absent, so minimal/low-cost deployment profiles keep working.
Evidence and metrics: end-to-end release rehearsal result, CI coverage of shipped targets (count gap), migration step present and exercised, rollback drill including schema, no-op path tested.
