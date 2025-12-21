# ISRU Component Feasibility Analysis

## Top 7 Most Common Components - ISRU Assessment

### ✓ 1. fastener_kit_medium (107 BOMs) - COMPLETED
**ISRU Potential: 100%**
- Status: ✓ Successfully produced (1.0 kg)
- Materials: Steel from regolith
- All components achievable with basic metalworking

### ✓ 6. bearing_set_heavy (41 BOMs) - COMPLETED
**ISRU Potential: 100%**
- Status: ✓ Successfully produced (4.0 kg)
- Materials: Hardened steel from regolith
- Requires: Machining, heat treatment, precision grinding

---

## Remaining High-Value Components:

### 2. control_panel_basic (51 BOMs)
**ISRU Potential: 60% - MEDIUM**

**Can Make with ISRU:**
- ✓ **Enclosure** (steel/aluminum sheet metal) - 40% of mass
- ✓ **Mounting plate** (sheet metal)
- ✓ **Toggle switches** (mechanical contacts, springs) - 20% of mass
- ✓ **Push buttons** (springs, contacts)
- ✓ **Mechanical indicators** (flags, dials)
- ✓ **Terminal blocks** (metal contacts)
- ✓ **Wiring** (aluminum wire, insulation harder)

**Cannot Make (Need Imports):**
- ✗ LEDs (semiconductors)
- ✗ Complex displays (electronics)
- ✗ Sensitive electronic switches
- ⚠ Wire insulation (limited options)

**Recommendation:** BUILD IT
- Make basic mechanical control panel
- Import only LEDs/displays as needed
- Functional with mechanical switches and indicators
- ~60% ISRU by mass, fully functional for many applications

**Estimated Requirements:**
- Sheet metal: 5-10 kg (steel/aluminum)
- Wire: 1-2 kg (aluminum)
- Small hardware: 0.5 kg (fasteners, springs, contacts)
- Imports: 1-2 kg (LEDs, wire insulation, labels)

---

### 7. drive_motor_medium (25 BOMs)
**ISRU Potential: 95%+ - VERY HIGH**

