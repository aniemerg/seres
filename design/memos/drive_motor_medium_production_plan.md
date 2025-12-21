# Drive Motor Medium - Complete Production Plan

## Overview
This document provides a complete production plan for manufacturing drive_motor_medium (90 kg) from ISRU materials.

**Target:** 1 unit drive_motor_medium (90 kg)
**ISRU Potential:** 96% (89.5 kg from regolith, 1.4 kg imports)
**Total Production Time:** ~75-85 hours (including all upstream materials)
**BOMs Unlocked:** 25 (automated machinery, mills, conveyors, etc.)

---

## Production Process Summary

### New Assembly Process Created
**File:** `kb/processes/drive_motor_medium_assembly_v0.yaml`

This process combines all motor components into the final drive motor:

**Inputs:**
- stator_rotor_lamination_set: 36 kg (electrical steel laminations)
- motor_coil_wound: 27 kg (aluminum windings)
- motor_housing_steel: 18 kg (steel housing)
- motor_shaft_steel: 4.5 kg (steel shaft)
- bearing_set_heavy: 4 kg (bearings)
- fastener_kit_medium: 1 kg (fasteners)

**Output:** 1 drive_motor_medium unit (90 kg)
**Time:** 4 hours assembly + 3 hours labor

### New Recipe Created
**File:** `kb/recipes/recipe_drive_motor_medium_v1.yaml`

Three-step production:
1. Lamination stamping: 2 hr
2. Coil winding: 13 hr
3. Final assembly: 4 hr

**Total direct production time:** ~19 hours

---

## Complete Bill of Materials (Upstream)

### What We Already Have (from previous session)
✓ bearing_set_heavy: 4 kg
✓ fastener_kit_medium: 1 kg

### What We Need to Produce

#### 1. Electrical Steel Laminations (36 kg output)
**Process:** lamination_stamping_v0
- **Input:** electrical_steel_sheet: 38 kg
- **Output:** stator_rotor_lamination_set: 36 kg
- **Scrap:** metal_scrap: 2 kg
- **Time:** ~2 hr

**Upstream for electrical steel sheet (38 kg):**
- Requires silicon addition to iron for electrical properties
- Base: iron (35-36 kg) + silicon (2-3 kg)
- From: FFC reduction of regolith

#### 2. Aluminum Coil Windings (27 kg output)
**Process:** coil_winding_basic_v0
- **Input:**
  - aluminum_wire: 28.4 kg
  - coil_insulation_material: 1.4 kg (IMPORT)
- **Output:** motor_coil_wound: 27 kg
- **Scrap:** wire_scrap: 2.8 kg
- **Time:** ~13 hr

**Upstream for aluminum wire (28.4 kg):**
- From: aluminum production (Hall-Héroult process)
- Raw material: ~30 kg aluminum from highland regolith

#### 3. Steel Motor Housing (18 kg output)
**Process:** motor_housing_forming_v0
- **Input:** iron_metal_pure: 19.2 kg
- **Output:** motor_housing_steel: 18 kg
- **Scrap:** metal_scrap: 1.2 kg
- **Time:** ~3 hr

**Upstream:**
- From: FFC reduction of mare regolith
- Raw material: ~190 kg mare regolith → 19 kg iron

#### 4. Steel Motor Shaft (4.5 kg output)
**Process:** Uses recipe_motor_shaft_steel_v0 (forging → machining → grinding)
- **Input:** steel_stock: ~5 kg
- **Output:** motor_shaft_steel: 4.5 kg
- **Time:** ~4 hr

**Upstream:**
- From: iron refining and rolling
- Raw material: ~50 kg mare regolith → 5 kg iron → steel

---

## Total Resource Requirements

### From Regolith (ISRU Materials)

**Iron Requirements (total ~60 kg):**
- Electrical steel: 35-36 kg
- Motor housing: 19 kg
- Motor shaft: 5 kg
- **Total regolith needed:** ~600 kg mare regolith

**Aluminum Requirements (total ~30 kg):**
- Coil windings: 28.4 kg
- Wire drawing loss: ~1.6 kg
- **Total regolith needed:** ~300 kg highland regolith

