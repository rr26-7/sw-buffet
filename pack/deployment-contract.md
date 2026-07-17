# SW Pack - Deployment Contract

Purpose
This page defines how to deploy the SW Pack prompts and instructions from the repository into agent-capable software. It is declarative: it names the source content, generated artifact types, and validation expectations. It is not a local package, installer script, byte archive, or fixed path map.

Source of truth
This git repository is the source of truth for the SW Pack (v2). Authoritative content lives in the readable SW Pack pages: START HERE, 00 Deploy This Agent Pack, this Deployment Contract, 01 Evidence and Source Map, 02 Decision Object Schema, the decision matrices (03-10 and 13 Cost Abuse Financial Risk Decisions), 11 Decision Steward Agent Prompt, 12 Code Quality AI Implementation Gates, and 14 Frontier Capability Risk Agent Prompt.

Deployment principle
A capable AI agent should read the current SW Pack files from the repository (pack/ and core/), discover which supported IDEs or agent surfaces are installed or requested, check current vendor documentation or local configuration when the target format/location is uncertain, and generate the appropriate agent/rule/instruction files for those surfaces. Do not preserve a local source package folder. Temporary staging files are acceptable only during deployment and should be removed afterwards.

Supported surfaces
- Codex: project or user instructions, AGENTS.md-style guidance, and role prompts where the current Codex surface supports them.
- VS Code / GitHub Copilot: custom agents, custom instructions, prompt files, or equivalent current Copilot customization surfaces.
- Cursor: agents, rules, skills, AGENTS.md, or equivalent current Cursor customization surfaces.
- Antigravity / Gemini CLI: plugins, rules, skills, custom agents, or equivalent current surfaces.
- Other IDEs: generate equivalent role prompts, shared instructions, and project-local rules if the IDE supports them.

Generated content model
- Shared instructions: decision phases, evidence policy, decision object schema, conflict gate, usage modes, code quality implementation gate, and source map.
- Role prompts: generate prompts for the seven SW DEV roles from their definitions in START HERE (Agent ownership plus role-card addenda). Dedicated prompt pages exist only for Decision Steward (SW Pack - 11) and Frontier Capability Risk Auditor (SW Pack - 14); the other five role prompts are derived from START HERE content - no dedicated pages are required or implied.
- Project-local guidance: AGENTS.md or equivalent, plus docs/agentic-decisions style references when useful for a repository.
- Tool-specific wrappers: frontmatter, manifest files, plugin descriptors, folder layout, and file names required by the current IDE. These wrappers are generated from current docs/local conventions and are not source-of-truth content.

Deployment validation
- Confirm which target surfaces were detected or requested.
- Confirm which files/artifacts were written and why they match the current target surface.
- Confirm the installed/generated content includes usage modes, run modes (audit | development, multi-pass rule, audit-default fallback), code quality implementation gate, final readiness checklist, conflict protocol, and the seven role prompts.
- Do not claim unsupported subagent or handoff behavior. If a surface only supports rules/instructions, install rules/instructions and state the limitation.
- Do not embed user-specific absolute source paths in the pack content. Installed output paths may be reported after deployment as environment facts, not as source-of-truth rules.

Update rule
When the SW Pack changes in the repository, regenerate installed agent/rule/instruction outputs from the repository files. Do not edit generated IDE files as the canonical source.

Non-goals
- No byte archive.
- No hash inventory.
- No hardcoded local package directory.
- No permanent install script requirement.
- No fixed vendor path assumptions when the vendor surface may change.

