# Common Components Priority List

## Purpose
This document tracks the most frequently used components across the KB to prioritize production planning and identify high-value manufacturing targets.

## Analysis Date
Generated: 2025-01-XX from analysis of 1,871 recipes and 389 BOMs

---

## Top 10 Universal Components (by BOM frequency)

### 1. fastener_kit_medium - 107 BOMs ✓ ISRU CAPABLE
**Status**: Successfully produced from ISRU steel (569.7h)
- **What it is**: Assorted bolts, nuts, washers M6-M12 (1.0 kg kit = ~366 pieces)
- **Why critical**: Nearly every machine needs mechanical fasteners
- **Production chain**: Regolith → Iron → Steel → Rolling → Fasteners
- **Materials needed**: 1.1 kg steel_stock → 1.0 kg kit
- **Time**: 2 hours per kit
- **Machines required**: Forge, lathe, press brake, labor bot

### 2. control_panel_basic - 51 BOMs
**Status**: Not yet attempted
- **What it is**: User interface panel with switches, indicators, displays
- **Components likely needed**:
  - Enclosure (steel/aluminum sheet metal)
  - Switches and buttons (mechanical contacts, springs)
  - Indicator lights (LEDs or incandescent)
  - Wiring and connectors
  - Label plate or display
- **Estimated complexity**: MEDIUM - requires electronics assembly
- **ISRU potential**: Enclosure yes, electronics partial (need semiconductors)

### 3. control_compute_module_imported - 47 BOMs
**Status**: Currently imported (bootstrap component)
- **What it is**: Microcontroller/computer for machine control
- **Components needed**: CPU, memory, I/O interfaces, power regulation
- **Estimated complexity**: HIGH - requires semiconductor fabrication
- **ISRU potential**: LOW in early stages (complex electronics)
- **Notes**: Likely remains import until advanced semiconductor fab available

### 4. sensor_suite_general - 43 BOMs
**Status**: Not yet attempted
- **What it is**: Standard sensor package (temperature, pressure, position, etc.)
- **Components likely needed**:
  - Thermocouples (metal junctions)
  - Pressure sensors (diaphragm + strain gauge)
  - Proximity sensors (inductive/capacitive)
  - Wiring harness
- **Estimated complexity**: MEDIUM - mix of mechanical and electronic sensors
- **ISRU potential**: MEDIUM (thermocouples, pressure sensors achievable; some electronics difficult)

### 5. power_conditioning_module - 43 BOMs
**Status**: Not yet attempted
- **What it is**: Power supply/regulation for machines (AC/DC conversion, voltage regulation)
- **Components likely needed**:
  - Transformer (copper windings, iron core)
  - Rectifier (diodes)
  - Capacitors (electrolytic)
  - Voltage regulator circuit
  - Enclosure and mounting
- **Estimated complexity**: MEDIUM-HIGH - requires electronics fabrication
- **ISRU potential**: MEDIUM (transformer yes, semiconductors difficult)

### 6. bearing_set_heavy - 41 BOMs ⭐ NEXT TARGET
**Status**: Next production candidate
- **What it is**: Ball or roller bearings for heavy rotating machinery
- **Components needed**:
  - Inner race (hardened steel ring)
  - Outer race (hardened steel ring)
  - Rolling elements (steel balls or rollers)
  - Cage/retainer (steel or brass)
  - Grease/lubricant
- **Estimated complexity**: MEDIUM - requires precision machining and heat treatment
- **ISRU potential**: HIGH - all components are metal (steel, some need hardening)
- **Machines required**: Lathe (have), grinding (precision), heat treatment furnace (have)
- **Why promising**: We have steel, heat treatment capability, machining tools

### 7. drive_motor_medium - 25 BOMs
**Status**: Proven capability (made motor_electric_small)
- **What it is**: 90 kg medium electric motor for machine drives
- **Production chain**: Similar to motor_electric_small but larger scale
- **ISRU potential**: HIGH - we've already made a small motor (12 kg)
- **Materials needed**: Electrical steel, copper/aluminum wire, steel housing, bearings
- **Scaling factor**: 7.5x larger than small motor we produced
- **Notes**: Larger motor = more materials but same process

---

## Production Priority Recommendations

### Tier 1: High Value, ISRU Ready (DO NOW)
1. ✓ **fastener_kit_medium** - COMPLETED
2. **bearing_set_heavy** - 41 BOMs, all steel components
3. **fastener_kit_small** - 24 BOMs, same process as medium
4. **fastener_kit_large** - 13 BOMs, same process as medium

### Tier 2: Medium Value, Partial ISRU (DO SOON)
5. **control_panel_basic** - 51 BOMs, enclosure + switches achievable
6. **sensor_suite_general** - 43 BOMs, thermocouples and mechanical sensors achievable
7. **drive_motor_medium** - 25 BOMs, proven process at larger scale

### Tier 3: High Value, Import Dependent (DEFER)
8. **power_conditioning_module** - 43 BOMs, requires semiconductors
9. **control_compute_module_imported** - 47 BOMs, complex electronics

---

## Strategic Impact

### With Fasteners Alone (✓ achieved):
- **107 BOMs unlocked** with fastener_kit_medium
- **Total with all fastener kits**: 144 BOMs (107 + 24 + 13)

### With Fasteners + Bearings:
- **148 unique BOMs unlocked** (107 + 41)
- Enables: Motors, gearboxes, conveyors, rotating machinery, machine tools

### With Fasteners + Bearings + Motors:
- **173 unique BOMs unlocked** (107 + 41 + 25)
- Enables: Automated production lines, material handling, powered equipment

---

## Next Steps

1. **Immediate**: Investigate bearing_set_heavy production requirements
   - Check existing recipes/processes for bearings
   - Identify precision machining requirements
   - Determine heat treatment specifications
   - Estimate material quantities needed

2. **Short term**: Scale up fastener production
   - Make fastener_kit_small (24 BOMs)
   - Make fastener_kit_large (13 BOMs)
   - Build inventory for multiple machines

3. **Medium term**: Control systems
   - Develop control_panel_basic (enclosure + mechanical switches first)
   - Explore simple sensor production (thermocouples, pressure sensors)

4. **Long term**: Electronics manufacturing
   - Research semiconductor fabrication options
   - Consider import substitution timeline for compute modules

---

## Material Requirements Summary

### For 10 High-Value Components:
- **Steel**: ~15-20 kg (fasteners, bearings, motor housings, panels)
- **Copper/Aluminum**: ~5-10 kg (motor windings, electrical connections)
- **Electronics**: Variable (sensors, power modules, compute)

### Current ISRU Capacity:
- ✓ Iron/Steel: 7+ kg available, 200+ kg regolith reserves
- ✓ Aluminum: 2.5 kg available, 100+ kg highland regolith reserves
- ✓ Copper: Limited (can substitute aluminum for many uses)
- ✗ Semiconductors: Not yet available (import required)

### Bottleneck Analysis:
- **Not limited by materials** (abundant regolith)
- **Not limited by basic machinery** (have forge, lathe, press, furnace)
- **Limited by**: Precision grinding, electronics fabrication, time
