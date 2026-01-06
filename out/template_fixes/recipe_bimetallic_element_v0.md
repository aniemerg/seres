# Fix Intelligence: recipe_bimetallic_element_v0

## Files

- **Recipe:** `kb/recipes/recipe_bimetallic_element_v0.yaml`
- **Target item:** `bimetallic_element`
  - File: `kb/items/bimetallic_element.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'bimetallic_strip_forming_v0') requires input 'steel_strip_thin' which is not available

**Location:** Step 0
**Process:** `bimetallic_strip_forming_v0`
  - File: `kb/processes/bimetallic_strip_forming_v0.yaml`

**Current step:**
```yaml
- process_id: bimetallic_strip_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_bimetallic_element_v0.yaml`
- **BOM available:** No
