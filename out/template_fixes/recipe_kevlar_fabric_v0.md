# Fix Intelligence: recipe_kevlar_fabric_v0

## Files

- **Recipe:** `kb/recipes/recipe_kevlar_fabric_v0.yaml`
- **Target item:** `kevlar_fabric_import_v0`
  - File: `kb/items/kevlar_fabric_import_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'kevlar_fabric_synthesis_v0') requires input 'aramid_precursor_v0' which is not available

**Location:** Step 0
**Process:** `kevlar_fabric_synthesis_v0`
  - File: `kb/processes/kevlar_fabric_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: kevlar_fabric_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_kevlar_fabric_v0.yaml`
- **BOM available:** No
