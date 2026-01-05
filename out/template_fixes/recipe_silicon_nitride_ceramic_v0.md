# Fix Intelligence: recipe_silicon_nitride_ceramic_v0

## Files

- **Recipe:** `kb/recipes/recipe_silicon_nitride_ceramic_v0.yaml`
- **Target item:** `silicon_nitride_ceramic_v0`
  - File: `kb/items/silicon_nitride_ceramic_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'powder_milling_process_v0') requires input 'silicon_powder_v0' which is not available

**Location:** Step 0
**Process:** `powder_milling_process_v0`
  - File: `kb/processes/powder_milling_process_v0.yaml`

**Current step:**
```yaml
- process_id: powder_milling_process_v0
  inputs:
  - item_id: silicon_powder_v0
    qty: 0.7
    unit: kg
  - item_id: nitrogen_gas_purified
    qty: 0.3
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `silicon_powder_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `nitrogen_gas_purified` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'powder_compaction_process_v0') requires input 'sintering_aid_mgo' which is not available

**Location:** Step 1
**Process:** `powder_compaction_process_v0`
  - File: `kb/processes/powder_compaction_process_v0.yaml`

**Current step:**
```yaml
- process_id: powder_compaction_process_v0
  inputs:
  - item_id: silicon_nitride_powder_fine
    qty: 0.95
    unit: kg
  - item_id: sintering_aid_mgo
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `silicon_nitride_powder_fine` not found

This item doesn't exist in the KB.

#### Problem: Item `sintering_aid_mgo` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_silicon_nitride_ceramic_v0.yaml`
- **BOM available:** No
