# Fix Intelligence: recipe_robot_tool_quick_change_v0

## Files

- **Recipe:** `kb/recipes/recipe_robot_tool_quick_change_v0.yaml`
- **Target item:** `robot_tool_quick_change_v0`
  - File: `kb/items/robot_tool_quick_change_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'robot_quick_change_fabrication_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 0
**Process:** `robot_quick_change_fabrication_v0`
  - File: `kb/processes/robot_quick_change_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: robot_quick_change_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_robot_tool_quick_change_v0.yaml`
- **BOM available:** No
