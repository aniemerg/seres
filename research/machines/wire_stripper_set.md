# Wire Stripper Set

## Machine identity

- KB ID: `wire_stripper_set`
- KB name: Wire stripper set
- KB file: `kb/items/machines/wire_stripper_set.yaml`
- Current KB type: `machine`
- Current KB mass: 1.5 kg
- Current KB description: manual wire strippers, automatic wire strippers, cable strippers, and utility knife for removing insulation without damaging conductors.

## KB usage and needed function

The KB uses `wire_stripper_set` for:

- `wire_cutting_and_stripping_v0`
- `cable_harness_assembly_v0`
- `power_cable_assembly_v0`
- `crimping_and_termination_v0`

The needed function is preparation of electrical conductors for termination, soldering, crimping, and harness assembly by removing insulation to a controlled strip length without nicking or cutting conductor strands.

## Reality classification

Classification: real practical hand-tool set, not a standalone machine.

Wire strippers are common electrical and electronics assembly tools. The 1.5 kg mass is plausible for a set of manual strippers, automatic strippers, cable strippers, spare blades, and a utility knife. The item is better modeled as an electrical tool kit than a machine.

## Evidence links

- Klein Tools describes a Katapult wire stripper/cutter for 8-20 AWG solid and 10-22 AWG stranded wire, with precision-ground stripping holes for insulation removal. Source: https://www.homedepot.com/p/Klein-Tools-Katapult-Wire-Stripper-and-Cutter-for-8-20-AWG-Solid-and-10-22-AWG-Stranded-Wire-11063W/204660476
- KNIPEX lists automatic wire strippers for standard insulation, rubber cables, flat cables, and different cross-sections. Source: https://www.knipex.com/products/wire-strippers-and-stripping-tools
- Molex lists application tooling including hand tools for low-volume connector work and a hand wire-stripping tool for 34-8 AWG wire. Sources: https://www.molex.com/en-us/products/application-tooling and https://www.molex.com/en-us/products/part-detail/638170000
- Electrical Contractor Magazine describes wire strippers as tools for removing insulation from conductors, with automatic tools useful where speed, consistency, and strip-length accuracy matter. Source: https://www.ecmag.com/magazine/articles/article-detail/wire-strippers-tools-to-remove-insulation-from-conductors
- Eraser Company sells automatic wire and cable strippers, including rotary wire strippers with adjustable blade depth and strip length for consistent stripping. Source: https://www.eraser.com/products/wire-cable-strippers/
- Klein Tools sells large cable strippers designed to remove insulation without nicking large MTW/THHN/THWN-2 conductors. Source: https://www.kleintools.com/catalog/cable-and-wire-stripping-tools/large-cable-stripper-20-250-mcm

## Commercial alternatives

- Gauged manual wire stripper/cutter.
- Self-adjusting automatic hand stripper.
- Cable jacket stripper.
- Precision small-wire stripper for electronics.
- Electric bench wire stripping machine.
- Connector-specific strip/crimp tools.
- Full electrical hand-tool kit including cutters, crimpers, screwdrivers, probes, and strippers.

## Build or open-source references

Simple wire strippers are locally manufacturable:

- Hardened steel jaws/blades with gauge notches or adjustable stops.
- Pivot, spring, and handles.
- Insulated grips.
- Strip-length stop for repeatability.

Automatic self-adjusting strippers and high-volume electric stripping machines are harder but still conventional. The KB recipe, which machines jaws/blades, heat treats them, and assembles insulated handles and springs, is plausible for a manual set.

## Related machine research

Related reports already present:

- `wire_crimping_tools.md`
- `hand_tools_electrical.md`
- `assembly_tools_basic.md`
- `measurement_equipment.md`

Wire strippers should remain separate from crimping tools where connector quality matters, but they may be bundled into `hand_tools_electrical` for coarse process modeling.

## Recommendation for KB realism

Keep as a real tool set, but reclassify as electrical hand tooling rather than a machine.

Recommended future cleanup:

- Keep separate if wire/cable preparation is modeled explicitly.
- Otherwise fold into `hand_tools_electrical`.
- Use powered stripping machines only if high-volume harness production or scrap-wire processing is modeled.

The current mass, BOM direction, and recipe are realistic for a manual tool set.

## Confidence and open questions

Confidence: high.

Open questions:

- Should the KB model strip-length accuracy and conductor damage for critical harnesses?
- Should large power-cable strippers be separate from small electronics wire strippers?
- Should wire strippers and crimp tools be bundled into one harness assembly kit?
