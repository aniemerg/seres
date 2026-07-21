# ebf3_controls Mapping

Authority note: this is a first-pass scaffold mapping from a user-derived table.
It preserves candidate item IDs and high-level modeling intent, but it is not a
decomposition planning file and cannot by itself justify child BOM creation,
material selection, recipe closure, or local manufacturability.

Controls leaf items aligned to the source table after
`research/ebf3_bom_sources/organized/controls_level_2_audit.md`; no leaf
recipes yet to preserve fidelity.

| Source row | Item ID | Modeling decision |
| --- | --- | --- |
| CTL-1 | `ebf3_control_computer` | Industrial PC/control computer for operator commands, subsystem coordination, and fabrication process management. |
| CTL-2 | `ebf3_realtime_control_processor` | Deterministic controller/FPGA/DSP/MCU hardware for high-voltage, motion, wire-feed, and interlock timing. |
| CTL-3 | `ebf3_control_software` | Control software stored on controller media; command sequencing, interlocks, data logging, and process control logic. |
| CTL-4 | `ebf3_can_bus_interface` | CAN-bus communication interface between control computer and HV, magnetic, modulator, alarm, and subsystem controllers. |
| CTL-5 | `ebf3_analog_input_adc_module` | Analog input and ADC module for voltage, current, temperature, and feedback measurement. |
| CTL-6 | `ebf3_sensor_interface_module` | Sensor interface electronics for thermocouples, pressure sensors, beam diagnostics, and isolated signal conditioning. |
| CTL-7 | `ebf3_data_logger_timebase` | Data logger and timebase module for process history and later analysis. |
| CTL-8 | `ebf3_visible_camera` | Visible camera assembly for monitoring deposition and chamber process state. |
| CTL-9 | `ebf3_thermal_imaging_monitoring_system` | Thermal imaging monitoring system for melt-pool temperature or thermal-field monitoring. |
| CTL-10 | `ebf3_motion_control_drive_module` | Motion drive/control module for commanded positioning subsystem motion. |
| CTL-11 | `ebf3_wire_feed_control_module` | Wire-feed control electronics for feed motor command and feedback. |
| CTL-12 | `ebf3_safety_blocking_logic` | Safety logic, alarm, and blocking/interlock module. |
| CTL-13 | `ebf3_controls_cabinet` | Controls cabinet assembly for control computer, I/O, communication hardware, safety logic, terminal blocks, and cabinet hardware. |

Masses are first-pass allocations constrained to the current subsystem mass. Leaf items intentionally have no local recipes yet.

Deferred candidates kept out of the source-table Level-2 presentation:

- `ebf3_process_monitor_lighting`
- `ebf3_control_cabinet_harness`
