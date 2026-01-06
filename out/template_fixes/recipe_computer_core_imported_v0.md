# Fix Intelligence: recipe_computer_core_imported_v0

## Files

- **Recipe:** `kb/recipes/recipe_computer_core_imported_v0.yaml`
- **Target item:** `computer_core_imported`
  - File: `kb/items/computer_core_imported.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

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

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'power_supply_small_inhouse_v0') requires input 'power_supply_components_basic' which is not available

**Location:** Step 1
**Process:** `power_supply_small_inhouse_v0`
  - File: `kb/processes/power_supply_small_inhouse_v0.yaml`

**Current step:**
```yaml
- process_id: power_supply_small_inhouse_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'computer_core_assembly_v0') requires input 'enclosure_small' which is not available

**Location:** Step 2
**Process:** `computer_core_assembly_v0`
  - File: `kb/processes/computer_core_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: computer_core_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_computer_core_imported_v0.yaml`
- **BOM available:** No
