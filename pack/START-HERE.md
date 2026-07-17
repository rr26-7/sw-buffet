# SW Pack - START HERE (Decision Phases)

Purpose
This page turns the SW Agentic Dev Workflow prompts into an explicit phased decision process for software creation. It extends the existing algorithm matrix into product, architecture, API, data, security, reliability, delivery, frontend, and commercial decisions.

Grounding rule
No unverifiable claims. Current, risky, legal, security, dependency, cloud, payment, or platform-specific claims must be backed by official documentation, repo evidence, tests, prototypes, telemetry, or a clearly labeled assumption.
Audience and consumption model
These pages are written for frontier-model AI agents (Fable 5 class and above), not for direct human reading; density and accretive layered additions are intentional and optimized for machine processing. Humans interact through the AI: the human supplies the software brief; the AI interprets it through this pack, selects the usage mode and the relevant decision phases, recommends next steps, and surfaces risks and hard gates to the human. When a human needs the rationale of any rule, they ask the AI to explain it. The human-readable workflow overview lives in SW Pack - 00 Deploy This Agent Pack.

Decision phases
P0 - Intake and no-go scan: define user outcome, business context, constraints, data sensitivity, regulatory surface, and irreversible risks. State the unit of delivered value the work optimizes for (the outcome that counts, e.g. a completed user task or a verified contribution), so later trade-offs can be measured against it rather than against raw activity.
P1 - Stakeholders and concerns: capture stakeholders, concerns, viewpoints, and architecture description needs using ISO/IEC/IEEE 42010 as the anchor.
P2 - Quality Attribute Vector: score functional suitability, performance, reliability, security, maintainability, usability/accessibility, compatibility, portability/deployability, cost efficiency, and compliance risk. This is inspired by ISO/IEC 25010, not a substitute for buying the standard. Express this vector as a single weighted objective: minimize expected total cost (compute, operations, risk, maintenance) per unit of delivered value, subject to hard ceilings (cost/abuse, SLO). Name the value unit, the dominant term, and the ceiling. Keep it qualitative unless telemetry exists; treat unmeasurable terms as needs-evidence rather than inventing numbers. Required only in Mode H; a one-line objective is enough in Mode N; skip in Mode S.
P3 - Architecture and topology: choose modular monolith, layered monolith, microservices, event-driven, serverless, edge/offline-first, desktop/local-first, or hybrid.
P4 - API and integration: choose REST/OpenAPI, gRPC, GraphQL, realtime/streaming browser transports, event contracts, or typed same-language RPC.
P5 - Data, consistency, and privacy: choose storage models, transaction boundaries, consistency model, retention, classification, residency, deletion/export, and auditability.
P6 - Security and compliance: threat model, authn/authz, validation, secrets, supply chain, SBOM, payment scope, privacy obligations, and audit evidence.
P7 - Reliability and observability: define SLIs, SLOs, error budget, telemetry, incident response, RPO/RTO, resilience patterns, and capacity model.
P8 - Delivery, testing, and supply chain: define CI/CD gates, test pyramid/portfolio, release strategy, feature flags, rollback, provenance, and dependency hygiene.
P9 - Frontend, accessibility, and commercial model: choose app shape, state strategy, WCAG target, i18n, docs, billing model, metering, entitlements, and support model.
P10 - ADR and verification review: write accepted/rejected decisions, evidence map, metrics, verification plan, owners, and review triggers.

Agent ownership
SW DEV Product UI Lifecycle: P0 and P9, with requirements, UX, accessibility, docs, lifecycle, and commercial risk.
SW DEV Architect: P1 through P5, with architecture, topology, contracts, data boundaries, and ADR structure.
SW DEV Engineering and Performance: implementation feasibility across P4, P5, P7, and P8; performance, concurrency, resource use, and code quality.
SW DEV DevSecOps and Observability: P6 through P8; security, compliance evidence, delivery, telemetry, SLOs, and operations.
SW DEV Orchestrator: P10; final integration, contradictions, missing evidence, and cross-agent consistency.
SW DEV Decision Steward: validates decision objects before implementation and before final orchestration. SW DEV Frontier Capability Risk Auditor: audits AI-assisted changes for frontier-model failure classes (consistency drift, concurrency defects, knowledge-boundary hallucination, security-invariant erosion, attention loss); see SW Pack - 14.

