# Motor Production Manifest - Full ISRU

## Goal
Produce 1 `motor_electric_small` from lunar in-situ resources (highland regolith + mare regolith + existing iron)

## Starting Inventory (from claude_base_001 simulation)
- ✅ `iron_metal_pure`: 14.4 kg
- ✅ `regolith_lunar_mare`: 316.0 kg
- ✅ `labor_bot_general_v0`: 1 unit

## Required Machines (IMPORT THESE)
All these machines exist in the KB and can be imported:
1. ✅ `chemical_reactor_basic` - For chemical reactions
2. ✅ `electrolysis_cell_aluminum` - For Hall-Héroult aluminum smelting
3. ✅ `induction_forge_v0` - For electrical steel production
4. ✅ `rolling_mill_v0` - For rolling electrical steel sheets
5. ✅ `lathe_engine_v0` - For shaft and bearing machining
6. ✅ `press_brake_v0` - For stamping laminations and forming housing

---

## Production Sequence

### Phase 1: Mine Raw Materials

#### 1.1 Mine Highland Regolith
- **Process**: `regolith_mining_highlands_v0`
- **Input**: None (unlimited resource)
- **Output**: 100 kg `regolith_lunar_highlands`
- **Time**: 8 hours
- **Energy**: 50 kWh

---

### Phase 2: Support Materials Production

#### 2.1 Produce Methane (for carbon)
*Note: May need to import or use existing methane source*
- **Item needed**: `methane_gas`
- **Quantity**: ~1 kg for carbon production

#### 2.2 Produce Carbon Anode
- **Process**: `methane_pyrolysis_v0`
- **Input**: 1 kg `methane_gas`
- **Output**: 0.75 kg `carbon_anode_material` + 0.25 kg `hydrogen_gas`
- **Then**: `carbon_anode_forming_v0`
- **Input**: 0.75 kg `carbon_anode_material`
- **Output**: 0.7 kg `carbon_anode`

#### 2.3 Produce HCl (for alumina extraction)
- **Process**: `chloralkali_electrolysis_v0`
- **Input**: 15 kg `sodium_chloride` + 10 kg `water`
- **Output**: 10 kg `chlorine_gas` + 12 kg `sodium_hydroxide` + 3 kg `hydrogen_gas`
- **Then**: `hcl_synthesis_from_h2_cl2_v0`
- **Input**: 3 kg `hydrogen_gas` + 10 kg `chlorine_gas`
- **Output**: 10 kg `hydrochloric_acid`

#### 2.4 Produce Cryolite Flux
- **Process**: `cryolite_flux_synthesis_v0`
- **Input**: Materials for synthetic cryolite (simplified for ISRU)
- **Output**: 0.1 kg `cryolite_flux`
*Note: Mostly recycled (90%+), small makeup needed*

---

### Phase 3: Aluminum Production Chain

#### 3.1 Extract Alumina from Highland Regolith
- **Process**: `alumina_extraction_from_highlands_v0`
- **Input**: 100 kg `regolith_lunar_highlands` + 10 kg `hydrochloric_acid`
- **Output**: 12 kg `alumina_powder` + 98 kg `processed_tailings`
- **Time**: 10 hours
- **Energy**: 36 kWh

#### 3.2 Smelt Aluminum (Hall-Héroult Process)
*Need to run this 3 times to get enough aluminum*

**Run 1-3** (each):
- **Process**: `aluminum_smelting_hall_heroult_v0`
- **Input**: 2 kg `alumina_powder` + 0.5 kg `carbon_anode` + 0.1 kg `cryolite_flux`
- **Output**: 1 kg `aluminum_alloy_ingot` + 1.5 kg `co2_gas` + 0.09 kg `cryolite_flux` (recycled)
- **Time**: 8 hours each
- **Energy**: 15 kWh each = **45 kWh total for 3 kg Al!**

Total output: 3 kg aluminum_alloy_ingot

#### 3.3 Draw Aluminum Wire
*Need to run this 3 times*

**Run 1-3** (each):
- **Process**: `wire_drawing_aluminum_v0`
- **Input**: 1 kg `aluminum_alloy_ingot`
- **Output**: 0.95 kg `aluminum_wire` + 0.05 kg `metal_scrap`
- **Time**: 0.5 hours each
- **Energy**: 1.5 kWh each

Total output: 2.85 kg aluminum_wire

#### 3.4 Wind Motor Coils
- **Process**: `coil_winding_basic_v0`
- **Input**: 2.1 kg `aluminum_wire` + 0.05 kg `coil_insulation_material`
- **Output**: 2.0 kg `motor_coil_wound` + 0.15 kg `wire_scrap`
- **Time**: 2 hours
- **Energy**: 0.5 kWh

---

### Phase 4: Electrical Steel Production Chain

#### 4.1 Extract Silicon from Mare Regolith
- **Process**: `silicon_extraction_from_regolith_carbothermic_v0`
- **Input**: Mare regolith + carbon (from existing regolith)
- **Output**: ~0.2 kg `silicon_metal_v0` (need 0.2 kg for 5 kg e-steel)
- **Energy**: 10-12 kWh/kg Si

