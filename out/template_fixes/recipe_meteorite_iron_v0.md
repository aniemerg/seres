# Fix Intelligence: recipe_meteorite_iron_v0

## Files

- **Recipe:** `kb/recipes/recipe_meteorite_iron_v0.yaml`
- **Target item:** `meteorite_iron`
  - File: `kb/items/meteorite_iron.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'environment_source_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `environment_source_v0`
  - File: `kb/processes/environment_source_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: environment_source_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'beneficiate_regolith_magnetic_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 1
**Process:** `beneficiate_regolith_magnetic_v0`
  - File: `kb/processes/beneficiate_regolith_magnetic_v0.yaml`

**Current step:**
```yaml
- process_id: beneficiate_regolith_magnetic_v0
  inputs:
  - item_id: regolith_lunar_mare
    qty: 100.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `regolith_lunar_mare` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_meteorite_iron_v0.yaml`
- **BOM available:** No
