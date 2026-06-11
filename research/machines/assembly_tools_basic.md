# Assembly Tools Basic

## Machine identity

- KB ID: `assembly_tools_basic`
- KB name: Basic assembly tools
- KB file: `kb/items/machines/assembly_tools_basic.yaml`
- Current KB type: `machine`
- Current KB mass: 50 kg
- Current KB capabilities: `assembly`, `mechanical_assembly`, `electrical_assembly`
- Current KB description: ADR 003 stub referenced by many processes but originally undefined.
- Current KB BOM: tool station frame, general tool set, power conditioning module, sensor suite, and imported control compute module.

## KB usage and needed function

`assembly_tools_basic` is one of the most widely used support resources in the KB, appearing in mechanical assembly, electrical assembly, PCB assembly, solder-paste application, motor assembly, sensor integration, bearing assembly, tank assembly, seal installation, fastener fabrication, enclosure assembly, heater installation, support removal, and many other manual/final assembly processes.

The needed function is a general assembly support kit: workbench/station, hand tools, drivers, torque tools, clamps, fixtures, bins, ESD/electrical tools, basic powered drivers, and possibly simple sensors or controllers for guided assembly.

## Reality classification

Classification: real tool/station bundle, not a single machine.

Industrial assembly tools and workstations are real. However, the KB item is broader than a normal "tool kit." With a station frame, power conditioning, sensors, and imported compute, it resembles an instrumented assembly station. If the intent is simple hand tools, it overlaps with `hand_tools_basic`; if the intent is repeatable mechanical/electrical assembly, the station framing and torque/control tools are reasonable.

The 50 kg mass is plausible for a bench/station plus tools, but not for all possible fixtures and specialty tools implied by the many process references.

## Evidence links

- Atlas Copco describes assembly solutions ranging from electric and pneumatic power tools to handheld and fixtured assembly solutions and software platforms. Source: https://www.atlascopco.com/en-us/itba/product/assembly-tools-and-solutions-overview
- Atlas Copco sells electric assembly tools with intelligent controllers and ergonomic focus for fastening precision. Source: https://www.atlascopco.com/en-us/itba/products/assembly-solutions/electric-assembly-tools
- Technical Tool Products describes assembly technologies including manual, pneumatic, and electric assembly, hand-held and fixtured tooling, presses, torque arms, and multi-spindles. Source: https://www.technicaltoolproducts.com/applications/assembly-tools/
- Assembly Magazine notes that manual torque wrenches and screwdrivers are still widely useful for applying dynamic torque and auditing assemblies. Source: https://www.assemblymag.com/articles/93104-manual-torque-tools-still-rule
- Williams Industrial states that torque wrenches provide high torque accuracy and repeatability, with calibration certificates. Source: https://www.williams-industrial.com/us_en/torque
- PB Swiss Tools lists preset torque screwdrivers for repeatable tightening torque in industrial assembly and machining, with calibration recommendations. Source: https://www.pbswisstools.com/en/tools/quality-hand-tools/torque-tools/all-products

## Commercial alternatives

- Basic hand-tool set.
- Assembly workstation with bins, lighting, ESD mat, and tool holders.
- Torque wrench/screwdriver set.
- Electric torque screwdriver and controller.
- Pneumatic/electric rivet, crimp, or fastening tools.
- Fixture and clamp set.
- ESD-safe electronics assembly kit.
- Guided assembly station with sensors and process control.

## Build or open-source references

A basic assembly station can be locally built from:

- Steel or aluminum workbench frame.
- Tool storage, bins, lighting, and power distribution.
- Vises, clamps, fixture plates, and stops.
- Hand tools, torque tools, and powered screwdrivers.
- ESD mat/wrist strap where electronics are handled.
- Simple continuity tester, torque tester, or sensor feedback for guided work.

The hardest local items are calibrated torque tools, ESD-safe electronics tools, high-quality powered drivers, and any guided assembly sensors/controllers. Many hand tools are locally manufacturable later, but calibration and repeatability need reference equipment.

## Related machine research

Related reports already present:

- `hand_tools_basic.md`
- `hand_tools_mechanical.md`
- `measurement_equipment.md`
- `inspection_tools_basic.md`
- `wire_crimping_tools.md`
- `fixturing_workbench.md`
- `welding_tools_set.md`

`assembly_tools_basic` should not duplicate all of `hand_tools_basic`. It can be the workstation/resource bundle for assembly workflows, while `hand_tools_basic` remains the portable general tool kit.

## Recommendation for KB realism

Keep the concept, but clarify it as an assembly station/tool bundle rather than a machine.

Recommended future wording: "basic assembly workstation and tool set." If the KB wants only a hand-tool kit, consolidate with `hand_tools_basic`. If the KB wants assembly repeatability, keep this item and include torque tools, clamps/fixtures, ESD provisions, bins, power, and basic guided-assembly sensors.

Avoid using this item as a magical substitute for specialty tooling. Processes such as crimping, hydraulic assembly, precision bearing fits, PCB rework, and welding should still require their dedicated tools where needed.

## Confidence and open questions

Confidence: high that the concept is real; high that it is a tool/station bundle rather than a machine; medium on how much overlap with `hand_tools_basic` should remain.

Open questions:

- Is `assembly_tools_basic` intended to include a workbench/station, or only portable tools?
- Should calibrated torque tools be separate, or included here?
- Should electronics/ESD assembly tools be split from mechanical assembly tools?
