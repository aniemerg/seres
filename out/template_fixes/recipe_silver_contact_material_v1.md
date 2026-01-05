# Fix Intelligence: recipe_silver_contact_material_v1

## Files

- **Recipe:** `kb/recipes/recipe_silver_contact_material_v1.yaml`
- **Target item:** `silver_contact_material`
  - File: `kb/items/silver_contact_material.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_silver_contact_material_v0` → silver_contact_material (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'casting_silver_contact_material_v0') requires input 'silver_ingot' which is not available

**Location:** Step 0
**Process:** `casting_silver_contact_material_v0`
  - File: `kb/processes/casting_silver_contact_material_v0.yaml`

**Current step:**
```yaml
- process_id: casting_silver_contact_material_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_silver_contact_material_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
