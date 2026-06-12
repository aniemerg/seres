# Coil winding machine

## Machine identity

- KB ID: `coil_winding_machine`
- KB name: Coil winding machine
- KB file: `kb/items/machines/coil_winding_machine.yaml`
- KB kind: `machine`
- Current KB mass: 120 kg
- Current KB structure: motorized spindle, wire tensioning, turn counting/control, frame, motor, tension-control unit, guide rails, bearings, sensors, control panel, and safety enclosure.

## KB usage and needed function

The KB uses `coil_winding_machine` for winding copper/magnet wire and resistive wire into electromagnetic or heating components:

- `kb/processes/coil_winding_basic_v0.yaml`
- `kb/processes/coil_winding_motor_v0.yaml`
- `kb/processes/transformer_winding_v0.yaml`
- `kb/processes/wire_winding_precision_v0.yaml`
- `kb/processes/photolithographic_coil_winding_v0.yaml`

It supports motors, transformers, inductors, antennas, relays, solenoids, resistors, and heating elements. The necessary function is controlled rotation plus wire guiding and tension control so the machine can count turns, maintain winding pitch, and avoid wire damage.

## Reality classification

Classification: real practical machine.

Coil winding machines are standard industrial and benchtop equipment. The KB item is not a placeholder; it is a generic automated or semi-automated coil winder. The 120 kg mass is plausible for a benchtop-to-light-industrial unit with frame, motor, controls, and guarding.

## Evidence links

- Whitelegg Machines describes benchtop coil and transformer winding machines with digital controllers for small inductors, motors, relays, solenoids, transformer primaries, chokes, and other coils. Source: https://www.coilwindingmachines.eu/linear_benchtop_winding_machines/index.html
- Armature Coil Equipment describes electromagnetic coil winding machines for motors, transformers, solenoids, and industrial electronic equipment. Source: https://www.armaturecoil.com/coil-winding-equipment/
- Itasca Automation describes single-spindle coil winders with automatic wire tension control, wire break detection, programmable memory, adjustable spindle speeds, and multiple winding modes. Source: https://www.itascaautosys.com/products/single-spindle-coil-winders/
- Sagar Industries lists commercial LV transformer coil winding machines with automatic operation and motorized winding. Source: https://www.sagareng.com/transformer-coil-winding-machines.html

## Commercial alternatives

Commercial alternatives include:

- Manual coil winding machine with mechanical turn counter.
- Benchtop semi-automatic coil winder with digital control.
- Transformer coil winding machine for heavier wire and larger coils.
- Motor stator/armature winding machine.
- CNC or programmable multi-axis coil winder for precision and repeatability.

The KB's generic machine is suitable for low- to medium-volume winding of motors, transformers, inductors, relays, solenoids, and heating coils.

## Build or open-source references

Small coil winders are practical to build:

- Instructables has an Arduino-based coil winder: https://www.instructables.com/Coil-Winder-Using-Arduino/
- Arduino forum discussions describe stepper-motor coil winders with turn counting, pause controls, wire spool fixtures, and wire straightening guides: https://forum.arduino.cc/t/an-arduino-to-control-and-count-to-200-rev-for-a-coil-winder/1323683

DIY units can cover simple inductors and small coils. Precision motor and transformer winding may require better tension control, traverse control, insulation handling, and safety enclosure.

## Related machine research

Related KB entries include:

- `coil_winding_machine_v0`
- `winding_machine`
- `winding_drums`
- `tension_control_unit`
- `tension_control_system`
- `wire_tensioning_mechanism`
- `turn_counter_module`
- `motor_assembly_standard_v0`
- `transformer_power_medium`

There is likely duplication between `coil_winding_machine`, `coil_winding_machine_v0`, and `winding_machine`. Future cleanup should decide whether one generic winding machine can cover coil, wire, and fiber spooling tasks or whether coil winding should remain distinct because of turn-count and winding-pattern precision.

## Recommendation for KB realism

Keep the item.

Recommended clarification: define it as a generic semi-automatic coil winder for motors, transformers, inductors, solenoids, relays, and heating coils. Preserve tension control and turn counting as core features.

Future cleanup:

- Normalize references that point to `coil_winding_machine_v0` if `coil_winding_machine` is the intended current ID.
- Decide whether `winding_machine` is a broader spooling/fiber machine and `coil_winding_machine` is the electrical-coil-specialized variant.
- Keep consumables such as magnet wire, insulation, bobbins/forms, and varnish separate from the machine.

## Confidence and open questions

Confidence: high that the machine is real and that the KB abstraction is appropriate.

Open questions:

- Does one machine need to handle both fine magnet wire and heavy transformer/heating-element wire, or should heavy winding be a separate variant?
- Are bobbins, coil forms, slot liners, insulation paper, varnish/impregnation, and curing modeled in downstream recipes?
- Should photolithographic coil creation use this machine, or should it be a separate PCB/photolithography process with no physical wire winding?