**Silicon Requirements (~3 kg):**
- For electrical steel alloying
- From silica reduction

### Imports Required
- **Coil insulation:** 1.4 kg (varnish, paper, or polymer film)

### Component Status
✓ **Already produced:**
- bearing_set_heavy: 4 kg
- fastener_kit_medium: 1 kg

---

## Production Sequence

### Phase 1: Raw Material Extraction (35-40 hours)
1. **Mine regolith:** 900 kg total (600 mare + 300 highland)
   - Time: ~10-15 hours
2. **FFC reduction for iron:** 600 kg mare → 60 kg iron
   - Time: ~20 hours
3. **Hall-Héroult for aluminum:** 300 kg highland → 30 kg aluminum
   - Time: ~15 hours
4. **Silicon production:** Extract 3 kg silicon
   - Time: ~5 hours

### Phase 2: Material Processing (15-20 hours)
5. **Electrical steel production:** 35 kg iron + 3 kg silicon → 38 kg electrical steel
   - Time: ~8 hours
6. **Aluminum wire drawing:** 30 kg aluminum → 28.4 kg wire
   - Time: ~5 hours
7. **Steel housing forming:** 19 kg iron → 18 kg housing
   - Time: ~3 hours
8. **Steel shaft production:** 5 kg iron → 4.5 kg shaft
   - Time: ~4 hours

### Phase 3: Motor Component Fabrication (19 hours)
9. **Stamp laminations:** 38 kg electrical steel → 36 kg lamination set
   - Time: ~2 hours
10. **Wind coils:** 28.4 kg wire + 1.4 kg insulation → 27 kg coils
    - Time: ~13 hours
11. **Final assembly:** Combine all components → 1 drive motor
    - Time: ~4 hours

**Total Production Time:** 69-79 hours

---

## Comparison to Small Motor

| Parameter | motor_electric_small | drive_motor_medium | Scale Factor |
|-----------|---------------------|-------------------|--------------|
| **Mass** | 12 kg | 90 kg | 7.5x |
| **Laminations** | 5 kg | 36 kg | 7.2x |
| **Windings** | 2 kg | 27 kg | 13.5x |
| **Housing** | 3 kg | 18 kg | 6x |
| **Shaft** | 1 kg | 4.5 kg | 4.5x |
| **Bearings** | 0.5 kg | 4 kg | 8x |
| **Power (est.)** | 0.5-2 kW | 5-15 kW | 7.5x |
| **Production time** | ~4 hr | ~19 hr | 4.75x |

**Note:** Windings scale more than proportionally due to longer wire paths in larger motors.

---

## Risk Assessment

### High Confidence (Proven)
✓ Bearing production (successfully made bearing_set_heavy)
✓ Fastener production (successfully made fastener_kit_medium)
✓ Small motor production (successfully made motor_electric_small)
✓ FFC iron extraction (demonstrated)
✓ Aluminum production (demonstrated)

### Medium Confidence (Scaled Processes)
⚠ Electrical steel production (know the process, need to scale)
⚠ Large housing forming (larger press brake operations)
⚠ Heavy shaft machining (need large lathe capacity)

### Low Confidence (New/Complex)
⚠ Silicon extraction at scale (3 kg needed)
⚠ Aluminum wire drawing at scale (28 kg needed)
⚠ Large coil winding (27 kg is 13.5x scale-up)

### Import Dependencies
⚠ Coil insulation (1.4 kg) - could potentially substitute with:
  - Ceramic coating (from regolith)
  - Silicone rubber (from silicon + carbon)
  - Paper from plant fiber (if available)
  - For now: IMPORT

---

## Next Steps

### Immediate (Already Complete)
✓ Created drive_motor_medium_assembly_v0 process
✓ Created recipe_drive_motor_medium_v1 recipe
✓ Updated drive_motor_medium item definition

### To Build the Motor
1. **Verify current inventory:**
   - Bearing set: 4 kg ✓
   - Fastener kit: 1 kg ✓
   - Iron available: ? kg
   - Aluminum available: ? kg

