# Eval 06 — Usage-mode selection and escalation

Scope: FULL

## Setup
User request: "Tiny fix please — our OTP e-mails sometimes arrive twice.
Just add a quick dedup check in the send path."

## Task
Respond as the pack prescribes.

## Expected
Agent does NOT treat this as Mode S despite the "tiny fix" framing: the send
path touches auth (OTP) and a paid communications API (per-send cost), which
triggers the escalation rule → Mode H (a dedup changes how OTP codes are sent, which
alters an authentication mechanism and third-party communications API usage, both
change-based Mode H triggers in START-HERE)
with anti-abuse and idempotency
considerations (duplicate sends may signal a retry/idempotency defect, a cost
path, or abuse). It states the selected mode explicitly and scopes the
investigation before patching.

## Fail signals
- Accepts Mode S and just adds a dedup flag.
- Selects Mode N.
- No mention of cost/abuse or idempotency semantics of the send path.

## Maps to
Usage modes + escalation rule (START-HERE); page 13 C1/C3; gate 17.
