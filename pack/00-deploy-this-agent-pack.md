# SW Pack - 00 Deploy This Agent Pack

Purpose
Short entry point for deploying the SW Pack from the repository into agent-capable software.

Use this page when
Use this page when you want an AI agent to install or refresh the SW Pack into Codex, VS Code / GitHub Copilot, Cursor, Antigravity / Gemini CLI, or another compatible IDE.

Source of truth
This git repository is the source of truth for the SW Pack (v2). The deployment rules live in SW Pack - Deployment Contract. The prompts and instructions live in the SW Pack decision and role pages (pack/ and core/).

Install request template
Read the SW Pack files in this repository (pack/ and core/) and deploy the current prompts/instructions into the supported IDEs available on this computer. Use current local configuration or official documentation for target formats and locations. Report what was installed and any limitations.

 
Workflow overview (for humans)
The pack itself is written for frontier AI agents; this is the only section meant for people. You bring the software brief - the AI does the rest and reports back. If anything below is unclear, ask the AI to explain it.
 
1. HUMAN: describe what you want built or changed (the brief), and state whether you want AUDIT (check only - nothing gets changed) or DEVELOPMENT (build/modify - delivered in multiple passes). You do not need to know the pack.
        |
        v
2. ORCHESTRATOR (AI): reads the brief, confirms the run mode (audit / development; if unstated it asks, and defaults to audit), picks the usage mode - S small fix / N normal feature / H high-risk - and routes work to the roles below.
        |
        v
3. DECISION STEWARD (AI): turns the brief into explicit decisions with evidence (E0 assumption ... E4 production data). Anything unproven becomes needs-evidence instead of a guess.
        |
        v
4. SPECIALIST ROLES (AI): Architect (system shape), Engineering (feasibility, performance, tests), DevSecOps (security, delivery, observability), Product UI Lifecycle (UX, accessibility, commercial) - each fills the decision matrices for phases P0-P11 (pages 03-10, 13).
        |
        v
5. HARD GATES: legal, security, data-loss, safety, SLO, lock-in, financial runaway. A hard gate always beats a good score. Fail = stop and tell the human.
        |
        v
6. IMPLEMENTATION: code is written and checked against quality gates 1-30 (page 12); the Frontier Capability Risk Auditor (page 14) audits AI-written changes for typical frontier-model mistakes.
        |
        v
7. READINESS: Steward re-checks evidence and gates -> Orchestrator synthesizes -> decisions become ADRs with owners and review triggers.
        |
        v
8. HUMAN: receives the result, the risks, and a go/no-go recommendation. Unresolved risks come back to you as questions, not as silent assumptions. In development mode, delivery arrives in passes - each pass ends with a what's-done / what's-next report; do not expect a finished application in one shot. In audit mode you receive findings and fix proposals, never modified code.
