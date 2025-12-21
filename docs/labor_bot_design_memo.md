# Labor Bot Design Memo
**Lunar Manufacturing Robot - Technical Specification**
**Date**: 2024-12-21
**Author**: System Design Analysis
**Version**: 1.0

## Executive Summary

This memo establishes the technical requirements and detailed design for the `labor_bot_general_v0` - a general-purpose robotic manipulator for lunar manufacturing operations. The design specifies a 6-DOF industrial robot arm (120 kg total mass) optimized for assembly, material handling, and quality control tasks within a pressurized lunar habitat.

## 1. Mission Requirements

### 1.1 Primary Functions
- **Assembly operations**: Positioning and fastening components during machine construction
- **Material handling**: Moving parts between workstations and storage
- **Quality control**: Visual inspection and dimensional verification
- **Machine operation**: Loading/unloading parts from manufacturing equipment
- **General manipulation**: Versatile tasks requiring dexterity and precision

### 1.2 Operational Environment
- **Location**: Inside pressurized habitat (not EVA-rated)
- **Atmosphere**: Earth-normal (eliminates vacuum-hardening requirements)
- **Temperature**: Controlled 15-25°C (eliminates extreme thermal cycling)
- **Gravity**: Lunar 1.62 m/s² (1/6 Earth)
  - Advantage: Reduced motor torque requirements
  - Advantage: Lower structural loading
  - Consideration: Modified dynamics for motion planning
- **Dust**: Minimal inside habitat, but seals required for regolith handling
- **Power**: 240V 3-phase AC from base electrical grid
- **Radiation**: Shielded by habitat structure (no special hardening needed)

### 1.3 Performance Requirements
- **Reach**: 2.0 m (covers standard 2m x 2m work cell)
- **Payload**: 20 kg at full extension (120 kg in 1/6g feels like 20 kg on Earth)
- **Repeatability**: ±0.5 mm (adequate for mechanical assembly)
- **Speed**: 1.5 m/s maximum velocity (conservative for safety)
- **Degrees of freedom**: 6 (full 3D positioning and orientation)
- **Uptime**: 90% availability (8 hours/day operation, 2 hours maintenance buffer)
- **Service life**: 10,000 operating hours before major overhaul

## 2. Design Architecture

### 2.1 Configuration Selection

**Chosen architecture: 6R serial manipulator** (6 revolute joints in series)

This industrial robot configuration provides:
- Full 6-DOF positioning (3 position + 3 orientation)
- Simple inverse kinematics
- Large workspace volume
- Proven reliability in terrestrial factories
- Modular design allows joint-level repair

**Rejected alternatives:**
- *Humanoid robot*: Unnecessary complexity, poor payload/mass ratio
- *Cartesian gantry*: Large footprint, limited flexibility
- *SCARA robot*: Only 4 DOF, limited vertical reach
- *Delta robot*: High speed but small workspace and low payload

### 2.2 Kinematic Design

**Joint configuration** (from base to end effector):
1. **J1 - Base rotation**: ±180° (azimuth)
2. **J2 - Shoulder pitch**: ±135° (vertical swing)
3. **J3 - Elbow pitch**: ±150° (arm fold)
4. **J4 - Wrist roll**: ±360° continuous
5. **J5 - Wrist pitch**: ±135°
6. **J6 - Flange roll**: ±360° continuous

**Link lengths**:
- Base to shoulder (J1-J2): 0.4 m
- Shoulder to elbow (J2-J3): 1.0 m (upper arm)
- Elbow to wrist (J3-J4): 0.8 m (forearm)
- Wrist to flange (J4-J6): 0.2 m

**Workspace**: Approximately 12 m³ (spherical sector minus base interference)

## 3. Detailed Subsystem Specifications

### 3.1 Mechanical Structure (35 kg)

#### 3.1.1 Base Frame (10 kg)
- **Material**: Cast or welded steel
- **Dimensions**: 0.6m × 0.6m × 0.4m
- **Function**: Mounts robot to floor/table, houses J1 rotation mechanism
- **Features**:
  - Four mounting points (M16 bolts)
  - Cable entry ports
  - Leveling feet
