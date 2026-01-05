# Fix Intelligence: recipe_magnetic_tape_reel_v0

## Files

- **Recipe:** `kb/recipes/recipe_magnetic_tape_reel_v0.yaml`
- **Target item:** `magnetic_tape_reel`
  - File: `kb/items/magnetic_tape_reel.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'magnetic_tape_reel_fabrication_v0') requires input 'iron_powder_v0' which is not available

**Location:** Step 0
**Process:** `magnetic_tape_reel_fabrication_v0`
  - File: `kb/processes/magnetic_tape_reel_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: magnetic_tape_reel_fabrication_v0
  inputs:
  - item_id: polyester_film
    qty: 0.03
    unit: kg
  - item_id: iron_powder_v0
    qty: 0.01
    unit: kg
  - item_id: plastic_pellets
    qty: 0.01
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `polyester_film` not found

This item doesn't exist in the KB.

#### Problem: Item `iron_powder_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `plastic_pellets` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_magnetic_tape_reel_v0.yaml`
- **BOM available:** No
