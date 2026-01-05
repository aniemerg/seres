# Fix Intelligence: recipe_jacket_shell_welded_v0

## Files

- **Recipe:** `kb/recipes/recipe_jacket_shell_welded_v0.yaml`
- **Target item:** `jacket_shell_welded`
  - File: `kb/items/jacket_shell_welded.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'welding_process_tig_v0') requires input 'jacket_panels_formed' which is not available

**Location:** Step 0
**Process:** `welding_process_tig_v0`
  - File: `kb/processes/welding_process_tig_v0.yaml`

**Current step:**
```yaml
- process_id: welding_process_tig_v0
  inputs:
  - item_id: jacket_panels_formed
    qty: 2.8
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `jacket_panels_formed` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_jacket_shell_welded_v0.yaml`
- **BOM available:** No
