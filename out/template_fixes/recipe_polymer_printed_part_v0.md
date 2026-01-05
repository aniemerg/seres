# Fix Intelligence: recipe_polymer_printed_part_v0

## Files

- **Recipe:** `kb/recipes/recipe_polymer_printed_part_v0.yaml`
- **Target item:** `polymer_printed_part`
  - File: `kb/items/polymer_printed_part.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'additive_manufacturing_polymer_v0') requires input 'polymer_printing_feedstock' which is not available

**Location:** Step 0
**Process:** `additive_manufacturing_polymer_v0`
  - File: `kb/processes/additive_manufacturing_polymer_v0.yaml`

**Current step:**
```yaml
- process_id: additive_manufacturing_polymer_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_polymer_printed_part_v0.yaml`
- **BOM available:** No
