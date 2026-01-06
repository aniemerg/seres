# Fix Intelligence: recipe_ceramic_binder_v0

## Files

- **Recipe:** `kb/recipes/recipe_ceramic_binder_v0.yaml`
- **Target item:** `ceramic_binder`
  - File: `kb/items/ceramic_binder.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'chemical_synthesis_process_v0') requires input 'cellulose_raw' which is not available

**Location:** Step 0
**Process:** `chemical_synthesis_process_v0`
  - File: `kb/processes/chemical_synthesis_process_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: chemical_synthesis_process_v0
  inputs:
  - item_id: cellulose_raw
    qty: 1.0
    unit: kg
  - item_id: sodium_hydroxide
    qty: 0.3
    unit: kg
  - item_id: monochloroacetic_acid
    qty: 0.4
    unit: kg
  - item_id: water
    qty: 5.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `cellulose_raw` not found

This item doesn't exist in the KB.

#### Problem: Item `sodium_hydroxide` not found

This item doesn't exist in the KB.

#### Problem: Item `monochloroacetic_acid` not found

This item doesn't exist in the KB.

#### Problem: Item `water` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'precipitation_and_washing_v0') requires input 'cmc_solution' which is not available

**Location:** Step 1
**Process:** `precipitation_and_washing_v0`
  - File: `kb/processes/precipitation_and_washing_v0.yaml`

**Current step:**
```yaml
- process_id: precipitation_and_washing_v0
  inputs:
  - item_id: cmc_solution
    qty: 3.5
    unit: kg
  - item_id: ethanol_or_isopropanol
    qty: 1.0
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

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_ceramic_binder_v0.yaml`
- **BOM available:** No
