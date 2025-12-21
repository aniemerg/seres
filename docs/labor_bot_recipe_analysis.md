# Labor Bot Parts - Recipe Analysis
**Categorization of parts as import vs lunar manufacturing**
**Date**: 2024-12-21

## Purpose

Determine which of the 18 new labor bot parts should:
1. **Remain imports** (Earth-sourced) - complex electronics, magnets, precision optics
2. **Have manufacturing recipes** (lunar ISRU) - structural parts, simple assemblies

Based on lunar resource availability and manufacturing capability constraints from `docs/labor_bot_design_memo.md`.

---

## CATEGORY A: Import Required (11 parts)

These parts require technologies not available from lunar ISRU in early phases.

### A1. Electronics and Controllers (5 parts)

#### servo_drive_controller
**Rationale**: Complex power electronics with microcontroller
- Field-oriented control (FOC) requires DSP or microcontroller
- Power MOSFETs/IGBTs for 3-phase motor drive
- High-speed communication (EtherCAT)
**Decision**: **IMPORT**

#### safety_controller_plc
**Rationale**: Safety-critical electronics requiring certification
- Dual-channel redundant processors
- Safety-rated firmware (IEC 61508 SIL 2)
- Cannot substitute with non-certified components
**Decision**: **IMPORT**

#### power_distribution_board
**Rationale**: PCB fabrication with circuit breakers
- Thermal circuit breakers are complex electromechanical
- PCB manufacturing requires photolithography (available?)
- Could manufacture later, but import initially
**Decision**: **IMPORT** (initially)

#### emergency_stop_system
**Rationale**: Safety-critical dual-channel relay
- Safety relay requires certified components
- E-stop buttons have specific mechanical latching
- Wiring harness could be manufactured, but safety relay import
**Decision**: **IMPORT**

#### safety_light_curtain
**Rationale**: Precision optoelectronics
- Infrared LED arrays (850nm wavelength)
- Matched photodiode receivers
- Signal processing electronics for beam detection
- Safety-rated output relay (SIL 2)
**Decision**: **IMPORT**

### A2. Precision Sensors (3 parts)

#### force_torque_sensor_6axis
**Rationale**: Strain gauges require precise resistance control
- Aluminum flexure is manufacturable from lunar Al
- Strain gauges require 120Ω or 350Ω precision resistors
- Adhesive bonding and temperature compensation complex
- Signal conditioning electronics
**Decision**: **IMPORT** (initially; flexure could be manufactured later)

#### touch_sensor_capacitive
**Rationale**: Capacitive sensing IC required
- Sensing electrode (copper/aluminum) manufacturable
- Capacitance-to-digital converter IC is specialized
**Decision**: **IMPORT**

#### proximity_sensor_inductive
**Rationale**: Sensing electronics import
- LC oscillator coil winding potentially manufacturable
- But oscillator IC and output driver import
- Housing manufacturable
**Decision**: **IMPORT** (initially)

### A3. Precision Mechanisms (2 parts)

#### harmonic_drive_reducer_medium
**Rationale**: Extreme precision required for repeatability
- Tooth accuracy requires advanced CNC and metrology
- Heat treatment needs controlled atmosphere furnace
- Flexspline material needs high fatigue resistance
- **Could manufacture later** with precision grinding capability
**Decision**: **IMPORT** (initially; manufacture in Phase 2)

#### quick_change_tool_interface
**Rationale**: Precision mating surfaces and pneumatic valve
- Mechanical coupling requires ±0.05mm precision
- Pneumatic valve with seals complex
- Electrical connector (8-pin auto-mating) import
- **Mechanical parts manufacturable**, but valve/connector import
**Decision**: **IMPORT** (initially; partial manufacture later)

### A4. Specialized Components (1 part)

#### battery_backup_small
**Rationale**: Lithium-ion cells
- Requires lithium (scarce on Moon)
- Cell chemistry and safety management complex
- **Unless lunar lithium extraction developed**
**Decision**: **IMPORT**

---

## CATEGORY B: Lunar Manufacturing (7 parts)

These parts can be manufactured from available lunar materials.

### B1. Structural Parts (3 parts)

#### robot_arm_link_aluminum
**Rationale**: Aluminum casting or welding
- Material: Aluminum from anorthite (abundant in highlands)
- Process: Casting or welding box beams
- Machining: CNC mill for mounting surfaces
- No precision beyond ±0.5mm required
**Manufacturing recipe needed**: Casting + machining

#### robot_wrist_3axis
**Rationale**: Aluminum housings + steel shafts
- Aluminum castings from lunar Al
- Steel shafts from iron (mare regolith)
- CNC machining for bearing bores
- Assembly with bearings (bearings might be import?)
**Manufacturing recipe needed**: Casting + machining + assembly
**Note**: Bearings themselves might be import (precision balls)

#### machine_frame_small
**Existing part with recipe**: Already in KB
**Verify**: Check if recipe exists

### B2. Optical/Illumination (1 part)

#### led_ring_light
**Rationale**: LEDs import, but housing and diffuser manufacturable
- High-brightness white LEDs: **IMPORT**
- Aluminum heatsink ring: Lunar Al
- LED driver electronics: **IMPORT**
- Acrylic diffuser: Polymer synthesis or lunar glass
**Decision**: **IMPORT** (LED assembly) - electronics dominant
**Alternative**: Could create assembly recipe if LED chips available

### B3. Thermal and Covers (3 parts)