- **Lunar manufacturability**: ✓ Steel casting or welding from lunar iron

#### 3.1.2 Upper Arm Link (8 kg)
- **Material**: Aluminum alloy (high strength-to-weight)
- **Length**: 1.0 m
- **Cross-section**: Box beam 100mm × 150mm, 5mm wall
- **Features**:
  - Houses J2 motor and gearbox at shoulder
  - Internal cable routing channels
  - Mounting bosses for J3 at elbow
- **Lunar manufacturability**: ✓ Aluminum from anorthite, machined or welded

#### 3.1.3 Forearm Link (7 kg)
- **Material**: Aluminum alloy
- **Length**: 0.8 m
- **Cross-section**: Tapered box beam 80mm × 120mm → 60mm × 80mm
- **Features**:
  - Houses J3 motor and gearbox at elbow
  - Internal cable routing
  - Wrist mounting flange
- **Lunar manufacturability**: ✓ Aluminum, machined or welded

#### 3.1.4 Wrist Assembly (5 kg)
- **Material**: Aluminum housing with steel shafts
- **Configuration**: Roll-pitch-roll (J4-J5-J6)
- **Features**:
  - Compact 3-axis module (200mm length)
  - ISO 9409-1-50-4-M6 mounting flange
  - Through-hole for pneumatics/signals (16mm diameter)
- **Lunar manufacturability**: ✓ Aluminum housing, steel shafts

#### 3.1.5 Joint Housings (5 kg total, ~0.8 kg each)
- **Material**: Aluminum castings
- **Function**: Enclose motors and gearboxes, provide bearing supports
- **Features**:
  - Sealed against dust ingress (double lip seals)
  - Mounting for position encoders
  - Thermal interface for heat dissipation
- **Lunar manufacturability**: ✓ Aluminum casting

**Manufacturing processes required:**
- Metal casting (aluminum and steel)
- CNC machining (bearing bores, gear teeth, mounting surfaces)
- Welding (structural joints)
- Surface treatment (anodizing for aluminum, paint for steel)

### 3.2 Actuation System (30 kg)

#### 3.2.1 Brushless DC Motors (18 kg, 6 motors)

**Joint 1 (Base)**: 4 kg, 400W, 3000 rpm
- Torque requirement: 120 Nm (20 kg payload × 2m reach ÷ 6g ÷ gear ratio)
- Peak torque: 200 Nm (acceleration)

**Joint 2 (Shoulder)**: 4 kg, 400W, 3000 rpm
- Torque requirement: 120 Nm
- Peak torque: 200 Nm

**Joint 3 (Elbow)**: 3 kg, 300W, 3000 rpm
- Torque requirement: 60 Nm (shorter moment arm)
- Peak torque: 100 Nm

**Joints 4-6 (Wrist)**: 2.5 kg each, 200W, 4000 rpm
- Torque requirement: 20 Nm each
- Peak torque: 35 Nm

**Motor specifications (all joints)**:
- Type: 3-phase permanent magnet synchronous motor (PMSM)
- Magnets: Neodymium-iron-boron (NdFeB) - *likely import*
- Windings: Copper wire, class H insulation (180°C)
- Stator: Laminated electrical steel
- Rotor: Steel shaft with magnet pockets
- Encoder: Integrated 20-bit absolute encoder per motor
- Cooling: Conductive to housing, radiative dissipation
- Protection: IP54 (dust and splash resistant)

**Lunar manufacturability**:
- ⚠️ **Partial** - Stator laminations and copper wire manufacturable
- ✗ **Magnets**: NdFeB requires rare earths (not abundant on Moon) - *import required*
- ✗ **Encoders**: High-precision optical/magnetic encoders - *import required*

#### 3.2.2 Harmonic Drive Reducers (12 kg, 6 units)

**Function**: High-ratio (100:1) zero-backlash speed reduction

**Configuration**:
- Joints 1-3: 2 kg each, ratio 100:1, 50mm diameter
- Joints 4-6: 2 kg each, ratio 80:1, 40mm diameter