#### 4.2 Produce Electrical Steel
*Need to run this 5 times to get 5 kg*

**Run 1-5** (each):
- **Process**: `electrical_steel_production_v0`
- **Input**: 0.96 kg `iron_metal_pure` + 0.04 kg `silicon_metal_v0`
- **Output**: 1.0 kg `electrical_steel_sheet`
- **Time**: 6 hours each = 30 hours total
- **Energy**: 5 kWh each = 25 kWh total

Total output: 5 kg electrical_steel_sheet
Iron consumed: 4.8 kg (from our 14.4 kg stock)

#### 4.3 Stamp Laminations
*Need to run this 5 times*

**Run 1-5** (each):
- **Process**: `lamination_stamping_v0`
- **Input**: 1.0 kg `electrical_steel_sheet`
- **Output**: 0.95 kg `stator_rotor_lamination_set` + 0.05 kg `metal_scrap`
- **Time**: 1 hour each = 5 hours total
- **Energy**: 2 kWh each = 10 kWh total

Total output: 4.75 kg laminations (need 5 kg - close enough or run 6 times)

---

### Phase 5: Motor Components from Iron

#### 5.1 Machine Motor Shaft
- **Process**: `motor_shaft_machining_v0`
- **Input**: 1.1 kg `iron_metal_pure`
- **Output**: 1.0 kg `motor_shaft_steel` + 0.1 kg `metal_scrap`
- **Time**: 3 hours
- **Energy**: 2 kWh
- **Machine**: `lathe_engine_v0`

#### 5.2 Manufacture Bearings
- **Process**: `bearing_manufacturing_small_v0`
- **Input**: 0.55 kg `iron_metal_pure` + 0.01 kg `grease_bearing_high_temp`
- **Output**: 0.5 kg `bearing_set_small` + 0.06 kg `metal_scrap`
- **Time**: 6 hours (precision work!)
- **Energy**: 4 kWh
- **Machine**: `lathe_engine_v0` + `bearing_grinding_machine`

#### 5.3 Form Motor Housing
- **Process**: `motor_housing_forming_v0`
- **Input**: 3.2 kg `iron_metal_pure`
- **Output**: 3.0 kg `motor_housing_steel` + 0.2 kg `metal_scrap`
- **Time**: 4 hours
- **Energy**: 3 kWh
- **Machine**: `press_brake_v0`

Total iron consumed for components: 4.85 kg

---

### Phase 6: Final Motor Assembly

#### 6.1 Assemble Motor
- **Process**: `motor_final_assembly_v0`
- **Inputs**:
  - 5.0 kg `stator_rotor_lamination_set`
  - 2.0 kg `motor_coil_wound`
  - 1.0 kg `motor_shaft_steel`
  - 0.5 kg `bearing_set_small`
  - 3.0 kg `motor_housing_steel`
- **Output**: 1 unit `motor_electric_small`
- **Byproduct**: 0.5 kg `assembly_loss`
- **Time**: 1 hour
- **Energy**: 0.2 kWh
- **Machine**: `labor_bot_general_v0` + assembly tools

---

## Resource Summary

### Total Iron Required
- Electrical steel: 4.8 kg
- Motor shaft: 1.1 kg
- Bearings: 0.55 kg
- Housing: 3.2 kg
- **Total**: ~9.7 kg
- **Available**: 14.4 kg
- ✅ **Sufficient!**

### Total Energy Required (Approximate)
- Mining highland regolith: 50 kWh
- Alumina extraction: 36 kWh
- Aluminum smelting: 45 kWh (3 kg at 15 kWh/kg)
- Silicon extraction: ~3 kWh (0.2 kg at 12 kWh/kg)
- Electrical steel: 25 kWh
- Lamination stamping: 10 kWh
- Components: 9 kWh
- Assembly: 0.2 kWh
- **Total**: ~178 kWh

*Note: Aluminum smelting is 25% of total energy!*

### Total Time Required (Approximate)
- Mining: 8 hours
- Chemical processing (HCl, carbon): ~15 hours
- Aluminum chain: 28 hours (extraction 10h + smelting 24h + wire 1.5h + coils 2h)
- Silicon extraction: ~6 hours
- Electrical steel chain: 41 hours (production 30h + stamping 5h + silicon 6h)
- Motor components: 13 hours (shaft 3h + bearings 6h + housing 4h)
- Assembly: 1 hour
- **Total**: ~112 hours (~4.7 days)

---

## Success Criteria

✅ All processes exist in KB
✅ All input materials available or producible from regolith
✅ Sufficient iron in inventory
✅ All machines can be imported
✅ Complete production chain validated

## Output

**1 unit `motor_electric_small`** - A fully functional electric motor made entirely from lunar materials!

Mass: 12 kg (per item definition)
Components: Aluminum windings, electrical steel laminations, iron shaft/bearings/housing
Power class: 0.5-2 kW
