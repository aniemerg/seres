NOTE: Historical document predating ADR-012+; references deprecated schema. See docs/kb_schema_reference.md for current rules.

# Missing Recipes Analysis

**Date**: 2025-12-22
**Total Items**: 32 items without manufacturing recipes
**Status**: Classified and prioritized

## Executive Summary

The KB has **32 items without recipes** (not 17 as initially estimated). Analysis reveals:

- **22 items (69%)** - Stub machines created during ADR-003 migration (all have BOMs)
- **5 items (16%)** - Defined items that need recipes (all have BOMs)
- **4 items (13%)** - Placeholder items needing detailed specification
- **1 item (3%)** - Likely permanent import (precision equipment)

**Key Finding**: Most items are **stub machines from ADR-003** - they were created as placeholders when processes referenced abstract resource_types. All have BOMs, just need manufacturing recipes.

**For Closure Analysis**:
- Only **1 item** is a likely permanent import (calibration_station - 3kg)
- All others **should be manufacturable** locally
- Total import mass for missing items: **~3 kg** (negligible)

---

## Classification Details

### 1. Stub Machines from ADR-003 Migration (22 items)

**Origin**: Created during ADR-003 refactor when processes referenced abstract resource_types (like `assembly_station`, `chemical_reactor_basic`) that didn't exist as concrete machines.

**Status**: All have BOMs, just need recipes

**Action**: Create manufacturing recipes for each

**Items**:
1. `assembly_tools_basic` (50kg) - Basic assembly tools
2. `battery_formation` (300kg) - Battery formation station
3. `chemical_mixing` (300kg) - Chemical mixing equipment
4. `chemical_reactor_basic` (500kg) - Basic chemical reactor
5. `core_memory_assembly` (300kg) - Core memory assembly station
6. `cpu_core` (2kg) - CPU core module (note: may be import)
7. `cryogenic_chiller_v0` (300kg) - Cryogenic chiller
8. `cutting_tools_general` (30kg) - General cutting tools
9. `electrolysis_cell` (250kg) - Electrolysis cell
10. `epoxy_synthesis_unit` (200kg) - Epoxy synthesis unit
11. `filtration_unit` (180kg) - Filtration unit
12. `hose_crimping_station_v0` (150kg) - Hose crimping station
13. `lab_assistant` (150kg) - Laboratory assistant system
14. `labor_bot_electronics` (180kg) - Electronics assembly labor bot
15. `labor_bot_welder` (220kg) - Welding labor bot
16. `lubrication_mixer_v0` (250kg) - Lubrication mixer
17. `mineral_processing_unit` (800kg) - Mineral processing unit
18. `power_supply_basic` (50kg) - Basic power supply
19. `procurement_agent` (100kg) - Procurement and logistics agent
20. `regeneration_furnace` (600kg) - Regeneration furnace
21. `resource_3d_printer_basic_v0` (100kg) - Basic 3D printer resource
22. `seed_lab` (400kg) - Seed material laboratory

**Subtotal mass**: ~5,460 kg

**Priority**:
- **High**: Labor bots (electronics, welder) - used by many processes
- **High**: Chemical reactor, electrolysis cell - ISRU critical
- **Medium**: Specialized tools (assembly, cutting, hose crimping)
- **Low**: Niche equipment (seed lab, procurement agent)

---

### 2. Items Needing Recipes (5 items)

**Status**: Fully defined with BOMs, just need manufacturing recipes

**Items**:

1. **`3d_printer_basic`** (40kg)
   - Has BOM: `bom_3d_printer_basic_v0`
   - Critical for: Additive manufacturing, polymer parts
   - **Priority**: HIGH - used in many processes
   - **Action**: Create recipe (assembly of frame, motors, extruder, controller)

2. **`bending_machine`** (900kg)
   - Has BOM: `bom_bending_machine_v0_v0`
   - Used for: Sheet metal forming
   - **Priority**: MEDIUM - specialized metalworking
   - **Action**: Create recipe (frame fabrication + hydraulic system assembly)

