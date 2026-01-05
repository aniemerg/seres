# Fix Intelligence: recipe_turning_tools_general_v0

## Files

- **Recipe:** `kb/recipes/recipe_turning_tools_general_v0.yaml`
- **Target item:** `turning_tools_general`
  - File: `kb/items/turning_tools_general.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tool_steel_high_carbon_cast_v0') requires input 'steel_billet_or_slab' which is not available

**Location:** Step 0
**Process:** `tool_steel_high_carbon_cast_v0`
  - File: `kb/processes/tool_steel_high_carbon_cast_v0.yaml`

**Current step:**
```yaml
- process_id: tool_steel_high_carbon_cast_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_turning_tools_general_v0.yaml`
- **BOM available:** No
