# Fix Intelligence: recipe_analog_test_bench_neural_circuits_v0

## Files

- **Recipe:** `kb/recipes/recipe_analog_test_bench_neural_circuits_v0.yaml`
- **Target item:** `analog_test_bench_neural_circuits_v0`
  - File: `kb/items/analog_test_bench_neural_circuits_v0.yaml`
- **BOM:** `kb/boms/bom_analog_test_bench_neural_circuits_v0.yaml` ✓
  - Components: 2
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machine_assembly_basic_v0`
  - File: `kb/processes/machine_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machine_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 2 components:

- `machine_frame_small` (qty: 1.0 unit)
- `power_electronics_module` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: machine_frame_small
    qty: 1.0
    unit: unit
  - item_id: power_electronics_module
    qty: 1.0
    unit: unit
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_analog_test_bench_neural_circuits_v0.yaml`
- **BOM available:** Yes (2 components)
