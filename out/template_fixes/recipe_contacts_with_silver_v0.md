# Fix Intelligence: recipe_contacts_with_silver_v0

## Files

- **Recipe:** `kb/recipes/recipe_contacts_with_silver_v0.yaml`
- **Target item:** `contacts_with_silver`
  - File: `kb/items/contacts_with_silver.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'contact_material_application_v0') requires input 'steel_sheet_1mm' which is not available

**Location:** Step 0
**Process:** `contact_material_application_v0`
  - File: `kb/processes/contact_material_application_v0.yaml`

**Current step:**
```yaml
- process_id: contact_material_application_v0
  inputs:
  - item_id: steel_sheet_1mm
    qty: 0.05
    unit: kg
  - item_id: silver_contact_material
    qty: 0.005
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_sheet_1mm` not found

This item doesn't exist in the KB.

#### Problem: Item `silver_contact_material` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_contacts_with_silver_v0.yaml`
- **BOM available:** No