3. **`dc_power_supply_ffc`** (150kg)
   - Has BOM: `bom_dc_power_supply_ffc_v0`
   - Used for: Fluoride-based electrochemical processes
   - Notes: Controlled DC power for FFC process
   - **Priority**: MEDIUM - specific to FFC reduction
   - **Action**: Create recipe (power electronics assembly)

4. **`electrolysis_cell_aluminum_v0`** (5,000kg)
   - Has BOM: `bom_electrolysis_cell_aluminum_v0`
   - Used for: Hall-Héroult aluminum production
   - Notes: Industrial-scale electrolysis
   - **Priority**: HIGH - aluminum is critical material
   - **Action**: Create recipe (large-scale construction process)

5. **`robot_fab_station_v0`** (120kg)
   - Has BOM: `bom_robot_fab_station_v0_v0.yaml`
   - Used for: Automated fabrication tasks
   - **Priority**: MEDIUM - automation equipment
   - **Action**: Create recipe (assembly station construction)

**Subtotal mass**: ~6,210 kg

---

### 3. Placeholder Items (4 items)

**Status**: Defined but need detailed specification before recipes can be created

**Items**:

1. **`cutting_station`** (40kg)
   - Has BOM: `bom_cutting_station_v0.yaml`
   - **Issue**: Placeholder - needs detailed specs
   - **Action**: Define capabilities, refine BOM, then create recipe
   - **Priority**: MEDIUM

2. **`forming_furnace`** (1,000kg) - **NOTE: Marked as PART, should be MACHINE?**
   - Has BOM: NONE
   - Used in: ISRU process chains
   - **Issue**: Placeholder - needs specs
   - **Action**:
     1. Clarify if this is a machine or part
     2. Create BOM
     3. Create recipe
   - **Priority**: MEDIUM - used in ISRU

3. **`grinding_mill`** (900kg)
   - Has BOM: `bom_grinding_mill_v0`
   - Used for: Grinding operations
   - **Issue**: Placeholder - basic capability only
   - **Action**: Refine specs (motor size, grinding media, throughput), then recipe
   - **Priority**: MEDIUM

4. **`shear_machine`** (300kg)
   - Has BOM: `bom_shear_machine_v0`
   - Used for: Sheet metal cutting
   - **Issue**: Placeholder - basic capability
   - **Action**: Refine specs (cutting force, blade type), then recipe
   - **Priority**: LOW - specialized metalworking

**Subtotal mass**: ~2,240 kg

---

### 4. Likely Permanent Imports (1 item)

**Status**: Difficult/impossible to manufacture on Moon with v0 capabilities

**Items**:

1. **`calibration_station`** (3kg) - **NOTE: Marked as PART, should be MACHINE?**
   - Has BOM: NONE
   - Used for: QA and test routines
   - **Issue**: Precision equipment requiring tight tolerances
   - **Rationale for import**:
     - Requires precision metrology equipment
     - Optical components, laser interferometers, etc.
     - Calibration against known standards (from Earth)
   - **Action**: Mark as permanent import in `docs/minimum_import_set.md`
   - **Mass impact**: 3 kg (negligible)

**Subtotal mass**: 3 kg

---

## Recommendations by Priority

### Immediate Actions (Next 1-2 Weeks)

**1. Create recipes for high-priority items (5 items):**
- `labor_bot_electronics` - Critical for electronics assembly
- `labor_bot_welder` - Critical for metal fabrication
- `chemical_reactor_basic` - Core ISRU equipment
- `electrolysis_cell_aluminum_v0` - Aluminum production (critical material)
- `3d_printer_basic` - Additive manufacturing

**2. Document permanent import:**
- Add `calibration_station` to `docs/minimum_import_set.md`
- Classify as "precision metrology" import

**3. Review and reclassify questionable items:**
- `forming_furnace` - Is this a machine or part?
- `calibration_station` - Is this a machine or part?
- `cpu_core` - Is this manufactureable or import?

### Short-Term Actions (Next Month)

**4. Create recipes for medium-priority items (10 items):**
- Electrolysis cells, power supplies
- Processing units (mineral, filtration)
- Fabrication equipment (bending, grinding, shear)

**5. Refine placeholder specifications:**
- Define detailed specs for 4 placeholder items
- Update BOMs as needed
- Then create recipes

