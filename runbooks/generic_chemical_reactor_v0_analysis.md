# Generic Chemical Reactor v0 - In-Situ Resource Analysis

## Executive Summary

**Current Status (at 2510 hours / 104.6 days):**
- Machines completed: **0** (recipes still running)
- In-situ mass percentage: **0%** (all consumed materials were imported)
- Regolith processed: 1400 kg → 840 kg powder
- Metal alloy production: In progress (oxygen extraction not complete)

## Recipe Requirements

Each generic_chemical_reactor_v0 requires:
```
- metal_alloy_bulk: 1.0 kg
- machined_part_raw: 1.0 kg
- enclosure_steel_small: 1.0 kg
- assembled_electrical_equipment: 1.0 kg
- electrical_wire_and_connectors: 2.0 kg
- control_components: 1.0 unit
```

Total material mass per reactor (excluding discrete parts): **~6 kg**

## What Was Actually Imported

For 2 reactors (runbook attempted to build 2):
```
- metal_alloy_bulk: 1.0 kg (only enough for 1 reactor!)
- machined_part_raw: 1.0 kg
- enclosure_steel_small: 1.0 kg
- assembled_electrical_equipment: 2.0 kg
- electrical_wire_and_connectors: 4.0 kg
- control_components: 2.0 units
- steel_plate_or_sheet: 2.0 kg (for forming operations)
```

## In-Situ Production Attempted

### Regolith Processing Chain (STARTED)
```
regolith_lunar_mare (1400 kg)
  → screening → regolith_coarse_fraction (840 kg) + regolith_fine_fraction (560 kg)
    → crushing → regolith_powder (840 kg)
      → electrolysis → metal_alloy_bulk (336 kg) [STILL RUNNING - completes at 2724 hours]
```

**Status:** Electrolysis started at 204 hours, will complete at 2724 hours (2520 hour duration)
**Result:** Would produce 336 kg metal_alloy_bulk (enough for 336 reactors!)

### Sheet Metal Forming (COMPLETED)
```
steel_plate_or_sheet (2.0 kg imported)
  → press_brake forming → formed_sheet_metal_parts (1.0 kg)
```

**Status:** Completed at 2504.3 hours
**In-situ percentage:** 0% (used imported steel)

## Why No Machines Were Completed

The runbook advanced time to 2510 hours, but:

1. **First recipe started:** 0 hours, still processing through 7 steps
2. **Second recipe started:** 2506 hours, just began 4 hours ago
3. **Oxygen extraction:** Won't complete until 2724 hours (214 hours remaining)

The recipes need more time to complete their assembly steps.

## Theoretical In-Situ Analysis (If We Waited)

If we waited for the oxygen extraction to complete and used that metal_alloy_bulk:

### Option A: Use In-Situ Metal Alloy for Second Reactor

**Reactor composition by source:**
```
Component                          Mass    Source        In-Situ?
----------------------------------------  -------------  --------
metal_alloy_bulk                   1.0 kg  Regolith      ✓ YES
machined_part_raw                  1.0 kg  Imported      ✗ NO
enclosure_steel_small              1.0 kg  Imported      ✗ NO
assembled_electrical_equipment     1.0 kg  Imported      ✗ NO
electrical_wire_and_connectors     2.0 kg  Imported      ✗ NO
control_components                 1.0 unit Imported     ✗ NO
----------------------------------------
Total mass:                        ~7.0 kg
In-situ mass:                      1.0 kg
In-situ percentage:                14.3%
```

### Option B: Fully In-Situ Metal Components

If we also produced steel plate from the metal_alloy_bulk and used it for enclosures:

**Additional processes needed:**
1. Metal alloy → steel ingot (refining)
2. Steel ingot → steel plate (rolling)
3. Steel plate → enclosure parts (forming)

**Theoretical in-situ potential:**
```
Component                          Mass    Source        In-Situ?
----------------------------------------  -------------  --------
metal_alloy_bulk                   1.0 kg  Regolith      ✓ YES
machined_part_raw                  1.0 kg  Regolith*     ✓ YES*
enclosure_steel_small              1.0 kg  Regolith*     ✓ YES*
assembled_electrical_equipment     1.0 kg  Imported      ✗ NO
electrical_wire_and_connectors     2.0 kg  Imported      ✗ NO
control_components                 1.0 unit Imported     ✗ NO
----------------------------------------
Total mass:                        ~7.0 kg
In-situ mass:                      3.0 kg
In-situ percentage:                42.9%

* Requires additional recipes not in current KB
```

## Closure Gaps Identified

### Tier 1: Achievable with current processes
- ✓ Metal alloys from regolith (process exists, takes 2520 hours)
- ✓ Sheet metal forming (process exists, quick)

### Tier 2: Requires new recipes
- ✗ Steel plate production from metal alloy bulk
- ✗ Machined parts from local metal stock
- ✗ Enclosure fabrication from formed sheet metal

### Tier 3: Major gaps (electronics)
- ✗ Electronic component fabrication
- ✗ Control system assembly
- ✗ Wire and connector production

## Recommendations

1. **Update runbook timing:** Add 220+ hours advance-time after second recipe start to see completion
2. **Add steel processing chain:** Create recipes for metal_alloy_bulk → steel_plate_or_sheet
3. **Connect forming to enclosures:** Map formed_sheet_metal_parts → enclosure_steel_small
4. **Track material provenance:** Enhance simulation to track which kg came from which source
5. **Electronics pathway:** Begin mapping processes for basic electronic component production

## Energy Analysis

- Total energy consumed: 404 kWh (in 2510 hours)
- Regolith processing: ~392 kWh (96.5% of energy)
- Forming operations: ~0.6 kWh
- Assembly operations: ~11 kWh

**Key insight:** Molten regolith electrolysis is extremely energy-intensive (8400 kWh per 336 kg batch = 25 kWh/kg)

## Conclusion

The runbook successfully **demonstrates the production chain** but didn't run long enough to show completed machines. The actual in-situ percentage is **0%** because:
- No machines completed yet
- In-situ metal production (oxygen extraction) still running
- All materials consumed so far were imported

**Maximum achievable in-situ percentage with current KB:** 14.3% (metal alloys only)
**Potential with steel processing recipes:** 42.9% (all metal components)
**Fundamental limit:** ~57% (electronics must be imported with current technology)
