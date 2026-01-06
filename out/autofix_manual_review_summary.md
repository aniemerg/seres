# Auto-Fix Manual Review Summary

**Date:** 2026-01-04
**Experiment:** 10 recipes, 17 fix attempts tested
**Validation:** 100% passed (17/17)
**Semantic correctness:** MIXED - see analysis below

---

## Key Finding: Validation ≠ Correctness

**All fixes passed validation** but **many are semantically incorrect**.

### Why This Happens

Validation only checks:
- ✅ Do the referenced items exist in KB?
- ✅ Are items available (from recipe inputs, BOM, or previous outputs)?

Validation does NOT check:
- ❌ Do the inputs make sense for the process?
- ❌ Should ALL BOM components be used, or just some?
- ❌ Are the quantities appropriate?

---

## Strategy Analysis

### Strategy 1: BOM All Components

**Approach:** Add ALL BOM components as step inputs

**Results:**
- Validation success: 8/8 (100%)
- Semantic correctness: **LOW (est. 20-40%)**

**Problems Observed:**

#### Example 1: recipe_3d_printer_basic_v0, Step 1 (calibration)

**BOM fix:**
```yaml
inputs:
- printer_frame_generic
- extruder_head_basic
- power_electronics_module
- power_supply_low_voltage
- power_supply_chassis_basic
```

**Analysis:** ⚠️ **QUESTIONABLE**
- Adds ALL 5 BOM components to calibration step
- Alternative (previous output): Just use assembled `3d_printer_basic_v0`
- **Better approach:** Calibrate the assembled unit, not individual components

#### Example 2: recipe_acid_reactor_v0, Step 0 (welding)

**BOM fix:**
```yaml
inputs:
- chemical_reactor_vessel_v0
- acid_resistant_lining
- jacket_with_fittings
- reactor_agitator_mixer_v0  # ← Can't weld a mixer!
- gas_outlet_manifold
- valve_set_gas_handling      # ← Can't weld valves!
- thermocouple_type_s_v0      # ← Can't weld a sensor!
```

**Analysis:** ❌ **WRONG**
- Notes say "Fabricate stainless steel vessel"
- Should use raw steel, not finished components
- Mixer, valves, thermocouples are ADDED later, not welded

#### Example 3: recipe_acid_reactor_v0, Step 1 (ceramic coating)

**BOM fix:** Adds ALL 7 components again

**Analysis:** ❌ **WRONG**
- Notes say "Apply acid-resistant lining"
- Should coat ONE thing (the vessel), not 7 things
- Adding `acid_resistant_lining` as INPUT to apply lining doesn't make sense

### Strategy 2: Previous Step Outputs

**Approach:** Use outputs from previous steps as inputs

**Results:**
- Validation success: 9/9 (100%)
- Semantic correctness: **MEDIUM-HIGH (est. 60-80%)**

**Problems Observed:**

#### Example 1: recipe_3d_printer_basic_v0, Step 1 (calibration)

**Previous output fix:**
```yaml
inputs:
- 3d_printer_basic_v0  # From step 0
```

**Analysis:** ✅ **CORRECT**
- Calibrate the assembled printer from previous step
- Makes logical sense

#### Example 2: recipe_acid_reactor_v0, Step 1 (coating)

**Previous output fix:**
```yaml
inputs:
- welded_fabrications (9.5 kg)  # From step 0
```

**Analysis:** ✅ **CORRECT**
- Coat the welded vessel from previous step
- Makes logical sense

**Limitations:**

When previous step doesn't produce the right output, this strategy fails:
- Step 0 produces "widget_base"
- Step 1 needs "widget_base" + "fasteners" + "sealant"
- Previous output only gives 1/3 of needed inputs

---

## Patterns Identified

### Pattern 1: Final Assembly/Test Steps

**Observation:** When step is assembly/calibration/test of final product:
- **BOM fix**: Adds all individual components
- **Previous output fix**: Uses assembled product from earlier
- **Winner**: Previous output (usually correct)

**Examples:**
- Calibration: Should calibrate assembled unit, not components
- Integration test: Should test integrated system, not parts
- Final assembly: Previous step likely produced sub-assembly

