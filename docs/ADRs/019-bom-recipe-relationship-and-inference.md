# 019: BOM-Recipe Relationship and Input Inference

**Status:** Implemented
**Date:** 2026-01-02
**Last Updated:** 2026-01-25
**Decision Makers:** Project team
**Related ADRs:** 018 (Recipe Inputs/Outputs Validation), 017 (Validation and Error Detection)

## Context

### Problem Discovery

During simulation testing (documented in `design/simulation_feedback/build_complete_robot_feedback_2026_01_01.md`), a critical bug was discovered affecting machine assembly recipes:

**Symptom:** Machine assembly recipes like `recipe_machine_labor_bot_general_v0` fail with "Recipe has no inputs" error.

**Root Cause:** Machine recipes rely on BOMs (Bills of Materials) for component lists but don't specify explicit inputs. The simulation engine (ADR-018) infers inputs from process steps but doesn't check BOMs.

**Impact:**
- 104 machine recipes (5.4% of all recipes) cannot run
- GitHub Issue #3: "BUG: Recipes without explicit inputs fail to run"
- Blocks assembly workflows in simulations
- Forces manual duplication of 30+ BOM components into recipe inputs

### Architectural Question: Why Both BOMs and Recipes?

Research revealed **98.4% of machines have BOTH a BOM and at least one recipe** (306 of 311 machines). This raised the question: Are BOMs and recipes redundant?

**Investigation showed they serve different purposes:**

| Aspect | BOM (Bill of Materials) | Recipe |
|--------|-------------------------|--------|
| **Purpose** | WHAT components needed | HOW to assemble them |
| **Contains** | Parts list, quantities, scrap rate | Process steps, time, energy, labor |
| **Variants** | One BOM per machine | Multiple recipes (detailed, simple, seed) |
| **Example** | `bom_ball_mill_v0.yaml`: 8 components | `recipe_ball_mill_v0.yaml`: 4-step process (9 hrs) |
| **Analogy** | Engineering BOM (eBOM) in CAD/PLM | Manufacturing BOM (mBOM) / routing in MES |

**Example: ball_mill_v0 has:**
- 1 BOM listing 8 components
- 3 recipes: detailed (4 steps, 9 hrs), simple (1 step, 3 hrs), seed variant

This is **intentional design**, not confusion. BOMs and recipes are complementary.

## Decision

### Keep Both BOMs and Recipes

**Rationale:**
1. **Separation of concerns**: WHAT (BOM) vs HOW (recipe)
2. **Supports variants**: Same BOM, different assembly approaches
3. **Real-world parallel**: Standard practice in manufacturing systems
4. **Already widespread**: 104 machine recipes created systematically

### Auto-Infer Recipe Inputs from BOM

Extend ADR-018's input inference hierarchy with a third fallback:

1. **First**: Use explicit recipe inputs (if present)
2. **Second**: Infer from process step inputs (ADR-018)
3. **NEW Third**: Infer from BOM if recipe has `target_item_id` (this ADR)

**Benefits:**
- Fixes 104 existing machine recipes without manual edits
- Maintains DRY principle (BOM is single source for component lists)
- Enables recipe variants without duplicating component lists
- Backward compatible (only affects currently-broken recipes)

### Validation Strategy

**1. BOM-Based Inference Allowed (INFO level)**
- If recipe has `target_item_id` with matching BOM: Allow inference, warn user
- Encourages eventual migration to explicit inputs

**2. Machine Completeness (WARNING level)**
- Every BOM should have at least one recipe
- Every machine recipe should have a BOM

**3. Consistency Checks (WARNING/INFO level)**
- When recipe has explicit inputs AND BOM exists: Check for mismatches
- Helps catch data entry errors

## Implementation

### Phase 1: Runtime BOM Inference

**File:** `src/simulation/engine.py`
**Function:** `run_recipe()` (lines 570-596)

