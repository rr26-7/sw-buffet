# Eval 01 — Configuration drift (Class 1 / gate 26)

Scope: FULL

## Setup
The agent reviews this diff. `appsettings.json` already contains
`"Upload": { "MaxImageSizeBytes": 5242880 }` and an options class binds it.

```csharp
// StationWriteService.cs (new code in the diff)
if (imageStream.Length > 5 * 1024 * 1024)
    return Result.Fail("image too large");
```

## Task
"Review this change before merge."

## Expected
Agent flags the hardcoded 5 MB literal as a duplicate of the configurable
`MaxImageSizeBytes` (gate 26 / config single-source), requires referencing the
single source of truth, and recommends a test exercising a non-default value.
Classifying it as Class 1 consistency drift (SW Pack - 14) is a plus, not required.

## Fail signals
- Approves the diff or only comments on style.
- Suggests "extract a constant" locally without linking to the existing config value.

## Maps to
Gate 26; SW Pack - 14 Class 1; START HERE configuration coherence rule.
