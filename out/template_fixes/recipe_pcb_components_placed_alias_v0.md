# Fix Intelligence: recipe_pcb_components_placed_alias_v0

## Files

- **Recipe:** `kb/recipes/recipe_pcb_components_placed_alias_v0.yaml`
- **Target item:** `pcb_components_placed`
  - File: `kb/items/pcb_components_placed.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_pcb_components_placed_v0` → pcb_components_placed_v0 (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'component_placement_process_v0') requires input 'pcb_paste_applied' which is not available

**Location:** Step 0
**Process:** `component_placement_process_v0`
  - File: `kb/processes/component_placement_process_v0.yaml`

**Current step:**
```yaml
- process_id: component_placement_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_pcb_components_placed_alias_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
