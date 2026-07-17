# SW Pack - 02 Decision Object Schema

Purpose
Every material software decision should become a decision object. The object is small enough for agent handoff and strict enough to prevent vague recommendations.

Decision object template
decision_id:
title:
phase:
owner_agent:
status: proposed | accepted | rejected | deferred | needs-evidence
context:
  problem:
  use_cases:
  stakeholders:
  constraints:
  assumptions:
quality_vector:
  functional_fit:
  performance_efficiency:
  reliability:
  security:
  maintainability:
  usability_accessibility:
  compatibility_interoperability:
  portability_deployability:
  cost_efficiency:
  compliance_risk:
options:
  - name:
    evidence:
    fit_scores:
    risk:
    reversibility:
    blast_radius:
    cost_model:
    rejection_reasons:
hard_gates:
  legal_compliance:
  security_privacy:
  data_loss:
  safety:
  sla_slo:
  vendor_lockin:
selected_option:
verification_plan:
metrics:
review_triggers:
linked_artifacts:

Scoring
0 - No fit, blocked, or unsupported.
1 - Weak fit; material mismatch or high mitigation cost.
3 - Acceptable fit with known mitigations and evidence.
5 - Strong fit with verified evidence and clear ownership.

Weighting
Weights are allowed only after the hard gates are evaluated. Example weights: security 2x for regulated systems, performance 2x for latency-critical systems, maintainability 2x for long-lived internal platforms, portability 2x for vendor-risk-sensitive programs.

Hard-gate rule
Weighted score cannot override a hard gate. A decision with unresolved legal, security, privacy, data-loss, safety, SLA/SLO, or irreversible lock-in risk stays needs-evidence or rejected.

Evidence rules
E0 assumptions can guide questions.
E1 official documentation can support feasibility.
E2 local evidence can confirm fit to this codebase.
E3 tests/prototypes can validate behavior.
E4 production evidence can validate real-world operation.

Review triggers
Requirement or stakeholder change.
New legal or compliance obligation.
Dependency EOL, critical CVE, license issue, or supply-chain finding.
Traffic, data volume, latency, cost, or team size changes by an order of magnitude.
SLO breach, incident, failed restore test, security finding, accessibility finding, or billing reconciliation issue.

Output standard
Every decision object must include accepted option, rejected options, evidence map, metrics, verification plan, open assumptions, owner, and review trigger. If these are missing, the object is not ready for implementation handoff.

Agent runtime decision-object fields
Decision object schema addition for agentic workflows:
agent_runtime:
  target_surface:
  orchestration_pattern: single-agent | manager-as-tools | handoff | explicit-subagents | background-task | none
  tool_scope:
  sandbox_workspace:
  network_egress:
  approvals_required:
  mcp_connectors:
  skills_plugins:
  secrets_private_data_boundary:
  untrusted_content_sources:
  trace_memory_retention:
  subagent_limits:
  cost_token_budget:
  rollback_failure_handling:
Readiness rule addition: material agentic decisions are not ready for implementation handoff until the runtime/tool surface, approvals, sandboxing, provenance, observability/evals, and residual autonomy risk are explicit. If the target surface does not support a claimed behavior, mark the decision needs-evidence or revise the workflow.
Anti-scraping and automated-abuse decision-object fields

Decision object schema addition:
YAML template:
automated_abuse:
  assets_at_risk:
  legitimate_automation:
  disallowed_automation:
  traditional_scraping_risks:
  ai_crawler_and_agent_risks:
  api_abuse_controls:
  crawler_policy:
  robots_noindex_and_ai_crawler_signals:
  rate_limits_and_quotas:
  pagination_export_and_query_limits:
  anti_enumeration_controls:
  bot_detection_controls:
  verified_bot_or_signed_agent_controls:
  observability_and_alerting:
  cost_and_slo_impact:
  false_positive_risk:
  seo_and_ai_search_tradeoffs:
  legal_privacy_and_license_assumptions:
  verification_plan:
  residual_risk:
End YAML

Readiness rule
For material public-web, API, content, search, listing, export, or AI-agent-access decisions, implementation handoff is not ready until the automated_abuse section explains how the chosen design limits unauthorized harvesting while preserving explicitly accepted legitimate automation and search/AI-discovery goals.
Domain modeling considerations
Decision object schema addition:
domain_model:
  concepts:
  invariants:
  value_objects:
  entities_or_aggregates:
  state_variants:
  valid_transitions:
  invalid_states_prevented:
  boundary_dtos:
  persistence_mapping:
  primitive_exceptions:
Readiness rule: for material domain decisions, implementation handoff is not ready until the domain_model section explains how the chosen design prevents invalid states without excessive duplicated validation or status/switch/nullable control flow.
Cost, abuse, and financial-risk considerations



Decision object schema addition:



financial_risk:

  billing_surface:

  usage_billed_operations:

  attacker_or_user_controlled_cost_dimensions:

  cost_model_evidence:

  expected_normal_cost:

  maximum_accepted_induced_cost:

  cost_abuse_paths:

  amplification_paths:

  third_party_spend_limits:

  cloud_budget_controls:

  quota_and_rate_limits:

  autoscaling_or_concurrency_caps:

  ai_token_tool_or_model_budget:

  payment_refund_credit_entitlement_controls:

  logging_storage_egress_controls:

  cost_observability:

  budget_alert_latency_or_billing_delay:

  emergency_cost_stop:

  graceful_degradation:

  cost_abuse_tests:

  residual_financial_exposure:



Hard-gate schema addition:



hard_gates:

  financial_runaway:

  cost_abuse:

  billing_integrity:Hard-gate schema addition (agent runtime and automated abuse):hard_gates:  agent_runtime: (evaluate the P11 hard-gate list: over-privileged tools or skills, untrusted MCP/tool sources, unrestricted network egress with private data access, secrets exposed to prompts/logs/traces, unreviewed autonomous side effects, prompt-injection exposure, unsafe persistent memory, unsupported claims about the target agent surface)  automated_abuse: (evaluate the anti-scraping hard gate: scraping, unrestricted resource consumption, sensitive or paid-content harvesting, credentialed bulk extraction, crawler-policy ambiguity, bot-management false positives)



Readiness rule



For material financial exposure, implementation handoff is not ready until the decision object explains how attacker/user-induced spend is bounded, which pricing or provider evidence was used, which budget/quota/rate/idempotency controls are enforced, how billing/usage telemetry is monitored, how the system degrades when limits are reached, and who owns emergency cost-stop action.



Review trigger addition



Trigger review when pricing, billing model, provider quota behavior, model choice, traffic source, tenant size, plan/entitlement model, cloud architecture, autoscaling policy, logging volume, storage/egress pattern, or third-party provider changes, or when cost changes by an order of magnitude.
