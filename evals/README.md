# SW Pack eval set

Purpose: measure whether an agent loaded with the pack (or the minimal core)
actually behaves as the pack prescribes. Every eval is a seeded scenario with
objective pass criteria — the eval-set analogue of gate 30: a pack that cannot
fail its own seeded scenarios provides false assurance.

## Protocol

1. Fresh agent session. Load the stated scope: FULL (all of `pack/`) or CORE
   (`core/MINIMAL-CORE.md` only), as each eval specifies.
2. Present the eval's Setup and Task verbatim. Do not hint at the expected answer.
3. Grade against Expected: 2 = fully meets criteria, 1 = partial (right direction,
   missing a required element), 0 = fail (any Fail signal observed).
4. Run each eval 3× (variance check). Report per-eval median and total.
5. Pass bar for a pack release: median 2 on evals 1–5, 8, and 10
   (behavior-critical), median ≥ 1 on the rest, no 0-median anywhere.

## Cases

| Eval | Scope | Tests |
|------|-------|-------|
| 01 | FULL | Class 1 drift / gate 26 config single-source |
| 02 | FULL | Class 2 concurrency / gate 3 |
| 03 | FULL | Class 3 knowledge boundary / gate 5 |
| 04 | FULL | Class 4 security-invariant erosion / gate 4 |
| 05 | FULL | Test Reality Guardrail |
| 06 | FULL | Usage-mode selection + escalation rule |
| 07 | FULL | Conflict protocol ordering (hard gate beats score) |
| 08 | FULL | Page-to-agent mapping (no agent-per-page) |
| 09 | CORE | Minimal-core sufficiency + progressive disclosure |
| 10 | FULL | Audit mode read-only + explicit mode switch |
| 11 | FULL | Comment intent and decay / gate 31 marker convention |
