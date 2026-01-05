# Fix Intelligence: recipe_test_equipment_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_test_equipment_basic_v0.yaml`
- **Target item:** `test_equipment_basic`
  - File: `kb/items/test_equipment_basic.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'test_equipment_basic_assembly_v0') requires input 'assembled_electronics' which is not available

**Location:** Step 0
**Process:** `test_equipment_basic_assembly_v0`
  - File: `kb/processes/test_equipment_basic_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: test_equipment_basic_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_test_equipment_basic_v0.yaml`
- **BOM available:** No
