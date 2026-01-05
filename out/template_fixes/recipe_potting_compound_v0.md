# Fix Intelligence: recipe_potting_compound_v0

## Files

- **Recipe:** `kb/recipes/recipe_potting_compound_v0.yaml`
- **Target item:** `potting_compound`
  - File: `kb/items/potting_compound.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'potting_compound_synthesis_v0') requires input 'epoxy_resin_base' which is not available

**Location:** Step 0
**Process:** `potting_compound_synthesis_v0`
  - File: `kb/processes/potting_compound_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: potting_compound_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_potting_compound_v0.yaml`
- **BOM available:** No
