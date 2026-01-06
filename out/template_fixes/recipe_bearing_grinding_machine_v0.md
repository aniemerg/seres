# Fix Intelligence: recipe_bearing_grinding_machine_v0

## Files

- **Recipe:** `kb/recipes/recipe_bearing_grinding_machine_v0.yaml`
- **Target item:** `bearing_grinding_machine_v0`
  - File: `kb/items/bearing_grinding_machine_v0.yaml`
- **BOM:** `kb/boms/bom_bearing_grinding_machine_v0.yaml` ✓
  - Components: 9
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'bearing_machine_assembly_v0') requires input 'import_misc_components_set' which is not available

**Location:** Step 0
**Process:** `bearing_machine_assembly_v0`
  - File: `kb/processes/bearing_machine_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: bearing_machine_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_bearing_grinding_machine_v0.yaml`
- **BOM available:** Yes (9 components)
