# Fix Intelligence: recipe_parabolic_mirror_dish_v0

## Files

- **Recipe:** `kb/recipes/recipe_parabolic_mirror_dish_v0.yaml`
- **Target item:** `parabolic_mirror_dish_v0`
  - File: `kb/items/parabolic_mirror_dish_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_metal_cutting_v0') requires input 'sheet_metal_or_structural_steel' which is not available

**Location:** Step 0
**Process:** `sheet_metal_cutting_v0`
  - File: `kb/processes/sheet_metal_cutting_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_cutting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'sheet_metal_bending_and_forming_v0') requires input 'metal_sheet' which is not available

**Location:** Step 1
**Process:** `sheet_metal_bending_and_forming_v0`
  - File: `kb/processes/sheet_metal_bending_and_forming_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_bending_and_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'finishing_deburring_v0') requires input 'machined_part_raw' which is not available

**Location:** Step 2
**Process:** `finishing_deburring_v0`
  - File: `kb/processes/finishing_deburring_v0.yaml`

**Current step:**
```yaml
- process_id: finishing_deburring_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_parabolic_mirror_dish_v0.yaml`
- **BOM available:** No
