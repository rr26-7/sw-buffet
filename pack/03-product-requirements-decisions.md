# SW Pack - 03 Product Requirements Decisions

Decision scope
Use this matrix before architecture and technology choices. It prevents agents from optimizing for code before the software's purpose is explicit.

Rows
Problem framing
Options: user outcome, workflow pain, compliance mandate, cost reduction, platform capability, migration, incident fix.
Prefer when: the option maps to a measurable user/business/system outcome.
Avoid when: the request is only a feature list without success criteria.
Evidence and metrics: interviews, current process data, support tickets, analytics, compliance deadline, incident record, business KPI.
Owner: Product UI Lifecycle, then Orchestrator.

Product shape
Options: internal tool, B2B SaaS, consumer app, platform/API, data/ML system, regulated system, embedded/desktop/local-first system.
Prefer when: deployment, support, privacy, UX, and operational needs match the shape.
Avoid when: monetization, compliance, data sensitivity, or offline constraints are unknown.
Evidence and metrics: target users, tenancy model, data classification, uptime target, commercial model, support model.
Owner: Product UI Lifecycle with Architect.

Requirement confidence
Options: discovery, MVP, regulated specification, migration, rewrite, incident remediation, scale-out.
Prefer when: delivery governance matches uncertainty.
Avoid when: high-uncertainty work is treated like fixed-scope delivery or regulated work lacks traceability.
Evidence and metrics: assumptions list, acceptance criteria, traceability needs, regulatory evidence, migration inventory.
Owner: Product UI Lifecycle with Orchestrator.

Prioritization method
Options: RICE, WSJF, MoSCoW, risk-first, compliance-first, incident-first.
Prefer when: the method matches decision pressure.
Avoid when: scoring hides hard gates or unverified assumptions.
Evidence and metrics: reach, impact, confidence, effort, cost of delay, job size, risk exposure, deadline.
Owner: Product UI Lifecycle.

Success metrics
Options: activation/adoption, task completion, retention, conversion, latency, error budget, compliance evidence, support load, cost per user/tenant/request.
Prefer when: metrics are observable and tied to outcomes.
Avoid when: metrics encourage local optimization that damages reliability, privacy, or accessibility.
Evidence and metrics: baseline, target, instrument owner, dashboard/runbook link.
Owner: Product UI Lifecycle with DevSecOps Observability.

Scope control
Options: MVP, staged rollout, feature flags, kill switch, phased migration, beta cohort, canary.
Prefer when: reversibility and blast radius matter.
Avoid when: release is all-or-nothing without rollback, migration, or support plan.
Evidence and metrics: rollout plan, rollback plan, migration rehearsal, cohort definition, guardrail metrics.
Owner: Product UI Lifecycle with DevSecOps Observability.

Primary source anchors
ISO/IEC/IEEE 42010 for stakeholders and concerns.
ISO/IEC 25010 for quality attributes.
DORA for delivery metrics.
WCAG and W3C i18n for user-facing quality.
GDPR/CCPA/PCI where data privacy or payment scope exists.
