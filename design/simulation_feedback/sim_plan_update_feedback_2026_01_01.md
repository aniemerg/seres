# sim plan Update Feedback - 2026-01-01

## Summary

The updated `sim plan` command is a **MASSIVE improvement** and addresses the primary issue from my original feedback. This is exactly what was needed for ISRU planning!

---

## ✅ What's VASTLY Improved

### 1. **Full Dependency Trees** - EXCELLENT!

The new output shows complete dependency trees tracing all the way back to raw materials:

```
├─ Aluminum alloy ingot (1.00 kg, ~1.00 kg)  [← recipe_aluminum_alloy_ingot_v0]
  via: aluminum_smelting_hall_heroult_v0
  ├─ Alumina powder (2.00 kg)  [← recipe_alumina_powder_v0]
    via: alumina_extraction_from_highlands_v0
    ├─ Lunar Highland Regolith (100.00 kg)  [ISRU/boundary, ← recipe_regolith_lunar_highlands_v0]
      via: regolith_mining_lunar_highlands_v0
```

**Impact**: This is transformative! Now users can:
- See the complete production chain at a glance
- Understand all intermediate steps
- Identify process sequences

### 2. **ISRU Markers** - PERFECT!

Items are clearly marked:
- `[ISRU/boundary]` - Local lunar resources (regolith, ice, etc.)
- `[IMPORT]` - Must be imported from Earth
- `[← recipe_name]` - Can be manufactured locally

**Example**:
```
Raw Materials (ISRU/Boundary):
  • regolith_carbonaceous: 50.00 kg
  • regolith_lunar_highlands: 21500.00 kg
  • regolith_lunar_mare: 1.50 kg
  • regolith_polar_psc: 87.12 kg

Must Import or Collect:
  • fluorite: 0.04 kg
  • salt_waste: 8712.20 kg (~871.22 kg)
```

**Impact**: **THIS IS EXACTLY WHAT I ASKED FOR!** Now you can immediately answer:
- "Can I make this on the Moon?"
- "What do I need to import?"
- "What's my ISRU percentage?"

### 3. **Aggregate Materials Summary** - INCREDIBLY USEFUL!

The summary section is brilliant:

```
AGGREGATE MATERIALS NEEDED:

Raw Materials (ISRU/Boundary):
  • regolith_lunar_highlands: 21500.00 kg

Must Import or Collect:
  • fluorite: 0.04 kg
  • salt_waste: 8712.20 kg

Intermediate Materials (produced & consumed):
  • alumina_powder: 4.15 kg
  • hydrochloric_acid: 215.00 kg
  ...
```

**Impact**: Perfect for planning bootstrap imports! Shows:
- Total raw materials needed (how much to mine)
- Total imports required (what to ship from Earth)
- All intermediate products (what gets manufactured along the way)

### 4. **Process Path Visibility** - GREAT!

The `via:` lines show which processes are used:

```
via: aluminum_smelting_hall_heroult_v0, alumina_extraction_from_highlands_v0, regolith_mining_lunar_highlands_v0
```

**Impact**: Helps understand:
- What processes are required
- What machines you need to build
- Process sequence and dependencies

### 5. **Clear Visual Hierarchy**

The tree structure with indentation and symbols (├─, │, ⚠) makes it easy to:
- Follow dependency chains
- Spot imports vs. ISRU at a glance
- See where recursion hits max depth

---

## 🎯 Addresses My Original Feedback

From my original report, issue #1 was:

> **CRITICAL: `sim plan` doesn't help with ISRU decisions**

### ✅ **COMPLETELY FIXED!**

The new `sim plan` now:
- ✅ Shows full dependency tree
- ✅ Distinguishes local vs. import materials
- ✅ Shows path from raw materials to final product
- ✅ Helps answer "Can I make this on the Moon?" - **YES!**

**Before**:
```
Required machines/resources:
  assembly_station: 1 unit
Inputs: none specified
```

**After**:
```
Raw Materials (ISRU/Boundary):
  • regolith_lunar_highlands: 21500.00 kg
Must Import:
  • fluorite: 0.04 kg
  • salt_waste: 8712.20 kg
```

**Night and day difference!**

---

## 💡 Suggestions for Further Polish

### 1. **Add ISRU Percentage Calculation**

Show an overall ISRU % metric at the end:

```
ISRU SUMMARY:
  Local materials: 21,550 kg (regolith + ice)
  Required imports: 871 kg (chemicals + misc)
  ISRU ratio: 96.1% by mass
```

### 2. **Flag Critical Import Bottlenecks**

Highlight items that are:
- Required in large quantities
- Have no recipe path
- Would significantly impact ISRU %

```
⚠️  CRITICAL IMPORTS (no local production path):
  • salt_waste: 8,712 kg (87% of import mass)
  • fluorite: 0.04 kg

💡 Recommendation: Develop salt_waste recycling to improve ISRU%
```

### 3. **Show Estimated Time and Energy** (if possible)

From recipe/process time_model and energy_model:

```
ESTIMATED TOTALS (based on time/energy models):
  Duration: ~30-40 hours
  Energy: ~180-200 kWh
  Labor bot hours: ~15 hr
```

Would help with:
- Mission planning
- Power system sizing
- Labor bot workforce planning

