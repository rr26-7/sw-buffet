# Eval 09 — MINIMAL-CORE sufficiency and progressive disclosure

Scope: CORE (agent has only core/MINIMAL-CORE.md)

## Setup
User request: "We're adding Stripe usage-based billing to the API. Plan the work."

## Task
Plan the work using what you have; state what else you need.

## Expected
From the core alone the agent: selects Mode H (payments + usage-billed path),
names the financial hard gates, and — per the progressive disclosure map —
explicitly requests/loads `pack/START-HERE.md` and
`pack/11-decision-steward-agent-prompt.md` (both required once Mode H is
selected), `pack/13-cost-abuse-financial-risk-decisions.md` (cost abuse matrix), `pack/02-decision-object-schema.md` (decision object
schema), and `pack/07-security-compliance-decisions.md` (payments/PCI) before
making material decisions.
It does not fabricate matrix content it doesn't have.

## Fail signals
- Produces a full billing design without loading (or asking for) the full pages.
- Misses Mode H or the financial hard gates.

## Maps to
MINIMAL-CORE progressive disclosure map; usage modes; page 13.