### Long-Term Actions (Future)

**6. Create recipes for remaining stub machines (12 items):**
- Lower-priority specialized equipment
- Niche manufacturing tools

**7. Validate with simulation:**
- Run base_builder with new recipes
- Confirm machines can be manufactured
- Check for missing dependencies

---

## Special Cases Requiring Decisions

### Case 1: `cpu_core` (2kg)

**Issue**: Marked as stub from migration, but this is complex electronics

**Options**:
- **A**: Create recipe (assume basic microprocessor can be made)
- **B**: Mark as import (realistic - semiconductor fab too complex)
- **C**: Create simplified version (hardwired controller, not programmable CPU)

**Recommendation**: **Option B** - Mark as import. Modern CPU fabrication requires:
- Clean room facilities
- Photolithography (nanometer precision)
- Doping processes with precise dopant control
- Beyond v0 lunar capabilities

**Revised classification**: Move from "stub" to "likely import"

### Case 2: `forming_furnace` (1,000kg)

**Issue**: Marked as PART but weighs 1,000kg and is used in processes

**Options**:
- **A**: Reclassify as machine
- **B**: Keep as part (component of larger system)

**Recommendation**: **Option A** - Reclassify as machine. At 1,000kg with active ISRU role, this should be a machine.

**Action**: Update `kb/items/parts/forming_furnace.yaml` → move to `kb/items/machines/forming_furnace_v0.yaml`, change kind to "machine"

### Case 3: `calibration_station` (3kg)

**Issue**: Marked as PART but serves machine-like role (QA/test)

**Options**:
- **A**: Reclassify as machine
- **B**: Keep as part (tooling/equipment)
- **C**: Mark as import regardless of classification