Agent runtime deployment controls
Deployment content model addition: generated outputs must include P11 Agent runtime, tooling, and governance guidance, plus a role-card style handoff contract for each SW DEV role.
Deployment validation addition: confirm the target surface supports the generated behavior. If it supports only instructions/rules, install instructions/rules and state that subagent, handoff, hook, approval, sandbox, or skill behavior is not guaranteed by that surface.
Skill/plugin validation addition: generated skills/plugins must have concise descriptions for progressive disclosure, scoped tool guidance, provenance/source notes, and no hidden broad permissions. Installed content must not grant tool or shell access merely because the SW Pack role name implies expertise.
Role prompt update rule: older waterfall wording is superseded by role-card addenda. Specialist roles are bounded capabilities invoked by Orchestrator or Decision Steward according to the selected usage mode; they are not required to produce large standalone artifacts unless the decision risk calls for it.
Cost, abuse, and financial-risk considerations



Deployment content model addition



Generated outputs must include cost-abuse and financial-risk guidance when the target surface supports shared instructions, role prompts, skills, or rules. This includes decision-phase guidance, decision-object fields, implementation gates, and the dedicated page "SW Pack - 13 Cost Abuse Financial Risk Decisions".



Deployment validation addition



Confirm that installed/generated content includes financial hard gates, cost-abuse examples, cloud cost-control requirements, and evidence rules for pricing, quotas, budgets, billing telemetry, and provider-specific limits. Do not claim that budget alerts alone prevent spend unless the provider documentation and local automation prove an enforceable stop action.
Domain modeling considerations
Deployment validation addition: generated/installed content must include the domain model and type safety phase, the anti-slop implementation gates, and role guidance for DTO-boundary mapping, rich domain types, explicit state variants, and accepted primitive exceptions. If a target IDE only supports generic instructions, include this guidance in the shared instructions.

Claude agent surface (deployment)
Supported surfaces addition: Claude Code, Claude Desktop / Cowork, and Claude Agent SDK are supported target surfaces.
- Claude Code: shared instructions map to CLAUDE.md (project or user memory); the seven SW DEV role prompts map to custom subagents or skills; decision phases, schemas, and gates map to skills (SKILL.md per the Agent Skills standard) with concise descriptions for progressive disclosure; approval/validation gates may use hooks; MCP servers, plugins, and permissions follow current local configuration.
- Claude Desktop / Cowork: install skills and connectors (MCP); per-application and per-action approvals are the runtime approval boundary; do not claim hook or custom-subagent behavior on this surface unless current documentation confirms it.
- Claude Agent SDK: programmatic agents with explicit tool allowlists, permission modes, and hooks for custom orchestration.
Generated content mapping addition: P11 runtime governance must be expressed as enforceable configuration where the surface supports it (permissions, allowed tools, sandbox, hooks), not only as prose instructions.
Validation addition: before deployment, verify current Claude documentation at https://code.claude.com/docs (Claude Code) and https://agentskills.io (skills format). If a Claude surface only supports instructions/rules, install instructions and state the limitation.
Anti-scraping and automated-abuse considerations

Deployment content model addition
Generated outputs must include anti-scraping and automated-abuse guidance when the target surface supports shared instructions, rules, skills, implementation gates, or decision schemas. This includes the operating rule, automated_abuse decision-object fields, implementation gates, source anchors, and the rule that robots.txt is not an access-control mechanism.

Deployment validation addition
Confirm that installed/generated content includes scrape-worthy surface identification, crawler/AI-agent policy verification, rate limits/quotas, anti-enumeration controls, WAF/CDN/bot-management assumptions, observability requirements, false-positive handling, and official-source verification for current crawler/provider behavior.
 
Page-to-agent mapping (anti-misinterpretation rule)
The pack defines exactly seven agents - the SW DEV roles. Pages are content artifacts, not agents. Decision matrices (03-10, 13), the schema (02), the evidence map (01), and the gates (12) deploy as shared instructions or skills that any role consults; never instantiate an agent per page and never treat matrix text as a standalone role prompt or persona. Only SW Pack - 11 and SW Pack - 14 are dedicated role prompts; the other five role prompts derive from START HERE. Orchestrator invokes roles; roles consult matrices. On surfaces without subagents, a single agent assumes the seven roles sequentially, keeping role boundaries explicit in its reasoning; while executing one role it must not adopt instructions scoped to another role or to a matrix as its own identity.
