# Fix Intelligence: recipe_coating_station_v1

## Files

- **Recipe:** `kb/recipes/recipe_coating_station_v1.yaml`
- **Target item:** `coating_station`
  - File: `kb/items/coating_station.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_coating_station_v0` → coating_station_v0 (5 steps)

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'welded_fabrication_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `welded_fabrication_basic_v0`
  - File: `kb/processes/welded_fabrication_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welded_fabrication_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `integration_test_basic_v0`
  - File: `kb/processes/integration_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: integration_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_coating_station_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
