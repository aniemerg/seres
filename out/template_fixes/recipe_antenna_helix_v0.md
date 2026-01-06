# Fix Intelligence: recipe_antenna_helix_v0

## Files

- **Recipe:** `kb/recipes/recipe_antenna_helix_v0.yaml`
- **Target item:** `antenna_helix_v0`
  - File: `kb/items/antenna_helix_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'wire_cutting_and_stripping_v0') requires input 'magnet_wire_copper' which is not available

**Location:** Step 0
**Process:** `wire_cutting_and_stripping_v0`
  - File: `kb/processes/wire_cutting_and_stripping_v0.yaml`

**Current step:**
```yaml
- process_id: wire_cutting_and_stripping_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'coil_winding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `coil_winding_basic_v0`
  - File: `kb/processes/coil_winding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: coil_winding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_wire_lengths` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_antenna_helix_v0.yaml`
- **BOM available:** No
