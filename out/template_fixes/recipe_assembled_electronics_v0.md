# Fix Intelligence: recipe_assembled_electronics_v0

## Files

- **Recipe:** `kb/recipes/recipe_assembled_electronics_v0.yaml`
- **Target item:** `assembled_electronics`
  - File: `kb/items/assembled_electronics.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electronics_assembly_v0') requires input 'pcb_populated' which is not available

**Location:** Step 0
**Process:** `electronics_assembly_v0`
  - File: `kb/processes/electronics_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronics_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_assembled_electronics_v0.yaml`
- **BOM available:** No
