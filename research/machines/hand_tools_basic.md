# Hand tools basic

## Machine identity

- KB ID: `hand_tools_basic`
- KB name: Hand tools (basic set)
- KB file: `kb/items/machines/hand_tools_basic.yaml`
- KB kind: `machine`
- Current KB mass: 4.1 kg
- Current KB scope: basic hand tool kit including wrenches, screwdrivers, pliers, hammers, and measuring tape.

## KB usage and needed function

The KB uses `hand_tools_basic` widely as generic support tooling for assembly, cutting, fitting, installation, gasket cutting, glazing, plumbing/pneumatics, surface finishing, cleanup, inspection, PCB assembly, test-equipment assembly, and other low-complexity manual tasks.

It also appears as a component of broader tool or equipment sets, including `cutting_tools_general` and `test_equipment_electronics`.

The needed function is general-purpose manual manipulation and maintenance support, usually combined with `labor_bot_general_v0`.

## Reality classification

Classification: real practical tool kit, not a machine.

Basic hand tool sets are real and commercially available. The KB item is realistic as a reusable tool kit, but classifying it as `kind: machine` is only a schema convenience. It should not be interpreted as powered capital equipment.

The 4.1 kg mass is plausible for a compact basic kit. It is low for a full mechanic or industrial maintenance set, but acceptable for the stated list of simple tools.

## Evidence links

- Grainger lists general maintenance tool sets as assortments of tools to inspect, service, and repair machinery, mechanical systems, and structural components. Source: https://www.grainger.com/category/tools/hand-tools/assorted-tool-sets-kits/general-maintenance-tool-sets
- Harbor Freight lists hand tool sets such as a master technician set containing common mechanic tools including ratcheting wrenches, pliers, and sockets. Source: https://www.harborfreight.com/hand-tools/tool-sets.html
- Home Depot lists professional/industrial hand tool sets and household tool kits with screwdrivers, wrenches, hammers, tape measures, and pliers. Source: https://www.homedepot.com/b/Tools-Hand-Tools-Hand-Tool-Sets/N-5yc1vZc22x
- SafetyCulture describes hand tools as manually operated tools that do not require a power source. Source: https://safetyculture.com/topics/hand-and-power-tools/

## Commercial alternatives

Commercial alternatives include:

- Basic homeowner or maintenance tool kit.
- Industrial maintenance hand tool set.
- Mechanic's tool set.
- Electrical hand tool kit.
- Mechanical hand tool kit.
- Task-specific kits for plumbing, electronics, assembly, or machine maintenance.

For the KB, one generic `hand_tools_basic` set is appropriate for low-precision and low-force tasks. Specialized kits should only be retained where material, safety, or task requirements differ.

## Build or open-source references

Hand tools can be locally manufactured one by one through forging, machining, heat treatment, grinding, handle fabrication, and assembly. The KB already has a recipe for the basic set.

Open-source "build" references are less relevant than manufacturing process coverage because the object is a collection of common tools. The important realism issues are steel quality, heat treatment, grip/insulation, tolerances, and durability.

## Related machine research

Related KB items and research candidates include:

- `hand_tools_mechanical`
- `hand_tools_electrical`
- `assembly_tools_basic`
- `cutting_tools_general`
- `wire_crimping_tools`
- `refractory_installation_tools`
- `tool_set_general`

`hand_tools_basic` overlaps with mechanical and electrical hand-tool sets. Conservative mode favors one generic set unless electrical insulation, crimping, torque calibration, or other special properties matter.

## Recommendation for KB realism

Keep as a tool kit, but do not treat it as a true machine.

Recommended future cleanup:

- Reclassify as part/tooling if the schema supports it, or document that `kind: machine` is being used to represent reusable shop tooling.
- Keep `hand_tools_basic` as the general fallback for labor-bot manual work.
- Avoid proliferating many near-identical hand-tool kits unless safety or process compatibility requires it.
- Consider whether `hand_tools_mechanical` and `hand_tools_basic` should be consolidated.

## Confidence and open questions

Confidence: high that the item is real; high that it is better described as reusable tooling than a machine.

Open questions:

- Does the KB need a distinct `tool` kind or should tooling continue to use `kind: machine` for simulator capacity checks?
- Are insulated electrical tools and calibrated torque tools separate enough to keep distinct?
- Is 4.1 kg enough for the number and durability of tools implied by all processes using this kit?