**Components per unit**:
- Wave generator (elliptical cam with bearing)
- Flexspline (thin-walled cup with external teeth)
- Circular spline (rigid ring with internal teeth)

**Materials**:
- Flexspline: High-strength alloy steel (needs fatigue resistance)
- Circular spline: Tool steel
- Wave generator: Bearing steel

**Lunar manufacturability**:
- ⚠️ **Partial** - Steel components manufacturable with precision machining
- ✗ **Heat treatment**: Requires controlled atmosphere furnaces
- ✗ **Precision**: Tooth accuracy requires advanced metrology - *initially import, later manufacture*

### 3.3 Power System (8 kg)

#### 3.3.1 Main Power Supply (5 kg)
- **Input**: 240V 3-phase AC, 50/60 Hz
- **Output**: 48V DC bus for motor controllers
- **Power rating**: 2.5 kW continuous, 4 kW peak (2 sec)
- **Efficiency**: 92%
- **Components**:
  - AC/DC converter module: 3 kg
  - Input filters and contactors: 1 kg
  - Enclosure: 1 kg
- **Lunar manufacturability**: ⚠️ Transformer and power electronics likely import initially

#### 3.3.2 Power Distribution Board (2 kg)
- **Function**: Routes 48V DC to 6 motor controllers
- **Components**:
  - PCB with bus bars (copper)
  - Circuit breakers (6× thermal)
  - Status LEDs
  - Terminal blocks
- **Lunar manufacturability**: ✓ Copper conductors manufacturable, circuit breakers import

#### 3.3.3 Emergency Battery Backup (1 kg)
- **Type**: Lithium-ion battery pack
- **Capacity**: 100 Wh (enough for controlled shutdown + brake holding)
- **Voltage**: 48V nominal
- **Function**: Hold brakes if power lost, prevent arm drop
- **Lunar manufacturability**: ✗ Li-ion cells import (unless lunar lithium extraction developed)

### 3.4 Control System (6 kg)

#### 3.4.1 Main Controller - Industrial PC (3 kg)
- **Processor**: ARM or x86, 4+ cores, 2+ GHz
- **RAM**: 8 GB
- **Storage**: 256 GB SSD
- **I/O interfaces**:
  - EtherCAT real-time bus (motor controllers)
  - Ethernet (network connectivity)
  - USB (programming/diagnostics)
  - GPIO (safety interlocks)
- **Operating system**: Linux with PREEMPT_RT real-time patches
- **Control software**:
  - Inverse kinematics solver
  - Trajectory planner (5th-order polynomial)
  - PID controllers (position and velocity loops)
  - Collision detection
  - ROS (Robot Operating System) compatibility
- **Lunar manufacturability**: ✗ Import required (complex electronics)

#### 3.4.2 Motor Controllers (2 kg, 6× servo drives)
- **Type**: Field-oriented control (FOC) for BLDC motors
- **Communication**: EtherCAT (1 kHz update rate)
- **Features**:
  - Current limiting
  - Regenerative braking
  - Over-temperature protection
  - Position/velocity/torque modes
- **Mass**: ~300g per drive
- **Lunar manufacturability**: ✗ Import required (power electronics, microcontrollers)

#### 3.4.3 Safety Controller (1 kg)
- **Type**: Programmable safety controller (SIL 2 rated)
- **Function**: Independent monitoring of:
  - Emergency stop circuit
  - Light curtain / barrier status
  - Joint position limits
  - Velocity limits
  - Torque limits
- **Action**: Trigger safe torque off (STO) to all motors if fault detected
- **Lunar manufacturability**: ✗ Import required (safety-critical electronics)

### 3.5 Sensing System (12 kg)

#### 3.5.1 Position Encoders (3 kg, integrated in motors)
- **Type**: 20-bit absolute rotary encoders
- **Resolution**: 0.00034° (~1 arc-second)
- **Interface**: EnDat 2.2 or BiSS-C digital protocol
- **Function**: Joint angle measurement for closed-loop control
- **Already counted in motor mass above**