### Pattern 2: Fabrication Steps (Early in Recipe)

**Observation:** When step is welding/forming/machining raw materials:
- **BOM fix**: Adds finished components (WRONG - they don't exist yet!)
- **Previous output fix**: Often N/A (step 0 has no previous)
- **Winner**: Neither - needs raw materials not in BOM

**Examples:**
- Welding: Needs raw steel, not finished valve assemblies
- Casting: Needs molten metal, not finished parts
- Machining: Needs bar stock, not machined components

### Pattern 3: Middle Processing Steps

**Observation:** Sequential processing (coat, heat-treat, inspect):
- **BOM fix**: Adds all components (usually wrong)
- **Previous output fix**: Uses output from immediate predecessor (usually correct)
- **Winner**: Previous output

**Examples:**
- Coating after welding: Coat the welded part
- Heat treat after machining: Heat treat the machined part
- Inspection after assembly: Inspect the assembly

---

## Recommendations

### For Auto-Fix Deployment

**DO NOT auto-apply BOM fixes** without human review:
- High false positive rate (60-80%)
- Often adds components that can't be used in that process
- Validation passes but semantics are wrong

**CAN auto-apply previous output fixes** with confidence threshold:
- Medium-high success rate (60-80%)
- Logical for sequential processing
- Lower risk of semantic errors

**Suggested auto-fix rules:**

```python
if step_idx > 0 and previous_step_produces_output:
    # High confidence: Use previous output for middle/late steps
    if step_idx > len(steps) / 2:  # Second half of recipe
        AUTO_APPLY = True
    else:
        SUGGEST_ONLY = True
elif bom_exists and step_idx == len(steps) - 1:
    # Low-medium confidence: BOM for final assembly/test only
    SUGGEST_ONLY = True
else:
    # No auto-fix
    MANUAL_ONLY = True
```

### For Agent-Assisted Fixing

**Provide both strategies** with context:

```markdown
### Option A: Previous step output (RECOMMENDED)
- item_id: welded_fabrications
- Reasoning: Sequential processing - coat the welded part

### Option B: BOM components (USE WITH CAUTION)
- 7 components including valves, sensors, mixers
- Warning: Check if ALL components needed for THIS step
- Note: Some may be added in later steps
```

**Add semantic checks:**
- Process is "welding" + input is "thermocouple" = FLAG (can't weld sensors!)
- Process is "coating" + 10+ inputs = FLAG (coating usually 1 item)
- Process is "calibration" + inputs are individual parts = FLAG (calibrate assembly)

### For Tool Enhancement

**Improve BOM strategy:**
1. Filter BOM by material compatibility
   - Welding: Only metal items
   - Coating: Only items that can be coated (not liquids/gases)
   - Assembly: Only structural components (not consumables)

2. Use process notes as hints
   - "Fabricate vessel" → Look for vessel-related items, not accessories
   - "Install mixer" → Look for mixer, not vessel

3. Rank by relevance
   - Primary structural components first
   - Accessories/sensors last
   - Let agent choose how many to include

---

## Statistics Summary

| Metric | Value |
|--------|-------|
| Total fixes attempted | 17 |
| Validation passed | 17 (100%) |
| BOM fixes | 8 |
| Previous output fixes | 9 |
| **Estimated semantic correctness:** | |
| - BOM strategy | 20-40% |
| - Previous output strategy | 60-80% |
| **Overall semantic correctness** | ~50% |

---

## Conclusion

**Auto-fix is possible BUT requires intelligence:**

1. ✅ **Previous output strategy** is reasonably safe for auto-apply with rules
2. ❌ **BOM all-components strategy** needs heavy filtering or human review
3. 📊 **Validation alone is insufficient** - semantic checks needed
4. 🤖 **Agent-assisted fixing** is the sweet spot - provide smart suggestions, let agent decide

**Next steps:**
1. Enhance BOM filtering (material type, process compatibility)
2. Add semantic validation rules (process-input compatibility checks)
3. Deploy conservative auto-fix for "previous output" strategy only
4. Keep BOM suggestions for agent review
5. Aim for 80%+ semantic correctness before auto-deployment
