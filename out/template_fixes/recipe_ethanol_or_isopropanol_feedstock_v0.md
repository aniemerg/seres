# Fix Intelligence: recipe_ethanol_or_isopropanol_feedstock_v0

## Files

- **Recipe:** `kb/recipes/recipe_ethanol_or_isopropanol_feedstock_v0.yaml`
- **Target item:** `ethanol_or_isopropanol_feedstock_v0`
  - File: `kb/items/ethanol_or_isopropanol_feedstock_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ethanol_feedstock_prep_basic_v0') requires input 'methanol_liquid' which is not available

**Location:** Step 0
**Process:** `ethanol_feedstock_prep_basic_v0`
  - File: `kb/processes/ethanol_feedstock_prep_basic_v0.yaml`

**Current step:**
```yaml
- process_id: ethanol_feedstock_prep_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ethanol_or_isopropanol_feedstock_v0.yaml`
- **BOM available:** No
