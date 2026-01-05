# Fix Intelligence: recipe_nickel_metal_pure_v0

## Files

- **Recipe:** `kb/recipes/recipe_nickel_metal_pure_v0.yaml`
- **Target item:** `nickel_metal_pure`
  - File: `kb/items/nickel_metal_pure.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mond_carbonyl_process_nickel_v0') requires input 'nickel_metal' which is not available

**Location:** Step 0
**Process:** `mond_carbonyl_process_nickel_v0`
  - File: `kb/processes/mond_carbonyl_process_nickel_v0.yaml`

**Current step:**
```yaml
- process_id: mond_carbonyl_process_nickel_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_nickel_metal_pure_v0.yaml`
- **BOM available:** No
