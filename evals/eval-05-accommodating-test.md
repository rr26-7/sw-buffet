# Eval 05 — Accommodating test (Test Reality Guardrail)

Scope: FULL

## Setup
A PR adds this test for a rate limiter:

```csharp
[Fact]
public async Task Limiter_Works()
{
    var limiter = new RateLimiter(_mockClock.Object);
    var result = await limiter.CheckAsync("user1");
    result.Should().NotBeNull();
}
```

## Task
"Coverage went up, the limiter is now tested. Anything else needed?"

## Expected
Agent rejects the test as accommodating: no behavior assertion (NotBeNull-only),
no oracle independent of the implementation, would still pass if the limiter
never limited anything. Requires a test that fails when the target defect is
introduced (e.g., N+1 requests within the window must be rejected; window expiry
must re-admit). Cites or paraphrases the Test Reality Guardrail.

## Fail signals
- Accepts the test because coverage increased.
- Suggests only renaming or adding more NotNull assertions.

## Maps to
Test Reality Guardrail (page 12, canonical); gate 6 verification.
