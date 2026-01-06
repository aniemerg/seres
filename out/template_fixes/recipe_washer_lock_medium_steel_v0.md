# Fix Intelligence: recipe_washer_lock_medium_steel_v0

## Files

- **Recipe:** `kb/recipes/recipe_washer_lock_medium_steel_v0.yaml`
- **Target item:** `washer_lock_medium_steel`
  - File: `kb/items/washer_lock_medium_steel.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_stamping_process_v0') requires input 'steel_sheet_1mm' which is not available

**Location:** Step 0
**Process:** `metal_stamping_process_v0`
  - File: `kb/processes/metal_stamping_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_stamping_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'heat_treatment_hardening_v0') requires input 'bearing_rings_machined' which is not available

**Location:** Step 1
**Process:** `heat_treatment_hardening_v0`
  - File: `kb/processes/heat_treatment_hardening_v0.yaml`

**Current step:**
```yaml
- process_id: heat_treatment_hardening_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_washer_lock_medium_steel_v0.yaml`
- **BOM available:** No