#### 3.5.2 Vision System (2 kg)
- **Configuration**: Stereo cameras (2× 5 MP sensors)
- **Mounting**: On wrist near tool flange
- **Field of view**: 60° horizontal, 45° vertical
- **Frame rate**: 30 fps
- **Processing**: External (on main controller)
- **Function**:
  - Part location and orientation (pose estimation)
  - Quality inspection (visual defects)
  - Obstacle detection
- **Lunar manufacturability**: ✗ Camera sensors import; lenses potentially manufacturable from lunar glass

#### 3.5.3 Force/Torque Sensor (2 kg)
- **Type**: 6-axis (Fx, Fy, Fz, Tx, Ty, Tz)
- **Mounting**: Between wrist flange (J6) and tool adapter
- **Capacity**: ±200 N force, ±20 Nm torque
- **Resolution**: 0.1 N, 0.01 Nm
- **Technology**: Strain gauge bridge on machined aluminum flexure
- **Function**:
  - Contact detection
  - Force-controlled assembly (press fits, compliance)
  - Tool weight compensation
- **Lunar manufacturability**: ⚠️ Aluminum flexure manufacturable; strain gauges likely import

#### 3.5.4 Touch Sensors and Proximity (1 kg)
- **Touch sensors**: Capacitive touch on gripper fingers (2×)
- **Proximity sensors**: Inductive sensors at workspace boundaries (4×)
- **Function**: Collision detection, workspace limiting
- **Lunar manufacturability**: ✗ Sensor elements import

#### 3.5.5 Camera Mounting and Lighting (4 kg)
- **Camera mount**: Aluminum bracket with adjustable tilt
- **LED ring lights**: 2× white LED arrays (12W each) for part illumination
- **Diffusers**: Acrylic or glass
- **Cabling**: Integrated into wrist cable bundle
- **Lunar manufacturability**: ✓ Brackets and diffusers manufacturable; LEDs import

### 3.6 End Effector System (8 kg)

#### 3.6.1 Parallel Jaw Gripper (4 kg)
- **Type**: Electric 2-finger parallel gripper
- **Jaw stroke**: 120 mm (60 mm per finger)
- **Gripping force**: 200 N (adjustable)
- **Fingers**: Interchangeable soft/hard jaws
- **Body**: Aluminum housing
- **Mechanism**: Ball screw driven by stepper motor
- **Sensors**: Jaw position encoder, force sensor
- **Lunar manufacturability**: ✓ Mostly manufacturable; stepper motor requires magnets (import)

#### 3.6.2 Gripper Actuator (2 kg)
- **Type**: NEMA 23 stepper motor with integrated driver
- **Torque**: 2 Nm
- **Ball screw**: 10 mm diameter, 5 mm pitch
- **Travel**: 120 mm
- **Speed**: 100 mm/s
- **Lunar manufacturability**: ⚠️ Stepper motor magnets import; ball screw manufacturable

#### 3.6.3 Quick-Change Tool Interface (2 kg)
- **Type**: Mechanical coupling with electrical pass-through
- **Standard**: ISO 9409-1-50-4-M6 mounting pattern
- **Features**:
  - Pneumatic lock/unlock (or manual)
  - 8-pin electrical connector (power + signals)
  - Automatic coupling on insertion
  - Tool detection sensor
- **Function**: Allows robot to swap between gripper, vacuum cup, screwdriver, etc.
- **Lunar manufacturability**: ✓ Mechanical parts manufacturable; connector import

### 3.7 Wiring and Integration (15 kg)

#### 3.7.1 Motor Power Cables (6 kg)
- **Type**: Shielded 3-phase + encoder (8-conductor)
- **Gauge**: 16 AWG (1.3 mm²) power, 24 AWG signal
- **Length**: 3m per joint × 6 joints = 18m total
- **Connectors**: M12 or M23 industrial circular connectors
- **Routing**: Through hollow joint shafts and cable carriers
- **Lunar manufacturability**: ✓ Copper wire from lunar copper; insulation import or synthesize

