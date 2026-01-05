# Fix Intelligence: recipe_centrifugal_bowl_steel_v0

## Files

- **Recipe:** `kb/recipes/recipe_centrifugal_bowl_steel_v0.yaml`
- **Target item:** `centrifugal_bowl_steel`
  - File: `kb/items/centrifugal_bowl_steel.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_fabrication_welding_v0') requires input 'sheet_metal_or_structural_steel' which is not available

**Location:** Step 0
**Process:** `metal_fabrication_welding_v0`
  - File: `kb/processes/metal_fabrication_welding_v0.yaml`

**Current step:**
```yaml
- process_id: metal_fabrication_welding_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'machining_rough_v0') requires input 'cut_parts' which is not available

**Location:** Step 1
**Process:** `machining_rough_v0`
  - File: `kb/processes/machining_rough_v0.yaml`

**Current step:**
```yaml
- process_id: machining_rough_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'balancing_dynamic_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `balancing_dynamic_basic_v0`
  - File: `kb/processes/balancing_dynamic_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: balancing_dynamic_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (9.5 kg)
- Step 1 produces: `rough_part` (0.95 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_centrifugal_bowl_steel_v0.yaml`
- **BOM available:** No
