# Fix Intelligence: recipe_vacuum_tube_subassembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_vacuum_tube_subassembly_v0.yaml`
- **Target item:** `vacuum_tube_subassembly`
  - File: `kb/items/vacuum_tube_subassembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_vacuum_tube_subassembly_v0_target_v0` → vacuum_tube_subassembly (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tube_subassembly_assembly_v0') requires input 'vacuum_tube_triode_v0' which is not available

**Location:** Step 0
**Process:** `tube_subassembly_assembly_v0`
  - File: `kb/processes/tube_subassembly_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: tube_subassembly_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_vacuum_tube_subassembly_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