Hard gates
Do not proceed without explicit mitigation when a decision can cause legal/compliance breach, security/privacy breach, data loss, safety risk, SLO/SLA breach, irreversible cost escalation, critical vendor lock-in, or reliance on unverified critical dependency behavior.

Operating mode
Operating mode: Use the smallest matrix that can decide the issue. When uncertainty is material, create a decision object with status needs-evidence instead of guessing. Weighted scores help compare options, but hard gates override scores. The weighted objective is a lens to align trade-offs and expose the dominant term - not an acceptance gate and not a metric to game; weights are a policy choice, revisited when the product's stage changes.
Conflict protocol
Scope: use when roles disagree, new evidence contradicts an accepted decision, or two decision objects imply incompatible actions.
1. Record both positions as conflict notes on the affected decision object(s), each with its evidence level. No silent overwrite; superseded decisions link forward.
2. Decide by rules, in order: hard gates first - any position violating a hard gate loses regardless of score. Then evidence precedence: for this-codebase facts, local and production evidence (E2/E4) beats general documentation; for current provider/framework behavior, official documentation (E1) beats local inference; experiments (E3) beat both when they directly test the disputed claim. Then, on an evidence tie, prefer the more reversible option with the smaller blast radius.
3. If still unresolved, Decision Steward sets needs-evidence and names the lowest-cost discriminating test; Orchestrator schedules it or proposes a temporary, clearly labeled assumption.
4. Escalate to the human when the conflict is a value tradeoff, an accepted-risk decision, or touches a hard-gate exception: present both positions, the evidence, and one recommendation.
5. Record the resolution and the dissent in the decision object / ADR. Dissent is information, not noise.

Usage modes
Mode S - Small change: use for localized fixes with no new dependency, no data model change, no auth/security boundary, no external integration, no billing/compliance impact, and no architecture decision. Output only: goal, touched surface, tests run, and risks.
Mode N - Normal feature: use relevant matrices only. Create compact decision objects for material choices. Require verification plan, owner, and review triggers.
Mode H - High-risk/system decision: use all relevant decision phases and Decision Steward review. Required for auth, privacy, regulated data, payments, irreversible migrations, new cloud/provider dependency, SLO/SLA commitment, major architecture/API/data decisions, AI agents with tool access, or material vendor lock-in.
Escalation rule: if a small change touches a hard gate or creates material uncertainty, promote it to Normal or High-risk instead of forcing a shortcut.

Run modes and multi-pass execution
The brief must state the run mode: audit or development. Run mode is orthogonal to usage modes: usage modes (S/N/H) set process depth; the run mode sets whether the agent may change anything. Both apply in every engagement.
Development mode: the agent plans, implements, and verifies changes. Software is never delivered in a single pass. Passes iterate the decision phases, they do not replace them: a typical sequence is pass 1 decision inventory and skeleton (P0-P5 decisions), pass 2 implementation of accepted decisions (implementation gates, SW Pack - 12), pass 3 verification and hardening (readiness), with further passes consuming gate, eval, and audit findings. Every pass ends with an explicit statement of what is done, what remains, and the entry point for the next pass. A compiling application is not a finished application; readiness is declared only by the Decision Steward checklist, never by pass count.
Audit mode: read-only. The agent examines the software and produces findings, decision objects, and risks. No code changes, no fixes, no "small improvements while we're here" - a fix proposal is output, not action. The brownfield domain-model trigger below and the SW Pack - 14 brownfield audit are audit-mode runs; their findings become the backlog for a later development-mode pass.
If the brief does not state the run mode, ask - run mode is material. If asking is impossible, default to audit mode (no side effects) and state the default explicitly.

Brownfield domain-model trigger. On an existing codebase, run the domain-model gate (SW Pack - 12 gates 9-12 plus the Domain smell proportionality rule) as a one-time AUDIT that produces a ranked findings list - not a blanket rewrite. Rank by the proportionality rule (representable-and-reachable invalid states first). Fix the HIGH items, defer or explicitly accept the rest with recorded rationale (decision-object primitive_exceptions). Do NOT attempt to convert every anemic entity or wrap every primitive in one pass; that is churn without proportional risk reduction. Where a rich type already exists (value object / discriminated union) but the persistence entity bypasses it, prefer reusing that type in the entity - that is the cheapest high-value fix. Record index freshness and, where a code graph is available, use it to find every representable-invalid-state pattern rather than eyeballing a few files.

Agent runtime, tooling, and governance (P11)

