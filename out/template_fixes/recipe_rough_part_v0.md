# Fix Intelligence: recipe_rough_part_v0

## Files

- **Recipe:** `kb/recipes/recipe_rough_part_v0.yaml`
- **Target item:** `rough_part`
  - File: `kb/items/rough_part.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `casting_basic_v0`
  - File: `kb/processes/casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

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

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_rough_part_v0.yaml`
- **BOM available:** No
