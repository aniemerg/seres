# Plastic extruder

## Machine identity

- Queue item: `machine_reality_plastic_extruder`
- KB ID: `plastic_extruder`
- KB file: `kb/items/machines/plastic_extruder.yaml`
- KB name: Plastic extruder
- KB kind: `machine`
- KB modeled mass: 250 kg

In the KB, this is a small screw plastic extruder for filament, profile, or sheet production. The item notes identify the expected subassemblies: heated barrel, screw, drive motor, die, and frame. Its BOM also includes an extruder head, induction heater/heating plate, motor, gearbox, welded steel frame, and fasteners.

## KB usage and needed function

`plastic_extruder` is used as a machine requirement by several processes:

- `plastic_extrusion_v0`
- `plastic_sheet_extrusion_v0`
- `metal_plastic_filament_extrusion_v0`
- `gasket_sheet_material_extrusion_v0`
- `projection_screen_sheet_casting_v0`

The required KB function is continuous heating, melting, conveying, and forcing thermoplastic pellets or filled plastic material through a die to make profiles, sheets, gasket stock, filament-like forms, or similar extruded plastic products.

## Reality classification

Classification: real practical machine, modeled as a generic small single-screw plastic extruder.

The KB item is not a placeholder. Commercial extruders and open-source/community-built plastic extruders both exist. The exact KB ID is generic, but the modeled components match the normal physical architecture of a single-screw plastic extruder: feed hopper, heated barrel, screw, motor/drive, gearbox, die/head, heating/cooling, controls, and instrumentation.

The KB mass of 250 kg is plausible for a small shop or lab-scale machine, although it is heavier than desktop filament extruders and lighter than many industrial extrusion lines. That mass is acceptable if the KB intends a robust small production machine rather than a benchtop filament-only unit.

## Evidence links

- SpecialChem overview of extrusion equipment: https://www.specialchem.com/plastics/guide/an-in-depth-look-at-extrusion
  - Identifies extruders as machines with motor, barrel, drive system, screw, gearbox, die, heating/cooling, feed system, filtration, and instrumentation.
  - Describes screw-driven movement of plastic pellets through a heated barrel and die.

- Bausano single-screw extruders: https://www.bausano.com/en/extruders-range/single-screw-extruders
  - Commercial manufacturer page for single-screw plastic extrusion lines.
  - Describes use for PVC, PE, PP and other thermoplastics in profiles, pipes, gaskets, and recycled or filled materials.
  - Lists major machine elements including screw/barrel, heating, motor, gearbox, feeder, controls, head, and cooling.

- Dynisco technical PDF, "The Screw and Barrel System": https://www.dynisco.com/userfiles/files/The_Screw_and_Barrel_System.pdf
  - Explains that single-screw extruders use screw/barrel interaction to convey, melt, and generate pressure in plastic material.
  - Describes the steel helical screw rotating inside the barrel and moving material from hopper to die.

- Precious Plastic extrusion machine guide: https://www.onearmy.earth/news/extrusion-machine
  - Documents an open-source plastic extrusion machine used for recycled plastic beams, bricks, and other products.
  - Describes heating plastic, transporting it with a motor-powered screw, pressing it through a nozzle or into a mold, and continuous operation.

## Commercial alternatives

- Industrial/small production single-screw extruder lines, e.g. Bausano E-GO, are available for pipe and profile production.
- Filament-focused commercial units also exist at smaller scale. Examples include Filabot EX-series machines and Felfil Evo-style desktop filament extruders. These are useful alternates if the KB only needs 3D-printer filament, but they are too narrow for general profile/sheet/gasket extrusion.
- Used extrusion equipment marketplaces commonly list single-screw extruders with heated barrels, gearboxes, motor drives, and screw diameters, which supports the practicality of buying such machinery rather than treating it as speculative.

## Build or open-source references

- Precious Plastic provides open-source/community documentation for extrusion machines, including build kits and workspace setup material. This supports a "can be built locally from general fabrication plus purchased/imported control and drive components" interpretation.
- OHO wiki mirrors Precious Plastic extrusion machine assets and mentions drawings, bill of materials, CAD files, and related downloads: https://en.oho.wiki/wiki/Plastic_extrusion_machine%2C_Precious_Plastic

Open-source builds are most relevant for recycled-plastic beams, bricks, and simple profiles. Precision sheet extrusion or tight-tolerance filament requires better controls, pullers, cooling, diameter measurement, and winding equipment, so the KB should not assume a bare extruder alone covers the entire downstream line.

## Related machine research

No existing `research/machines` report was found for plastic extrusion, polymer extrusion, or a related plastic machine at the time of this task. Related future comparisons, if already queued, would be `molding_press`, `pellet_press`, `mixer_or_blender`, and `cutting_tools_general`, because those may share polymer-processing or shop-tool boundary decisions.

## Recommendation for KB realism

Keep `plastic_extruder` as a real machine, but consider clarifying the item name or notes to "small single-screw plastic extruder" if future KB edits are allowed. The current ID is acceptable as a generic capacity provider.

Recommended interpretation:

- Keep as a machine, not a part or placeholder.
- Treat as a generic small single-screw extruder suitable for profiles, simple sheet/gasket stock, and coarse filament/profile output.
- Do not split unless the KB needs to distinguish desktop filament extrusion, industrial pipe/profile extrusion, sheet line extrusion, and recycled-plastic beam extrusion.
- For realistic process modeling, add or preserve separate downstream equipment where needed: cooling bath or table, haul-off/puller, cutter, winder, sheet calendar/roll stack, or diameter/thickness measurement. The extruder alone does not provide every capability of a full extrusion line.
- The BOM concept is realistic, but `extruder_head_basic`, screw/barrel, heaters, motor/gearbox, and controls are critical components; the KB should avoid collapsing these into vague "plastic extruder" mass if later manufacturing closure work needs detail.

## Confidence and open questions

Confidence: high.

Open questions:

- Is the KB intended to represent a general shop extruder or a filament-specific extruder? Current usage suggests general shop extrusion, not filament only.
- Are the throughput and energy assumptions in `plastic_extrusion_v0` intended for a 250 kg machine? They look plausible for a small production extruder, but not for a small desktop filament extruder.
- Some process names imply sheet or screen casting. Those may need downstream sheet-forming/cooling equipment in addition to the extruder if high realism is required.

