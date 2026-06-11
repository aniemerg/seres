# Electrical Hand Tools Machine Reality Research

## Machine identity

- KB item id: `hand_tools_electrical`
- KB name: Electrical hand tools
- KB file: `kb/items/parts/hand_tools_electrical.yaml`
- Current KB kind: `machine`
- Current KB mass: 5 kg
- Current BOM: `bom_hand_tools_electrical_v0`
- Current recipe: `recipe_hand_tools_electrical_v0`

## KB usage and needed function

The item is used in cable harness assembly, crimping/soldering, electrical wiring and controls, power cable assembly, and as part of `hand_tools_basic`.

The needed function is a small electrical hand-tool kit: insulated screwdrivers and pliers, wire strippers, cutters, crimpers, probes, and terminal installation tools. It supports manual low-volume wiring work but does not replace test instruments, soldering stations, or connector-specific crimp tooling where those are required.

## Reality classification

Real practical tool kit, not a standalone machine.

Electrical hand tool kits are real and essential. The 5 kg mass is plausible for a compact set. The item is appropriately reusable as a simulator resource, but should be understood as a hand-tool kit rather than powered equipment.

## Evidence links

- Klein Tools sells insulated tool kits and electrical hand tools for electricians, including screwdrivers, pliers, cutters, and strippers: <https://www.kleintools.com/catalog/insulated-tool-kits>
- Wiha lists insulated tool sets with screwdrivers, pliers, cutters, and nut drivers for electrical work: <https://www.wihatools.com/collections/insulated-tool-sets>
- TE Connectivity lists commercial hand crimping tools and certified crimp tools for electrical terminals and connectors: <https://www.te.com/en/products/application-tooling/hand-crimping-tools.html>
- Molex lists hand tools, crimp tools, wire strippers/cutters, applicators, and support tooling for connector assembly: <https://www.molex.com/en-us/products/tools>

## Commercial alternatives

- Insulated electrician tool kit.
- Electronics assembly hand-tool kit.
- Connector-specific hand crimp tool set.
- Pneumatic or battery-powered crimping tools for higher throughput.
- Separate soldering station and test instruments for solder/test operations.

## Build or open-source references

Basic pliers, cutters, stripper bodies, screwdriver shafts, and crimper frames can be locally machined/forged and heat treated. Reliable insulated tools need safe dielectric handle materials, controlled insulation coverage, and testing. Reliable crimps need precise die geometry and connector-specific validation.

The current KB recipe is plausible for a coarse local tool kit, but connector-grade crimping should still use dedicated dies/tools where process quality matters.

## Related machine research

Related local reports:

- `research/machines/hand_tools_mechanical.md`
- `research/machines/hand_tools_basic.md`
- `research/machines/wire_crimping_tools.md`
- `research/machines/soldering_station.md`
- `research/machines/multimeter_set.md`

## Recommendation for KB realism

Keep as an electrical hand-tool kit.

Recommended options:

- Treat as reusable hand tooling, not as a machine.
- Keep separate from `hand_tools_mechanical` where insulation, wire stripping, and electrical safety matter.
- Do not use as a substitute for `wire_crimping_tools` or `crimping_tool_set` where connector-specific crimp quality matters.
- Do not use as a substitute for `soldering_station`, `multimeter_set`, or `test_bench_electrical`.
- Consider consolidation into `hand_tools_basic` for coarse assembly processes under Conservative Mode.

## Confidence and open questions

Confidence: high that the item is real and useful; high that it is a tool kit rather than a machine; medium on how much overlap should remain with crimping-specific tool items.

Open questions:

- Should cable harness assembly require both `hand_tools_electrical` and `crimping_tool_set`, or is that redundant?
- Are insulated tools required because processes involve live circuits, or only general electrical assembly?
- Should electrical hand tools include multimeter probes without including the multimeter itself?
