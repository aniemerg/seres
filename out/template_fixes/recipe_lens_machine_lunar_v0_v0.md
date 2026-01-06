# Fix Intelligence: recipe_lens_machine_lunar_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_lens_machine_lunar_v0_v0.yaml`
- **Target item:** `lens_machine_lunar_v0`
  - File: `kb/items/lens_machine_lunar_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'lens_machine_lunar_v0_assembly_v0') requires input 'machine_frame_small' which is not available

**Location:** Step 0
**Process:** `lens_machine_lunar_v0_assembly_v0`
  - File: `kb/processes/lens_machine_lunar_v0_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: lens_machine_lunar_v0_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_lens_machine_lunar_v0_v0.yaml`
- **BOM available:** No
