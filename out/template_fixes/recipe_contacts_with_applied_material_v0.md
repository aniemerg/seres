# Fix Intelligence: recipe_contacts_with_applied_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_contacts_with_applied_material_v0.yaml`
- **Target item:** `contacts_with_applied_material_v0`
  - File: `kb/items/contacts_with_applied_material_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'contact_material_application_v0') requires input 'contact_substrate_base' which is not available

**Location:** Step 0
**Process:** `contact_material_application_v0`
  - File: `kb/processes/contact_material_application_v0.yaml`

**Current step:**
```yaml
- process_id: contact_material_application_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_contacts_with_applied_material_v0.yaml`
- **BOM available:** No
