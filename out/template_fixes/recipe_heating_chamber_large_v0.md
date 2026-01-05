# Fix Intelligence: recipe_heating_chamber_large_v0

## Files

- **Recipe:** `kb/recipes/recipe_heating_chamber_large_v0.yaml`
- **Target item:** `heating_chamber_large`
  - File: `kb/items/heating_chamber_large.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'welding_and_fabrication_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `welding_and_fabrication_v0`
  - File: `kb/processes/welding_and_fabrication_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_and_fabrication_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- Step 0 produces: `welded_fabrications` (9.5 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `welded_fabrications` (9.5 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_heating_chamber_large_v0.yaml`
- **BOM available:** No