Decision phase addition: P11 - Agent runtime, tooling, and governance: choose the target agent surface, orchestration pattern, sandbox/workspace boundary, tool trust model, approval policy, network egress policy, secret exposure boundary, MCP/server trust boundary, skill/plugin provenance, trace/memory retention, subagent concurrency limits, runtime timeout, token/cost budget, and rollback/failure handling for autonomous tool calls.
Orchestration pattern must be explicit: single-agent workflow; manager calls specialists as bounded tools while keeping final-answer ownership; handoff where a specialist owns a branch; explicit subagents/background tasks for bounded exploration, review, or implementation; or no multi-agent workflow when the extra role split adds ceremony without reducing risk.
Agent ownership update: Orchestrator confirms the run mode (audit | development), selects usage mode, routes bounded specialist work, records contradictions, and synthesizes the final user-facing result. Decision Steward owns evidence quality, decision status, hard-gate validation, and readiness/go-no-go recommendation. DevSecOps owns runtime/tool/security controls. Architect owns topology/API/data/domain decisions. Engineering owns implementation feasibility, tests, performance, and code quality. Product UI Lifecycle owns outcome, UX, accessibility, lifecycle, and commercial risk. Frontier Capability Risk Auditor owns frontier failure-class findings (consistency drift, concurrency defects, knowledge-boundary hallucination, security-invariant erosion, attention loss) and capability-stress scoring; invoked by Orchestrator or Decision Steward (SW Pack - 14).
Hard-gate addition: do not proceed without explicit mitigation for over-privileged tools or skills, untrusted MCP/tool sources, unrestricted network egress with private data access, secrets exposed to prompts/logs/traces, unreviewed autonomous side effects, prompt-injection exposure from repo/web/email/docs, unsafe persistent memory, or unsupported claims about a target agent surface.
Usage mode update: Mode H is required for AI agents with broad tool access, external side effects, MCP/connectors, skill/plugin installation, secrets or private data access, autonomous background execution, production deployment authority, or material cross-agent handoffs. Mode N may use only the relevant P11 checks. Mode S records the runtime/tool surface only when it affects the touched scope.
Output discipline update: default to compact decision objects, evidence, tests, risks, and next handoff. Large blueprints, generated snippets, and full multi-role outputs are only required when the selected usage mode and risk justify them.
Cost, abuse, and financial-risk considerations



Decision phase additions



P0 addition - Intake and no-go scan: identify usage-billed surfaces, attacker/user-triggered expensive operations, third-party billable APIs, payment/refund/credit exposure, AI/model/token costs, cloud cost exposure, logging/telemetry volume, build/deploy minutes, storage/egress, communications spend, and the accountable business owner for spend risk.



P2 addition - Quality Attribute Vector: cost efficiency must include financial-abuse resistance, not only normal operating cost. Score whether the design bounds attacker-induced spend, budget exhaustion, credit/refund leakage, metering drift, and cost-triggered availability loss.



P3-P5 addition - Architecture, API, and data decisions: identify amplification paths where one request, event, tenant, prompt, file, job, export, queue message, webhook, or workflow can fan out into disproportionate compute, storage, egress, model, payment, logging, or third-party cost.



P6 addition - Security and compliance: threat model financial denial of service, denial of wallet, billing/metering abuse, quota bypass, payment/refund abuse, entitlement abuse, promo/credit abuse, third-party spend abuse, and cloud/provider cost-control gaps.



P7 addition - Reliability and observability: define cost SLOs or guardrails where relevant, including spend anomaly detection, budget/quota alerts, usage telemetry, graceful degradation before hard cost caps cause total outage, and runbooks for emergency cost stops.



P8 addition - Delivery, testing, and supply chain: add cost-abuse tests for expensive paths, IaC cost review where practical, budget/alert/quota verification, load/capacity tests with explicit spend ceilings, and regression tests for metering, idempotency, and rate limits.



P9 addition - Frontend, accessibility, and commercial model: verify billing model, metering, entitlements, trials, coupons, credits, refunds, seat limits, plan limits, tenant quotas, and user-visible limits prevent predictable abuse and support clear customer communication.



Agent ownership addition



Product UI Lifecycle owns commercial/billing model, user-visible limits, pricing/plan semantics, support impact, and customer-facing communication.

Architect owns cost-amplification topology and boundary design.

Engineering and Performance owns resource limits, idempotency, queues, throttles, concurrency, performance-cost tradeoffs, and regression tests.

DevSecOps and Observability owns cloud/provider limits, budget alerts/actions, anomaly detection, telemetry, emergency cost stops, and incident readiness.

