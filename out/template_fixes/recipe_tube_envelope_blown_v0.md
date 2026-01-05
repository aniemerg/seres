# Fix Intelligence: recipe_tube_envelope_blown_v0

## Files

- **Recipe:** `kb/recipes/recipe_tube_envelope_blown_v0.yaml`
- **Target item:** `tube_envelope_blown`
  - File: `kb/items/tube_envelope_blown.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'glass_blowing_process_v0') requires input 'glass_tube_borosilicate' which is not available

**Location:** Step 0
**Process:** `glass_blowing_process_v0`
  - File: `kb/processes/glass_blowing_process_v0.yaml`

**Current step:**
```yaml
- process_id: glass_blowing_process_v0
  inputs:
  - item_id: glass_tube_borosilicate
    qty: 0.02
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `glass_tube_borosilicate` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_tube_envelope_blown_v0.yaml`
- **BOM available:** No
