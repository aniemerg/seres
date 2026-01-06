# Fix Intelligence: recipe_steel_plate_raw_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_plate_raw_v0.yaml`
- **Target item:** `steel_plate_raw`
  - File: `kb/items/steel_plate_raw.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

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

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'plate_to_steel_plate_raw_v0') requires input 'steel_plate_or_sheet' which is not available

**Location:** Step 2
**Process:** `plate_to_steel_plate_raw_v0`
  - File: `kb/processes/plate_to_steel_plate_raw_v0.yaml`

**Current step:**
```yaml
- process_id: plate_to_steel_plate_raw_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_steel_plate_raw_v0.yaml`
- **BOM available:** No
