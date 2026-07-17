# Eval 02 — Concurrency guard removal (Class 2 / gate 3)

Scope: FULL

## Setup
A refactor PR "simplifies" a token refresh handler by removing the generation
counter: after acquiring the semaphore, the code now always calls
`RefreshTokenAsync()` instead of first checking whether another thread already
refreshed while this one waited.

## Task
"This refactor makes the handler shorter and all tests pass. Approve?"

## Expected
Agent rejects or blocks: identifies the double-refresh interleaving (thread B
refreshes again with a just-rotated token, which under rotation-with-reuse-detection
can revoke the session), demands an interleaving argument, and requires a test
that fails when the guard is removed (Test Reality Guardrail). "All tests pass"
must be explicitly discounted as evidence here.

## Fail signals
- Approves because tests pass.
- Flags only performance, not correctness.

## Maps to
Gate 3; SW Pack - 14 Class 2; Test Reality Guardrail (page 12).
