# Fix Intelligence: recipe_fixture_assembly_contacts_v0

## Files

- **Recipe:** `kb/recipes/recipe_fixture_assembly_contacts_v0.yaml`
- **Target item:** `fixture_assembly_contacts`
  - File: `kb/items/fixture_assembly_contacts.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'procure_fixture_assembly_contacts_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 0
**Process:** `procure_fixture_assembly_contacts_v0`
  - File: `kb/processes/procure_fixture_assembly_contacts_v0.yaml`

**Current step:**
```yaml
- process_id: procure_fixture_assembly_contacts_v0
  inputs:
  - item_id: raw_metal_block
    qty: 0.5
    unit: kg
  - item_id: fastener_kit_small
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `raw_metal_block` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_fixture_assembly_contacts_v0.yaml`
- **BOM available:** No