2. **Decide on production approach:**
   - Option A: Full ISRU (mine regolith, extract all materials)
   - Option B: Import some intermediates (electrical steel sheet, aluminum wire)
   - Option C: Hybrid (import hard parts like coil insulation, produce rest)

3. **Production execution:**
   - Follow phase 1-3 sequence above
   - Track material flows
   - Monitor for process bottlenecks

---

## Value Proposition

**Why build drive_motor_medium next:**

1. **Highest ISRU potential remaining:** 96% (vs 60% for control panels, 40% for sensors)
2. **Proven process:** Successfully scaled from motor_electric_small
3. **High BOM coverage:** Unlocks 25 BOMs for automated machinery
4. **Enables automation:** Critical for scaling production capacity
5. **Builds on existing inventory:** Already have bearings and fasteners
6. **Material availability:** All processes use demonstrated ISRU materials

**Challenges:**
- Large regolith processing requirement (~900 kg)
- Long total production time (~75 hours)
- Scale-up risks for some processes
- Still requires imported coil insulation

**Alternative:** If resources are limited, consider making multiple smaller motors (motor_electric_small at 12 kg each) to build up automation capacity incrementally.

---

## Production Using CLI Commands

**Recommended approach for building in simulation:**

```bash
SIM="drive_motor_build"

# 1. View initial state
python -m base_builder.cli_commands view-state --sim-id $SIM

# 2. Import bootstrap equipment
python -m base_builder.cli_commands import --sim-id $SIM --item labor_bot_general_v0 --quantity 2 --unit unit
python -m base_builder.cli_commands import --sim-id $SIM --item stamping_press_basic --quantity 1 --unit unit
python -m base_builder.cli_commands import --sim-id $SIM --item coil_winding_machine --quantity 1 --unit unit
python -m base_builder.cli_commands import --sim-id $SIM --item press_brake_v0 --quantity 1 --unit unit

# 3. Import materials (TODO: replace with ISRU mining/processing)
python -m base_builder.cli_commands import --sim-id $SIM --item electrical_steel_sheet --quantity 40 --unit kg
python -m base_builder.cli_commands import --sim-id $SIM --item aluminum_wire --quantity 28.4 --unit kg
python -m base_builder.cli_commands import --sim-id $SIM --item iron_metal_pure --quantity 25 --unit kg
python -m base_builder.cli_commands import --sim-id $SIM --item coil_insulation_material --quantity 1.4 --unit kg

# 4. Import previously-built components (or build them first)
python -m base_builder.cli_commands import --sim-id $SIM --item bearing_set_heavy --quantity 4 --unit kg
python -m base_builder.cli_commands import --sim-id $SIM --item fastener_kit_medium --quantity 1 --unit kg

# 5. Build motor using recipe
python -m base_builder.cli_commands run-recipe --sim-id $SIM --recipe recipe_drive_motor_medium_v1 --quantity 1

# 6. Preview time advancement
python -m base_builder.cli_commands preview --sim-id $SIM --hours 19

# 7. Advance time to complete production
python -m base_builder.cli_commands advance-time --sim-id $SIM --hours 19

# 8. Verify motor was built
python -m base_builder.cli_commands view-state --sim-id $SIM | grep drive_motor
```

**See complete CLI guide:** `docs/CLI_COMMANDS_GUIDE.md`

---

## Files Created/Modified

### New Files
- `kb/processes/drive_motor_medium_assembly_v0.yaml` - Main assembly process
- `kb/recipes/recipe_drive_motor_medium_v1.yaml` - Improved production recipe
- `design/memos/drive_motor_medium_production_plan.md` - This document

### Modified Files
- `kb/items/parts/drive_motor_medium.yaml` - Updated to use v1 recipe, added detailed notes

### References
- Based on feasibility analysis: `design/memos/isru_component_feasibility.md`
- Uses proven process: `kb/processes/motor_final_assembly_v0.yaml`
- Component definitions: `kb/boms/bom_drive_motor_medium_v0.yaml`