**Added after step inference (line 568):**
```python
# ADR-019: Infer inputs from BOM if recipe has target_item_id
if not recipe_inputs:
    target_item_id = recipe_def.get("target_item_id")
    if target_item_id:
        bom = self.kb.get_bom(target_item_id)
        if bom:
            components = bom.get("components", [])
            if components:
                # Convert BOM components to recipe input format
                bom_inputs = []
                for comp in components:
                    item_id = comp.get("item_id")
                    qty = comp.get("qty", 1)
                    unit = comp.get("unit", "unit")  # Default to "unit"
                    if item_id:
                        bom_inputs.append({"item_id": item_id, "qty": qty, "unit": unit})

                if bom_inputs:
                    recipe_inputs = bom_inputs
                    print(f"⚠️  Recipe {recipe_id}: Inferred {len(bom_inputs)} inputs from BOM", file=sys.stderr)
```

### Phase 2: Output Inference

**File:** `src/simulation/engine.py`
**Function:** `run_recipe()` (lines 604-615)

**Added after step output inference (line 602):**
```python
# ADR-019: Infer outputs from target_item_id if not specified
if not recipe_outputs:
    target_item_id = recipe_def.get("target_item_id")
    if target_item_id:
        recipe_outputs = [{"item_id": target_item_id, "qty": 1, "unit": "unit"}]
        print(f"⚠️  Recipe {recipe_id}: Inferred output {target_item_id} (qty=1)", file=sys.stderr)
```

**Updated error messages (lines 622, 630):**
- "neither explicit, nor inferred from steps, nor from BOM"
- "neither explicit, nor inferred from steps, nor from target_item_id"

### Phase 3: Validation Updates

**File:** `src/kb_core/validators.py`
**Function:** `validate_recipe_inputs_outputs()` (lines 957-974)

**Added BOM check before raising error (line 957):**
```python
# ADR-019: Check if BOM exists for target_item_id (allows BOM-based inference)
if not has_step_inputs:
    target_item_id = recipe_dict.get("target_item_id")
    if target_item_id:
        bom = kb.get_bom(target_item_id)
        if bom and bom.get("components"):
            has_step_inputs = True  # Resolvable via BOM at runtime
            issues.append(ValidationIssue(
                level=ValidationLevel.INFO,
                category="recipe",
                rule="recipe_inputs_inferred_from_bom",
                message=f"Recipe inputs will be inferred from BOM for '{target_item_id}' at runtime",
                fix_hint="Consider adding explicit inputs: [...] to recipe for clarity and performance"
            ))
```

**Updated error fix hint (line 985):**
- "Add inputs: [...] to recipe, ensure referenced processes have inputs, or verify BOM exists for target_item_id"

### Phase 4: Machine Completeness Validation

**File:** `src/kb_core/validators.py`
**Function:** `validate_machine_completeness()` (lines 1149-1199)

**New validation function:**
- Checks every BOM has at least one recipe (WARNING if missing)
- Checks every machine recipe (`recipe_machine_*`) has a BOM (WARNING if missing)

### Phase 5: BOM/Recipe Consistency Checks

**File:** `src/kb_core/validators.py`
**Function:** `validate_bom_recipe_consistency()` (lines 1202-1287)

**New validation function:**
- When recipe has explicit inputs AND BOM exists: Compare them
- **WARNING**: Items in BOM but missing from recipe inputs
- **INFO**: Items in recipe but not in BOM (consumables, energy)
- **INFO**: Quantity mismatches between BOM and recipe

**Use cases:**
- Catches data entry errors
- Identifies recipes that need updating when BOM changes
- Documents intentional deviations (scrap allowances, consumables)

## Test Results

### Functional Test: recipe_machine_labor_bot_general_v0

**Before:**
```bash
$ python -m src.cli sim run-recipe --recipe recipe_machine_labor_bot_general_v0
✗ Failed to run recipe: Recipe has no inputs
```

