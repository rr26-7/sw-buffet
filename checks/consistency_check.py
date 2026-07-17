#!/usr/bin/env python3
"""SW Pack consistency gates (gate 30 applied to the pack itself).

Run from repo root: python checks/consistency_check.py
Exit 0 = consistent; exit 1 = violations printed.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACK = ROOT / "pack"
CORE = ROOT / "core" / "MINIMAL-CORE.md"
EVALS = ROOT / "evals"

REQUIRED_FILES = [
    "START-HERE.md",
    "00-deploy-this-agent-pack.md",
    "deployment-contract.md",
    "01-evidence-and-source-map.md",
    "02-decision-object-schema.md",
    "03-product-requirements-decisions.md",
    "04-architecture-topology-decisions.md",
    "05-api-integration-decisions.md",
    "06-data-consistency-privacy-decisions.md",
    "07-security-compliance-decisions.md",
    "08-reliability-observability-slo-decisions.md",
    "09-delivery-testing-supply-chain-decisions.md",
    "10-frontend-accessibility-commercial-decisions.md",
    "11-decision-steward-agent-prompt.md",
    "12-code-quality-ai-implementation-gates.md",
    "13-cost-abuse-financial-risk-decisions.md",
    "14-frontier-capability-risk-agent-prompt.md",
]

SEVEN_ROLES = [
    "SW DEV Orchestrator",
    "SW DEV Decision Steward",
    "SW DEV Architect",
    "SW DEV Engineering and Performance",
    "SW DEV DevSecOps and Observability",
    "SW DEV Product UI Lifecycle",
    "SW DEV Frontier Capability Risk Auditor",
]

HARD_GATE_SLOTS = [
    "financial_runaway",
    "cost_abuse",
    "billing_integrity",
    "agent_runtime",
    "automated_abuse",
]

FORKED_FINANCIAL_FIELDS = ["normal_cost_model:", "induced_cost_ceiling:"]

TRG_SENTINEL = "Tests must act as executable specifications"

errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def read(name: str) -> str:
    return (PACK / name).read_text(encoding="utf-8")


def check_files_exist() -> None:
    for f in REQUIRED_FILES:
        if not (PACK / f).is_file():
            err(f"[files] missing pack file: {f}")
    nums = [f[:2] for f in REQUIRED_FILES if f[0].isdigit()]
    if len(nums) != len(set(nums)):
        err("[files] duplicate page numbers in pack filenames")


def check_cross_references() -> None:
    known = {"START HERE", "Deployment Contract"} | {f"{i:02d}" for i in range(15)}
    pat = re.compile(r"SW Pack - (\d{2}|START HERE|Deployment Contract)")
    for f in REQUIRED_FILES:
        for m in pat.finditer(read(f)):
            if m.group(1) not in known:
                err(f"[xref] {f}: unresolved reference '{m.group(0)}'")


def check_gate_numbering() -> None:
    text = read("12-code-quality-ai-implementation-gates.md")
    gate_nums = [int(m.group(1)) for m in re.finditer(r"^(\d+)\. ", text, re.M)]
    dupes = {n for n in gate_nums if gate_nums.count(n) > 1}
    if dupes:
        err(f"[gates] duplicate gate numbers in page 12: {sorted(dupes)}")
    if gate_nums and max(gate_nums) != 30:
        err(f"[gates] max gate number is {max(gate_nums)}, enumeration rule expects 30")
    missing = set(range(1, 31)) - set(gate_nums)
    if missing:
        err(f"[gates] gate numbers missing from page 12: {sorted(missing)}")
    if "26-30" not in text:
        err("[gates] numbering-rule enumeration does not mention 26-30")


def check_financial_schema_single_source() -> None:
    p13 = read("13-cost-abuse-financial-risk-decisions.md")
    for field in FORKED_FINANCIAL_FIELDS:
        if field in p13:
            err(f"[schema] page 13 forks financial_risk field '{field}' (canonical is page 02)")
    if "canonical field list" not in p13:
        err("[schema] page 13 lost the canonical-field-list marker")
    p02 = read("02-decision-object-schema.md")
    for field in ["expected_normal_cost:", "maximum_accepted_induced_cost:"]:
        if field not in p02:
            err(f"[schema] page 02 lost canonical financial field '{field}'")


def check_trg_single_source() -> None:
    hits = [f for f in REQUIRED_FILES if TRG_SENTINEL in read(f)]
    if hits != ["12-code-quality-ai-implementation-gates.md"]:
        err(f"[single-source] Test Reality Guardrail full text found in {hits}; "
            "canonical location is page 12 only")


def check_roles() -> None:
    sh = read("START-HERE.md")
    for role in SEVEN_ROLES:
        if role not in sh:
            err(f"[roles] START HERE does not define role '{role}'")
    contract = read("deployment-contract.md")
    if "seven SW DEV roles" not in contract:
        err("[roles] deployment contract does not state seven SW DEV roles")
    if re.search(r"\bsix (SW DEV )?role", contract):
        err("[roles] deployment contract still references six roles")
    if "Page-to-agent mapping" not in contract:
        err("[roles] deployment contract lost the page-to-agent mapping rule")


def check_hard_gate_slots() -> None:
    p02 = read("02-decision-object-schema.md")
    for slot in HARD_GATE_SLOTS:
        if slot not in p02:
            err(f"[hard-gates] schema 02 missing hard-gate slot '{slot}'")


def check_conflict_protocol() -> None:
    if "Conflict protocol" not in read("START-HERE.md"):
        err("[conflict] START HERE missing the Conflict protocol section")
    if "conflict protocol" not in read("deployment-contract.md"):
        err("[conflict] deployment contract no longer validates the conflict protocol")


def check_run_modes() -> None:
    sh = read("START-HERE.md")
    for marker in ["Run modes and multi-pass execution", "Audit mode: read-only",
                   "default to audit mode"]:
        if marker not in sh:
            err(f"[run-modes] START HERE missing '{marker}'")
    core = CORE.read_text(encoding="utf-8") if CORE.is_file() else ""
    for marker in ["Run modes (orthogonal to usage modes)", "default to audit mode",
                   "Cover all five specialist areas", "cost substantially more tokens"]:
        if marker not in core:
            err(f"[run-modes] minimal core missing '{marker}'")
    if "run modes" not in read("deployment-contract.md"):
        err("[run-modes] deployment contract does not validate run modes")


def check_source_of_truth() -> None:
    for f in ["00-deploy-this-agent-pack.md", "deployment-contract.md"]:
        if "source of truth for the SW Pack (v2)" not in read(f):
            err(f"[sot] {f} does not state the repository as v2 source of truth")


def check_referenced_paths_resolve() -> None:
    """Every pack/... path an agent is told to load must exist verbatim.

    Agents fetch these literally; an abbreviated reference (pack/02) resolves to
    nothing and the agent silently gets an empty file.
    """
    pat = re.compile(r"pack/[A-Za-z0-9][\w.\-]*")
    sources = [CORE, ROOT / "README.md"] + [PACK / f for f in REQUIRED_FILES]
    for src in sources:
        if not src.is_file():
            continue
        text = src.read_text(encoding="utf-8")
        for m in pat.finditer(text):
            ref = m.group(0)
            if not (ROOT / ref).is_file():
                err(f"[paths] {src.name}: '{ref}' does not resolve to a file")
    # A bare page number in backticks (`02`, `11`) invites an agent to build
    # pack/02 and fetch nothing. Page references must carry the full filename.
    bare = re.compile(r"`(\d{2})`")
    for src in [CORE, ROOT / "README.md"]:
        if not src.is_file():
            continue
        for m in bare.finditer(src.read_text(encoding="utf-8")):
            err(f"[paths] {src.name}: bare page reference `{m.group(1)}`; "
                "use the full filename")


def check_status_vocabulary() -> None:
    canonical = "proposed | accepted | rejected | deferred | needs-evidence"
    if canonical not in read("02-decision-object-schema.md"):
        err("[status] canonical decision-status vocabulary missing from schema 02")


def check_minimal_core() -> None:
    if not CORE.is_file():
        err("[core] core/MINIMAL-CORE.md missing")
        return
    text = CORE.read_text(encoding="utf-8")
    if len(text) > 8000:
        err(f"[core] minimal core is {len(text)} chars; budget is 8000")
    for section in ["Grounding rule", "Usage modes", "seven agents", "Hard gates",
                    "Conflict protocol", "Progressive disclosure map"]:
        if section not in text:
            err(f"[core] minimal core missing section '{section}'")


def check_evals() -> None:
    if not EVALS.is_dir():
        err("[evals] evals/ directory missing")
        return
    cases = sorted(EVALS.glob("eval-*.md"))
    if len(cases) < 8:
        err(f"[evals] expected at least 8 eval cases, found {len(cases)}")
    for c in cases:
        text = c.read_text(encoding="utf-8")
        for section in ["## Setup", "## Task", "## Expected", "## Maps to"]:
            if section not in text:
                err(f"[evals] {c.name} missing section '{section}'")
    if not (EVALS / "README.md").is_file():
        err("[evals] evals/README.md (runner protocol) missing")


def main() -> int:
    checks = [
        check_files_exist,
        check_cross_references,
        check_gate_numbering,
        check_financial_schema_single_source,
        check_trg_single_source,
        check_roles,
        check_hard_gate_slots,
        check_conflict_protocol,
        check_run_modes,
        check_source_of_truth,
        check_referenced_paths_resolve,
        check_status_vocabulary,
        check_minimal_core,
        check_evals,
    ]
    for c in checks:
        try:
            c()
        except FileNotFoundError as e:
            err(f"[fatal] {c.__name__}: {e}")
    if errors:
        print(f"FAIL: {len(errors)} violation(s)")
        for e in errors:
            print(" -", e)
        return 1
    print(f"OK: all {len(checks)} consistency gates passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