#### 3.7.2 Signal Cables (2 kg)
- **Types**:
  - EtherCAT bus: CAT6a shielded Ethernet
  - Camera data: USB 3.0
  - Force sensor: 6-wire + shield
  - Safety signals: 4-wire
- **Total length**: ~25m
- **Lunar manufacturability**: ⚠️ Copper conductors manufacturable; high-speed cable import

#### 3.7.3 Cable Management (3 kg)
- **Drag chains**: Polymer energy chains for base and shoulder (2m each)
- **Spiral wrap**: For forearm and wrist cables
- **Mounting clips**: Aluminum or polymer
- **Lunar manufacturability**: ⚠️ Polymer chains import initially; aluminum clips manufacturable

#### 3.7.4 Connectors and Terminals (2 kg)
- **Types**: M12, M23, RJ45, USB-C
- **Quantity**: ~40 connectors total
- **Terminal blocks**: DIN-rail mounted
- **Lunar manufacturability**: ✗ Precision connectors import

#### 3.7.5 Thermal Management (2 kg)
- **Challenge**: No convective cooling in vacuum-adjacent environment
- **Solution**: Heat pipes from motors to base-mounted radiator
- **Components**:
  - Copper heat pipes (6× from motors): 1 kg
  - Aluminum radiator fins: 0.8 kg
  - Thermal interface pads: 0.2 kg
- **Radiator**: Mounted on base, 0.3 m² surface area
- **Heat dissipation**: 500W continuous (motors at 50% duty cycle)
- **Lunar manufacturability**: ✓ Copper and aluminum manufacturable

### 3.8 Safety and Enclosure (6 kg)

#### 3.8.1 Emergency Stop System (1 kg)
- **Mushroom buttons**: 2× (one on control pendant, one on robot base)
- **Safety relay**: Dual-channel monitored
- **Action**: Removes power to all motor drives (STO - Safe Torque Off)
- **Reset**: Manual reset required after E-stop
- **Lunar manufacturability**: ⚠️ Buttons and relays import

#### 3.8.2 Light Curtains / Safety Barriers (2 kg)
- **Type**: Optical safety curtain or area scanner
- **Coverage**: 2m × 2m work cell perimeter
- **Response time**: <100 ms
- **Function**: Detects human entry, triggers safe stop
- **Standard**: IEC 61496 Type 4 (safety light curtain)
- **Lunar manufacturability**: ✗ Import required (precision optics and electronics)

#### 3.8.3 Protective Covers (3 kg)
- **Material**: Polycarbonate or aluminum sheet
- **Coverage**: Motor housings, gear reducers, wrist mechanisms
- **Function**:
  - Prevent pinch points
  - Dust protection
  - Cable protection
- **Lunar manufacturability**: ✓ Aluminum sheet manufacturable; polycarbonate import

## 4. Mass Budget Summary

| Subsystem | Mass (kg) | % of Total |
|-----------|-----------|------------|
| Mechanical structure | 35 | 29% |
| Actuation (motors + gearboxes) | 30 | 25% |
| Power system | 8 | 7% |
| Control system | 6 | 5% |
| Sensing system | 12 | 10% |
| End effector | 8 | 7% |
| Wiring and integration | 15 | 12% |
| Safety and enclosure | 6 | 5% |
| **TOTAL** | **120** | **100%** |

**Mass distribution by manufacturing source:**
- Lunar-manufacturable (structures, cables, heat sinks): ~55 kg (46%)
- Partially manufacturable (motors, gearboxes, sensors): ~35 kg (29%)
- Import required (electronics, magnets, precision components): ~30 kg (25%)

## 5. Construction and Assembly

### 5.1 Assembly Sequence (Assuming All Parts Available)

**Phase 1: Base Assembly (8 hours)**
1. Install J1 motor and gearbox into base frame
2. Install J1 position encoder and wiring
3. Mount base to floor/table and level
4. Connect base to power distribution board
5. Initial J1 motion test

