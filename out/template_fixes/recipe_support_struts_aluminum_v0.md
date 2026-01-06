# Fix Intelligence: recipe_support_struts_aluminum_v0

## Files

- **Recipe:** `kb/recipes/recipe_support_struts_aluminum_v0.yaml`
- **Target item:** `support_struts_aluminum`
  - File: `kb/items/support_struts_aluminum.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'aluminum_support_struts_basic_v0') requires input 'aluminum_tube_stock' which is not available

**Location:** Step 0
**Process:** `aluminum_support_struts_basic_v0`
  - File: `kb/processes/aluminum_support_struts_basic_v0.yaml`

**Current step:**
```yaml
- process_id: aluminum_support_struts_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_support_struts_aluminum_v0.yaml`
- **BOM available:** No
