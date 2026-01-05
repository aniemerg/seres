# Fix Intelligence: recipe_electronic_assembly_v1

## Files

- **Recipe:** `kb/recipes/recipe_electronic_assembly_v1.yaml`
- **Target item:** `electronic_assembly`
  - File: `kb/items/electronic_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_electronic_assembly_v0` → electronic_assembly (1 steps)
- `recipe_electronic_assembly_v2` → electronic_assembly (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electronic_assembly_v0') requires input 'pcb_populated' which is not available

**Location:** Step 0
**Process:** `electronic_assembly_v0`
  - File: `kb/processes/electronic_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronic_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_electronic_assembly_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