Decision Steward validates unresolved financial hard gates before implementation and final readiness.



Hard gate addition



Do not proceed without explicit mitigation when a decision can permit unbounded spend, material attacker-induced spend, budget exhaustion that causes service outage, uncontrolled third-party charges, payment/refund/credit leakage, AI/token/tool-call cost runaway, cloud autoscaling/egress/log/storage runaway, or reliance on lagging budget alerts as the only control.



Mode H addition



Mode H is required for material usage-billed systems, cloud autoscaling/serverless/event-driven cost paths, payment/refund/credit systems, AI/model/tool-call systems with paid inference or paid tools, multi-tenant quota enforcement, third-party communications APIs, or any design where an external actor can trigger spend beyond a low agreed threshold.
Domain modeling considerations
Decision phase addition: P2.5 - Domain model and type safety: identify core domain concepts, invariants, invalid states, valid state transitions, value objects, entities/aggregates, domain operations, boundary DTO mappings, persistence mappings, and justified primitive exceptions before architecture, API, and data shapes are finalized.
Agent ownership addition: Decision Steward validates P2.5 decision objects; Architect designs the domain/type model and persistence mapping; Engineering implements rich domain types and safe operations; DevSecOps verifies boundary parsing/validation; Product UI Lifecycle verifies explicit UI states; Orchestrator checks cross-agent consistency.
Operating rule addition: avoid primitive obsession, anemic domain models, enum/status/boolean fields with nullable companion payloads, validation explosion, and throw-driven invalid operations in core domain code. DTOs, persistence records, and external payloads may use primitives, but must be mapped at boundaries into validated domain or command types where domain correctness matters.
Proportionality rule: do not wrap every primitive mechanically. Apply rich types where invalid states, business rules, money, identity, time, permissions, lifecycle state, safety, security, privacy, or data integrity matter.

Pipeline completeness and audit calibration
Origin: derived from a comparative audit exercise (protocol-driven vs. unconstrained audit of the same codebase). All four failure classes below are domain-neutral and generalize beyond any single project.
Operating rule additions:
1. Pipeline completeness: a delivery decision is not done when artifacts exist; it is done when the pipeline carries them end to end. Every shipped target (every app, every platform TFM, every artifact users receive) must be compiled by CI, and schema/data migrations must have an explicit, owned step in the release path. Rollback plans must state what happens to schema and data, not only to code.
2. Audit evidence calibration: when scoring deployability, reliability, or delivery, the evidence is a verified end-to-end path (build, migrate, deploy, smoke, rollback), not the existence of its parts. Existence of migrations, runbooks, or workflows is E2 evidence of presence, not of completeness.
3. Working-tree hygiene: secret and sensitive-data scans must include untracked and ignored files, not only committed history. Local-only secrets, exports, and machine-specific configs are still exposure and still rot.
4. Configuration coherence: a configurable value must have exactly one source of truth. Any hardcoded duplicate of a configurable value elsewhere in the code is a defect class (silent divergence breaks behavior when the option changes) and should be caught at review or by a test that exercises a non-default value.
Anti-scraping and automated-abuse considerations

Scope
Use this section when building, reviewing, or operating public web surfaces, APIs, search, listing, catalog, pricing, availability, media/download, documentation, knowledge-base, RAG-source, user-generated-content, or commercially sensitive content that can be harvested by humans, classic scrapers, headless browsers, browser automation, AI crawlers, or AI agents.

Operating rule addition
Treat scraping, bot abuse, and AI crawler/agent access as first-class product, security, privacy, reliability, SEO/AI-discovery, and commercial concerns. Do not rely on robots.txt as an access-control mechanism. Verify current crawler, AI-provider, WAF/CDN, bot-management, and platform behavior against official documentation, repository evidence, controlled tests, telemetry, or mark the decision needs-evidence.

