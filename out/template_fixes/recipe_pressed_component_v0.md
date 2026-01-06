# Fix Intelligence: recipe_pressed_component_v0

## Files

- **Recipe:** `kb/recipes/recipe_pressed_component_v0.yaml`
- **Target item:** `pressed_component`
  - File: `kb/items/pressed_component.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'batching_and_mixing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `batching_and_mixing_basic_v0`
  - File: `kb/processes/batching_and_mixing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: batching_and_mixing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

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

- Step 0 produces: `powder_mixture` (1.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'molding_press_operation_v0') requires input 'powder_feedstock' which is not available

**Location:** Step 2
**Process:** `molding_press_operation_v0`
  - File: `kb/processes/molding_press_operation_v0.yaml`

**Current step:**
```yaml
- process_id: molding_press_operation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_pressed_component_v0.yaml`
- **BOM available:** No
