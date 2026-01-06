# Fix Intelligence: recipe_deposited_metal_structure_v0

## Files

- **Recipe:** `kb/recipes/recipe_deposited_metal_structure_v0.yaml`
- **Target item:** `deposited_metal_structure`
  - File: `kb/items/deposited_metal_structure.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'wire_arc_additive_process_v0') requires input 'metal_wire_feed' which is not available

**Location:** Step 0
**Process:** `wire_arc_additive_process_v0`
  - File: `kb/processes/wire_arc_additive_process_v0.yaml`

**Current step:**
```yaml
- process_id: wire_arc_additive_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_deposited_metal_structure_v0.yaml`
- **BOM available:** No
