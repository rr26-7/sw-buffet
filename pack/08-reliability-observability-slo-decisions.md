# SW Pack - 08 Reliability Observability SLO Decisions

Decision scope
Use this matrix for availability, resilience, telemetry, incident response, capacity, backups, and operational promises.

Availability target
Options: best effort, business-hours support, business-critical, high availability, regulated/high assurance.
Prefer when: user impact, revenue impact, compliance, and operational budget justify the target.
Avoid when: availability is promised without SLO, staffing, architecture, and cost model.
Metrics: uptime SLI, successful request rate, latency SLI, error budget, incident impact.
Sources: Google SRE SLO guidance.

SLO design
Options: availability SLO, latency SLO, freshness SLO, correctness SLO, durability SLO, support-response SLO.
Prefer when: the SLI is user-centered, measurable, and tied to alerting/release policy.
Avoid when: alerts are based only on infrastructure symptoms or vanity metrics.
Metrics: SLI, SLO target, error budget burn, alert precision, false positives/negatives.
Sources: Google SRE and OpenTelemetry.

Resilience pattern
Options: timeout, retry with backoff, circuit breaker, bulkhead, rate limit, queue/backpressure, graceful degradation.
Prefer when: failure mode is known and the pattern prevents amplification.
Avoid when: retries can duplicate side effects or overload dependencies.
Metrics: dependency error rate, retry rate, saturation, queue depth, p95/p99 latency, shed load.

State recovery
Options: backup/restore, point-in-time recovery, active-passive, active-active, migration rollback, restore rehearsal.
Prefer when: RPO/RTO and data criticality are explicit.
Avoid when: backups exist but restore is untested.
Metrics: RPO, RTO, restore test time, backup age, data-loss drill result.

Observability
Options: logs, metrics, traces, correlation IDs, events, topology/dependency map, runbooks.
Prefer when: debugging a user-impacting issue can follow a request across components.
Avoid when: logs contain secrets/PII or telemetry cannot be joined by request/user/tenant safely.
Metrics: trace coverage, log coverage, metric cardinality, alert-to-runbook coverage, MTTR/time-to-restore.
Sources: OpenTelemetry and Google SRE.

Capacity and performance
Options: load test, stress test, soak test, autoscaling, queue sizing, database capacity plan, cost guardrails.
Prefer when: expected scale, bottlenecks, and saturation signals are measurable.
Avoid when: capacity is inferred from local tests without representative workload.
Metrics: p95/p99 latency, throughput, saturation, queue lag, CPU/memory/IO, cost per request/tenant/user.

Incident response
Options: on-call, runbooks, severity model, postmortem, rollback playbook, customer comms.
Prefer when: promised availability or sensitive data requires operational accountability.
Avoid when: production alerts have no owner or escalation path.
Metrics: MTTA, MTTR/time-to-restore, incident count, recurrence rate, action item completion.
Sources: DORA and Google SRE.