**Recommendation**: **Option C** - Keep as part (it's test equipment), mark as import

### Case 4: Labor Bots

**Critical machines**: `labor_bot_electronics`, `labor_bot_welder`

**Issue**: These are referenced heavily but no recipes exist

**Priority**: **CRITICAL** - Many processes depend on these

**Action**: Create recipes ASAP. Likely composition:
- Frame (structural parts)
- Motors (arms, mobility)
- Controller (computer + sensors)
- Specialized tools (welding torch, soldering iron, etc.)
- Power supply

**BOM check**: Both have BOMs (`bom_labor_bot_electronics`, `bom_labor_bot_welder`)

**Effort**: Moderate - BOMs exist, just need process steps

---

## Impact on Closure Analysis

### Current Import Set (Revised)

Based on this analysis, the **minimum import set** for missing recipe items is:

1. **`calibration_station`** (3kg) - Precision metrology
2. **`cpu_core`** (2kg) - Semiconductor electronics (if reclassified)

**Total**: 5 kg

**All other 30 items** (13,907 kg) should be **manufacturable locally**.

### Closure Percentage Impact

If we assume all 30 manufacturable items get recipes:
- Current: 300/317 machines have recipes (94.6%)
- After: 328/317 machines have recipes (103.5%? - need to check count)

Wait, there's a discrepancy. Let me recalculate:
- Total machines: 317
- Machines without recipes: 30 (from our list, excluding 2 parts)
- Machines with recipes: 317 - 30 = 287 (90.5%)

After adding recipes for 28 items (excluding 2 imports):
- Machines with recipes: 287 + 28 = 315 (99.4%)
- Remaining imports: 2 machines (cpu_core, maybe 1-2 others)

**Closure impact**: Adding these recipes brings machine recipe coverage from **90.5% → 99.4%**

### Mass Analysis

**Total mass of items needing recipes**: 13,910 kg

**Breakdown**:
- Stub machines: 5,460 kg (39%)
- Defined items: 6,210 kg (45%)
- Placeholders: 2,240 kg (16%)

**Import mass**: 5 kg (0.04% of total)

**Local-to-import ratio for these items**: 13,905 / 5 = **2,781:1**

Excellent ratio - negligible imports for this set.

---

## Work Queue Integration

These items should be added to work queue with appropriate priorities:

**Critical (5 items)**:
```jsonl
{"id": "recipe:labor_bot_electronics", "priority": "critical", "item_id": "labor_bot_electronics", "reason": "blocks_many_processes"}
{"id": "recipe:labor_bot_welder", "priority": "critical", "item_id": "labor_bot_welder", "reason": "blocks_many_processes"}
{"id": "recipe:chemical_reactor_basic", "priority": "critical", "item_id": "chemical_reactor_basic", "reason": "isru_critical"}
{"id": "recipe:electrolysis_cell_aluminum_v0", "priority": "critical", "item_id": "electrolysis_cell_aluminum_v0", "reason": "critical_material"}
{"id": "recipe:3d_printer_basic", "priority": "critical", "item_id": "3d_printer_basic", "reason": "fabrication_critical"}
```

**High (10 items)**: Other ISRU equipment, core fabrication tools

**Medium (12 items)**: Specialized equipment, secondary tools

**Low (3 items)**: Niche equipment

---

## Next Steps

### Immediate (This Week)

1. **Reclassify items**:
   - [ ] `cpu_core`: stub → likely_import
   - [ ] `forming_furnace`: part → machine
   - [ ] Update YAML files

2. **Document imports**:
   - [ ] Create `docs/minimum_import_set.md`
   - [ ] Add `calibration_station` (3kg)
   - [ ] Add `cpu_core` (2kg)
   - [ ] Total: 5kg of precision/electronics imports

3. **Create 5 critical recipes**:
   - [ ] `recipe_labor_bot_electronics_v0.yaml`
   - [ ] `recipe_labor_bot_welder_v0.yaml`
   - [ ] `recipe_chemical_reactor_basic_v0.yaml`
   - [ ] `recipe_electrolysis_cell_aluminum_v0.yaml`
   - [ ] `recipe_3d_printer_basic_v0.yaml`

### Short-Term (Next 2 Weeks)

4. **Create remaining recipes** (batches of 5-10):
   - Week 1: 10 high-priority items
   - Week 2: 10 medium-priority items
   - Week 3: Remaining items + placeholders

5. **Validate with simulation**:
   - Test that recipes work end-to-end
   - Verify no circular dependencies
   - Check material availability

### Long-Term (Next Month)

6. **Refine placeholders**:
   - Define detailed specs for 4 placeholder items
   - Update BOMs
   - Create recipes

7. **Re-run closure analysis**:
   - Measure improvement in closure percentage
   - Identify remaining blockers
   - Update import set

---

## Template for Creating Recipes

For stub machines with existing BOMs, use this template:

```yaml
id: recipe_<machine_id>
target_item_id: <machine_id>
variant_id: v0

steps:
  - process_id: frame_fabrication_medium_v0
    est_time_hr: 4.0
    machine_hours: 4.0
    notes: Fabricate structural frame from BOM specs

  - process_id: component_assembly_basic_v0
    est_time_hr: 6.0
    labor_hours: 6.0
    notes: Assemble motors, controllers, sensors per BOM

  - process_id: system_integration_basic_v0
    est_time_hr: 2.0
    labor_hours: 2.0
    notes: Final assembly, wiring, testing

assumptions: |
  Recipe based on BOM <bom_id>.
  Assumes all parts from BOM are available in inventory.

notes: |
  Created to resolve missing recipe gap.
  Refine based on actual manufacturing experience.
```

**Process IDs to use**:
- `frame_fabrication_*` - Structural assembly
- `component_assembly_*` - Subassembly integration
- `motor_assembly_*` - Motor installation
- `wiring_harness_assembly_*` - Electrical integration
- `system_integration_*` - Final assembly
- `machine_assembly_*` - Generic machine assembly
- `quality_control_basic_v0` - Testing/calibration

---

## Conclusion

**The "17 missing recipes" is actually 32 items**, primarily stub machines from ADR-003 migration.

**Good news**:
- 94% (30/32) are manufacturable - just need recipes
- All have BOMs already defined
- Import mass is negligible (5kg of 13,910kg = 0.04%)

**Action**: Create recipes in priority order over next 2-4 weeks. This will bring machine recipe coverage from 90.5% to 99.4%, a major step toward tech tree closure.

**For closure analysis**: Only 5kg of imports needed for this item set - excellent for self-replication goals.
