# Fix Intelligence: recipe_hot_wire_cutting_wire_v0

## Files

- **Recipe:** `kb/recipes/recipe_hot_wire_cutting_wire_v0.yaml`
- **Target item:** `hot_wire_cutting_wire`
  - File: `kb/items/hot_wire_cutting_wire.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'wire_drawing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `wire_drawing_basic_v0`
  - File: `kb/processes/wire_drawing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wire_drawing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'metal_cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `metal_cutting_basic_v0`
  - File: `kb/processes/metal_cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `metal_wire_feed` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_hot_wire_cutting_wire_v0.yaml`
- **BOM available:** No
