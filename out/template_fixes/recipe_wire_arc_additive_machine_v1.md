# Fix Intelligence: recipe_wire_arc_additive_machine_v1

## Files

- **Recipe:** `kb/recipes/recipe_wire_arc_additive_machine_v1.yaml`
- **Target item:** `wire_arc_additive_machine`
  - File: `kb/items/wire_arc_additive_machine.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_wire_arc_additive_machine_v2` → wire_arc_additive_machine (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'import_receiving_basic_v0') requires input 'bulk_material_or_parts' which is not available

**Location:** Step 0
**Process:** `import_receiving_basic_v0`
  - File: `kb/processes/import_receiving_basic_v0.yaml`

**Current step:**
```yaml
- process_id: import_receiving_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_wire_arc_additive_machine_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