**Phase 2: Arm Assembly (16 hours)**
6. Assemble J2 (shoulder) into upper arm link
7. Assemble J3 (elbow) into forearm link
8. Mechanically connect shoulder to base (J1 output flange)
9. Mechanically connect forearm to upper arm (J2 output flange)
10. Route motor cables through arm structure
11. Install cable drag chains

**Phase 3: Wrist Assembly (8 hours)**
12. Assemble J4-J5-J6 wrist module (pre-assembled subassembly)
13. Mount wrist to forearm (J3 output flange)
14. Install force/torque sensor to wrist flange
15. Route wrist cables through forearm

**Phase 4: Electrical Integration (24 hours)**
16. Install motor controllers in control cabinet
17. Install main controller and safety controller
18. Connect all motor power cables to controllers
19. Connect all encoder signals to controller
20. Install power supply and distribution board
21. Install emergency battery backup
22. Wire emergency stop circuit
23. Install safety light curtains
24. Complete all electrical terminations and labeling

**Phase 5: End Effector Integration (4 hours)**
25. Install quick-change tool interface to force sensor
26. Assemble gripper
27. Attach gripper to tool interface
28. Connect gripper actuator signals and power

**Phase 6: Sensor Integration (12 hours)**
29. Mount vision cameras to wrist
30. Mount LED ring lights
31. Install proximity sensors at workspace boundaries
32. Connect all sensor signals to controller
33. Install thermal management system (heat pipes and radiator)

**Phase 7: Software and Calibration (30 hours)**
34. Load controller firmware and OS
35. Load robot control software
36. Configure EtherCAT network
37. Perform motor phasing and direction check
38. Establish encoder zero positions (mechanical reference)
39. Measure link lengths and DH parameters
40. Calibrate camera intrinsics (lens distortion)
41. Calibrate camera extrinsics (hand-eye transform)
42. Calibrate force/torque sensor (zero offset and scale)
43. Configure safety limits (workspace, velocity, force)
44. Test trajectory planning and motion control

**Phase 8: Testing and Commissioning (20 hours)**
45. No-load motion tests (all axes)
46. Payload tests (5 kg, 10 kg, 15 kg, 20 kg)
47. Repeatability test (100 moves to same position)
48. Accuracy test (move to calibrated reference points)
49. Safety system tests (E-stop, light curtain, software limits)
50. Vision system tests (part detection and pose estimation)
51. Force control tests (compliant insertion, contact detection)
52. Continuous operation test (8 hours at representative duty cycle)
53. Final inspection and documentation

**Total assembly time**: 122 hours (~15 working days with one technician, ~8 days with two)

### 5.2 Special Tooling Required for Assembly

- Torque wrenches (10-200 Nm range)
- Hex key sets (metric M3-M12)
- Multimeter and oscilloscope
- Crimp tools for electrical terminals
- Cable cutters and strippers
- Encoder alignment tools
- Collision detection test fixtures
- Calibration targets (checkerboard, sphere)
- Load weights (5, 10, 15, 20 kg calibrated masses)
- Leveling instruments

## 6. Operational Considerations

### 6.1 Power Consumption

**Continuous operation (typical assembly task):**
- Motors (50% duty cycle, 40% average load): 600W
- Controller and drives: 150W
- Vision and sensors: 50W
- LED lighting: 24W
- **Total average**: ~825W

**Peak power (all axes accelerating with full payload):**
- Motors (100% torque): 2400W
- Controller and drives: 200W
- Sensors and lighting: 74W
- **Total peak**: ~2700W

**Energy per 8-hour shift**: 6.6 kWh

### 6.2 Maintenance Schedule

**Daily** (before shift):
- Visual inspection for damage
- Check emergency stop function
- Verify no unusual noises or vibrations

**Weekly**:
- Clean camera lenses and gripper jaws
- Check cable routing (no rubbing or kinks)
- Verify torque on critical fasteners

**Monthly**:
- Lubricate gearboxes (if not sealed units)
- Inspect cable wear in drag chains
- Test safety light curtain function
- Review error logs

**Annual** (or every 2000 hours):
- Replace gearbox lubricant
- Inspect motor bearings
- Re-calibrate force sensor and cameras
- Replace worn gripper jaws
- Check all electrical connections
- Update controller software