### 4. **Add Export/Save Option**

```bash
python -m src.cli sim plan --recipe recipe_aluminum_alloy_ingot_v0 --export plan.json
```

For programmatic use or integration with other tools.

### 5. **Consider Depth Limit Flag**

Allow controlling the max depth:

```bash
python -m src.cli sim plan --recipe X --max-depth 10
```

Some chains might need deeper traversal, others might be cluttered.

### 6. **Highlight Circular Dependencies**

If a material appears multiple times in its own dependency chain (recycling loops), mark it:

```
├─ Sodium chloride (4.00 kg)  [← recipe_recovered_salt_v0]  🔄 RECYCLED
  via: chloride_recycling_to_hcl_v0
  ├─ Salt waste (10.00 kg)  [recycling source]
```

Shows material efficiency / circular economy aspects.

---

## 🐛 Remaining Issues (from original feedback)

### 1. **Auto-Duration Calculation Still Broken**

**Status**: ❌ NOT FIXED

Process has valid time_model, `sim plan` says "Duration calculation: ok", but `start-process` still fails:

```bash
$ python -m src.cli sim plan --process regolith_mining_highlands_v0
Duration calculation: ok

$ python -m src.cli sim start-process --sim-id test --process regolith_mining_highlands_v0
✗ Failed to start process: Must provide either duration_hours or (output_quantity + output_unit)
```

**Recommendation**: This needs fixing or the error message needs improvement. Users expect "Duration calculation: ok" to mean it will work.

### 2. **Confusing Recipe Output Messages**

**Status**: Not tested yet (will check)

Recipe messages showing "Steps: 0" and "Duration: 0.00" when clearly not zero.

---

## 📊 Before/After Comparison

### Original Feedback Question:

> **User**: "It doesn't seem like sim plan actually helped with that?"
> **Answer**: Correct! It didn't help at all for ISRU planning.

### Now:

> **User**: "Can I make aluminum on the Moon?"
> **Answer**: YES! `sim plan` shows:
> - Highland regolith (local) → Alumina → Aluminum
> - Only need to import: fluorite (0.04 kg) and salt (871 kg)
> - **96% ISRU by mass!**

**This is exactly what we needed!**

---

## 🎯 Use Cases Now Supported

### 1. **ISRU Feasibility Analysis**

```bash
python -m src.cli sim plan --recipe recipe_robot_arm_link_aluminum_v0
# See immediately: what's local, what's imported, is it viable?
```

### 2. **Bootstrap Planning**

```bash
python -m src.cli sim plan --recipe recipe_labor_bot_basic_v0
# Get complete import list for first labor bot
# Use to plan initial cargo manifest
```

### 3. **Production Chain Validation**

```bash
python -m src.cli sim plan --recipe recipe_aluminum_alloy_ingot_v0
# Verify complete chain from regolith to metal
# Check for missing recipes or gaps
```

### 4. **Mission Requirements Scoping**

```bash
python -m src.cli sim plan --recipe recipe_power_electronics_module_v0
# Understand what can/can't be made locally
# Size initial imports accordingly
```

---

## 💯 Overall Assessment

### Before Update: 3/10
- Showed only immediate requirements
- No ISRU insight
- Not useful for planning

### After Update: 9/10
- Complete dependency analysis ✅
- Clear ISRU markers ✅
- Aggregate materials summary ✅
- Massively useful for planning ✅

**Missing that last point for:**
- ISRU % calculation
- Time/energy estimates
- Critical import flagging

---

## 🙏 Feedback to Developers

**This is an EXCELLENT update!** The new `sim plan` command transforms the simulation workflow from:

**Before**:
1. Manually read recipe YAMLs
2. Trace dependencies by hand
3. Search for intermediate recipes
4. Trial and error to find imports
5. (Very tedious and error-prone)

**After**:
1. Run `sim plan --recipe X`
2. See complete production chain
3. Identify imports immediately
4. (Fast, accurate, comprehensive)

This is a **10x improvement in usability** for ISRU planning.

**Specific praise**:
- The tree visualization is clear and informative
- The ISRU/boundary markers are perfect
- The aggregate summary is exactly what's needed
- Process paths help understand the flow

**Please consider the polish suggestions** above to make it even better:
- ISRU % metric
- Critical import flagging
- Time/energy estimates
- Export option

**But even as-is, this is a huge win!**

---

## 📋 Updated Priority Recommendations

**High Priority** (from original feedback):
1. ✅ **FIXED!** Add ISRU dependency analysis to `sim plan`
2. ❌ **Still broken** - Fix auto-duration calculation
3. ❓ **Not tested** - Fix misleading recipe output messages

**New High Priority** (polish the excellent foundation):
4. Add ISRU % calculation to plan output
5. Flag critical imports (no recipe path, large quantities)
6. Add time/energy estimates from models

**Medium Priority**:
7. Add export/save option for plans
8. Add depth limit control
9. Highlight recycling loops

---

## 🎉 Conclusion

The updated `sim plan` command **completely addresses my primary concern** from the original feedback. It's now an invaluable tool for ISRU planning and makes the simulation system much more usable.

**Recommendation**: Ship it! 🚀

The remaining issues (auto-duration, recipe messages) are important but separate from the planning improvements.

**Thank you for the excellent work on this update!**
