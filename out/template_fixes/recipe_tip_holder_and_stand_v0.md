# Fix Intelligence: recipe_tip_holder_and_stand_v0

## Files

- **Recipe:** `kb/recipes/recipe_tip_holder_and_stand_v0.yaml`
- **Target item:** `tip_holder_and_stand`
  - File: `kb/items/tip_holder_and_stand.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_and_fabrication_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_and_fabrication_v0`
  - File: `kb/processes/welding_and_fabrication_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_and_fabrication_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `tip_holder_and_stand` (1.0 unit)

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

- Step 0 produces: `tip_holder_and_stand` (1.0 unit)
- Step 1 produces: `welded_fabrications` (9.5 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_tip_holder_and_stand_v0.yaml`
- **BOM available:** No
