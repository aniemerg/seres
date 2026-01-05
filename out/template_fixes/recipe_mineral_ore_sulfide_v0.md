# Fix Intelligence: recipe_mineral_ore_sulfide_v0

## Files

- **Recipe:** `kb/recipes/recipe_mineral_ore_sulfide_v0.yaml`
- **Target item:** `mineral_ore_sulfide`
  - File: `kb/items/mineral_ore_sulfide.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mineral_ore_sulfide_extraction_v0') requires input 'regolith_carbonaceous' which is not available

**Location:** Step 0
**Process:** `mineral_ore_sulfide_extraction_v0`
  - File: `kb/processes/mineral_ore_sulfide_extraction_v0.yaml`

**Current step:**
```yaml
- process_id: mineral_ore_sulfide_extraction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_mineral_ore_sulfide_v0.yaml`
- **BOM available:** No
