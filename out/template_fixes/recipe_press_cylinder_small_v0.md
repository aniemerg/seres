# Fix Intelligence: recipe_press_cylinder_small_v0

## Files

- **Recipe:** `kb/recipes/recipe_press_cylinder_small_v0.yaml`
- **Target item:** `press_cylinder_small`
  - File: `kb/items/press_cylinder_small.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'sealing_and_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_press_cylinder_small_v0.yaml`
- **BOM available:** No
