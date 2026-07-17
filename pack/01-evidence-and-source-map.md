# SW Pack - 01 Evidence and Source Map

Last checked
2026-05-24.

Evidence policy
Use primary sources first: official standards pages, official specifications, official product docs, repo evidence, tests, prototypes, telemetry, audit logs, or legal text. Secondary articles can suggest questions, but they do not decide the matrix.

Evidence levels
E0 - Assumption: explicitly labeled, must not decide high-risk items alone.
E1 - Official documentation: standards, specifications, vendor docs, legal/regulatory source.
E2 - Local evidence: repository code, configuration, logs, CI output, issue tracker, existing architecture docs.
E3 - Experiment: prototype, benchmark, contract test, threat model exercise, accessibility audit, migration rehearsal.
E4 - Production evidence: telemetry, incidents, SLO/error-budget history, audit results, cost reports, support tickets.

Core architecture and quality sources
ISO/IEC/IEEE 42010:2022 - Architecture description: https://www.iso.org/standard/74393.html
ISO/IEC 25010:2023 - Product quality model: https://www.iso.org/standard/78176.html
C4 model: https://c4model.com/
arc42 architecture template: https://arc42.org/

API and integration sources
HTTP Semantics RFC 9110: https://www.rfc-editor.org/rfc/rfc9110
OpenAPI latest specification: https://spec.openapis.org/oas/latest.html
gRPC core concepts: https://grpc.io/docs/what-is-grpc/core-concepts/
GraphQL learning/spec entry point: https://graphql.org/learn/
WHATWG WebSockets living standard: https://websockets.spec.whatwg.org/
W3C WebTransport: https://www.w3.org/TR/webtransport/
HTML Server-Sent Events: https://html.spec.whatwg.org/multipage/server-sent-events.html
WebRTC: https://www.w3.org/TR/webrtc/
MDN WebTransport API and browser compatibility: https://developer.mozilla.org/en-US/docs/Web/API/WebTransport_API

Security, privacy, compliance, and supply chain sources
OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
OWASP Secure Coding Practices: https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/
OWASP Cheat Sheet Series: https://owasp.org/www-project-cheat-sheets/
OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
OWASP Agentic Skills Top 10: https://owasp.org/www-project-agentic-skills-top-10/
OpenSSF Scorecard: https://openssf.org/scorecard/
NIST SP 800-218 SSDF: https://csrc.nist.gov/pubs/sp/800/218/final
SLSA: https://slsa.dev/
SPDX: https://spdx.dev/
CycloneDX: https://cyclonedx.org/
GDPR Article 5 principles: https://gdpr-info.eu/art-5-gdpr/
GDPR Article 25 data protection by design/default: https://gdpr-info.eu/art-25-gdpr/
California CCPA official AG page: https://oag.ca.gov/privacy/ccpa
PCI Security Standards Council: https://www.pcisecuritystandards.org/

Reliability, operations, and delivery sources
Google SRE workbook - implementing SLOs: https://sre.google/workbook/implementing-slos/
OpenTelemetry docs: https://opentelemetry.io/docs/
DORA: https://dora.dev/
CNCF cloud native definition: https://github.com/cncf/toc/blob/main/DEFINITION.md
Twelve-Factor App: https://12factor.net/

Frontend, internationalization, and commercial sources
WCAG 2.2: https://www.w3.org/TR/WCAG22/
W3C Internationalization: https://www.w3.org/International/
Stripe idempotent requests: https://docs.stripe.com/api/idempotent_requests
Stripe usage-based billing: https://docs.stripe.com/billing/subscriptions/usage-based

Source-use rule
If a provider, framework, browser, database, cloud service, or payment API is selected, re-check that exact provider's official current documentation before implementation. This source map is a stable backbone, not permission to invent product-specific behavior.

Agent runtime source map
Last checked: 2026-06-07.
Agent runtime and workflow sources:
OpenAI Agents SDK overview: https://developers.openai.com/api/docs/guides/agents
OpenAI Agents SDK orchestration and handoffs: https://developers.openai.com/api/docs/guides/agents/orchestration
OpenAI Agents SDK guardrails and human review: https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
OpenAI Agents SDK sandbox agents: https://developers.openai.com/api/docs/guides/agents/sandboxes
OpenAI Agents SDK integrations and observability: https://developers.openai.com/api/docs/guides/agents/integrations-observability
OpenAI Agents SDK agent evals: https://developers.openai.com/api/docs/guides/agent-evals
Codex AGENTS.md: https://developers.openai.com/codex/guides/agents-md
Codex skills: https://developers.openai.com/codex/skills
Codex subagents: https://developers.openai.com/codex/subagents
Codex approvals and security: https://developers.openai.com/codex/agent-approvals-security
GitHub Copilot cloud/custom agents: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent
GitHub Copilot agent skills: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
Model Context Protocol: https://modelcontextprotocol.io
Agent Skills standard: https://agentskills.io
OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
OWASP Agentic Skills Top 10: https://owasp.org/www-project-agentic-skills-top-10/
Source-use rule addition: before installing or enabling a skill, plugin, MCP server, connector, custom subagent, or autonomous workflow, verify the current target surface documentation and local configuration. Do not infer support for handoffs, subagents, permissions, hooks, approvals, or sandboxing from another tool.

