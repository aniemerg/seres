# Mechanical Hand Tools Machine Reality Research

## Machine identity

- KB item id: `hand_tools_mechanical`
- KB name: Mechanical hand tools
- KB file: `kb/items/machines/hand_tools_mechanical.yaml`
- Current KB kind: `machine`
- Current KB mass: 15 kg
- Current BOM: `bom_hand_tools_mechanical_v0`
- Current recipe: `recipe_hand_tools_mechanical_v0`

## KB usage and needed function

The item is directly used by `finishing_deburring_v0` and `belt_installation_and_tensioning_v0`. It is also a component of `hand_tools_basic`. Most general assembly processes use `assembly_tools_basic`.

The needed function is a reusable mechanical hand-tool kit: wrenches, sockets, screwdrivers, pliers, hammers, Allen keys, punches, files, and similar manually operated tools for assembly, repair, tensioning, deburring, and adjustment.

## Reality classification

Real practical tool kit, not a standalone machine.

Mechanical hand-tool sets are real and essential. The 15 kg mass is plausible for a robust mechanical maintenance kit. Classifying it as `kind: machine` is a simulator/resource convenience; for imported-machine-list realism it should be treated as a tool kit.

## Evidence links

Evidence from `research/machines/hand_tools_basic.md` applies:

- Home Depot lists professional and industrial hand tool sets containing screwdrivers, wrenches, hammers, tape measures, pliers, and similar tools: <https://www.homedepot.com/b/Tools-Hand-Tools-Hand-Tool-Sets/N-5yc1vZc22x>
- SafetyCulture defines hand tools as manually operated tools that do not require a power source: <https://safetyculture.com/topics/hand-and-power-tools/>
- Grainger sells mechanics tool sets including sockets, wrenches, pliers, screwdrivers, hex keys, and tool storage: <https://www.grainger.com/category/tools/hand-tools/tool-sets/mechanics-tool-sets>
- McMaster-Carr sells mechanics' tool sets with wrenches, sockets, pliers, screwdrivers, punches, files, and related mechanical tools: <https://www.mcmaster.com/products/tool-sets/>

## Commercial alternatives

- Mechanics tool set for maintenance and machine assembly.
- Industrial maintenance tool kit with sockets, wrenches, pliers, punches, files, and hammers.
- Electrical hand-tool kit for insulated electrical work, crimping, and wire stripping.
- Assembly station tool set with fixtures, clamps, bins, torque tools, and benches.
- Precision tool kit for small mechanisms or electronics.

## Build or open-source references

Many hand tools can be locally forged, machined, heat treated, ground, and fitted with handles. High-quality sockets, ratchets, precision hex keys, hardened files, and screwdrivers require alloy steels, heat treatment, grinding, broaching, and durable finishes.

The KB recipe is reasonable as a coarse route to a local tool kit, but it should not hide specialized tooling needs such as torque wrenches, calibrated gauges, insulated electrical tools, or precision metrology.

## Related machine research

Related local reports:

- `research/machines/hand_tools_basic.md`
- `research/machines/inspection_tools_basic.md`
- `research/machines/wire_crimping_tools.md`
- `research/machines/refractory_installation_tools.md`
- `research/machines/cutting_tools_general.md`

## Recommendation for KB realism

Keep as a tool kit, but avoid counting it as a machine.

Recommended options:

- Treat `hand_tools_mechanical` as reusable tool inventory.
- Keep separate from `hand_tools_electrical` only where insulated handles, crimping, wire stripping, or electrical safety matters.
- Consider consolidating into `hand_tools_basic` or `assembly_tools_basic` for coarse processes under Conservative Mode.
- Use specific tool kits only where they change safety or function: electrical, welding, refractory, inspection, crimping, or precision tooling.
- Do not use this item as a substitute for powered cutting, machining, pressing, or welding equipment.

## Confidence and open questions

Confidence: high that the item is real; high that it is a tool kit rather than a machine; medium on whether the KB benefits from separate `hand_tools_basic`, `hand_tools_mechanical`, and `assembly_tools_basic` items.

Open questions:

- Should `finishing_deburring_v0` need `hand_tools_mechanical` specifically, or a deburring/cutting-tool kit?
- Is `hand_tools_basic` meant to be a meta-kit that includes this item plus electrical tools?
- Should labor-bot bootstrap inventory include one general tool kit or multiple specialized kits?
