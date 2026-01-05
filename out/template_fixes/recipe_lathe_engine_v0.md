# Fix Intelligence: recipe_lathe_engine_v0

## Files

- **Recipe:** `kb/recipes/recipe_lathe_engine_v0.yaml`
- **Target item:** `lathe_engine_v0`
  - File: `kb/items/lathe_engine_v0.yaml`
- **BOM:** `kb/boms/bom_lathe_engine_v0.yaml` ✓
  - Components: 14
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'lathe_engine_assembly_v0') requires input 'lathe_bed_and_headstock' which is not available

**Location:** Step 0
**Process:** `lathe_engine_assembly_v0`
  - File: `kb/processes/lathe_engine_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: lathe_engine_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_lathe_engine_v0.yaml`
- **BOM available:** Yes (14 components)
