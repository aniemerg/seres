# Controls Level-2 Audit

Status: review completed; source-table aligned BOM correction applied.

Purpose:

- Compare current controls BOM leaves against the source table and available
  source evidence.
- Preserve boundaries between controls, power supplies, cabin, wire feeder,
  positioning, and fixed gun.
- Keep controls as command, acquisition, monitoring, and logic hardware/software;
  do not move load hardware, feedthroughs, or power-conversion hardware here.

Source registry:

- `research/ebf3_bom_sources/sources/level_1_subsystems/controls/controls_sources.md`

Related boundary reviews:

- `research/ebf3_bom_sources/derived/ebf3_subsystem_boundaries.md`
- `research/ebf3_bom_sources/organized/hv_electrical_interface_review.md`
- `research/ebf3_bom_sources/organized/hv_grounding_return_review.md`

## Source Use

### RAW-NASA-EBF-PATENT

Evidence:

- "computer system"
- "control software"
- "video cameras"
- "thermal imaging cameras"
- "at least one sensor"
- "recording data"
- "instrumentation Subsystem"

Use:

- Supports control computer, software, visual/thermal monitoring, sensors,
  timebase/data logging, and a controls/instrumentation package.
- Does not assign chamber viewports, passive mounts, or feedthrough shells to
  controls.

### RAW-NASA-EBF-SPACE

Evidence:

- "operated from a laptop computer using control software"
- "Thermal Imaging of EBF3"

Use:

- Supports the control-computer/software row and thermal-imaging monitoring row.

### RAW-BINP-60KEV-30KW

Evidence:

- "CAN-bus interface"
- "control computer can control"
- "monitor output voltage, beam current, cathode heat current"
- "magnetic lens and correctors currents"
- "alarm and blocking system"

Use:

- Supports CAN communication, central monitoring, current/voltage acquisition,
  and safety/blocking logic.

### RAW-BINP-60KV-15KW-HV-TANK

Evidence:

- "DSP and PLM"
- "analogue input buffers"
- "controller measured 7 analogue channels"
- "CAN-bus interface"

Use:

- Supports real-time control processor, analog input/ADC, and isolated control
  interface concepts.

### LOCAL-EBF3-CONTROLS-TABLE

Use:

- Introduces CTL-1 through CTL-13 candidates.
- Candidate-only; it cannot justify recipes, materials, or child BOMs by itself.

## Main Finding

The current controls BOM mostly matched the source table. Two rows needed
correction:

- Table row CTL-9 is **thermal imaging monitoring system**, but the current BOM
  had `ebf3_process_monitor_lighting`.
- Table row CTL-13 is **controls cabinet**, but the current BOM had
  `ebf3_control_cabinet_harness`.

Lighting and cabinet harnessing remain plausible controls/cabin details, but
they should not replace the source-table top-level rows.

## Level-2 Decision Matrix

| Source table row | Current or recommended item | Decision | Rationale |
| --- | --- | --- | --- |
| CTL-1 control computer | `ebf3_control_computer` | keep | NASA sources support computer/control operation. |
| CTL-2 real-time control processor | `ebf3_realtime_control_processor` | keep | BINP sources support DSP/PLM control. |
| CTL-3 control software | `ebf3_control_software` | keep | NASA sources support control software. |
| CTL-4 CAN-bus communication interface | `ebf3_can_bus_interface` | keep | BINP source supports CAN-bus interface. |
| CTL-5 analog input and ADC module | `ebf3_analog_input_adc_module` | keep | BINP source supports measured analog channels; HV-side sensors remain outside controls. |
| CTL-6 sensor interface module | `ebf3_sensor_interface_module` | keep | NASA source supports sensors; controls own conditioning/acquisition. |
| CTL-7 data logging and timebase module | `ebf3_data_logger_timebase` | keep | NASA source supports timing/data storage. |
| CTL-8 visible monitoring camera | `ebf3_visible_camera` | keep | NASA source supports video cameras. |
| CTL-9 thermal imaging monitoring system | `ebf3_thermal_imaging_monitoring_system` | corrected | NASA source supports thermal imaging; lighting is a deferred support item. |
| CTL-10 motion-control interface | `ebf3_motion_control_drive_module` | keep with boundary note | Controls own command interface; power driver outputs belong to power supplies and motion hardware belongs to positioning. |
| CTL-11 wire-feed control interface | `ebf3_wire_feed_control_module` | keep with boundary note | Controls own command/feedback interface; feeder mechanism remains in wire feeder. |
| CTL-12 alarm and blocking logic module | `ebf3_safety_blocking_logic` | keep | BINP source supports alarm/blocking system. |
| CTL-13 controls cabinet | `ebf3_controls_cabinet` | corrected | Source table row is cabinet-level hardware; harness becomes a child/deferred detail. |

## Applied BOM Correction

- Replaced `ebf3_process_monitor_lighting` with
  `ebf3_thermal_imaging_monitoring_system` at CTL-9.
- Replaced `ebf3_control_cabinet_harness` with `ebf3_controls_cabinet` at
  CTL-13.
- Kept lighting and cabinet harness as deferred candidates, not deleted.

## Batch Child Split Review

| Parent scope | Current status | Rationale |
| --- | --- | --- |
| Control computer and real-time processor | adopt package split / detail deferred | NASA and BINP support computer/control-processor functions. Board, storage, connector, and enclosure children are package markers; processor architecture and software deployment remain unresolved. |
| CAN, ADC, sensor interface, data logger | adopt package split / detail deferred | BINP supports CAN bus, analog channels, and monitored currents/voltages. Analog Devices PLC references support ADC, signal-conditioning, isolation, and I/O module concepts. Circuit design and calibration remain unresolved. |
| Visible and thermal monitoring | adopt package split / detail deferred | NASA supports video/thermal monitoring. Sensor module, lens, housing, cable/processing board children are retained; camera model, optics, viewport relation, and lighting ownership remain unresolved. |
| Motion and wire-feed control modules | adopt package split / split-boundary guarded | Controls owns command/acquisition interfaces. Power stages and mechanism hardware remain in power supplies, positioning, and wire feeder. |
| Safety logic and controls cabinet | adopt package split / detail deferred | BINP supports alarm/blocking; cabinet child split is a package representation only. Harness routing, interlock locations, grounding, and certification remain unresolved. |
| Control software | keep leaf | Software is not a physical assembly; later work should split functions or artifacts only if software modeling becomes a project goal. |

## Manufacturing Readiness

No controls item is local-ready. Industrial controllers, ADC modules, isolated
interfaces, cameras, thermal imaging hardware, software media, interlocks,
cabinet wiring, calibration, shielding, and certification all need separate
material/process and electronics-readiness reviews before recipes are attached.
