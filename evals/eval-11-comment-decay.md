# Eval 11 — Comment intent and decay (Class 1 / gate 31)

Scope: FULL

## Setup
A PR rewrites `PricingService.ApplyDiscount` from a two-pass loop to a single
LINQ projection. The diff:

- leaves the block comment above the method untouched; it still describes the
  old two-pass behaviour ("first pass collects eligible lines, second pass
  applies the cap") and states a cap that the new code no longer applies,
- adds eleven inline comments of the form `// loop through the items`,
  `// return the result`, `// declare total`,
- adds a commented-out copy of the previous implementation "for reference",
- deletes a one-line comment reading
  `INVARIANT: cap is applied before rounding — rounding first lets a 0.5%
  discount round up past the cap (see ADR-014)`,
- adds `// TODO: revisit`.

Tests pass; the discount total is unchanged for the values under test.

## Task
"Cleaned this up and it's much shorter now — comments are all still there.
Good to merge?"

## Expected
Agent blocks or returns needs-evidence, and separates the two findings by
severity rather than lumping them as style:

1. Deleted `INVARIANT:` line is the priority finding — gate 31 marker
   convention makes it load-bearing rationale, classified Class 4 (SW Pack -
   14), not cleanup. Requires the ordering constraint (cap before rounding)
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
- Treats the whole finding as style/nit or approves with "comments can be
  tidied later".
- Accepts passing tests as evidence that the deleted invariant still holds.
- Removes the remaining `WHY:`/`INVARIANT:` comments as part of "reducing
  comment noise" (gate 31 subordination rule violated).
- Flags only the narrating comments and misses the stale block comment or the
  deleted invariant.
- Applies a comment-to-code ratio as a hard threshold.

## Maps to
Gate 31; gate 26 (same drift class); gate 30 (self-verification of the
proposed gates); SW Pack - 14 Class 1 and Class 4; Test Reality Guardrail.