Decision phase additions
P0 - Intake and no-go scan: identify scrape-worthy assets, public vs non-public content, acceptable automation, disallowed automation, bulk-access expectations, terms/licensing constraints, data sensitivity, and irreversible commercial or privacy risks.
P4 - API and integration: decide quotas, rate limits, pagination/windowing, export limits, API-key scopes, per-user/per-tenant controls, anti-enumeration, GraphQL complexity/batching limits, webhook/job limits, and legitimate partner/bulk access paths.
P5 - Data, consistency, and privacy: classify public content, personal data, tenant data, licensed content, paid content, and derived data; define retention, deletion/export, evidence redaction, and privacy boundaries for logs and bot telemetry.
P6 - Security and compliance: threat-model OWASP OAT-011 Scraping, OWASP API4:2023 Unrestricted Resource Consumption, credentialed scraping, headless/browser automation, bot evasion, crawler impersonation, AI training crawlers, AI search crawlers, and user-initiated AI agents.
P7 - Reliability and observability: define telemetry for request rate by principal, token, IP, ASN, user agent, verified-bot signal, and path; track 429/challenge outcomes, anomaly detections, false positives, cost impact, SLO impact, alerts, and runbook actions.
P8 - Delivery, testing, and supply chain: test abuse controls, WAF/CDN/bot policies, limit enforcement, robots/noindex/crawler policy deployment, and regression checks for high-risk endpoints before release.
P9 - Frontend, accessibility, and commercial model: document tradeoffs among search visibility, AI-search visibility, user-triggered agents, licensing/monetization, legitimate accessibility or archival use, support load, and false-positive risk.
P10 - ADR and verification review: create a decision object for material automated-abuse choices. Keep the status needs-evidence when current provider or crawler behavior is unverified.

Agent ownership addition
DevSecOps and Observability owns automated-abuse threat modeling, bot controls, telemetry, alerts, WAF/CDN policy, and incident readiness.
Architect owns API/data boundaries, public vs private resource design, bulk-access alternatives, pagination/export/query shapes, and ADR structure.
Engineering and Performance owns implementable limits, anti-enumeration mechanics, efficient detection hooks, tests, and performance/cost evidence.
Product UI Lifecycle owns SEO/AI-discovery tradeoffs, content licensing, user experience, accessibility, legitimate automation, rollout, and support impact.
Decision Steward validates hard gates, evidence quality, and readiness when scraping could create legal, privacy, security, commercial, cost, or SLO risk.

Hard gate addition
Do not proceed to implementation handoff or production release with unresolved material risk from scraping, unrestricted resource consumption, sensitive-data harvesting, paid-content harvesting, credentialed bulk extraction, crawler-policy ambiguity, bot-management false positives, SLO breach, or cost escalation.

Source anchors to verify at use time
OWASP OAT-011 Scraping: https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-011_Scraping
OWASP API4:2023 Unrestricted Resource Consumption: https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/
RFC 9309 Robots Exclusion Protocol: https://datatracker.ietf.org/doc/html/rfc9309
Google robots.txt guidance: https://developers.google.com/search/docs/crawling-indexing/robots/intro
OpenAI crawler documentation: https://developers.openai.com/api/docs/bots
Cloudflare managed robots.txt / AI crawler controls: https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/
IETF Web Bot Authentication working group: https://datatracker.ietf.org/wg/webbotauth/about/

Code graph analysis
Code is a graph, not text. When analyzing a codebase, prefer structured code intelligence over raw text search: code knowledge graphs, code property graphs (AST + control flow + data flow), call graphs, dependency graphs, and semantic/vector indexes.
If a code-graph tool is available (e.g. a code knowledge graph MCP server such as codebase-memory-mcp or CodeGraphContext, or engines such as CodeQL, Joern, Sourcegraph), index the repository first and use graph queries as primary evidence: architecture overview and module clusters for P3; caller/callee and impact tracing before changes for P8 and P10; data-flow and taint tracing for P6 security review; complexity, hot-path, and coupling metrics for P2 and P7; cross-service route and event links for P4.
Graph query results are E2 local evidence. Record the tool, query, and result summary in the decision object. When a call graph is available, text grep alone must not be used to claim no callers or no impact.
Graph lifecycle: build the code graph from the first commit, not after the software exists. Greenfield projects create the index at inception (empty or scaffold repo is fine) and re-index incrementally on every material change via watch mode, git hook, or a CI step, so the graph is design feedback during development, not a post-hoc audit. Use it continuously: architecture clusters and boundaries validate P3 decisions as code grows; complexity, hot-path, and coupling metrics catch structural drift at each increment (P2, P7); change-impact and caller tracing run before every non-trivial edit (P8); data-flow checks accompany each new trust boundary (P6). A stale graph is not evidence: record index freshness (commit/timestamp) with every graph-based claim. Where the tool supports it, persist graph artifacts and architecture decision records across sessions and share them with the team (e.g. codebase-memory-mcp persistence artifact and manage_adr; CodeQL databases in CI; Sourcegraph precise indexes).