**Can Make with ISRU:**
- ✓ **Electrical steel laminations** (we've made this!) - 40% of mass
- ✓ **Copper/aluminum windings** (we've made aluminum wire) - 30% of mass
- ✓ **Steel housing** (sheet metal forming) - 20% of mass
- ✓ **Steel shaft** (machining) - 5% of mass
- ✓ **Bearings** (we just made them!) - 4% of mass

**Cannot Make (Need Imports):**
- ⚠ **Coil insulation** (minimal - 1% of mass)
- ⚠ **Terminal block insulators** (minimal)

**Recommendation:** BUILD IT - HIGHEST PRIORITY
- We've already proven the process with motor_electric_small (12 kg)
- drive_motor_medium is 90 kg (7.5x scale-up)
- Same processes, just more material
- Unlocks 25 BOMs for automated machinery

**Estimated Requirements:**
- Electrical steel: 35-40 kg
- Aluminum wire: 25-30 kg (or copper if available)
- Steel housing/shaft: 20-25 kg
- Bearings: 4-8 kg
- Coil insulation: 1-2 kg (import)
- Total ISRU: ~85 kg, Import: ~2 kg

**Production Time:** ~15-20 hours
**Materials Available:**
- Iron: 3.14 kg (need more regolith processing)
- Aluminum: 2.5 kg (need more highland regolith)

---

### 4. sensor_suite_general (43 BOMs)
**ISRU Potential: 40% - MEDIUM-LOW**

**Can Make with ISRU:**
- ✓ **Thermocouples** (metal junctions: iron-constantan, chromel-alumel)
- ✓ **RTD sensors** (resistance temp detectors: platinum/copper wire)
- ✓ **Pressure sensors (mechanical)** (bourdon tubes, diaphragms)
- ✓ **Strain gauges** (metal foil on substrate)
- ✓ **Mechanical limit switches** (contacts, springs)
- ✓ **Potentiometers (simple)** (resistive wire, wiper)

**Cannot Make (Need Imports):**
- ✗ Proximity sensors (need coils + electronics)
- ✗ Optical sensors (need photodiodes, LEDs)
- ✗ Capacitive sensors (need electronics)
- ✗ Amplifier circuits (semiconductors)
- ✗ Signal conditioning (semiconductors)

**Recommendation:** PARTIAL BUILD
- Make mechanical sensors (thermocouples, RTDs, pressure)
- These are actually very useful and reliable
- Import electronic sensors as needed
- ~40% ISRU achievable for functional sensor suite

**Estimated Requirements:**
- Steel/metal stock: 2-3 kg (sensor bodies, diaphragms)
- Fine wire: 0.5-1 kg (thermocouples, RTDs)
- Imports: 1-2 kg (electronics, connectors)

---

### 3. control_compute_module_imported (47 BOMs)
**ISRU Potential: 10% - VERY LOW**

**Cannot Make (Core Function):**
- ✗ CPU/Microcontroller (semiconductor fab required)
- ✗ Memory (semiconductors)
- ✗ I/O interfaces (semiconductors)
- ✗ Oscillators (quartz + electronics)

**Can Make with ISRU:**
- ✓ Enclosure (minimal mass)
- ✓ Heatsink (aluminum/copper)
- ⚠ Power regulation (transformer yes, regulators no)

**Recommendation:** KEEP IMPORTING
- Core functionality requires semiconductor fabrication
- Not achievable with current ISRU capability
- Maybe 10% by mass (enclosure, heatsink) but non-functional

---

### 5. power_conditioning_module (43 BOMs)
**ISRU Potential: 35% - MEDIUM-LOW**

**Can Make with ISRU:**
- ✓ **Transformer** (copper/aluminum windings + iron core) - 60% of power stage
- ✓ **Enclosure** (steel/aluminum)
- ✓ **Mounting hardware**
- ⚠ **Simple capacitors** (plate capacitors, not electrolytic)

**Cannot Make (Need Imports):**
- ✗ Rectifier diodes (semiconductors)
- ✗ Voltage regulators (semiconductors)
- ✗ Electrolytic capacitors
- ✗ Control circuits (semiconductors)

**Recommendation:** PARTIAL BUILD - LOW PRIORITY
- Can make transformer (largest component)
- But need semiconductors for AC/DC conversion and regulation
- Consider for specific applications (isolation transformers, step-down only)
- ~35% ISRU achievable but limited functionality

---

## Priority Ranking for Next Production:

### Tier 1: High ISRU, High Value - DO NOW
1. **drive_motor_medium** (25 BOMs, 95% ISRU)
   - Proven process (scaled up from small motor)
   - High impact (enables automation)
   - Materials available (need more regolith processing)

### Tier 2: Medium ISRU, High Value - DO SOON
2. **control_panel_basic** (51 BOMs, 60% ISRU)
   - Enclosure + mechanical switches achievable
   - High BOM coverage
   - Useful even without fancy displays

3. **sensor_suite_general** (43 BOMs, 40% ISRU)
   - Thermocouples and RTDs very useful
   - Mechanical sensors reliable
   - Good complement to control panels

### Tier 3: Low ISRU - DEFER
4. **power_conditioning_module** (43 BOMs, 35% ISRU)
   - Can make transformers but need semiconductors
   - Limited functionality without power electronics

5. **control_compute_module_imported** (47 BOMs, 10% ISRU)
   - Keep importing until semiconductor fab available

---

## Resource Requirements for Next Target (drive_motor_medium):

### Materials Needed:
- **Iron**: ~90 kg (for electrical steel + housing)
  - Have: 3.14 kg
  - Need from regolith: ~95 kg iron → 950 kg mare regolith

- **Aluminum**: ~30 kg (for windings)
  - Have: 2.5 kg
  - Need from regolith: ~32 kg aluminum → 320 kg highland regolith

- **Silicon**: ~4 kg (for electrical steel alloying)
  - Have: 0.53 kg
  - Need: ~4 kg (from silica reduction)

### Regolith Processing Required:
- Mare regolith: 950 kg (we have 211 kg available)
- Highland regolith: 320 kg (we have 100 kg available)
- **OR mine more regolith first**

### Production Time Estimate:
- Regolith mining: ~10-15 hours
- Iron extraction: ~20 hours
- Aluminum extraction: ~15 hours
- Silicon production: ~5 hours
- Electrical steel production: ~8 hours
- Motor component fabrication: ~10 hours
- Motor assembly: ~3 hours
- **Total: ~70-80 hours**

### Machines Required:
- ✓ FFC reactor (have or can import)
- ✓ Hall-Héroult cell (for aluminum)
- ✓ Furnace (heat treatment)
- ✓ Rolling mill (have)
- ✓ Lathe (have)
- ✓ Coil winding equipment (have or improvise)
- ✓ Assembly tools (have)

---

## Recommendation:

**Next Target: drive_motor_medium**

**Rationale:**
1. **Highest ISRU potential** of remaining components (95%+)
2. **Proven process** - we've made motor_electric_small
3. **High value** - 25 BOMs unlocked
4. **Enables automation** - critical for scaling production
5. **Builds on our strengths** - we have the processes for steel, aluminum, motors, bearings

**Challenges:**
- Need significant regolith processing (~1300 kg total)
- Long production time (~70-80 hours)
- Large material quantities

**Alternative (if resources limited):**
- Make **control_panel_basic** instead (smaller, faster, still useful)
- Or make **multiple bearing sets** to build up inventory
- Or make **multiple fastener kits** (always needed)
