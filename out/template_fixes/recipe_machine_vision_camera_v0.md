# Fix Intelligence: recipe_machine_vision_camera_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_vision_camera_v0.yaml`
- **Target item:** `machine_vision_camera_v0`
  - File: `kb/items/machine_vision_camera_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machine_vision_camera_assembly_v0') requires input 'electronic_components_set' which is not available

**Location:** Step 0
**Process:** `machine_vision_camera_assembly_v0`
  - File: `kb/processes/machine_vision_camera_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: machine_vision_camera_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_machine_vision_camera_v0.yaml`
- **BOM available:** No
