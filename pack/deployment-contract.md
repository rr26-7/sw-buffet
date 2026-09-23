# sw-buffet deployment-contract: Deploying the Pack to Agent Surfaces

Purpose
This page defines how to deploy sw-buffet prompts and instructions from the repository into agent-capable software. It is declarative: it names the source content, generated artifact types, and validation expectations. It is not a local package, installer script, byte archive, or fixed path map.

Source of truth
This git repository is the source of truth for sw-buffet. Authoritative content lives in the readable sw-buffet pages: START-HERE, page 00 (Deploy This Agent Pack), this deployment-contract, page 01 (Evidence and Source Map), page 02 (Decision Object Schema), the decision matrices (pages 03-10, 13, and 15), page 11 (Decision Steward Agent Prompt), page 12 (Code Quality AI Implementation Gates), and page 14 (Frontier Capability Risk Agent Prompt), plus core/MINIMAL-CORE.md.

Deployment principle
A capable AI agent should read sw-buffet files (pack/ and core/) of one tagged release or pinned commit of the repository, never a moving branch, loaded raw, discover which supported IDEs or agent surfaces are installed or requested, check current vendor documentation or local configuration when the target format/location is uncertain, and generate the appropriate agent/rule/instruction files for those surfaces. Do not preserve a local source package folder. Temporary staging files are acceptable only during deployment and should be removed afterwards.

Supported surfaces
Every surface gets the same mapping: shared instructions go to the surface's project or user instruction file, the seven role prompts to its subagent or skill mechanism where one exists, decision phases, schemas, and gates to skills or rules, and approval gates to its hook or permission mechanism where one exists. Where a surface supports only instructions or rules, install those and state the limitation.
- Claude Code: project or user instructions (CLAUDE.md), subagents, skills, hooks, MCP, and permissions where the current surface supports them.
- Claude Desktop / Cowork: skills and connectors (MCP) where the current surface supports them; per-application and per-action approvals are the approval boundary.
- Claude Agent SDK / OpenAI Agents SDK: programmatic agents with tool allowlists, permission or approval modes, and hooks or guardrails where the current SDK supports them.
- Codex: project or user instructions (AGENTS.md), skills, subagents, and approvals where the current surface supports them.
- VS Code / GitHub Copilot: custom instructions, custom agents, prompt files, skills, and MCP where the current surface supports them.
- Cursor: rules, AGENTS.md, subagents, skills, hooks, and MCP where the current surface supports them.
- Antigravity / Gemini CLI: context files (GEMINI.md), rules, skills, custom agents, and MCP where the current surface supports them.
- Qwen Code: AGENTS.md-style guidance, subagents, skills, hooks, and MCP where the current surface supports them.
- Kimi CLI: shared instructions and role prompts where the current surface supports them.
- Other IDEs: generate equivalent role prompts, shared instructions, and project-local rules if the IDE supports them.
Validation: before deploying to a surface, verify its current official documentation (links: page 01, agent surface source maps). Support for subagents, skills, hooks, permissions, and MCP differs per surface and changes fast.
P11 runtime governance is expressed as enforceable configuration where the surface supports it (permissions, allowed tools, sandbox, hooks), not only as prose instructions.

Generated content model
- Shared instructions: decision phases, evidence policy, decision object schema, conflict gate, usage modes, code quality implementation gate, and source map.
- Role prompts: generate prompts for the seven roles from their definitions in START-HERE (the Role cards section plus Agent ownership). Dedicated prompt pages exist only for Decision Steward (page 11) and Frontier Capability Risk Auditor (page 14); the other five role prompts are derived from START-HERE content - no dedicated pages are required or implied.
- Project-local guidance: AGENTS.md or equivalent, plus docs/agentic-decisions style references when useful for a repository.
- Tool-specific wrappers: frontmatter, manifest files, plugin descriptors, folder layout, and file names required by the current IDE. These wrappers are generated from current docs/local conventions and are not source-of-truth content.

