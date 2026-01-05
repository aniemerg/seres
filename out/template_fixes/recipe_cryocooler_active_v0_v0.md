# Fix Intelligence: recipe_cryocooler_active_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_cryocooler_active_v0_v0.yaml`
- **Target item:** `cryocooler_active_v0`
  - File: `kb/items/cryocooler_active_v0.yaml`
- **BOM:** `kb/boms/bom_cryocooler_active_v0.yaml` ✓
  - Components: 1
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cryocooler_core_unit_assembly_v0') requires input 'machined_metal_block_v0' which is not available

**Location:** Step 0
**Process:** `cryocooler_core_unit_assembly_v0`
  - File: `kb/processes/cryocooler_core_unit_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: cryocooler_core_unit_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'cryocooler_active_assembly_v0') requires input 'electronic_components_set' which is not available

**Location:** Step 1
**Process:** `cryocooler_active_assembly_v0`
  - File: `kb/processes/cryocooler_active_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: cryocooler_active_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_cryocooler_active_v0_v0.yaml`
- **BOM available:** Yes (1 components)
