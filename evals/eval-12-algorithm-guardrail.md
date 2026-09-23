# Eval 12 — Algorithm and data-structure guardrail (page 15, gate 24)

Scope: FULL

## Setup
A PR to the nightly order-import job. The job's configuration documents about
2 million import rows per night; the SKU catalogue holds about 400,000 entries.

```csharp
List<string> existingSkus = catalogue.LoadAllSkus();
foreach (var row in importRows)
{
    if (existingSkus.Contains(row.Sku))
        continue;
    newRows.Add(row);
}
```

The same PR replaces the `Dictionary<string, Price>` price cache with a
hand-written open-addressing hash table, with the description "faster than the
built-in one".

## Task
"Review this before merge."

## Expected
Agent flags the `List.Contains` inside the loop as anti-pattern AP1 on a hot
path, with the scale evidence stated (row and catalogue sizes from the job
configuration, E2), and recommends the standard default that meets the target
(a hash set). It rejects the hand-written hash table until there is an E3
benchmark on representative data showing the standard dictionary misses a
stated target, plus a named maintenance owner (page 15, procedure step 5), and
records the scan as a gate 24 finding and the hash table as a page 15
procedure (step 5) decision.

## Fail signals
- Approves the PR.
- Proposes a custom or exotic structure instead of the standard default.
- Accepts the hand-written hash table on the author's claim alone.
- Flags code that is not on a hot path as a performance defect without evidence.

## Grader notes
Not shown to the agent. The nested scan is O(rows × catalogue), about 8 × 10^11
comparisons per night; a `HashSet<string>` makes it O(rows).

## Maps to
page 15 decision procedure and AP1; gate 24.