Claude agent surface source map
Last checked: 2026-06-10.
Claude surface sources:
Claude Code subagents: https://code.claude.com/docs/en/sub-agents
Claude Code skills: https://code.claude.com/docs/en/skills
Claude Code hooks: https://code.claude.com/docs/en/hooks
Claude Code memory (CLAUDE.md): https://code.claude.com/docs/en/memory
Claude Code MCP: https://code.claude.com/docs/en/mcp
Claude Code permissions: https://code.claude.com/docs/en/permissions
Claude Code plugins: https://code.claude.com/docs/en/plugins
Claude Code settings: https://code.claude.com/docs/en/settings
Agent Skills standard: https://agentskills.io
Source-use rule addition: Claude Desktop, Cowork, and Claude Agent SDK capabilities change frequently; verify current official documentation for the exact surface before claiming subagent, hook, sandbox, or approval behavior.
Cost, abuse, and financial-risk considerations



Cost abuse, resource consumption, and financial resilience sources



OWASP API4:2023 Unrestricted Resource Consumption: https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/

OWASP LLM10:2025 Unbounded Consumption: https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/

MITRE CWE-400 Uncontrolled Resource Consumption: https://cwe.mitre.org/data/definitions/400.html

MITRE CWE-770 Allocation of Resources Without Limits or Throttling: https://cwe.mitre.org/data/definitions/770.html

MITRE CWE-799 Improper Control of Interaction Frequency: https://cwe.mitre.org/data/definitions/799.html

AWS Budgets: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html

AWS Cost Anomaly Detection: https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html

AWS Auto Scaling capacity limits: https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html

Google Cloud budgets and alerts: https://docs.cloud.google.com/billing/docs/how-to/budgets

Google Cloud API usage caps: https://docs.cloud.google.com/apis/docs/capping-api-usage

Azure Cost Management budgets: https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets



Source facts



OWASP API4:2023 treats unrestricted resource consumption as an API risk that can cause denial of service and operational cost increases; it calls out CPU, memory, storage, network bandwidth, per-request service-provider APIs such as email/SMS/phone/biometrics, GraphQL batching, records-per-page, and third-party spending limits.



OWASP API4 includes examples where repeated password-reset SMS calls at $0.05 each can create thousands of dollars of loss in minutes, and where cloud object-storage/cache behavior can turn a normal monthly bill into a large unexpected bill. Its prevention guidance includes timeouts, payload limits, rate limits, operation-specific throttles, server-side validation, third-party spending limits, and billing alerts when hard spending limits are unavailable.



OWASP LLM10:2025 identifies unbounded consumption in LLM apps as a source of denial of service, economic loss, service degradation, model theft, and "Denial of Wallet" in pay-per-use cloud AI services. It recommends input validation, rate limits, user quotas, resource management, timeouts, throttling, sandboxing, logging, monitoring, anomaly detection, graceful degradation, and limits on queued actions.



MITRE CWE-400 describes uncontrolled resource consumption as improper control over limited resources, with common consequences including denial of service through CPU, memory, and other resource consumption. Its mitigations include architecture-level throttling, request-rate tracking, protocol scale limits, and safe failure on resource allocation errors.



AWS Budgets can track cost and usage budgets and supports actual/forecasted notifications and budget actions, but AWS documents that budget information is updated up to three times a day and that charges/notifications can lag behind usage.



AWS Cost Anomaly Detection uses machine learning to detect anomalous spend patterns and can report root-cause dimensions such as service, account, region, and usage type, but AWS documents that Cost Explorer data can lag up to 24 hours and new monitors/services need time before detection is effective.



AWS Auto Scaling groups have minimum and maximum capacity limits; maximum capacity is a relevant cost and availability guardrail for autoscaling systems.



Google Cloud budgets track costs and can notify or trigger Pub/Sub automation, but Google explicitly states that setting a budget does not automatically cap usage or spending. Google also documents several-hour notification delays and says API usage caps are service-specific, not project-wide spending caps, with quota-enforcement latency requiring buffer.



Azure Cost Management budgets support actual and forecasted cost alerts and action groups. Microsoft documents that budget threshold notifications are normally sent within an hour of evaluation and that action groups can trigger automation such as Azure Functions or webhooks.



Source-use rule addition



For any material cost or billing decision, re-check the exact provider, product, pricing, quota, budget, anomaly, autoscaling, payment, AI/model, communications, logging, storage, egress, CI/CD, or third-party API documentation before implementation. Use local billing data, telemetry, cost forecasts, and bounded tests where possible; otherwise label the cost model as an assumption.

Code intelligence and graph analysis sources
Graph-based code analysis (code knowledge graphs, code property graphs, call/data-flow graphs) yields E2/E3 evidence and is preferred over plain text search for impact, dependency, architecture, and security analysis.
Code Property Graph (Joern): https://docs.joern.io/code-property-graph/
CPG specification: https://github.com/ShiftLeftSecurity/codepropertygraph
CodeQL: https://codeql.github.com/docs/
Sourcegraph code intelligence: https://sourcegraph.com/docs
codebase-memory-mcp (knowledge graph MCP server): https://github.com/DeusData/codebase-memory-mcp
CodeGraphContext (graph MCP server): https://github.com/CodeGraphContext/CodeGraphContext
Bridging Code Property Graphs and Language Models (research): https://arxiv.org/html/2603.24837v1
