# Fix Intelligence: recipe_bolt_hex_medium_steel_v0

## Files

- **Recipe:** `kb/recipes/recipe_bolt_hex_medium_steel_v0.yaml`
- **Target item:** `bolt_hex_medium_steel`
  - File: `kb/items/bolt_hex_medium_steel.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_forging_process_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `metal_forging_process_v0`
  - File: `kb/processes/metal_forging_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_forging_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `bearing_ring_blanks` (1.3 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_bolt_hex_medium_steel_v0.yaml`
- **BOM available:** No
