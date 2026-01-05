# Fix Intelligence: recipe_lab_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_lab_v0_v0.yaml`
- **Target item:** `lab_v0_v0`
  - File: `kb/items/lab_v0_v0.yaml`
- **BOM:** `kb/boms/bom_lab_v0_v0.yaml` ✓
  - Components: 1
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

BOM has 1 components:

- `lab_console_unit_v0` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: lab_console_unit_v0
    qty: 1.0
    unit: unit
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_lab_v0_v0.yaml`
- **BOM available:** Yes (1 components)
