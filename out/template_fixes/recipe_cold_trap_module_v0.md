# Fix Intelligence: recipe_cold_trap_module_v0

## Files

- **Recipe:** `kb/recipes/recipe_cold_trap_module_v0.yaml`
- **Target item:** `cold_trap_module_v0`
  - File: `kb/items/cold_trap_module_v0.yaml`
- **BOM:** `kb/boms/bom_cold_trap_module_v0.yaml` ✓
  - Components: 7
- **Steps:** 1 total

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

BOM has 7 components:

- `chamber_shell_sealed` (qty: 1 None)
- `cooling_water_jacket` (qty: 1 None)
- `circulation_pump_coolant` (qty: 1 None)
- `heat_rejection_radiator` (qty: 1 None)
- `vacuum_seal_assembly` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `support_frame_small` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: chamber_shell_sealed
    qty: 1
    unit: None
  - item_id: cooling_water_jacket
    qty: 1
    unit: None
  - item_id: circulation_pump_coolant
    qty: 1
    unit: None
  - item_id: heat_rejection_radiator
    qty: 1
    unit: None
  - item_id: vacuum_seal_assembly
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: support_frame_small
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_cold_trap_module_v0.yaml`
- **BOM available:** Yes (7 components)
