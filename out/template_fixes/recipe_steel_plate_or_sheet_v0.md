# Fix Intelligence: recipe_steel_plate_or_sheet_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_plate_or_sheet_v0.yaml`
- **Target item:** `steel_plate_or_sheet`
  - File: `kb/items/steel_plate_or_sheet.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'heating_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `heating_basic_v0`
  - File: `kb/processes/heating_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: heating_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'rolling_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `rolling_basic_v0`
  - File: `kb/processes/rolling_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: rolling_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_steel_plate_or_sheet_v0.yaml`
- **BOM available:** No
