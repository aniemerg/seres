# Fix Intelligence: recipe_electrical_feedthrough_vacuum_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrical_feedthrough_vacuum_v0.yaml`
- **Target item:** `electrical_feedthrough_vacuum`
  - File: `kb/items/electrical_feedthrough_vacuum.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electrical_feedthrough_vacuum_fabrication_v0') requires input 'magnet_wire_copper' which is not available

**Location:** Step 0
**Process:** `electrical_feedthrough_vacuum_fabrication_v0`
  - File: `kb/processes/electrical_feedthrough_vacuum_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_feedthrough_vacuum_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_electrical_feedthrough_vacuum_v0.yaml`
- **BOM available:** No
