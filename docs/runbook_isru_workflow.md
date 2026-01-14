# Runbook + ISRU Workflow (for Codex/Claude)

This guide explains how to create simulation runbooks that maximize local (ISRU) production, how to iterate when the KB has gaps, and how to verify provenance.

## Goal

Create automated simulation scripts (runbooks) that build machines using maximum local resource production instead of Earth imports.

## Core workflow

1. **Start from the target machine recipe**
   - Identify the top-level recipe and its inputs.
   - Draft a runbook that can build the machine (baseline imports are OK to prove the recipe runs).

2. **Iterate toward ISRU**
   - Replace imports with local recipes one by one.
   - Prefer in-situ chains already in the KB.
   - Add the tooling/energy imports required to run those local chains.

3. **Run and debug**
   - Execute the runbook early and often with `.venv/bin/python`.
   - Use failures to locate KB issues (unit mismatches, missing mass, recipe I/O mismatch).

4. **Fix KB gaps (only when needed)**
   - Read the relevant KB docs before editing.
   - Make minimal corrections (units, unit_kind, masses, recipe inputs/outputs).
   - Re-run the runbook to validate the fix.

5. **Validate output and provenance**
   - Confirm the machine exists in inventory.
   - Use the provenance CLI to confirm ISRU vs imported contributions.

## Key commands

- Run a runbook:
  - `.venv/bin/python run_runbook_debug.py sim runbook --file runbooks/<name>.md`
- View state:
  - `.venv/bin/python -m src.cli sim view-state --sim-id <sim_id>`
- Provenance breakdown:
  - `.venv/bin/python -m src.cli sim provenance --sim-id <sim_id>`
  - Per-item detail: `--item <item_id>`
  - JSON output: `--json`

## Modularity (important)

When you need an intermediate machine or part:
- Check if a runbook already exists for it.
- If it exists, reuse it; if not, create a new runbook for that subcomponent.

## Machine Runbook Queue

If asked to use the queue:
- Create an empty runbook file first to reserve the slot.
- Add it to `runbooks/machine_runbook_queue.md`.

## Runbook structure guidance

Keep the runbook staged for clarity:
- **Baseline imports + initial build** (proves the recipe works).
- **Local subcomponents** (replace imports with in-situ recipes).
- **Final assembly** (build the target machine with more ISRU coverage).

## Provenance expectations

**IMPORTANT**: When working on a runbook for a specific machine, the ISRU percentage you're optimizing is **that machine's ISRU**, not the overall simulation ISRU.

Use the provenance CLI to:
- Check the specific machine's ISRU: `--item <machine_id>` (e.g., `--item reduction_furnace_v0`)
- The overall simulation ISRU includes all imported equipment and is less relevant
- Report the machine's ISRU percentage in `machine_runbook_queue.md`
- Show what portion of the machine came from local vs imported sources

Example workflow:
```bash
# Run the runbook
.venv/bin/python run_runbook_debug.py sim runbook --file runbooks/reduction_furnace_v0_runbook.md

# Check the SPECIFIC MACHINE's ISRU (this is what matters!)
.venv/bin/python -m src.cli sim provenance --sim-id reduction_furnace_v0_runbook --item reduction_furnace_v0

# Update the queue with the machine's ISRU percentage
```

The goal is to maximize the percentage of the target machine that comes from local resources, even if you need to import fabrication equipment to produce those local components.

## Improving the KB to Enable ISRU

**It is good and encouraged to improve the KB when it helps unlock better ISRU!** However, improvements must follow conservative principles to maintain KB quality.

### When to Improve the KB

Improve the KB when you discover:
- **Missing recipes for local production** (e.g., no recipe exists for producing a part from regolith)
- **Mass/unit mismatches** that prevent recipes from running (like the reduction_furnace_shell 520kg vs 495kg issue)
- **Missing processes** that would enable local material transformation
- **Incorrect material flows** that prevent ISRU chains from connecting

### How to Improve the KB (The Right Way)

**CRITICAL**: Always follow conservative principles. Read these docs BEFORE making KB changes:

1. **[docs/conservative_mode_guide.md](conservative_mode_guide.md)** - Core principle: minimize new creation, maximize reuse
   - Don't create new items if existing ones can be reused
   - Don't create phase variants (water_vapor, water_liquid) - use process transformations
   - Search for existing equivalents before creating anything

2. **[docs/parts_and_labor_guidelines.md](parts_and_labor_guidelines.md)** - Guidelines for part masses, complexity, labor
   - Use conservative mass estimates
   - Include proper labor_hours and machine_hours
   - Follow established patterns for similar parts

3. **[docs/material_class_system.md](material_class_system.md)** - Material classification rules
   - Assign correct material_class to new items (for future use)
   - **NOTE**: Material class substitution is currently DISABLED - recipes must use exact item_id
   - Understand material properties and processing

4. **[docs/knowledge_acquisition_protocol.md](knowledge_acquisition_protocol.md)** - Structured extraction principles
   - Preserve provenance and uncertainty
   - Use explicit source tags when estimating
   - Model what matters first (mass/energy/time)

5. **[docs/kb_schema_reference.md](kb_schema_reference.md)** - Schema requirements
   - Follow current schema standards (012/014/016)
   - Validate your changes with the KB validation tools

### KB Improvement Workflow

1. **Identify the gap**: What's preventing better ISRU?
2. **Root cause analysis**: Is this really missing, or does an equivalent exist?
3. **Search thoroughly**: Check kb/items/, kb/recipes/, kb/processes/ for existing solutions
4. **Minimal fix**: Make the smallest change that enables the ISRU improvement
5. **Validate**: Run validation and test the runbook to confirm it works
6. **Document**: Add notes about provenance, uncertainty, and assumptions

### Examples

**Good KB Improvement**:
- Found: No recipe for `insulation_pack_high_temp` from regolith
- Action: Created `recipe_insulation_pack_high_temp_regolith_v0` using existing `thermal_insulation_regolith_based_v0`
- Result: Enabled 18.5% ISRU for reduction_furnace_v0

**Bad KB Improvement**:
- Found: Need liquid water for a process
- Wrong: Create new item `water_liquid_v0`
- Right: Use existing `water` item with a phase-change process step

## Notes

- Prefer `.venv/bin/python` for all CLI calls.
- Keep edits minimal and consistent with KB schemas and unit conventions.
- When in doubt about KB changes, ask or consult the conservative mode guide.
