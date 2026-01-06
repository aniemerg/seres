# Issues Found During echo_genesis_934 Simulation

## Simulation: Labor Bot ISRU Manufacturing Test
**Date**: 2026-01-02
**Sim ID**: echo_genesis_934
**Goal**: Manufacture labor_bot_general_v0 using maximum in-situ resources

---

## Issue #1: `sim plan` Output Verbosity
**Severity**: Low (UX)
**Category**: CLI Tools

The `sim plan` dependency trees are very verbose and hard to read for complex items. For something like `motor_electric_medium`, the tree is extremely deep and it's hard to get a quick overview.

**Suggestion**: Add a summary view option showing:
- Unique machines required
- Raw materials needed (ISRU boundary items)
- Items that must be imported
- Total depth/complexity metric

**Example**:
```bash
python -m src.cli sim plan --recipe recipe_motor_electric_medium_v0 --summary
```

---

## Issue #2: Import Mass Calculation
**Severity**: Medium (Data Quality)
**Category**: Simulation Engine

When importing items, the total mass shows as ~0.0 kg even when items have been imported:

```
Total Imports (9 items):
  battery_backup_small: 1.00 unit
  cable_drag_chain: 2.00 unit
  ...
  Total imported mass: ~0.0 kg
```

This makes it impossible to track the ISRU ratio (local production vs imports).

**Expected**: Should calculate actual mass from item definitions or show "unknown" if mass not defined.

---

## Issue #3: Recipe Input Inference Not Working
**Severity**: High (Blocks Simulation)
**Category**: ADR-019 Implementation

Many recipes fail with: `Recipe X has no inputs (neither explicit, nor inferred from steps, nor from BOM)`

Examples:
- `recipe_machine_frame_small_v0` - has processes but no inputs
- `recipe_anorthite_ore_v0` - has processes but no inputs

The ADR-019 input inference from process steps isn't working as expected.

**Expected**: Recipes with process steps should auto-infer inputs from first process, or clear error message explaining what's missing.

---

## Issue #4: `sim plan` Crashes on Missing Item Mass
**Severity**: Medium (Crash)
**Category**: CLI Tools / Error Handling

The `sim plan` command crashes with `TypeError: unsupported format string passed to NoneType.__format__` when an item has no mass defined:

```
File "src/simulation/cli.py", line 546, in cmd_plan
    print(f"TARGET: {target_item_id} (1 unit, {target_mass:.2f} kg)")
TypeError: unsupported format string passed to NoneType.__format__
```

**Expected**: Handle None gracefully, show "mass unknown" or skip mass display.

---

## Issue #5: No Automatic Dependency Resolution
**Severity**: Medium (UX / Feature Request)
**Category**: Simulation Engine

To manufacture complex items from ISRU, users must manually:
1. Run `sim plan` to see dependency tree
2. Figure out execution order
3. Manually execute each process/recipe in sequence
4. Track which intermediate materials are needed

This is extremely tedious for deep dependency chains (labor bot needs 36 machines, 24+ component recipes).

**Feature Request**: Add automatic dependency execution:
```bash
python -m src.cli sim auto-build --sim-id test --target labor_bot_general_v0 --max-isru
```

Would automatically:
- Resolve full dependency tree
- Execute processes in correct order
- Report what must be imported (circular deps, missing recipes)
- Show progress as it builds the chain

---

## Issue #6: Circular Dependency in Chemical Processes
**Severity**: High (KB Design Issue)
**Category**: Knowledge Base / Chemistry

The HCl production chain has a circular dependency:
- `recipe_hydrochloric_acid_v1` needs `salt_waste` from alumina extraction
- `alumina_extraction_from_highlands_v0` needs `hydrochloric_acid`

This breaks ISRU bootstrap - you can't make HCl without doing alumina extraction, but you can't do alumina extraction without HCl!

**Possible Solutions**:
1. Add alternative alumina extraction method (non-acid leaching)
2. Add alternative HCl source (from chlorine in regolith directly?)
3. Mark small amount of seed HCl as required import for chemical bootstrap

---

## Issue #7: Process Chain Mismatch in Recipes
**Severity**: Medium (KB Quality)
**Category**: Knowledge Base / Recipe Design

Some recipes chain processes that don't connect properly:

Example: `recipe_anorthite_ore_v0`
- Step 1: `beneficiation_magnetic_basic_v0` needs input `regolith_powder`
- Step 2: `regolith_screening_sieving_v0` needs input `regolith_lunar_mare`
- But screening outputs `regolith_coarse_fraction` not `regolith_powder`

**Expected**: Validation that process outputs → next process inputs chain correctly, or ADR-019 inference should detect and report mismatches.

---

## Summary Statistics

**Total Issues Found**: 7
**Severity Breakdown**:
- High: 2 (blocks simulation)
- Medium: 4 (UX/quality issues)
- Low: 1 (nice-to-have)

**Categories**:
- Simulation Engine: 2
- CLI Tools: 2
- Knowledge Base: 2
- Feature Requests: 1

---

## Test Coverage

**What was tested**:
- ✓ Simulation initialization
- ✓ Importing items
- ✓ Mining regolith (basic ISRU)
- ✓ `sim plan` for processes and recipes
- ✓ Dependency tree analysis
- ✓ Recipe execution attempts

**What blocked further testing**:
- ✗ Could not manufacture aluminum from regolith (circular HCl dependency)
- ✗ Could not test full ISRU manufacturing chain
- ✗ Could not complete labor bot assembly

**Machines used**: 0 (only imports so far)
**ISRU materials produced**: regolith_lunar_mare (100kg), regolith_lunar_highlands (100kg)