Deployment validation
- Confirm which target surfaces were detected or requested.
- Confirm which files/artifacts were written and why they match the current target surface.
- Record the pack release tag or commit that the generated files were rendered from, in the deployment report and in each generated file where the surface allows a comment or metadata field.
- Confirm the installed/generated content includes usage modes, run modes (audit | development, multi-pass rule, audit-default fallback), code quality implementation gate, final readiness checklist, conflict protocol, audit usage mode and audit execution policy, run-mode change rule, human approval rule, subagent entry rule, and the seven role prompts.
- Do not claim unsupported subagent or handoff behavior. If a surface only supports rules/instructions, install rules/instructions and state the limitation.
- Generated instruction files are renderings of one pack release; the surface loads them as project or user instructions. Content the agent later examines in a target repository stays data (page 12 gate 5).
- Do not embed user-specific absolute source paths in the pack content. Installed output paths may be reported after deployment as environment facts, not as source-of-truth rules.

Update rule
When a new sw-buffet release is tagged, regenerate installed agent/rule/instruction outputs from that release's files. Do not edit generated IDE files as the canonical source.

Non-goals
- No byte archive.
- No hash inventory: the release tag is the version record.
- No hardcoded local package directory.
- No permanent install script requirement.
- No fixed vendor path assumptions when the vendor surface may change.

Agent runtime deployment controls
Deployment content model addition: generated outputs must include P11 Agent runtime, tooling, and governance guidance, plus the handoff contract from each role's card (START-HERE Role cards; page 11 and page 14 for the two dedicated roles).
Deployment validation addition: confirm the target surface supports the generated behavior. If it supports only instructions/rules, install instructions/rules and state that subagent, handoff, hook, approval, sandbox, or skill behavior is not guaranteed by that surface.
Skill/plugin validation addition: generated skills/plugins must have concise descriptions for progressive disclosure, scoped tool guidance, provenance/source notes, and no hidden broad permissions. Installed content must not grant tool or shell access merely because sw-buffet role name implies expertise.
Role prompt update rule: older waterfall wording is superseded by the Role cards section of START-HERE. Specialist roles are bounded capabilities started by the Orchestrator, at the Decision Steward's request where the pack says so, according to the selected usage mode; they are not required to produce large standalone artifacts unless the decision risk calls for it.
Cost, abuse, and financial-risk considerations



Deployment content model addition



Generated outputs must include cost-abuse and financial-risk guidance when the target surface supports shared instructions, role prompts, skills, or rules. This includes decision-phase guidance, decision-object fields, implementation gates, and the dedicated page 13 (Cost Abuse Financial Risk Decisions).



Deployment validation addition



Confirm that installed/generated content includes financial hard gates, cost-abuse examples, cloud cost-control requirements, and evidence rules for pricing, quotas, budgets, billing telemetry, and provider-specific limits. Do not claim that budget alerts alone prevent spend unless the provider documentation and local automation prove an enforceable stop action.
Domain modeling considerations
Deployment validation addition: generated/installed content must include the domain model and type safety phase, the anti-slop implementation gates, and role guidance for DTO-boundary mapping, rich domain types, explicit state variants, and accepted primitive exceptions. If a target IDE only supports generic instructions, include this guidance in the shared instructions.

Anti-scraping and automated-abuse considerations

Deployment content model addition
Generated outputs must include anti-scraping and automated-abuse guidance when the target surface supports shared instructions, rules, skills, implementation gates, or decision schemas. This includes the operating rule, automated_abuse decision-object fields, implementation gates, source anchors, and the rule that robots.txt is not an access-control mechanism.

Deployment validation addition
Confirm that installed/generated content includes scrape-worthy surface identification, crawler/AI-agent policy verification, rate limits/quotas, anti-enumeration controls, WAF/CDN/bot-management assumptions, observability requirements, false-positive handling, and official-source verification for current crawler/provider behavior.
 
Page-to-agent mapping (anti-misinterpretation rule)
The pack defines exactly seven roles. Pages are content artifacts, not agents. Decision matrices (pages 03-10, 13, 15), the schema (page 02), the evidence map (page 01), and the gates (page 12) deploy as shared instructions or skills that any role consults; never instantiate an agent per page and never treat matrix text as a standalone role prompt or persona. Only page 11 and page 14 are dedicated role prompts; the other five role prompts derive from START-HERE. Orchestrator invokes roles; roles consult matrices. On surfaces without subagents, a single agent assumes the seven roles sequentially, keeping role boundaries explicit in its reasoning; while executing one role it must not adopt instructions scoped to another role or to a matrix as its own identity.
