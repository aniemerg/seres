# Fix Intelligence: recipe_antenna_matching_network_v0

## Files

- **Recipe:** `kb/recipes/recipe_antenna_matching_network_v0.yaml`
- **Target item:** `antenna_matching_network_v0`
  - File: `kb/items/antenna_matching_network_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'antenna_matching_network_assembly_v0') requires input 'electronic_components_set' which is not available

**Location:** Step 0
**Process:** `antenna_matching_network_assembly_v0`
  - File: `kb/processes/antenna_matching_network_assembly_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: antenna_matching_network_assembly_v0
  inputs:
  - item_id: electronic_components_set
    qty: 0.2
    unit: kg
  - item_id: enclosure_small
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `electronic_components_set` not found

This item doesn't exist in the KB.

#### Problem: Item `enclosure_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_antenna_matching_network_v0.yaml`
- **BOM available:** No
