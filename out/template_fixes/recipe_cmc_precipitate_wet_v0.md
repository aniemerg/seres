# Fix Intelligence: recipe_cmc_precipitate_wet_v0

## Files

- **Recipe:** `kb/recipes/recipe_cmc_precipitate_wet_v0.yaml`
- **Target item:** `cmc_precipitate_wet`
  - File: `kb/items/cmc_precipitate_wet.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'precipitation_and_washing_v0') requires input 'cmc_solution' which is not available

**Location:** Step 0
**Process:** `precipitation_and_washing_v0`
  - File: `kb/processes/precipitation_and_washing_v0.yaml`

**Current step:**
```yaml
- process_id: precipitation_and_washing_v0
  inputs:
  - item_id: cmc_solution
    qty: 6.0
    unit: kg
  - item_id: ethanol_or_isopropanol
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `cmc_solution` not found

This item doesn't exist in the KB.

#### Problem: Generic placeholder `ethanol_or_isopropanol`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `methanol_liquid`
- `ethanol_or_isopropanol_feedstock_v0`
- `ethanol_or_isopropanol`

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_cmc_precipitate_wet_v0.yaml`
- **BOM available:** No