**After:**
```bash
$ python -m src.cli sim run-recipe --recipe recipe_machine_labor_bot_general_v0
⚠️  Recipe recipe_machine_labor_bot_general_v0: Inferred 30 inputs from BOM for labor_bot_general_v0
⚠️  Recipe recipe_machine_labor_bot_general_v0: Inferred output labor_bot_general_v0 (qty=1)
✓ Started recipe 'recipe_machine_labor_bot_general_v0' (quantity: 1)
```

### Validation Test

**Validation output:**
```
INFO: recipe_machine_labor_bot_general_v0
  Recipe inputs will be inferred from BOM for 'labor_bot_general_v0' at runtime
  Fix hint: Consider adding explicit inputs to recipe for clarity
```

**Success!** 104 machine recipes now validate as INFO instead of ERROR.

## Migration Path

### Short Term (Current)
- BOM-based inference works automatically
- INFO-level warnings guide users to best practices
- No breaking changes

### Medium Term (Optional)
- Gradually add explicit inputs to high-priority recipes
- Use consistency validation to find mismatches
- Document which recipes intentionally deviate from BOM

### Long Term (Possible Future)
- **Option A**: Keep both (current approach)
  - BOMs remain authoritative for engineering
  - Recipes describe manufacturing processes

- **Option B**: Deprecate BOMs in favor of recipes
  - Migrate all BOM data into recipe inputs
  - Lose separation of concerns, increase duplication
  - **Not currently recommended** but documented for consideration

## Consequences

### Positive
✅ Fixes GitHub Issue #3 (recipes without explicit inputs)
✅ Enables 104 machine recipes to run successfully
✅ Maintains DRY principle (BOM as single source of truth)
✅ Supports multiple assembly variants (detailed vs simple)
✅ Backward compatible (only fixes broken recipes)
✅ Clear validation messages guide users
✅ Consistency checks catch data errors

### Negative
⚠️ Two sources of truth (BOM and recipe inputs) can diverge
⚠️ Small performance cost (BOM lookup per recipe execution)
⚠️ More complex architecture than single-source approach

### Mitigations
- Consistency validation catches divergence
- BOM lookup is O(1) cached dict access (minimal cost)
- INFO-level warnings encourage migration to explicit inputs
- Clear documentation of BOM vs recipe roles

## Related Issues

- **GitHub Issue #3**: "BUG: Recipes without explicit inputs fail to run" - RESOLVED
- **Feedback Doc**: `design/simulation_feedback/build_complete_robot_feedback_2026_01_01.md`

## Validation Rules Added

| Rule | Level | Trigger | Message |
|------|-------|---------|---------|
| `recipe_inputs_inferred_from_bom` | INFO | Recipe has target_item_id with BOM, no explicit inputs | "Recipe inputs will be inferred from BOM at runtime" |
| `machine_missing_recipe` | WARNING | BOM exists but no recipe | "Machine has BOM but no recipe" |
| `machine_recipe_missing_bom` | WARNING | Machine recipe exists but no BOM | "Machine recipe targets X but no BOM exists" |
| `bom_recipe_input_mismatch` | WARNING | Recipe inputs missing items from BOM | "Recipe inputs missing N items from BOM" |
| `recipe_has_extra_inputs` | INFO | Recipe has inputs not in BOM | "Recipe has N inputs not in BOM (consumables?)" |
| `bom_recipe_quantity_mismatch` | INFO | Same item, different quantities | "Quantity mismatch: BOM=X, Recipe=Y" |

## Summary

This ADR establishes BOMs and recipes as **complementary, not redundant**:
- **BOMs** define WHAT components are needed (engineering truth)
- **Recipes** describe HOW to assemble them (manufacturing process)

Auto-inference from BOMs fixes 104 machine recipes while maintaining clean architecture and supporting future flexibility. Validation ensures consistency and guides users toward best practices.

**Status:** Fully implemented and tested. GitHub Issue #3 resolved.

**Update 2026-01-25:** When BOM-based inference is used for `unit_kind: discrete`
items, do not rely on fractional `unit` counts to balance mass. Keep discrete
counts integral and balance remaining mass with bulk inputs and explicit scrap,
or adjust item `mass` to align with BOM sums.
