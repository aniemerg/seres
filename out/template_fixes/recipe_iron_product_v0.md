# Fix Intelligence: recipe_iron_product_v0

## Files

- **Recipe:** `kb/recipes/recipe_iron_product_v0.yaml`
- **Target item:** `iron_product`
  - File: `kb/items/iron_product.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'iron_reduction_from_ilmenite_v0') requires input 'ilmenite_concentrate' which is not available

**Location:** Step 0
**Process:** `iron_reduction_from_ilmenite_v0`
  - File: `kb/processes/iron_reduction_from_ilmenite_v0.yaml`

**Current step:**
```yaml
- process_id: iron_reduction_from_ilmenite_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_iron_product_v0.yaml`
- **BOM available:** No
