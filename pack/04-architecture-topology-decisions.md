# SW Pack - 04 Architecture Topology Decisions

Decision scope
Use this matrix when selecting the system shape, deployment topology, service boundaries, and operational ownership.

Modular monolith / vertical slice
Prefer when: small to medium team, strong need for fast iteration, shared data model, low operational maturity, or unclear domain boundaries.
Avoid when: independent deployment, separate scaling, strict isolation, or different regulatory boundaries are mandatory now.
Metrics: deployment frequency, lead time, code ownership clarity, module coupling, build/test time, p95 latency, cost per tenant/user.

Layered monolith
Prefer when: stable domain, conventional CRUD, simple operations, strong consistency, and team familiarity matter.
Avoid when: layers become cross-cutting bottlenecks or domain boundaries are hidden by generic service layers.
Metrics: change coupling, test time, defect clustering, dependency direction violations.

Microservices
Prefer when: independent teams own bounded contexts, independent deployment/scaling is required, failure isolation matters, and operations are mature.
Avoid when: team is small, data consistency is central, observability/CI/CD is weak, or boundaries are speculative.
Metrics: DORA metrics, incident rate, inter-service latency, dependency count, change failure rate, MTTR/time-to-restore, ownership count.

Event-driven architecture
Prefer when: async workflows, integration decoupling, replay, audit trails, and temporal separation matter.
Avoid when: immediate consistency and simple request/response dominate, event schema governance is absent, or ordering/idempotency cannot be handled.
Metrics: queue lag, consumer failure rate, replay success, duplicate handling, schema compatibility, end-to-end latency.

Serverless/FaaS
Prefer when: bursty workloads, low ops surface, event triggers, and managed scaling fit.
Avoid when: predictable long-running workloads, tight latency control, portability, local debugging, or cold-start constraints dominate.
Metrics: cold start, p95/p99 latency, invocation cost, error rate, concurrency limits, vendor-specific coupling.

Edge/offline-first client-heavy
Prefer when: latency, offline continuity, local data capture, or geographic distance matters.
Avoid when: conflict resolution, device trust, local storage privacy, or update control is unsolved.
Metrics: sync conflict rate, offline success rate, client crash rate, local storage security findings, update adoption.

Desktop/local-first
Prefer when: local resources, files, devices, privacy, offline work, or user-controlled data are core requirements.
Avoid when: central governance, browser distribution, or multi-device collaboration is dominant and local sync is unplanned.
Metrics: install/update success, crash rate, local data recovery, sync conflict rate, support tickets.

Architecture axes
Team topology, deployment independence, data consistency, latency budget, regulatory boundary, failure isolation, operational maturity, portability, cost, reversibility, and blast radius.

Primary source anchors
ISO/IEC/IEEE 42010, ISO/IEC 25010, CNCF cloud native definition, Twelve-Factor App, DORA, Google SRE.
Domain modeling considerations
Architecture axis addition: domain boundaries and type safety. Evaluate whether the chosen topology keeps core invariants close to the domain model instead of scattering rules across controllers, services, validators, jobs, and UI code.
Prefer modular/vertical boundaries that expose domain operations and value objects where useful. Avoid generic service layers that turn domain entities into passive records while behavior and validation drift into unrelated modules.
Metrics: invariant locality, invalid-state tests, cross-module validation duplication, status/switch branching count for domain state, and clarity of aggregate/module ownership.
