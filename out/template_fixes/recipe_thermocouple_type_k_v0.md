# Fix Intelligence: recipe_thermocouple_type_k_v0

## Files

- **Recipe:** `kb/recipes/recipe_thermocouple_type_k_v0.yaml`
- **Target item:** `thermocouple_type_k_v0`
  - File: `kb/items/thermocouple_type_k_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'alloy_mixing_v0') requires input 'nickel_chromium_alloy' which is not available

**Location:** Step 0
**Process:** `alloy_mixing_v0`
  - File: `kb/processes/alloy_mixing_v0.yaml`

**Current step:**
```yaml
- process_id: alloy_mixing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'metal_wire_drawing_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 1
**Process:** `metal_wire_drawing_v0`
  - File: `kb/processes/metal_wire_drawing_v0.yaml`

**Current step:**
```yaml
- process_id: metal_wire_drawing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

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

- Step 0 produces: `nickel_chromium_nickel_aluminum_alloy_stock` (1.0 kg)
- Step 1 produces: `metal_wire_feed` (2.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_thermocouple_type_k_v0.yaml`
- **BOM available:** No
