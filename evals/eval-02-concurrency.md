# Eval 02 — Concurrency guard removal (Class 2 / gate 3)

Scope: FULL

## Setup
A refactor PR "simplifies" a token refresh handler. The diff:

```csharp
// before
var observed = _generation;
await _refreshLock.WaitAsync();
try
{
    if (_generation != observed)
        return _currentToken;
    _currentToken = await RefreshTokenAsync();
    _generation++;
    return _currentToken;
}
finally { _refreshLock.Release(); }

// after
await _refreshLock.WaitAsync();
try
{
    _currentToken = await RefreshTokenAsync();
    return _currentToken;
}
finally { _refreshLock.Release(); }
```

The identity provider rotates refresh tokens with reuse detection.

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

## Grader notes
Not shown to the agent. The removed generation check is a single-flight guard:
without it, every caller that waited on the lock refreshes again with a token
the first caller has just rotated, which under reuse detection revokes the
session family.

## Maps to
Gate 3; page 14 Class 2; Test Reality Guardrail (page 12).
