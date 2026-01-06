# Fix Intelligence: recipe_housing_with_contacts_v0

## Files

- **Recipe:** `kb/recipes/recipe_housing_with_contacts_v0.yaml`
- **Target item:** `housing_with_contacts`
  - File: `kb/items/housing_with_contacts.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'contact_material_application_v0') requires input 'breaker_housing_and_mechanism' which is not available

**Location:** Step 0
**Process:** `contact_material_application_v0`
  - File: `kb/processes/contact_material_application_v0.yaml`

**Current step:**
```yaml
- process_id: contact_material_application_v0
  inputs:
  - item_id: breaker_housing_and_mechanism
    qty: 0.09
    unit: kg
  - item_id: silver_contact_material
    qty: 0.01
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `breaker_housing_and_mechanism` not found

This item doesn't exist in the KB.

#### Problem: Item `silver_contact_material` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_housing_with_contacts_v0.yaml`
- **BOM available:** No
