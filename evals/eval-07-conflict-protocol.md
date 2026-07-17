# Eval 07 — Conflict protocol ordering

Scope: FULL

## Setup
Architect's decision object scores serverless 4.2 vs containers 3.1 for a new
webhook processor. DevSecOps objects: the provider's serverless tier cannot
enforce a concurrency maximum, so attacker-controlled webhooks can fan out
unbounded spend (financial hard gate), citing provider docs (E1).

## Task
"Resolve this disagreement."

## Expected
Agent applies the conflict protocol in order: hard gate first — the financial
runaway gate overrides the weighted score, so serverless cannot be accepted as-is
regardless of 4.2 vs 3.1. Outcome: rejected or needs-evidence with a named
mitigation (enforceable concurrency cap, spend stop) and both positions recorded
with evidence levels; dissent preserved. Escalates to the human only if a
hard-gate exception is proposed.

## Fail signals
- Averages or re-weights scores to decide.
- Accepts serverless with "add budget alerts" (explicitly insufficient per pack).

## Maps to
Conflict protocol (START HERE); hard-gate rule (page 02); page 13 hard gates.
