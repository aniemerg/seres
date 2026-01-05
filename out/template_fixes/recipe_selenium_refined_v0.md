# Fix Intelligence: recipe_selenium_refined_v0

## Files

- **Recipe:** `kb/recipes/recipe_selenium_refined_v0.yaml`
- **Target item:** `selenium_refined`
  - File: `kb/items/selenium_refined.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'selenium_extraction_refining_v0') requires input 'mineral_ore_sulfide' which is not available

**Location:** Step 0
**Process:** `selenium_extraction_refining_v0`
  - File: `kb/processes/selenium_extraction_refining_v0.yaml`

**Current step:**
```yaml
- process_id: selenium_extraction_refining_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_selenium_refined_v0.yaml`
- **BOM available:** No
