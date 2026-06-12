# Welding Consumables

## Machine identity

- KB ID: `welding_consumables`
- KB name: Welding Consumables and Filler Material Set
- KB file: `kb/items/machines/welding_consumables.yaml`
- Current KB type: `machine`
- Current KB mass: 25 kg
- Current KB description: welding rods, filler wire, and consumable materials for welding operations.
- Current KB BOM: steel welding rods, aluminum wire used as filler-wire placeholder, and storage enclosure.

## KB usage and needed function

The KB uses `welding_consumables` as a BOM/recipe input for fabrication tasks such as `recipe_machine_chemical_mixer_tank_import_v0`, `recipe_pressure_vessel_steel_v0`, and `recipe_structural_steel_frame_v0`. It is also related to `welding_tig_unit_v0`, `welding_tools_set`, and general welding processes.

The needed function is consumable filler and process material supply: stick electrodes, MIG wire, TIG rods, flux-cored wire, filler rods, tungsten electrodes, flux, and possibly shielding gas depending on process.

## Reality classification

Classification: real consumable material set, not a machine.

Welding consumables are standard industrial supplies. A 25 kg inventory is plausible as a small starter stock. However, it should not be modeled as a machine. It should be a consumable item/material kit consumed by welding recipes, possibly with storage requirements for low-hydrogen electrodes and fluxes.

## Evidence links

- ESAB sells filler metals including electrodes, wires, rods, fluxes, and powders for many welding processes and materials. Source: https://esab.com/us/nam_en/products-solutions/categories/filler-metals/
- Lincoln Electric lists filler metals, electrodes, and wire for welding processes. Source: https://www.lincolnelectric.com/en/Products/Filler-Metals
- Hobart Brothers explains AWS filler-metal and stick-electrode classifications and distinguishes welding rods, solid wires, and electrodes. Source: https://www.hobartbrothers.com/resources/technical-articles/electrode-classification/
- AWS publishes filler metal specifications by material and welding process, including aluminum, nickel, copper, titanium, tungsten electrodes, brazing alloys, shielding gases, and fluxes. Source: https://pubs.aws.org/t/fillermetalspecifications
- ESAB describes proper storage/redrying of stick electrodes, including moisture-proof containers and holding ovens for some electrode types. Source: https://esab.com/us/nam_en/esab-university/blogs/storing-and-redrying-stick-electrodes-the-right-way/
- WeldingMart notes that TIG filler rods are filler metals used during welding and are distinct from tungsten electrodes carrying the arc. Source: https://weldingmart.com/collections/tig-rod-welding-rods

## Commercial alternatives

- Stick welding electrode inventory.
- MIG wire spools.
- TIG filler rod set.
- Flux-cored wire.
- Tungsten electrode set.
- Brazing rods and flux.
- Shielding gas cylinders or local gas supply.
- Rod oven or sealed dry storage for low-hydrogen electrodes.

## Build or open-source references

Some consumables are locally manufacturable if wire drawing, alloy control, flux formulation, coating/extrusion, drying, and packaging exist:

- TIG filler rods can be straightened/drawn alloy wire or rod.
- MIG wire needs continuous controlled-diameter wire, surface finish, spooling, and feed reliability.
- Stick electrodes require core wire, flux coating, extrusion/dipping, drying, and moisture-controlled storage.
- Flux-cored wire requires tube forming and flux filling.
- Tungsten electrodes require refractory-metal supply and grinding.

For self-reproduction, the base alloy match matters. Using generic steel rods or aluminum wire as a placeholder can be unrealistic for stainless, pressure vessels, dissimilar metals, aluminum welding, and high-strength steels.

## Related machine research

Related reports already present:

- `welding_tools_set.md`
- `welding_tig_unit_v0.md`
- `electrodes.md`
- `cutting_tools_general.md`

`welding_tools_set` is PPE/accessory tooling. `welding_consumables` is consumed material. `welding_tig_unit_v0` or `welding_arc_welder_v0` provides the welding process capability.

## Recommendation for KB realism

Keep the concept, but reclassify as consumable material inventory rather than a machine.

Recommended future cleanup:

- Split by process/material where needed: steel stick electrodes, TIG filler rods, MIG wire, aluminum filler wire, stainless filler, tungsten electrodes, flux, shielding gas.
- Treat mass as consumed by welding recipes.
- Add storage constraints for low-hydrogen electrodes or flux where weld quality matters.
- Do not list this as an imported machine in realism summaries.

The current BOM is acceptable as a coarse placeholder, but aluminum wire should not be a generic filler substitute except where aluminum filler is actually compatible.

## Confidence and open questions

Confidence: high that welding consumables are real; high that the item is misclassified as a machine; medium on the best split by welding process.

Open questions:

- Should shielding gas be part of this inventory or separate resource/material?
- Which welding processes are the KB assuming for structural steel, pressure vessels, aluminum, and TIG tube work?
- Should weld recipes consume filler by weld length or deposited mass?