**Major overhaul** (every 10,000 hours / 5 years):
- Replace motor bearings
- Inspect gearbox components (flexsplines, bearings)
- Replace cables showing wear
- Replace any degraded seals
- Complete re-calibration

### 6.3 Common Failure Modes and Spares

**High-wear items** (stock spares):
- Gripper jaws (consumable, every 500 hours)
- Motor cables (flex fatigue, every 5000 hours)
- Encoder batteries (lithium, 5-10 year life)
- Light curtain emitters/receivers (impact damage)

**Critical spares** (for rapid repair):
- Complete motor assemblies (1 large, 1 small)
- Motor controller drives (2 units)
- Force/torque sensor
- Vision cameras (2 units)
- Emergency stop buttons

**Repair capability**:
- Most mechanical parts can be re-manufactured on Moon
- Electronics must be imported or cannibalized
- Gearboxes repairable if precision metrology available

## 7. Lunar Manufacturing Analysis

### 7.1 Materials Sourcing

**Abundant on Moon (from regolith/anorthite)**:
- Aluminum (15% of highland regolith)
- Iron (5-10% of mare regolith)
- Silicon (glasses, ceramics)
- Oxygen (oxides, make water for chemistry)

**Accessible with extraction**:
- Copper (trace in regolith, or from meteoritic iron)
- Titanium (ilmenite FeTiO₃ abundant in mare)
- Calcium (anorthite CaAl₂Si₂O₈)

**Scarce or absent**:
- Rare earths (neodymium for magnets) - *very low concentrations*
- Lithium - *possible in some minerals but very low*
- Cobalt - *meteoritic iron only*
- Phosphorus - *trace only*

### 7.2 Manufacturing Processes Required

**Level 1: Currently in KB** (✓)
- Casting (aluminum, iron, steel)
- Machining (CNC milling, turning, drilling)
- Welding (arc, resistance)
- Sheet metal forming

**Level 2: Needed for labor bot** (some gaps)
- Precision grinding (bearing races, gear teeth)
- Wire drawing (electrical wire)
- Magnet wire insulation (enamel coating)
- Heat treatment (steel hardening)
- Electrical steel lamination stamping
- Injection molding or extrusion (plastics, if polymer synthesis exists)

**Level 3: Advanced (probably import)** (✗)
- Semiconductor fabrication (ICs, microcontrollers)
- Printed circuit board manufacturing
- Permanent magnet sintering (NdFeB)
- High-precision optical manufacturing
- LCD/OLED display manufacturing

### 7.3 Critical Import Dependencies

**Category A: No lunar alternative in near term**
1. Neodymium magnets (motor rotors)
2. Microcontrollers and processors (motor drives, main computer, safety controller)
3. High-precision encoders (optical or magnetic, 20-bit)
4. Camera image sensors (CMOS/CCD)
5. Strain gauges (force sensor)
6. Safety light curtain optoelectronics
7. Lithium-ion battery cells

**Category B: Initially import, later manufacture**
8. Harmonic drive flexsplines (need precision heat treatment and metrology)
9. High-speed data cables (USB, Ethernet)
10. Electrical connectors (M12, M23)
11. Insulated wire (need polymer synthesis or enamel coating)
12. Polycarbonate/acrylic (need polymer synthesis)

**Category C: Lunar-manufacturable**
13. Aluminum and steel structures
14. Copper conductors
15. Glass (lenses, diffusers)
16. Mechanical fasteners
17. Heat pipes and radiators

### 7.4 Minimum Import Mass

**Per robot (assuming Category A + B imports)**:
- Motors (magnets + encoders): 18 kg (all 6 motors)
- Controllers and electronics: 6 kg (computers, drives, safety)
- Sensors: 5 kg (cameras, force, proximity)
- Cables and connectors: 3 kg (special cables)
- Gripper motor: 2 kg (stepper with magnets)
- Batteries: 1 kg
- **Subtotal Category A+B**: ~35 kg