#### thermal_management_system
**Rationale**: Copper and aluminum from lunar resources
- Copper heat pipes: Lunar copper (trace in regolith)
- Aluminum radiator fins: Lunar Al
- Heat pipe fabrication: Requires vacuum sealing + fluid charging
- **Challenging but possible**
**Manufacturing recipe needed**: Heat pipe fabrication + radiator assembly

#### cable_drag_chain
**Rationale**: Polymer or metal links
- Polymer chain: Requires polymer synthesis (H + C)
  - Hydrogen from water (lunar ice or imported)
  - Carbon from CO2 reduction or imported
- Alternative: Metal links (steel or aluminum) instead of polymer
- Hinge pins: Steel
**Decision**: **IMPORT polymer version** OR **manufacture metal version**
**Recommendation**: Import initially (nylon), manufacture metal version later

#### protective_cover_set
**Rationale**: Sheet metal or polycarbonate
- Aluminum sheet covers: Lunar Al, sheet rolling
- Polycarbonate: Polymer synthesis or import
- Fasteners (screws): Steel from lunar iron
**Manufacturing recipe needed**: Sheet metal forming
**Note**: Polycarbonate likely import, aluminum covers manufacturable

### B4. End Effector (1 part)

#### electric_parallel_gripper
**Rationale**: Aluminum body manufacturable, motor import
- Aluminum body housing: Lunar Al machining
- Ball screw mechanism: Precision machining (possible)
- Linear bearings: Might be import (precision balls)
- Stepper motor (NEMA 23): **IMPORT** (needs magnets)
- Jaw inserts: Aluminum or rubber (aluminum manufacturable)
**Decision**: **PARTIAL** - Create assembly recipe
**Components**:
  - Gripper body and mechanism: MANUFACTURE
  - Stepper motor: IMPORT (use existing stepper_motor_precision)
  - Bearings: IMPORT or manufacture

---

## Summary Table

| Part | Category | Decision | Justification |
|------|----------|----------|---------------|
| servo_drive_controller | Electronics | **IMPORT** | Power electronics, microcontroller |
| safety_controller_plc | Electronics | **IMPORT** | Safety-certified components |
| power_distribution_board | Electronics | **IMPORT** | Circuit breakers, PCB |
| emergency_stop_system | Safety | **IMPORT** | Safety relay, certified E-stop |
| safety_light_curtain | Optoelectronics | **IMPORT** | IR LEDs, photodiodes, safety relay |
| force_torque_sensor_6axis | Sensor | **IMPORT** | Strain gauges, conditioning electronics |
| touch_sensor_capacitive | Sensor | **IMPORT** | Capacitive sensing IC |
| proximity_sensor_inductive | Sensor | **IMPORT** | Oscillator IC, output driver |
| harmonic_drive_reducer_medium | Precision mech | **IMPORT** | Precision teeth, heat treatment |
| quick_change_tool_interface | Precision mech | **IMPORT** | Pneumatic valve, connector |
| battery_backup_small | Energy storage | **IMPORT** | Li-ion cells, lithium scarce |
| robot_arm_link_aluminum | Structure | **MANUFACTURE** | Al casting/welding + machining |
| robot_wrist_3axis | Structure | **MANUFACTURE** | Al casting + steel shafts |
| led_ring_light | Illumination | **IMPORT** | LED chips dominant component |
| thermal_management_system | Thermal | **MANUFACTURE** | Cu heat pipes + Al radiator |
| cable_drag_chain | Cable mgmt | **IMPORT** | Polymer synthesis challenging |
| protective_cover_set | Covers | **MANUFACTURE** | Sheet metal forming |
| electric_parallel_gripper | End effector | **ASSEMBLY** | Body: manufacture, Motor: import |

**Totals**:
- **Import**: 14 parts (primarily electronics, sensors, precision)
- **Manufacture**: 4 parts (structural, thermal, covers, gripper body)

---

## Action Items

### 1. Create Import Recipes (14 parts)

Simple import stub recipes for:
- servo_drive_controller
- safety_controller_plc
- power_distribution_board
- emergency_stop_system
- safety_light_curtain
- force_torque_sensor_6axis
- touch_sensor_capacitive
- proximity_sensor_inductive
- harmonic_drive_reducer_medium
- quick_change_tool_interface
- battery_backup_small
- led_ring_light
- cable_drag_chain

### 2. Create Manufacturing Recipes (4 parts)

Detailed recipes with processes and materials for:
- **robot_arm_link_aluminum**: Casting + machining
- **robot_wrist_3axis**: Casting + machining + assembly
- **thermal_management_system**: Heat pipe fabrication + radiator assembly
- **protective_cover_set**: Sheet metal forming + fasteners

### 3. Create Assembly Recipe (1 part)

Assembly recipe combining manufactured body with imported motor:
- **electric_parallel_gripper**: Gripper body + stepper motor + bearings

### 4. Verify Existing Parts

Check that reused parts have recipes:
- machine_frame_small
- motor_electric_small
- motor_electric_medium
- power_supply_small_imported
- computer_core_imported
- sensor_suite_general
- stepper_motor_precision
- assembled_cable_harness
- electrical_wire_and_connectors
- instrument_mounts_basic

---

## Notes

**Import percentage**: 14 of 18 new parts = 78% imports

This aligns with design memo analysis:
- 25% of robot mass is critical electronics/magnets requiring import
- 29% is motors/gearboxes (partial import: magnets + precision components)
- 46% is structures/cables/thermal (lunar manufacturability)

**Phase 2 opportunities**:
- Harmonic drives: Manufacture with advanced precision grinding
- Sensors: Manufacture with strain gauge and IC fabrication capability
- Polymer components: Manufacture with polymer synthesis from H2 + CO2
