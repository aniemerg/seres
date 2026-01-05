# Fix Intelligence: recipe_carbon_reductant_v0

## Files

- **Recipe:** `kb/recipes/recipe_carbon_reductant_v0.yaml`
- **Target item:** `carbon_reductant`
  - File: `kb/items/carbon_reductant.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'carbon_extraction_from_carbonaceous_v0') requires input 'regolith_carbonaceous' which is not available

**Location:** Step 0
**Process:** `carbon_extraction_from_carbonaceous_v0`
  - File: `kb/processes/carbon_extraction_from_carbonaceous_v0.yaml`

**Current step:**
```yaml
- process_id: carbon_extraction_from_carbonaceous_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'drying_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `drying_basic_v0`
  - File: `kb/processes/drying_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: drying_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `carbon_reductant` (0.3 kg)
- Step 0 produces: `tailings` (9.7 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'sizing_grinding_basic_v0') requires input 'coarse_powder' which is not available

**Location:** Step 2
**Process:** `sizing_grinding_basic_v0`
  - File: `kb/processes/sizing_grinding_basic_v0.yaml`

**Current step:**
```yaml
- process_id: sizing_grinding_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_carbon_reductant_v0.yaml`
- **BOM available:** No