**If Category B items are manufactured locally** (future state):
- Reduces to ~25 kg per robot (motors, electronics, sensors only)

**Implication**: For a fleet of 10 labor bots, need 250-350 kg of Earth imports - a significant but not prohibitive launch mass.

## 8. Design Rationale and Trade-offs

### 8.1 Why 120 kg Total Mass?

- Comparable to commercial collaborative robots (UR10: 33 kg, but 10 kg payload)
- Lunar-manufacturable structure is ~35 kg (aluminum/steel)
- Standard industrial motors and drives: ~40 kg
- Leaves budget for sensors, cabling, integration: ~45 kg
- Heavy enough to be stable (low lunar gravity), light enough to manufacture and move

### 8.2 Why 6-DOF Serial Arm vs. Alternatives?

**Advantages**:
- Proven industrial design (millions of units on Earth)
- Full 3D manipulation capability
- Modular (can repair individual joints)
- Large workspace relative to footprint
- Simple mounting (bolts to floor/table)

**Disadvantages vs. alternatives**:
- *Gantry robot*: Would have larger workspace but huge footprint, much heavier
- *SCARA*: Lighter but only 4-DOF (limited orientation control)
- *Delta*: Very fast but tiny workspace, low payload
- *Humanoid*: Much more complex, poor payload/mass ratio, harder to manufacture

### 8.3 Why Harmonic Drives vs. Other Gearboxes?

**Advantages**:
- Zero backlash (critical for precision)
- High ratio in compact package (100:1 in <100mm)
- Coaxial (input/output on same axis - simplifies design)
- Proven in space applications (ISS Canadarm2)

**Disadvantages**:
- Expensive on Earth (mitigated by lunar manufacturing)
- Limited life (flexspline fatigue) - plan for replacement at 10,000 hours
- Requires precision manufacturing - initially import, later manufacture with better metrology

### 8.4 Why Electric Gripper vs. Pneumatic?

**Electric advantages**:
- No compressed air infrastructure needed
- Precise force control
- Lower maintenance
- Easier integration (just cables, no air lines)

**Pneumatic advantages** (not chosen):
- Faster actuation
- Higher force for same mass
- BUT requires air compressor, regulators, valves, plumbing

**Decision**: Electric chosen for simplicity and precision, even though slightly heavier.

## 9. Future Enhancements

**Modular tool library**:
- Vacuum gripper for flat parts
- Small parts gripper (50mm stroke)
- Electric screwdriver
- Welding torch
- Camera inspection tool
- Part marking tool

**Advanced sensing**:
- Tactile sensors in gripper
- 3D laser scanner for part digitization
- Thermal camera for quality control

**Mobility**:
- Mount on linear track for extended reach
- Mount on mobile base for flexible positioning

**Redundancy**:
- 7-DOF arm for collision avoidance and singularity avoidance
- Dual-arm system for complex assembly

## 10. Conclusion

The `labor_bot_general_v0` is a 120 kg, 6-DOF industrial robot arm optimized for lunar manufacturing within pressurized habitats. The design balances:

- **Capability**: 2m reach, 20 kg payload, full 6-DOF manipulation
- **Manufacturability**: 46% of mass from lunar materials, structural components from Al/Fe
- **Import minimization**: 25 kg of critical electronics/magnets per unit
- **Reliability**: Proven industrial design, modular for repair
- **Assembly time**: 120 hours with available parts

**Critical import dependencies**: Motors (NdFeB magnets), controllers (microelectronics), sensors (optics/semiconductors), high-precision gearboxes (initial), and specialized cables.

The detailed BOM derived from this analysis specifies 45 distinct components organized into 8 subsystems, providing a realistic foundation for simulation of lunar manufacturing capabilities.

---

**References for further detail**:
- ISO 9283: Manipulating industrial robots - Performance criteria
- ISO 10218: Robots and robotic devices - Safety requirements
- IEC 61496: Safety of machinery - Electro-sensitive protective equipment
- Technical specifications based on commercial robots: ABB IRB 1600, KUKA KR 10, Fanuc M-10iA
