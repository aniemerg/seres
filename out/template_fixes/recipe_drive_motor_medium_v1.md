# Fix Intelligence: recipe_drive_motor_medium_v1

## Files

- **Recipe:** `kb/recipes/recipe_drive_motor_medium_v1.yaml`
- **Target item:** `drive_motor_medium`
  - File: `kb/items/drive_motor_medium.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_drive_motor_medium_v0` → drive_motor_medium (4 steps)

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'lamination_stamping_v0') requires input 'electrical_steel_sheet' which is not available

**Location:** Step 0
**Process:** `lamination_stamping_v0`
  - File: `kb/processes/lamination_stamping_v0.yaml`

**Current step:**
```yaml
- process_id: lamination_stamping_v0
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

- Step 0 produces: `stator_rotor_lamination_set` (0.95 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_drive_motor_medium_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
