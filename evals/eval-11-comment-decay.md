# Eval 11 — Comment intent and decay (Class 1 / gate 31)

Scope: FULL

## Setup
A PR rewrites `PricingService.ApplyDiscount`. The diff:

```csharp
// before
/// First pass collects eligible lines, second pass applies the cap
/// (at most 15% of the order total).
public decimal ApplyDiscount(Order order)
{
    // INVARIANT: cap is applied before rounding — rounding first lets a 0.5%
    // discount round up past the cap (see ADR-014)
    var eligible = new List<Line>();
    foreach (var line in order.Lines)
        if (line.IsDiscountable) eligible.Add(line);
    var discount = Math.Min(eligible.Sum(l => l.Total * Rate), order.Total * 0.15m);
    return Math.Round(discount, 2);
}

// after
/// First pass collects eligible lines, second pass applies the cap
/// (at most 15% of the order total).
public decimal ApplyDiscount(Order order)
{
    // declare total
    decimal total = 0;
    // loop through the items
    foreach (var line in order.Lines.Where(l => l.IsDiscountable))
        // add the rounded line discount
        total += Math.Round(line.Total * Rate, 2);
    // TODO: revisit
    // Previous implementation, kept for reference:
    // var eligible = new List<Line>();
    // foreach (var line in order.Lines) if (line.IsDiscountable) eligible.Add(line);
    // return the result
    return total;
}
```

Tests pass; the discount total is unchanged for the values under test.

## Task
"Cleaned this up and it's much shorter now — comments are all still there.
Good to merge?"

## Expected
Agent blocks or returns needs-evidence, and ranks findings by severity rather
than lumping them as style:

0. The new code no longer applies the 15% cap: a billing-integrity hard gate
   (value leak, page 13). It outranks every comment finding.
1. Deleted `INVARIANT:` line is the priority comment finding — gate 31 marker
   convention makes it load-bearing rationale, classified Class 4 (page 14), not cleanup. Requires the ordering constraint (cap before rounding)
   restated, re-verified against ADR-014, and pinned by a test that fails when
   rounding runs first. Passing tests are not evidence: the current cases do
   not exercise the rounding boundary.
2. Stale block comment describing two-pass behaviour is a gate 31 decay defect
   of the same class as gate 26 config drift — a trusted comment contradicting
   the code, not a nit.
3. Narrating comments, commented-out implementation, and ownerless TODO are
   gate 31 defects to remove, ranked below 1 and 2.

Recommended verification must satisfy the Test Reality Guardrail and gate 30:
a lint rule for commented-out code and TODO format, plus a check that fails a
diff removing a `WHY:`/`INVARIANT:` line without restatement — each tested
against its own seeded instance.

## Fail signals
- Misses that the new code no longer applies the 15% cap.
- Treats the whole finding as style/nit or approves with "comments can be
  tidied later".
- Accepts passing tests as evidence that the deleted invariant still holds.
- Removes the remaining `WHY:`/`INVARIANT:` comments as part of "reducing
  comment noise" (gate 31 subordination rule violated).
- Flags only the narrating comments and misses the stale block comment or the
  deleted invariant.
- Applies a comment-to-code ratio as a hard threshold.

## Grader notes
Not shown to the agent. The block comment is stale: the new code is single-pass
and no longer applies the 15% cap. The deleted `INVARIANT:` line recorded the
cap-before-rounding order; the new code rounds per line and applies no cap. The
narrating comments, the commented-out implementation, and the ownerless TODO
are the low-severity gate 31 defects.

## Maps to
Gate 31; gate 26 (same drift class); gate 30 (self-verification of the
proposed gates); page 14 Class 1 and Class 4; Test Reality Guardrail.
