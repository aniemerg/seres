# Control compute module imported

## Machine identity

- KB ID: `control_compute_module_imported`
- KB file: `kb/items/machines/control_compute_module_imported.yaml`
- KB name: Control compute module (imported)
- KB mass: 2 kg per unit
- Current KB role: imported embedded controller/PLC/SBC module used across many machine BOMs for control logic, sensing, automation, and sometimes AI/compute.

## KB usage and needed function

Local usage shows this is a high-leverage imported electronics boundary item:

- It appears in the minimal/self-reproducing imported-machine set.
- `docs/parts_and_labor_guidelines.md` lists it as a common reusable imported computing module.
- It appears in dozens of machine BOMs, including furnaces, presses, grinders, separators, 3D printers, solar arrays, quench tanks, feeders, CMMs, and automation stations.
- It is also referenced by data/error-correction processes, which suggests broader compute use beyond simple PLC logic.
- The recipe says the imported compute module is inspected and functionally tested.

The needed function is reusable control electronics: CPU/microcontroller/PLC, memory, I/O interfaces, communications, sensor/actuator control, and potentially embedded AI. It is not a mechanical machine in the usual sense, but in the KB it acts as a reusable capacity/component.

## Reality classification

Classification: real practical imported electronics module / broad category.

Industrial PLCs, programmable automation controllers, embedded controllers, and industrial single-board computers are real. The KB item is plausible as a generic imported controller. The "imported" tag is important: advanced semiconductors, reliable embedded compute, and safety-rated control electronics are not realistically produced by an early self-reproducing industrial seed.

## Evidence links

- Renesas describes industrial PLCs as rugged computers for automating real-time mechanical and industrial processes: https://www.renesas.com/en/applications/industrial/industrial-automation/industrial-programmable-logic-controller-plc
- Unitronics defines PLCs as ruggedized computers used for industrial automation of processes, machine functions, or production lines: https://www.unitronicsplc.com/what-is-plc-programmable-logic-controller/
- Rockwell Automation describes PLCs as industrial computers that monitor inputs, execute programmed logic, and drive outputs in real time: https://www.rockwellautomation.com/en-us/products/hardware/programmable-controllers.html
- DigiKey describes industrial automation use of single-board computers from Arduino, Industrial Shields, KUNBUS, and similar suppliers: https://www.digikey.com/en/articles/how-single-board-computers-extend-the-reach-of-industrial-automation
- Gateworks describes industrial-grade ARM single-board computers for smart factories, autonomous robots, energy infrastructure, and mission-critical control: https://www.gateworks.com/products/industrial-single-board-computers/
- Eaton describes PLCs as solid-state electronic devices that control machine or process operation: https://www.eaton.com/us/en-us/products/controls-drives-automation-sensors/programamble-logic-controllers.html

## Commercial alternatives

Commercial alternatives include:

- Brick PLCs for simple machine control.
- Modular PLC/PAC systems with remote I/O.
- Industrial SBCs with I/O expansion.
- Microcontroller control boards for non-safety hobby/light industrial use.
- Safety PLCs and certified safety controllers for hazardous machines.
- Edge AI modules for machine vision/advanced autonomy.

For the KB, one imported module can serve as a conservative placeholder, but safety-critical and high-performance AI control should eventually be distinguished.

## Build or open-source references

- OpenPLC and Raspberry Pi/Arduino-based PLC approaches show that low-cost open-source control is possible for simple systems: https://www.openplcproject.com/ and https://www.sunfounder.com/blogs/news/raspberry-pi-plc-a-low-cost-flexible-solution-for-industrial-automation
- AutomationDirect describes Arduino-compatible industrial open-source controller options: https://library.automationdirect.com/plc-vs-industrial-open-source-controller-what-to-know-for-the-plc-guru/

These support local assembly/integration, not local semiconductor manufacture. Even if boards can be assembled locally, processors, memory, precision power management, communications ICs, and safety certification remain imported or advanced-manufacturing dependencies.

## Related machine research

Related local reports:

- `research/machines/pcb_fab_equipment.md`
- `research/machines/power_conditioning_equipment.md`
- `research/machines/solar_array_v0.md`
- `research/machines/quench_tank.md`

Related KB items:

- `control_components`
- `control_circuit_board_basic`
- `microcontroller_or_embedded_board`
- `computer_core_imported`
- `safety_controller_plc`
- `sensor_suite_general`
- `power_conditioning_module`

No follow-up tasks were enqueued, per task constraint.

## Recommendation for KB realism

Keep as a real imported boundary component, but make the scope explicit.

Recommended cleanup when KB edits are allowed:

- Keep `control_compute_module_imported` as an import boundary for early phases.
- Consider renaming display name to "Imported industrial control module" if it mainly means PLC/SBC control, or split if AI compute is different.
- Do not count it as locally manufacturable merely because PCB assembly exists in the KB.
- Consider separating ordinary embedded controller, safety PLC, and AI/vision compute if mass/risk matters.
- Keep it reusable across many BOMs under Conservative Mode; it prevents proliferation of near-identical controller boards.

## Confidence and open questions

Confidence: high that this represents real equipment; high that import status is realistic for early phases.

Open questions:

- Does this item represent a PLC, industrial SBC, microcontroller board, AI module, or a mix?
- Which machines need safety-rated controls rather than a generic controller?
- Should software/firmware development be modeled separately from imported hardware?
