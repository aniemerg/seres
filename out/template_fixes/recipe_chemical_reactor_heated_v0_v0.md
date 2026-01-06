# Fix Intelligence: recipe_chemical_reactor_heated_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_chemical_reactor_heated_v0_v0.yaml`
- **Target item:** `chemical_reactor_heated_v0_v0`
  - File: `kb/items/chemical_reactor_heated_v0_v0.yaml`
- **BOM:** `kb/boms/bom_chemical_reactor_heated_v0_v0.yaml` ✓
  - Components: 5
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mock_assembly_v0') requires input 'atomization_unit_v0' which is not available

**Location:** Step 0
**Process:** `mock_assembly_v0`
  - File: `kb/processes/mock_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: mock_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_chemical_reactor_heated_v0_v0.yaml`
- **BOM available:** Yes (5 components)
