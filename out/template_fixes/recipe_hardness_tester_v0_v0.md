# Fix Intelligence: recipe_hardness_tester_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_hardness_tester_v0_v0.yaml`
- **Target item:** `hardness_tester_v0`
  - File: `kb/items/hardness_tester_v0.yaml`
- **BOM:** `kb/boms/bom_hardness_tester_v0.yaml` ✓
  - Components: 6
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_hardness_tester_v0` → hardness_tester_v0 (1 steps)

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 6 components:

- `machine_frame_small` (qty: 1 None)
- `motor_electric_small` (qty: 1 None)
- `load_cell_strain_gauge_v0` (qty: 1 None)
- `control_circuit_board_basic` (qty: 1 None)
- `enclosure_small` (qty: 1 None)
- `fastener_kit_small` (qty: 0.5 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: machine_frame_small
    qty: 1
    unit: None
  - item_id: motor_electric_small
    qty: 1
    unit: None
  - item_id: load_cell_strain_gauge_v0
    qty: 1
    unit: None
  - item_id: control_circuit_board_basic
    qty: 1
    unit: None
  - item_id: enclosure_small
    qty: 1
    unit: None
  - item_id: fastener_kit_small
    qty: 0.5
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_hardness_tester_v0_v0.yaml`
- **BOM available:** Yes (6 components)
- **Similar recipes:** 1 found
